[Prev](pointers.html) | [Contents](index.html) | [Next](strings.html)

* * *

# 6 Arrays

> _“Should array indices start at 0 or 1? My compromise of 0.5 was rejected without, I thought, proper consideration.”_
> 
> —Stan Kelly-Bootle, computer scientist

Luckily, C has arrays. I mean, I know it’s considered a low-level language[54](function-specifiers-alignment-specifiersoperators.html#fn54) but it does at least have the concept of arrays built-in. And since a great many languages drew inspiration from C’s syntax, you’re probably already familiar with using `[` and `]` for declaring and using arrays.

But C only _barely_ has arrays! As we’ll find out later, arrays are just syntactic sugar in C—they’re actually all pointers and stuff deep down. _Freak out!_ But for now, let’s just use them as arrays. _Phew_.

## 6.1 Easy Example

Let’s just crank out an example:
    
    
    [](arrays.html#cb85-1)#include <stdio.h>
    [](arrays.html#cb85-2)
    [](arrays.html#cb85-3)int main(void)
    [](arrays.html#cb85-4){
    [](arrays.html#cb85-5)    int i;
    [](arrays.html#cb85-6)    float f[4];  // Declare an array of 4 floats
    [](arrays.html#cb85-7)
    [](arrays.html#cb85-8)    f[0] = 3.14159;  // Indexing starts at 0, of course.
    [](arrays.html#cb85-9)    f[1] = 1.41421;
    [](arrays.html#cb85-10)    f[2] = 1.61803;
    [](arrays.html#cb85-11)    f[3] = 2.71828;
    [](arrays.html#cb85-12)
    [](arrays.html#cb85-13)    // Print them all out:
    [](arrays.html#cb85-14)
    [](arrays.html#cb85-15)    for (i = 0; i < 4; i++) {
    [](arrays.html#cb85-16)        printf("%f\n", f[i]);
    [](arrays.html#cb85-17)    }
    [](arrays.html#cb85-18)}

When you declare an array, you have to give it a size. And the size has to be fixed[55](function-specifiers-alignment-specifiersoperators.html#fn55).

In the above example, we made an array of 4 `float`s. The value in the square brackets in the declaration lets us know that.

Later on in subsequent lines, we access the values in the array, setting them or getting them, again with square brackets. 

Hopefully this looks familiar from languages you already know!

## 6.2 Getting the Length of an Array

You can’t…ish. C doesn’t record this information[56](function-specifiers-alignment-specifiersoperators.html#fn56). You have to manage it separately in another variable.

When I say “can’t”, I actually mean there are some circumstances when you _can_. There is a trick to get the number of elements in an array in the scope in which an array is declared. But, generally speaking, this won’t work the way you want if you pass the array to a function[57](function-specifiers-alignment-specifiersoperators.html#fn57).

Let’s take a look at this trick. The basic idea is that you take the `sizeof` the array, and then divide that by the size of each element to get the length. For example, if an `int` is 4 bytes, and the array is 32 bytes long, there must be room for \\(\frac{32}{4}\\) or \\(8\\) `int`s in there.
    
    
    [](arrays.html#cb86-1)int x[12];  // 12 ints
    [](arrays.html#cb86-2)
    [](arrays.html#cb86-3)printf("%zu\n", sizeof x);     // 48 total bytes
    [](arrays.html#cb86-4)printf("%zu\n", sizeof(int));  // 4 bytes per int
    [](arrays.html#cb86-5)
    [](arrays.html#cb86-6)printf("%zu\n", sizeof x / sizeof(int));  // 48/4 = 12 ints!

If it’s an array of `char`s, then `sizeof` the array _is_ the number of elements, since `sizeof(char)` is defined to be 1. For anything else, you have to divide by the size of each element.

But this trick only works in the scope in which the array was defined. If you pass the array to a function, it doesn’t work. Even if you make it “big” in the function signature:
    
    
    [](arrays.html#cb87-1)void foo(int x[12])
    [](arrays.html#cb87-2){
    [](arrays.html#cb87-3)    printf("%zu\n", sizeof x);     // 8?! What happened to 48?
    [](arrays.html#cb87-4)    printf("%zu\n", sizeof(int));  // 4 bytes per int
    [](arrays.html#cb87-5)
    [](arrays.html#cb87-6)    printf("%zu\n", sizeof x / sizeof(int));  // 8/4 = 2 ints?? WRONG.
    [](arrays.html#cb87-7)}

This is because when you “pass” arrays to functions, you’re only passing a pointer to the first element, and that’s what `sizeof` measures. More on this in the [Passing Single Dimensional Arrays to Functions](arrays.html#passing1darrays) section, below.

One more thing you can do with `sizeof` and arrays is get the size of an array of a fixed number of elements without declaring the array. This is like how you can get the size of an `int` with `sizeof(int)`.

For example, to see how many bytes would be needed for an array of 48 `double`s, you can do this:
    
    
    [](arrays.html#cb88-1)sizeof(double [48]);

## 6.3 Array Initializers

You can initialize an array with constants ahead of time:
    
    
    [](arrays.html#cb89-1)#include <stdio.h>
    [](arrays.html#cb89-2)
    [](arrays.html#cb89-3)int main(void)
    [](arrays.html#cb89-4){
    [](arrays.html#cb89-5)    int i;
    [](arrays.html#cb89-6)    int a[5] = {22, 37, 3490, 18, 95};  // Initialize with these values
    [](arrays.html#cb89-7)
    [](arrays.html#cb89-8)    for (i = 0; i < 5; i++) {
    [](arrays.html#cb89-9)        printf("%d\n", a[i]);
    [](arrays.html#cb89-10)    }
    [](arrays.html#cb89-11)}

You should never have more items in your initializer than there is room for in the array, or the compiler will get cranky:
    
    
    [](arrays.html#cb90-1)foo.c: In function ‘main’:
    [](arrays.html#cb90-2)foo.c:6:39: warning: excess elements in array initializer
    [](arrays.html#cb90-3)    6 |     int a[5] = {22, 37, 3490, 18, 95, 999};
    [](arrays.html#cb90-4)      |                                       ^~~
    [](arrays.html#cb90-5)foo.c:6:39: note: (near initialization for ‘a’)

But (fun fact!) you can have _fewer_ items in your initializer than there is room for in the array. The remaining elements in the array will be automatically initialized with zero. This is true in general for all types of array initializers: if you have an initializer, anything not explicitly set to a value will be set to zero.
    
    
    [](arrays.html#cb91-1)int a[5] = {22, 37, 3490};
    [](arrays.html#cb91-2)
    [](arrays.html#cb91-3)// is the same as:
    [](arrays.html#cb91-4)
    [](arrays.html#cb91-5)int a[5] = {22, 37, 3490, 0, 0};

It’s a common shortcut to see this in an initializer when you want to set an entire array to zero:
    
    
    [](arrays.html#cb92-1)int a[100] = {0};

Which means, “Make the first element zero, and then automatically make the rest zero, as well.”

You can set specific array elements in the initializer, as well, by specifying an index for the value! When you do this, C will happily keep initializing subsequent values for you until the initializer runs out, filling everything else with `0`.

To do this, put the index in square brackets with an `=` after, and then set the value.

Here’s an example where we build an array:
    
    
    [](arrays.html#cb93-1)int a[10] = {0, 11, 22, [5]=55, 66, 77};

Because we listed index 5 as the start for `55`, the resulting data in the array is:
    
    
    [](arrays.html#cb94-1)0 11 22 0 0 55 66 77 0 0

You can put simple constant expressions in there, as well.
    
    
    [](arrays.html#cb95-1)#define COUNT 5
    [](arrays.html#cb95-2)
    [](arrays.html#cb95-3)int a[COUNT] = {[COUNT-3]=3, 2, 1};

which gives us:
    
    
    [](arrays.html#cb96-1)0 0 3 2 1

Lastly, you can also have C compute the size of the array from the initializer, just by leaving the size off:
    
    
    [](arrays.html#cb97-1)int a[3] = {22, 37, 3490};
    [](arrays.html#cb97-2)
    [](arrays.html#cb97-3)// is the same as:
    [](arrays.html#cb97-4)
    [](arrays.html#cb97-5)int a[] = {22, 37, 3490};  // Left the size off!

## 6.4 Out of Bounds!

C doesn’t stop you from accessing arrays out of bounds. It might not even warn you.

Let’s steal the example from above and keep printing off the end of the array. It only has 5 elements, but let’s try to print 10 and see what happens:
    
    
    [](arrays.html#cb98-1)#include <stdio.h>
    [](arrays.html#cb98-2)
    [](arrays.html#cb98-3)int main(void)
    [](arrays.html#cb98-4){
    [](arrays.html#cb98-5)    int i;
    [](arrays.html#cb98-6)    int a[5] = {22, 37, 3490, 18, 95};
    [](arrays.html#cb98-7)
    [](arrays.html#cb98-8)    for (i = 0; i < 10; i++) {  // BAD NEWS: printing too many elements!
    [](arrays.html#cb98-9)        printf("%d\n", a[i]);
    [](arrays.html#cb98-10)    }
    [](arrays.html#cb98-11)}

Running it on my computer prints:
    
    
    [](arrays.html#cb99-1)22
    [](arrays.html#cb99-2)37
    [](arrays.html#cb99-3)3490
    [](arrays.html#cb99-4)18
    [](arrays.html#cb99-5)95
    [](arrays.html#cb99-6)32765
    [](arrays.html#cb99-7)1847052032
    [](arrays.html#cb99-8)1780534144
    [](arrays.html#cb99-9)-56487472
    [](arrays.html#cb99-10)21890

Yikes! What’s that? Well, turns out printing off the end of an array results in what C developers call _undefined behavior_. We’ll talk more about this beast later, but for now it means, “You’ve done something bad, and anything could happen during your program run.”

And by anything, I mean typically things like finding zeroes, finding garbage numbers, or crashing. But really the C spec says in this circumstance the compiler is allowed to emit code that does _anything_[ 58](function-specifiers-alignment-specifiersoperators.html#fn58).

Short version: don’t do anything that causes undefined behavior. Ever[59](function-specifiers-alignment-specifiersoperators.html#fn59). 

## 6.5 Multidimensional Arrays

You can add as many dimensions as you want to your arrays.
    
    
    [](arrays.html#cb100-1)int a[10];
    [](arrays.html#cb100-2)int b[2][7];
    [](arrays.html#cb100-3)int c[4][5][6];

These are stored in memory in [row-major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order)[60](function-specifiers-alignment-specifiersoperators.html#fn60). This means with a 2D array, the first index listed indicates the row, and the second the column.

You can also use initializers on multidimensional arrays by nesting them:
    
    
    [](arrays.html#cb101-1)#include <stdio.h>
    [](arrays.html#cb101-2)
    [](arrays.html#cb101-3)int main(void)
    [](arrays.html#cb101-4){
    [](arrays.html#cb101-5)    int row, col;
    [](arrays.html#cb101-6)
    [](arrays.html#cb101-7)    int a[2][5] = {      // Initialize a 2D array
    [](arrays.html#cb101-8)        {0, 1, 2, 3, 4},
    [](arrays.html#cb101-9)        {5, 6, 7, 8, 9}
    [](arrays.html#cb101-10)    };
    [](arrays.html#cb101-11)
    [](arrays.html#cb101-12)    for (row = 0; row < 2; row++) {
    [](arrays.html#cb101-13)        for (col = 0; col < 5; col++) {
    [](arrays.html#cb101-14)            printf("(%d,%d) = %d\n", row, col, a[row][col]);
    [](arrays.html#cb101-15)        }
    [](arrays.html#cb101-16)    }
    [](arrays.html#cb101-17)}

For output of:
    
    
    [](arrays.html#cb102-1)(0,0) = 0
    [](arrays.html#cb102-2)(0,1) = 1
    [](arrays.html#cb102-3)(0,2) = 2
    [](arrays.html#cb102-4)(0,3) = 3
    [](arrays.html#cb102-5)(0,4) = 4
    [](arrays.html#cb102-6)(1,0) = 5
    [](arrays.html#cb102-7)(1,1) = 6
    [](arrays.html#cb102-8)(1,2) = 7
    [](arrays.html#cb102-9)(1,3) = 8
    [](arrays.html#cb102-10)(1,4) = 9

And you can initialize with explicit indexes:
    
    
    [](arrays.html#cb103-1)// Make a 3x3 identity matrix
    [](arrays.html#cb103-2)
    [](arrays.html#cb103-3)int a[3][3] = {[0][0]=1, [1][1]=1, [2][2]=1};

which builds a 2D array like this:
    
    
    [](arrays.html#cb104-1)1 0 0
    [](arrays.html#cb104-2)0 1 0
    [](arrays.html#cb104-3)0 0 1

## 6.6 Arrays and Pointers

[_Casually_] So… I kinda might have mentioned up there that arrays were pointers, deep down? We should take a shallow dive into that now so that things aren’t completely confusing. Later on, we’ll look at what the real relationship between arrays and pointers is, but for now I just want to look at passing arrays to functions.

### 6.6.1 Getting a Pointer to an Array

I want to tell you a secret. Generally speaking, when a C programmer talks about a pointer to an array, they’re talking about a pointer _to the first element_ of the array[61](function-specifiers-alignment-specifiersoperators.html#fn61).

So let’s get a pointer to the first element of an array.
    
    
    [](arrays.html#cb105-1)#include <stdio.h>
    [](arrays.html#cb105-2)
    [](arrays.html#cb105-3)int main(void)
    [](arrays.html#cb105-4){
    [](arrays.html#cb105-5)    int a[5] = {11, 22, 33, 44, 55};
    [](arrays.html#cb105-6)    int *p;
    [](arrays.html#cb105-7)
    [](arrays.html#cb105-8)    p = &a[0];  // p points to the array
    [](arrays.html#cb105-9)                // Well, to the first element, actually
    [](arrays.html#cb105-10)
    [](arrays.html#cb105-11)    printf("%d\n", *p);  // Prints "11"
    [](arrays.html#cb105-12)}

This is so common to do in C that the language allows us a shorthand:
    
    
    [](arrays.html#cb106-1)p = &a[0];  // p points to the array
    [](arrays.html#cb106-2)
    [](arrays.html#cb106-3)// is the same as:
    [](arrays.html#cb106-4)
    [](arrays.html#cb106-5)p = a;      // p points to the array, but much nicer-looking!

Just referring to the array name in isolation is the same as getting a pointer to the first element of the array! We’re going to use this extensively in the upcoming examples.

But hold on a second—isn’t `p` an `int*`? And `*p` gives us `11`, same as `a[0]`? Yessss. You’re starting to get a glimpse of how arrays and pointers are related in C. (We’ll talk about this a lot more in the [Pointers II](pointers2.html#pointers2) chapter, under [Array/Pointer Equivalence](pointers2.html#arraypointerequiv).) 

### 6.6.2 Passing Single Dimensional Arrays to Functions

Let’s do an example with a single dimensional array. I’m going to write a couple functions that we can pass the array to that do different things.

Prepare for some mind-blowing function signatures!
    
    
    [](arrays.html#cb107-1)#include <stdio.h>
    [](arrays.html#cb107-2)
    [](arrays.html#cb107-3)// Passing as a pointer to the first element
    [](arrays.html#cb107-4)void times2(int *a, int len)
    [](arrays.html#cb107-5){
    [](arrays.html#cb107-6)    for (int i = 0; i < len; i++)
    [](arrays.html#cb107-7)        printf("%d\n", a[i] * 2);
    [](arrays.html#cb107-8)}
    [](arrays.html#cb107-9)
    [](arrays.html#cb107-10)// Same thing, but using array notation
    [](arrays.html#cb107-11)void times3(int a[], int len)
    [](arrays.html#cb107-12){
    [](arrays.html#cb107-13)    for (int i = 0; i < len; i++)
    [](arrays.html#cb107-14)        printf("%d\n", a[i] * 3);
    [](arrays.html#cb107-15)}
    [](arrays.html#cb107-16)
    [](arrays.html#cb107-17)// Same thing, but using array notation with size
    [](arrays.html#cb107-18)void times4(int a[5], int len)
    [](arrays.html#cb107-19){
    [](arrays.html#cb107-20)    for (int i = 0; i < len; i++)
    [](arrays.html#cb107-21)        printf("%d\n", a[i] * 4);
    [](arrays.html#cb107-22)}
    [](arrays.html#cb107-23)
    [](arrays.html#cb107-24)int main(void)
    [](arrays.html#cb107-25){
    [](arrays.html#cb107-26)    int x[5] = {11, 22, 33, 44, 55};
    [](arrays.html#cb107-27)
    [](arrays.html#cb107-28)    times2(x, 5);
    [](arrays.html#cb107-29)    times3(x, 5);
    [](arrays.html#cb107-30)    times4(x, 5);
    [](arrays.html#cb107-31)}

All those methods of listing the array as a parameter in the function are identical.
    
    
    [](arrays.html#cb108-1)void times2(int *a, int len)
    [](arrays.html#cb108-2)void times3(int a[], int len)
    [](arrays.html#cb108-3)void times4(int a[5], int len)

In usage by C regulars, the first is the most common, by far.

And, in fact, in the latter situation, the compiler doesn’t even care what number you pass in (other than it has to be greater than zero[62](function-specifiers-alignment-specifiersoperators.html#fn62)). It doesn’t enforce anything at all.

Now that I’ve said that, the size of the array in the function declaration actually _does_ matter when you’re passing multidimensional arrays into functions, but let’s come back to that. 

### 6.6.3 Changing Arrays in Functions

We’ve said that arrays are just pointers in disguise. This means that if you pass an array to a function, you’re likely passing a pointer to the first element in the array.

But if the function has a pointer to the data, it is able to manipulate that data! So changes that a function makes to an array will be visible back out in the caller.

Here’s an example where we pass a pointer to an array to a function, the function manipulates the values in that array, and those changes are visible out in the caller.
    
    
    [](arrays.html#cb109-1)#include <stdio.h>
    [](arrays.html#cb109-2)
    [](arrays.html#cb109-3)void double_array(int *a, int len)
    [](arrays.html#cb109-4){
    [](arrays.html#cb109-5)    // Multiply each element by 2
    [](arrays.html#cb109-6)    //
    [](arrays.html#cb109-7)    // This doubles the values in x in main() since x and a both point
    [](arrays.html#cb109-8)    // to the same array in memory!
    [](arrays.html#cb109-9)
    [](arrays.html#cb109-10)    for (int i = 0; i < len; i++)
    [](arrays.html#cb109-11)        a[i] *= 2;
    [](arrays.html#cb109-12)}
    [](arrays.html#cb109-13)
    [](arrays.html#cb109-14)int main(void)
    [](arrays.html#cb109-15){
    [](arrays.html#cb109-16)    int x[5] = {1, 2, 3, 4, 5};
    [](arrays.html#cb109-17)
    [](arrays.html#cb109-18)    double_array(x, 5);
    [](arrays.html#cb109-19)
    [](arrays.html#cb109-20)    for (int i = 0; i < 5; i++)
    [](arrays.html#cb109-21)        printf("%d\n", x[i]);  // 2, 4, 6, 8, 10!
    [](arrays.html#cb109-22)}

Even though we passed the array in as parameter `a` which is type `int*`, look at how we access it using array notation with `a[i]`! Whaaaat. This is totally allowed.

Later when we talk about the equivalence between arrays and pointers, we’ll see how this makes a lot more sense. For now, it’s enough to know that functions can make changes to arrays that are visible out in the caller. 

### 6.6.4 Passing Multidimensional Arrays to Functions

The story changes a little when we’re talking about multidimensional arrays. C needs to know all the dimensions (except the first one) so it has enough information to know where in memory to look to find a value.

Here’s an example where we’re explicit with all the dimensions:
    
    
    [](arrays.html#cb110-1)#include <stdio.h>
    [](arrays.html#cb110-2)
    [](arrays.html#cb110-3)void print_2D_array(int a[2][3])
    [](arrays.html#cb110-4){
    [](arrays.html#cb110-5)    for (int row = 0; row < 2; row++) {
    [](arrays.html#cb110-6)        for (int col = 0; col < 3; col++)
    [](arrays.html#cb110-7)            printf("%d ", a[row][col]);
    [](arrays.html#cb110-8)        printf("\n");
    [](arrays.html#cb110-9)    }
    [](arrays.html#cb110-10)}
    [](arrays.html#cb110-11)
    [](arrays.html#cb110-12)int main(void)
    [](arrays.html#cb110-13){
    [](arrays.html#cb110-14)    int x[2][3] = {
    [](arrays.html#cb110-15)        {1, 2, 3},
    [](arrays.html#cb110-16)        {4, 5, 6}
    [](arrays.html#cb110-17)    };
    [](arrays.html#cb110-18)
    [](arrays.html#cb110-19)    print_2D_array(x);
    [](arrays.html#cb110-20)}

But in this case, these two[63](function-specifiers-alignment-specifiersoperators.html#fn63) are equivalent:
    
    
    [](arrays.html#cb111-1)void print_2D_array(int a[2][3])
    [](arrays.html#cb111-2)void print_2D_array(int a[][3])

The compiler really only needs the second dimension so it can figure out how far in memory to skip for each increment of the first dimension. In general, it needs to know all the dimensions except the first one.

Also, remember that the compiler does minimal compile-time bounds checking (if you’re lucky), and C does zero runtime checking of bounds. No seat belts! Don’t crash by accessing array elements out of bounds! 

* * *

[Prev](pointers.html) | [Contents](index.html) | [Next](strings.html)
