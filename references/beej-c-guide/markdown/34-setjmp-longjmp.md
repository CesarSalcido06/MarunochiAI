[Prev](arrays-part-ii.html) | [Contents](index.html) | [Next](incomplete-types.html)

* * *

# 34 Long Jumps with `setjmp`, `longjmp`

We’ve already seen `goto`, which jumps in function scope. But `longjmp()` allows you to jump back to an earlier point in execution, back to a function that called this one.

There are a lot of limitations and caveats, but this can be a useful function for bailing out from deep in the call stack back up to an earlier state.

In my experience, this is very rarely-used functionality.

## 34.1 Using `setjmp` and `longjmp`

The dance we’re going to do here is to basically put a bookmark in execution with `setjmp()`. Later on, we’ll call `longjmp()` and it’ll jump back to the earlier point in execution where we set the bookmark with `setjmp()`.

And it can do this even if you’ve called subfunctions.

Here’s a quick demo where we call into functions a couple levels deep and then bail out of it.

We’re going to use a file scope variable `env` to keep the _state_ of things when we call `setjmp()` so we can restore them when we call `longjmp()` later. This is the variable in which we remember our “place”.

The variable `env` is of type `jmp_buf`, an opaque type declared in `<setjmp.h>`.
    
    
    [](setjmp-longjmp.html#cb675-1)#include <stdio.h>
    [](setjmp-longjmp.html#cb675-2)#include <setjmp.h>
    [](setjmp-longjmp.html#cb675-3)
    [](setjmp-longjmp.html#cb675-4)jmp_buf env;
    [](setjmp-longjmp.html#cb675-5)
    [](setjmp-longjmp.html#cb675-6)void depth2(void)
    [](setjmp-longjmp.html#cb675-7){
    [](setjmp-longjmp.html#cb675-8)    printf("Entering depth 2\n");
    [](setjmp-longjmp.html#cb675-9)    longjmp(env, 3490);           // Bail out
    [](setjmp-longjmp.html#cb675-10)    printf("Leaving depth 2\n");  // This won't happen
    [](setjmp-longjmp.html#cb675-11)}
    [](setjmp-longjmp.html#cb675-12)
    [](setjmp-longjmp.html#cb675-13)void depth1(void)
    [](setjmp-longjmp.html#cb675-14){
    [](setjmp-longjmp.html#cb675-15)    printf("Entering depth 1\n");
    [](setjmp-longjmp.html#cb675-16)    depth2();
    [](setjmp-longjmp.html#cb675-17)    printf("Leaving depth 1\n");  // This won't happen
    [](setjmp-longjmp.html#cb675-18)}
    [](setjmp-longjmp.html#cb675-19)
    [](setjmp-longjmp.html#cb675-20)int main(void)
    [](setjmp-longjmp.html#cb675-21){
    [](setjmp-longjmp.html#cb675-22)    switch (setjmp(env)) {
    [](setjmp-longjmp.html#cb675-23)      case 0:
    [](setjmp-longjmp.html#cb675-24)          printf("Calling into functions, setjmp() returned 0\n");
    [](setjmp-longjmp.html#cb675-25)          depth1();
    [](setjmp-longjmp.html#cb675-26)          printf("Returned from functions\n");  // This won't happen
    [](setjmp-longjmp.html#cb675-27)          break;
    [](setjmp-longjmp.html#cb675-28)
    [](setjmp-longjmp.html#cb675-29)      case 3490:
    [](setjmp-longjmp.html#cb675-30)          printf("Bailed back to main, setjmp() returned 3490\n");
    [](setjmp-longjmp.html#cb675-31)          break;
    [](setjmp-longjmp.html#cb675-32)    }
    [](setjmp-longjmp.html#cb675-33)}

When run, this outputs:
    
    
    [](setjmp-longjmp.html#cb676-1)Calling into functions, setjmp() returned 0
    [](setjmp-longjmp.html#cb676-2)Entering depth 1
    [](setjmp-longjmp.html#cb676-3)Entering depth 2
    [](setjmp-longjmp.html#cb676-4)Bailed back to main, setjmp() returned 3490

If you try to take that output and match it up with the code, it’s clear there’s some really _funky_ stuff going on.

One of the most notable things is that `setjmp()` returns _twice_. What the actual frank? What is this sorcery?!

So here’s the deal: if `setjmp()` returns `0`, it means that you’ve successfully set the “bookmark” at that point.

If it returns non-zero, it means you’ve just returned to the “bookmark” set earlier. (And the value returned is the one you pass to `longjmp()`.)

This way you can tell the difference between setting the bookmark and returning to it later.

So when the code, above, calls `setjmp()` the first time, `setjmp()` _stores_ the state in the `env` variable and returns `0`. Later when we call `longjmp()` with that same `env`, it restores the state and `setjmp()` returns the value `longjmp()` was passed.

## 34.2 Pitfalls

Under the hood, this is pretty straightforward. Typically the _stack pointer_ keeps track of the locations in memory that local variables are stored, and the _program counter_ keeps track of the address of the currently-executing instruction[181](function-specifiers-alignment-specifiersoperators.html#fn181).

So if we want to jump back to an earlier function, it’s basically only a matter of restoring the stack pointer and program counter to the values kept in the `jmp_buf` variable, and making sure the return value is set correctly. And then execution will resume there.

But a variety of factors confound this, making a significant number of undefined behavior traps.

### 34.2.1 The Values of Local Variables

If you want the values of automatic (non-`static` and non-`extern`) local variables to persist in the function that called `setjmp()` after a `longjmp()` happens, you must declare those variables to be `volatile`.

Technically, they only have to be `volatile` if they change between the time `setjmp()` is called and `longjmp()` is called[182](function-specifiers-alignment-specifiersoperators.html#fn182).

For example, if we run this code:
    
    
    [](setjmp-longjmp.html#cb677-1)int x = 20;
    [](setjmp-longjmp.html#cb677-2)
    [](setjmp-longjmp.html#cb677-3)if (setjmp(env) == 0) {
    [](setjmp-longjmp.html#cb677-4)    x = 30;
    [](setjmp-longjmp.html#cb677-5)}

and then later `longjmp()` back, the value of `x` will be indeterminate.

If we want to fix this, `x` must be `volatile`:
    
    
    [](setjmp-longjmp.html#cb678-1)volatile int x = 20;
    [](setjmp-longjmp.html#cb678-2)
    [](setjmp-longjmp.html#cb678-3)if (setjmp(env) == 0) {
    [](setjmp-longjmp.html#cb678-4)    x = 30;
    [](setjmp-longjmp.html#cb678-5)}

Now the value will be the correct `30` after a `longjmp()` returns us to this point.

### 34.2.2 How Much State is Saved?

When you `longjmp()`, execution resumes at the point of the corresponding `setjmp()`. And that’s it.

The spec points out that it’s just as if you’d jumped back into the function at that point with local variables set to whatever values they had when the `longjmp()` call was made.

Things that aren’t restored include, paraphrasing the spec:

  * Floating point status flags
  * Open files
  * Any other component of the abstract machine



### 34.2.3 You Can’t Name Anything `setjmp`

You can’t have any `extern` identifiers with the name `setjmp`. Or, if `setjmp` is a macro, you can’t undefine it.

Both are undefined behavior.

### 34.2.4 You Can’t `setjmp()` in a Larger Expression

That is, you can’t do something like this:
    
    
    [](setjmp-longjmp.html#cb679-1)if (x == 12 && setjmp(env) == 0) { ... }

That’s too complex to be allowed by the spec due to the machinations that must occur when unrolling the stack and all that. We can’t `longjmp()` back into some complex expression that’s only been partially executed.

So there are limits on the complexity of that expression.

  * It can be the entire controlling expression of the conditional.
        
        [](setjmp-longjmp.html#cb680-1)if (setjmp(env)) {...}
        
        [](setjmp-longjmp.html#cb681-1)switch (setjmp(env)) {...}

  * It can be part of a relational or equality expression, as long as the other operand is an integer constant. And the whole thing is the controlling expression of the conditional.
        
        [](setjmp-longjmp.html#cb682-1)if (setjmp(env) == 0) {...}

  * The operand to a logical NOT (`!`) operation, being the entire controlling expression.
        
        [](setjmp-longjmp.html#cb683-1)if (!setjmp(env)) {...}

  * A standalone expression, possibly cast to `void`.
        
        [](setjmp-longjmp.html#cb684-1)setjmp(env);
        
        [](setjmp-longjmp.html#cb685-1)(void)setjmp(env);




### 34.2.5 When Can’t You `longjmp()`?

It’s undefined behavior if:

  * You didn’t call `setjmp()` earlier
  * You called `setjmp()` from another thread
  * You called `setjmp()` in the scope of a variable length array (VLA), and execution left the scope of that VLA before `longjmp()` was called.
  * The function containing the `setjmp()` exited before `longjmp()` was called.



On that last one, “exited” includes normal returns from the function, as well as the case if another `longjmp()` jumped back to “earlier” in the call stack than the function in question.

### 34.2.6 You Can’t Pass `0` to `longjmp()`

If you try to pass the value `0` to `longjmp()`, it will silently change that value to `1`.

Since `setjmp()` ultimately returns this value, and having `setjmp()` return `0` has special meaning, returning `0` is prohibited.

### 34.2.7 `longjmp()` and Variable Length Arrays

If you are in scope of a VLA and `longjmp()` out there, the memory allocated to the VLA could leak[183](function-specifiers-alignment-specifiersoperators.html#fn183).

Same thing happens if you `longjmp()` back over any earlier functions that had VLAs still in scope.

This is one thing that really bugged me about VLAs—that you could write perfectly legitimate C code that squandered memory. But, hey—I’m not in charge of the spec.

* * *

[Prev](arrays-part-ii.html) | [Contents](index.html) | [Next](incomplete-types.html)
