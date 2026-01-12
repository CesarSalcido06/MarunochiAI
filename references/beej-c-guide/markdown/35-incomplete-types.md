[Prev](setjmp-longjmp.html) | [Contents](index.html) | [Next](complex-numbers.html)

* * *

# 35 Incomplete Types

It might surprise you to learn that this builds without error:
    
    
    [](incomplete-types.html#cb686-1)extern int a[];
    [](incomplete-types.html#cb686-2)
    [](incomplete-types.html#cb686-3)int main(void)
    [](incomplete-types.html#cb686-4){
    [](incomplete-types.html#cb686-5)    struct foo *x;
    [](incomplete-types.html#cb686-6)    union bar *y;
    [](incomplete-types.html#cb686-7)    enum baz *z;
    [](incomplete-types.html#cb686-8)}

We never gave a size for `a`. And we have pointers to `struct`s `foo`, `bar`, and `baz` that never seem to be declared anywhere.

And the only warnings I get are that `x`, `y`, and `z` are unused.

These are examples of _incomplete types_.

An incomplete type is a type the size (i.e. the size you’d get back from `sizeof`) for which is not known. Another way to think of it is a type that you haven’t finished declaring.

You can have a pointer to an incomplete type, but you can’t dereference it or use pointer arithmetic on it. And you can’t `sizeof` it.

So what can you do with it?

## 35.1 Use Case: Self-Referential Structures

I only know of one real use case: forward references to `struct`s or `union`s with self-referential or co-dependent structures. (I’m going to use `struct` for the rest of these examples, but they all apply equally to `union`s, as well.)

Let’s do the classic example first.

But before I do, know this! As you declare a `struct`, the `struct` is incomplete until the closing brace is reached!
    
    
    [](incomplete-types.html#cb687-1)struct antelope {              // struct antelope is incomplete here
    [](incomplete-types.html#cb687-2)    int leg_count;             // Still incomplete
    [](incomplete-types.html#cb687-3)    float stomach_fullness;    // Still incomplete
    [](incomplete-types.html#cb687-4)    float top_speed;           // Still incomplete
    [](incomplete-types.html#cb687-5)    char *nickname;            // Still incomplete
    [](incomplete-types.html#cb687-6)};                             // NOW it's complete.

So what? Seems sane enough.

But what if we’re doing a linked list? Each linked list node needs to have a reference to another node. But how can we create a reference to another node if we haven’t finished even declaring the node yet?

C’s allowance for incomplete types makes it possible. We can’t declare a node, but we _can_ declare a pointer to one, even if it’s incomplete!
    
    
    [](incomplete-types.html#cb688-1)struct node {
    [](incomplete-types.html#cb688-2)    int val;
    [](incomplete-types.html#cb688-3)    struct node *next;  // struct node is incomplete, but that's OK!
    [](incomplete-types.html#cb688-4)};

Even though the `struct node` is incomplete on line 3, we can still declare a pointer to one[184](function-specifiers-alignment-specifiersoperators.html#fn184).

We can do the same thing if we have two different `struct`s that refer to each other:
    
    
    [](incomplete-types.html#cb689-1)struct a {
    [](incomplete-types.html#cb689-2)    struct b *x;  // Refers to a `struct b`
    [](incomplete-types.html#cb689-3)};
    [](incomplete-types.html#cb689-4)
    [](incomplete-types.html#cb689-5)struct b {
    [](incomplete-types.html#cb689-6)    struct a *x;  // Refers to a `struct a`
    [](incomplete-types.html#cb689-7)};

We’d never be able to make that pair of structures without the relaxed rules for incomplete types.

## 35.2 Incomplete Type Error Messages

Are you getting errors like these?
    
    
    [](incomplete-types.html#cb690-1)invalid application of ‘sizeof’ to incomplete type
    [](incomplete-types.html#cb690-2)
    [](incomplete-types.html#cb690-3)invalid use of undefined type
    [](incomplete-types.html#cb690-4)
    [](incomplete-types.html#cb690-5)dereferencing pointer to incomplete type

Most likely culprit: you probably forgot to `#include` the header file that declares the type.

## 35.3 Other Incomplete Types

Declaring a `struct` or `union` with no body makes an incomplete type, e.g. `struct foo;`.

`enums` are incomplete until the closing brace.

`void` is an incomplete type.

Arrays declared `extern` with no size are incomplete, e.g.:
    
    
    [](incomplete-types.html#cb691-1)extern int a[];

If it’s a non-`extern` array with no size followed by an initializer, it’s incomplete until the closing brace of the initializer.

## 35.4 Use Case: Arrays in Header Files

It can be useful to declare incomplete array types in header files. In those cases, the actual storage (where the complete array is declared) should be in a single `.c` file. If you put it in the `.h` file, it will be duplicated every time the header file is included.

So what you can do is make a header file with an incomplete type that refers to the array, like so:
    
    
    [](incomplete-types.html#cb692-1)// File: bar.h
    [](incomplete-types.html#cb692-2)
    [](incomplete-types.html#cb692-3)#ifndef BAR_H
    [](incomplete-types.html#cb692-4)#define BAR_H
    [](incomplete-types.html#cb692-5)
    [](incomplete-types.html#cb692-6)extern int my_array[];  // Incomplete type
    [](incomplete-types.html#cb692-7)
    [](incomplete-types.html#cb692-8)#endif

And the in the `.c` file, actually define the array:
    
    
    [](incomplete-types.html#cb693-1)// File: bar.c
    [](incomplete-types.html#cb693-2)
    [](incomplete-types.html#cb693-3)int my_array[1024];     // Complete type!

Then you can include the header from as many places as you’d like, and every one of those places will refer to the same underlying `my_array`.
    
    
    [](incomplete-types.html#cb694-1)// File: foo.c
    [](incomplete-types.html#cb694-2)
    [](incomplete-types.html#cb694-3)#include <stdio.h>
    [](incomplete-types.html#cb694-4)#include "bar.h"    // includes the incomplete type for my_array
    [](incomplete-types.html#cb694-5)
    [](incomplete-types.html#cb694-6)int main(void)
    [](incomplete-types.html#cb694-7){
    [](incomplete-types.html#cb694-8)    my_array[0] = 10;
    [](incomplete-types.html#cb694-9)
    [](incomplete-types.html#cb694-10)    printf("%d\n", my_array[0]);
    [](incomplete-types.html#cb694-11)}

When compiling multiple files, remember to specify all the `.c` files to the compiler, but not the `.h` files, e.g.:
    
    
    [](incomplete-types.html#cb695-1)gcc -o foo foo.c bar.c

## 35.5 Completing Incomplete Types

If you have an incomplete type, you can complete it by defining the complete `struct`, `union`, `enum`, or array in the same scope.
    
    
    [](incomplete-types.html#cb696-1)struct foo;        // incomplete type
    [](incomplete-types.html#cb696-2)
    [](incomplete-types.html#cb696-3)struct foo *p;     // pointer, no problem
    [](incomplete-types.html#cb696-4)
    [](incomplete-types.html#cb696-5)// struct foo f;   // Error: incomplete type!
    [](incomplete-types.html#cb696-6)
    [](incomplete-types.html#cb696-7)struct foo {
    [](incomplete-types.html#cb696-8)    int x, y, z;
    [](incomplete-types.html#cb696-9)};                 // Now the struct foo is complete!
    [](incomplete-types.html#cb696-10)
    [](incomplete-types.html#cb696-11)struct foo f;      // Success!

Note that though `void` is an incomplete type, there’s no way to complete it. Not that anyone ever thinks of doing that weird thing. But it does explain why you can do this:
    
    
    [](incomplete-types.html#cb697-1)void *p;             // OK: pointer to incomplete type

and not either of these:
    
    
    [](incomplete-types.html#cb698-1)void v;              // Error: declare variable of incomplete type
    [](incomplete-types.html#cb698-2)
    [](incomplete-types.html#cb698-3)printf("%d\n", *p);  // Error: dereference incomplete type

The more you know…

* * *

[Prev](setjmp-longjmp.html) | [Contents](index.html) | [Next](complex-numbers.html)
