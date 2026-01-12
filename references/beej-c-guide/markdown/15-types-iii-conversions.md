[Prev](types-ii-way-more-types.html) | [Contents](index.html) | [Next](types-iv-qualifiers-and-specifiers.html)

* * *

# 15 Types III: Conversions

In this chapter, we want to talk all about converting from one type to another. C has a variety of ways of doing this, and some might be a little different that you’re used to in other languages.

Before we talk about how to make conversions happen, let’s talk about how they work when they _do_ happen.

## 15.1 String Conversions

Unlike many languages, C doesn’t do string-to-number (and vice-versa) conversions in quite as streamlined a manner as it does numeric conversions.

For these, we’ll have to call functions to do the dirty work.

### 15.1.1 Numeric Value to String

When we want to convert a number to a string, we can use either `sprintf()` (pronounced _SPRINT-f_) or `snprintf()` (_s-n-print-f_)[107](function-specifiers-alignment-specifiersoperators.html#fn107)

These basically work like `printf()`, except they output to a string instead, and you can print that string later, or whatever.

For example, turning part of the value π into a string:
    
    
    [](types-iii-conversions.html#cb240-1)#include <stdio.h>
    [](types-iii-conversions.html#cb240-2)
    [](types-iii-conversions.html#cb240-3)int main(void)
    [](types-iii-conversions.html#cb240-4){
    [](types-iii-conversions.html#cb240-5)    char s[10];
    [](types-iii-conversions.html#cb240-6)    float f = 3.14159;
    [](types-iii-conversions.html#cb240-7)
    [](types-iii-conversions.html#cb240-8)    // Convert "f" to string, storing in "s", writing at most 10 characters
    [](types-iii-conversions.html#cb240-9)    // including the NUL terminator
    [](types-iii-conversions.html#cb240-10)
    [](types-iii-conversions.html#cb240-11)    snprintf(s, 10, "%f", f);
    [](types-iii-conversions.html#cb240-12)
    [](types-iii-conversions.html#cb240-13)    printf("String value: %s\n", s);  // String value: 3.141590
    [](types-iii-conversions.html#cb240-14)}

So you can use `%d` or `%u` like you’re used to for integers.

### 15.1.2 String to Numeric Value

There are a couple families of functions to do this in C. We’ll call these the `atoi` (pronounced _a-to-i_) family and the `strtol` (_stir-to-long_) family.

For basic conversion from a string to a number, try the `atoi` functions from `<stdlib.h>`. These have bad error-handling characteristics (including undefined behavior if you pass in a bad string), so use them carefully.

Function | Description  
---|---  
`atoi` | String to `int`  
`atof` | String to `float`  
`atol` | String to `long int`  
`atoll` | String to `long long int`  
  
Though the spec doesn’t cop to it, the `a` at the beginning of the function stands for [ASCII](https://en.wikipedia.org/wiki/ASCII)[108](function-specifiers-alignment-specifiersoperators.html#fn108), so really `atoi()` is “ASCII-to-integer”, but saying so today is a bit ASCII-centric.

Here’s an example converting a string to a `float`:
    
    
    [](types-iii-conversions.html#cb241-1)#include <stdio.h>
    [](types-iii-conversions.html#cb241-2)#include <stdlib.h>
    [](types-iii-conversions.html#cb241-3)
    [](types-iii-conversions.html#cb241-4)int main(void)
    [](types-iii-conversions.html#cb241-5){
    [](types-iii-conversions.html#cb241-6)    char *pi = "3.14159";
    [](types-iii-conversions.html#cb241-7)    float f;
    [](types-iii-conversions.html#cb241-8)
    [](types-iii-conversions.html#cb241-9)    f = atof(pi);
    [](types-iii-conversions.html#cb241-10)
    [](types-iii-conversions.html#cb241-11)    printf("%f\n", f);
    [](types-iii-conversions.html#cb241-12)}

But, like I said, we get undefined behavior from weird things like this:
    
    
    [](types-iii-conversions.html#cb242-1)int x = atoi("what");  // "What" ain't no number I ever heard of

(When I run that, I get `0` back, but you really shouldn’t count on that in any way. You could get something completely different.)

For better error handling characteristics, let’s check out all those `strtol` functions, also in `<stdlib.h>`. Not only that, but they convert to more types and more bases, too!

Function | Description  
---|---  
`strtol` | String to `long int`  
`strtoll` | String to `long long int`  
`strtoul` | String to `unsigned long int`  
`strtoull` | String to `unsigned long long int`  
`strtof` | String to `float`  
`strtod` | String to `double`  
`strtold` | String to `long double`  
  
These functions all follow a similar pattern of use, and are a lot of people’s first experience with pointers to pointers! But never fret—it’s easier than it looks.

Let’s do an example where we convert a string to an `unsigned long`, discarding error information (i.e. information about bad characters in the input string):
    
    
    [](types-iii-conversions.html#cb243-1)#include <stdio.h>
    [](types-iii-conversions.html#cb243-2)#include <stdlib.h>
    [](types-iii-conversions.html#cb243-3)
    [](types-iii-conversions.html#cb243-4)int main(void)
    [](types-iii-conversions.html#cb243-5){
    [](types-iii-conversions.html#cb243-6)    char *s = "3490";
    [](types-iii-conversions.html#cb243-7)
    [](types-iii-conversions.html#cb243-8)    // Convert string s, a number in base 10, to an unsigned long int.
    [](types-iii-conversions.html#cb243-9)    // NULL means we don't care to learn about any error information.
    [](types-iii-conversions.html#cb243-10)
    [](types-iii-conversions.html#cb243-11)    unsigned long int x = strtoul(s, NULL, 10);
    [](types-iii-conversions.html#cb243-12)
    [](types-iii-conversions.html#cb243-13)    printf("%lu\n", x);  // 3490
    [](types-iii-conversions.html#cb243-14)}

Notice a couple things there. Even though we didn’t deign to capture any information about error characters in the string, `strtoul()` won’t give us undefined behavior; it will just return `0`.

Also, we specified that this was a decimal (base 10) number.

Does this mean we can convert numbers of different bases? Sure! Let’s do binary!
    
    
    [](types-iii-conversions.html#cb244-1)#include <stdio.h>
    [](types-iii-conversions.html#cb244-2)#include <stdlib.h>
    [](types-iii-conversions.html#cb244-3)
    [](types-iii-conversions.html#cb244-4)int main(void)
    [](types-iii-conversions.html#cb244-5){
    [](types-iii-conversions.html#cb244-6)    char *s = "101010";  // What's the meaning of this number?
    [](types-iii-conversions.html#cb244-7)
    [](types-iii-conversions.html#cb244-8)    // Convert string s, a number in base 2, to an unsigned long int.
    [](types-iii-conversions.html#cb244-9)
    [](types-iii-conversions.html#cb244-10)    unsigned long int x = strtoul(s, NULL, 2);
    [](types-iii-conversions.html#cb244-11)
    [](types-iii-conversions.html#cb244-12)    printf("%lu\n", x);  // 42
    [](types-iii-conversions.html#cb244-13)}

OK, that’s all fun and games, but what’s with that `NULL` in there? What’s that for?

That helps us figure out if an error occurred in the processing of the string. It’s a pointer to a pointer to a `char`, which sounds scary, but isn’t once you wrap your head around it.

Let’s do an example where we feed in a deliberately bad number, and we’ll see how `strtol()` lets us know where the first invalid digit is.
    
    
    [](types-iii-conversions.html#cb245-1)#include <stdio.h>
    [](types-iii-conversions.html#cb245-2)#include <stdlib.h>
    [](types-iii-conversions.html#cb245-3)
    [](types-iii-conversions.html#cb245-4)int main(void)
    [](types-iii-conversions.html#cb245-5){
    [](types-iii-conversions.html#cb245-6)    char *s = "34x90";  // "x" is not a valid digit in base 10!
    [](types-iii-conversions.html#cb245-7)    char *badchar;
    [](types-iii-conversions.html#cb245-8)
    [](types-iii-conversions.html#cb245-9)    // Convert string s, a number in base 10, to an unsigned long int.
    [](types-iii-conversions.html#cb245-10)
    [](types-iii-conversions.html#cb245-11)    unsigned long int x = strtoul(s, &badchar, 10);
    [](types-iii-conversions.html#cb245-12)
    [](types-iii-conversions.html#cb245-13)    // It tries to convert as much as possible, so gets this far:
    [](types-iii-conversions.html#cb245-14)
    [](types-iii-conversions.html#cb245-15)    printf("%lu\n", x);  // 34
    [](types-iii-conversions.html#cb245-16)
    [](types-iii-conversions.html#cb245-17)    // But we can see the offending bad character because badchar
    [](types-iii-conversions.html#cb245-18)    // points to it!
    [](types-iii-conversions.html#cb245-19)
    [](types-iii-conversions.html#cb245-20)    printf("Invalid character: %c\n", *badchar);  // "x"
    [](types-iii-conversions.html#cb245-21)}

So there we have `strtoul()` modifying what `badchar` points to in order to show us where things went wrong[109](function-specifiers-alignment-specifiersoperators.html#fn109).

But what if nothing goes wrong? In that case, `badchar` will point to the `NUL` terminator at the end of the string. So we can test for it:
    
    
    [](types-iii-conversions.html#cb246-1)#include <stdio.h>
    [](types-iii-conversions.html#cb246-2)#include <stdlib.h>
    [](types-iii-conversions.html#cb246-3)
    [](types-iii-conversions.html#cb246-4)int main(void)
    [](types-iii-conversions.html#cb246-5){
    [](types-iii-conversions.html#cb246-6)    char *s = "3490";  // "x" is not a valid digit in base 10!
    [](types-iii-conversions.html#cb246-7)    char *badchar;
    [](types-iii-conversions.html#cb246-8)
    [](types-iii-conversions.html#cb246-9)    // Convert string s, a number in base 10, to an unsigned long int.
    [](types-iii-conversions.html#cb246-10)
    [](types-iii-conversions.html#cb246-11)    unsigned long int x = strtoul(s, &badchar, 10);
    [](types-iii-conversions.html#cb246-12)
    [](types-iii-conversions.html#cb246-13)    // Check if things went well
    [](types-iii-conversions.html#cb246-14)
    [](types-iii-conversions.html#cb246-15)    if (*badchar == '\0') {
    [](types-iii-conversions.html#cb246-16)        printf("Success! %lu\n", x);
    [](types-iii-conversions.html#cb246-17)    } else  {
    [](types-iii-conversions.html#cb246-18)        printf("Partial conversion: %lu\n", x);
    [](types-iii-conversions.html#cb246-19)        printf("Invalid character: %c\n", *badchar);
    [](types-iii-conversions.html#cb246-20)    }
    [](types-iii-conversions.html#cb246-21)}

So there you have it. The `atoi()`-style functions are good in a controlled pinch, but the `strtol()`-style functions give you far more control over error handling and the base of the input.

## 15.2 `char` Conversions

What if you have a single character with a digit in it, like `'5'`… Is that the same as the value `5`?

Let’s try it and see.
    
    
    [](types-iii-conversions.html#cb247-1)printf("%d %d\n", 5, '5');

On my UTF-8 system, this prints:
    
    
    [](types-iii-conversions.html#cb248-1)5 53

So… no. And 53? What is that? That’s the UTF-8 (and ASCII) code point for the character symbol `'5'`[110](function-specifiers-alignment-specifiersoperators.html#fn110)

So how do we convert the character `'5'` (which apparently has value 53) into the value `5`?

With one clever trick, that’s how!

The C Standard guarantees that these character will have code points that are in sequence and in this order:
    
    
    [](types-iii-conversions.html#cb249-1)0  1  2  3  4  5  6  7  8  9

Ponder for a second–how can we use that? Spoilers ahead…

Let’s take a look at the characters and their code points in UTF-8:
    
    
    [](types-iii-conversions.html#cb250-1)0  1  2  3  4  5  6  7  8  9
    [](types-iii-conversions.html#cb250-2)48 49 50 51 52 53 54 55 56 57

You see there that `'5'` is `53`, just like we were getting. And `'0'` is `48`.

So we can subtract `'0'` from any digit character to get its numeric value:
    
    
    [](types-iii-conversions.html#cb251-1)char c = '6';
    [](types-iii-conversions.html#cb251-2)
    [](types-iii-conversions.html#cb251-3)int x = c;  // x has value 54, the code point for '6'
    [](types-iii-conversions.html#cb251-4)
    [](types-iii-conversions.html#cb251-5)int y = c - '0'; // y has value 6, just like we want

And we can convert the other way, too, just by adding the value on.
    
    
    [](types-iii-conversions.html#cb252-1)int x = 6;
    [](types-iii-conversions.html#cb252-2)
    [](types-iii-conversions.html#cb252-3)char c = x + '0';  // c has value 54
    [](types-iii-conversions.html#cb252-4)
    [](types-iii-conversions.html#cb252-5)printf("%d\n", c);  // prints 54
    [](types-iii-conversions.html#cb252-6)printf("%c\n", c);  // prints 6 with %c

You might think this is a weird way to do this conversion, and by today’s standards, it certainly is. But back in the olden days when computers were made literally out of wood, this was the method for doing this conversion. And it wasn’t broke, so C never fixed it.

## 15.3 Numeric Conversions

### 15.3.1 Boolean

If you convert a zero to `bool`, the result is `0`. Otherwise it’s `1`.

### 15.3.2 Integer to Integer Conversions

If an integer type is converted to unsigned and doesn’t fit in it, the unsigned result wraps around odometer-style until it fits in the unsigned[111](function-specifiers-alignment-specifiersoperators.html#fn111).

If an integer type is converted to a signed number and doesn’t fit, the result is implementation-defined! Something documented will happen, but you’ll have to look it up[112](function-specifiers-alignment-specifiersoperators.html#fn112)

### 15.3.3 Integer and Floating Point Conversions

If a floating point type is converted to an integer type, the fractional part is discarded with prejudice[113](function-specifiers-alignment-specifiersoperators.html#fn113).

But—and here’s the catch—if the number is too large to fit in the integer, you get undefined behavior. So don’t do that.

Going From integer or floating point to floating point, C makes a best effort to find the closest floating point number to the integer that it can.

Again, though, if the original value can’t be represented, it’s undefined behavior.

## 15.4 Implicit Conversions

These are conversions the compiler does automatically for you when you mix and match types.

### 15.4.1 The Integer Promotions

In a number of places, if an `int` can be used to represent a value from `char` or `short` (signed or unsigned), that value is _promoted_ up to `int`. If it doesn’t fit in an `int`, it’s promoted to `unsigned int`.

This is how we can do something like this:
    
    
    [](types-iii-conversions.html#cb253-1)char x = 10, y = 20;
    [](types-iii-conversions.html#cb253-2)int i = x + y;

In that case, `x` and `y` get promoted to `int` by C before the math takes place.

The integer promotions take place during The Usual Arithmetic Conversions, with variadic functions[114](function-specifiers-alignment-specifiersoperators.html#fn114), unary `+` and `-` operators, or when passing values to functions without prototypes[115](function-specifiers-alignment-specifiersoperators.html#fn115).

### 15.4.2 The Usual Arithmetic Conversions

These are automatic conversions that C does around numeric operations that you ask for. (That’s actually what they’re called, by the way, by C11 §6.3.1.8.) Note that for this section, we’re just talking about numeric types—strings will come later.

These conversions answer questions about what happens when you mix types, like this:
    
    
    [](types-iii-conversions.html#cb254-1)int x = 3 + 1.2;   // Mixing int and double
    [](types-iii-conversions.html#cb254-2)                   // 4.2 is converted to int
    [](types-iii-conversions.html#cb254-3)                   // 4 is stored in x
    [](types-iii-conversions.html#cb254-4)
    [](types-iii-conversions.html#cb254-5)float y = 12 * 2;  // Mixing float and int
    [](types-iii-conversions.html#cb254-6)                   // 24 is converted to float
    [](types-iii-conversions.html#cb254-7)                   // 24.0 is stored in y

Do they become `int`s? Do they become `float`s? How does it work?

Here are the steps, paraphrased for easy consumption.

  1. If one thing in the expression is a floating type, convert the other things to that floating type.

  2. Otherwise, if both types are integer types, perform the integer promotions on each, then make the operand types as big as they need to be hold the common largest value. Sometimes this involves changing signed to unsigned.




If you want to know the gritty details, check out C11 §6.3.1.8. But you probably don’t.

Just generally remember that int types become float types if there’s a floating point type anywhere in there, and the compiler makes an effort to make sure mixed integer types don’t overflow.

Finally, if you convert from one floating point type to another, the compiler will try to make an exact conversion. If it can’t, it’ll do the best approximation it can. If the number is too large to fit in the type you’re converting into, _boom_ : undefined behavior!

### 15.4.3 `void*`

The `void*` type is interesting because it can be converted from or to any pointer type.
    
    
    [](types-iii-conversions.html#cb255-1)int x = 10;
    [](types-iii-conversions.html#cb255-2)
    [](types-iii-conversions.html#cb255-3)void *p = &x;  // &x is type int*, but we store it in a void*
    [](types-iii-conversions.html#cb255-4)
    [](types-iii-conversions.html#cb255-5)int *q = p;    // p is void*, but we store it in an int*

## 15.5 Explicit Conversions

These are conversions from type to type that you have to ask for; the compiler won’t do it for you.

You can convert from one type to another by assigning one type to another with an `=`.

You can also convert explicitly with a _cast_.

### 15.5.1 Casting

You can explicitly change the type of an expression by putting a new type in parentheses in front of it. Some C devs frown on the practice unless absolutely necessary, but it’s likely you’ll come across some C code with these in it.

Let’s do an example where we want to convert an `int` into a `long` so that we can store it in a `long`.

Note: this example is contrived and the cast in this case is completely unnecessary because the `x + 12` expression would automatically be changed to `long int` to match the wider type of `y`.
    
    
    [](types-iii-conversions.html#cb256-1)int x = 10;
    [](types-iii-conversions.html#cb256-2)long int y = (long int)x + 12;

In that example, even those `x` was type `int` before, the expression `(long int)x` has type `long int`. We say, “We cast `x` to `long int`.”

More commonly, you might see a cast being used to convert a `void*` into a specific pointer type so it can be dereferenced.

A callback from the built-in `qsort()` function might display this behavior since it has `void*`s passed into it:
    
    
    [](types-iii-conversions.html#cb257-1)int compar(const void *elem1, const void *elem2)
    [](types-iii-conversions.html#cb257-2){
    [](types-iii-conversions.html#cb257-3)    if (*((const int*)elem2) > *((const int*)elem1)) return 1;
    [](types-iii-conversions.html#cb257-4)    if (*((const int*)elem2) < *((const int*)elem1)) return -1;
    [](types-iii-conversions.html#cb257-5)    return 0;
    [](types-iii-conversions.html#cb257-6)}

But you could also clearly write it with an assignment:
    
    
    [](types-iii-conversions.html#cb258-1)int compar(const void *elem1, const void *elem2)
    [](types-iii-conversions.html#cb258-2){
    [](types-iii-conversions.html#cb258-3)    const int *e1 = elem1;
    [](types-iii-conversions.html#cb258-4)    const int *e2 = elem2;
    [](types-iii-conversions.html#cb258-5)
    [](types-iii-conversions.html#cb258-6)    return *e2 - *e1;
    [](types-iii-conversions.html#cb258-7)}

One place you’ll see casts more commonly is to avoid a warning when printing pointer values with the rarely-used `%p` which gets picky with anything other than a `void*`:
    
    
    [](types-iii-conversions.html#cb259-1)int x = 3490;
    [](types-iii-conversions.html#cb259-2)int *p = &x;
    [](types-iii-conversions.html#cb259-3)
    [](types-iii-conversions.html#cb259-4)printf("%p\n", p);

generates this warning:
    
    
    [](types-iii-conversions.html#cb260-1)warning: format ‘%p’ expects argument of type ‘void *’, but argument
    [](types-iii-conversions.html#cb260-2)         2 has type ‘int *’

You can fix it with a cast:
    
    
    [](types-iii-conversions.html#cb261-1)printf("%p\n", (void *)p);

Another place is with explicit pointer changes, if you don’t want to use an intervening `void*`, but these are also pretty uncommon:
    
    
    [](types-iii-conversions.html#cb262-1)long x = 3490;
    [](types-iii-conversions.html#cb262-2)long *p = &x;
    [](types-iii-conversions.html#cb262-3)unsigned char *c = (unsigned char *)p;

A third place it’s often required is with the character conversion functions in [`<ctype.h>`](https://beej.us/guide/bgclr/html/split/ctype.html)[116](function-specifiers-alignment-specifiersoperators.html#fn116) where you should cast questionably-signed values to `unsigned char` to avoid undefined behavior.

Again, casting is rarely _needed_ in practice. If you find yourself casting, there might be another way to do the same thing, or maybe you’re casting unnecessarily.

Or maybe it is necessary. Personally, I try to avoid it, but am not afraid to use it if I have to.

* * *

[Prev](types-ii-way-more-types.html) | [Contents](index.html) | [Next](types-iv-qualifiers-and-specifiers.html)
