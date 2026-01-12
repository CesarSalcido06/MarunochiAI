[Prev](date-and-time-functionality.html) | [Contents](index.html) | [Next](chapter-atomics.html)

* * *

# 39 Multithreading

C11 introduced, formally, multithreading to the C language. It’s very eerily similar to [POSIX threads](https://en.wikipedia.org/wiki/POSIX_Threads)[197](function-specifiers-alignment-specifiersoperators.html#fn197), if you’ve ever used those.

And if you’ve not, no worries. We’ll talk it through.

Do note, however, that I’m not intending this to be a full-blown classic multithreading how-to[198](function-specifiers-alignment-specifiersoperators.html#fn198); you’ll have to pick up a different very thick book for that, specifically. Sorry!

Threading is an optional feature. If a C11+ compiler defines `__STDC_NO_THREADS__`, threads will **not** be present in the library. Why they decided to go with a negative sense in that macro is beyond me, but there we are.

You can test for it like this:
    
    
    [](multithreading.html#cb744-1)#ifdef __STDC_NO_THREADS__
    [](multithreading.html#cb744-2)#error I need threads to build this program!
    [](multithreading.html#cb744-3)#endif

Also, you might need to specify certain linker options when building. In the case of Unix-likes, try appending a `-lpthreads` to the end of the command line to link the `pthreads` library[199](function-specifiers-alignment-specifiersoperators.html#fn199):
    
    
    [](multithreading.html#cb745-1)gcc -std=c11 -o foo foo.c -lpthreads

If you’re getting linker errors on your system, it could be because the appropriate library wasn’t included.

## 39.1 Background

Threads are a way to have all those shiny CPU cores you paid for do work for you in the same program.

Normally, a C program just runs on a single CPU core. But if you know how to split up the work, you can give pieces of it to a number of threads and have them do the work simultaneously.

Though the spec doesn’t say it, on your system it’s very likely that C (or the OS at its behest) will attempt to balance the threads over all your CPU cores.

And if you have more threads than cores, that’s OK. You just won’t realize all those gains if they’re all trying to compete for CPU time.

## 39.2 Things You Can Do

You can create a thread. It will begin running the function you specify. The parent thread that spawned it will also continue to run.

And you can wait for the thread to complete. This is called _joining_.

Or if you don’t care when the thread completes and don’t want to wait, you can _detach it_.

A thread can explicitly _exit_ , or it can implicitly call it quits by returning from its main function.

A thread can also _sleep_ for a period of time, doing nothing while other threads run.

The `main()` program is a thread, as well.

Additionally, we have thread local storage, mutexes, and conditional variables. But more on those later. Let’s just look at the basics for now.

## 39.3 Data Races and the Standard Library

Some of the functions in the standard library (e.g. `asctime()` and `strtok()`) return or use `static` data elements that aren’t threadsafe. But in general unless it’s said otherwise, the standard library makes an effort to be so[200](function-specifiers-alignment-specifiersoperators.html#fn200).

But keep an eye out. If a standard library function is maintaining state between calls in a variable you don’t own, or if a function is returning a pointer to a thing that you didn’t pass in, it’s not threadsafe.

## 39.4 Creating and Waiting for Threads

Let’s hack something up!

We’ll make some threads (create) and wait for them to complete (join).

We have a tiny bit to understand first, though.

Every single thread is identified by an opaque variable of type `thrd_t`. It’s a unique identifier per thread in your program. When you create a thread, it’s given a new ID.

Also when you make the thread, you have to give it a pointer to a function to run, and a pointer to an argument to pass to it (or `NULL` if you don’t have anything to pass).

The thread will begin execution on the function you specify.

When you want to wait for a thread to complete, you have to specify its thread ID so C knows which one to wait for.

So the basic idea is:

  1. Write a function to act as the thread’s “`main`”. It’s not `main()`-proper, but analogous to it. The thread will start running there.
  2. From the main thread, launch a new thread with `thrd_create()`, and pass it a pointer to the function to run.
  3. In that function, have the thread do whatever it has to do.
  4. Meantimes, the main thread can continue doing whatever _it_ has to do.
  5. When the main thread decides to, it can wait for the child thread to complete by calling `thrd_join()`. Generally you **must** `thrd_join()` the thread to clean up after it or else you’ll leak memory[201](function-specifiers-alignment-specifiersoperators.html#fn201)



`thrd_create()` takes a pointer to the function to run, and it’s of type `thrd_start_t`, which is `int (*)(void *)`. That’s Greek for “a pointer to a function that takes an `void*` as an argument, and returns an `int`.”

Let’s make a thread! We’ll launch it from the main thread with `thrd_create()` to run a function, do some other things, then wait for it to complete with `thrd_join()`. I’ve named the thread’s main function `run()`, but you can name it anything as long as the types match `thrd_start_t`.
    
    
    [](multithreading.html#cb746-1)#include <stdio.h>
    [](multithreading.html#cb746-2)#include <threads.h>
    [](multithreading.html#cb746-3)
    [](multithreading.html#cb746-4)// This is the function the thread will run. It can be called anything.
    [](multithreading.html#cb746-5)//
    [](multithreading.html#cb746-6)// arg is the argument pointer passed to `thrd_create()`.
    [](multithreading.html#cb746-7)//
    [](multithreading.html#cb746-8)// The parent thread will get the return value back from `thrd_join()`'
    [](multithreading.html#cb746-9)// later.
    [](multithreading.html#cb746-10)
    [](multithreading.html#cb746-11)int run(void *arg)
    [](multithreading.html#cb746-12){
    [](multithreading.html#cb746-13)    int *a = arg;  // We'll pass in an int* from thrd_create()
    [](multithreading.html#cb746-14)
    [](multithreading.html#cb746-15)    printf("THREAD: Running thread with arg %d\n", *a);
    [](multithreading.html#cb746-16)
    [](multithreading.html#cb746-17)    return 12;  // Value to be picked up by thrd_join() (chose 12 at random)
    [](multithreading.html#cb746-18)}
    [](multithreading.html#cb746-19)
    [](multithreading.html#cb746-20)int main(void)
    [](multithreading.html#cb746-21){
    [](multithreading.html#cb746-22)    thrd_t t;  // t will hold the thread ID
    [](multithreading.html#cb746-23)    int arg = 3490;
    [](multithreading.html#cb746-24)
    [](multithreading.html#cb746-25)    printf("Launching a thread\n");
    [](multithreading.html#cb746-26)
    [](multithreading.html#cb746-27)    // Launch a thread to the run() function, passing a pointer to 3490
    [](multithreading.html#cb746-28)    // as an argument. Also stored the thread ID in t:
    [](multithreading.html#cb746-29)
    [](multithreading.html#cb746-30)    thrd_create(&t, run, &arg);
    [](multithreading.html#cb746-31)
    [](multithreading.html#cb746-32)    printf("Doing other things while the thread runs\n");
    [](multithreading.html#cb746-33)
    [](multithreading.html#cb746-34)    printf("Waiting for thread to complete...\n");
    [](multithreading.html#cb746-35)
    [](multithreading.html#cb746-36)    int res;  // Holds return value from the thread exit
    [](multithreading.html#cb746-37)
    [](multithreading.html#cb746-38)    // Wait here for the thread to complete; store the return value
    [](multithreading.html#cb746-39)    // in res:
    [](multithreading.html#cb746-40)
    [](multithreading.html#cb746-41)    thrd_join(t, &res);
    [](multithreading.html#cb746-42)
    [](multithreading.html#cb746-43)    printf("Thread exited with return value %d\n", res);
    [](multithreading.html#cb746-44)}

See how we did the `thrd_create()` there to call the `run()` function? Then we did other things in `main()` and then stopped and waited for the thread to complete with `thrd_join()`.

Sample output (yours might vary):
    
    
    [](multithreading.html#cb747-1)Launching a thread
    [](multithreading.html#cb747-2)Doing other things while the thread runs
    [](multithreading.html#cb747-3)Waiting for thread to complete...
    [](multithreading.html#cb747-4)THREAD: Running thread with arg 3490
    [](multithreading.html#cb747-5)Thread exited with return value 12

The `arg` that you pass to the function has to have a lifetime long enough so that the thread can pick it up before it goes away. Also, it needs to not be overwritten by the main thread before the new thread can use it.

Let’s look at an example that launches 5 threads. One thing to note here is how we use an array of `thrd_t`s to keep track of all the thread IDs.
    
    
    [](multithreading.html#cb748-1)#include <stdio.h>
    [](multithreading.html#cb748-2)#include <threads.h>
    [](multithreading.html#cb748-3)
    [](multithreading.html#cb748-4)int run(void *arg)
    [](multithreading.html#cb748-5){
    [](multithreading.html#cb748-6)    int i = *(int*)arg;
    [](multithreading.html#cb748-7)
    [](multithreading.html#cb748-8)    printf("THREAD %d: running!\n", i);
    [](multithreading.html#cb748-9)
    [](multithreading.html#cb748-10)    return i;
    [](multithreading.html#cb748-11)}
    [](multithreading.html#cb748-12)
    [](multithreading.html#cb748-13)#define THREAD_COUNT 5
    [](multithreading.html#cb748-14)
    [](multithreading.html#cb748-15)int main(void)
    [](multithreading.html#cb748-16){
    [](multithreading.html#cb748-17)    thrd_t t[THREAD_COUNT];
    [](multithreading.html#cb748-18)
    [](multithreading.html#cb748-19)    int i;
    [](multithreading.html#cb748-20)
    [](multithreading.html#cb748-21)    printf("Launching threads...\n");
    [](multithreading.html#cb748-22)    for (i = 0; i < THREAD_COUNT; i++)
    [](multithreading.html#cb748-23)
    [](multithreading.html#cb748-24)        // NOTE! In the following line, we pass a pointer to i, 
    [](multithreading.html#cb748-25)        // but each thread sees the same pointer. So they'll
    [](multithreading.html#cb748-26)        // print out weird things as i changes value here in
    [](multithreading.html#cb748-27)        // the main thread! (More in the text, below.)
    [](multithreading.html#cb748-28)
    [](multithreading.html#cb748-29)        thrd_create(t + i, run, &i);
    [](multithreading.html#cb748-30)
    [](multithreading.html#cb748-31)    printf("Doing other things while the thread runs...\n");
    [](multithreading.html#cb748-32)    printf("Waiting for thread to complete...\n");
    [](multithreading.html#cb748-33)
    [](multithreading.html#cb748-34)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb748-35)        int res;
    [](multithreading.html#cb748-36)        thrd_join(t[i], &res);
    [](multithreading.html#cb748-37)
    [](multithreading.html#cb748-38)        printf("Thread %d complete!\n", res);
    [](multithreading.html#cb748-39)    }
    [](multithreading.html#cb748-40)
    [](multithreading.html#cb748-41)    printf("All threads complete!\n");
    [](multithreading.html#cb748-42)}

When I run the threads, I count `i` up from 0 to 4. And pass a pointer to it to `thrd_create()`. This pointer ends up in the `run()` routine where we make a copy of it.

Simple enough? Here’s the output:
    
    
    [](multithreading.html#cb749-1)Launching threads...
    [](multithreading.html#cb749-2)THREAD 2: running!
    [](multithreading.html#cb749-3)THREAD 3: running!
    [](multithreading.html#cb749-4)THREAD 4: running!
    [](multithreading.html#cb749-5)THREAD 2: running!
    [](multithreading.html#cb749-6)Doing other things while the thread runs...
    [](multithreading.html#cb749-7)Waiting for thread to complete...
    [](multithreading.html#cb749-8)Thread 2 complete!
    [](multithreading.html#cb749-9)Thread 2 complete!
    [](multithreading.html#cb749-10)THREAD 5: running!
    [](multithreading.html#cb749-11)Thread 3 complete!
    [](multithreading.html#cb749-12)Thread 4 complete!
    [](multithreading.html#cb749-13)Thread 5 complete!
    [](multithreading.html#cb749-14)All threads complete!

Whaaa—? Where’s `THREAD 0`? And why do we have a `THREAD 5` when clearly `i` is never more than `4` when we call `thrd_create()`? And two `THREAD 2`s? Madness!

This is getting into the fun land of _race conditions_. The main thread is modifying `i` before the thread has a chance to copy it. Indeed, `i` makes it all the way to `5` and ends the loop before the last thread gets a chance to copy it.

We’ve got to have a per-thread variable that we can refer to so we can pass it in as the `arg`.

We could have a big array of them. Or we could `malloc()` space (and free it somewhere—maybe in the thread itself.)

Let’s give that a shot:
    
    
    [](multithreading.html#cb750-1)#include <stdio.h>
    [](multithreading.html#cb750-2)#include <stdlib.h>
    [](multithreading.html#cb750-3)#include <threads.h>
    [](multithreading.html#cb750-4)
    [](multithreading.html#cb750-5)int run(void *arg)
    [](multithreading.html#cb750-6){
    [](multithreading.html#cb750-7)    int i = *(int*)arg;  // Copy the arg
    [](multithreading.html#cb750-8)
    [](multithreading.html#cb750-9)    free(arg);  // Done with this
    [](multithreading.html#cb750-10)
    [](multithreading.html#cb750-11)    printf("THREAD %d: running!\n", i);
    [](multithreading.html#cb750-12)
    [](multithreading.html#cb750-13)    return i;
    [](multithreading.html#cb750-14)}
    [](multithreading.html#cb750-15)
    [](multithreading.html#cb750-16)#define THREAD_COUNT 5
    [](multithreading.html#cb750-17)
    [](multithreading.html#cb750-18)int main(void)
    [](multithreading.html#cb750-19){
    [](multithreading.html#cb750-20)    thrd_t t[THREAD_COUNT];
    [](multithreading.html#cb750-21)
    [](multithreading.html#cb750-22)    int i;
    [](multithreading.html#cb750-23)
    [](multithreading.html#cb750-24)    printf("Launching threads...\n");
    [](multithreading.html#cb750-25)    for (i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb750-26)
    [](multithreading.html#cb750-27)        // Get some space for a per-thread argument:
    [](multithreading.html#cb750-28)
    [](multithreading.html#cb750-29)        int *arg = malloc(sizeof *arg);
    [](multithreading.html#cb750-30)        *arg = i;
    [](multithreading.html#cb750-31)
    [](multithreading.html#cb750-32)        thrd_create(t + i, run, arg);
    [](multithreading.html#cb750-33)    }
    [](multithreading.html#cb750-34)
    [](multithreading.html#cb750-35)    // ...

Notice on lines 27-30 we `malloc()` space for an `int` and copy the value of `i` into it. Each new thread gets its own freshly-`malloc()`d variable and we pass a pointer to that to the `run()` function.

Once `run()` makes its own copy of the `arg` on line 7, it `free()`s the `malloc()`d `int`. And now that it has its own copy, it can do with it what it pleases.

And a run shows the result:
    
    
    [](multithreading.html#cb751-1)Launching threads...
    [](multithreading.html#cb751-2)THREAD 0: running!
    [](multithreading.html#cb751-3)THREAD 1: running!
    [](multithreading.html#cb751-4)THREAD 2: running!
    [](multithreading.html#cb751-5)THREAD 3: running!
    [](multithreading.html#cb751-6)Doing other things while the thread runs...
    [](multithreading.html#cb751-7)Waiting for thread to complete...
    [](multithreading.html#cb751-8)Thread 0 complete!
    [](multithreading.html#cb751-9)Thread 1 complete!
    [](multithreading.html#cb751-10)Thread 2 complete!
    [](multithreading.html#cb751-11)Thread 3 complete!
    [](multithreading.html#cb751-12)THREAD 4: running!
    [](multithreading.html#cb751-13)Thread 4 complete!
    [](multithreading.html#cb751-14)All threads complete!

There we go! Threads 0-4 all in effect!

Your run might vary—how the threads get scheduled to run is beyond the C spec. We see in the above example that thread 4 didn’t even begin until threads 0-1 had completed. Indeed, if I run this again, I likely get different output. We cannot guarantee a thread execution order.

## 39.5 Detaching Threads

If you want to fire-and-forget a thread (i.e. so you don’t have to `thrd_join()` it later), you can do that with `thrd_detach()`.

This removes the parent thread’s ability to get the return value from the child thread, but if you don’t care about that and just want threads to clean up nicely on their own, this is the way to go.

Basically we’re going to do this:
    
    
    [](multithreading.html#cb752-1)thrd_create(&t, run, NULL);
    [](multithreading.html#cb752-2)thrd_detach(t);

where the `thrd_detach()` call is the parent thread saying, “Hey, I’m not going to wait for this child thread to complete with `thrd_join()`. So go ahead and clean it up on your own when it completes.”
    
    
    [](multithreading.html#cb753-1)#include <stdio.h>
    [](multithreading.html#cb753-2)#include <threads.h>
    [](multithreading.html#cb753-3)
    [](multithreading.html#cb753-4)int run(void *arg)
    [](multithreading.html#cb753-5){
    [](multithreading.html#cb753-6)    (void)arg;
    [](multithreading.html#cb753-7)
    [](multithreading.html#cb753-8)    //printf("Thread running! %lu\n", thrd_current()); // non-portable!
    [](multithreading.html#cb753-9)    printf("Thread running!\n");
    [](multithreading.html#cb753-10)
    [](multithreading.html#cb753-11)    return 0;
    [](multithreading.html#cb753-12)}
    [](multithreading.html#cb753-13)
    [](multithreading.html#cb753-14)#define THREAD_COUNT 10
    [](multithreading.html#cb753-15)
    [](multithreading.html#cb753-16)int main(void)
    [](multithreading.html#cb753-17){
    [](multithreading.html#cb753-18)    thrd_t t;
    [](multithreading.html#cb753-19)
    [](multithreading.html#cb753-20)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb753-21)        thrd_create(&t, run, NULL);
    [](multithreading.html#cb753-22)        thrd_detach(t);               // <-- DETACH!
    [](multithreading.html#cb753-23)    }
    [](multithreading.html#cb753-24)
    [](multithreading.html#cb753-25)    // Sleep for a second to let all the threads finish
    [](multithreading.html#cb753-26)    thrd_sleep(&(struct timespec){.tv_sec=1}, NULL);
    [](multithreading.html#cb753-27)}

Note that in this code, we put the main thread to sleep for 1 second with `thrd_sleep()`—more on that later.

Also in the `run()` function, I have a commented-out line in there that prints out the thread ID as an `unsigned long`. This is non-portable, because the spec doesn’t say what type a `thrd_t` is under the hood—it could be a `struct` for all we know. But that line works on my system.

Something interesting I saw when I ran the code, above, and printed out the thread IDs was that some threads had duplicate IDs! This seems like it should be impossible, but C is allowed to _reuse_ thread IDs after the corresponding thread has exited. So what I was seeing was that some threads completed their run before other threads were launched.

## 39.6 Thread Local Data

Threads are interesting because they don’t have their own memory beyond local variables. If you want a `static` variable or file scope variable, all threads will see that same variable.

This can lead to race conditions, where you get _Weird Things_ ™ happening.

Check out this example. We have a `static` variable `foo` in block scope in `run()`. This variable will be visible to all threads that pass through the `run()` function. And the various threads can effectively step on each others toes.

Each thread copies `foo` into a local variable `x` (which is not shared between threads—all the threads have their own call stacks). So they _should_ be the same, right?

And the first time we print them, they are[202](function-specifiers-alignment-specifiersoperators.html#fn202). But then right after that, we check to make sure they’re still the same.

And they _usually_ are. But not always!
    
    
    [](multithreading.html#cb754-1)#include <stdio.h>
    [](multithreading.html#cb754-2)#include <stdlib.h>
    [](multithreading.html#cb754-3)#include <threads.h>
    [](multithreading.html#cb754-4)
    [](multithreading.html#cb754-5)int run(void *arg)
    [](multithreading.html#cb754-6){
    [](multithreading.html#cb754-7)    int n = *(int*)arg;  // Thread number for humans to differentiate
    [](multithreading.html#cb754-8)
    [](multithreading.html#cb754-9)    free(arg);
    [](multithreading.html#cb754-10)
    [](multithreading.html#cb754-11)    static int foo = 10;  // Static value shared between threads
    [](multithreading.html#cb754-12)
    [](multithreading.html#cb754-13)    int x = foo;  // Automatic local variable--each thread has its own
    [](multithreading.html#cb754-14)
    [](multithreading.html#cb754-15)    // We just assigned x from foo, so they'd better be equal here.
    [](multithreading.html#cb754-16)    // (In all my test runs, they were, but even this isn't guaranteed!)
    [](multithreading.html#cb754-17)
    [](multithreading.html#cb754-18)    printf("Thread %d: x = %d, foo = %d\n", n, x, foo);
    [](multithreading.html#cb754-19)
    [](multithreading.html#cb754-20)    // And they should be equal here, but they're not always!
    [](multithreading.html#cb754-21)    // (Sometimes they were, sometimes they weren't!)
    [](multithreading.html#cb754-22)
    [](multithreading.html#cb754-23)    // What happens is another thread gets in and increments foo
    [](multithreading.html#cb754-24)    // right now, but this thread's x remains what it was before!
    [](multithreading.html#cb754-25)
    [](multithreading.html#cb754-26)    if (x != foo) {
    [](multithreading.html#cb754-27)        printf("Thread %d: Craziness! x != foo! %d != %d\n", n, x, foo);
    [](multithreading.html#cb754-28)    }
    [](multithreading.html#cb754-29)
    [](multithreading.html#cb754-30)    foo++;  // Increment shared value
    [](multithreading.html#cb754-31)
    [](multithreading.html#cb754-32)    return 0;
    [](multithreading.html#cb754-33)}
    [](multithreading.html#cb754-34)
    [](multithreading.html#cb754-35)#define THREAD_COUNT 5
    [](multithreading.html#cb754-36)
    [](multithreading.html#cb754-37)int main(void)
    [](multithreading.html#cb754-38){
    [](multithreading.html#cb754-39)    thrd_t t[THREAD_COUNT];
    [](multithreading.html#cb754-40)
    [](multithreading.html#cb754-41)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb754-42)        int *n = malloc(sizeof *n);  // Holds a thread serial number
    [](multithreading.html#cb754-43)        *n = i;
    [](multithreading.html#cb754-44)        thrd_create(t + i, run, n);
    [](multithreading.html#cb754-45)    }
    [](multithreading.html#cb754-46)
    [](multithreading.html#cb754-47)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb754-48)        thrd_join(t[i], NULL);
    [](multithreading.html#cb754-49)    }
    [](multithreading.html#cb754-50)}

Here’s an example output (though this varies from run to run):
    
    
    [](multithreading.html#cb755-1)Thread 0: x = 10, foo = 10
    [](multithreading.html#cb755-2)Thread 1: x = 10, foo = 10
    [](multithreading.html#cb755-3)Thread 1: Craziness! x != foo! 10 != 11
    [](multithreading.html#cb755-4)Thread 2: x = 12, foo = 12
    [](multithreading.html#cb755-5)Thread 4: x = 13, foo = 13
    [](multithreading.html#cb755-6)Thread 3: x = 14, foo = 14

In thread 1, between the two `printf()`s, the value of `foo` somehow changed from `10` to `11`, even though clearly there’s no increment between the `printf()`s!

It was another thread that got in there (probably thread 0, from the look of it) and incremented the value of `foo` behind thread 1’s back!

Let’s solve this problem two different ways. (If you want all the threads to share the variable _and_ not step on each other’s toes, you’ll have to read on to the [mutex](multithreading.html#mutex) section.)

### 39.6.1 `_Thread_local` Storage-Class

First things first, let’s just look at the easy way around this: the `_Thread_local` storage-class.

Basically we’re just going to slap this on the front of our block scope `static` variable and things will work! It tells C that every thread should have its own version of this variable, so none of them step on each other’s toes.

The `<threads.h>` header defines `thread_local` as an alias to `_Thread_local` so your code doesn’t have to look so ugly.

Let’s take the previous example and make `foo` into a `thread_local` variable so that we don’t share that data.
    
    
    [](multithreading.html#cb756-5)int run(void *arg)
    [](multithreading.html#cb756-6){
    [](multithreading.html#cb756-7)    int n = *(int*)arg;  // Thread number for humans to differentiate
    [](multithreading.html#cb756-8)
    [](multithreading.html#cb756-9)    free(arg);
    [](multithreading.html#cb756-10)
    [](multithreading.html#cb756-11)    thread_local static int foo = 10;  // <-- No longer shared!!

And running we get:
    
    
    [](multithreading.html#cb757-1)Thread 0: x = 10, foo = 10
    [](multithreading.html#cb757-2)Thread 1: x = 10, foo = 10
    [](multithreading.html#cb757-3)Thread 2: x = 10, foo = 10
    [](multithreading.html#cb757-4)Thread 4: x = 10, foo = 10
    [](multithreading.html#cb757-5)Thread 3: x = 10, foo = 10

No more weird problems!

One thing: if a `thread_local` variable is block scope, it **must** be `static`. Them’s the rules. (But this is OK because non-`static` variables are per-thread already since each thread has it’s own non-`static` variables.)

A bit of a lie there: block scope `thread_local` variables can also be `extern`.

### 39.6.2 Another Option: Thread-Specific Storage

Thread-specific storage (TSS) is another way of getting per-thread data.

One additional feature is that these functions allow you to specify a destructor that will be called on the data when the TSS variable is deleted. Commonly this destructor is `free()` to automatically clean up `malloc()`d per-thread data. Or `NULL` if you don’t need to destroy anything.

The destructor is type `tss_dtor_t` which is a pointer to a function that returns `void` and takes a `void*` as an argument (the `void*` points to the data stored in the variable). In other words, it’s a `void (*)(void*)`, if that clears it up. Which I admit it probably doesn’t. Check out the example, below.

Generally, `thread_local` is probably your go-to, but if you like the destructor idea, then you can make use of that.

The usage is a bit weird in that we need a variable of type `tss_t` to be alive to represent the value on a per thread basis. Then we initialize it with `tss_create()`. Eventually we get rid of it with `tss_delete()`. Note that calling `tss_delete()` doesn’t run all the destructors—it’s `thrd_exit()` (or returning from the run function) that does that. `tss_delete()` just releases any memory allocated by `tss_create()`. 

In the middle, threads can call `tss_set()` and `tss_get()` to set and get the value.

In the following code, we set up the TSS variable before creating the threads, then clean up after the threads.

In the `run()` function, the threads `malloc()` some space for a string and store that pointer in the TSS variable.

When the thread exits, the destructor function (`free()` in this case) is called for _all_ the threads.
    
    
    [](multithreading.html#cb758-1)#include <stdio.h>
    [](multithreading.html#cb758-2)#include <stdlib.h>
    [](multithreading.html#cb758-3)#include <threads.h>
    [](multithreading.html#cb758-4)
    [](multithreading.html#cb758-5)tss_t str;
    [](multithreading.html#cb758-6)
    [](multithreading.html#cb758-7)void some_function(void)
    [](multithreading.html#cb758-8){
    [](multithreading.html#cb758-9)    // Retrieve the per-thread value of this string
    [](multithreading.html#cb758-10)    char *tss_string = tss_get(str);
    [](multithreading.html#cb758-11)
    [](multithreading.html#cb758-12)    // And print it
    [](multithreading.html#cb758-13)    printf("TSS string: %s\n", tss_string);
    [](multithreading.html#cb758-14)}
    [](multithreading.html#cb758-15)
    [](multithreading.html#cb758-16)int run(void *arg)
    [](multithreading.html#cb758-17){
    [](multithreading.html#cb758-18)    int serial = *(int*)arg;  // Get this thread's serial number
    [](multithreading.html#cb758-19)    free(arg);
    [](multithreading.html#cb758-20)
    [](multithreading.html#cb758-21)    // malloc() space to hold the data for this thread
    [](multithreading.html#cb758-22)    char *s = malloc(64);
    [](multithreading.html#cb758-23)    sprintf(s, "thread %d! :)", serial);  // Happy little string
    [](multithreading.html#cb758-24)
    [](multithreading.html#cb758-25)    // Set this TSS variable to point at the string
    [](multithreading.html#cb758-26)    tss_set(str, s);
    [](multithreading.html#cb758-27)
    [](multithreading.html#cb758-28)    // Call a function that will get the variable
    [](multithreading.html#cb758-29)    some_function();
    [](multithreading.html#cb758-30)
    [](multithreading.html#cb758-31)    return 0;   // Equivalent to thrd_exit(0)
    [](multithreading.html#cb758-32)}
    [](multithreading.html#cb758-33)
    [](multithreading.html#cb758-34)#define THREAD_COUNT 15
    [](multithreading.html#cb758-35)
    [](multithreading.html#cb758-36)int main(void)
    [](multithreading.html#cb758-37){
    [](multithreading.html#cb758-38)    thrd_t t[THREAD_COUNT];
    [](multithreading.html#cb758-39)
    [](multithreading.html#cb758-40)    // Make a new TSS variable, the free() function is the destructor
    [](multithreading.html#cb758-41)    tss_create(&str, free);
    [](multithreading.html#cb758-42)
    [](multithreading.html#cb758-43)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb758-44)        int *n = malloc(sizeof *n);  // Holds a thread serial number
    [](multithreading.html#cb758-45)        *n = i;
    [](multithreading.html#cb758-46)        thrd_create(t + i, run, n);
    [](multithreading.html#cb758-47)    }
    [](multithreading.html#cb758-48)
    [](multithreading.html#cb758-49)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb758-50)        thrd_join(t[i], NULL);
    [](multithreading.html#cb758-51)    }
    [](multithreading.html#cb758-52)
    [](multithreading.html#cb758-53)    // All threads are done, so we're done with this
    [](multithreading.html#cb758-54)    tss_delete(str);
    [](multithreading.html#cb758-55)}

Again, this is kind of a painful way of doing things compared to `thread_local`, so unless you really need that destructor functionality, I’d use that instead.

## 39.7 Mutexes

If you want to only allow a single thread into a critical section of code at a time, you can protect that section with a mutex[203](function-specifiers-alignment-specifiersoperators.html#fn203).

For example, if we had a `static` variable and we wanted to be able to get and set it in two operations without another thread jumping in the middle and corrupting it, we could use a mutex for that.

You can acquire a mutex or release it. If you attempt to acquire the mutex and succeed, you may continue execution. If you attempt and fail (because someone else holds it), you will _block_[ 204](function-specifiers-alignment-specifiersoperators.html#fn204) until the mutex is released.

If multiple threads are blocked waiting for a mutex to be released, one of them will be chosen to run (at random, from our perspective), and the others will continue to sleep.

The gameplan is that first we’ll initialize a mutex variable to make it ready to use with `mtx_init()`.

Then subsequent threads can call `mtx_lock()` and `mtx_unlock()` to get and release the mutex.

When we’re completely done with the mutex, we can destroy it with `mtx_destroy()`, the logical opposite of `mtx_init()`.

First, let’s look at some code that does _not_ use a mutex, and endeavors to print out a shared (`static`) serial number and then increment it. Because we’re not using a mutex over the getting of the value (to print it) and the setting (to increment it), threads might get in each other’s way in that critical section.
    
    
    [](multithreading.html#cb759-1)#include <stdio.h>
    [](multithreading.html#cb759-2)#include <threads.h>
    [](multithreading.html#cb759-3)
    [](multithreading.html#cb759-4)int run(void *arg)
    [](multithreading.html#cb759-5){
    [](multithreading.html#cb759-6)    (void)arg;
    [](multithreading.html#cb759-7)
    [](multithreading.html#cb759-8)    static int serial = 0;   // Shared static variable!
    [](multithreading.html#cb759-9)
    [](multithreading.html#cb759-10)    printf("Thread running! %d\n", serial);
    [](multithreading.html#cb759-11)
    [](multithreading.html#cb759-12)    serial++;
    [](multithreading.html#cb759-13)
    [](multithreading.html#cb759-14)    return 0;
    [](multithreading.html#cb759-15)}
    [](multithreading.html#cb759-16)
    [](multithreading.html#cb759-17)#define THREAD_COUNT 10
    [](multithreading.html#cb759-18)
    [](multithreading.html#cb759-19)int main(void)
    [](multithreading.html#cb759-20){
    [](multithreading.html#cb759-21)    thrd_t t[THREAD_COUNT];
    [](multithreading.html#cb759-22)
    [](multithreading.html#cb759-23)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb759-24)        thrd_create(t + i, run, NULL);
    [](multithreading.html#cb759-25)    }
    [](multithreading.html#cb759-26)
    [](multithreading.html#cb759-27)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb759-28)        thrd_join(t[i], NULL);
    [](multithreading.html#cb759-29)    }
    [](multithreading.html#cb759-30)}

When I run this, I get something that looks like this:
    
    
    [](multithreading.html#cb760-1)Thread running! 0
    [](multithreading.html#cb760-2)Thread running! 0
    [](multithreading.html#cb760-3)Thread running! 0
    [](multithreading.html#cb760-4)Thread running! 3
    [](multithreading.html#cb760-5)Thread running! 4
    [](multithreading.html#cb760-6)Thread running! 5
    [](multithreading.html#cb760-7)Thread running! 6
    [](multithreading.html#cb760-8)Thread running! 7
    [](multithreading.html#cb760-9)Thread running! 8
    [](multithreading.html#cb760-10)Thread running! 9

Clearly multiple threads are getting in there and running the `printf()` before anyone gets a change to update the `serial` variable.

What we want to do is wrap the getting of the variable and setting of it into a single mutex-protected stretch of code.

We’ll add a new variable to represent the mutex of type `mtx_t` in file scope, initialize it, and then the threads can lock and unlock it in the `run()` function.
    
    
    [](multithreading.html#cb761-1)#include <stdio.h>
    [](multithreading.html#cb761-2)#include <threads.h>
    [](multithreading.html#cb761-3)
    [](multithreading.html#cb761-4)mtx_t serial_mtx;     // <-- MUTEX VARIABLE
    [](multithreading.html#cb761-5)
    [](multithreading.html#cb761-6)int run(void *arg)
    [](multithreading.html#cb761-7){
    [](multithreading.html#cb761-8)    (void)arg;
    [](multithreading.html#cb761-9)
    [](multithreading.html#cb761-10)    static int serial = 0;   // Shared static variable!
    [](multithreading.html#cb761-11)
    [](multithreading.html#cb761-12)    // Acquire the mutex--all threads will block on this call until
    [](multithreading.html#cb761-13)    // they get the lock:
    [](multithreading.html#cb761-14)
    [](multithreading.html#cb761-15)    mtx_lock(&serial_mtx);           // <-- ACQUIRE MUTEX
    [](multithreading.html#cb761-16)
    [](multithreading.html#cb761-17)    printf("Thread running! %d\n", serial);
    [](multithreading.html#cb761-18)
    [](multithreading.html#cb761-19)    serial++;
    [](multithreading.html#cb761-20)
    [](multithreading.html#cb761-21)    // Done getting and setting the data, so free the lock. This will
    [](multithreading.html#cb761-22)    // unblock threads on the mtx_lock() call:
    [](multithreading.html#cb761-23)
    [](multithreading.html#cb761-24)    mtx_unlock(&serial_mtx);         // <-- RELEASE MUTEX
    [](multithreading.html#cb761-25)
    [](multithreading.html#cb761-26)    return 0;
    [](multithreading.html#cb761-27)}
    [](multithreading.html#cb761-28)
    [](multithreading.html#cb761-29)#define THREAD_COUNT 10
    [](multithreading.html#cb761-30)
    [](multithreading.html#cb761-31)int main(void)
    [](multithreading.html#cb761-32){
    [](multithreading.html#cb761-33)    thrd_t t[THREAD_COUNT];
    [](multithreading.html#cb761-34)
    [](multithreading.html#cb761-35)    // Initialize the mutex variable, indicating this is a normal
    [](multithreading.html#cb761-36)    // no-frills, mutex:
    [](multithreading.html#cb761-37)
    [](multithreading.html#cb761-38)    mtx_init(&serial_mtx, mtx_plain);        // <-- CREATE MUTEX
    [](multithreading.html#cb761-39)
    [](multithreading.html#cb761-40)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb761-41)        thrd_create(t + i, run, NULL);
    [](multithreading.html#cb761-42)    }
    [](multithreading.html#cb761-43)
    [](multithreading.html#cb761-44)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb761-45)        thrd_join(t[i], NULL);
    [](multithreading.html#cb761-46)    }
    [](multithreading.html#cb761-47)
    [](multithreading.html#cb761-48)    // Done with the mutex, destroy it:
    [](multithreading.html#cb761-49)
    [](multithreading.html#cb761-50)    mtx_destroy(&serial_mtx);                // <-- DESTROY MUTEX
    [](multithreading.html#cb761-51)}

See how on lines 38 and 50 of `main()` we initialize and destroy the mutex.

But each individual thread acquires the mutex on line 15 and releases it on line 24.

In between the `mtx_lock()` and `mtx_unlock()` is the _critical section_ , the area of code where we don’t want multiple threads mucking about at the same time.

And now we get proper output!
    
    
    [](multithreading.html#cb762-1)Thread running! 0
    [](multithreading.html#cb762-2)Thread running! 1
    [](multithreading.html#cb762-3)Thread running! 2
    [](multithreading.html#cb762-4)Thread running! 3
    [](multithreading.html#cb762-5)Thread running! 4
    [](multithreading.html#cb762-6)Thread running! 5
    [](multithreading.html#cb762-7)Thread running! 6
    [](multithreading.html#cb762-8)Thread running! 7
    [](multithreading.html#cb762-9)Thread running! 8
    [](multithreading.html#cb762-10)Thread running! 9

If you need multiple mutexes, no problem: just have multiple mutex variables.

And always remember the Number One Rule of Multiple Mutexes: _Unlock mutexes in the opposite order in which you lock them!_

### 39.7.1 Different Mutex Types

As hinted earlier, we have a few mutex types that you can create with `mtx_init()`. (Some of these types are the result of a bitwise-OR operation, as noted in the table.)

Type | Description  
---|---  
`mtx_plain` | Regular ol’ mutex  
`mtx_timed` | Mutex that supports timeouts  
`mtx_plain|mtx_recursive` | Recursive mutex  
`mtx_timed|mtx_recursive` | Recursive mutex that supports timeouts  
  
“Recursive” means that the holder of a lock can call `mtx_lock()` multiple times on the same lock. (They have to unlock it an equal number of times before anyone else can take the mutex.) This might ease coding from time to time, especially if you call a function that needs to lock the mutex when you already hold the mutex.

And the timeout gives a thread a chance to _try_ to get the lock for a while, but then bail out if it can’t get it in that timeframe.

For a timeout mutex, be sure to create it with `mtx_timed`:
    
    
    [](multithreading.html#cb763-1)mtx_init(&serial_mtx, mtx_timed);

And then when you wait for it, you have to specify a time in UTC when it will unlock[205](function-specifiers-alignment-specifiersoperators.html#fn205).

The function `timespec_get()` from `<time.h>` can be of assistance here. It’ll get you the current time in UTC in a `struct timespec` which is just what we need. In fact, it seems to exist merely for this purpose.

It has two fields: `tv_sec` has the current time in seconds since epoch, and `tv_nsec` has the nanoseconds (billionths of a second) as the “fractional” part.

So you can load that up with the current time, and then add to it to get a specific timeout.

Then call `mtx_timedlock()` instead of `mtx_lock()`. If it returns the value `thrd_timedout`, it timed out.
    
    
    [](multithreading.html#cb764-1)struct timespec timeout;
    [](multithreading.html#cb764-2)
    [](multithreading.html#cb764-3)timespec_get(&timeout, TIME_UTC);  // Get current time
    [](multithreading.html#cb764-4)timeout.tv_sec += 1;               // Timeout 1 second after now
    [](multithreading.html#cb764-5)
    [](multithreading.html#cb764-6)int result = mtx_timedlock(&serial_mtx, &timeout));
    [](multithreading.html#cb764-7)
    [](multithreading.html#cb764-8)if (result == thrd_timedout) {
    [](multithreading.html#cb764-9)    printf("Mutex lock timed out!\n");
    [](multithreading.html#cb764-10)}

Other than that, timed locks are the same as regular locks.

## 39.8 Condition Variables

Condition Variables are the last piece of the puzzle we need to make performant multithreaded applications and to compose more complex multithreaded structures.

A condition variable provides a way for threads to go to sleep until some event on another thread occurs.

In other words, we might have a number of threads that are rearing to go, but they have to wait until some event is true before they continue. Basically they’re being told “wait for it!” until they get notified.

And this works hand-in-hand with mutexes since what we’re going to wait on generally depends on the value of some data, and that data generally needs to be protected by a mutex.

It’s important to note that the condition variable itself isn’t the holder of any particular data from our perspective. It’s merely the variable by which C keeps track of the waiting/not-waiting status of a particular thread or group of threads.

Let’s write a contrived program that reads in groups of 5 numbers from the main thread one at a time. Then, when 5 numbers have been entered, the child thread wakes up, sums up those 5 numbers, and prints the result.

The numbers will be stored in a global, shared array, as will the index into the array of the about-to-be-entered number.

Since these are shared values, we at least have to hide them behind a mutex for both the main and child threads. (The main will be writing data to them and the child will be reading data from them.)

But that’s not enough. The child thread needs to block (“sleep”) until 5 numbers have been read into the array. And then the parent thread needs to wake up the child thread so it can do its work.

And when it wakes up, it needs to be holding that mutex. And it will! When a thread waits on a condition variable, it also acquires a mutex when it wakes up.

All this takes place around an additional variable of type `cnd_t` that is the _condition variable_. We create this variable with the `cnd_init()` function and destroy it when we’re done with it with the `cnd_destroy()` function.

But how’s this all work? Let’s look at the outline of what the child thread will do:

  1. Lock the mutex with `mtx_lock()`
  2. If we haven’t entered all the numbers, wait on the condition variable with `cnd_wait()`
  3. Do the work that needs doing
  4. Unlock the mutex with `mtx_unlock()`



Meanwhile the main thread will be doing this:

  1. Lock the mutex with `mtx_lock()`
  2. Store the recently-read number into the array
  3. If the array is full, signal the child to wake up with `cnd_signal()`
  4. Unlock the mutex with `mtx_unlock()`



If you didn’t skim that too hard (it’s OK—I’m not offended), you might notice something weird: how can the main thread hold the mutex lock and signal the child, if the child has to hold the mutex lock to wait for the signal? They can’t both hold the lock!

And indeed they don’t! There’s some behind-the-scenes magic with condition variables: when you `cnd_wait()`, it releases the mutex that you specify and the thread goes to sleep. And when someone signals that thread to wake up, it reacquires the lock as if nothing had happened.

It’s a little different on the `cnd_signal()` side of things. This doesn’t do anything with the mutex. The signaling thread still must manually release the mutex before the waiting threads can wake up.

One more thing on the `cnd_wait()`. You’ll probably be calling `cnd_wait()` if some condition[206](function-specifiers-alignment-specifiersoperators.html#fn206) is not yet met (e.g. in this case, if not all the numbers have yet been entered). Here’s the deal: this condition should be in a `while` loop, not an `if` statement. Why?

It’s because of a mysterious phenomenon called a _spurious wakeup_. Sometimes, in some implementations, a thread can be woken up out of a `cnd_wait()` sleep for seemingly _no reason_. _[X-Files music]_[ 207](function-specifiers-alignment-specifiersoperators.html#fn207). And so we have to check to see that the condition we need is still actually met when we wake up. And if it’s not, back to sleep with us!

So let’s do this thing! Starting with the main thread:

  * The main thread will set up the mutex and condition variable, and will launch the child thread.

  * Then it will, in an infinite loop, get numbers as input from the console.

  * It will also acquire the mutex to store the inputted number into a global array.

  * When the array has 5 numbers in it, the main thread will signal the child thread that it’s time to wake up and do its work.

  * Then the main thread will unlock the mutex and go back to reading the next number from the console.




Meanwhile, the child thread has been up to its own shenanigans:

  * The child thread grabs the mutex

  * While the condition is not met (i.e. while the shared array doesn’t yet have 5 numbers in it), the child thread sleeps by waiting on the condition variable. When it waits, it implicitly unlocks the mutex.

  * Once the main thread signals the child thread to wake up, it wakes up to do the work and gets the mutex lock back.

  * The child thread sums the numbers and resets the variable that is the index into the array.

  * It then releases the mutex and runs again in an infinite loop.




And here’s the code! Give it some study so you can see where all the above pieces are being handled:
    
    
    [](multithreading.html#cb765-1)#include <stdio.h>
    [](multithreading.html#cb765-2)#include <threads.h>
    [](multithreading.html#cb765-3)
    [](multithreading.html#cb765-4)#define VALUE_COUNT_MAX 5
    [](multithreading.html#cb765-5)
    [](multithreading.html#cb765-6)int value[VALUE_COUNT_MAX];  // Shared global
    [](multithreading.html#cb765-7)int value_count = 0;   // Shared global, too
    [](multithreading.html#cb765-8)
    [](multithreading.html#cb765-9)mtx_t value_mtx;   // Mutex around value
    [](multithreading.html#cb765-10)cnd_t value_cnd;   // Condition variable on value
    [](multithreading.html#cb765-11)
    [](multithreading.html#cb765-12)int run(void *arg)
    [](multithreading.html#cb765-13){
    [](multithreading.html#cb765-14)    (void)arg;
    [](multithreading.html#cb765-15)
    [](multithreading.html#cb765-16)    for (;;) {
    [](multithreading.html#cb765-17)        mtx_lock(&value_mtx);      // <-- GRAB THE MUTEX
    [](multithreading.html#cb765-18)
    [](multithreading.html#cb765-19)        while (value_count < VALUE_COUNT_MAX) {
    [](multithreading.html#cb765-20)            printf("Thread: is waiting\n");
    [](multithreading.html#cb765-21)            cnd_wait(&value_cnd, &value_mtx);  // <-- CONDITION WAIT
    [](multithreading.html#cb765-22)        }
    [](multithreading.html#cb765-23)
    [](multithreading.html#cb765-24)        printf("Thread: is awake!\n");
    [](multithreading.html#cb765-25)
    [](multithreading.html#cb765-26)        int t = 0;
    [](multithreading.html#cb765-27)
    [](multithreading.html#cb765-28)        // Add everything up
    [](multithreading.html#cb765-29)        for (int i = 0; i < VALUE_COUNT_MAX; i++)
    [](multithreading.html#cb765-30)            t += value[i];
    [](multithreading.html#cb765-31)
    [](multithreading.html#cb765-32)        printf("Thread: total is %d\n", t);
    [](multithreading.html#cb765-33)
    [](multithreading.html#cb765-34)        // Reset input index for main thread
    [](multithreading.html#cb765-35)        value_count = 0;
    [](multithreading.html#cb765-36)
    [](multithreading.html#cb765-37)        mtx_unlock(&value_mtx);   // <-- MUTEX UNLOCK
    [](multithreading.html#cb765-38)    }
    [](multithreading.html#cb765-39)
    [](multithreading.html#cb765-40)    return 0;
    [](multithreading.html#cb765-41)}
    [](multithreading.html#cb765-42)
    [](multithreading.html#cb765-43)int main(void)
    [](multithreading.html#cb765-44){
    [](multithreading.html#cb765-45)    thrd_t t;
    [](multithreading.html#cb765-46)
    [](multithreading.html#cb765-47)    // Spawn a new thread
    [](multithreading.html#cb765-48)
    [](multithreading.html#cb765-49)    thrd_create(&t, run, NULL);
    [](multithreading.html#cb765-50)    thrd_detach(t);
    [](multithreading.html#cb765-51)
    [](multithreading.html#cb765-52)    // Set up the mutex and condition variable
    [](multithreading.html#cb765-53)
    [](multithreading.html#cb765-54)    mtx_init(&value_mtx, mtx_plain);
    [](multithreading.html#cb765-55)    cnd_init(&value_cnd);
    [](multithreading.html#cb765-56)
    [](multithreading.html#cb765-57)    for (;;) {
    [](multithreading.html#cb765-58)        int n;
    [](multithreading.html#cb765-59)
    [](multithreading.html#cb765-60)        scanf("%d", &n);
    [](multithreading.html#cb765-61)
    [](multithreading.html#cb765-62)        mtx_lock(&value_mtx);    // <-- LOCK MUTEX
    [](multithreading.html#cb765-63)
    [](multithreading.html#cb765-64)        value[value_count++] = n;
    [](multithreading.html#cb765-65)
    [](multithreading.html#cb765-66)        if (value_count == VALUE_COUNT_MAX) {
    [](multithreading.html#cb765-67)            printf("Main: signaling thread\n");
    [](multithreading.html#cb765-68)            cnd_signal(&value_cnd);  // <-- SIGNAL CONDITION
    [](multithreading.html#cb765-69)        }
    [](multithreading.html#cb765-70)
    [](multithreading.html#cb765-71)        mtx_unlock(&value_mtx);  // <-- UNLOCK MUTEX
    [](multithreading.html#cb765-72)    }
    [](multithreading.html#cb765-73)
    [](multithreading.html#cb765-74)    // Clean up (I know that's an infinite loop above here, but I
    [](multithreading.html#cb765-75)    // want to at least pretend to be proper):
    [](multithreading.html#cb765-76)
    [](multithreading.html#cb765-77)    mtx_destroy(&value_mtx);
    [](multithreading.html#cb765-78)    cnd_destroy(&value_cnd);
    [](multithreading.html#cb765-79)}

And here’s some sample output (individual numbers on lines are my input):
    
    
    [](multithreading.html#cb766-1)Thread: is waiting
    [](multithreading.html#cb766-2)1
    [](multithreading.html#cb766-3)1
    [](multithreading.html#cb766-4)1
    [](multithreading.html#cb766-5)1
    [](multithreading.html#cb766-6)1
    [](multithreading.html#cb766-7)Main: signaling thread
    [](multithreading.html#cb766-8)Thread: is awake!
    [](multithreading.html#cb766-9)Thread: total is 5
    [](multithreading.html#cb766-10)Thread: is waiting
    [](multithreading.html#cb766-11)2
    [](multithreading.html#cb766-12)8
    [](multithreading.html#cb766-13)5
    [](multithreading.html#cb766-14)9
    [](multithreading.html#cb766-15)0
    [](multithreading.html#cb766-16)Main: signaling thread
    [](multithreading.html#cb766-17)Thread: is awake!
    [](multithreading.html#cb766-18)Thread: total is 24
    [](multithreading.html#cb766-19)Thread: is waiting

It’s a common use of condition variables in producer-consumer situations like this. If we didn’t have a way to put the child thread to sleep while it waited for some condition to be met, it would be force to poll which is a big waste of CPU.

### 39.8.1 Timed Condition Wait

There’s a variant of `cnd_wait()` that allows you to specify a timeout so you can stop waiting.

Since the child thread must relock the mutex, this doesn’t necessarily mean that you’ll be popping back to life the instant the timeout occurs; you still must wait for any other threads to release the mutex.

But it does mean that you won’t be waiting until the `cnd_signal()` happens.

To make this work, call `cnd_timedwait()` instead of `cnd_wait()`. If it returns the value `thrd_timedout`, it timed out.

The timestamp is an absolute time in UTC, not a time-from-now. Thankfully the `timespec_get()` function in `<time.h>` seems custom-made for exactly this case.
    
    
    [](multithreading.html#cb767-1)struct timespec timeout;
    [](multithreading.html#cb767-2)
    [](multithreading.html#cb767-3)timespec_get(&timeout, TIME_UTC);  // Get current time
    [](multithreading.html#cb767-4)timeout.tv_sec += 1;               // Timeout 1 second after now
    [](multithreading.html#cb767-5)
    [](multithreading.html#cb767-6)int result = cnd_timedwait(&condition, &mutex, &timeout));
    [](multithreading.html#cb767-7)
    [](multithreading.html#cb767-8)if (result == thrd_timedout) {
    [](multithreading.html#cb767-9)    printf("Condition variable timed out!\n");
    [](multithreading.html#cb767-10)}

### 39.8.2 Broadcast: Wake Up All Waiting Threads

`cnd_signal()` only wakes up one thread to continue working. Depending on how you have your logic done, it might make sense to wake up more than one thread to continue once the condition is met.

Of course only one of them can grab the mutex, but if you have a situation where:

  * The newly-awoken thread is responsible for waking up the next one, and—

  * There’s a chance the spurious-wakeup loop condition will prevent it from doing so, then—




you’ll want to broadcast the wake up so that you’re sure to get at least one of the threads out of that loop to launch the next one.

How, you ask?

Simply use `cnd_broadcast()` instead of `cnd_signal()`. Exact same usage, except `cnd_broadcast()` wakes up **all** the sleeping threads that were waiting on that condition variable.

## 39.9 Running a Function One Time

Let’s say you have a function that _could_ be run by many threads, but you don’t know when, and it’s not work trying to write all that logic.

There’s a way around it: use `call_once()`. Tons of threads could try to run the function, but only the first one counts[208](function-specifiers-alignment-specifiersoperators.html#fn208)

To work with this, you need a special flag variable you declare to keep track of whether or not the thing’s been run. And you need a function to run, which takes no parameters and returns no value.
    
    
    [](multithreading.html#cb768-1)once_flag of = ONCE_FLAG_INIT;  // Initialize it like this
    [](multithreading.html#cb768-2)
    [](multithreading.html#cb768-3)void run_once_function(void)
    [](multithreading.html#cb768-4){
    [](multithreading.html#cb768-5)    printf("I'll only run once!\n");
    [](multithreading.html#cb768-6)}
    [](multithreading.html#cb768-7)
    [](multithreading.html#cb768-8)int run(void *arg)
    [](multithreading.html#cb768-9){
    [](multithreading.html#cb768-10)    (void)arg;
    [](multithreading.html#cb768-11)
    [](multithreading.html#cb768-12)    call_once(&of, run_once_function);
    [](multithreading.html#cb768-13)
    [](multithreading.html#cb768-14)    // ...

In this example, no matter how many threads get to the `run()` function, the `run_once_function()` will only be called a single time.

* * *

[Prev](date-and-time-functionality.html) | [Contents](index.html) | [Next](chapter-atomics.html)
