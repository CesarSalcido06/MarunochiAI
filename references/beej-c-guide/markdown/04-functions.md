[Prev](variables-and-statements.html) | [Contents](index.html) | [Next](pointers.html)

* * *

# 4 Functions

> _“Sir, not in an environment such as this. That’s why I’ve also been programmed for over thirty secondary functions that—”_
> 
> —C3PO, before being rudely interrupted, reporting a now-unimpressive number of additional functions, _Star Wars_ script

Very much like other languages you’re used to, C has the concept of _functions_.

Functions can accept a variety of _arguments_ and return a value. One important thing, though: the arguments and return value types are predeclared—because that’s how C likes it!

Let’s take a look at a function. This is a function that takes an `int` as an argument, and returns an `int`.
    
    
    [](functions.html#cb59-1)#include <stdio.h>
    [](functions.html#cb59-2)
    [](functions.html#cb59-3)int plus_one(int n)  // The "definition"
    [](functions.html#cb59-4){
    [](functions.html#cb59-5)    return n + 1;
    [](functions.html#cb59-6)}
    [](functions.html#cb59-7) 

The `int` before the `plus_one` indicates the return type.

The `int n` indicates that this function takes one `int` argument, stored in _parameter_ `n`. A parameter is a special type of local variable into which the arguments are copied.

I’m going to drive home the point that the arguments are copied into the parameters, here. Lots of things in C are easier to understand if you know that the parameter is a _copy_ of the argument, not the argument itself. More on that in a minute.

Continuing the program down into `main()`, we can see the call to the function, where we assign the return value into local variable `j`:
    
    
    [](functions.html#cb60-8)int main(void)
    [](functions.html#cb60-9){
    [](functions.html#cb60-10)    int i = 10, j;
    [](functions.html#cb60-11)    
    [](functions.html#cb60-12)    j = plus_one(i);  // The "call"
    [](functions.html#cb60-13)
    [](functions.html#cb60-14)    printf("i + 1 is %d\n", j);
    [](functions.html#cb60-15)}

> Before I forget, notice that I defined the function before I used it. If I hadn’t done that, the compiler wouldn’t know about it yet when it compiles `main()` and it would have given an unknown function call error. There is a more proper way to do the above code with _function prototypes_ , but we’ll talk about that later.

Also notice that `main()` is a function!

It returns an `int`.

But what’s this `void` thing? This is a keyword that’s used to indicate that the function accepts no arguments.

You can also return `void` to indicate that you don’t return a value:
    
    
    [](functions.html#cb61-1)#include <stdio.h>
    [](functions.html#cb61-2)
    [](functions.html#cb61-3)// This function takes no arguments and returns no value:
    [](functions.html#cb61-4)
    [](functions.html#cb61-5)void hello(void)
    [](functions.html#cb61-6){
    [](functions.html#cb61-7)    printf("Hello, world!\n");
    [](functions.html#cb61-8)}
    [](functions.html#cb61-9)
    [](functions.html#cb61-10)int main(void)
    [](functions.html#cb61-11){
    [](functions.html#cb61-12)    hello();  // Prints "Hello, world!"
    [](functions.html#cb61-13)}

## 4.1 Passing by Value

I’d mentioned earlier that when you pass an argument to a function, a copy of that argument gets made and stored in the corresponding parameter.

If the argument is a variable, a copy of the value of that variable gets made and stored in the parameter.

More generally, the entire argument expression is evaluated and its value determined. That value is copied to the parameter.

In any case, the value in the parameter is its own thing. It is independent of whatever values or variables you used as arguments when you made the function call.

So let’s look at an example here. Study it and see if you can determine the output before running it:
    
    
    [](functions.html#cb62-1)#include <stdio.h>
    [](functions.html#cb62-2)
    [](functions.html#cb62-3)void increment(int a)
    [](functions.html#cb62-4){
    [](functions.html#cb62-5)    a++;
    [](functions.html#cb62-6)}
    [](functions.html#cb62-7)
    [](functions.html#cb62-8)int main(void)
    [](functions.html#cb62-9){
    [](functions.html#cb62-10)    int i = 10;
    [](functions.html#cb62-11)
    [](functions.html#cb62-12)    increment(i);
    [](functions.html#cb62-13)
    [](functions.html#cb62-14)    printf("i == %d\n", i);  // What does this print?
    [](functions.html#cb62-15)}

At first glance, it looks like `i` is `10`, and we pass it to the function `increment()`. There the value gets incremented, so when we print it, it must be `11`, right?

> _“Get used to disappointment.”_
> 
> —Dread Pirate Roberts, _The Princess Bride_

But it’s not `11`—it prints `10`! How?

It’s all about the fact that the expressions you pass to functions get _copied_ onto their corresponding parameters. The parameter is a copy, not the original.

So `i` is `10` out in `main()`. And we pass it to `increment()`. The corresponding parameter is called `a` in that function.

And the copy happens, as if by assignment. Loosely, `a = i`. So at that point, `a` is `10`. And out in `main()`, `i` is also `10`.

Then we increment `a` to `11`. But we’re not touching `i` at all! It remains `10`.

Finally, the function is complete. All its local variables are discarded (bye, `a`!) and we return to `main()`, where `i` is still `10`.

And we print it, getting `10`, and we’re done.

This is why in the previous example with the `plus_one()` function, we `return`ed the locally modified value so that we could see it again in `main()`.

Seems a little bit restrictive, huh? Like you can only get one piece of data back from a function, is what you’re thinking. There is, however, another way to get data back; C folks call it _passing by reference_ and that’s a story we’ll tell another time.

But no fancy-schmancy name will distract you from the fact that _EVERYTHING_ you pass to a function _WITHOUT EXCEPTION_ is copied into its corresponding parameter, and the function operates on that local copy, _NO MATTER WHAT_. Remember that, even when we’re talking about this so-called passing by reference. 

## 4.2 Function Prototypes

So if you recall back in the ice age a few sections ago, I mentioned that you had to define the function before you used it, otherwise the compiler wouldn’t know about it ahead of time, and would bomb out with an error.

This isn’t quite strictly true. You can notify the compiler in advance that you’ll be using a function of a certain type that has a certain parameter list. That way the function can be defined anywhere (even in a different file), as long as the _function prototype_ has been declared before you call that function.

Fortunately, the function prototype is really quite easy. It’s merely a copy of the first line of the function definition with a semicolon tacked on the end for good measure. For example, this code calls a function that is defined later, because a prototype has been declared first:
    
    
    [](functions.html#cb63-1)#include <stdio.h>
    [](functions.html#cb63-2)
    [](functions.html#cb63-3)int foo(void);  // This is the prototype!
    [](functions.html#cb63-4)
    [](functions.html#cb63-5)int main(void)
    [](functions.html#cb63-6){
    [](functions.html#cb63-7)    int i;
    [](functions.html#cb63-8)    
    [](functions.html#cb63-9)    // We can call foo() here before it's definition because the
    [](functions.html#cb63-10)    // prototype has already been declared, above!
    [](functions.html#cb63-11)
    [](functions.html#cb63-12)    i = foo();
    [](functions.html#cb63-13)    
    [](functions.html#cb63-14)    printf("%d\n", i);  // 3490
    [](functions.html#cb63-15)}
    [](functions.html#cb63-16)
    [](functions.html#cb63-17)int foo(void)  // This is the definition, just like the prototype!
    [](functions.html#cb63-18){
    [](functions.html#cb63-19)    return 3490;
    [](functions.html#cb63-20)}

If you don’t declare your function before you use it (either with a prototype or its definition), you’re performing something called an _implicit declaration_. This was allowed in the first C standard (C89), and that standard has rules about it, but is no longer allowed today. And there is no legitimate reason to rely on it in new code.

You might notice something about the sample code we’ve been using… That is, we’ve been using the good old `printf()` function without defining it or declaring a prototype! How do we get away with this lawlessness? We don’t, actually. There is a prototype; it’s in that header file `stdio.h` that we included with `#include`, remember? So we’re still legit, officer!

## 4.3 Empty Parameter Lists

You might see these from time to time in older code, but you shouldn’t ever code one up in new code. Always use `void` to indicate that a function takes no parameters. There’s never[44](function-specifiers-alignment-specifiersoperators.html#fn44) a reason to skip this in modern code.

If you’re good at just remembering to put `void` in for empty parameter lists in functions and prototypes, you can skip the rest of this section.

There are two contexts for this:

  * Omitting all parameters where the function is defined
  * Omitting all parameters in a prototype



Let’s look at a potential function definition first:
    
    
    [](functions.html#cb64-1)void foo()  // Should really have a `void` in there
    [](functions.html#cb64-2){
    [](functions.html#cb64-3)    printf("Hello, world!\n");
    [](functions.html#cb64-4)}

While the spec spells out that the behavior in this instance is _as-if_ you’d indicated `void` (C11 §6.7.6.3¶14), the `void` type is there for a reason. Use it.

But in the case of a function prototype, there is a _significant_ difference between using `void` and not:
    
    
    [](functions.html#cb65-1)void foo();
    [](functions.html#cb65-2)void foo(void);  // Not the same!

Leaving `void` out of the prototype indicates to the compiler that there is no additional information about the parameters to the function. It effectively turns off all that type checking.

With a prototype **definitely** use `void` when you have an empty parameter list.

* * *

[Prev](variables-and-statements.html) | [Contents](index.html) | [Next](pointers.html)
