[Prev](chapter-atomics.html) | [Contents](index.html) | [Next](function-specifiers-alignment-specifiersoperators.html)

* * *

# 41 Function Specifiers, Alignment Specifiers/Operators

These don’t see a heck of a lot of use in my experience, but we’ll cover them here for the sake of completeness.

## 41.1 Function Specifiers

When you declare a function, you can give the compiler a couple tips about how the functions could or will be used. This enables or encourages the compiler to make certain optimizations.

### 41.1.1 `inline` for Speed—Maybe

You can declare a function to be inline like this:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb796-1)static inline int add(int x, int y) {
    [](function-specifiers-alignment-specifiersoperators.html#cb796-2)    return x + y;
    [](function-specifiers-alignment-specifiersoperators.html#cb796-3)}

This is meant to encourage the compiler to make this function call as fast as possible. And, historically, one way to do this was _inlining_ , which means that the body of the function would be embedded in its entirety where the call was made. This would avoid all the overhead of setting up the function call and tearing it down at the expense of larger code size as the function was copied all over the place instead of being reused.

The quick-and-dirty things to remember are:

  1. You probably don’t need to use `inline` for speed. Modern compilers know what’s best.

  2. If you do use it for speed, use it with file scope, i.e. `static inline`. This avoids the messy rules of external linkage and inline functions.




Stop reading this section now.

Glutton for punishment, eh?

Let’s try leaving the `static` off.
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb797-1)#include <stdio.h>
    [](function-specifiers-alignment-specifiersoperators.html#cb797-2)
    [](function-specifiers-alignment-specifiersoperators.html#cb797-3)inline int add(int x, int y)
    [](function-specifiers-alignment-specifiersoperators.html#cb797-4){
    [](function-specifiers-alignment-specifiersoperators.html#cb797-5)    return x + y;
    [](function-specifiers-alignment-specifiersoperators.html#cb797-6)}
    [](function-specifiers-alignment-specifiersoperators.html#cb797-7)
    [](function-specifiers-alignment-specifiersoperators.html#cb797-8)int main(void)
    [](function-specifiers-alignment-specifiersoperators.html#cb797-9){
    [](function-specifiers-alignment-specifiersoperators.html#cb797-10)    printf("%d\n", add(1, 2));
    [](function-specifiers-alignment-specifiersoperators.html#cb797-11)}

`gcc` gives a linker error on `add()`[232](function-specifiers-alignment-specifiersoperators.html#fn232). The spec requires that if you have a non-`extern` inline function you must also provide a version with external linkage.

So you’d have to have an `extern` version somewhere else for this to work. If the compiler has both an `inline` function in the current file and an external version of the same function elsewhere, it gets to choose which one to call. So I highly recommend they be the same.

Another thing you can do is to declare the function as `extern inline`. This will attempt to inline in the same file (for speed), but will also create a version with external linkage.

### 41.1.2 `noreturn` and `_Noreturn`

This indicates to the compiler that a particular function will not ever return to its caller, i.e. the program will exit by some mechanism before the function returns.

It allows the compiler to perhaps perform some optimizations around the function call.

It also allows you to indicate to other devs that some program logic depends on a function _not_ returning.

You’ll likely never need to use this, but you’ll see it on some library calls like [`exit()`](https://beej.us/guide/bgclr/html/split/stdlib.html#man-exit)[233](function-specifiers-alignment-specifiersoperators.html#fn233) and [`abort()`](https://beej.us/guide/bgclr/html/split/stdlib.html#man-abort)[234](function-specifiers-alignment-specifiersoperators.html#fn234).

The built-in keyword is `_Noreturn`, but if it doesn’t break your existing code, everyone would recommend including `<stdnoreturn.h>` and using the easier-to-read `noreturn` instead.

It’s undefined behavior if a function specified as `noreturn` actually does return. It’s computationally dishonest, see.

Here’s an example of using `noreturn` correctly:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb798-1)#include <stdio.h>
    [](function-specifiers-alignment-specifiersoperators.html#cb798-2)#include <stdlib.h>
    [](function-specifiers-alignment-specifiersoperators.html#cb798-3)#include <stdnoreturn.h>
    [](function-specifiers-alignment-specifiersoperators.html#cb798-4)
    [](function-specifiers-alignment-specifiersoperators.html#cb798-5)noreturn void foo(void) // This function should never return!
    [](function-specifiers-alignment-specifiersoperators.html#cb798-6){
    [](function-specifiers-alignment-specifiersoperators.html#cb798-7)    printf("Happy days\n");
    [](function-specifiers-alignment-specifiersoperators.html#cb798-8)
    [](function-specifiers-alignment-specifiersoperators.html#cb798-9)    exit(1);            // And it doesn't return--it exits here!
    [](function-specifiers-alignment-specifiersoperators.html#cb798-10)}
    [](function-specifiers-alignment-specifiersoperators.html#cb798-11)
    [](function-specifiers-alignment-specifiersoperators.html#cb798-12)int main(void)
    [](function-specifiers-alignment-specifiersoperators.html#cb798-13){
    [](function-specifiers-alignment-specifiersoperators.html#cb798-14)    foo();
    [](function-specifiers-alignment-specifiersoperators.html#cb798-15)}

If the compiler detects that a `noreturn` function could return, it might warn you, helpfully.

Replacing the `foo()` function with this:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb799-1)noreturn void foo(void)
    [](function-specifiers-alignment-specifiersoperators.html#cb799-2){
    [](function-specifiers-alignment-specifiersoperators.html#cb799-3)    printf("Breakin' the law\n");
    [](function-specifiers-alignment-specifiersoperators.html#cb799-4)}

gets me a warning:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb800-1)foo.c:7:1: warning: function declared 'noreturn' should not return

## 41.2 Alignment Specifiers and Operators

[_Alignment_](https://en.wikipedia.org/wiki/Data_structure_alignment)[ 235](function-specifiers-alignment-specifiersoperators.html#fn235) is all about multiples of addresses on which objects can be stored. Can you store this at any address? Or must it be a starting address that’s divisible by 2? Or 8? Or 16?

If you’re coding up something low-level like a memory allocator that interfaces with your OS, you might need to consider this. Most devs go their careers without using this functionality in C.

### 41.2.1 `alignas` and `_Alignas`

This isn’t a function. Rather, it’s an _alignment specifier_ that you can use with a variable declaration.

The built-in specifier is `_Alignas`, but the header `<stdalign.h>` defines it as `alignas` for something better looking.

If you need your `char` to be aligned like an `int`, you can force it like this when you declare it:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb801-1)char alignas(int) c;

You can also pass a constant value or expression in for the alignment. This has to be something supported by the system, but the spec stops short of dictating what values you can put in there. Small powers of 2 (1, 2, 4, 8, and 16) are generally safe bets.
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb802-1)char alignas(8) c;   // align on 8-byte boundaries

If you want to align at the maximum used alignment by your system, include `<stddef.h>` and use the type `max_align_t`, like so:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb803-1)char alignas(max_align_t) c;

You could potentially _over-align_ by specifying an alignment more than that of `max_align_t`, but whether or not such things are allowed is system dependent.

### 41.2.2 `alignof` and `_Alignof`

This operator will return the address multiple a particular type uses for alignment on this system. For example, maybe `char`s are aligned every 1 address, and `int`s are aligned every 4 addresses.

The built-in operator is `_Alignof`, but the header `<stdalign.h>` defines it as `alignof` if you want to look cooler.

Here’s a program that will print out the alignments of a variety of different types. Again, these will vary from system to system. Note that the type `max_align_t` will give you the maximum alignment used by the system.
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb804-1)#include <stdalign.h>
    [](function-specifiers-alignment-specifiersoperators.html#cb804-2)#include <stdio.h>     // for printf()
    [](function-specifiers-alignment-specifiersoperators.html#cb804-3)#include <stddef.h>    // for max_align_t
    [](function-specifiers-alignment-specifiersoperators.html#cb804-4)
    [](function-specifiers-alignment-specifiersoperators.html#cb804-5)struct t {
    [](function-specifiers-alignment-specifiersoperators.html#cb804-6)    int a;
    [](function-specifiers-alignment-specifiersoperators.html#cb804-7)    char b;
    [](function-specifiers-alignment-specifiersoperators.html#cb804-8)    float c;
    [](function-specifiers-alignment-specifiersoperators.html#cb804-9)};
    [](function-specifiers-alignment-specifiersoperators.html#cb804-10)
    [](function-specifiers-alignment-specifiersoperators.html#cb804-11)int main(void)
    [](function-specifiers-alignment-specifiersoperators.html#cb804-12){
    [](function-specifiers-alignment-specifiersoperators.html#cb804-13)    printf("char       : %zu\n", alignof(char));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-14)    printf("short      : %zu\n", alignof(short));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-15)    printf("int        : %zu\n", alignof(int));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-16)    printf("long       : %zu\n", alignof(long));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-17)    printf("long long  : %zu\n", alignof(long long));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-18)    printf("double     : %zu\n", alignof(double));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-19)    printf("long double: %zu\n", alignof(long double));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-20)    printf("struct t   : %zu\n", alignof(struct t));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-21)    printf("max_align_t: %zu\n", alignof(max_align_t));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-22)}

Output on my system:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb805-1)char       : 1
    [](function-specifiers-alignment-specifiersoperators.html#cb805-2)short      : 2
    [](function-specifiers-alignment-specifiersoperators.html#cb805-3)int        : 4
    [](function-specifiers-alignment-specifiersoperators.html#cb805-4)long       : 8
    [](function-specifiers-alignment-specifiersoperators.html#cb805-5)long long  : 8
    [](function-specifiers-alignment-specifiersoperators.html#cb805-6)double     : 8
    [](function-specifiers-alignment-specifiersoperators.html#cb805-7)long double: 16
    [](function-specifiers-alignment-specifiersoperators.html#cb805-8)struct t   : 16
    [](function-specifiers-alignment-specifiersoperators.html#cb805-9)max_align_t: 16

## 41.3 `memalignment()` Function

New in C23!

(Caveat: none of my compilers support this function yet, so the code is largely untested.)

`alignof` is great if you know the type of your data. But what if you’re _woefully ignorant_ of the type, and only have a pointer to the data?

How could that even happen?

Well, with our good friend the `void*`, of course. We can’t pass that to `alignof`, but what if we need to know the alignment of the thing it points to?

We might want to know this if we’re about to use the memory for something that has significant alignment needs. For example, atomic and floating types often behave badly if misaligned.

So with this function we can check the alignment of some data as long as we have a pointer to that data, even if it’s a `void*`.

Let’s do a quick test to see if a void pointer is well-aligned for use as an atomic type, and, if so, let’s get a variable to use it as that type:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb806-1)void foo(void *p)
    [](function-specifiers-alignment-specifiersoperators.html#cb806-2){
    [](function-specifiers-alignment-specifiersoperators.html#cb806-3)    if (memalignment(p) >= alignof(atomic int)) {
    [](function-specifiers-alignment-specifiersoperators.html#cb806-4)        atomic int *i = p;
    [](function-specifiers-alignment-specifiersoperators.html#cb806-5)        do_things(i);
    [](function-specifiers-alignment-specifiersoperators.html#cb806-6)    } else
    [](function-specifiers-alignment-specifiersoperators.html#cb806-7)        puts("This pointer is no good as an atomic int\n");
    [](function-specifiers-alignment-specifiersoperators.html#cb806-8)
    [](function-specifiers-alignment-specifiersoperators.html#cb806-9)...

I suspect you will rarely (to the point of never, likely) need to use this function unless you’re doing some low-level stuff.

And there you have it. Alignment!

* * *

  1. https://www.ioccc.org/[↩︎](foreword.html#fnref1)

  2. https://en.wikipedia.org/wiki/Python_(programming_language)[↩︎](foreword.html#fnref2)

  3. https://en.wikipedia.org/wiki/JavaScript[↩︎](foreword.html#fnref3)

  4. https://en.wikipedia.org/wiki/Java_(programming_language)[↩︎](foreword.html#fnref4)

  5. https://en.wikipedia.org/wiki/Rust_(programming_language)[↩︎](foreword.html#fnref5)

  6. https://en.wikipedia.org/wiki/Go_(programming_language)[↩︎](foreword.html#fnref6)

  7. https://en.wikipedia.org/wiki/Swift_(programming_language)[↩︎](foreword.html#fnref7)

  8. https://en.wikipedia.org/wiki/Objective-C[↩︎](foreword.html#fnref8)

  9. https://beej.us/guide/bgclr/[↩︎](foreword.html#fnref9)

  10. https://en.wikipedia.org/wiki/ANSI_C[↩︎](foreword.html#fnref10)

  11. https://en.wikipedia.org/wiki/POSIX[↩︎](foreword.html#fnref11)

  12. https://visualstudio.microsoft.com/vs/community/[↩︎](foreword.html#fnref12)

  13. https://docs.microsoft.com/en-us/windows/wsl/install-win10[↩︎](foreword.html#fnref13)

  14. https://developer.apple.com/xcode/[↩︎](foreword.html#fnref14)

  15. https://beej.us/guide/bgc/[↩︎](foreword.html#fnref15)

  16. https://en.cppreference.com/[↩︎](foreword.html#fnref16)

  17. https://groups.google.com/g/comp.lang.c[↩︎](foreword.html#fnref17)

  18. https://www.reddit.com/r/C_Programming/[↩︎](foreword.html#fnref18)

  19. https://en.wikipedia.org/wiki/Assembly_language[↩︎](hello-world.html#fnref19)

  20. https://en.wikipedia.org/wiki/Bare_machine[↩︎](hello-world.html#fnref20)

  21. https://en.wikipedia.org/wiki/Operating_system[↩︎](hello-world.html#fnref21)

  22. https://en.wikipedia.org/wiki/Embedded_system[↩︎](hello-world.html#fnref22)

  23. https://en.wikipedia.org/wiki/Rust_(programming_language)[↩︎](hello-world.html#fnref23)

  24. https://en.wikipedia.org/wiki/Grok[↩︎](hello-world.html#fnref24)

  25. I know someone will fight me on that, but it’s gotta be at least in the top three, right?[↩︎](hello-world.html#fnref25)

  26. Well, technically there are more than two, but hey, let’s pretend there are two—ignorance is bliss, right?[↩︎](hello-world.html#fnref26)

  27. https://en.wikipedia.org/wiki/Assembly_language[↩︎](hello-world.html#fnref27)

  28. https://en.wikipedia.org/wiki/Machine_code[↩︎](hello-world.html#fnref28)

  29. Technically, it contains preprocessor directives and function prototypes (more on that later) for common input and output needs.[↩︎](hello-world.html#fnref29)

  30. https://en.wikipedia.org/wiki/Unix[↩︎](hello-world.html#fnref30)

  31. If you don’t give it an output filename, it will export to a file called `a.out` by default—this filename has its roots deep in Unix history.[↩︎](hello-world.html#fnref31)

  32. https://formulae.brew.sh/formula/gcc[↩︎](hello-world.html#fnref32)

  33. A “byte” is typically an 8-bit binary number. Think of it as an integer that can only hold the values from 0 to 255, inclusive. Technically, C allows bytes to be any number of bits and if you want to unambiguously refer to an 8-bit number, you should use the term _octet_. But programmers are going to assume you mean 8-bits when you say “byte” unless you specify otherwise.[↩︎](variables-and-statements.html#fnref33)

  34. I’m seriously oversimplifying how modern memory works, here. But the mental model works, so please forgive me.[↩︎](variables-and-statements.html#fnref34)

  35. I’m lying here a little. Technically `3.14159` is of type `double`, but we’re not there yet and I want you to associate `float` with “Floating Point”, and C will happily coerce that type into a `float`. In short, don’t worry about it until later.[↩︎](variables-and-statements.html#fnref35)

  36. Read this as “pointer to a char” or “char pointer”. “Char” for character. Though I can’t find a study, it seems anecdotally most people pronounce this as “char”, a minority say “car”, and a handful say “care”. We’ll talk more about pointers later.[↩︎](variables-and-statements.html#fnref36)

  37. Colloquially, we say they have “random” values, but they aren’t truly—or even pseudo-truly—random numbers.[↩︎](variables-and-statements.html#fnref37)

  38. This isn’t strictly 100% true. When we get to learning about static storage duration, you’ll find the some variables are initialized to zero automatically. But the safe thing to do is always initialize them.[↩︎](variables-and-statements.html#fnref38)

  39. Technically just one bit of a `char` is used to represent the `bool`, so it can either be zero or one. Except that what goes in the remaining (padding) bits of the `char` is unspecified. For `false`, it must surely be all zero. But for `true`, I’m uncertain that it must all be zero.[↩︎](variables-and-statements.html#fnref39)

  40. The `_t` is short for `type`.[↩︎](variables-and-statements.html#fnref40)

  41. Except for with variable length arrays—but that’s a story for another time.[↩︎](variables-and-statements.html#fnref41)

  42. https://beej.us/guide/bgclr/html/split/stdlib.html#man-srand[↩︎](variables-and-statements.html#fnref42)

  43. This was considered such a hazard that the designers of the Go Programming Language made `break` the default; you have to explicitly use Go’s `fallthrough` statement if you want to fall into the next case.[↩︎](variables-and-statements.html#fnref43)

  44. Never say “never”.[↩︎](functions.html#fnref44)

  45. Typically. I’m sure there are exceptions out there in the dark corridors of computing history.[↩︎](pointers.html#fnref45)

  46. A byte is a number made up of no more than 8 binary digits, or _bits_ for short. This means in decimal digits just like grandma used to use, it can hold an unsigned number between 0 and 255, inclusive.[↩︎](pointers.html#fnref46)

  47. The order that bytes come in is referred to as the _endianness_ of the number. The usual suspects are _big-endian_ (with the most significant byte first) and _little-endian_ (with the most-significant byte last), or, uncommonly now, _mixed-endian_ (with the most-significant bytes somewhere else).[↩︎](pointers.html#fnref47)

  48. That is, base 16 with digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F.[↩︎](pointers.html#fnref48)

  49. https://en.wikipedia.org/wiki/Virtual_memory[↩︎](pointers.html#fnref49)

  50. That’s not all! It’s used in `/*comments*/` and multiplication and in function prototypes with variable length arrays! It’s all the same `*`, but the context gives it different meaning.[↩︎](pointers.html#fnref50)

  51. https://en.wikipedia.org/wiki/Null_pointer#History[↩︎](pointers.html#fnref51)

  52. https://en.wikipedia.org/wiki/Sentinel_value[↩︎](pointers.html#fnref52)

  53. The pointer type variables are `a`, `d`, `f`, and `i`, because those are the ones with `*` in front of them.[↩︎](pointers.html#fnref53)

  54. These days, anyway.[↩︎](arrays.html#fnref54)

  55. Again, not really, but variable-length arrays—of which I’m not really a fan—are a story for another time.[↩︎](arrays.html#fnref55)

  56. Since arrays are just pointers to the first element of the array under the hood, there’s no additional information recording the length.[↩︎](arrays.html#fnref56)

  57. Because when you pass an array to a function, you’re actually just passing a pointer to the first element of that array, not the “entire” array.[↩︎](arrays.html#fnref57)

  58. In the good old MS-DOS days before memory protection was a thing, I was writing some particularly abusive C code that deliberately engaged in all kinds of undefined behavior. But I knew what I was doing, and things were working pretty well. Until I made a misstep that caused a lockup and, as I found upon reboot, nuked all my BIOS settings. That was fun. (Shout-out to @man for those fun times.)[↩︎](arrays.html#fnref58)

  59. There are a lot of things that cause undefined behavior, not just out-of-bounds array accesses. This is what makes the C language so _exciting_.[↩︎](arrays.html#fnref59)

  60. https://en.wikipedia.org/wiki/Row-_and_column-major_order[↩︎](arrays.html#fnref60)

  61. This is technically incorrect, as a pointer to an array and a pointer to the first element of an array have different types. But we can burn that bridge when we get to it.[↩︎](arrays.html#fnref61)

  62. C11 §6.7.6.2¶1 requires it be greater than zero. But you might see code out there with arrays declared of zero length at the end of `struct`s and GCC is particularly lenient about it unless you compile with `-pedantic`. This zero-length array was a hackish mechanism for making variable-length structures. Unfortunately, it’s technically undefined behavior to access such an array even though it basically worked everywhere. C99 codified a well-defined replacement for it called _flexible array members_ , which we’ll chat about later.[↩︎](arrays.html#fnref62)

  63. This is also equivalent: `void print_2D_array(int (*a)[3])`, but that’s more than I want to get into right now.[↩︎](arrays.html#fnref63)

  64. Though it is true that C doesn’t track the length of strings.[↩︎](strings.html#fnref64)

  65. If you’re using the basic character set or an 8-bit character set, you’re used to one character being one byte. This isn’t true in all character encodings, though.[↩︎](strings.html#fnref65)

  66. This is different than the `NULL` pointer, and I’ll abbreviate it `NUL` when talking about the character versus `NULL` for the pointer.[↩︎](strings.html#fnref66)

  67. Later we’ll learn a neater way to do it with pointer arithmetic.[↩︎](strings.html#fnref67)

  68. There’s another function called `strncpy()` that limits the number of bytes copied. Some people say that you should always use `strncpy()` because of the buffer overrun protection. Other people say you should never use `strncpy()` because it won’t necessarily terminate your strings, another grotesque footgun. If you want to be really safe, you can write your own version of `strncpy()` that always terminates the string.[↩︎](strings.html#fnref68)

  69. Although in C individual items in memory like `int`s are referred to as “objects”, they’re not objects in an object-oriented programming sense.[↩︎](structs.html#fnref69)

  70. The Saturn was a popular brand of economy car in the United States until it was put out of business by the 2008 crash, sadly so to us fans.[↩︎](structs.html#fnref70)

  71. A pointer is likely 8 bytes on a 64-bit system.[↩︎](structs.html#fnref71)

  72. A _deep copy_ follows pointer in the `struct` and copies the data they point to, as well. A _shallow copy_ just copies the pointers, but not the things they point to. C doesn’t come with any built-in deep copy functionality.[↩︎](structs.html#fnref72)

  73. https://beej.us/guide/bgclr/html/split/stringref.html#man-strcmp[↩︎](structs.html#fnref73)

  74. https://beej.us/guide/bgclr/html/split/stringref.html#man-memset[↩︎](structs.html#fnref74)

  75. https://stackoverflow.com/questions/141720/how-do-you-compare-structs-for-equality-in-c[↩︎](structs.html#fnref75)

  76. We used to have three different newlines in broad effect: Carriage Return (CR, used on old Macs), Linefeed (LF, used on Unix systems), and Carriage Return/Linefeed (CRLF, used on Windows systems). Thankfully the introduction of OS X, being Unix-based, reduced this number to two.[↩︎](file-inputoutput.html#fnref76)

  77. If the buffer’s not big enough to read in an entire line, it’ll just stop reading mid-line, and the next call to `fgets()` will continue reading the rest of the line.[↩︎](file-inputoutput.html#fnref77)

  78. Normally the second program would read all the bytes at once, and _then_ print them out in a loop. That would be more efficient. But we’re going for demo value, here.[↩︎](file-inputoutput.html#fnref78)

  79. https://en.wikipedia.org/wiki/Hex_dump[↩︎](file-inputoutput.html#fnref79)

  80. https://en.wikipedia.org/wiki/Endianess[↩︎](file-inputoutput.html#fnref80)

  81. And this is why I used individual bytes in my `fwrite()` and `fread()` examples, above, shrewdly.[↩︎](file-inputoutput.html#fnref81)

  82. https://en.wikipedia.org/wiki/Protocol_buffers[↩︎](file-inputoutput.html#fnref82)

  83. We’ll talk more about these later.[↩︎](typedef-making-new-types.html#fnref83)

  84. Recall that the `sizeof` operator tells you the size in bytes of an object in memory.[↩︎](pointers2.html#fnref84)

  85. Or string, which is really an array of `char`s. Somewhat peculiarly, you can also have a pointer that references _one past_ the end of the array without a problem and still do math on it. You just can’t dereference it when it’s out there.[↩︎](pointers2.html#fnref85)

  86. https://beej.us/guide/bgclr/html/split/stdlib.html#man-qsort[↩︎](pointers2.html#fnref86)

  87. https://beej.us/guide/bgclr/html/split/stdlib.html#man-bsearch[↩︎](pointers2.html#fnref87)

  88. Because remember that array notation is just a dereference and some pointer math, and you can’t dereference a `void*`![↩︎](pointers2.html#fnref88)

  89. You can also _cast_ the `void*` to another type, but we haven’t gotten to casts yet.[↩︎](pointers2.html#fnref89)

  90. Or until the program exits, in which case all the memory allocated by it is freed. Asterisk: some systems allow you to allocate memory that persists after a program exits, but it’s system dependent, out of scope for this guide, and you’ll certainly never do it on accident.[↩︎](manual-memory-allocation.html#fnref90)

  91. http://www.open-std.org/jtc1/sc22/wg14/www/docs/summary.htm#dr_460[↩︎](manual-memory-allocation.html#fnref91)

  92. https://en.wikipedia.org/wiki/Bit_bucket[↩︎](scope.html#fnref92)

  93. “Bit” is short for _binary digit_. Binary is just another way of representing numbers. Instead of digits 0-9 like we’re used to, it’s digits 0-1.[↩︎](types-ii-way-more-types.html#fnref93)

  94. https://en.wikipedia.org/wiki/Two%27s_complement[↩︎](types-ii-way-more-types.html#fnref94)

  95. The industry term for a sequence of exactly, indisputably 8 bits is an _octet_.[↩︎](types-ii-way-more-types.html#fnref95)

  96. In general, if you have an \\(n\\) bit two’s complement number, the signed range is \\(-2^{n-1}\\) to \\(2^{n-1}-1\\). And the unsigned range is \\(0\\) to \\(2^n-1\\).[↩︎](types-ii-way-more-types.html#fnref96)

  97. https://en.wikipedia.org/wiki/ASCII[↩︎](types-ii-way-more-types.html#fnref97)

  98. https://en.wikipedia.org/wiki/List_of_information_system_character_sets[↩︎](types-ii-way-more-types.html#fnref98)

  99. https://en.wikipedia.org/wiki/Unicode[↩︎](types-ii-way-more-types.html#fnref99)

  100. Depends on if a `char` defaults to `signed char` or `unsigned char`[↩︎](types-ii-way-more-types.html#fnref100)

  101. https://en.wikipedia.org/wiki/Signed_number_representations#Signed_magnitude_representation[↩︎](types-ii-way-more-types.html#fnref101)

  102. My `char` is signed.[↩︎](types-ii-way-more-types.html#fnref102)

  103. https://en.wikipedia.org/wiki/IEEE_754[↩︎](types-ii-way-more-types.html#fnref103)

  104. This program runs as its comments indicate on a system with `FLT_DIG` of `6` that uses IEEE-754 base-2 floating point numbers. Otherwise, you might get different output.[↩︎](types-ii-way-more-types.html#fnref104)

  105. It’s really surprising to me that C doesn’t have this in the spec yet. In the C99 Rationale document, they write, “A proposal to add binary constants was rejected due to lack of precedent and insufficient utility.” Which seems kind of silly in light of some of the other features they kitchen-sinked in there! I’ll bet one of the next releases has it.[↩︎](types-ii-way-more-types.html#fnref105)

  106. https://en.wikipedia.org/wiki/Scientific_notation[↩︎](types-ii-way-more-types.html#fnref106)

  107. They’re the same except `snprintf()` allows you to specify a maximum number of bytes to output, preventing the overrunning of the end of your string. So it’s safer.[↩︎](types-iii-conversions.html#fnref107)

  108. https://en.wikipedia.org/wiki/ASCII[↩︎](types-iii-conversions.html#fnref108)

  109. We have to pass a pointer to `badchar` to `strtoul()` or it won’t be able to modify it in any way we can see, analogous to why you have to pass a pointer to an `int` to a function if you want that function to be able to change that value of that `int`.[↩︎](types-iii-conversions.html#fnref109)

  110. Each character has a value associated with it for any given character encoding scheme.[↩︎](types-iii-conversions.html#fnref110)

  111. In practice, what’s probably happening on your implementation is that the high-order bits are just being dropped from the result, so a 16-bit number `0x1234` being converted to an 8-bit number ends up as `0x0034`, or just `0x34`.[↩︎](types-iii-conversions.html#fnref111)

  112. Again, in practice, what will likely happen on your system is that the bit pattern for the original will be truncated and then just used to represent the signed number, two’s complement. For example, my system takes an `unsigned char` of `192` and converts it to `signed char` `-64`. In two’s complement, the bit pattern for both these numbers is binary `11000000`.[↩︎](types-iii-conversions.html#fnref112)

  113. Not really—it’s just discarded regularly.[↩︎](types-iii-conversions.html#fnref113)

  114. Functions with a variable number of arguments.[↩︎](types-iii-conversions.html#fnref114)

  115. This is rarely done because the compiler will complain and having a prototype is the _Right Thing_ to do. I think this still works for historic reasons, before prototypes were a thing.[↩︎](types-iii-conversions.html#fnref115)

  116. https://beej.us/guide/bgclr/html/split/ctype.html[↩︎](types-iii-conversions.html#fnref116)

  117. https://gustedt.wordpress.com/2010/08/17/a-common-misconsception-the-register-keyword/[↩︎](types-iv-qualifiers-and-specifiers.html#fnref117)

  118. https://en.wikipedia.org/wiki/Processor_register[↩︎](types-iv-qualifiers-and-specifiers.html#fnref118)

  119. https://en.wikipedia.org/wiki/Boids[↩︎](multifile-projects.html#fnref119)

  120. Historially, MS-DOS and Windows programs would do this differently than Unix. In Unix, the shell would _expand_ the wildcard into all matching files before your program saw it, whereas the Microsoft variants would pass the wildcard expression into the program to deal with. In any case, there are arguments that get passed into the program.[↩︎](the-outside-environment.html#fnref120)

  121. Since they’re just regular parameter names, you don’t actually have to call them `argc` and `argv`. But it’s so very idiomatic to use those names, if you get creative, other C programmers will look at you with a suspicious eye, indeed![↩︎](the-outside-environment.html#fnref121)

  122. `ps`, Process Status, is a Unix command to see what processes are running at the moment.[↩︎](the-outside-environment.html#fnref122)

  123. https://en.wikipedia.org/wiki/Inception[↩︎](the-outside-environment.html#fnref123)

  124. https://en.wikipedia.org/wiki/Shell_(computing)[↩︎](the-outside-environment.html#fnref124)

  125. In Windows `cmd.exe`, type `echo %errorlevel%`. In PowerShell, type `$LastExitCode`.[↩︎](the-outside-environment.html#fnref125)

  126. If you need a numeric value, convert the string with something like `atoi()` or `strtol()`.[↩︎](the-outside-environment.html#fnref126)

  127. In Windows CMD.EXE, use `set FROTZ=value`. In PowerShell, use `$Env:FROTZ=value`.[↩︎](the-outside-environment.html#fnref127)

  128. https://pubs.opengroup.org/onlinepubs/9699919799/functions/exec.html[↩︎](the-outside-environment.html#fnref128)

  129. You can’t always just wrap the code in `/*` `*/` comments because those won’t nest.[↩︎](the-c-preprocessor.html#fnref129)

  130. This isn’t really a macro—it’s technically an identifier. But it’s the only predefined identifier and it feels very macro-like, so I’m including it here. Like a rebel.[↩︎](the-c-preprocessor.html#fnref130)

  131. A hosted implementation basically means you’re running the full C standard, probably on an operating system of some kind. Which you probably are. If you’re running on bare metal in some kind of embedded system, you’re probably on a _standalone implementation_.[↩︎](the-c-preprocessor.html#fnref131)

  132. OK, I know that was a cop-out answer. Basically there’s an optional extension compilers can implement wherein they agree to limit certain types of undefined behavior so that the C code is more amenable to static code analysis. It is unlikely you’ll need to use this.[↩︎](the-c-preprocessor.html#fnref132)

  133. _Breakin’ the law… breakin’ the law…_[↩︎](the-c-preprocessor.html#fnref133)

  134. https://www.openmp.org/[↩︎](the-c-preprocessor.html#fnref134)

  135. Technically we say that it has an _incomplete type_.[↩︎](structs-ii-more-fun-with-structs.html#fnref135)

  136. Though some compilers have options to force this to occur—search for `__attribute__((packed))` to see how to do this with GCC.[↩︎](structs-ii-more-fun-with-structs.html#fnref136)

  137. `super` isn’t a keyword, incidentally. I’m just stealing some OOP terminology.[↩︎](structs-ii-more-fun-with-structs.html#fnref137)

  138. Assuming 8-bit `char`s, i.e. `CHAR_BIT == 8`.[↩︎](structs-ii-more-fun-with-structs.html#fnref138)

  139. https://en.wikipedia.org/wiki/Type_punning[↩︎](structs-ii-more-fun-with-structs.html#fnref139)

  140. I just made up that number, but it’s probably not far off[↩︎](characters-and-strings-ii.html#fnref140)

  141. There’s some devil in the details with values that are stored in registers only, but we can safely ignore that for our purposes here. Also the C spec makes no stance on these “register” things beyond the `register` keyword, the description for which doesn’t mention registers.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref141)

  142. You’re very likely to get different numbers on yours.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref142)

  143. There is absolutely nothing in the spec that says this will always work this way, but it happens to work this way on my system.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref143)

  144. Even if `E` is `NULL`, it turns out, weirdly.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref144)

  145. https://beej.us/guide/bgclr/html/split/stringref.html#man-memcpy[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref145)

  146. Your C compiler is not required to add padding bytes, and the values of any padding bytes that are added are indeterminate.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref146)

  147. This will vary depending on the architecture, but my system is _little endian_ , which means the least-significant byte of the number is stored first. _Big endian_ systems will have the `12` first and the `78` last. But the spec doesn’t dictate anything about this representation.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref147)

  148. It’s an optional feature, so it might not be there—but it probably is.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref148)

  149. I’m printing out the 16-bit values reversed since I’m on a little-endian machine and it makes it easier to read here.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref149)

  150. Assuming they point to the same array object.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref150)

  151. The Go Programming Language drew its type declaration syntax inspiration from the opposite of what C does.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref151)

  152. Not that other languages don’t do this—they do. It is interesting how many modern languages use the same operators for bitwise that C does.[↩︎](bitwise-operations.html#fnref152)

  153. https://en.wikipedia.org/wiki/Bitwise_operation[↩︎](bitwise-operations.html#fnref153)

  154. That is, us lowly developers aren’t supposed to know what’s in there or what it means. The spec doesn’t dictate what it is in detail.[↩︎](variadic-functions.html#fnref154)

  155. Honestly, it would be possible to remove that limitation from the language, but the idea is that the macros `va_start()`, `va_arg()`, and `va_end()` should be able to be written in C. And to make that happen, we need some way to initialize a pointer to the location of the first parameter. And to do that, we need the _name_ of the first parameter. It would require a language extension to make this possible, and so far the committee hasn’t found a rationale for doing so.[↩︎](variadic-functions.html#fnref155)

  156. “This planet has—or rather had—a problem, which was this: most of the people living on it were unhappy for pretty much of the time. Many solutions were suggested for this problem, but most of these were largely concerned with the movement of small green pieces of paper, which was odd because on the whole it wasn’t the small green pieces of paper that were unhappy.” —The Hitchhiker’s Guide to the Galaxy, Douglas Adams[↩︎](locale-and-internationalization.html#fnref156)

  157. Remember that `char` is just a byte-sized integer.[↩︎](locale-and-internationalization.html#fnref157)

  158. Except for `isdigit()` and `isxdigit()`.[↩︎](locale-and-internationalization.html#fnref158)

  159. For example, we could store the code point in a big-endian 32-bit integer. Straightforward! We just invented an encoding! Actually not; that’s what UTF-32BE encoding is. Oh well—back to the grind![↩︎](unicode-wide-characters-and-all-that.html#fnref159)

  160. Ish. Technically, it’s variable width—there’s a way to represent code points higher than \\(2^{16}\\) by putting two UTF-16 characters together.[↩︎](unicode-wide-characters-and-all-that.html#fnref160)

  161. There’s a special character called the _Byte Order Mark_ (BOM), code point 0xFEFF, that can optionally precede the data stream and indicate the endianess. It is not required, however.[↩︎](unicode-wide-characters-and-all-that.html#fnref161)

  162. Again, this is only true in UTF-16 for characters that fit in two bytes.[↩︎](unicode-wide-characters-and-all-that.html#fnref162)

  163. https://en.wikipedia.org/wiki/UTF-8[↩︎](unicode-wide-characters-and-all-that.html#fnref163)

  164. https://www.youtube.com/watch?v=MijmeoH9LT4[↩︎](unicode-wide-characters-and-all-that.html#fnref164)

  165. Presumably the compiler makes the best effort to translate the code point to whatever the output encoding is, but I can’t find any guarantees in the spec.[↩︎](unicode-wide-characters-and-all-that.html#fnref165)

  166. With a format specifier like `"%.12s"`, for example.[↩︎](unicode-wide-characters-and-all-that.html#fnref166)

  167. `wcscoll()` is the same as `wcsxfrm()` followed by `wcscmp()`.[↩︎](unicode-wide-characters-and-all-that.html#fnref167)

  168. Ish—things get funky with multi-`char16_t` UTF-16 encodings.[↩︎](unicode-wide-characters-and-all-that.html#fnref168)

  169. https://en.wikipedia.org/wiki/Iconv[↩︎](unicode-wide-characters-and-all-that.html#fnref169)

  170. http://site.icu-project.org/[↩︎](unicode-wide-characters-and-all-that.html#fnref170)

  171. https://en.wikipedia.org/wiki/Core_dump[↩︎](exiting-a-program.html#fnref171)

  172. Apparently it doesn’t do Unix-style signals at all deep down, and they’re simulated for console apps.[↩︎](signal-handling.html#fnref172)

  173. Confusingly, `sig_atomic_t` predates the lock-free atomics and is not the same thing.[↩︎](signal-handling.html#fnref173)

  174. If `sig_action_t` is signed, the range will be at least `-127` to `127`. If unsigned, at least `0` to `255`.[↩︎](signal-handling.html#fnref174)

  175. This is due to how VLAs are typically allocated on the stack, whereas `static` variables are on the heap. And the whole idea with VLAs is they’ll be automatically dellocated when the stack frame is popped at the end of the function.[↩︎](variable-length-arrays-vlas.html#fnref175)

  176. https://en.wikipedia.org/wiki/Goto#Criticism[↩︎](goto.html#fnref176)

  177. I’d like to point out that using `goto` in all these cases is avoidable. You can use variables and loops instead. It’s just that some people think `goto` produces the _best_ code in those circumstances.[↩︎](goto.html#fnref177)

  178. https://en.wikipedia.org/wiki/Tail_call[↩︎](goto.html#fnref178)

  179. Which isn’t quite the same, since it’s an array, not a pointer to an `int`.[↩︎](types-part-v-compound-literals-and-generic-selections.html#fnref179)

  180. A variable used here _is_ an expression.[↩︎](types-part-v-compound-literals-and-generic-selections.html#fnref180)

  181. Both “stack pointer” and “program counter” are related to the underlying architecture and C implementation, and are not part of the spec.[↩︎](setjmp-longjmp.html#fnref181)

  182. The rationale here is that the program might store a value temporarily in a _CPU register_ while it’s doing work on it. In that timeframe, the register holds the correct value, and the value on the stack might be out of date. Then later the register values would get overwritten and the changes to the variable lost.[↩︎](setjmp-longjmp.html#fnref182)

  183. That is, remain allocated until the program ends with no way to free it.[↩︎](setjmp-longjmp.html#fnref183)

  184. This works because in C, pointers are the same size regardless of the type of data they point to. So the compiler doesn’t need to know the size of the `struct node` at this point; it just needs to know the size of a pointer.[↩︎](incomplete-types.html#fnref184)

  185. https://en.wikipedia.org/wiki/Complex_number[↩︎](complex-numbers.html#fnref185)

  186. This was a harder one to research, and I’ll take any more information anyone can give me. `I` could be defined as `_Complex_I` or `_Imaginary_I`, if the latter exists. `_Imaginary_I` will handle signed zeros, but `_Complex_I` _might_ not. This has implications with branch cuts and other complex-numbery-mathy things. Maybe. Can you tell I’m really getting out of my element here? In any case, the `CMPLX()` macros behave as if `I` were defined as `_Imaginary_I`, with signed zeros, even if `_Imaginary_I` doesn’t exist on the system.[↩︎](complex-numbers.html#fnref186)

  187. The simplicity of this statement doesn’t do justice to the incredible amount of work that goes into simply understanding how floating point actually functions. https://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/[↩︎](complex-numbers.html#fnref187)

  188. This is the only one that doesn’t begin with an extra leading `c`, strangely.[↩︎](complex-numbers.html#fnref188)

  189. Some architectures have different sized data that the CPU and RAM can operate with at a faster rate than others. In those cases, if you need the fastest 8-bit number, it might give you have a 16- or 32-bit type instead because that’s just faster. So with this, you won’t know how big the type is, but it will be least as big as you say.[↩︎](fixed-width-integer-types.html#fnref189)

  190. Namely, the system has 8, 16, 32, or 64 bit integers with no padding that use two’s complement representation, in which case the `intN_t` variant for that particular number of bits _must_ be defined.[↩︎](fixed-width-integer-types.html#fnref190)

  191. On Earth, anyway. Who know what crazy systems they use _out there_ …[↩︎](date-and-time-functionality.html#fnref191)

  192. OK, don’t murder me! GMT is technically a time zone while UTC is a global time system. Also some countries might adjust GMT for daylight saving time, whereas UTC is never adjusted for daylight saving time.[↩︎](date-and-time-functionality.html#fnref192)

  193. Admittedly, there are more than two.[↩︎](date-and-time-functionality.html#fnref193)

  194. https://en.wikipedia.org/wiki/Unix_time[↩︎](date-and-time-functionality.html#fnref194)

  195. https://beej.us/guide/bgclr/html/split/time.html#man-strftime[↩︎](date-and-time-functionality.html#fnref195)

  196. You will on POSIX, where `time_t` is definitely an integer. Unfortunately the entire world isn’t POSIX, so there we are.[↩︎](date-and-time-functionality.html#fnref196)

  197. https://en.wikipedia.org/wiki/POSIX_Threads[↩︎](multithreading.html#fnref197)

  198. I’m more a fan of shared-nothing, myself, and my skills with classic multithreading constructs are rusty, to say the least.[↩︎](multithreading.html#fnref198)

  199. Yes, `pthreads` with a “`p`”. It’s short for POSIX threads, a library that C11 borrowed liberally from for its threads implementation.[↩︎](multithreading.html#fnref199)

  200. Per §7.1.4¶5.[↩︎](multithreading.html#fnref200)

  201. Unless you `thrd_detach()`. More on this later.[↩︎](multithreading.html#fnref201)

  202. Though I don’t think they have to be. It’s just that the threads don’t seem to get rescheduled until some system call like might happen with a `printf()`… which is why I have the `printf()` in there.[↩︎](multithreading.html#fnref202)

  203. Short for “mutual exclusion”, AKA a “lock” on a section of code that only one thread is permitted to execute.[↩︎](multithreading.html#fnref203)

  204. That is, your process will go to sleep.[↩︎](multithreading.html#fnref204)

  205. You might have expected it to be “time from now”, but you’d just like to think that, wouldn’t you![↩︎](multithreading.html#fnref205)

  206. And that’s why they’re called _condition variables_![↩︎](multithreading.html#fnref206)

  207. I’m not saying it’s aliens… but it’s aliens. OK, really more likely another thread might have been woken up and gotten to the work first.[↩︎](multithreading.html#fnref207)

  208. Survival of the fittest! Right? I admit it’s actually nothing like that.[↩︎](multithreading.html#fnref208)

  209. The `__STDC_VERSION__` macro didn’t exist in early C89, so if you’re worried about that, check it with `#ifdef`.[↩︎](chapter-atomics.html#fnref209)

  210. The reason for this is when optimized, my compiler has put the value of `x` in a register to make the `while` loop fast. But the register has no way of knowing that the variable was updated in another thread, so it never sees the `3490`. This isn’t really related to the _all-or-nothing_ part of atomicity, but is more related to the synchronization aspects in the next section.[↩︎](chapter-atomics.html#fnref210)

  211. Until I say otherwise, I’m speaking generally about _sequentially consistent_ operations. More on what that means soon.[↩︎](chapter-atomics.html#fnref211)

  212. Sanest from a programmer perspective.[↩︎](chapter-atomics.html#fnref212)

  213. Apparently C++23 is adding this as a macro.[↩︎](chapter-atomics.html#fnref213)

  214. The spec notes that they might differ in size, representation, and alignment.[↩︎](chapter-atomics.html#fnref214)

  215. I just pulled that example out of nowhere. Maybe it doesn’t matter on Intel/AMD, but it could matter somewhere, dangit![↩︎](chapter-atomics.html#fnref215)

  216. C++ elaborates that if the signal is the result of a call to `raise()`, it is sequenced _after_ the `raise()`.[↩︎](chapter-atomics.html#fnref216)

  217. https://en.wikipedia.org/wiki/Test-and-set[↩︎](chapter-atomics.html#fnref217)

  218. Because consume is all about the operations that are dependent on the value of the acquired atomic variable, and there is no atomic variable with a fence.[↩︎](chapter-atomics.html#fnref218)

  219. https://www.youtube.com/watch?v=A8eCGOqgvH4[↩︎](chapter-atomics.html#fnref219)

  220. https://www.youtube.com/watch?v=KeLBd2EJLOU[↩︎](chapter-atomics.html#fnref220)

  221. https://preshing.com/archives/[↩︎](chapter-atomics.html#fnref221)

  222. https://preshing.com/20120612/an-introduction-to-lock-free-programming/[↩︎](chapter-atomics.html#fnref222)

  223. https://preshing.com/20120913/acquire-and-release-semantics/[↩︎](chapter-atomics.html#fnref223)

  224. https://preshing.com/20130702/the-happens-before-relation/[↩︎](chapter-atomics.html#fnref224)

  225. https://preshing.com/20130823/the-synchronizes-with-relation/[↩︎](chapter-atomics.html#fnref225)

  226. https://preshing.com/20140709/the-purpose-of-memory_order_consume-in-cpp11/[↩︎](chapter-atomics.html#fnref226)

  227. https://preshing.com/20150402/you-can-do-any-kind-of-atomic-read-modify-write-operation/[↩︎](chapter-atomics.html#fnref227)

  228. https://en.cppreference.com/w/c/atomic/memory_order[↩︎](chapter-atomics.html#fnref228)

  229. https://en.cppreference.com/w/c/language/atomic[↩︎](chapter-atomics.html#fnref229)

  230. https://docs.microsoft.com/en-us/windows/win32/dxtecharts/lockless-programming[↩︎](chapter-atomics.html#fnref230)

  231. https://www.reddit.com/r/C_Programming/[↩︎](chapter-atomics.html#fnref231)

  232. Unless you compile with optimizations on (probably)! But I think when it does this, it’s not behaving to spec.[↩︎](function-specifiers-alignment-specifiersoperators.html#fnref232)

  233. https://beej.us/guide/bgclr/html/split/stdlib.html#man-exit[↩︎](function-specifiers-alignment-specifiersoperators.html#fnref233)

  234. https://beej.us/guide/bgclr/html/split/stdlib.html#man-abort[↩︎](function-specifiers-alignment-specifiersoperators.html#fnref234)

  235. https://en.wikipedia.org/wiki/Data_structure_alignment[↩︎](function-specifiers-alignment-specifiersoperators.html#fnref235)




* * *

[Prev](chapter-atomics.html) | [Contents](index.html) | [Next](function-specifiers-alignment-specifiersoperators.html)
