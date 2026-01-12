[Prev](signal-handling.html) | [Contents](index.html) | [Next](goto.html)

* * *

# 30 Variable-Length Arrays (VLAs)

C provides a way for you to declare an array whose size is determined at runtime. This gives you the benefits of dynamic runtime sizing like you get with `malloc()`, but without needing to worry about `free()`ing the memory after.

Now, a lot of people don’t like VLAs. They’ve been banned from the Linux kernel, for example. We’ll dig into more of that rationale [later](variable-length-arrays-vlas.html#vla-general-issues).

This is an optional feature of the language. The macro `__STDC_NO_VLA__` is set to `1` if VLAs are _not_ present. (They were mandatory in C99, and then became optional in C11.)
    
    
    [](variable-length-arrays-vlas.html#cb592-1)#if __STDC_NO_VLA__ == 1
    [](variable-length-arrays-vlas.html#cb592-2)   #error Sorry, need VLAs for this program!
    [](variable-length-arrays-vlas.html#cb592-3)#endif

But since neither GCC nor Clang bother to define this macro, you may get limited mileage from this.

Let’s dive in first with an example, and then we’ll look for the devil in the details.

## 30.1 The Basics

A normal array is declared with a constant size, like this:
    
    
    [](variable-length-arrays-vlas.html#cb593-1)int v[10];

But with VLAs, we can use a size determined at runtime to set the array, like this:
    
    
    [](variable-length-arrays-vlas.html#cb594-1)int n = 10;
    [](variable-length-arrays-vlas.html#cb594-2)int v[n];

Now, that looks like the same thing, and in many ways is, but this gives you the flexibility to compute the size you need, and then get an array of exactly that size.

Let’s ask the user to input the size of the array, and then store the index-times-10 in each of those array elements:
    
    
    [](variable-length-arrays-vlas.html#cb595-1)#include <stdio.h>
    [](variable-length-arrays-vlas.html#cb595-2)
    [](variable-length-arrays-vlas.html#cb595-3)int main(void)
    [](variable-length-arrays-vlas.html#cb595-4){
    [](variable-length-arrays-vlas.html#cb595-5)    int n;
    [](variable-length-arrays-vlas.html#cb595-6)    char buf[32];
    [](variable-length-arrays-vlas.html#cb595-7)
    [](variable-length-arrays-vlas.html#cb595-8)    printf("Enter a number: "); fflush(stdout);
    [](variable-length-arrays-vlas.html#cb595-9)    fgets(buf, sizeof buf, stdin);
    [](variable-length-arrays-vlas.html#cb595-10)    n = strtoul(buf, NULL, 10);
    [](variable-length-arrays-vlas.html#cb595-11)
    [](variable-length-arrays-vlas.html#cb595-12)    int v[n];
    [](variable-length-arrays-vlas.html#cb595-13)
    [](variable-length-arrays-vlas.html#cb595-14)    for (int i = 0; i < n; i++)
    [](variable-length-arrays-vlas.html#cb595-15)        v[i] = i * 10;
    [](variable-length-arrays-vlas.html#cb595-16)
    [](variable-length-arrays-vlas.html#cb595-17)    for (int i = 0; i < n; i++)
    [](variable-length-arrays-vlas.html#cb595-18)        printf("v[%d] = %d\n", i, v[i]);
    [](variable-length-arrays-vlas.html#cb595-19)}

(On line 7, I have an `fflush()` that should force the line to output even though I don’t have a newline at the end.)

Line 12 is where we declare the VLA—once execution gets past that line, the size of the array is set to whatever `n` was at that moment. The array length can’t be changed later.

You can put an expression in the brackets, as well:
    
    
    [](variable-length-arrays-vlas.html#cb596-1)int v[x * 100];

Some restrictions:

  * You can’t declare a VLA at file scope, and you can’t make a `static` one in block scope[175](function-specifiers-alignment-specifiersoperators.html#fn175).
  * You can’t use an initializer list to initialize the array.



Also, entering a negative value for the size of the array invokes undefined behavior—in this universe, anyway.

## 30.2 `sizeof` and VLAs

We’re used to `sizeof` giving us the size in bytes of any particular object, including arrays. And VLAs are no exception.

The main difference is that `sizeof` on a VLA is executed at _runtime_ , whereas on a non-variably-sized variable it is computed at _compile time_.

But the usage is the same.

You can even compute the number of elements in a VLA with the usual array trick:
    
    
    [](variable-length-arrays-vlas.html#cb597-1)size_t num_elems = sizeof v / sizeof v[0];

There’s a subtle and correct implication from the above line: pointer arithmetic works just like you’d expect for a regular array. So go ahead and use it to your heart’s content:
    
    
    [](variable-length-arrays-vlas.html#cb598-1)#include <stdio.h>
    [](variable-length-arrays-vlas.html#cb598-2)
    [](variable-length-arrays-vlas.html#cb598-3)int main(void)
    [](variable-length-arrays-vlas.html#cb598-4){
    [](variable-length-arrays-vlas.html#cb598-5)    int n = 5;
    [](variable-length-arrays-vlas.html#cb598-6)    int v[n];
    [](variable-length-arrays-vlas.html#cb598-7)
    [](variable-length-arrays-vlas.html#cb598-8)    int *p = v;
    [](variable-length-arrays-vlas.html#cb598-9)
    [](variable-length-arrays-vlas.html#cb598-10)    *(p+2) = 12;
    [](variable-length-arrays-vlas.html#cb598-11)    printf("%d\n", v[2]);  // 12
    [](variable-length-arrays-vlas.html#cb598-12)
    [](variable-length-arrays-vlas.html#cb598-13)    p[3] = 34;
    [](variable-length-arrays-vlas.html#cb598-14)    printf("%d\n", v[3]);  // 34
    [](variable-length-arrays-vlas.html#cb598-15)}

Like with regular arrays, you can use parentheses with `sizeof()` to get the size of a would-be VLA without actually declaring one:
    
    
    [](variable-length-arrays-vlas.html#cb599-1)int x = 12;
    [](variable-length-arrays-vlas.html#cb599-2)
    [](variable-length-arrays-vlas.html#cb599-3)printf("%zu\n", sizeof(int [x]));  // Prints 48 on my system

## 30.3 Multidimensional VLAs

You can go ahead and make all kinds of VLAs with one or more dimensions set to a variable
    
    
    [](variable-length-arrays-vlas.html#cb600-1)int w = 10;
    [](variable-length-arrays-vlas.html#cb600-2)int h = 20;
    [](variable-length-arrays-vlas.html#cb600-3)
    [](variable-length-arrays-vlas.html#cb600-4)int x[h][w];
    [](variable-length-arrays-vlas.html#cb600-5)int y[5][w];
    [](variable-length-arrays-vlas.html#cb600-6)int z[10][w][20];

Again, you can navigate these just like you would a regular array.

## 30.4 Passing One-Dimensional VLAs to Functions

Passing single-dimensional VLAs into a function can be no different than passing a regular array in. You just go for it.
    
    
    [](variable-length-arrays-vlas.html#cb601-1)#include <stdio.h>
    [](variable-length-arrays-vlas.html#cb601-2)
    [](variable-length-arrays-vlas.html#cb601-3)int sum(int count, int *v)
    [](variable-length-arrays-vlas.html#cb601-4){
    [](variable-length-arrays-vlas.html#cb601-5)    int total = 0;
    [](variable-length-arrays-vlas.html#cb601-6)
    [](variable-length-arrays-vlas.html#cb601-7)    for (int i = 0; i < count; i++)
    [](variable-length-arrays-vlas.html#cb601-8)        total += v[i];
    [](variable-length-arrays-vlas.html#cb601-9)
    [](variable-length-arrays-vlas.html#cb601-10)    return total;
    [](variable-length-arrays-vlas.html#cb601-11)}
    [](variable-length-arrays-vlas.html#cb601-12)
    [](variable-length-arrays-vlas.html#cb601-13)int main(void)
    [](variable-length-arrays-vlas.html#cb601-14){
    [](variable-length-arrays-vlas.html#cb601-15)    int x[5];   // Standard array
    [](variable-length-arrays-vlas.html#cb601-16)
    [](variable-length-arrays-vlas.html#cb601-17)    int a = 5;
    [](variable-length-arrays-vlas.html#cb601-18)    int y[a];   // VLA
    [](variable-length-arrays-vlas.html#cb601-19)
    [](variable-length-arrays-vlas.html#cb601-20)    for (int i = 0; i < a; i++)
    [](variable-length-arrays-vlas.html#cb601-21)        x[i] = y[i] = i + 1;
    [](variable-length-arrays-vlas.html#cb601-22)
    [](variable-length-arrays-vlas.html#cb601-23)    printf("%d\n", sum(5, x));
    [](variable-length-arrays-vlas.html#cb601-24)    printf("%d\n", sum(a, y));
    [](variable-length-arrays-vlas.html#cb601-25)}

But there’s a bit more to it than that. You can also let C know that the array is a specific VLA size by passing that in first and then giving that dimension in the parameter list:
    
    
    [](variable-length-arrays-vlas.html#cb602-1)int sum(int count, int v[count])
    [](variable-length-arrays-vlas.html#cb602-2){
    [](variable-length-arrays-vlas.html#cb602-3)    // ...
    [](variable-length-arrays-vlas.html#cb602-4)}

Incidentally, there are a couple ways of listing a prototype for the above function; one of them involves an `*` if you don’t want to specifically name the value in the VLA. It just indicates that the type is a VLA as opposed to a regular pointer.

VLA prototypes:
    
    
    [](variable-length-arrays-vlas.html#cb603-1)void do_something(int count, int v[count]);  // With names
    [](variable-length-arrays-vlas.html#cb603-2)void do_something(int, int v[*]);            // Without names

Again, that `*` thing only works with the prototype—in the function itself, you’ll have to put the explicit size.

Now— _let’s get multidimensional_! This is where the fun begins.

## 30.5 Passing Multi-Dimensional VLAs to Functions

Same thing as we did with the second form of one-dimensional VLAs, above, but this time we’re passing in two dimensions and using those.

In the following example, we build a multiplication table matrix of a variable width and height, and then pass it to a function to print it out.
    
    
    [](variable-length-arrays-vlas.html#cb604-1)#include <stdio.h>
    [](variable-length-arrays-vlas.html#cb604-2)
    [](variable-length-arrays-vlas.html#cb604-3)void print_matrix(int h, int w, int m[h][w])
    [](variable-length-arrays-vlas.html#cb604-4){
    [](variable-length-arrays-vlas.html#cb604-5)    for (int row = 0; row < h; row++) {
    [](variable-length-arrays-vlas.html#cb604-6)        for (int col = 0; col < w; col++)
    [](variable-length-arrays-vlas.html#cb604-7)            printf("%2d ", m[row][col]);
    [](variable-length-arrays-vlas.html#cb604-8)        printf("\n");
    [](variable-length-arrays-vlas.html#cb604-9)    }
    [](variable-length-arrays-vlas.html#cb604-10)}
    [](variable-length-arrays-vlas.html#cb604-11)
    [](variable-length-arrays-vlas.html#cb604-12)int main(void)
    [](variable-length-arrays-vlas.html#cb604-13){
    [](variable-length-arrays-vlas.html#cb604-14)    int rows = 4;
    [](variable-length-arrays-vlas.html#cb604-15)    int cols = 7;
    [](variable-length-arrays-vlas.html#cb604-16)
    [](variable-length-arrays-vlas.html#cb604-17)    int matrix[rows][cols];
    [](variable-length-arrays-vlas.html#cb604-18)
    [](variable-length-arrays-vlas.html#cb604-19)    for (int row = 0; row < rows; row++)
    [](variable-length-arrays-vlas.html#cb604-20)        for (int col = 0; col < cols; col++)
    [](variable-length-arrays-vlas.html#cb604-21)            matrix[row][col] = row * col;
    [](variable-length-arrays-vlas.html#cb604-22)
    [](variable-length-arrays-vlas.html#cb604-23)    print_matrix(rows, cols, matrix);
    [](variable-length-arrays-vlas.html#cb604-24)}

### 30.5.1 Partial Multidimensional VLAs

You can have some of the dimensions fixed and some variable. Let’s say we have a record length fixed at 5 elements, but we don’t know how many records there are.
    
    
    [](variable-length-arrays-vlas.html#cb605-1)#include <stdio.h>
    [](variable-length-arrays-vlas.html#cb605-2)
    [](variable-length-arrays-vlas.html#cb605-3)void print_records(int count, int record[count][5])
    [](variable-length-arrays-vlas.html#cb605-4){
    [](variable-length-arrays-vlas.html#cb605-5)    for (int i = 0; i < count; i++) {
    [](variable-length-arrays-vlas.html#cb605-6)        for (int j = 0; j < 5; j++)
    [](variable-length-arrays-vlas.html#cb605-7)            printf("%2d ", record[i][j]);
    [](variable-length-arrays-vlas.html#cb605-8)        printf("\n");
    [](variable-length-arrays-vlas.html#cb605-9)    }
    [](variable-length-arrays-vlas.html#cb605-10)}
    [](variable-length-arrays-vlas.html#cb605-11)
    [](variable-length-arrays-vlas.html#cb605-12)int main(void)
    [](variable-length-arrays-vlas.html#cb605-13){
    [](variable-length-arrays-vlas.html#cb605-14)    int rec_count = 3;
    [](variable-length-arrays-vlas.html#cb605-15)    int records[rec_count][5];
    [](variable-length-arrays-vlas.html#cb605-16)
    [](variable-length-arrays-vlas.html#cb605-17)    // Fill with some dummy data
    [](variable-length-arrays-vlas.html#cb605-18)    for (int i = 0; i < rec_count; i++)
    [](variable-length-arrays-vlas.html#cb605-19)        for (int j = 0; j < 5; j++)
    [](variable-length-arrays-vlas.html#cb605-20)            records[i][j] = (i+1)*(j+2);
    [](variable-length-arrays-vlas.html#cb605-21)
    [](variable-length-arrays-vlas.html#cb605-22)    print_records(rec_count, records);
    [](variable-length-arrays-vlas.html#cb605-23)}

## 30.6 Compatibility with Regular Arrays

Because VLAs are just like regular arrays in memory, it’s perfectly permissible to pass them interchangeably… as long as the dimensions match.

For example, if we have a function that specifically wants a \\(3\times5\\) array, we can still pass a VLA into it.
    
    
    [](variable-length-arrays-vlas.html#cb606-1)int foo(int m[5][3]) {...}
    [](variable-length-arrays-vlas.html#cb606-2)
    [](variable-length-arrays-vlas.html#cb606-3)\\ ...
    [](variable-length-arrays-vlas.html#cb606-4)
    [](variable-length-arrays-vlas.html#cb606-5)int w = 3, h = 5;
    [](variable-length-arrays-vlas.html#cb606-6)int matrix[h][w];
    [](variable-length-arrays-vlas.html#cb606-7)
    [](variable-length-arrays-vlas.html#cb606-8)foo(matrix);   // OK!

Likewise, if you have a VLA function, you can pass a regular array into it:
    
    
    [](variable-length-arrays-vlas.html#cb607-1)int foo(int h, int w, int m[h][w]) {...}
    [](variable-length-arrays-vlas.html#cb607-2)
    [](variable-length-arrays-vlas.html#cb607-3)\\ ...
    [](variable-length-arrays-vlas.html#cb607-4)
    [](variable-length-arrays-vlas.html#cb607-5)int matrix[3][5];
    [](variable-length-arrays-vlas.html#cb607-6)
    [](variable-length-arrays-vlas.html#cb607-7)foo(3, 5, matrix);   // OK!

Beware, though: if your dimensions mismatch, you’re going to have some undefined behavior going on, likely.

## 30.7 `typedef` and VLAs

You can `typedef` a VLA, but the behavior might not be as you expect.

Basically, `typedef` makes a new type with the values as they existed the moment the `typedef` was executed.

So it’s not a `typedef` of a VLA so much as a new fixed size array type of the dimensions at the time.
    
    
    [](variable-length-arrays-vlas.html#cb608-1)#include <stdio.h>
    [](variable-length-arrays-vlas.html#cb608-2)
    [](variable-length-arrays-vlas.html#cb608-3)int main(void)
    [](variable-length-arrays-vlas.html#cb608-4){
    [](variable-length-arrays-vlas.html#cb608-5)    int w = 10;
    [](variable-length-arrays-vlas.html#cb608-6)
    [](variable-length-arrays-vlas.html#cb608-7)    typedef int goat[w];
    [](variable-length-arrays-vlas.html#cb608-8)
    [](variable-length-arrays-vlas.html#cb608-9)    // goat is an array of 10 ints
    [](variable-length-arrays-vlas.html#cb608-10)    goat x;
    [](variable-length-arrays-vlas.html#cb608-11)
    [](variable-length-arrays-vlas.html#cb608-12)    // Init with squares of numbers
    [](variable-length-arrays-vlas.html#cb608-13)    for (int i = 0; i < w; i++)
    [](variable-length-arrays-vlas.html#cb608-14)        x[i] = i*i;
    [](variable-length-arrays-vlas.html#cb608-15)
    [](variable-length-arrays-vlas.html#cb608-16)    // Print them
    [](variable-length-arrays-vlas.html#cb608-17)    for (int i = 0; i < w; i++)
    [](variable-length-arrays-vlas.html#cb608-18)        printf("%d\n", x[i]);
    [](variable-length-arrays-vlas.html#cb608-19)
    [](variable-length-arrays-vlas.html#cb608-20)    // Now let's change w...
    [](variable-length-arrays-vlas.html#cb608-21)
    [](variable-length-arrays-vlas.html#cb608-22)    w = 20;
    [](variable-length-arrays-vlas.html#cb608-23)
    [](variable-length-arrays-vlas.html#cb608-24)    // But goat is STILL an array of 10 ints, because that was the
    [](variable-length-arrays-vlas.html#cb608-25)    // value of w when the typedef executed.
    [](variable-length-arrays-vlas.html#cb608-26)}

So it acts like an array of fixed size.

But you still can’t use an initializer list on it.

## 30.8 Jumping Pitfalls

You have to watch out when using `goto` near VLAs because a lot of things aren’t legal.

And when you’re using `longjmp()` there’s a case where you could leak memory with VLAs.

But both of these things we’ll cover in their respective chapters.

## 30.9 General Issues

VLAs have been banned from the Linux kernel for a few reasons:

  * Lots of places they were used should have just been fixed-size.
  * The code behind VLAs is slower (to a degree that most people wouldn’t notice, but makes a difference in an operating system).
  * VLAs are not supported to the same degree by all C compilers.
  * Stack size is limited, and VLAs go on the stack. If some code accidentally (or maliciously) passes a large value into a kernel function that allocates a VLA, _Bad Things_ ™ could happen.



Other folks online point out that there’s no way to detect a VLA’s failure to allocate, and programs that suffered such problems would likely just crash. While fixed-size arrays also have the same issue, it’s far more likely that someone accidentally make a _VLA Of Unusual Size_ than somehow accidentally declare a fixed-size, say, 30 megabyte array.

* * *

[Prev](signal-handling.html) | [Contents](index.html) | [Next](goto.html)
