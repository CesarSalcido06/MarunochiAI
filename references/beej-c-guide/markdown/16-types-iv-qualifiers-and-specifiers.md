[Prev](types-iii-conversions.html) | [Contents](index.html) | [Next](multifile-projects.html)

* * *

# 16 Types IV: Qualifiers and Specifiers

Now that we have some more types under our belts, turns out we can give these types some additional attributes that control their behavior. These are the _type qualifiers_ and _storage-class specifiers_.

## 16.1 Type Qualifiers

These are going to allow you to declare constant values, and also to give the compiler optimization hints that it can use.

### 16.1.1 `const`

This is the most common type qualifier you’ll see. It means the variable is constant, and any attempt to modify it will result in a very angry compiler.
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb263-1)const int x = 2;
    [](types-iv-qualifiers-and-specifiers.html#cb263-2)
    [](types-iv-qualifiers-and-specifiers.html#cb263-3)x = 4;  // COMPILER PUKING SOUNDS, can't assign to a constant

You can’t change a `const` value.

Often you see `const` in parameter lists for functions:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb264-1)void foo(const int x)
    [](types-iv-qualifiers-and-specifiers.html#cb264-2){
    [](types-iv-qualifiers-and-specifiers.html#cb264-3)    printf("%d\n", x + 30);  // OK, doesn't modify "x"
    [](types-iv-qualifiers-and-specifiers.html#cb264-4)}

#### 16.1.1.1 `const` and Pointers

This one gets a little funky, because there are two usages that have two meanings when it comes to pointers.

For one thing, we can make it so you can’t change the thing the pointer points to. You do this by putting the `const` up front with the type name (before the asterisk) in the type declaration.
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb265-1)int x[] = {10, 20};
    [](types-iv-qualifiers-and-specifiers.html#cb265-2)const int *p = x; 
    [](types-iv-qualifiers-and-specifiers.html#cb265-3)
    [](types-iv-qualifiers-and-specifiers.html#cb265-4)p++;  // We can modify p, no problem
    [](types-iv-qualifiers-and-specifiers.html#cb265-5)
    [](types-iv-qualifiers-and-specifiers.html#cb265-6)*p = 30; // Compiler error! Can't change what it points to

Somewhat confusingly, these two things are equivalent:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb266-1)const int *p;  // Can't modify what p points to
    [](types-iv-qualifiers-and-specifiers.html#cb266-2)int const *p;  // Can't modify what p points to, just like the previous line

Great, so we can’t change the thing the pointer points to, but we can change the pointer itself. What if we want the other way around? We want to be able to change what the pointer points to, but _not_ the pointer itself?

Just move the `const` after the asterisk in the declaration:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb267-1)int *const p;   // We can't modify "p" with pointer arithmetic
    [](types-iv-qualifiers-and-specifiers.html#cb267-2)
    [](types-iv-qualifiers-and-specifiers.html#cb267-3)p++;  // Compiler error!

But we can modify what they point to:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb268-1)int x = 10;
    [](types-iv-qualifiers-and-specifiers.html#cb268-2)int *const p = &x;
    [](types-iv-qualifiers-and-specifiers.html#cb268-3)
    [](types-iv-qualifiers-and-specifiers.html#cb268-4)*p = 20;   // Set "x" to 20, no problem

You can also make both things `const`:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb269-1)const int *const p;  // Can't modify p or *p!

Finally, if you have multiple levels of indirection, you should `const` the appropriate levels. Just because a pointer is `const`, doesn’t mean the pointer it points to must also be. You can explicitly set them like in the following examples:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb270-1)char **p;
    [](types-iv-qualifiers-and-specifiers.html#cb270-2)p++;     // OK!
    [](types-iv-qualifiers-and-specifiers.html#cb270-3)(*p)++;  // OK!
    [](types-iv-qualifiers-and-specifiers.html#cb270-4)
    [](types-iv-qualifiers-and-specifiers.html#cb270-5)char **const p;
    [](types-iv-qualifiers-and-specifiers.html#cb270-6)p++;     // Error!
    [](types-iv-qualifiers-and-specifiers.html#cb270-7)(*p)++;  // OK!
    [](types-iv-qualifiers-and-specifiers.html#cb270-8)
    [](types-iv-qualifiers-and-specifiers.html#cb270-9)char *const *p;
    [](types-iv-qualifiers-and-specifiers.html#cb270-10)p++;     // OK!
    [](types-iv-qualifiers-and-specifiers.html#cb270-11)(*p)++;  // Error!
    [](types-iv-qualifiers-and-specifiers.html#cb270-12)
    [](types-iv-qualifiers-and-specifiers.html#cb270-13)char *const *const p;
    [](types-iv-qualifiers-and-specifiers.html#cb270-14)p++;     // Error!
    [](types-iv-qualifiers-and-specifiers.html#cb270-15)(*p)++;  // Error!

#### 16.1.1.2 `const` Correctness

One more thing I have to mention is that the compiler will warn on something like this:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb271-1)const int x = 20;
    [](types-iv-qualifiers-and-specifiers.html#cb271-2)int *p = &x;

saying something to the effect of:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb272-1)initialization discards 'const' qualifier from pointer type target

What’s happening there?

Well, we need to look at the types on either side of the assignment:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb273-1)    const int x = 20;
    [](types-iv-qualifiers-and-specifiers.html#cb273-2)    int *p = &x;
    [](types-iv-qualifiers-and-specifiers.html#cb273-3)//    ^       ^
    [](types-iv-qualifiers-and-specifiers.html#cb273-4)//    |       |
    [](types-iv-qualifiers-and-specifiers.html#cb273-5)//  int*    const int*

The compiler is warning us that the value on the right side of the assignment is `const`, but the one of the left is not. And the compiler is letting us know that it is discarding the “const-ness” of the expression on the right.

That is, we _can_ still try to do the following, but it’s just wrong. The compiler will warn, and it’s undefined behavior:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb274-1)const int x = 20;
    [](types-iv-qualifiers-and-specifiers.html#cb274-2)int *p = &x;
    [](types-iv-qualifiers-and-specifiers.html#cb274-3)
    [](types-iv-qualifiers-and-specifiers.html#cb274-4)*p = 40;  // Undefined behavior--maybe it modifies "x", maybe not!
    [](types-iv-qualifiers-and-specifiers.html#cb274-5)
    [](types-iv-qualifiers-and-specifiers.html#cb274-6)printf("%d\n", x);  // 40, if you're lucky

### 16.1.2 `restrict`

TLDR: you never have to use this and you can ignore it every time you see it. If you use it correctly, you will likely realize some performance gain. If you use it incorrectly, you will realize undefined behavior.

`restrict` is a hint to the compiler that a particular piece of memory will only be accessed by one pointer and never another. (That is, there will be no aliasing of the particular object the `restrict` pointer points to.) If a developer declares a pointer to be `restrict` and then accesses the object it points to in another way (e.g. via another pointer), the behavior is undefined.

Basically you’re telling C, “Hey—I guarantee that this one single pointer is the only way I access this memory, and if I’m lying, you can pull undefined behavior on me.”

And C uses that information to perform certain optimizations. For instance, if you’re dereferencing the `restrict` pointer repeatedly in a loop, C might decide to cache the result in a register and only store the final result once the loop completes. If any other pointer referred to that same memory and accessed it in the loop, the results would not be accurate.

(Note that `restrict` has no effect if the object pointed to is never written to. It’s all about optimizations surrounding writes to memory.)

Let’s write a function to swap two variables, and we’ll use the `restrict` keyword to assure C that we’ll never pass in pointers to the same thing. And then let’s blow it and try passing in pointers to the same thing.
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb275-1)void swap(int *restrict a, int *restrict b)
    [](types-iv-qualifiers-and-specifiers.html#cb275-2){
    [](types-iv-qualifiers-and-specifiers.html#cb275-3)    int t;
    [](types-iv-qualifiers-and-specifiers.html#cb275-4)
    [](types-iv-qualifiers-and-specifiers.html#cb275-5)    t = *a;
    [](types-iv-qualifiers-and-specifiers.html#cb275-6)    *a = *b;
    [](types-iv-qualifiers-and-specifiers.html#cb275-7)    *b = t;
    [](types-iv-qualifiers-and-specifiers.html#cb275-8)}
    [](types-iv-qualifiers-and-specifiers.html#cb275-9)
    [](types-iv-qualifiers-and-specifiers.html#cb275-10)int main(void)
    [](types-iv-qualifiers-and-specifiers.html#cb275-11){
    [](types-iv-qualifiers-and-specifiers.html#cb275-12)    int x = 10, y = 20;
    [](types-iv-qualifiers-and-specifiers.html#cb275-13)
    [](types-iv-qualifiers-and-specifiers.html#cb275-14)    swap(&x, &y);  // OK! "a" and "b", above, point to different things
    [](types-iv-qualifiers-and-specifiers.html#cb275-15)
    [](types-iv-qualifiers-and-specifiers.html#cb275-16)    swap(&x, &x);  // Undefined behavior! "a" and "b" point to the same thing
    [](types-iv-qualifiers-and-specifiers.html#cb275-17)}

If we were to take out the `restrict` keywords, above, that would allow both calls to work safely. But then the compiler might not be able to optimize.

`restrict` has block scope, that is, the restriction only lasts for the scope it’s used. If it’s in a parameter list for a function, it’s in the block scope of that function.

If the restricted pointer points to an array, it only applies to the individual objects in the array. Other pointers could read and write from the array as long as they didn’t read or write any of the same elements as the restricted one.

If it’s outside any function in file scope, the restriction covers the entire program.

You’re likely to see this in library functions like `printf()`:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb276-1)int printf(const char * restrict format, ...);

Again, that’s just telling the compiler that inside the `printf()` function, there will be only one pointer that refers to any part of that `format` string.

One last note: if you’re using array notation in your function parameter for some reason instead of pointer notation, you can use `restrict` like so:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb277-1)void foo(int p[restrict])     // With no size
    [](types-iv-qualifiers-and-specifiers.html#cb277-2)
    [](types-iv-qualifiers-and-specifiers.html#cb277-3)void foo(int p[restrict 10])  // Or with a size

But pointer notation would be more common.

### 16.1.3 `volatile`

You’re unlikely to see or need this unless you’re dealing with hardware directly.

`volatile` tells the compiler that a value might change behind its back and should be looked up every time.

An example might be where the compiler is looking in memory at an address that continuously updates behind the scenes, e.g. some kind of hardware timer.

If the compiler decides to optimize that and store the value in a register for a protracted time, the value in memory will update and won’t be reflected in the register.

By declaring something `volatile`, you’re telling the compiler, “Hey, the thing this points at might change at any time for reasons outside this program code.”
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb278-1)volatile int *p;

### 16.1.4 `_Atomic`

This is an optional C feature that we’ll talk about in [the Atomics chapter](chapter-atomics.html#chapter-atomics).

## 16.2 Storage-Class Specifiers

Storage-class specifiers are similar to type quantifiers. They give the compiler more information about the type of a variable.

### 16.2.1 `auto`

You barely ever see this keyword, since `auto` is the default for block scope variables. It’s implied.

These are the same:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb279-1){
    [](types-iv-qualifiers-and-specifiers.html#cb279-2)    int a;         // auto is the default...
    [](types-iv-qualifiers-and-specifiers.html#cb279-3)    auto int a;    // So this is redundant
    [](types-iv-qualifiers-and-specifiers.html#cb279-4)}

The `auto` keyword indicates that this object has _automatic storage duration_. That is, it exists in the scope in which it is defined, and is automatically deallocated when the scope is exited.

One gotcha about automatic variables is that their value is indeterminate until you explicitly initialize them. We say they’re full of “random” or “garbage” data, though neither of those really makes me happy. In any case, you won’t know what’s in it unless you initialize it.

Always initialize all automatic variables before use!

### 16.2.2 `static`

This keyword has two meanings, depending on if the variable is file scope or block scope.

Let’s start with block scope.

#### 16.2.2.1 `static` in Block Scope

In this case, we’re basically saying, “I just want a single instance of this variable to exist, shared between calls.”

That is, its value will persist between calls.

`static` in block scope with an initializer will only be initialized one time on program startup, not each time the function is called.

Let’s do an example:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb280-1)#include <stdio.h>
    [](types-iv-qualifiers-and-specifiers.html#cb280-2)
    [](types-iv-qualifiers-and-specifiers.html#cb280-3)void counter(void)
    [](types-iv-qualifiers-and-specifiers.html#cb280-4){
    [](types-iv-qualifiers-and-specifiers.html#cb280-5)    static int count = 1;  // This is initialized one time
    [](types-iv-qualifiers-and-specifiers.html#cb280-6)
    [](types-iv-qualifiers-and-specifiers.html#cb280-7)    printf("This has been called %d time(s)\n", count);
    [](types-iv-qualifiers-and-specifiers.html#cb280-8)
    [](types-iv-qualifiers-and-specifiers.html#cb280-9)    count++;
    [](types-iv-qualifiers-and-specifiers.html#cb280-10)}
    [](types-iv-qualifiers-and-specifiers.html#cb280-11)
    [](types-iv-qualifiers-and-specifiers.html#cb280-12)int main(void)
    [](types-iv-qualifiers-and-specifiers.html#cb280-13){
    [](types-iv-qualifiers-and-specifiers.html#cb280-14)    counter();  // "This has been called 1 time(s)"
    [](types-iv-qualifiers-and-specifiers.html#cb280-15)    counter();  // "This has been called 2 time(s)"
    [](types-iv-qualifiers-and-specifiers.html#cb280-16)    counter();  // "This has been called 3 time(s)"
    [](types-iv-qualifiers-and-specifiers.html#cb280-17)    counter();  // "This has been called 4 time(s)"
    [](types-iv-qualifiers-and-specifiers.html#cb280-18)}

See how the value of `count` persists between calls?

One thing of note is that `static` block scope variables are initialized to `0` by default.
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb281-1)static int foo;      // Default starting value is `0`...
    [](types-iv-qualifiers-and-specifiers.html#cb281-2)static int foo = 0;  // So the `0` assignment is redundant

Finally, be advised that if you’re writing multithreaded programs, you have to be sure you don’t let multiple threads trample the same variable.

#### 16.2.2.2 `static` in File Scope

When you get out to file scope, outside any blocks, the meaning rather changes.

Variables at file scope already persist between function calls, so that behavior is already there.

Instead what `static` means in this context is that this variable isn’t visible outside of this particular source file. Kinda like “global”, but only in this file.

More on that in the section about building with multiple source files.

### 16.2.3 `extern`

The `extern` storage-class specifier gives us a way to refer to objects in other source files.

Let’s say, for example, the file `bar.c` had the following as its entirety:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb282-1)// bar.c
    [](types-iv-qualifiers-and-specifiers.html#cb282-2)
    [](types-iv-qualifiers-and-specifiers.html#cb282-3)int a = 37;

Just that. Declaring a new `int a` in file scope.

But what if we had another source file, `foo.c`, and we wanted to refer to the `a` that’s in `bar.c`?

It’s easy with the `extern` keyword:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb283-1)// foo.c
    [](types-iv-qualifiers-and-specifiers.html#cb283-2)
    [](types-iv-qualifiers-and-specifiers.html#cb283-3)extern int a;
    [](types-iv-qualifiers-and-specifiers.html#cb283-4)
    [](types-iv-qualifiers-and-specifiers.html#cb283-5)int main(void)
    [](types-iv-qualifiers-and-specifiers.html#cb283-6){
    [](types-iv-qualifiers-and-specifiers.html#cb283-7)    printf("%d\n", a);  // 37, from bar.c!
    [](types-iv-qualifiers-and-specifiers.html#cb283-8)
    [](types-iv-qualifiers-and-specifiers.html#cb283-9)    a = 99;
    [](types-iv-qualifiers-and-specifiers.html#cb283-10)
    [](types-iv-qualifiers-and-specifiers.html#cb283-11)    printf("%d\n", a);  // Same "a" from bar.c, but it's now 99
    [](types-iv-qualifiers-and-specifiers.html#cb283-12)}

We could have also made the `extern int a` in block scope, and it still would have referred to the `a` in `bar.c`:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb284-1)// foo.c
    [](types-iv-qualifiers-and-specifiers.html#cb284-2)
    [](types-iv-qualifiers-and-specifiers.html#cb284-3)int main(void)
    [](types-iv-qualifiers-and-specifiers.html#cb284-4){
    [](types-iv-qualifiers-and-specifiers.html#cb284-5)    extern int a;
    [](types-iv-qualifiers-and-specifiers.html#cb284-6)
    [](types-iv-qualifiers-and-specifiers.html#cb284-7)    printf("%d\n", a);  // 37, from bar.c!
    [](types-iv-qualifiers-and-specifiers.html#cb284-8)
    [](types-iv-qualifiers-and-specifiers.html#cb284-9)    a = 99;
    [](types-iv-qualifiers-and-specifiers.html#cb284-10)
    [](types-iv-qualifiers-and-specifiers.html#cb284-11)    printf("%d\n", a);  // Same "a" from bar.c, but it's now 99
    [](types-iv-qualifiers-and-specifiers.html#cb284-12)}

Now, if `a` in `bar.c` had been marked `static`. this wouldn’t have worked. `static` variables at file scope are not visible outside that file.

A final note about `extern` on functions. For functions, `extern` is the default, so it’s redundant. You can declare a function `static` if you only want it visible in a single source file.

### 16.2.4 `register`

This is a keyword to hint to the compiler that this variable is frequently-used, and should be made as fast as possible to access. The compiler is under no obligation to agree to it.

Now, modern C compiler optimizers are pretty effective at figuring this out themselves, so it’s rare to see these days.

But if you must:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb285-1)#include <stdio.h>
    [](types-iv-qualifiers-and-specifiers.html#cb285-2)
    [](types-iv-qualifiers-and-specifiers.html#cb285-3)int main(void)
    [](types-iv-qualifiers-and-specifiers.html#cb285-4){
    [](types-iv-qualifiers-and-specifiers.html#cb285-5)    register int a;   // Make "a" as fast to use as possible.
    [](types-iv-qualifiers-and-specifiers.html#cb285-6)
    [](types-iv-qualifiers-and-specifiers.html#cb285-7)    for (a = 0; a < 10; a++)
    [](types-iv-qualifiers-and-specifiers.html#cb285-8)        printf("%d\n", a);
    [](types-iv-qualifiers-and-specifiers.html#cb285-9)}

It does come at a price, however. You can’t take the address of a register:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb286-1)register int a;
    [](types-iv-qualifiers-and-specifiers.html#cb286-2)int *p = &a;    // COMPILER ERROR! Can't take address of a register

The same applies to any part of an array:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb287-1)register int a[] = {11, 22, 33, 44, 55};
    [](types-iv-qualifiers-and-specifiers.html#cb287-2)int *p = a;  // COMPILER ERROR! Can't take address of a[0]

Or dereferencing part of an array:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb288-1)register int a[] = {11, 22, 33, 44, 55};
    [](types-iv-qualifiers-and-specifiers.html#cb288-2)
    [](types-iv-qualifiers-and-specifiers.html#cb288-3)int a = *(a + 2);  // COMPILER ERROR! Address of a[0] taken

Interestingly, for the equivalent with array notation, gcc only warns:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb289-1)register int a[] = {11, 22, 33, 44, 55};
    [](types-iv-qualifiers-and-specifiers.html#cb289-2)
    [](types-iv-qualifiers-and-specifiers.html#cb289-3)int a = a[2];  // COMPILER WARNING!

with:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb290-1)warning: ISO C forbids subscripting ‘register’ array

The fact that you can’t take the address of a register variable frees the compiler up to make optimizations around that assumption if it hasn’t figured them out already. Also adding `register` to a `const` variable prevents one from accidentally passing its pointer to another function that willfully ignore its constness[117](function-specifiers-alignment-specifiersoperators.html#fn117).

A bit of historic backstory, here: deep inside the CPU are little dedicated “variables” called [_registers_](https://en.wikipedia.org/wiki/Processor_register)[ 118](function-specifiers-alignment-specifiersoperators.html#fn118). They are super fast to access compared to RAM, so using them gets you a speed boost. But they’re not in RAM, so they don’t have an associated memory address (which is why you can’t take the address-of or get a pointer to them).

But, like I said, modern compilers are really good at producing optimal code, using registers whenever possible regardless of whether or not you specified the `register` keyword. Not only that, but the spec allows them to just treat it as if you’d typed `auto`, if they want. So no guarantees.

### 16.2.5 `_Thread_local`

When you’re using multiple threads and you have some variables in either global or `static` block scope, this is a way to make sure that each thread gets its own copy of the variable. This’ll help you avoid race conditions and threads stepping on each other’s toes.

If you’re in block scope, you have to use this along with either `extern` or `static`.

Also, if you include `<threads.h>`, you can use the rather more palatable `thread_local` as an alias for the uglier `_Thread_local`.

More information can be found in the [Threads section](multithreading.html#thread-local).

* * *

[Prev](types-iii-conversions.html) | [Contents](index.html) | [Next](multifile-projects.html)
