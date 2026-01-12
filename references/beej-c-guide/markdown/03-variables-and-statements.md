[Prev](hello-world.html) | [Contents](index.html) | [Next](functions.html)

* * *

# 3 Variables and Statements

> _“It takes all kinds to make a world, does it not, Padre?”_  
>  _“So it does, my son, so it does.”_
> 
> —Pirate Captain Thomas Bartholomew Red to the Padre, Pirates

There sure can be lotsa stuff in a C program.

Yup.

And for various reasons, it’ll be easier for all of us if we classify some of the types of things you can find in a program, so we can be clear what we’re talking about.

## 3.1 Variables

It’s said that “variables hold values”. But another way to think about it is that a variable is a human-readable name that refers to some data in memory.

We’re going to take a second here and take a peek down the rabbit hole that is pointers. Don’t worry about it.

You can think of memory as a big array of bytes[33](function-specifiers-alignment-specifiersoperators.html#fn33). Data is stored in this “array”[34](function-specifiers-alignment-specifiersoperators.html#fn34). If a number is larger than a single byte, it is stored in multiple bytes. Because memory is like an array, each byte of memory can be referred to by its index. This index into memory is also called an _address_ , or a _location_ , or a _pointer_.

When you have a variable in C, the value of that variable is in memory _somewhere_ , at some address. Of course. After all, where else would it be? But it’s a pain to refer to a value by its numeric address, so we make a name for it instead, and that’s what the variable is.

The reason I’m bringing all this up is twofold:

  1. It’s going to make it easier to understand pointer variables later—they’re variables that hold the address of other variables!
  2. Also, it’s going to make it easier to understand pointers later.



So a variable is a name for some data that’s stored in memory at some address.

### 3.1.1 Variable Names

You can use any characters in the range 0-9, A-Z, a-z, and underscore for variable names, with the following rules:

  * You can’t start a variable with a digit 0-9.
  * You can’t start a variable name with two underscores.
  * You can’t start a variable name with an underscore followed by a capital A-Z.



For Unicode, just try it. There are some rules in the spec in §D.2 that talk about which Unicode codepoint ranges are allowed in which parts of identifiers, but that’s too much to write about here and is probably something you’ll never have to think about anyway.

### 3.1.2 Variable Types

Depending on which languages you already have in your toolkit, you might or might not be familiar with the idea of types. But C’s kinda picky about them, so we should do a refresher.

Some example types, some of the most basic:

Type | Example | C Type  
---|---|---  
Integer | `3490` | `int`  
Floating point | `3.14159` | `float`[35](function-specifiers-alignment-specifiersoperators.html#fn35)  
Character (single) | `'c'` | `char`  
String | `"Hello, world!"` | `char *`[36](function-specifiers-alignment-specifiersoperators.html#fn36)  
  
C makes an effort to convert automatically between most numeric types when you ask it to. But other than that, all conversions are manual, notably between string and numeric.

Almost all of the types in C are variants on these types.

Before you can use a variable, you have to _declare_ that variable and tell C what type the variable holds. Once declared, the type of variable cannot be changed later at runtime. What you set it to is what it is until it falls out of scope and is reabsorbed into the universe.

Let’s take our previous “Hello, world” code and add a couple variables to it:
    
    
    [](variables-and-statements.html#cb10-1)#include <stdio.h>
    [](variables-and-statements.html#cb10-2)
    [](variables-and-statements.html#cb10-3)int main(void)
    [](variables-and-statements.html#cb10-4){
    [](variables-and-statements.html#cb10-5)    int i;    // Holds signed integers, e.g. -3, -2, 0, 1, 10
    [](variables-and-statements.html#cb10-6)    float f;  // Holds signed floating point numbers, e.g. -3.1416
    [](variables-and-statements.html#cb10-7)
    [](variables-and-statements.html#cb10-8)    printf("Hello, World!\n");  // Ah, blessed familiarity
    [](variables-and-statements.html#cb10-9)}

There! We’ve declared a couple of variables. We haven’t used them yet, and they’re both uninitialized. One holds an integer number, and the other holds a floating point number (a real number, basically, if you have a math background).

Uninitialized variables have indeterminate value[37](function-specifiers-alignment-specifiersoperators.html#fn37). They have to be initialized or else you must assume they contain some nonsense number.

> This is one of the places C can “get you”. Much of the time, in my experience, the indeterminate value is zero… but it can vary from run to run! Never assume the value will be zero, even if you see it is. _Always_ explicitly initialize variables to some value before you use them[38](function-specifiers-alignment-specifiersoperators.html#fn38).

What’s this? You want to store some numbers in those variables? Insanity!

Let’s go ahead and do that: 
    
    
    [](variables-and-statements.html#cb11-1)int main(void)
    [](variables-and-statements.html#cb11-2){
    [](variables-and-statements.html#cb11-3)    int i;
    [](variables-and-statements.html#cb11-4)
    [](variables-and-statements.html#cb11-5)    i = 2; // Assign the value 2 into the variable i
    [](variables-and-statements.html#cb11-6)
    [](variables-and-statements.html#cb11-7)    printf("Hello, World!\n");
    [](variables-and-statements.html#cb11-8)}

Killer. We’ve stored a value. Let’s print it.

We’re going to do that by passing _two_ amazing arguments to the `printf()` function. The first argument is a string that describes what to print and how to print it (called the _format string_), and the second is the value to print, namely whatever is in the variable `i`.

`printf()` hunts through the format string for a variety of special sequences which start with a percent sign (`%`) that tell it what to print. For example, if it finds a `%d`, it looks to the next parameter that was passed, and prints it out as an integer. If it finds a `%f`, it prints the value out as a float. If it finds a `%s`, it prints a string.

As such, we can print out the value of various types like so:
    
    
    [](variables-and-statements.html#cb12-1)#include <stdio.h>
    [](variables-and-statements.html#cb12-2)
    [](variables-and-statements.html#cb12-3)int main(void)
    [](variables-and-statements.html#cb12-4){
    [](variables-and-statements.html#cb12-5)    int i = 2;
    [](variables-and-statements.html#cb12-6)    float f = 3.14;
    [](variables-and-statements.html#cb12-7)    char *s = "Hello, world!";  // char * ("char pointer") is the string type
    [](variables-and-statements.html#cb12-8)
    [](variables-and-statements.html#cb12-9)    printf("%s  i = %d and f = %f!\n", s, i, f);
    [](variables-and-statements.html#cb12-10)}

And the output will be:
    
    
    [](variables-and-statements.html#cb13-1)Hello, world!  i = 2 and f = 3.14!

In this way, `printf()` might be similar to various types of format strings or parameterized strings in other languages you’re familiar with. 

### 3.1.3 Boolean Types

C has Boolean types, true or false?

`1`!

Historically, C didn’t have a Boolean type, and some might argue it still doesn’t.

In C, `0` means “false”, and non-zero means “true”.

So `1` is true. And `-37` is true. And `0` is false.

You can just declare Boolean types as `int`s:
    
    
    [](variables-and-statements.html#cb14-1)int x = 1;
    [](variables-and-statements.html#cb14-2)
    [](variables-and-statements.html#cb14-3)if (x) {
    [](variables-and-statements.html#cb14-4)    printf("x is true!\n");
    [](variables-and-statements.html#cb14-5)}

In C23, you get actual `bool`, `true`, and `false`. Before that, if you have a modern-enough version of C, you can `#include <stdbool.h>` to get the same thing.
    
    
    [](variables-and-statements.html#cb15-1)#include <stdio.h>
    [](variables-and-statements.html#cb15-2)#include <stdbool.h>  // not needed in C23
    [](variables-and-statements.html#cb15-3)
    [](variables-and-statements.html#cb15-4)int main(void) {
    [](variables-and-statements.html#cb15-5)    bool x = true;
    [](variables-and-statements.html#cb15-6)
    [](variables-and-statements.html#cb15-7)    if (x) {
    [](variables-and-statements.html#cb15-8)        printf("x is true!\n");
    [](variables-and-statements.html#cb15-9)    }
    [](variables-and-statements.html#cb15-10)}

While technically you should be setting a `bool` variable to `true`, `false`, or the result of some expression that evaluates to true or false, you can actually convert all kinds of things to `bool`. There are some specific rules, but zero-ish things tend to evaluate to `false`, and non-zero-ish things to true.

But be careful if you mix and match since the numeric value of `true` is `1`, probably[39](function-specifiers-alignment-specifiersoperators.html#fn39), and if you’re relying on some other positive value to be true, you might get a mismatch. For example:
    
    
    [](variables-and-statements.html#cb16-1)printf("%d\n", true == 12);  // Prints "0", false!

## 3.2 Operators and Expressions

C operators should be familiar to you from other languages. Let’s blast through some of them here.

(There are a bunch more details than this, but we’re going to do enough in this section to get started.)

### 3.2.1 Arithmetic

Hopefully these are familiar: 
    
    
    [](variables-and-statements.html#cb17-1)i = i + 3;  // Addition (+) and assignment (=) operators, add 3 to i
    [](variables-and-statements.html#cb17-2)i = i - 8;  // Subtraction, subtract 8 from i
    [](variables-and-statements.html#cb17-3)i = i * 9;  // Multiplication
    [](variables-and-statements.html#cb17-4)i = i / 2;  // Division
    [](variables-and-statements.html#cb17-5)i = i % 5;  // Modulo (division remainder)

There are shorthand variants for all of the above. Each of those lines could more tersely be written as: 
    
    
    [](variables-and-statements.html#cb18-1)i += 3;  // Same as "i = i + 3", add 3 to i
    [](variables-and-statements.html#cb18-2)i -= 8;  // Same as "i = i - 8"
    [](variables-and-statements.html#cb18-3)i *= 9;  // Same as "i = i * 9"
    [](variables-and-statements.html#cb18-4)i /= 2;  // Same as "i = i / 2"
    [](variables-and-statements.html#cb18-5)i %= 5;  // Same as "i = i % 5"

There is no exponentiation. You’ll have to use one of the `pow()` function variants from `math.h`.

Let’s get into some of the weirder stuff you might not have in your other languages!

### 3.2.2 Ternary Operator

C also includes the _ternary operator_. This is an expression whose value depends on the result of a conditional embedded in it.
    
    
    [](variables-and-statements.html#cb19-1)// If x > 10, add 17 to y. Otherwise add 37 to y.
    [](variables-and-statements.html#cb19-2)
    [](variables-and-statements.html#cb19-3)y += x > 10? 17: 37;

What a mess! You’ll get used to it the more you read it. To help out a bit, I’ll rewrite the above expression using `if` statements:
    
    
    [](variables-and-statements.html#cb20-1)// This expression:
    [](variables-and-statements.html#cb20-2)
    [](variables-and-statements.html#cb20-3)y += x > 10? 17: 37;
    [](variables-and-statements.html#cb20-4)
    [](variables-and-statements.html#cb20-5)// is equivalent to this non-expression:
    [](variables-and-statements.html#cb20-6)
    [](variables-and-statements.html#cb20-7)if (x > 10)
    [](variables-and-statements.html#cb20-8)    y += 17;
    [](variables-and-statements.html#cb20-9)else
    [](variables-and-statements.html#cb20-10)    y += 37;

Compare those two until you see each of the components of the ternary operator.

Or, another example that prints if a number stored in `x` is odd or even:
    
    
    [](variables-and-statements.html#cb21-1)printf("The number %d is %s.\n", x, x % 2 == 0? "even": "odd");

The `%s` format specifier in `printf()` means print a string. If the expression `x % 2` evaluates to `0`, the value of the entire ternary expression evaluates to the string `"even"`. Otherwise it evaluates to the string `"odd"`. Pretty cool!

It’s important to note that the ternary operator isn’t flow control like the `if` statement is. It’s just an expression that evaluates to a value. 

### 3.2.3 Pre-and-Post Increment-and-Decrement

Now, let’s mess with another thing that you might not have seen.

These are the legendary post-increment and post-decrement operators:
    
    
    [](variables-and-statements.html#cb22-1)i++;        // Add one to i (post-increment)
    [](variables-and-statements.html#cb22-2)i--;        // Subtract one from i (post-decrement)

Very commonly, these are just used as shorter versions of:
    
    
    [](variables-and-statements.html#cb23-1)i += 1;        // Add one to i
    [](variables-and-statements.html#cb23-2)i -= 1;        // Subtract one from i

but they’re more subtly different than that, the clever scoundrels.

Let’s take a look at this variant, pre-increment and pre-decrement:
    
    
    [](variables-and-statements.html#cb24-1)++i;        // Add one to i (pre-increment)
    [](variables-and-statements.html#cb24-2)--i;        // Subtract one from i (pre-decrement)

With pre-increment and pre-decrement, the value of the variable is incremented or decremented _before_ the expression is evaluated. Then the expression is evaluated with the new value.

With post-increment and post-decrement, the value of the expression is first computed with the value as-is, and _then_ the value is incremented or decremented after the value of the expression has been determined.

You can actually embed them in expressions, like this:
    
    
    [](variables-and-statements.html#cb25-1)i = 10;
    [](variables-and-statements.html#cb25-2)j = 5 + i++;  // Compute 5 + i, _then_ increment i
    [](variables-and-statements.html#cb25-3)
    [](variables-and-statements.html#cb25-4)printf("%d, %d\n", i, j);  // Prints 11, 15

Let’s compare this to the pre-increment operator:
    
    
    [](variables-and-statements.html#cb26-1)i = 10;
    [](variables-and-statements.html#cb26-2)j = 5 + ++i;  // Increment i, _then_ compute 5 + i
    [](variables-and-statements.html#cb26-3)
    [](variables-and-statements.html#cb26-4)printf("%d, %d\n", i, j);  // Prints 11, 16

This technique is used frequently with array and pointer access and manipulation. It gives you a way to use the value in a variable, and also increment or decrement that value before or after it is used.

But by far the most common place you’ll see this is in a `for` loop:
    
    
    [](variables-and-statements.html#cb27-1)for (i = 0; i < 10; i++)
    [](variables-and-statements.html#cb27-2)    printf("i is %d\n", i);

But more on that later. 

### 3.2.4 The Comma Operator

This is an uncommonly-used way to separate expressions that will run left to right:
    
    
    [](variables-and-statements.html#cb28-1)x = 10, y = 20;  // First assign 10 to x, then 20 to y

Seems a bit silly, since you could just replace the comma with a semicolon, right?
    
    
    [](variables-and-statements.html#cb29-1)x = 10; y = 20;  // First assign 10 to x, then 20 to y

But that’s a little different. The latter is two separate expressions, while the former is a single expression!

With the comma operator, the value of the comma expression is the value of the rightmost expression:
    
    
    [](variables-and-statements.html#cb30-1)x = (1, 2, 3);
    [](variables-and-statements.html#cb30-2)
    [](variables-and-statements.html#cb30-3)printf("x is %d\n", x);  // Prints 3, because 3 is rightmost in the comma list

But even that’s pretty contrived. One common place the comma operator is used is in `for` loops to do multiple things in each section of the statement:
    
    
    [](variables-and-statements.html#cb31-1)for (i = 0, j = 10; i < 100; i++, j++)
    [](variables-and-statements.html#cb31-2)    printf("%d, %d\n", i, j);

We’ll revisit that later. 

### 3.2.5 Conditional Operators

For Boolean values, we have a raft of standard operators: 
    
    
    [](variables-and-statements.html#cb32-1)a == b;  // True if a is equivalent to b
    [](variables-and-statements.html#cb32-2)a != b;  // True if a is not equivalent to b
    [](variables-and-statements.html#cb32-3)a < b;   // True if a is less than b
    [](variables-and-statements.html#cb32-4)a > b;   // True if a is greater than b
    [](variables-and-statements.html#cb32-5)a <= b;  // True if a is less than or equal to b
    [](variables-and-statements.html#cb32-6)a >= b;  // True if a is greater than or equal to b

Don’t mix up assignment (`=`) with comparison (`==`)! Use two equals to compare, one to assign.

We can use the comparison expressions with `if` statements:
    
    
    [](variables-and-statements.html#cb33-1)if (a <= 10)
    [](variables-and-statements.html#cb33-2)    printf("Success!\n");

### 3.2.6 Boolean Operators

We can chain together or alter conditional expressions with Boolean operators for _and_ , _or_ , and _not_. 

Operator | Boolean meaning  
---|---  
`&&` | and  
`||` | or  
`!` | not  
  
An example of Boolean “and”:
    
    
    [](variables-and-statements.html#cb34-1)// Do something if x less than 10 and y greater than 20:
    [](variables-and-statements.html#cb34-2)
    [](variables-and-statements.html#cb34-3)if (x < 10 && y > 20)
    [](variables-and-statements.html#cb34-4)    printf("Doing something!\n");

An example of Boolean “not”:
    
    
    [](variables-and-statements.html#cb35-1)if (!(x < 12))
    [](variables-and-statements.html#cb35-2)    printf("x is not less than 12\n");

`!` has higher precedence than the other Boolean operators, so we have to use parentheses in that case.

Of course, that’s just the same as:
    
    
    [](variables-and-statements.html#cb36-1)if (x >= 12)
    [](variables-and-statements.html#cb36-2)    printf("x is not less than 12\n");

but I needed the example! 

### 3.2.7 The `sizeof` Operator

This operator tells you the size (in bytes) that a particular variable or data type uses in memory.

More particularly, it tells you the size (in bytes) that the _type of a particular expression_ (which might be just a single variable) uses in memory.

This can be different on different systems, except for `char` and its variants (which are always 1 byte).

And this might not seem very useful now, but we’ll be making references to it here and there, so it’s worth covering.

Since this computes the number of bytes needed to store a type, you might think it would return an `int`. Or… since the size can’t be negative, maybe an `unsigned`?

But it turns out C has a special type to represent the return value from `sizeof`. It’s `size_t`, pronounced “ _size tee_ ”[40](function-specifiers-alignment-specifiersoperators.html#fn40). All we know is that it’s an unsigned integer type that can hold the size in bytes of anything you can give to `sizeof`.

`size_t` shows up a lot of different places where counts of things are passed or returned. Think of it as a value that represents a count. 

You can take the `sizeof` a variable or expression:
    
    
    [](variables-and-statements.html#cb37-1)int a = 999;
    [](variables-and-statements.html#cb37-2)
    [](variables-and-statements.html#cb37-3)// %zu is the format specifier for type size_t
    [](variables-and-statements.html#cb37-4)// If your compiler balks at the "z" part, leave it off
    [](variables-and-statements.html#cb37-5)
    [](variables-and-statements.html#cb37-6)printf("%zu\n", sizeof a);      // Prints 4 on my system
    [](variables-and-statements.html#cb37-7)printf("%zu\n", sizeof(2 + 7)); // Prints 4 on my system
    [](variables-and-statements.html#cb37-8)printf("%zu\n", sizeof 3.14);   // Prints 8 on my system
    [](variables-and-statements.html#cb37-9)
    [](variables-and-statements.html#cb37-10)// If you need to print out negative size_t values, use %zd

Remember: it’s the size in bytes of the _type_ of the expression, not the size of the expression itself. That’s why the size of `2+7` is the same as the size of `a`—they’re both type `int`. We’ll revisit this number `4` in the very next block of code…

…Where we’ll see you can take the `sizeof` a type (note the parentheses are required around a type name, unlike an expression):
    
    
    [](variables-and-statements.html#cb38-1)printf("%zu\n", sizeof(int));   // Prints 4 on my system
    [](variables-and-statements.html#cb38-2)printf("%zu\n", sizeof(char));  // Prints 1 on all systems

It’s important to note that `sizeof` is a _compile-time_ operation[41](function-specifiers-alignment-specifiersoperators.html#fn41). The result of the expression is determined entirely at compile-time, not at runtime.

We’ll make use of this later on. 

## 3.3 Flow Control

Booleans are all good, but of course we’re nowhere if we can’t control program flow. Let’s take a look at a number of constructs: `if`, `for`, `while`, and `do-while`.

First, a general forward-looking note about statements and blocks of statements brought to you by your local friendly C developer:

After something like an `if` or `while` statement, you can either put a single statement to be executed, or a block of statements to all be executed in sequence.

Let’s start with a single statement:
    
    
    [](variables-and-statements.html#cb39-1)if (x == 10) printf("x is 10\n");

This is also sometimes written on a separate line. (Whitespace is largely irrelevant in C—it’s not like Python.)
    
    
    [](variables-and-statements.html#cb40-1)if (x == 10)
    [](variables-and-statements.html#cb40-2)    printf("x is 10\n");

But what if you want multiple things to happen due to the conditional? You can use squirrelly braces to mark a _block_ or _compound statement_.
    
    
    [](variables-and-statements.html#cb41-1)if (x == 10) {
    [](variables-and-statements.html#cb41-2)    printf("x is 10\n");
    [](variables-and-statements.html#cb41-3)    printf("And also this happens when x is 10\n");
    [](variables-and-statements.html#cb41-4)}

It’s a really common style to _always_ use squirrelly braces even if they aren’t necessary:
    
    
    [](variables-and-statements.html#cb42-1)if (x == 10) {
    [](variables-and-statements.html#cb42-2)    printf("x is 10\n");
    [](variables-and-statements.html#cb42-3)}

Some devs feel the code is easier to read and avoids errors like this where things visually look like they’re in the `if` block, but actually they aren’t.
    
    
    [](variables-and-statements.html#cb43-1)// BAD ERROR EXAMPLE
    [](variables-and-statements.html#cb43-2)
    [](variables-and-statements.html#cb43-3)if (x == 10)
    [](variables-and-statements.html#cb43-4)    printf("This happens if x is 10\n");
    [](variables-and-statements.html#cb43-5)    printf("This happens ALWAYS\n");  // Surprise!! Unconditional!

`while` and `for` and the other looping constructs work the same way as the examples above. If you want to do multiple things in a loop or after an `if`, wrap them up in squirrelly braces.

In other words, the `if` is going to run the one thing after the `if`. And that one thing can be a single statement or a block of statements. 

### 3.3.1 The `if`-`else` statement

We’ve already been using `if` for multiple examples, since it’s likely you’ve seen it in a language before, but here’s another:
    
    
    [](variables-and-statements.html#cb44-1)int i = 10;
    [](variables-and-statements.html#cb44-2)
    [](variables-and-statements.html#cb44-3)if (i > 10) {
    [](variables-and-statements.html#cb44-4)    printf("Yes, i is greater than 10.\n");
    [](variables-and-statements.html#cb44-5)    printf("And this will also print if i is greater than 10.\n");
    [](variables-and-statements.html#cb44-6)}
    [](variables-and-statements.html#cb44-7)
    [](variables-and-statements.html#cb44-8)if (i <= 10) printf("i is less than or equal to 10.\n");

In the example code, the message will print if `i` is greater than 10, otherwise execution continues to the next line. Notice the squirrley braces after the `if` statement; if the condition is true, either the first statement or expression right after the if will be executed, or else the collection of code in the squirlley braces after the `if` will be executed. This sort of _code block_ behavior is common to all statements.

Of course, because C is fun this way, you can also do something if the condition is false with an `else` clause on your `if`:
    
    
    [](variables-and-statements.html#cb45-1)int i = 99;
    [](variables-and-statements.html#cb45-2)
    [](variables-and-statements.html#cb45-3)if (i == 10)
    [](variables-and-statements.html#cb45-4)    printf("i is 10!\n");
    [](variables-and-statements.html#cb45-5)else {
    [](variables-and-statements.html#cb45-6)    printf("i is decidedly not 10.\n");
    [](variables-and-statements.html#cb45-7)    printf("Which irritates me a little, frankly.\n");
    [](variables-and-statements.html#cb45-8)}

And you can even cascade these to test a variety of conditions, like this:
    
    
    [](variables-and-statements.html#cb46-1)int i = 99;
    [](variables-and-statements.html#cb46-2)
    [](variables-and-statements.html#cb46-3)if (i == 10)
    [](variables-and-statements.html#cb46-4)    printf("i is 10!\n");
    [](variables-and-statements.html#cb46-5)
    [](variables-and-statements.html#cb46-6)else if (i == 20)
    [](variables-and-statements.html#cb46-7)    printf("i is 20!\n");
    [](variables-and-statements.html#cb46-8)
    [](variables-and-statements.html#cb46-9)else if (i == 99) {
    [](variables-and-statements.html#cb46-10)    printf("i is 99! My favorite\n");
    [](variables-and-statements.html#cb46-11)    printf("I can't tell you how happy I am.\n");
    [](variables-and-statements.html#cb46-12)    printf("Really.\n");
    [](variables-and-statements.html#cb46-13)}
    [](variables-and-statements.html#cb46-14)    
    [](variables-and-statements.html#cb46-15)else
    [](variables-and-statements.html#cb46-16)    printf("i is some crazy number I've never heard of.\n");

Though if you’re going that route, be sure to check out the [`switch`](variables-and-statements.html#switch-statement) statement for a potentially better solution. The catch is `switch` only works with equality comparisons with constant numbers. The above `if`-`else` cascade could check inequality, ranges, variables, or anything else you can craft in a conditional expression. 

### 3.3.2 The `while` statement

`while` is your average run-of-the-mill looping construct. Do a thing while a condition expression is true.

Let’s do one!
    
    
    [](variables-and-statements.html#cb47-1)// Print the following output:
    [](variables-and-statements.html#cb47-2)//
    [](variables-and-statements.html#cb47-3)//   i is now 0!
    [](variables-and-statements.html#cb47-4)//   i is now 1!
    [](variables-and-statements.html#cb47-5)//   [ more of the same between 2 and 7 ]
    [](variables-and-statements.html#cb47-6)//   i is now 8!
    [](variables-and-statements.html#cb47-7)//   i is now 9!
    [](variables-and-statements.html#cb47-8)
    [](variables-and-statements.html#cb47-9)int i = 0;
    [](variables-and-statements.html#cb47-10)
    [](variables-and-statements.html#cb47-11)while (i < 10) {
    [](variables-and-statements.html#cb47-12)    printf("i is now %d!\n", i);
    [](variables-and-statements.html#cb47-13)    i++;
    [](variables-and-statements.html#cb47-14)}
    [](variables-and-statements.html#cb47-15)
    [](variables-and-statements.html#cb47-16)printf("All done!\n");

That gets you a basic loop. C also has a `for` loop which would have been cleaner for that example.

A not-uncommon use of `while` is for infinite loops where you repeat while true:
    
    
    [](variables-and-statements.html#cb48-1)while (1) {
    [](variables-and-statements.html#cb48-2)    printf("1 is always true, so this repeats forever.\n");
    [](variables-and-statements.html#cb48-3)}

### 3.3.3 The `do-while` statement

So now that we’ve gotten the `while` statement under control, let’s take a look at its closely related cousin, `do-while`.

They are basically the same, except if the loop condition is false on the first pass, `do-while` will execute once, but `while` won’t execute at all. In other words, the test to see whether or not to execute the block happens at the _end_ of the block with `do-while`. It happens at the _beginning_ of the block with `while`.

Let’s see by example:
    
    
    [](variables-and-statements.html#cb49-1)// Using a while statement:
    [](variables-and-statements.html#cb49-2)
    [](variables-and-statements.html#cb49-3)i = 10;
    [](variables-and-statements.html#cb49-4)
    [](variables-and-statements.html#cb49-5)// this is not executed because i is not less than 10:
    [](variables-and-statements.html#cb49-6)while(i < 10) {
    [](variables-and-statements.html#cb49-7)    printf("while: i is %d\n", i);
    [](variables-and-statements.html#cb49-8)    i++;
    [](variables-and-statements.html#cb49-9)}
    [](variables-and-statements.html#cb49-10)
    [](variables-and-statements.html#cb49-11)// Using a do-while statement:
    [](variables-and-statements.html#cb49-12)
    [](variables-and-statements.html#cb49-13)i = 10;
    [](variables-and-statements.html#cb49-14)
    [](variables-and-statements.html#cb49-15)// this is executed once, because the loop condition is not checked until
    [](variables-and-statements.html#cb49-16)// after the body of the loop runs:
    [](variables-and-statements.html#cb49-17)
    [](variables-and-statements.html#cb49-18)do {
    [](variables-and-statements.html#cb49-19)    printf("do-while: i is %d\n", i);
    [](variables-and-statements.html#cb49-20)    i++;
    [](variables-and-statements.html#cb49-21)} while (i < 10);
    [](variables-and-statements.html#cb49-22)
    [](variables-and-statements.html#cb49-23)printf("All done!\n");

Notice that in both cases, the loop condition is false right away. So in the `while`, the loop fails, and the following block of code is never executed. With the `do-while`, however, the condition is checked _after_ the block of code executes, so it always executes at least once. In this case, it prints the message, increments `i`, then fails the condition, and continues to the “All done!” output.

The moral of the story is this: if you want the loop to execute at least once, no matter what the loop condition, use `do-while`.

All these examples might have been better done with a `for` loop. Let’s do something less deterministic—repeat until a certain random number comes up!
    
    
    [](variables-and-statements.html#cb50-1)#include <stdio.h>   // For printf
    [](variables-and-statements.html#cb50-2)#include <stdlib.h>  // For rand
    [](variables-and-statements.html#cb50-3)
    [](variables-and-statements.html#cb50-4)int main(void)
    [](variables-and-statements.html#cb50-5){
    [](variables-and-statements.html#cb50-6)    int r;
    [](variables-and-statements.html#cb50-7)
    [](variables-and-statements.html#cb50-8)    do {
    [](variables-and-statements.html#cb50-9)        r = rand() % 100; // Get a random number between 0 and 99
    [](variables-and-statements.html#cb50-10)        printf("%d\n", r);
    [](variables-and-statements.html#cb50-11)    } while (r != 37);    // Repeat until 37 comes up
    [](variables-and-statements.html#cb50-12)}

Side note: did you run that more than once? If you did, did you notice the same sequence of numbers came up again. And again. And again? This is because `rand()` is a pseudorandom number generator that must be _seeded_ with a different number in order to generate a different sequence. Look up the [`srand()`](https://beej.us/guide/bgclr/html/split/stdlib.html#man-srand)[42](function-specifiers-alignment-specifiersoperators.html#fn42) function for more details. 

### 3.3.4 The `for` statement

Welcome to one of the most popular loops in the world! The `for` loop!

This is a great loop if you know the number of times you want to loop in advance.

You could do the same thing using just a `while` loop, but the `for` loop can help keep the code cleaner.

Here are two pieces of equivalent code—note how the `for` loop is just a more compact representation:
    
    
    [](variables-and-statements.html#cb51-1)// Print numbers between 0 and 9, inclusive...
    [](variables-and-statements.html#cb51-2)
    [](variables-and-statements.html#cb51-3)// Using a while statement:
    [](variables-and-statements.html#cb51-4)
    [](variables-and-statements.html#cb51-5)i = 0;
    [](variables-and-statements.html#cb51-6)while (i < 10) {
    [](variables-and-statements.html#cb51-7)    printf("i is %d\n", i);
    [](variables-and-statements.html#cb51-8)    i++;
    [](variables-and-statements.html#cb51-9)}
    [](variables-and-statements.html#cb51-10)
    [](variables-and-statements.html#cb51-11)// Do the exact same thing with a for-loop:
    [](variables-and-statements.html#cb51-12)
    [](variables-and-statements.html#cb51-13)for (i = 0; i < 10; i++) {
    [](variables-and-statements.html#cb51-14)    printf("i is %d\n", i);
    [](variables-and-statements.html#cb51-15)}

That’s right, folks—they do exactly the same thing. But you can see how the `for` statement is a little more compact and easy on the eyes. (JavaScript users will fully appreciate its C origins at this point.)

It’s split into three parts, separated by semicolons. The first is the initialization, the second is the loop condition, and the third is what should happen at the end of the block if the loop condition is true. All three of these parts are optional.
    
    
    [](variables-and-statements.html#cb52-1)for (initialize things; loop if this is true; do this after each loop)

Note that the loop will not execute even a single time if the loop condition starts off false.

> **`for`-loop fun fact!**
> 
> You can use the comma operator to do multiple things in each clause of the `for` loop!
>     
>     
>     [](variables-and-statements.html#cb53-1)for (i = 0, j = 999; i < 10; i++, j--) {
>     [](variables-and-statements.html#cb53-2)    printf("%d, %d\n", i, j);
>     [](variables-and-statements.html#cb53-3)}

An empty `for` will run forever:
    
    
    [](variables-and-statements.html#cb54-1)for(;;) {  // "forever"
    [](variables-and-statements.html#cb54-2)    printf("I will print this again and again and again\n" );
    [](variables-and-statements.html#cb54-3)    printf("for all eternity until the heat-death of the universe.\n");
    [](variables-and-statements.html#cb54-4)
    [](variables-and-statements.html#cb54-5)    printf("Or until you hit CTRL-C.\n");
    [](variables-and-statements.html#cb54-6)}

### 3.3.5 The `switch` Statement

Depending on what languages you’re coming from, you might or might not be familiar with `switch`, or C’s version might even be more restrictive than you’re used to. This is a statement that allows you to take a variety of actions depending on the value of an integer expression.

Basically, it evaluates an expression to an integer value, jumps to the `case` that corresponds to that value. Execution resumes from that point. If a `break` statement is encountered, then execution jumps out of the `switch`.

Here’s an example where, for a given number of goats, we print out a gut-feel of how many goats that is.
    
    
    [](variables-and-statements.html#cb55-1)#include <stdio.h>
    [](variables-and-statements.html#cb55-2)
    [](variables-and-statements.html#cb55-3)int main(void)
    [](variables-and-statements.html#cb55-4){
    [](variables-and-statements.html#cb55-5)    int goat_count = 2;
    [](variables-and-statements.html#cb55-6)
    [](variables-and-statements.html#cb55-7)    switch (goat_count) {
    [](variables-and-statements.html#cb55-8)        case 0:
    [](variables-and-statements.html#cb55-9)            printf("You have no goats.\n");
    [](variables-and-statements.html#cb55-10)            break;
    [](variables-and-statements.html#cb55-11)
    [](variables-and-statements.html#cb55-12)        case 1:
    [](variables-and-statements.html#cb55-13)            printf("You have a singular goat.\n");
    [](variables-and-statements.html#cb55-14)            break;
    [](variables-and-statements.html#cb55-15)
    [](variables-and-statements.html#cb55-16)        case 2:
    [](variables-and-statements.html#cb55-17)            printf("You have a brace of goats.\n");
    [](variables-and-statements.html#cb55-18)            break;
    [](variables-and-statements.html#cb55-19)
    [](variables-and-statements.html#cb55-20)        default:
    [](variables-and-statements.html#cb55-21)            printf("You have a bona fide plethora of goats!\n");
    [](variables-and-statements.html#cb55-22)            break;
    [](variables-and-statements.html#cb55-23)    }
    [](variables-and-statements.html#cb55-24)}

In that example, the `switch` will jump to the `case 2` and execute from there. When (if) it hits a `break`, it jumps out of the `switch`. 

Also, you might see that `default` label there at the bottom. This is what happens when no cases match.

Every `case`, including `default`, is optional. And they can occur in any order, but it’s really typical for `default`, if any, to be listed last.

So the whole thing acts like an `if`-`else` cascade:
    
    
    [](variables-and-statements.html#cb56-1)if (goat_count == 0)
    [](variables-and-statements.html#cb56-2)    printf("You have no goats.\n");
    [](variables-and-statements.html#cb56-3)else if (goat_count == 1)
    [](variables-and-statements.html#cb56-4)    printf("You have a singular goat.\n");
    [](variables-and-statements.html#cb56-5)else if (goat_count == 2)
    [](variables-and-statements.html#cb56-6)    printf("You have a brace of goats.\n");
    [](variables-and-statements.html#cb56-7)else
    [](variables-and-statements.html#cb56-8)    printf("You have a bona fide plethora of goats!\n");

With some key differences:

  * `switch` is often faster to jump to the correct code (though the spec makes no such guarantee).
  * `if`-`else` can do things like relational conditionals like `<` and `>=` and floating point and other types, while `switch` cannot.



There’s one more neat thing about switch that you sometimes see that is quite interesting: _fall through_.

Remember how `break` causes us to jump out of the switch?

Well, what happens if we _don’t_ `break`?

Turns out we just keep on going into the next `case`! Demo!
    
    
    [](variables-and-statements.html#cb57-1)switch (x) {
    [](variables-and-statements.html#cb57-2)    case 1:
    [](variables-and-statements.html#cb57-3)        printf("1\n");
    [](variables-and-statements.html#cb57-4)        // Fall through!
    [](variables-and-statements.html#cb57-5)    case 2:
    [](variables-and-statements.html#cb57-6)        printf("2\n");
    [](variables-and-statements.html#cb57-7)        break;
    [](variables-and-statements.html#cb57-8)    case 3:
    [](variables-and-statements.html#cb57-9)        printf("3\n");
    [](variables-and-statements.html#cb57-10)        break;
    [](variables-and-statements.html#cb57-11)}

If `x == 1`, this `switch` will first hit `case 1`, it’ll print the `1`, but then it just continues on to the next line of code… which prints `2`!

And then, at last, we hit a `break` so we jump out of the `switch`.

if `x == 2`, then we just hit the `case 2`, print `2`, and `break` as normal.

Not having a `break` is called _fall through_.

ProTip: _ALWAYS_ put a comment in the code where you intend to fall through, like I did above. It will save other programmers from wondering if you meant to do that. 

In fact, this is one of the common places to introduce bugs in C programs: forgetting to put a `break` in your `case`. You gotta do it if you don’t want to just roll into the next case[43](function-specifiers-alignment-specifiersoperators.html#fn43). 

Earlier I said that `switch` works with integer types—keep it that way. Don’t use floating point or string types in there. One loophole-ish thing here is that you can use character types because those are secretly integers themselves. So this is perfectly acceptable:
    
    
    [](variables-and-statements.html#cb58-1)char c = 'b';
    [](variables-and-statements.html#cb58-2)
    [](variables-and-statements.html#cb58-3)switch (c) {
    [](variables-and-statements.html#cb58-4)    case 'a':
    [](variables-and-statements.html#cb58-5)        printf("It's 'a'!\n");
    [](variables-and-statements.html#cb58-6)        break;
    [](variables-and-statements.html#cb58-7)
    [](variables-and-statements.html#cb58-8)    case 'b':
    [](variables-and-statements.html#cb58-9)        printf("It's 'b'!\n");
    [](variables-and-statements.html#cb58-10)        break;
    [](variables-and-statements.html#cb58-11)
    [](variables-and-statements.html#cb58-12)    case 'c':
    [](variables-and-statements.html#cb58-13)        printf("It's 'c'!\n");
    [](variables-and-statements.html#cb58-14)        break;
    [](variables-and-statements.html#cb58-15)}

Finally, you can use `enum`s in `switch` since they are also integer types. But more on that in the `enum` chapter.

* * *

[Prev](hello-world.html) | [Contents](index.html) | [Next](functions.html)
