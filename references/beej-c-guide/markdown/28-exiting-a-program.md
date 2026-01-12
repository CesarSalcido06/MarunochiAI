[Prev](unicode-wide-characters-and-all-that.html) | [Contents](index.html) | [Next](signal-handling.html)

* * *

# 28 Exiting a Program

Turns out there are a lot of ways to do this, and even ways to set up “hooks” so that a function runs when a program exits.

In this chapter we’ll dive in and check them out.

We already covered the meaning of the exit status code in the [Exit Status](the-outside-environment.html#exit-status) section, so jump back there and review if you have to.

All the functions in this section are in `<stdlib.h>`.

## 28.1 Normal Exits

We’ll start with the regular ways to exit a program, and then jump to some of the rarer, more esoteric ones.

When you exit a program normally, all open I/O streams are flushed and temporary files removed. Basically it’s a nice exit where everything gets cleaned up and handled. It’s what you want to do almost all the time unless you have reasons to do otherwise.

### 28.1.1 Returning From `main()`

If you’ve noticed, `main()` has a return type of `int`… and yet I’ve rarely, if ever, been `return`ing anything from `main()` at all.

This is because for `main()` only (and I can’t stress enough this special case _only_ applies to `main()` and no other functions anywhere) has an _implicit_ `return 0` if you fall off the end.

You can explicitly `return` from `main()` any time you want, and some programmers feel it’s more _Right_ to always have a `return` at the end of `main()`. But if you leave it off, C will put one there for you.

So… here are the `return` rules for `main()`:

  * You can return an exit status from `main()` with a `return` statement. `main()` is the only function with this special behavior. Using `return` in any other function just returns from that function to the caller.
  * If you don’t explicitly `return` and just fall off the end of `main()`, it’s just as if you’d returned `0` or `EXIT_SUCCESS`.



### 28.1.2 `exit()`

This one has also made an appearance a few times. If you call `exit()` from anywhere in your program, it will exit at that point.

The argument you pass to `exit()` is the exit status.

### 28.1.3 Setting Up Exit Handlers with `atexit()`

You can register functions to be called when a program exits whether by returning from `main()` or calling the `exit()` function.

A call to `atexit()` with the handler function name will get it done. You can register multiple exit handlers, and they’ll be called in the reverse order of registration.

Here’s an example:
    
    
    [](exiting-a-program.html#cb576-1)#include <stdio.h>
    [](exiting-a-program.html#cb576-2)#include <stdlib.h>
    [](exiting-a-program.html#cb576-3)
    [](exiting-a-program.html#cb576-4)void on_exit_1(void)
    [](exiting-a-program.html#cb576-5){
    [](exiting-a-program.html#cb576-6)    printf("Exit handler 1 called!\n");
    [](exiting-a-program.html#cb576-7)}
    [](exiting-a-program.html#cb576-8)
    [](exiting-a-program.html#cb576-9)void on_exit_2(void)
    [](exiting-a-program.html#cb576-10){
    [](exiting-a-program.html#cb576-11)    printf("Exit handler 2 called!\n");
    [](exiting-a-program.html#cb576-12)}
    [](exiting-a-program.html#cb576-13)
    [](exiting-a-program.html#cb576-14)int main(void)
    [](exiting-a-program.html#cb576-15){
    [](exiting-a-program.html#cb576-16)    atexit(on_exit_1);
    [](exiting-a-program.html#cb576-17)    atexit(on_exit_2);
    [](exiting-a-program.html#cb576-18)    
    [](exiting-a-program.html#cb576-19)    printf("About to exit...\n");
    [](exiting-a-program.html#cb576-20)}

And the output is:
    
    
    [](exiting-a-program.html#cb577-1)About to exit...
    [](exiting-a-program.html#cb577-2)Exit handler 2 called!
    [](exiting-a-program.html#cb577-3)Exit handler 1 called!

## 28.2 Quicker Exits with `quick_exit()`

This is similar to a normal exit, except:

  * Open files might not be flushed.
  * Temporary files might not be removed.
  * `atexit()` handlers won’t be called.



But there is a way to register exit handlers: call `at_quick_exit()` analogously to how you’d call `atexit()`.
    
    
    [](exiting-a-program.html#cb578-1)#include <stdio.h>
    [](exiting-a-program.html#cb578-2)#include <stdlib.h>
    [](exiting-a-program.html#cb578-3)
    [](exiting-a-program.html#cb578-4)void on_quick_exit_1(void)
    [](exiting-a-program.html#cb578-5){
    [](exiting-a-program.html#cb578-6)    printf("Quick exit handler 1 called!\n");
    [](exiting-a-program.html#cb578-7)}
    [](exiting-a-program.html#cb578-8)
    [](exiting-a-program.html#cb578-9)void on_quick_exit_2(void)
    [](exiting-a-program.html#cb578-10){
    [](exiting-a-program.html#cb578-11)    printf("Quick exit handler 2 called!\n");
    [](exiting-a-program.html#cb578-12)}
    [](exiting-a-program.html#cb578-13)
    [](exiting-a-program.html#cb578-14)void on_exit(void)
    [](exiting-a-program.html#cb578-15){
    [](exiting-a-program.html#cb578-16)    printf("Normal exit--I won't be called!\n");
    [](exiting-a-program.html#cb578-17)}
    [](exiting-a-program.html#cb578-18)
    [](exiting-a-program.html#cb578-19)int main(void)
    [](exiting-a-program.html#cb578-20){
    [](exiting-a-program.html#cb578-21)    at_quick_exit(on_quick_exit_1);
    [](exiting-a-program.html#cb578-22)    at_quick_exit(on_quick_exit_2);
    [](exiting-a-program.html#cb578-23)
    [](exiting-a-program.html#cb578-24)    atexit(on_exit);  // This won't be called
    [](exiting-a-program.html#cb578-25)
    [](exiting-a-program.html#cb578-26)    printf("About to quick exit...\n");
    [](exiting-a-program.html#cb578-27)
    [](exiting-a-program.html#cb578-28)    quick_exit(0);
    [](exiting-a-program.html#cb578-29)}

Which gives this output:
    
    
    [](exiting-a-program.html#cb579-1)About to quick exit...
    [](exiting-a-program.html#cb579-2)Quick exit handler 2 called!
    [](exiting-a-program.html#cb579-3)Quick exit handler 1 called!

It works just like `exit()`/`atexit()`, except for the fact that file flushing and cleanup might not be done.

## 28.3 Nuke it from Orbit: `_Exit()`

Calling `_Exit()` exits immediately, period. No on-exit callback functions are executed. Files won’t be flushed. Temp files won’t be removed.

Use this if you have to exit _right fargin’ now_.

## 28.4 Exiting Sometimes: `assert()`

The `assert()` statement is used to insist that something be true, or else the program will exit.

Devs often use an assert to catch Should-Never-Happen type errors.
    
    
    [](exiting-a-program.html#cb580-1)#define PI 3.14159
    [](exiting-a-program.html#cb580-2)
    [](exiting-a-program.html#cb580-3)assert(PI > 3);   // Sure enough, it is, so carry on

versus:
    
    
    [](exiting-a-program.html#cb581-1)goats -= 100;
    [](exiting-a-program.html#cb581-2)
    [](exiting-a-program.html#cb581-3)assert(goats >= 0);  // Can't have negative goats

In that case, if I try to run it and `goats` falls under `0`, this happens:
    
    
    [](exiting-a-program.html#cb582-1)goat_counter: goat_counter.c:8: main: Assertion `goats >= 0' failed.
    [](exiting-a-program.html#cb582-2)Aborted

and I’m dropped back to the command line.

This isn’t very user-friendly, so it’s only used for things the user will never see. And often people [write their own assert macros that can more easily be turned off](the-c-preprocessor.html#my-assert).

## 28.5 Abnormal Exit: `abort()`

You can use this if something has gone horribly wrong and you want to indicate as much to the outside environment. This also won’t necessarily clean up any open files, etc.

I’ve rarely seen this used.

Some foreshadowing about _signals_ : this actually works by raising a `SIGABRT` which will end the process.

What happens after that is up to the system, but on Unix-likes, it was common to [dump core](https://en.wikipedia.org/wiki/Core_dump)[171](function-specifiers-alignment-specifiersoperators.html#fn171) as the program terminated.

* * *

[Prev](unicode-wide-characters-and-all-that.html) | [Contents](index.html) | [Next](signal-handling.html)
