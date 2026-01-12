[Prev](variable-length-arrays-vlas.html) | [Contents](index.html) | [Next](types-part-v-compound-literals-and-generic-selections.html)

* * *

# 31 `goto`

The `goto` statement is universally revered and can be here presented without contest.

Just kidding! Over the years, there has been a lot of back-and-forth over whether or not (often not) `goto` is [considered harmful](https://en.wikipedia.org/wiki/Goto#Criticism)[176](function-specifiers-alignment-specifiersoperators.html#fn176).

In this programmer’s opinion, you should use whichever constructs leads to the _best_ code, factoring in maintainability and speed. And sometimes this might be `goto`!

In this chapter, we’ll see how `goto` works in C, and then check out some of the common cases where it is used[177](function-specifiers-alignment-specifiersoperators.html#fn177).

## 31.1 A Simple Example

In this example, we’re going to use `goto` to skip a line of code and jump to a _label_. The label is the identifier that can be a `goto` target—it ends with a colon (`:`).
    
    
    [](goto.html#cb609-1)#include <stdio.h>
    [](goto.html#cb609-2)
    [](goto.html#cb609-3)int main(void)
    [](goto.html#cb609-4){
    [](goto.html#cb609-5)    printf("One\n");
    [](goto.html#cb609-6)    printf("Two\n");
    [](goto.html#cb609-7)
    [](goto.html#cb609-8)    goto skip_3;
    [](goto.html#cb609-9)
    [](goto.html#cb609-10)    printf("Three\n");
    [](goto.html#cb609-11)
    [](goto.html#cb609-12)skip_3:
    [](goto.html#cb609-13)
    [](goto.html#cb609-14)    printf("Five!\n");
    [](goto.html#cb609-15)}

The output is:
    
    
    [](goto.html#cb610-1)One
    [](goto.html#cb610-2)Two
    [](goto.html#cb610-3)Five!

`goto` sends execution jumping to the specified label, skipping everything in between.

You can jump forward or backward with `goto`.
    
    
    [](goto.html#cb611-1)infinite_loop:
    [](goto.html#cb611-2)    print("Hello, world!\n");
    [](goto.html#cb611-3)    goto infinite_loop;

Labels are skipped over during execution. The following will print all three numbers in order just as if the labels weren’t there:
    
    
    [](goto.html#cb612-1)    printf("Zero\n");
    [](goto.html#cb612-2)label_1:
    [](goto.html#cb612-3)label_2:
    [](goto.html#cb612-4)    printf("One\n");
    [](goto.html#cb612-5)label_3:
    [](goto.html#cb612-6)    printf("Two\n");
    [](goto.html#cb612-7)label_4:
    [](goto.html#cb612-8)    printf("Three\n");

As you’ve noticed, it’s common convention to justify the labels all the way on the left. This increases readability because a reader can quickly scan to find the destination.

Labels have _function scope_. That is, no matter how many levels deep in blocks they appear, you can still `goto` them from anywhere in the function.

It also means you can only `goto` labels that are in the same function as the `goto` itself. Labels in other functions are out of scope from `goto`’s perspective. And it means you can use the same label name in two functions—just not the same label name in the same function.

## 31.2 Labeled `continue`

In some languages, you can actually specify a label for a `continue` statement. C doesn’t allow it, but you can easily use `goto` instead.

To show the issue, check out `continue` in this nested loop:
    
    
    [](goto.html#cb613-1)for (int i = 0; i < 3; i++) {
    [](goto.html#cb613-2)    for (int j = 0; j < 3; j++) {
    [](goto.html#cb613-3)        printf("%d, %d\n", i, j);
    [](goto.html#cb613-4)        continue;   // Always goes to next j
    [](goto.html#cb613-5)    }
    [](goto.html#cb613-6)}

As we see, that `continue`, like all `continues`, goes to the next iteration of the nearest enclosing loop. What if we want to `continue` in the next loop out, the loop with `i`?

Well, we can `break` to get back to the outer loop, right?
    
    
    [](goto.html#cb614-1)for (int i = 0; i < 3; i++) {
    [](goto.html#cb614-2)    for (int j = 0; j < 3; j++) {
    [](goto.html#cb614-3)        printf("%d, %d\n", i, j);
    [](goto.html#cb614-4)        break;     // Gets us to the next iteration of i
    [](goto.html#cb614-5)    }
    [](goto.html#cb614-6)}

That gets us two levels of nested loop. But then if we nest another loop, we’re out of options. What about this, where we don’t have any statement that will get us out to the next iteration of `i`?
    
    
    [](goto.html#cb615-1)for (int i = 0; i < 3; i++) {
    [](goto.html#cb615-2)    for (int j = 0; j < 3; j++) {
    [](goto.html#cb615-3)        for (int k = 0; k < 3; k++) {
    [](goto.html#cb615-4)            printf("%d, %d, %d\n", i, j, k);
    [](goto.html#cb615-5)
    [](goto.html#cb615-6)            continue;  // Gets us to the next iteration of k
    [](goto.html#cb615-7)            break;     // Gets us to the next iteration of j
    [](goto.html#cb615-8)            ????;      // Gets us to the next iteration of i???
    [](goto.html#cb615-9)
    [](goto.html#cb615-10)        }
    [](goto.html#cb615-11)    }
    [](goto.html#cb615-12)}

The `goto` statement offers us a way!
    
    
    [](goto.html#cb616-1)    for (int i = 0; i < 3; i++) {
    [](goto.html#cb616-2)        for (int j = 0; j < 3; j++) {
    [](goto.html#cb616-3)            for (int k = 0; k < 3; k++) {
    [](goto.html#cb616-4)                printf("%d, %d, %d\n", i, j, k);
    [](goto.html#cb616-5)
    [](goto.html#cb616-6)                goto continue_i;   // Now continuing the i loop!!
    [](goto.html#cb616-7)            }
    [](goto.html#cb616-8)        }
    [](goto.html#cb616-9)continue_i: ;
    [](goto.html#cb616-10)    }

We have a `;` at the end there—that’s because you can’t have a label pointing to the plain end of a compound statement (or before a variable declaration).

## 31.3 Bailing Out

When you’re super nested in the middle of some code, you can use `goto` to get out of it in a manner that’s often cleaner than nesting more `if`s and using flag variables.
    
    
    [](goto.html#cb617-1)    // Pseudocode
    [](goto.html#cb617-2)
    [](goto.html#cb617-3)    for(...) {
    [](goto.html#cb617-4)        for (...) {
    [](goto.html#cb617-5)            while (...) {
    [](goto.html#cb617-6)                do {
    [](goto.html#cb617-7)                    if (some_error_condition)
    [](goto.html#cb617-8)                        goto bail;
    [](goto.html#cb617-9)
    [](goto.html#cb617-10)                } while(...);
    [](goto.html#cb617-11)            }
    [](goto.html#cb617-12)        }
    [](goto.html#cb617-13)    }
    [](goto.html#cb617-14)
    [](goto.html#cb617-15)bail:
    [](goto.html#cb617-16)    // Cleanup here

Without `goto`, you’d have to check an error condition flag in all of the loops to get all the way out.

## 31.4 Labeled `break`

This is a very similar situation to how `continue` only continues the innermost loop. `break` also only breaks out of the innermost loop.
    
    
    [](goto.html#cb618-1)    for (int i = 0; i < 3; i++) {
    [](goto.html#cb618-2)        for (int j = 0; j < 3; j++) {
    [](goto.html#cb618-3)            printf("%d, %d\n", i, j);
    [](goto.html#cb618-4)            break;   // Only breaks out of the j loop
    [](goto.html#cb618-5)        }
    [](goto.html#cb618-6)    }
    [](goto.html#cb618-7)
    [](goto.html#cb618-8)    printf("Done!\n");

But we can use `goto` to break farther:
    
    
    [](goto.html#cb619-1)    for (int i = 0; i < 3; i++) {
    [](goto.html#cb619-2)        for (int j = 0; j < 3; j++) {
    [](goto.html#cb619-3)            printf("%d, %d\n", i, j);
    [](goto.html#cb619-4)            goto break_i;   // Now breaking out of the i loop!
    [](goto.html#cb619-5)        }
    [](goto.html#cb619-6)    }
    [](goto.html#cb619-7)
    [](goto.html#cb619-8)break_i:
    [](goto.html#cb619-9)
    [](goto.html#cb619-10)    printf("Done!\n");

## 31.5 Multi-level Cleanup

If you’re calling multiple functions to initialize multiple systems and one of them fails, you should only de-initialize the ones that you’ve gotten to so far.

Let’s do a fake example where we start initializing systems and checking to see if any returns an error (we’ll use `-1` to indicate an error). If one of them does, we have to shutdown only the systems we’ve initialized so far.
    
    
    [](goto.html#cb620-1)    if (init_system_1() == -1)
    [](goto.html#cb620-2)        goto shutdown;
    [](goto.html#cb620-3)
    [](goto.html#cb620-4)    if (init_system_2() == -1)
    [](goto.html#cb620-5)        goto shutdown_1;
    [](goto.html#cb620-6)
    [](goto.html#cb620-7)    if (init_system_3() == -1)
    [](goto.html#cb620-8)        goto shutdown_2;
    [](goto.html#cb620-9)
    [](goto.html#cb620-10)    if (init_system_4() == -1)
    [](goto.html#cb620-11)        goto shutdown_3;
    [](goto.html#cb620-12)
    [](goto.html#cb620-13)    do_main_thing();   // Run our program
    [](goto.html#cb620-14)
    [](goto.html#cb620-15)    shutdown_system4();
    [](goto.html#cb620-16)
    [](goto.html#cb620-17)shutdown_3:
    [](goto.html#cb620-18)    shutdown_system3();
    [](goto.html#cb620-19)
    [](goto.html#cb620-20)shutdown_2:
    [](goto.html#cb620-21)    shutdown_system2();
    [](goto.html#cb620-22)
    [](goto.html#cb620-23)shutdown_1:
    [](goto.html#cb620-24)    shutdown_system1();
    [](goto.html#cb620-25)
    [](goto.html#cb620-26)shutdown:
    [](goto.html#cb620-27)    print("All subsystems shut down.\n");

Note that we’re shutting down in the reverse order that we initialized the subsystems. So if subsystem 4 fails to start up, it will shut down 3, 2, then 1 in that order.

## 31.6 Tail Call Optimization

Kinda. For recursive functions only.

If you’re unfamiliar, [Tail Call Optimization (TCO)](https://en.wikipedia.org/wiki/Tail_call)[178](function-specifiers-alignment-specifiersoperators.html#fn178) is a way to not waste stack space when calling other functions under very specific circumstances. Unfortunately the details are beyond the scope of this guide.

But if you have a recursive function you know can be optimized in this way, you can make use of this technique. (Note that you can’t tail call other functions due to the function scope of labels.)

Let’s do a straightforward example, factorial.

Here’s a recursive version that’s not TCO, but it can be!
    
    
    [](goto.html#cb621-1)#include <stdio.h>
    [](goto.html#cb621-2)#include <complex.h>
    [](goto.html#cb621-3)
    [](goto.html#cb621-4)int factorial(int n, int a)
    [](goto.html#cb621-5){
    [](goto.html#cb621-6)    if (n == 0)
    [](goto.html#cb621-7)        return a;
    [](goto.html#cb621-8)
    [](goto.html#cb621-9)    return factorial(n - 1, a * n);
    [](goto.html#cb621-10)}
    [](goto.html#cb621-11)
    [](goto.html#cb621-12)int main(void)
    [](goto.html#cb621-13){
    [](goto.html#cb621-14)    for (int i = 0; i < 8; i++)
    [](goto.html#cb621-15)        printf("%d! == %ld\n", i, factorial(i, 1));
    [](goto.html#cb621-16)}

To make it happen, you can replace the call with two steps:

  1. Set the values of the parameters to what they’d be on the next call.
  2. `goto` a label on the first line of the function.



Let’s try it:
    
    
    [](goto.html#cb622-1)#include <stdio.h>
    [](goto.html#cb622-2)
    [](goto.html#cb622-3)int factorial(int n, int a)
    [](goto.html#cb622-4){
    [](goto.html#cb622-5)tco:  // add this
    [](goto.html#cb622-6)
    [](goto.html#cb622-7)    if (n == 0)
    [](goto.html#cb622-8)        return a;
    [](goto.html#cb622-9)
    [](goto.html#cb622-10)    // replace return by setting new parameter values and
    [](goto.html#cb622-11)    // goto-ing the beginning of the function
    [](goto.html#cb622-12)
    [](goto.html#cb622-13)    //return factorial(n - 1, a * n);
    [](goto.html#cb622-14)
    [](goto.html#cb622-15)    int next_n = n - 1;  // See how these match up with
    [](goto.html#cb622-16)    int next_a = a * n;  // the recursive arguments, above?
    [](goto.html#cb622-17)
    [](goto.html#cb622-18)    n = next_n;   // Set the parameters to the new values
    [](goto.html#cb622-19)    a = next_a;
    [](goto.html#cb622-20)
    [](goto.html#cb622-21)    goto tco;   // And repeat!
    [](goto.html#cb622-22)}
    [](goto.html#cb622-23)
    [](goto.html#cb622-24)int main(void)
    [](goto.html#cb622-25){
    [](goto.html#cb622-26)    for (int i = 0; i < 8; i++)
    [](goto.html#cb622-27)        printf("%d! == %d\n", i, factorial(i, 1));
    [](goto.html#cb622-28)}

I used temporary variables up there to set the next values of the parameters before jumping to the start of the function. See how they correspond to the recursive arguments that were in the recursive call?

Now, why use temp variables? I could have done this instead:
    
    
    [](goto.html#cb623-1)    a *= n;
    [](goto.html#cb623-2)    n -= 1;
    [](goto.html#cb623-3)
    [](goto.html#cb623-4)    goto tco;

and that actually works just fine. But if I carelessly reverse those two lines of code:
    
    
    [](goto.html#cb624-1)    n -= 1;  // BAD NEWS
    [](goto.html#cb624-2)    a *= n;

—now we’re in trouble. We modified `n` before using it to modify `a`. That’s Bad because that’s not how it works when you call recursively. Using the temporary variables avoids this problem even if you’re not looking out for it. And the compiler likely optimizes them out, anyway.

## 31.7 Restarting Interrupted System Calls

This is outside the spec, but commonly seen in Unix-like systems.

Certain long-lived system calls might return an error if they’re interrupted by a signal, and `errno` will be set to `EINTR` to indicate the syscall was doing fine; it was just interrupted.

In those cases, it’s really common for the programmer to want to restart the call and try it again.
    
    
    [](goto.html#cb625-1)retry:
    [](goto.html#cb625-2)    byte_count = read(0, buf, sizeof(buf) - 1);  // Unix read() syscall
    [](goto.html#cb625-3)
    [](goto.html#cb625-4)    if (byte_count == -1) {            // An error occurred...
    [](goto.html#cb625-5)        if (errno == EINTR) {          // But it was just interrupted
    [](goto.html#cb625-6)            printf("Restarting...\n");
    [](goto.html#cb625-7)            goto retry;
    [](goto.html#cb625-8)        }

Many Unix-likes have an `SA_RESTART` flag you can pass to `sigaction()` to request the OS automatically restart any slow syscalls instead of failing with `EINTR`.

Again, this is Unix-specific and is outside the C standard.

That said, it’s possible to use a similar technique any time any function should be restarted.

## 31.8 `goto` and Thread Preemption

This example is ripped directly from [_Operating Systems: Three Easy Pieces_](http://www.ostep.org/), another excellent book from like-minded authors who also feel that quality books should be free to download. Not that I’m opinionated, or anything.
    
    
    [](goto.html#cb626-1)retry:
    [](goto.html#cb626-2)
    [](goto.html#cb626-3)    pthread_mutex_lock(L1);
    [](goto.html#cb626-4)
    [](goto.html#cb626-5)    if (pthread_mutex_trylock(L2) != 0) {
    [](goto.html#cb626-6)        pthread_mutex_unlock(L1);
    [](goto.html#cb626-7)        goto retry;
    [](goto.html#cb626-8)    }
    [](goto.html#cb626-9)
    [](goto.html#cb626-10)    save_the_day();
    [](goto.html#cb626-11)
    [](goto.html#cb626-12)    pthread_mutex_unlock(L2);
    [](goto.html#cb626-13)    pthread_mutex_unlock(L1);

There the thread happily acquires the mutex `L1`, but then potentially fails to get the second resource guarded by mutex `L2` (if some other uncooperative thread holds it, say). If our thread can’t get the `L2` lock, it unlocks `L1` and then uses `goto` to cleanly retry.

We hope our heroic thread eventually manages to acquire both mutexes and save the day, all while avoiding evil deadlock.

## 31.9 `goto` and Variable Scope

We’ve already seen that labels have function scope, but weird things can happen if we jump past some variable initialization.

Look at this example where we jump from a place where the variable `x` is out of scope into the middle of its scope (in the block).
    
    
    [](goto.html#cb627-1)    goto label;
    [](goto.html#cb627-2)
    [](goto.html#cb627-3)    {
    [](goto.html#cb627-4)        int x = 12345;
    [](goto.html#cb627-5)
    [](goto.html#cb627-6)label:
    [](goto.html#cb627-7)        printf("%d\n", x);
    [](goto.html#cb627-8)    }

This will compile and run, but gives me a warning:
    
    
    [](goto.html#cb628-1)warning: ‘x’ is used uninitialized in this function

And then it prints out `0` when I run it (your mileage may vary).

Basically what has happened is that we jumped into `x`’s scope (so it was OK to reference it in the `printf()`) but we jumped over the line that actually initialized it to `12345`. So the value was indeterminate.

The fix is, of course, to get the initialization _after_ the label one way or another.
    
    
    [](goto.html#cb629-1)    goto label;
    [](goto.html#cb629-2)
    [](goto.html#cb629-3)    {
    [](goto.html#cb629-4)        int x;
    [](goto.html#cb629-5)
    [](goto.html#cb629-6)label:
    [](goto.html#cb629-7)        x = 12345;
    [](goto.html#cb629-8)        printf("%d\n", x);
    [](goto.html#cb629-9)    }

Let’s look at one more example.
    
    
    [](goto.html#cb630-1)    {
    [](goto.html#cb630-2)        int x = 10;
    [](goto.html#cb630-3)
    [](goto.html#cb630-4)label:
    [](goto.html#cb630-5)
    [](goto.html#cb630-6)        printf("%d\n", x);
    [](goto.html#cb630-7)    }
    [](goto.html#cb630-8)
    [](goto.html#cb630-9)    goto label;

What happens here?

The first time through the block, we’re good. `x` is `10` and that’s what prints.

But after the `goto`, we’re jumping into the scope of `x`, but past its initialization. Which means we can still print it, but the value is indeterminate (since it hasn’t been reinitialized).

On my machine, it prints `10` again (to infinity), but that’s just luck. It could print any value after the `goto` since `x` is uninitialized.

## 31.10 `goto` and Variable-Length Arrays

When it comes to VLAs and `goto`, there’s one rule: you can’t jump from outside the scope of a VLA into the scope of that VLA.

If I try to do this:
    
    
    [](goto.html#cb631-1)    int x = 10;
    [](goto.html#cb631-2)
    [](goto.html#cb631-3)    goto label;
    [](goto.html#cb631-4)
    [](goto.html#cb631-5)    {
    [](goto.html#cb631-6)        int v[x];
    [](goto.html#cb631-7)
    [](goto.html#cb631-8)label:
    [](goto.html#cb631-9)
    [](goto.html#cb631-10)        printf("Hi!\n");
    [](goto.html#cb631-11)    }

I get an error:
    
    
    [](goto.html#cb632-1)error: jump into scope of identifier with variably modified type

You can jump in ahead of the VLA declaration, like this:
    
    
    [](goto.html#cb633-1)    int x = 10;
    [](goto.html#cb633-2)
    [](goto.html#cb633-3)    goto label;
    [](goto.html#cb633-4)
    [](goto.html#cb633-5)    {
    [](goto.html#cb633-6)label:  ;
    [](goto.html#cb633-7)        int v[x];
    [](goto.html#cb633-8)
    [](goto.html#cb633-9)        printf("Hi!\n");
    [](goto.html#cb633-10)    }

Because that way the VLA gets allocated properly before its inevitable deallocation once it falls out of scope.

* * *

[Prev](variable-length-arrays-vlas.html) | [Contents](index.html) | [Next](types-part-v-compound-literals-and-generic-selections.html)
