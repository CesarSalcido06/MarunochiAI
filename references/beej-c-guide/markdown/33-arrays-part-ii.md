[Prev](types-part-v-compound-literals-and-generic-selections.html) | [Contents](index.html) | [Next](setjmp-longjmp.html)

* * *

# 33 Arrays Part II

We’re going to go over a few extra misc things this chapter concerning arrays.

  * Type qualifiers with array parameters
  * The `static` keyword with array parameters
  * Partial multi-dimensional array initializers



They’re not super-commonly seen, but we’ll peek at them since they’re part of the newer spec.

## 33.1 Type Qualifiers for Arrays in Parameter Lists

If you recall from earlier, these two things are equivalent in function parameter lists:
    
    
    [](arrays-part-ii.html#cb656-1)int func(int *p) {...}
    [](arrays-part-ii.html#cb656-2)int func(int p[]) {...}

And you might also recall that you can add type qualifiers to a pointer variable like so:
    
    
    [](arrays-part-ii.html#cb657-1)int *const p;
    [](arrays-part-ii.html#cb657-2)int *volatile p;
    [](arrays-part-ii.html#cb657-3)int *const volatile p;
    [](arrays-part-ii.html#cb657-4)// etc.

But how can we do that when we’re using array notation in your parameter list?

Turns out it goes in the brackets. And you can put the optional count after. The two following lines are equivalent:
    
    
    [](arrays-part-ii.html#cb658-1)int func(int *const volatile p) {...}
    [](arrays-part-ii.html#cb658-2)int func(int p[const volatile]) {...}
    [](arrays-part-ii.html#cb658-3)int func(int p[const volatile 10]) {...}

If you have a multidimensional array, you need to put the type qualifiers in the first set of brackets.

## 33.2 `static` for Arrays in Parameter Lists

Similarly, you can use the keyword static in the array in a parameter list.

This is something I’ve never seen in the wild. It is **always** followed by a dimension:
    
    
    [](arrays-part-ii.html#cb659-1)int func(int p[static 4]) {...}

What this means, in the above example, is the compiler is going to assume that any array you pass to the function will be _at least_ 4 elements.

Anything else is undefined behavior.
    
    
    [](arrays-part-ii.html#cb660-1)int func(int p[static 4]) {...}
    [](arrays-part-ii.html#cb660-2)
    [](arrays-part-ii.html#cb660-3)int main(void)
    [](arrays-part-ii.html#cb660-4){
    [](arrays-part-ii.html#cb660-5)    int a[] = {11, 22, 33, 44};
    [](arrays-part-ii.html#cb660-6)    int b[] = {11, 22, 33, 44, 55};
    [](arrays-part-ii.html#cb660-7)    int c[] = {11, 22};
    [](arrays-part-ii.html#cb660-8)
    [](arrays-part-ii.html#cb660-9)    func(a);  // OK! a is 4 elements, the minimum
    [](arrays-part-ii.html#cb660-10)    func(b);  // OK! b is at least 4 elements
    [](arrays-part-ii.html#cb660-11)    func(c);  // Undefined behavior! c is under 4 elements!
    [](arrays-part-ii.html#cb660-12)}

This basically sets the minimum size array you can have.

Important note: there is nothing in the compiler that prohibits you from passing in a smaller array. The compiler probably won’t warn you, and it won’t detect it at runtime.

By putting `static` in there, you’re saying, “I double secret PROMISE that I will never pass in a smaller array than this.” And the compiler says, “Yeah, fine,” and trusts you to not do it.

And then the compiler can make certain code optimizations, safe in the knowledge that you, the programmer, will always do the right thing.

## 33.3 Equivalent Initializers

C is a little bit, shall we say, _flexible_ when it comes to array initializers.

We’ve already seen some of this, where any missing values are replaced with zero.

For example, we can initialize a 5 element array to `1,2,0,0,0` with this:
    
    
    [](arrays-part-ii.html#cb661-1)int a[5] = {1, 2};

Or set an array entirely to zero with:
    
    
    [](arrays-part-ii.html#cb662-1)int a[5] = {0};

But things get interesting when initializing multidimensional arrays.

Let’s make an array of 3 rows and 2 columns:
    
    
    [](arrays-part-ii.html#cb663-1)int a[3][2];

Let’s write some code to initialize it and print the result:
    
    
    [](arrays-part-ii.html#cb664-1)#include <stdio.h>
    [](arrays-part-ii.html#cb664-2)
    [](arrays-part-ii.html#cb664-3)int main(void)
    [](arrays-part-ii.html#cb664-4){
    [](arrays-part-ii.html#cb664-5)    int a[3][2] = {
    [](arrays-part-ii.html#cb664-6)        {1, 2},
    [](arrays-part-ii.html#cb664-7)        {3, 4},
    [](arrays-part-ii.html#cb664-8)        {5, 6}
    [](arrays-part-ii.html#cb664-9)    };
    [](arrays-part-ii.html#cb664-10)
    [](arrays-part-ii.html#cb664-11)    for (int row = 0; row < 3; row++) {
    [](arrays-part-ii.html#cb664-12)        for (int col = 0; col < 2; col++)
    [](arrays-part-ii.html#cb664-13)            printf("%d ", a[row][col]);
    [](arrays-part-ii.html#cb664-14)        printf("\n");
    [](arrays-part-ii.html#cb664-15)    }
    [](arrays-part-ii.html#cb664-16)}

And when we run it, we get the expected:
    
    
    [](arrays-part-ii.html#cb665-1)1 2
    [](arrays-part-ii.html#cb665-2)3 4
    [](arrays-part-ii.html#cb665-3)5 6

Let’s leave off some of the initializer elements and see they get set to zero:
    
    
    [](arrays-part-ii.html#cb666-1)    int a[3][2] = {
    [](arrays-part-ii.html#cb666-2)        {1, 2},
    [](arrays-part-ii.html#cb666-3)        {3},    // Left off the 4!
    [](arrays-part-ii.html#cb666-4)        {5, 6}
    [](arrays-part-ii.html#cb666-5)    };

which produces:
    
    
    [](arrays-part-ii.html#cb667-1)1 2
    [](arrays-part-ii.html#cb667-2)3 0
    [](arrays-part-ii.html#cb667-3)5 6

Now let’s leave off the entire last middle element:
    
    
    [](arrays-part-ii.html#cb668-1)    int a[3][2] = {
    [](arrays-part-ii.html#cb668-2)        {1, 2},
    [](arrays-part-ii.html#cb668-3)        // {3, 4},   // Just cut this whole thing out
    [](arrays-part-ii.html#cb668-4)        {5, 6}
    [](arrays-part-ii.html#cb668-5)    };

And now we get this, which might not be what you expect:
    
    
    [](arrays-part-ii.html#cb669-1)1 2
    [](arrays-part-ii.html#cb669-2)5 6
    [](arrays-part-ii.html#cb669-3)0 0

But if you stop to think about it, we only provided enough initializers for two rows, so they got used for the first two rows. And the remaining elements were initialized to zero.

So far so good. Generally, if we leave off parts of the initializer, the compiler sets the corresponding elements to `0`.

But let’s get _crazy_.
    
    
    [](arrays-part-ii.html#cb670-1)    int a[3][2] = { 1, 2, 3, 4, 5, 6 };

What—? That’s a 2D array, but it only has a 1D initializer!

Turns out that’s legal (though GCC will warn about it with the proper warnings turned on).

Basically, what it does is starts filling in elements in row 0, then row 1, then row 2 from left to right.

So when we print, it prints in order:
    
    
    [](arrays-part-ii.html#cb671-1)1 2
    [](arrays-part-ii.html#cb671-2)3 4
    [](arrays-part-ii.html#cb671-3)5 6

If we leave some off:
    
    
    [](arrays-part-ii.html#cb672-1)    int a[3][2] = { 1, 2, 3 };

they fill with `0`:
    
    
    [](arrays-part-ii.html#cb673-1)1 2
    [](arrays-part-ii.html#cb673-2)3 0
    [](arrays-part-ii.html#cb673-3)0 0

So if you want to fill the whole array with `0`, then go ahead and:
    
    
    [](arrays-part-ii.html#cb674-1)    int a[3][2] = {0};

But my recommendation is if you have a 2D array, use a 2D initializer. It just makes the code more readable. (Except for initializing the whole array with `0`, in which case it’s idiomatic to use `{0}` no matter the dimension of the array.)

* * *

[Prev](types-part-v-compound-literals-and-generic-selections.html) | [Contents](index.html) | [Next](setjmp-longjmp.html)
