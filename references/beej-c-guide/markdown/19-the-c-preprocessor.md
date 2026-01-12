[Prev](the-outside-environment.html) | [Contents](index.html) | [Next](structs-ii-more-fun-with-structs.html)

* * *

# 19 The C Preprocessor

Before your program gets compiled, it actually runs through a phase called _preprocessing_. It’s almost like there’s a language _on top_ of the C language that runs first. And it outputs the C code, which then gets compiled.

We’ve already seen this to an extent with `#include`! That’s the C Preprocessor! Where it sees that directive, it includes the named file right there, just as if you’d typed it in there. And _then_ the compiler builds the whole thing.

But it turns out it’s a lot more powerful than just being able to include things. You can define _macros_ that are substituted… and even macros that take arguments!

## 19.1 `#include`

Let’s start with the one we’ve already seen a bunch. This is, of course, a way to include other sources in your source. Very commonly used with header files.

While the spec allows for all kinds of behavior with `#include`, we’re going to take a more pragmatic approach and talk about the way it works on every system I’ve ever seen.

We can split header files into two categories: system and local. Things that are built-in, like `stdio.h`, `stdlib.h`, `math.h`, and so on, you can include with angle brackets:
    
    
    [](the-c-preprocessor.html#cb335-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb335-2)#include <stdlib.h>

The angle brackets tell C, “Hey, don’t look in the current directory for this header file—look in the system-wide include directory instead.”

Which, of course, implies that there must be a way to include local files from the current directory. And there is: with double quotes:
    
    
    [](the-c-preprocessor.html#cb336-1)#include "myheader.h"

Or you can very probably look in relative directories using forward slashes and dots, like this:
    
    
    [](the-c-preprocessor.html#cb337-1)#include "mydir/myheader.h"
    [](the-c-preprocessor.html#cb337-2)#include "../someheader.py"

Don’t use a backslash (`\`) for your path separators in your `#include`! It’s undefined behavior! Use forward slash (`/`) only, even on Windows.

In summary, used angle brackets (`<` and `>`) for the system includes, and use double quotes (`"`) for your personal includes.

## 19.2 Simple Macros

A _macro_ is an identifier that gets _expanded_ to another piece of code before the compiler even sees it. Think of it like a placeholder—when the preprocessor sees one of those identifiers, it replaces it with another value that you’ve defined.

We do this with `#define` (often read “pound define”, or perhaps “hash define”, but rarely, if ever, “octothorpe define”). Here’s an example:
    
    
    [](the-c-preprocessor.html#cb338-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb338-2)
    [](the-c-preprocessor.html#cb338-3)#define HELLO "Hello, world"
    [](the-c-preprocessor.html#cb338-4)#define PI 3.14159
    [](the-c-preprocessor.html#cb338-5)
    [](the-c-preprocessor.html#cb338-6)int main(void)
    [](the-c-preprocessor.html#cb338-7){
    [](the-c-preprocessor.html#cb338-8)    printf("%s, %f\n", HELLO, PI);
    [](the-c-preprocessor.html#cb338-9)}

On lines 3 and 4 we defined a couple macros. Wherever these appear elsewhere in the code (line 8), they’ll be substituted with the defined values.

From the C compiler’s perspective, it’s exactly as if we’d written this, instead:
    
    
    [](the-c-preprocessor.html#cb339-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb339-2)
    [](the-c-preprocessor.html#cb339-3)int main(void)
    [](the-c-preprocessor.html#cb339-4){
    [](the-c-preprocessor.html#cb339-5)    printf("%s, %f\n", "Hello, world", 3.14159);
    [](the-c-preprocessor.html#cb339-6)}

See how `HELLO` was replaced with `"Hello, world"` and `PI` was replaced with `3.14159`? From the compiler’s perspective, it’s just like those values had appeared right there in the code.

Note that the macros don’t have a specific type, _per se_. Really all that happens is they get replaced wholesale with whatever they’re `#define`d as. If the resulting C code is invalid, the compiler will puke.

You can also define a macro with no value:
    
    
    [](the-c-preprocessor.html#cb340-1)#define EXTRA_HAPPY

in that case, the macro exists and is defined, but is defined to be nothing. So anyplace it occurs in the text will just be replaced with nothing. We’ll see a use for this later.

It’s conventional to write macro names in `ALL_CAPS` even though that’s not technically required.

Overall, this gives you a way to define constant values that are effectively global and can be used _any_ place. Even in those places where a `const` variable won’t work, e.g. in `switch` `case`s and fixed array lengths.

That said, the debate rages online whether a typed `const` variable is better than `#define` macro in the general case.

It can also be used to replace or modify keywords, a concept completely foreign to `const`, though this practice should be used sparingly.

## 19.3 Conditional Compilation

It’s possible to get the preprocessor to decide whether or not to present certain blocks of code to the compiler, or just remove them entirely before compilation.

We do that by basically wrapping up the code in conditional blocks, similar to `if`-`else` statements.

### 19.3.1 If Defined, `#ifdef` and `#endif`

First of all, let’s try to compile specific code depending on whether or not a macro is even defined.
    
    
    [](the-c-preprocessor.html#cb341-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb341-2)
    [](the-c-preprocessor.html#cb341-3)#define EXTRA_HAPPY
    [](the-c-preprocessor.html#cb341-4)
    [](the-c-preprocessor.html#cb341-5)int main(void)
    [](the-c-preprocessor.html#cb341-6){
    [](the-c-preprocessor.html#cb341-7)
    [](the-c-preprocessor.html#cb341-8)#ifdef EXTRA_HAPPY
    [](the-c-preprocessor.html#cb341-9)    printf("I'm extra happy!\n");
    [](the-c-preprocessor.html#cb341-10)#endif
    [](the-c-preprocessor.html#cb341-11)
    [](the-c-preprocessor.html#cb341-12)    printf("OK!\n");
    [](the-c-preprocessor.html#cb341-13)}

In that example, we define `EXTRA_HAPPY` (to be nothing, but it _is_ defined), then on line 8 we check to see if it is defined with an `#ifdef` directive. If it is defined, the subsequent code will be included up until the `#endif`.

So because it is defined, the code will be included for compilation and the output will be:
    
    
    [](the-c-preprocessor.html#cb342-1)I'm extra happy!
    [](the-c-preprocessor.html#cb342-2)OK!

If we were to comment out the `#define`, like so:
    
    
    [](the-c-preprocessor.html#cb343-1)//#define EXTRA_HAPPY

then it wouldn’t be defined, and the code wouldn’t be included in compilation. And the output would just be:
    
    
    [](the-c-preprocessor.html#cb344-1)OK!

It’s important to remember that these decisions happen at compile time! The code actually gets compiled or removed depending on the condition. This is in contrast to a standard `if` statement that gets evaluated while the program is running.

### 19.3.2 If Not Defined, `#ifndef`

There’s also the negative sense of “if defined”: “if not defined”, or `#ifndef`. We could change the previous example to output different things based on whether or not something was defined:
    
    
    [](the-c-preprocessor.html#cb345-8)#ifdef EXTRA_HAPPY
    [](the-c-preprocessor.html#cb345-9)    printf("I'm extra happy!\n");
    [](the-c-preprocessor.html#cb345-10)#endif
    [](the-c-preprocessor.html#cb345-11)
    [](the-c-preprocessor.html#cb345-12)#ifndef EXTRA_HAPPY
    [](the-c-preprocessor.html#cb345-13)    printf("I'm just regular\n");
    [](the-c-preprocessor.html#cb345-14)#endif

We’ll see a cleaner way to do that in the next section.

Tying it all back in to header files, we’ve seen how we can cause header files to only be included one time by wrapping them in preprocessor directives like this:
    
    
    [](the-c-preprocessor.html#cb346-1)#ifndef MYHEADER_H  // First line of myheader.h
    [](the-c-preprocessor.html#cb346-2)#define MYHEADER_H
    [](the-c-preprocessor.html#cb346-3)
    [](the-c-preprocessor.html#cb346-4)int x = 12;
    [](the-c-preprocessor.html#cb346-5)
    [](the-c-preprocessor.html#cb346-6)#endif  // Last line of myheader.h

This demonstrates how a macro persists across files and multiple `#include`s. If it’s not yet defined, let’s define it and compile the whole header file.

But the next time it’s included, we see that `MYHEADER_H` _is_ defined, so we don’t send the header file to the compiler—it gets effectively removed.

### 19.3.3 `#else`

But that’s not all we can do! There’s also an `#else` that we can throw in the mix.

Let’s mod the previous example:
    
    
    [](the-c-preprocessor.html#cb347-8)#ifdef EXTRA_HAPPY
    [](the-c-preprocessor.html#cb347-9)    printf("I'm extra happy!\n");
    [](the-c-preprocessor.html#cb347-10)#else
    [](the-c-preprocessor.html#cb347-11)    printf("I'm just regular\n");
    [](the-c-preprocessor.html#cb347-12)#endif

Now if `EXTRA_HAPPY` is not defined, it’ll hit the `#else` clause and print:
    
    
    [](the-c-preprocessor.html#cb348-1)I'm just regular

### 19.3.4 Else-If: `#elifdef`, `#elifndef`

This feature is new in C23!

What if you want something more complex, though? Perhaps you need an if-else cascade structure to get your code built right?

Luckily we have these directives at our disposal. We can use `#elifdef` for “else if defined”:
    
    
    [](the-c-preprocessor.html#cb349-1)#ifdef MODE_1
    [](the-c-preprocessor.html#cb349-2)    printf("This is mode 1\n");
    [](the-c-preprocessor.html#cb349-3)#elifdef MODE_2
    [](the-c-preprocessor.html#cb349-4)    printf("This is mode 2\n");
    [](the-c-preprocessor.html#cb349-5)#elifdef MODE_3
    [](the-c-preprocessor.html#cb349-6)    printf("This is mode 3\n");
    [](the-c-preprocessor.html#cb349-7)#else
    [](the-c-preprocessor.html#cb349-8)    printf("This is some other mode\n");
    [](the-c-preprocessor.html#cb349-9)#endif

On the flipside, you can use `#elifndef` for “else if not defined”.

### 19.3.5 General Conditional: `#if`, `#elif`

This works very much like the `#ifdef` and `#ifndef` directives in that you can also have an `#else` and the whole thing wraps up with `#endif`.

The only difference is that the constant expression after the `#if` must evaluate to true (non-zero) for the code in the `#if` to be compiled. So instead of whether or not something is defined, we want an expression that evaluates to true.
    
    
    [](the-c-preprocessor.html#cb350-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb350-2)
    [](the-c-preprocessor.html#cb350-3)#define HAPPY_FACTOR 1
    [](the-c-preprocessor.html#cb350-4)
    [](the-c-preprocessor.html#cb350-5)int main(void)
    [](the-c-preprocessor.html#cb350-6){
    [](the-c-preprocessor.html#cb350-7)
    [](the-c-preprocessor.html#cb350-8)#if HAPPY_FACTOR == 0
    [](the-c-preprocessor.html#cb350-9)    printf("I'm not happy!\n");
    [](the-c-preprocessor.html#cb350-10)#elif HAPPY_FACTOR == 1
    [](the-c-preprocessor.html#cb350-11)    printf("I'm just regular\n");
    [](the-c-preprocessor.html#cb350-12)#else
    [](the-c-preprocessor.html#cb350-13)    printf("I'm extra happy!\n");
    [](the-c-preprocessor.html#cb350-14)#endif
    [](the-c-preprocessor.html#cb350-15)
    [](the-c-preprocessor.html#cb350-16)    printf("OK!\n");
    [](the-c-preprocessor.html#cb350-17)}

Again, for the unmatched `#if` clauses, the compiler won’t even see those lines. For the above code, after the preprocessor gets finished with it, all the compiler sees is:
    
    
    [](the-c-preprocessor.html#cb351-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb351-2)
    [](the-c-preprocessor.html#cb351-3)int main(void)
    [](the-c-preprocessor.html#cb351-4){
    [](the-c-preprocessor.html#cb351-5)
    [](the-c-preprocessor.html#cb351-6)    printf("I'm just regular\n");
    [](the-c-preprocessor.html#cb351-7)
    [](the-c-preprocessor.html#cb351-8)    printf("OK!\n");
    [](the-c-preprocessor.html#cb351-9)}

One hackish thing this is used for is to comment out large numbers of lines quickly[129](function-specifiers-alignment-specifiersoperators.html#fn129).

If you put an `#if 0` (“if false”) at the front of the block to be commented out and an `#endif` at the end, you can get this effect:
    
    
    [](the-c-preprocessor.html#cb352-1)#if 0
    [](the-c-preprocessor.html#cb352-2)    printf("All this code"); /* is effectively */
    [](the-c-preprocessor.html#cb352-3)    printf("commented out"); // by the #if 0
    [](the-c-preprocessor.html#cb352-4)#endif

What if you’re on a pre-C23 compiler and you don’t have `#elifdef` or `#elifndef` directive support? How can we get the same effect with `#if`? That is, what if I wanted this:
    
    
    [](the-c-preprocessor.html#cb353-1)#ifdef FOO
    [](the-c-preprocessor.html#cb353-2)    x = 2;
    [](the-c-preprocessor.html#cb353-3)#elifdef BAR  // POTENTIAL ERROR: Not supported before C23
    [](the-c-preprocessor.html#cb353-4)    x = 3;
    [](the-c-preprocessor.html#cb353-5)#endif

How could I do it?

Turns out there’s a preprocessor operator called `defined` that we can use with an `#if` statement.

These are equivalent:
    
    
    [](the-c-preprocessor.html#cb354-1)#ifdef FOO
    [](the-c-preprocessor.html#cb354-2)#if defined FOO
    [](the-c-preprocessor.html#cb354-3)#if defined(FOO)   // Parentheses optional

As are these:
    
    
    [](the-c-preprocessor.html#cb355-1)#ifndef FOO
    [](the-c-preprocessor.html#cb355-2)#if !defined FOO
    [](the-c-preprocessor.html#cb355-3)#if !defined(FOO)   // Parentheses optional

Notice how we can use the standard logical NOT operator (`!`) for “not defined”.

So now we’re back in `#if` land and we can use `#elif` with impunity!

This broken code:
    
    
    [](the-c-preprocessor.html#cb356-1)#ifdef FOO
    [](the-c-preprocessor.html#cb356-2)    x = 2;
    [](the-c-preprocessor.html#cb356-3)#elifdef BAR  // POTENTIAL ERROR: Not supported before C23
    [](the-c-preprocessor.html#cb356-4)    x = 3;
    [](the-c-preprocessor.html#cb356-5)#endif

can be replaced with:
    
    
    [](the-c-preprocessor.html#cb357-1)#if defined FOO
    [](the-c-preprocessor.html#cb357-2)    x = 2;
    [](the-c-preprocessor.html#cb357-3)#elif defined BAR
    [](the-c-preprocessor.html#cb357-4)    x = 3;
    [](the-c-preprocessor.html#cb357-5)#endif

### 19.3.6 Losing a Macro: `#undef`

If you’ve defined something but you don’t need it any longer, you can undefine it with `#undef`.
    
    
    [](the-c-preprocessor.html#cb358-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb358-2)
    [](the-c-preprocessor.html#cb358-3)int main(void)
    [](the-c-preprocessor.html#cb358-4){
    [](the-c-preprocessor.html#cb358-5)#define GOATS
    [](the-c-preprocessor.html#cb358-6)
    [](the-c-preprocessor.html#cb358-7)#ifdef GOATS
    [](the-c-preprocessor.html#cb358-8)    printf("Goats detected!\n");  // prints
    [](the-c-preprocessor.html#cb358-9)#endif
    [](the-c-preprocessor.html#cb358-10)
    [](the-c-preprocessor.html#cb358-11)#undef GOATS  // Make GOATS no longer defined
    [](the-c-preprocessor.html#cb358-12)
    [](the-c-preprocessor.html#cb358-13)#ifdef GOATS
    [](the-c-preprocessor.html#cb358-14)    printf("Goats detected, again!\n"); // doesn't print
    [](the-c-preprocessor.html#cb358-15)#endif
    [](the-c-preprocessor.html#cb358-16)}

## 19.4 Built-in Macros

The standard defines a lot of built-in macros that you can test and use for conditional compilation. Let’s look at those here.

### 19.4.1 Mandatory Macros

These are all defined:

Macro | Description  
---|---  
`__DATE__` | The date of compilation—like when you’re compiling this file—in `Mmm dd yyyy` format  
`__TIME__` | The time of compilation in `hh:mm:ss` format  
`__FILE__` | A string containing this file’s name  
`__LINE__` | The line number of the file this macro appears on  
`__func__` | The name of the function this appears in, as a string[130](function-specifiers-alignment-specifiersoperators.html#fn130)  
`__STDC__` | Defined with `1` if this is a standard C compiler  
`__STDC_HOSTED__` | This will be `1` if the compiler is a _hosted implementation_[ 131](function-specifiers-alignment-specifiersoperators.html#fn131), otherwise `0`  
`__STDC_VERSION__` | This version of C, a constant `long int` in the form `yyyymmL`, e.g. `201710L`  
  
Let’s put these together.
    
    
    [](the-c-preprocessor.html#cb359-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb359-2)
    [](the-c-preprocessor.html#cb359-3)int main(void)
    [](the-c-preprocessor.html#cb359-4){
    [](the-c-preprocessor.html#cb359-5)    printf("This function: %s\n", __func__);
    [](the-c-preprocessor.html#cb359-6)    printf("This file: %s\n", __FILE__);
    [](the-c-preprocessor.html#cb359-7)    printf("This line: %d\n", __LINE__);
    [](the-c-preprocessor.html#cb359-8)    printf("Compiled on: %s %s\n", __DATE__, __TIME__);
    [](the-c-preprocessor.html#cb359-9)    printf("C Version: %ld\n", __STDC_VERSION__);
    [](the-c-preprocessor.html#cb359-10)}

The output on my system is:
    
    
    [](the-c-preprocessor.html#cb360-1)This function: main
    [](the-c-preprocessor.html#cb360-2)This file: foo.c
    [](the-c-preprocessor.html#cb360-3)This line: 7
    [](the-c-preprocessor.html#cb360-4)Compiled on: Nov 23 2020 17:16:27
    [](the-c-preprocessor.html#cb360-5)C Version: 201710

`__FILE__`, `__func__` and `__LINE__` are particularly useful to report error conditions in messages to developers. The `assert()` macro in `<assert.h>` uses these to call out where in the code the assertion failed.

#### 19.4.1.1 `__STDC_VERSION__`s

In case you’re wondering, here are the version numbers for different major releases of the C Language Spec:

Release | ISO/IEC version | `__STDC_VERSION__`  
---|---|---  
C89 | ISO/IEC 9899:1990 | undefined  
**C89** | ISO/IEC 9899:1990/Amd.1:1995 | `199409L`  
**C99** | ISO/IEC 9899:1999 | `199901L`  
**C11** | ISO/IEC 9899:2011/Amd.1:2012 | `201112L`  
  
Note the macro did not exist originally in C89.

Also note that the plan is that the version numbers will strictly increase, so you could always check for, say, “at least C99” with:
    
    
    [](the-c-preprocessor.html#cb361-1)#if __STDC_VERSION__ >= 1999901L

### 19.4.2 Optional Macros

Your implementation might define these, as well. Or it might not.

Macro | Description  
---|---  
`__STDC_ISO_10646__` | If defined, `wchar_t` holds Unicode values, otherwise something else  
`__STDC_MB_MIGHT_NEQ_WC__` | A `1` indicates that the values in multibyte characters might not map equally to values in wide characters  
`__STDC_UTF_16__` | A `1` indicates that the system uses UTF-16 encoding in type `char16_t`  
`__STDC_UTF_32__` | A `1` indicates that the system uses UTF-32 encoding in type `char32_t`  
`__STDC_ANALYZABLE__` | A `1` indicates the code is analyzable[132](function-specifiers-alignment-specifiersoperators.html#fn132)  
`__STDC_IEC_559__` | `1` if IEEE-754 (aka IEC 60559) floating point is supported  
`__STDC_IEC_559_COMPLEX__` | `1` if IEC 60559 complex floating point is supported  
`__STDC_LIB_EXT1__` | `1` if this implementation supports a variety of “safe” alternate standard library functions (they have `_s` suffixes on the name)  
`__STDC_NO_ATOMICS__` | `1` if this implementation does **not** support `_Atomic` or `<stdatomic.h>`  
`__STDC_NO_COMPLEX__` | `1` if this implementation does **not** support complex types or `<complex.h>`  
`__STDC_NO_THREADS__` | `1` if this implementation does **not** support `<threads.h>`  
`__STDC_NO_VLA__` | `1` if this implementation does **not** support variable-length arrays  
  
## 19.5 Macros with Arguments

Macros are more powerful than simple substitution, though. You can set them up to take arguments that are substituted in, as well.

A question often arises for when to use parameterized macros versus functions. Short answer: use functions. But you’ll see lots of macros in the wild and in the standard library. People tend to use them for short, mathy things, and also for features that might change from platform to platform. You can define different keywords for one platform or another.

### 19.5.1 Macros with One Argument

Let’s start with a simple one that squares a number:
    
    
    [](the-c-preprocessor.html#cb362-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb362-2)
    [](the-c-preprocessor.html#cb362-3)#define SQR(x) x * x  // Not quite right, but bear with me
    [](the-c-preprocessor.html#cb362-4)
    [](the-c-preprocessor.html#cb362-5)int main(void)
    [](the-c-preprocessor.html#cb362-6){
    [](the-c-preprocessor.html#cb362-7)    printf("%d\n", SQR(12));  // 144
    [](the-c-preprocessor.html#cb362-8)}

What that’s saying is “everywhere you see `SQR` with some value, replace it with that value times itself”.

So line 7 will be changed to:
    
    
    [](the-c-preprocessor.html#cb363-7)    printf("%d\n", 12 * 12);  // 144

which C comfortably converts to 144.

But we’ve made an elementary error in that macro, one that we need to avoid.

Let’s check it out. What if we wanted to compute `SQR(3 + 4)`? Well, \\(3+4=7\\), so we must want to compute \\(7^2=49\\). That’s it; `49`—final answer.

Let’s drop it in our code and see that we get… 19?
    
    
    [](the-c-preprocessor.html#cb364-7)    printf("%d\n", SQR(3 + 4));  // 19!!??

What happened?

If we follow the macro expansion, we get
    
    
    [](the-c-preprocessor.html#cb365-7)    printf("%d\n", 3 + 4 * 3 + 4);  // 19!

Oops! Since multiplication takes precedence, we do the \\(4\times3=12\\) first, and get \\(3+12+4=19\\). Not what we were after.

So we have to fix this to make it right.

**This is so common that you should automatically do it every time you make a parameterized math macro!**

The fix is easy: just add some parentheses!
    
    
    [](the-c-preprocessor.html#cb366-3)#define SQR(x) (x) * (x)   // Better... but still not quite good enough!

And now our macro expands to:
    
    
    [](the-c-preprocessor.html#cb367-7)    printf("%d\n", (3 + 4) * (3 + 4));  // 49! Woo hoo!

But we actually still have the same problem which might manifest if we have a higher-precedence operator than multiply (`*`) nearby.

So the safe, proper way to put the macro together is to wrap the whole thing in additional parentheses, like so:
    
    
    [](the-c-preprocessor.html#cb368-3)#define SQR(x) ((x) * (x))   // Good!

Just make it a habit to do that when you make a math macro and you can’t go wrong.

### 19.5.2 Macros with More than One Argument

You can stack these things up as much as you want:
    
    
    [](the-c-preprocessor.html#cb369-1)#define TRIANGLE_AREA(w, h) (0.5 * (w) * (h))

Let’s do some macros that solve for \\(x\\) using the quadratic formula. Just in case you don’t have it on the top of your head, it says for equations of the form:

\\(ax^2+bx+c=0\\)

you can solve for \\(x\\) with the quadratic formula:

\\(x=\displaystyle\frac{-b\pm\sqrt{b^2-4ac}}{2a}\\)

Which is crazy. Also notice the plus-or-minus (\\(\pm\\)) in there, indicating that there are actually two solutions.

So let’s make macros for both:
    
    
    [](the-c-preprocessor.html#cb370-1)#define QUADP(a, b, c) ((-(b) + sqrt((b) * (b) - 4 * (a) * (c))) / (2 * (a)))
    [](the-c-preprocessor.html#cb370-2)#define QUADM(a, b, c) ((-(b) - sqrt((b) * (b) - 4 * (a) * (c))) / (2 * (a)))

So that gets us some math. But let’s define one more that we can use as arguments to `printf()` to print both answers.
    
    
    [](the-c-preprocessor.html#cb371-1)//          macro              replacement
    [](the-c-preprocessor.html#cb371-2)//      |-----------| |----------------------------|
    [](the-c-preprocessor.html#cb371-3)#define QUAD(a, b, c) QUADP(a, b, c), QUADM(a, b, c)

That’s just a couple values separated by a comma—and we can use that as a “combined” argument of sorts to `printf()` like this:
    
    
    [](the-c-preprocessor.html#cb372-1)printf("x = %f or x = %f\n", QUAD(2, 10, 5));

Let’s put it together into some code:
    
    
    [](the-c-preprocessor.html#cb373-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb373-2)#include <math.h>  // For sqrt()
    [](the-c-preprocessor.html#cb373-3)
    [](the-c-preprocessor.html#cb373-4)#define QUADP(a, b, c) ((-(b) + sqrt((b) * (b) - 4 * (a) * (c))) / (2 * (a)))
    [](the-c-preprocessor.html#cb373-5)#define QUADM(a, b, c) ((-(b) - sqrt((b) * (b) - 4 * (a) * (c))) / (2 * (a)))
    [](the-c-preprocessor.html#cb373-6)#define QUAD(a, b, c) QUADP(a, b, c), QUADM(a, b, c)
    [](the-c-preprocessor.html#cb373-7)
    [](the-c-preprocessor.html#cb373-8)int main(void)
    [](the-c-preprocessor.html#cb373-9){
    [](the-c-preprocessor.html#cb373-10)    printf("2*x^2 + 10*x + 5 = 0\n");
    [](the-c-preprocessor.html#cb373-11)    printf("x = %f or x = %f\n", QUAD(2, 10, 5));
    [](the-c-preprocessor.html#cb373-12)}

And this gives us the output:
    
    
    [](the-c-preprocessor.html#cb374-1)2*x^2 + 10*x + 5 = 0
    [](the-c-preprocessor.html#cb374-2)x = -0.563508 or x = -4.436492

Plugging in either of those values gives us roughly zero (a bit off because the numbers aren’t exact):

\\(2\times-0.563508^2+10\times-0.563508+5\approx0.000003\\)

### 19.5.3 Macros with Variable Arguments

There’s also a way to have a variable number of arguments passed to a macro, using ellipses (`...`) after the known, named arguments. When the macro is expanded, all of the extra arguments will be in a comma-separated list in the `__VA_ARGS__` macro, and can be replaced from there:
    
    
    [](the-c-preprocessor.html#cb375-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb375-2)
    [](the-c-preprocessor.html#cb375-3)// Combine the first two arguments to a single number,
    [](the-c-preprocessor.html#cb375-4)// then have a commalist of the rest of them:
    [](the-c-preprocessor.html#cb375-5)
    [](the-c-preprocessor.html#cb375-6)#define X(a, b, ...) (10*(a) + 20*(b)), __VA_ARGS__
    [](the-c-preprocessor.html#cb375-7)
    [](the-c-preprocessor.html#cb375-8)int main(void)
    [](the-c-preprocessor.html#cb375-9){
    [](the-c-preprocessor.html#cb375-10)    printf("%d %f %s %d\n", X(5, 4, 3.14, "Hi!", 12));
    [](the-c-preprocessor.html#cb375-11)}

The substitution that takes place on line 10 would be:
    
    
    [](the-c-preprocessor.html#cb376-10)    printf("%d %f %s %d\n", (10*(5) + 20*(4)), 3.14, "Hi!", 12);

for output:
    
    
    [](the-c-preprocessor.html#cb377-1)130 3.140000 Hi! 12

You can also “stringify” `__VA_ARGS__` by putting a `#` in front of it:
    
    
    [](the-c-preprocessor.html#cb378-1)#define X(...) #__VA_ARGS__
    [](the-c-preprocessor.html#cb378-2)
    [](the-c-preprocessor.html#cb378-3)printf("%s\n", X(1,2,3));  // Prints "1, 2, 3"

### 19.5.4 Stringification

Already mentioned, just above, you can turn any argument into a string by preceding it with a `#` in the replacement text.

For example, we could print anything as a string with this macro and `printf()`:
    
    
    [](the-c-preprocessor.html#cb379-1)#define STR(x) #x
    [](the-c-preprocessor.html#cb379-2)
    [](the-c-preprocessor.html#cb379-3)printf("%s\n", STR(3.14159));

In that case, the substitution leads to:
    
    
    [](the-c-preprocessor.html#cb380-1)printf("%s\n", "3.14159");

Let’s see if we can use this to greater effect so that we can pass any `int` variable name into a macro, and have it print out it’s name and value.
    
    
    [](the-c-preprocessor.html#cb381-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb381-2)
    [](the-c-preprocessor.html#cb381-3)#define PRINT_INT_VAL(x) printf("%s = %d\n", #x, x)
    [](the-c-preprocessor.html#cb381-4)
    [](the-c-preprocessor.html#cb381-5)int main(void)
    [](the-c-preprocessor.html#cb381-6){
    [](the-c-preprocessor.html#cb381-7)    int a = 5;
    [](the-c-preprocessor.html#cb381-8)
    [](the-c-preprocessor.html#cb381-9)    PRINT_INT_VAL(a);  // prints "a = 5"
    [](the-c-preprocessor.html#cb381-10)}

On line 9, we get the following macro replacement:
    
    
    [](the-c-preprocessor.html#cb382-9)    printf("%s = %d\n", "a", 5);

### 19.5.5 Concatenation

We can concatenate two arguments together with `##`, as well. Fun times!
    
    
    [](the-c-preprocessor.html#cb383-1)#define CAT(a, b) a ## b
    [](the-c-preprocessor.html#cb383-2)
    [](the-c-preprocessor.html#cb383-3)printf("%f\n", CAT(3.14, 1592));   // 3.141592

## 19.6 Multiline Macros

It’s possible to continue a macro to multiple lines if you escape the newline with a backslash (`\`).

Let’s write a multiline macro that prints numbers from `0` to the product of the two arguments passed in.
    
    
    [](the-c-preprocessor.html#cb384-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb384-2)
    [](the-c-preprocessor.html#cb384-3)#define PRINT_NUMS_TO_PRODUCT(a, b) do { \
    [](the-c-preprocessor.html#cb384-4)    int product = (a) * (b); \
    [](the-c-preprocessor.html#cb384-5)    for (int i = 0; i < product; i++) { \
    [](the-c-preprocessor.html#cb384-6)        printf("%d\n", i); \
    [](the-c-preprocessor.html#cb384-7)    } \
    [](the-c-preprocessor.html#cb384-8)} while(0)
    [](the-c-preprocessor.html#cb384-9)
    [](the-c-preprocessor.html#cb384-10)int main(void)
    [](the-c-preprocessor.html#cb384-11){
    [](the-c-preprocessor.html#cb384-12)    PRINT_NUMS_TO_PRODUCT(2, 4);  // Outputs numbers from 0 to 7
    [](the-c-preprocessor.html#cb384-13)}

A couple things to note there:

  * Escapes at the end of every line except the last one to indicate that the macro continues.
  * The whole thing is wrapped in a `do`-`while(0)` loop with squirrley braces.



The latter point might be a little weird, but it’s all about absorbing the trailing `;` the coder drops after the macro.

At first I thought that just using squirrely braces would be enough, but there’s a case where it fails if the coder puts a semicolon after the macro. Here’s that case:
    
    
    [](the-c-preprocessor.html#cb385-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb385-2)
    [](the-c-preprocessor.html#cb385-3)#define FOO(x) { (x)++; }
    [](the-c-preprocessor.html#cb385-4)
    [](the-c-preprocessor.html#cb385-5)int main(void)
    [](the-c-preprocessor.html#cb385-6){
    [](the-c-preprocessor.html#cb385-7)    int i = 0;
    [](the-c-preprocessor.html#cb385-8)
    [](the-c-preprocessor.html#cb385-9)    if (i == 0)
    [](the-c-preprocessor.html#cb385-10)        FOO(i);
    [](the-c-preprocessor.html#cb385-11)    else
    [](the-c-preprocessor.html#cb385-12)        printf(":-(\n");
    [](the-c-preprocessor.html#cb385-13)
    [](the-c-preprocessor.html#cb385-14)    printf("%d\n", i);
    [](the-c-preprocessor.html#cb385-15)}

Looks simple enough, but it won’t build without a syntax error:
    
    
    [](the-c-preprocessor.html#cb386-1)foo.c:11:5: error: ‘else’ without a previous ‘if’  

Do you see it?

Let’s look at the expansion:
    
    
    [](the-c-preprocessor.html#cb387-1)
    [](the-c-preprocessor.html#cb387-2)    if (i == 0) {
    [](the-c-preprocessor.html#cb387-3)        (i)++;
    [](the-c-preprocessor.html#cb387-4)    };             // <-- Trouble with a capital-T!
    [](the-c-preprocessor.html#cb387-5)
    [](the-c-preprocessor.html#cb387-6)    else
    [](the-c-preprocessor.html#cb387-7)        printf(":-(\n");

The `;` puts an end to the `if` statement, so the `else` is just floating out there illegally[133](function-specifiers-alignment-specifiersoperators.html#fn133).

So wrap that multiline macro with a `do`-`while(0)`.

## 19.7 Example: An Assert Macro

Adding asserts to your code is a good way to catch conditions that you think shouldn’t happen. C provides `assert()` functionality. It checks a condition, and if it’s false, the program bombs out telling you the file and line number on which the assertion failed.

But this is wanting.

  1. First of all, you can’t specify an additional message with the assert.
  2. Secondly, there’s no easy on-off switch for all the asserts.



We can address the first with macros.

Basically, when I have this code:
    
    
    [](the-c-preprocessor.html#cb388-1)ASSERT(x < 20, "x must be under 20");

I want something like this to happen (assuming the `ASSERT()` is on line 220 of `foo.c`):
    
    
    [](the-c-preprocessor.html#cb389-1)if (!(x < 20)) {
    [](the-c-preprocessor.html#cb389-2)    fprintf(stderr, "foo.c:220: assertion x < 20 failed: ");
    [](the-c-preprocessor.html#cb389-3)    fprintf(stderr, "x must be under 20\n");
    [](the-c-preprocessor.html#cb389-4)    exit(1);
    [](the-c-preprocessor.html#cb389-5)}

We can get the filename out of the `__FILE__` macro, and the line number from `__LINE__`. The message is already a string, but `x < 20` is not, so we’ll have to stringify it with `#`. We can make a multiline macro by using backslash escapes at the end of the line.
    
    
    [](the-c-preprocessor.html#cb390-1)#define ASSERT(c, m) \
    [](the-c-preprocessor.html#cb390-2)do { \
    [](the-c-preprocessor.html#cb390-3)    if (!(c)) { \
    [](the-c-preprocessor.html#cb390-4)        fprintf(stderr, __FILE__ ":%d: assertion %s failed: %s\n", \
    [](the-c-preprocessor.html#cb390-5)                        __LINE__, #c, m); \
    [](the-c-preprocessor.html#cb390-6)        exit(1); \
    [](the-c-preprocessor.html#cb390-7)    } \
    [](the-c-preprocessor.html#cb390-8)} while(0)

(It looks a little weird with `__FILE__` out front like that, but remember it is a string literal, and string literals next to each other are automagically concatenated. `__LINE__` on the other hand, it’s just an `int`.)

And that works! If I run this:
    
    
    [](the-c-preprocessor.html#cb391-1)int x = 30;
    [](the-c-preprocessor.html#cb391-2)
    [](the-c-preprocessor.html#cb391-3)ASSERT(x < 20, "x must be under 20");

I get this output:
    
    
    foo.c:23: assertion x < 20 failed: x must be under 20

Very nice!

The only thing left is a way to turn it on and off, and we could do that with conditional compilation.

Here’s the complete example:
    
    
    [](the-c-preprocessor.html#cb393-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb393-2)#include <stdlib.h>
    [](the-c-preprocessor.html#cb393-3)
    [](the-c-preprocessor.html#cb393-4)#define ASSERT_ENABLED 1
    [](the-c-preprocessor.html#cb393-5)
    [](the-c-preprocessor.html#cb393-6)#if ASSERT_ENABLED
    [](the-c-preprocessor.html#cb393-7)#define ASSERT(c, m) \
    [](the-c-preprocessor.html#cb393-8)do { \
    [](the-c-preprocessor.html#cb393-9)    if (!(c)) { \
    [](the-c-preprocessor.html#cb393-10)        fprintf(stderr, __FILE__ ":%d: assertion %s failed: %s\n", \
    [](the-c-preprocessor.html#cb393-11)                        __LINE__, #c, m); \
    [](the-c-preprocessor.html#cb393-12)        exit(1); \
    [](the-c-preprocessor.html#cb393-13)    } \
    [](the-c-preprocessor.html#cb393-14)} while(0)
    [](the-c-preprocessor.html#cb393-15)#else
    [](the-c-preprocessor.html#cb393-16)#define ASSERT(c, m)  // Empty macro if not enabled
    [](the-c-preprocessor.html#cb393-17)#endif
    [](the-c-preprocessor.html#cb393-18)
    [](the-c-preprocessor.html#cb393-19)int main(void)
    [](the-c-preprocessor.html#cb393-20){
    [](the-c-preprocessor.html#cb393-21)    int x = 30;
    [](the-c-preprocessor.html#cb393-22)
    [](the-c-preprocessor.html#cb393-23)    ASSERT(x < 20, "x must be under 20");
    [](the-c-preprocessor.html#cb393-24)}

This has the output:
    
    
    [](the-c-preprocessor.html#cb394-1)foo.c:23: assertion x < 20 failed: x must be under 20

## 19.8 The `#error` Directive

This directive causes the compiler to error out as soon as it sees it.

Commonly, this is used inside a conditional to prevent compilation unless some prerequisites are met:
    
    
    [](the-c-preprocessor.html#cb395-1)#ifndef __STDC_IEC_559__
    [](the-c-preprocessor.html#cb395-2)    #error I really need IEEE-754 floating point to compile. Sorry!
    [](the-c-preprocessor.html#cb395-3)#endif

Some compilers have a non-standard complementary `#warning` directive that will output a warning but not stop compilation, but this is not in the C11 spec.

## 19.9 The `#embed` Directive

New in C23!

And currently not yet working with any of my compilers, so take this section with a grain of salt!

The gist of this is that you can include bytes of a file as integer constants as if you’d typed them in.

For example, if you have a binary file named `foo.bin` that contains four bytes with decimal values 11, 22, 33, and 44, and you do this:
    
    
    [](the-c-preprocessor.html#cb396-1)int a[] = {
    [](the-c-preprocessor.html#cb396-2)#embed "foo.bin"
    [](the-c-preprocessor.html#cb396-3)};

It’ll be just as if you’d typed this:
    
    
    [](the-c-preprocessor.html#cb397-1)int a[] = {11,22,33,44};

This is a really powerful way to initialize an array with binary data without needing to convert it all to code first—the preprocessor does it for you!

A more typical use case might be a file containing a small image to be displayed that you don’t want to load at runtime.

Here’s another example:
    
    
    [](the-c-preprocessor.html#cb398-1)int a[] = {
    [](the-c-preprocessor.html#cb398-2)#embed <foo.bin>
    [](the-c-preprocessor.html#cb398-3)};

If you use angle brackets, the preprocessor looks in a series of implementation-defined places to locate the file, just like `#include` would do. If you use double quotes and the resource is not found, the compiler will try it as if you’d used angle brackets in a last desperate attempt to find the file.

`#embed` works like `#include` in that it effectively pastes values in before the compiler sees them. This means you can use it in all kinds of places:
    
    
    return
    #embed "somevalue.dat"
    ;

or
    
    
    int x =
    #embed "xvalue.dat"
    ;

Now—are these always bytes? Meaning they’ll have values from 0 to 255, inclusive? The answer is definitely by default “yes”, except when it is “no”.

Technically, the elements will be `CHAR_BIT` bits wide. And this is very likely 8 on your system, so you’d get that 0-255 range in your values. (They’ll always be non-negative.)

Also, it’s possible that an implementation might allow this to be overridden in some way, e.g. on the command line or with parameters.

The size of the file in bits must be a multiple of the element size. That is, if each element is 8 bits, the file size (in bits) must be a multiple of 8. In regular everyday usage, this is a confusing way of saying that each file needs to be an integer number of bytes… which of course it is. Honestly, I’m not even sure why I bothered with this paragraph. Read the spec if you’re really that curious.

### 19.9.1 `#embed` Parameters

There are all kinds of parameters you can specify to the `#embed` directive. Here’s an example with the yet-unintroduced `limit()` parameter:
    
    
    [](the-c-preprocessor.html#cb401-1)int a[] = {
    [](the-c-preprocessor.html#cb401-2)#embed "/dev/random" limit(5)
    [](the-c-preprocessor.html#cb401-3)};

But what if you already have `limit` defined somewhere else? Luckily you can put `__` around the keyword and it will work the same way:
    
    
    [](the-c-preprocessor.html#cb402-1)int a[] = {
    [](the-c-preprocessor.html#cb402-2)#embed "/dev/random" __limit__(5)
    [](the-c-preprocessor.html#cb402-3)};

Now… what’s this `limit` thing?

### 19.9.2 The `limit()` Parameter

You can specify a limit on the number of elements to embed with this parameter.

This is a maximum value, not an absolute value. If the file that’s embedded is shorter than the specified limit, only that many bytes will be imported.

The `/dev/random` example above is an example of the motivation for this—in Unix, that’s a _character device file_ that will return an infinite stream of pretty-random numbers.

Embedding an infinite number of bytes is hard on your RAM, so the `limit` parameter gives you a way to stop after a certain number.

Finally, you are allowed to use `#define` macros in your `limit`, in case you were curious.

### 19.9.3 The `if_empty` Parameter

This parameter defines what the embed result should be if the file exists but contains no data. Let’s say that the file `foo.dat` contains a single byte with the value 123. If we do this:
    
    
    [](the-c-preprocessor.html#cb403-1)int x = 
    [](the-c-preprocessor.html#cb403-2)#embed "foo.dat" if_empty(999)
    [](the-c-preprocessor.html#cb403-3);

we’ll get:
    
    
    [](the-c-preprocessor.html#cb404-1)int x = 123;   // When foo.dat contains a 123 byte

But what if the file `foo.dat` is zero bytes long (i.e. contains no data and is empty)? If that’s the case, it would expand to:
    
    
    [](the-c-preprocessor.html#cb405-1)int x = 999;   // When foo.dat is empty

Notably if the `limit` is set to `0`, then the `if_empty` will always be substituted. That is, a zero limit effectively means the file is empty.

This will always emit `x = 999` no matter what’s in `foo.dat`:
    
    
    [](the-c-preprocessor.html#cb406-1)int x = 
    [](the-c-preprocessor.html#cb406-2)#embed "foo.dat" limit(0) if_empty(999)
    [](the-c-preprocessor.html#cb406-3);

### 19.9.4 The `prefix()` and `suffix()` Parameters

This is a way to prepend some data on the embed.

Note that these only affect non-empty data! If the file is empty, neither `prefix` nor `suffix` has any effect.

Here’s an example where we embed three random numbers, but prefix the numbers with `11,` and suffix them with `,99`:
    
    
    [](the-c-preprocessor.html#cb407-1)int x[] = {
    [](the-c-preprocessor.html#cb407-2)#embed "/dev/urandom" limit(3) prefix(11,) suffix(,99)
    [](the-c-preprocessor.html#cb407-3)};

Example result:
    
    
    [](the-c-preprocessor.html#cb408-1)int x[] = {11,135,116,220,99};

There’s no requirement that you use both `prefix` and `suffix`. You can use both, one, the other, or neither.

We can make use of the characteristic that these are only applied to non-empty files to neat effect, as shown in the following example shamelessly stolen from the spec.

Let’s say we have a file `foo.dat` that has some data it in. And we want to use this to initialize an array, and then we want a suffix on the array that is a zero element.

No problem, right?
    
    
    [](the-c-preprocessor.html#cb409-1)int x[] = {
    [](the-c-preprocessor.html#cb409-2)#embed "foo.dat" suffix(,0)
    [](the-c-preprocessor.html#cb409-3)};

If `foo.dat` has 11, 22, and 33 in it, we’d get:
    
    
    [](the-c-preprocessor.html#cb410-1)int x[] = {11,22,33,0};

But wait! What if `foo.dat` is empty? Then we get:
    
    
    [](the-c-preprocessor.html#cb411-1)int x[] = {};

and that’s not good.

But we can fix it like this:
    
    
    [](the-c-preprocessor.html#cb412-1)int x[] = {
    [](the-c-preprocessor.html#cb412-2)#embed "foo.dat" suffix(,)
    [](the-c-preprocessor.html#cb412-3)    0
    [](the-c-preprocessor.html#cb412-4)};

Since the `suffix` parameter is omitted if the file is empty, this would just turn into:
    
    
    [](the-c-preprocessor.html#cb413-1)int x[] = {0};

which is fine.

### 19.9.5 The `__has_embed()` Identifier

This is a great way to test to see if a particular file is available to be embedded, and also whether or not it’s empty.

You use it with the `#if` directive.

Here’s a chunk of code that will get 5 random numbers from the random number generator character device. If that doesn’t exist, it tries to get them from a file `myrandoms.dat`. If that doesn’t exist, it uses some hard-coded values:
    
    
    [](the-c-preprocessor.html#cb414-1)    int random_nums[] = {
    [](the-c-preprocessor.html#cb414-2)#if __has_embed("/dev/urandom")
    [](the-c-preprocessor.html#cb414-3)    #embed "/dev/urandom" limit(5)
    [](the-c-preprocessor.html#cb414-4)#elif __has_embed("myrandoms.dat")
    [](the-c-preprocessor.html#cb414-5)    #embed "myrandoms.dat" limit(5)
    [](the-c-preprocessor.html#cb414-6)#else
    [](the-c-preprocessor.html#cb414-7)    140,178,92,167,120
    [](the-c-preprocessor.html#cb414-8)#endif
    [](the-c-preprocessor.html#cb414-9)    };

Technically, the `__has_embed()` identifier resolves to one of three values:

`__has_embed()` Result | Description  
---|---  
`__STDC_EMBED_NOT_FOUND__` | If the file isn’t found.  
`__STDC_EMBED_FOUND__` | If the file is found and is not empty.  
`__STDC_EMBED_EMPTY` | If the file is found and is empty.  
  
I have good reason to believe that `__STDC_EMBED_NOT_FOUND__` is `0` and the others aren’t zero (because it’s implied in the proposal and it makes logical sense), but I’m having trouble finding that in this version of the draft spec.

TODO

### 19.9.6 Other Parameters

A compiler implementation can define other embed parameters all it wants—look for these non-standard parameters in your compiler’s documentation.

For instance:
    
    
    [](the-c-preprocessor.html#cb415-1)#embed "foo.bin" limit(12) frotz(lamp)

These might commonly have a prefix on them to help with namespacing:
    
    
    [](the-c-preprocessor.html#cb416-1)#embed "foo.bin" limit(12) fmc::frotz(lamp)

It might be sensible to try to detect if these are available before you use them, and luckily we can use `__has_embed` to help us here.

Normally, `__has_embed()` will just tell us if the file is there or not. But—and here’s the fun bit—it will also return false if any additional parameters are also not supported!

So if we give it a file that we _know_ exists as well as a parameter that we want to test for the existence of, it will effectively tell us if that parameter is supported.

What file _always_ exists, though? Turns out we can use the `__FILE__` macro, which expands to the name of the source file that references it! That file _must_ exist, or something is seriously wrong in the chicken-and-egg department.

Let’s test that `frotz` parameter to see if we can use it:
    
    
    [](the-c-preprocessor.html#cb417-1)#if __has_embed(__FILE__ fmc::frotz(lamp))
    [](the-c-preprocessor.html#cb417-2)    puts("fmc::frotz(lamp) is supported!");
    [](the-c-preprocessor.html#cb417-3)#else
    [](the-c-preprocessor.html#cb417-4)    puts("fmc::frotz(lamp) is NOT supported!");
    [](the-c-preprocessor.html#cb417-5)#endif

### 19.9.7 Embedding Multi-Byte Values

What about getting some `int`s in there instead of individual bytes? What about multi-byte values in the embedded file?

This is not something supported by the C23 standard, but there could be implementation extensions defined for it in the future.

## 19.10 The `#pragma` Directive

This is one funky directive, short for “pragmatic”. You can use it to do… well, anything your compiler supports you doing with it.

Basically the only time you’re going to add this to your code is if some documentation tells you to do so.

### 19.10.1 Non-Standard Pragmas

Here’s one non-standard example of using `#pragma` to cause the compiler to execute a `for` loop in parallel with multiple threads (if the compiler supports the [OpenMP](https://www.openmp.org/)[134](function-specifiers-alignment-specifiersoperators.html#fn134) extension):
    
    
    [](the-c-preprocessor.html#cb418-1)#pragma omp parallel for
    [](the-c-preprocessor.html#cb418-2)for (int i = 0; i < 10; i++) { ... }

There are all kinds of `#pragma` directives documented across all four corners of the globe.

All unrecognized `#pragma`s are ignored by the compiler.

### 19.10.2 Standard Pragmas

There are also a few standard ones, and these start with `STDC`, and follow the same form:
    
    
    [](the-c-preprocessor.html#cb419-1)#pragma STDC pragma_name on-off

The `on-off` portion can be either `ON`, `OFF`, or `DEFAULT`.

And the `pragma_name` can be one of these:

Pragma Name | Description  
---|---  
`FP_CONTRACT` | Allow floating point expressions to be contracted into a single operation to avoid rounding errors that might occur from multiple operations.  
`FENV_ACCESS` | Set to `ON` if you plan to access the floating point status flags. If `OFF`, the compiler might perform optimizations that cause the values in the flags to be inconsistent or invalid.  
`CX_LIMITED_RANGE` | Set to `ON` to allow the compiler to skip overflow checks when performing complex arithmetic. Defaults to `OFF`.  
  
For example:
    
    
    [](the-c-preprocessor.html#cb420-1)#pragma STDC FP_CONTRACT OFF
    [](the-c-preprocessor.html#cb420-2)#pragma STDC CX_LIMITED_RANGE ON

As for `CX_LIMITED_RANGE`, the spec points out:

> The purpose of the pragma is to allow the implementation to use the formulas:
> 
> \\((x+iy)\times(u+iv) = (xu-yv)+i(yu+xv)\\)
> 
> \\((x+iy)/(u+iv) = [(xu+yv)+i(yu-xv)]/(u^2+v^2)\\)
> 
> \\(|x+iy|=\sqrt{x^2+y^2}\\)
> 
> where the programmer can determine they are safe.

### 19.10.3 `_Pragma` Operator

This is another way to declare a pragma that you could use in a macro.

These are equivalent:
    
    
    [](the-c-preprocessor.html#cb421-1)#pragma "Unnecessary" quotes
    [](the-c-preprocessor.html#cb421-2)_Pragma("\"Unnecessary\" quotes")

This can be used in a macro, if need be:
    
    
    [](the-c-preprocessor.html#cb422-1)#define PRAGMA(x) _Pragma(#x)

## 19.11 The `#line` Directive

This allows you to override the values for `__LINE__` and `__FILE__`. If you want.

I’ve never wanted to do this, but in K&R2, they write:

> For the benefit of other preprocessors that generate C programs […]

So maybe there’s that.

To override the line number to, say 300:
    
    
    [](the-c-preprocessor.html#cb423-1)#line 300

and `__LINE__` will keep counting up from there.

To override the line number and the filename:
    
    
    [](the-c-preprocessor.html#cb424-1)#line 300 "newfilename"

## 19.12 The Null Directive

A `#` on a line by itself is ignored by the preprocessor. Now, to be entirely honest, I don’t know what the use case is for this.

I’ve seen examples like this:
    
    
    [](the-c-preprocessor.html#cb425-1)#ifdef FOO
    [](the-c-preprocessor.html#cb425-2)    #
    [](the-c-preprocessor.html#cb425-3)#else
    [](the-c-preprocessor.html#cb425-4)    printf("Something");
    [](the-c-preprocessor.html#cb425-5)#endif

which is just cosmetic; the line with the solitary `#` can be deleted with no ill effect.

Or maybe for cosmetic consistency, like this:
    
    
    [](the-c-preprocessor.html#cb426-1)#
    [](the-c-preprocessor.html#cb426-2)#ifdef FOO
    [](the-c-preprocessor.html#cb426-3)    x = 2;
    [](the-c-preprocessor.html#cb426-4)#endif
    [](the-c-preprocessor.html#cb426-5)#
    [](the-c-preprocessor.html#cb426-6)#if BAR == 17
    [](the-c-preprocessor.html#cb426-7)    x = 12;
    [](the-c-preprocessor.html#cb426-8)#endif
    [](the-c-preprocessor.html#cb426-9)#

But, with respect to cosmetics, that’s just ugly.

Another post mentions elimination of comments—that in GCC, a comment after a `#` will not be seen by the compiler. Which I don’t doubt, but the specification doesn’t seem to say this is standard behavior.

My searches for rationale aren’t bearing much fruit. So I’m going to just say this is some good ol’ fashioned C esoterica.

* * *

[Prev](the-outside-environment.html) | [Contents](index.html) | [Next](structs-ii-more-fun-with-structs.html)
