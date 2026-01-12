[Prev](exiting-a-program.html) | [Contents](index.html) | [Next](variable-length-arrays-vlas.html)

* * *

# 29 Signal Handling

Before we start, I’m just going to advise you to generally ignore this entire chapter and use your OS’s (very likely) superior signal handling functions. Unix-likes have the `sigaction()` family of functions, and Windows has… whatever it does[172](function-specifiers-alignment-specifiersoperators.html#fn172).

With that out of the way, what are signals?

## 29.1 What Are Signals?

A _signal_ is _raised_ on a variety of external events. Your program can be configured to be interrupted to _handle_ the signal, and, optionally, continue where it left off once the signal has been handled.

Think of it like a function that’s automatically called when one of these external events occurs.

What are these events? On your system, there are probably a lot of them, but in the C spec there are just a few:

Signal | Description  
---|---  
`SIGABRT` | Abnormal termination—what happens when `abort()` is called.  
`SIGFPE` | Floating point exception.  
`SIGILL` | Illegal instruction.  
`SIGINT` | Interrupt—usually the result of `CTRL-C` being hit.  
`SIGSEGV` | “Segmentation Violation”: invalid memory access.  
`SIGTERM` | Termination requested.  
  
You can set up your program to ignore, handle, or allow the default action for each of these by using the `signal()` function.

## 29.2 Handling Signals with `signal()`

The `signal()` call takes two parameters: the signal in question, and an action to take when that signal is raised.

The action can be one of three things:

  * A pointer to a handler function.
  * `SIG_IGN` to ignore the signal.
  * `SIG_DFL` to restore the default handler for the signal.



Let’s write a program that you can’t `CTRL-C` out of. (Don’t fret—in the following program, you can also hit `RETURN` and it’ll exit.)
    
    
    [](signal-handling.html#cb583-1)#include <stdio.h>
    [](signal-handling.html#cb583-2)#include <signal.h>
    [](signal-handling.html#cb583-3)
    [](signal-handling.html#cb583-4)int main(void)
    [](signal-handling.html#cb583-5){
    [](signal-handling.html#cb583-6)    char s[1024];
    [](signal-handling.html#cb583-7)
    [](signal-handling.html#cb583-8)    signal(SIGINT, SIG_IGN);    // Ignore SIGINT, caused by ^C
    [](signal-handling.html#cb583-9)
    [](signal-handling.html#cb583-10)    printf("Try hitting ^C... (hit RETURN to exit)\n");
    [](signal-handling.html#cb583-11)
    [](signal-handling.html#cb583-12)    // Wait for a line of input so the program doesn't just exit
    [](signal-handling.html#cb583-13)    fgets(s, sizeof s, stdin);
    [](signal-handling.html#cb583-14)}

Check out line 8—we tell the program to ignore `SIGINT`, the interrupt signal that’s raised when `CTRL-C` is hit. No matter how much you hit it, the signal remains ignored. If you comment out line 8, you’ll see you can `CTRL-C` with impunity and quit the program on the spot.

## 29.3 Writing Signal Handlers

I mentioned you could also write a handler function that gets called when the signal is raised.

These are pretty straightforward, are also very capability-limited when it comes to the spec.

Before we start, let’s look at the function prototype for the `signal()` call:
    
    
    [](signal-handling.html#cb584-1)void (*signal(int sig, void (*func)(int)))(int);

Pretty easy to read, right?

_WRONG!_ `:)`

Let’s take a moment to take it apart for practice.

`signal()` takes two arguments: an integer `sig` representing the signal, and a pointer `func` to the handler (the handler returns `void` and takes an `int` as an argument), highlighted below:
    
    
    [](signal-handling.html#cb585-1)                sig          func
    [](signal-handling.html#cb585-2)              |-----|  |---------------|
    [](signal-handling.html#cb585-3)void (*signal(int sig, void (*func)(int)))(int);

Basically, we’re going to pass in the signal number we’re interested in catching, and we’re going to pass a pointer to a function of the form:
    
    
    [](signal-handling.html#cb586-1)void f(int x);

that will do the actual catching.

Now—what about the rest of that prototype? It’s basically all the return type. See, `signal()` will return whatever you passed as `func` on success… so that means it’s returning a pointer to a function that returns `void` and takes an `int` as an argument.
    
    
    [](signal-handling.html#cb587-1)returned
    [](signal-handling.html#cb587-2)function    indicates we're              and
    [](signal-handling.html#cb587-3)returns     returning a                  that function
    [](signal-handling.html#cb587-4)void        pointer to function          takes an int
    [](signal-handling.html#cb587-5)|--|        |                                   |---|
    [](signal-handling.html#cb587-6)void       (*signal(int sig, void (*func)(int)))(int);

Also, it can return `SIG_ERR` in case of an error.

Let’s do an example where we make it so you have to hit `CTRL-C` twice to exit.

I want to be clear that this program engages in undefined behavior in a couple ways. But it’ll probably work for you, and it’s hard to come up with portable non-trivial demos.
    
    
    [](signal-handling.html#cb588-1)#include <stdio.h>
    [](signal-handling.html#cb588-2)#include <stdlib.h>
    [](signal-handling.html#cb588-3)#include <signal.h>
    [](signal-handling.html#cb588-4)
    [](signal-handling.html#cb588-5)int count = 0;
    [](signal-handling.html#cb588-6)
    [](signal-handling.html#cb588-7)void sigint_handler(int signum)
    [](signal-handling.html#cb588-8){
    [](signal-handling.html#cb588-9)    // The compiler is allowed to run:
    [](signal-handling.html#cb588-10)    //
    [](signal-handling.html#cb588-11)    //   signal(signum, SIG_DFL)
    [](signal-handling.html#cb588-12)    //
    [](signal-handling.html#cb588-13)    // when the handler is called. So we reset the handler here:
    [](signal-handling.html#cb588-14)    signal(SIGINT, sigint_handler);
    [](signal-handling.html#cb588-15)
    [](signal-handling.html#cb588-16)    (void)signum;   // Get rid of unused variable warning
    [](signal-handling.html#cb588-17)
    [](signal-handling.html#cb588-18)    count++;                       // Undefined behavior
    [](signal-handling.html#cb588-19)    printf("Count: %d\n", count);  // Undefined behavior
    [](signal-handling.html#cb588-20)
    [](signal-handling.html#cb588-21)    if (count == 2) {
    [](signal-handling.html#cb588-22)        printf("Exiting!\n");      // Undefined behavior
    [](signal-handling.html#cb588-23)        exit(0);
    [](signal-handling.html#cb588-24)    }
    [](signal-handling.html#cb588-25)}
    [](signal-handling.html#cb588-26)
    [](signal-handling.html#cb588-27)int main(void)
    [](signal-handling.html#cb588-28){
    [](signal-handling.html#cb588-29)    signal(SIGINT, sigint_handler);
    [](signal-handling.html#cb588-30)
    [](signal-handling.html#cb588-31)    printf("Try hitting ^C...\n");
    [](signal-handling.html#cb588-32)
    [](signal-handling.html#cb588-33)    for(;;);  // Wait here forever
    [](signal-handling.html#cb588-34)}

One of the things you’ll notice is that on line 14 we reset the signal handler. This is because C has the option of resetting the signal handler to its `SIG_DFL` behavior before running your custom handler. In other words, it could be a one-off. So we reset it first thing so that we handle it again for the next one.

We’re ignoring the return value from `signal()` in this case. If we’d set it to a different handler earlier, it would return a pointer to that handler, which we could get like this:
    
    
    [](signal-handling.html#cb589-1)// old_handler is type "pointer to function that takes a single
    [](signal-handling.html#cb589-2)// int parameter and returns void":
    [](signal-handling.html#cb589-3)
    [](signal-handling.html#cb589-4)void (*old_handler)(int);
    [](signal-handling.html#cb589-5)
    [](signal-handling.html#cb589-6)old_handler = signal(SIGINT, sigint_handler);

That said, I’m not sure of a common use case for this. But if you need the old handler for some reason, you can get it that way.

Quick note on line 16—that’s just to tell the compiler to not warn that we’re not using this variable. It’s like saying, “I know I’m not using it; you don’t have to warn me.”

And lastly you’ll see that I’ve marked undefined behavior in a couple places. More on that in the next section.

## 29.4 What Can We Actually Do?

Turns out we’re pretty limited in what we can and can’t do in our signal handlers. This is one of the reasons why I say you shouldn’t even bother with this and instead use your OS’s signal handling instead (e.g. `sigaction()` for Unix-like systems).

Wikipedia goes so far as to say the only really portable thing you can do is call `signal()` with `SIG_IGN` or `SIG_DFL` and that’s it.

Here’s what we **can’t** portably do:

  * Call any standard library function. 
    * Like `printf()`, for example.
    * I think it’s probably safe to call restartable/reentrant functions, but the spec doesn’t allow that liberty.
  * Get or set values from a local `static`, file scope, or thread-local variable. 
    * Unless it’s a lock-free atomic object or…
    * You’re assigning into a variable of type `volatile sig_atomic_t`.



That last bit–`sig_atomic_t`–is your ticket to getting data out of a signal handler. (Unless you want to use lock-free atomic objects, which is outside the scope of this section[173](function-specifiers-alignment-specifiersoperators.html#fn173).) It’s an integer type that might or might not be signed. And it’s bounded by what you can put in there.

You can look at the minimum and maximum allowable values in the macros `SIG_ATOMIC_MIN` and `SIG_ATOMIC_MAX`[174](function-specifiers-alignment-specifiersoperators.html#fn174).

Confusingly, the spec also says you can’t refer “to any object with static or thread storage duration that is not a lock-free atomic object other than by assigning a value to an object declared as `volatile sig_atomic_t` […]”

My read on this is that you can’t read or write anything that’s not a lock-free atomic object. Also you can assign to an object that’s `volatile sig_atomic_t`.

But can you read from it? I honestly don’t see why not, except that the spec is very pointed about mentioning assigning into. But if you have to read it and make any kind of decision based on it, you might be opening up room for some kind of race conditions.

With that in mind, we can rewrite our “hit `CTRL-C` twice to exit” code to be a little more portable, albeit less verbose on the output.

Let’s change our `SIGINT` handler to do nothing except increment a value that’s of type `volatile sig_atomic_t`. So it’ll count the number of `CTRL-C`s that have been hit.

Then in our main loop, we’ll check to see if that counter is over `2`, then bail out if it is.
    
    
    [](signal-handling.html#cb590-1)#include <stdio.h>
    [](signal-handling.html#cb590-2)#include <signal.h>
    [](signal-handling.html#cb590-3)
    [](signal-handling.html#cb590-4)volatile sig_atomic_t count = 0;
    [](signal-handling.html#cb590-5)
    [](signal-handling.html#cb590-6)void sigint_handler(int signum)
    [](signal-handling.html#cb590-7){
    [](signal-handling.html#cb590-8)    (void)signum;                    // Unused variable warning
    [](signal-handling.html#cb590-9)
    [](signal-handling.html#cb590-10)    signal(SIGINT, sigint_handler);  // Reset signal handler
    [](signal-handling.html#cb590-11)
    [](signal-handling.html#cb590-12)    count++;                         // Undefined behavior
    [](signal-handling.html#cb590-13)}
    [](signal-handling.html#cb590-14)
    [](signal-handling.html#cb590-15)int main(void)
    [](signal-handling.html#cb590-16){
    [](signal-handling.html#cb590-17)    signal(SIGINT, sigint_handler);
    [](signal-handling.html#cb590-18)
    [](signal-handling.html#cb590-19)    printf("Hit ^C twice to exit.\n");
    [](signal-handling.html#cb590-20)
    [](signal-handling.html#cb590-21)    while(count < 2);
    [](signal-handling.html#cb590-22)}

Undefined behavior again? It’s my read that this is, because we have to read the value in order to increment and store it.

If we only want to postpone the exit by one hitting of `CTRL-C`, we can do that without too much trouble. But any more postponement would require some ridiculous function chaining.

What we’ll do is handle it once, and the handler will reset the signal to its default behavior (that is, to exit):
    
    
    [](signal-handling.html#cb591-1)#include <stdio.h>
    [](signal-handling.html#cb591-2)#include <signal.h>
    [](signal-handling.html#cb591-3)
    [](signal-handling.html#cb591-4)void sigint_handler(int signum)
    [](signal-handling.html#cb591-5){
    [](signal-handling.html#cb591-6)    (void)signum;                      // Unused variable warning
    [](signal-handling.html#cb591-7)    signal(SIGINT, SIG_DFL);           // Reset signal handler
    [](signal-handling.html#cb591-8)}
    [](signal-handling.html#cb591-9)
    [](signal-handling.html#cb591-10)int main(void)
    [](signal-handling.html#cb591-11){
    [](signal-handling.html#cb591-12)    signal(SIGINT, sigint_handler);
    [](signal-handling.html#cb591-13)
    [](signal-handling.html#cb591-14)    printf("Hit ^C twice to exit.\n");
    [](signal-handling.html#cb591-15)
    [](signal-handling.html#cb591-16)    while(1);
    [](signal-handling.html#cb591-17)}

Later when we look at lock-free atomic variables, we’ll see a way to fix the `count` version (assuming lock-free atomic variables are available on your particular system).

This is why at the beginning, I was suggesting checking out your OS’s built-in signal system as a probably-superior alternative.

## 29.5 Friends Don’t Let Friends `signal()`

Again, use your OS’s built-in signal handling or the equivalent. It’s not in the spec, not as portable, but probably is far more capable. Plus your OS probably has a number of signals defined that aren’t in the C spec. And it’s difficult to write portable code using `signal()` anyway.

* * *

[Prev](exiting-a-program.html) | [Contents](index.html) | [Next](variable-length-arrays-vlas.html)
