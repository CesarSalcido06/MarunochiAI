[Prev](typedef-making-new-types.html) | [Contents](index.html) | [Next](manual-memory-allocation.html)

* * *

# 11 Pointers II: Arithmetic

Time to get more into it with a number of new pointer topics! If you’re not up to speed with pointers, [check out the first section in the guide on the matter](pointers.html#pointers).

## 11.1 Pointer Arithmetic

Turns out you can do math on pointers, notably addition and subtraction.

But what does it mean when you do that?

In short, if you have a pointer to a type, adding one to the pointer moves to the next item of that type directly after it in memory.

It’s **important** to remember that as we move pointers around and look at different places in memory, we need to make sure that we’re always pointing to a valid place in memory before we dereference. If we’re off in the weeds and we try to see what’s there, the behavior is undefined and a crash is a common result.

This is a little chicken-and-eggy with [Array/Pointer Equivalence, below](pointers2.html#arraypointerequiv), but we’re going to give it a shot, anyway.

### 11.1.1 Adding to Pointers

First, let’s take an array of numbers.
    
    
    [](pointers2.html#cb172-1)int a[5] = {11, 22, 33, 44, 55};

Then let’s get a pointer to the first element in that array:
    
    
    [](pointers2.html#cb173-1)int a[5] = {11, 22, 33, 44, 55};
    [](pointers2.html#cb173-2)
    [](pointers2.html#cb173-3)int *p = &a[0];  // Or "int *p = a;" works just as well

Then let’s print the value there by dereferencing the pointer:
    
    
    [](pointers2.html#cb174-1)printf("%d\n", *p);  // Prints 11

Now let’s use pointer arithmetic to print the next element in the array, the one at index 1:
    
    
    [](pointers2.html#cb175-1)printf("%d\n", *(p + 1));  // Prints 22!!

What happened there? C knows that `p` is a pointer to an `int`. So it knows the `sizeof` an `int`[84](function-specifiers-alignment-specifiersoperators.html#fn84) and it knows to skip that many bytes to get to the next `int` after the first one!

In fact, the prior example could be written these two equivalent ways:
    
    
    [](pointers2.html#cb176-1)printf("%d\n", *p);        // Prints 11
    [](pointers2.html#cb176-2)printf("%d\n", *(p + 0));  // Prints 11

because adding `0` to a pointer results in the same pointer.

Let’s think of the upshot here. We can iterate over elements of an array this way instead of using an array:
    
    
    [](pointers2.html#cb177-1)int a[5] = {11, 22, 33, 44, 55};
    [](pointers2.html#cb177-2)
    [](pointers2.html#cb177-3)int *p = &a[0];  // Or "int *p = a;" works just as well
    [](pointers2.html#cb177-4)
    [](pointers2.html#cb177-5)for (int i = 0; i < 5; i++) {
    [](pointers2.html#cb177-6)    printf("%d\n", *(p + i));  // Same as p[i]!
    [](pointers2.html#cb177-7)}

And that works the same as if we used array notation! Oooo! Getting closer to that array/pointer equivalence thing! More on this later in this chapter.

But what’s actually happening, here? How does it work?

Remember from early on that memory is like a big array, where a byte is stored at each array index?

And the array index into memory has a few names:

  * Index into memory
  * Location
  * Address
  * _Pointer!_



So a pointer is an index into memory, somewhere.

For a random example, say that a number 3490 was stored at address (“index”) 23,237,489,202. If we have an `int` pointer to that 3490, that value of that pointer is 23,237,489,202… because the pointer is the memory address. Different words for the same thing.

And now let’s say we have another number, 4096, stored right after the 3490 at address 23,237,489,210 (8 higher than the 3490 because each `int` in this example is 8 bytes long).

If we add `1` to that pointer, it actually jumps ahead `sizeof(int)` bytes to the next `int`. It knows to jump that far ahead because it’s an `int` pointer. If it were a `float` pointer, it’d jump `sizeof(float)` bytes ahead to get to the next float!

So you can look at the next `int`, by adding `1` to the pointer, the one after that by adding `2` to the pointer, and so on.

### 11.1.2 Changing Pointers

We saw how we could add an integer to a pointer in the previous section. This time, let’s _modify the pointer, itself_.

You can just add (or subtract) integer values directly to (or from) any pointer!

Let’s do that example again, except with a couple changes. First, I’m going to add a `999` to the end of our numbers to act as a sentinel value. This will let us know where the end of the data is.
    
    
    [](pointers2.html#cb178-1)int a[] = {11, 22, 33, 44, 55, 999};  // Add 999 here as a sentinel
    [](pointers2.html#cb178-2)
    [](pointers2.html#cb178-3)int *p = &a[0];  // p points to the 11

And we also have `p` pointing to the element at index `0` of `a`, namely `11`, just like before.

Now—let’s start _incrementing_ `p` so that it points at subsequent elements of the array. We’ll do this until `p` points to the `999`; that is, we’ll do it until `*p == 999`:
    
    
    [](pointers2.html#cb179-1)while (*p != 999) {       // While the thing p points to isn't 999
    [](pointers2.html#cb179-2)    printf("%d\n", *p);   // Print it
    [](pointers2.html#cb179-3)    p++;                  // Move p to point to the next int!
    [](pointers2.html#cb179-4)}

Pretty crazy, right?

When we give it a run, first `p` points to `11`. Then we increment `p`, and it points to `22`, and then again, it points to `33`. And so on, until it points to `999` and we quit.

### 11.1.3 Subtracting Pointers

You can subtract a value from a pointer to get to earlier address, as well, just like we were adding to them before.

But we can also subtract two pointers to find the difference between them, e.g. we can calculate how many `int`s there are between two `int*`s. The catch is that this only works within a single array[85](function-specifiers-alignment-specifiersoperators.html#fn85)—if the pointers point to anything else, you get undefined behavior.

Remember how strings are `char*`s in C? Let’s see if we can use this to write another variant of `strlen()` to compute the length of a string that utilizes pointer subtraction.

The idea is that if we have a pointer to the beginning of the string, we can find a pointer to the end of the string by scanning ahead for the `NUL` character.

And if we have a pointer to the beginning of the string, and we computed the pointer to the end of the string, we can just subtract the two pointers to come up with the length!
    
    
    [](pointers2.html#cb180-1)#include <stdio.h>
    [](pointers2.html#cb180-2)
    [](pointers2.html#cb180-3)int my_strlen(char *s)
    [](pointers2.html#cb180-4){
    [](pointers2.html#cb180-5)    // Start scanning from the beginning of the string
    [](pointers2.html#cb180-6)    char *p = s;
    [](pointers2.html#cb180-7)
    [](pointers2.html#cb180-8)    // Scan until we find the NUL character
    [](pointers2.html#cb180-9)    while (*p != '\0')
    [](pointers2.html#cb180-10)        p++;
    [](pointers2.html#cb180-11)
    [](pointers2.html#cb180-12)    // Return the difference in pointers
    [](pointers2.html#cb180-13)    return p - s;
    [](pointers2.html#cb180-14)}
    [](pointers2.html#cb180-15)
    [](pointers2.html#cb180-16)int main(void)
    [](pointers2.html#cb180-17){
    [](pointers2.html#cb180-18)    printf("%d\n", my_strlen("Hello, world!"));  // Prints "13"
    [](pointers2.html#cb180-19)}

Remember that you can only use pointer subtraction between two pointers that point to the same array! 

## 11.2 Array/Pointer Equivalence

We’re finally ready to talk about this! We’ve seen plenty of examples of places where we’ve intermixed array notation, but let’s give out the _fundamental formula of array/pointer equivalence_ :
    
    
    [](pointers2.html#cb181-1)a[b] == *(a + b)

Study that! Those are equivalent and can be used interchangeably!

I’ve oversimplified a bit, because in my above example `a` and `b` can both be expressions, and we might want a few more parentheses to force order of operations in case the expressions are complex.

The spec is specific, as always, declaring (in C11 §6.5.2.1¶2):

> `E1[E2]` is identical to `(*((E1)+(E2)))`

but that’s a little harder to grok. Just make sure you include parentheses if the expressions are complicated so all your math happens in the right order.

This means we can _decide_ if we’re going to use array or pointer notation for any array or pointer (assuming it points to an element of an array).

Let’s use an array and pointer with both array and pointer notation:
    
    
    [](pointers2.html#cb182-1)#include <stdio.h>
    [](pointers2.html#cb182-2)
    [](pointers2.html#cb182-3)int main(void)
    [](pointers2.html#cb182-4){
    [](pointers2.html#cb182-5)    int a[] = {11, 22, 33, 44, 55};
    [](pointers2.html#cb182-6)
    [](pointers2.html#cb182-7)    int *p = a;  // p points to the first element of a, 11
    [](pointers2.html#cb182-8)
    [](pointers2.html#cb182-9)    // Print all elements of the array a variety of ways:
    [](pointers2.html#cb182-10)
    [](pointers2.html#cb182-11)    for (int i = 0; i < 5; i++)
    [](pointers2.html#cb182-12)        printf("%d\n", a[i]);      // Array notation with a
    [](pointers2.html#cb182-13)
    [](pointers2.html#cb182-14)    for (int i = 0; i < 5; i++)
    [](pointers2.html#cb182-15)        printf("%d\n", p[i]);      // Array notation with p
    [](pointers2.html#cb182-16)
    [](pointers2.html#cb182-17)    for (int i = 0; i < 5; i++)
    [](pointers2.html#cb182-18)        printf("%d\n", *(a + i));  // Pointer notation with a
    [](pointers2.html#cb182-19)
    [](pointers2.html#cb182-20)    for (int i = 0; i < 5; i++)
    [](pointers2.html#cb182-21)        printf("%d\n", *(p + i));  // Pointer notation with p
    [](pointers2.html#cb182-22)
    [](pointers2.html#cb182-23)    for (int i = 0; i < 5; i++)
    [](pointers2.html#cb182-24)        printf("%d\n", *(p++));    // Moving pointer p
    [](pointers2.html#cb182-25)        //printf("%d\n", *(a++));    // Moving array variable a--ERROR!
    [](pointers2.html#cb182-26)}

So you can see that in general, if you have an array variable, you can use pointer or array notion to access elements. Same with a pointer variable.

The one big difference is that you can _modify_ a pointer to point to a different address, but you can’t do that with an array variable.  In other words, you can’t assign into an array variable at all—only into individual elements of that array.

If you really want to copy one array to another, you have to use a function like `memcpy()` (or a loop) to make that happen.

### 11.2.1 Array/Pointer Equivalence in Function Calls

This is where you’ll encounter this concept the most, for sure.

If you have a function that takes a pointer argument, e.g.:
    
    
    [](pointers2.html#cb183-1)int my_strlen(char *s)

this means you can pass either an array or a pointer to this function and have it work!
    
    
    [](pointers2.html#cb184-1)char s[] = "Antelopes";
    [](pointers2.html#cb184-2)char *t = "Wombats";
    [](pointers2.html#cb184-3)
    [](pointers2.html#cb184-4)printf("%d\n", my_strlen(s));  // Works!
    [](pointers2.html#cb184-5)printf("%d\n", my_strlen(t));  // Works, too!

And it’s also why these two function signatures are equivalent:
    
    
    [](pointers2.html#cb185-1)int my_strlen(char *s)    // Works!
    [](pointers2.html#cb185-2)int my_strlen(char s[])   // Works, too!

## 11.3 `void` Pointers

You’ve already seen the `void` keyword used with functions that indicates no parameters or no return value, but this is an entirely separate, unrelated animal.

A `void*` is definitely a pointer to an existing _thing_. But the `void` part of it indicates that we don’t know the _type_ of the thing. And sometimes, believe it or not, that’s really useful. It enables us to write code that’s a little more type-agnostic, which is some nice flexibility to have in a typed language like C.

There are basically two use cases for this—let’s check them out and see if we can demystify it a bit.

  1. A function is going to operate on something byte-by-byte. For example, `memcpy()` copies bytes of memory from one pointer to another, but those pointers can point to any type. `memcpy()` takes advantage of the fact that if you iterate through `char*`s, you’re iterating through the bytes of an object no matter what type the object is. More on this in the [Multibyte Values](pointers-iii-pointers-to-pointers-and-more.html#multibyte-values) subsection.

  2. Another function is calling a function you passed to it (a callback), and it’s passing you data. You know the type of the data, but the function calling you doesn’t. So it passes you `void*`s—’cause it doesn’t know the type—and you convert those to the type you need. The built-in [`qsort()`](https://beej.us/guide/bgclr/html/split/stdlib.html#man-qsort)[86](function-specifiers-alignment-specifiersoperators.html#fn86) and [`bsearch()`](https://beej.us/guide/bgclr/html/split/stdlib.html#man-bsearch)[87](function-specifiers-alignment-specifiersoperators.html#fn87) use this technique.




Let’s look at an example, the built-in `memcpy()` function:
    
    
    [](pointers2.html#cb186-1)void *memcpy(void *s1, void *s2, size_t n);

This function copies `n` bytes of memory starting from address `s2` into the memory starting at address `s1`.

But look! `s1` and `s2` are `void*`s! Why? What does it mean? Let’s run more examples to see.

For instance, we could copy a string with `memcpy()` (though `strcpy()` is more appropriate for strings):
    
    
    [](pointers2.html#cb187-1)#include <stdio.h>
    [](pointers2.html#cb187-2)#include <string.h>
    [](pointers2.html#cb187-3)
    [](pointers2.html#cb187-4)int main(void)
    [](pointers2.html#cb187-5){
    [](pointers2.html#cb187-6)    char s[] = "Goats!";
    [](pointers2.html#cb187-7)    char t[100];
    [](pointers2.html#cb187-8)
    [](pointers2.html#cb187-9)    memcpy(t, s, 7);  // Copy 7 bytes--including the NUL terminator!
    [](pointers2.html#cb187-10)
    [](pointers2.html#cb187-11)    printf("%s\n", t);  // "Goats!"
    [](pointers2.html#cb187-12)}

Or we can copy some `int`s:
    
    
    [](pointers2.html#cb188-1)#include <stdio.h>
    [](pointers2.html#cb188-2)#include <string.h>
    [](pointers2.html#cb188-3)
    [](pointers2.html#cb188-4)int main(void)
    [](pointers2.html#cb188-5){
    [](pointers2.html#cb188-6)    int a[] = {11, 22, 33};
    [](pointers2.html#cb188-7)    int b[3];
    [](pointers2.html#cb188-8)
    [](pointers2.html#cb188-9)    memcpy(b, a, 3 * sizeof(int));  // Copy 3 ints of data
    [](pointers2.html#cb188-10)
    [](pointers2.html#cb188-11)    printf("%d\n", b[1]);  // 22
    [](pointers2.html#cb188-12)}

That one’s a little wild—you see what we did there with `memcpy()`? We copied the data from `a` to `b`, but we had to specify how many _bytes_ to copy, and an `int` is more than one byte.

OK, then—how many bytes does an `int` take? Answer: depends on the system. But we can tell how many bytes any type takes with the `sizeof` operator.

So there’s the answer: an `int` takes `sizeof(int)` bytes of memory to store.

And if we have 3 of them in our array, like we did in that example, the entire space used for the 3 `int`s must be `3 * sizeof(int)`.

(In the string example, earlier, it would have been more technically accurate to copy `7 * sizeof(char)` bytes. But `char`s are always one byte large, by definition, so that just devolves into `7 * 1`.)

We could even copy a `float` or a `struct` with `memcpy()`! (Though this is abusive—we should just use `=` for that):
    
    
    [](pointers2.html#cb189-1)struct antelope my_antelope;
    [](pointers2.html#cb189-2)struct antelope my_clone_antelope;
    [](pointers2.html#cb189-3)
    [](pointers2.html#cb189-4)// ...
    [](pointers2.html#cb189-5)
    [](pointers2.html#cb189-6)memcpy(&my_clone_antelope, &my_antelope, sizeof my_antelope);

Look at how versatile `memcpy()` is! If you have a pointer to a source and a pointer to a destination, and you have the number of bytes you want to copy, you can copy _any type of data_.

Imagine if we didn’t have `void*`. We’d have to write specialized `memcpy()` functions for each type:
    
    
    [](pointers2.html#cb190-1)memcpy_int(int *a, int *b, int count);
    [](pointers2.html#cb190-2)memcpy_float(float *a, float *b, int count);
    [](pointers2.html#cb190-3)memcpy_double(double *a, double *b, int count);
    [](pointers2.html#cb190-4)memcpy_char(char *a, char *b, int count);
    [](pointers2.html#cb190-5)memcpy_unsigned_char(unsigned char *a, unsigned char *b, int count);
    [](pointers2.html#cb190-6)
    [](pointers2.html#cb190-7)// etc... blech!

Much better to just use `void*` and have one function that can do it all.

That’s the power of `void*`. You can write a function that doesn’t care about the variable’s type and is still able to do things with it.

But with great power comes great responsibility. Maybe not _that_ great in this case, but there are some limits.

  1. You cannot do pointer arithmetic on a `void*`.
  2. You cannot dereference a `void*`.
  3. You cannot use the arrow operator on a `void*`, since it’s also a dereference.
  4. You cannot use array notation on a `void*`, since it’s also a dereference, as well[88](function-specifiers-alignment-specifiersoperators.html#fn88).



And if you think about it, these rules make sense. All those operations rely on knowing the `sizeof` the type of data pointed to, and with `void*`, we don’t know the size of the data being pointed to—it could be anything!

But wait—if you can’t dereference a `void*` what good can it ever do you?

Like with `memcpy()`, it helps you write generic functions that can handle multiple types of data. But the secret is that, deep down, _you convert the`void*` to another type before you use it_!

And conversion is easy: you can just assign into a variable of the desired type[89](function-specifiers-alignment-specifiersoperators.html#fn89).
    
    
    [](pointers2.html#cb191-1)char a = 'X';  // A single char
    [](pointers2.html#cb191-2)
    [](pointers2.html#cb191-3)void *p = &a;  // p points to the 'X'
    [](pointers2.html#cb191-4)char *q = p;   // q also points to the 'X'
    [](pointers2.html#cb191-5)
    [](pointers2.html#cb191-6)printf("%c\n", *p);  // ERROR--cannot dereference void*!
    [](pointers2.html#cb191-7)printf("%c\n", *q);  // Prints "X"

Let’s write our own `memcpy()` to try this out. We can copy bytes (`char`s), and we know the number of bytes because it’s passed in.
    
    
    [](pointers2.html#cb192-1)void *my_memcpy(void *dest, void *src, int byte_count)
    [](pointers2.html#cb192-2){
    [](pointers2.html#cb192-3)    // Convert void*s to char*s
    [](pointers2.html#cb192-4)    char *s = src, *d = dest;
    [](pointers2.html#cb192-5)
    [](pointers2.html#cb192-6)    // Now that we have char*s, we can dereference and copy them
    [](pointers2.html#cb192-7)    while (byte_count--) {
    [](pointers2.html#cb192-8)        *d++ = *s++;
    [](pointers2.html#cb192-9)    }
    [](pointers2.html#cb192-10)
    [](pointers2.html#cb192-11)    // Most of these functions return the destination, just in case
    [](pointers2.html#cb192-12)    // that's useful to the caller.
    [](pointers2.html#cb192-13)    return dest;
    [](pointers2.html#cb192-14)}

Right there at the beginning, we copy the `void*`s into `char*`s so that we can use them as `char*`s. It’s as easy as that.

Then some fun in a while loop, where we decrement `byte_count` until it becomes false (`0`). Remember that with post-decrement, the value of the expression is computed (for `while` to use) and _then_ the variable is decremented.

And some fun in the copy, where we assign `*d = *s` to copy the byte, but we do it with post-increment so that both `d` and `s` move to the next byte after the assignment is made.

Lastly, most memory and string functions return a copy of a pointer to the destination just in case the caller wants to use it.

Now that we’ve done that, I just want to quickly point out that we can use this technique to iterate over the bytes of _any_ object in C, `float`s, `struct`s, or anything! 

Let’s run one more real-world example with the built-in `qsort()` routine that can sort _anything_ thanks to the magic of `void*`s.

(In the following example, you can ignore the word `const`, which we haven’t covered yet.)
    
    
    [](pointers2.html#cb193-1)#include <stdio.h>
    [](pointers2.html#cb193-2)#include <stdlib.h>
    [](pointers2.html#cb193-3)
    [](pointers2.html#cb193-4)// The type of structure we're going to sort
    [](pointers2.html#cb193-5)struct animal {
    [](pointers2.html#cb193-6)    char *name;
    [](pointers2.html#cb193-7)    int leg_count;
    [](pointers2.html#cb193-8)};
    [](pointers2.html#cb193-9)
    [](pointers2.html#cb193-10)// This is a comparison function called by qsort() to help it determine
    [](pointers2.html#cb193-11)// what exactly to sort by. We'll use it to sort an array of struct
    [](pointers2.html#cb193-12)// animals by leg_count.
    [](pointers2.html#cb193-13)int compar(const void *elem1, const void *elem2)
    [](pointers2.html#cb193-14){
    [](pointers2.html#cb193-15)    // We know we're sorting struct animals, so let's make both
    [](pointers2.html#cb193-16)    // arguments pointers to struct animals
    [](pointers2.html#cb193-17)    const struct animal *animal1 = elem1;
    [](pointers2.html#cb193-18)    const struct animal *animal2 = elem2;
    [](pointers2.html#cb193-19)
    [](pointers2.html#cb193-20)    // Return <0 =0 or >0 depending on whatever we want to sort by.
    [](pointers2.html#cb193-21)
    [](pointers2.html#cb193-22)    // Let's sort ascending by leg_count, so we'll return the difference
    [](pointers2.html#cb193-23)    // in the leg_counts
    [](pointers2.html#cb193-24)    if (animal1->leg_count > animal2->leg_count)
    [](pointers2.html#cb193-25)        return 1;
    [](pointers2.html#cb193-26)    
    [](pointers2.html#cb193-27)    if (animal1->leg_count < animal2->leg_count)
    [](pointers2.html#cb193-28)        return -1;
    [](pointers2.html#cb193-29)
    [](pointers2.html#cb193-30)    return 0;
    [](pointers2.html#cb193-31)}
    [](pointers2.html#cb193-32)
    [](pointers2.html#cb193-33)int main(void)
    [](pointers2.html#cb193-34){
    [](pointers2.html#cb193-35)    // Let's build an array of 4 struct animals with different
    [](pointers2.html#cb193-36)    // characteristics. This array is out of order by leg_count, but
    [](pointers2.html#cb193-37)    // we'll sort it in a second.
    [](pointers2.html#cb193-38)    struct animal a[4] = {
    [](pointers2.html#cb193-39)        {.name="Dog", .leg_count=4},
    [](pointers2.html#cb193-40)        {.name="Monkey", .leg_count=2},
    [](pointers2.html#cb193-41)        {.name="Antelope", .leg_count=4},
    [](pointers2.html#cb193-42)        {.name="Snake", .leg_count=0}
    [](pointers2.html#cb193-43)    };
    [](pointers2.html#cb193-44)
    [](pointers2.html#cb193-45)    // Call qsort() to sort the array. qsort() needs to be told exactly
    [](pointers2.html#cb193-46)    // what to sort this data by, and we'll do that inside the compar()
    [](pointers2.html#cb193-47)    // function.
    [](pointers2.html#cb193-48)    //
    [](pointers2.html#cb193-49)    // This call is saying: qsort array a, which has 4 elements, and
    [](pointers2.html#cb193-50)    // each element is sizeof(struct animal) bytes big, and this is the
    [](pointers2.html#cb193-51)    // function that will compare any two elements.
    [](pointers2.html#cb193-52)    qsort(a, 4, sizeof(struct animal), compar);
    [](pointers2.html#cb193-53)
    [](pointers2.html#cb193-54)    // Print them all out
    [](pointers2.html#cb193-55)    for (int i = 0; i < 4; i++) {
    [](pointers2.html#cb193-56)        printf("%d: %s\n", a[i].leg_count, a[i].name);
    [](pointers2.html#cb193-57)    }
    [](pointers2.html#cb193-58)}

As long as you give `qsort()` a function that can compare two items that you have in your array to be sorted, it can sort anything. And it does this without needing to have the types of the items hardcoded in there anywhere. `qsort()` just rearranges blocks of bytes based on the results of the `compar()` function you passed in. 

* * *

[Prev](typedef-making-new-types.html) | [Contents](index.html) | [Next](manual-memory-allocation.html)
