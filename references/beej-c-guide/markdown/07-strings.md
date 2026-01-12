[Prev](arrays.html) | [Contents](index.html) | [Next](structs.html)

* * *

# 7 Strings

Finally! Strings! What could be simpler?

Well, turns out strings aren’t actually strings in C. That’s right! They’re pointers! Of course they are!

Much like arrays, strings in C _barely exist_.

But let’s check it out—it’s not really such a big deal.

## 7.1 String Literals

Before we start, let’s talk about string literals in C. These are sequences of characters in _double_ quotes (`"`). (Single quotes enclose characters, and are a different animal entirely.)

Examples:
    
    
    [](strings.html#cb112-1)"Hello, world!\n"
    [](strings.html#cb112-2)"This is a test."
    [](strings.html#cb112-3)"When asked if this string had quotes in it, she replied, \"It does.\""

The first one has a newline at the end—quite a common thing to see.

The last one has quotes embedded within it, but you see each is preceded by (we say “escaped by”) a backslash (`\`) indicating that a literal quote belongs in the string at this point. This is how the C compiler can tell the difference between printing a double quote and the double quote at the end of the string.

## 7.2 String Variables

Now that we know how to make a string literal, let’s assign it to a variable so we can do something with it.
    
    
    [](strings.html#cb113-1)char *s = "Hello, world!";

Check out that type: pointer to a `char`. The string variable `s` is actually a pointer to the first character in that string, namely the `H`.

And we can print it with the `%s` (for “string”) format specifier:
    
    
    [](strings.html#cb114-1)char *s = "Hello, world!";
    [](strings.html#cb114-2)
    [](strings.html#cb114-3)printf("%s\n", s);  // "Hello, world!"

## 7.3 String Variables as Arrays

Another option is this, nearly equivalent to the above `char*` usage:
    
    
    [](strings.html#cb115-1)char s[14] = "Hello, world!";
    [](strings.html#cb115-2)
    [](strings.html#cb115-3)// or, if we were properly lazy and have the compiler
    [](strings.html#cb115-4)// figure the length for us:
    [](strings.html#cb115-5)
    [](strings.html#cb115-6)char s[] = "Hello, world!";

This means you can use array notation to access characters in a string. Let’s do exactly that to print all the characters in a string on the same line:
    
    
    [](strings.html#cb116-1)#include <stdio.h>
    [](strings.html#cb116-2)
    [](strings.html#cb116-3)int main(void)
    [](strings.html#cb116-4){
    [](strings.html#cb116-5)    char s[] = "Hello, world!";
    [](strings.html#cb116-6)
    [](strings.html#cb116-7)    for (int i = 0; i < 13; i++)
    [](strings.html#cb116-8)        printf("%c", s[i]);
    [](strings.html#cb116-9)    printf("\n");
    [](strings.html#cb116-10)}

Note that we’re using the format specifier `%c` to print a single character.

Also, check this out. The program will still work fine if we change the definition of `s` to be a `char*` type:
    
    
    [](strings.html#cb117-1)#include <stdio.h>
    [](strings.html#cb117-2)
    [](strings.html#cb117-3)int main(void)
    [](strings.html#cb117-4){
    [](strings.html#cb117-5)    char *s = "Hello, world!";   // char* here
    [](strings.html#cb117-6)
    [](strings.html#cb117-7)    for (int i = 0; i < 13; i++)
    [](strings.html#cb117-8)        printf("%c", s[i]);    // But still use arrays here...?
    [](strings.html#cb117-9)    printf("\n");
    [](strings.html#cb117-10)}

And we still can use array notation to get the job done when printing it out! This is surprising, but is still only because we haven’t talked about array/pointer equivalence yet. But this is yet another hint that arrays and pointers are the same thing, deep down. 

## 7.4 String Initializers

We’ve already seen some examples with initializing string variables with string literals:
    
    
    [](strings.html#cb118-1)char *s = "Hello, world!";
    [](strings.html#cb118-2)char t[] = "Hello, again!";

But these two initialization s are subtly different. A string literal, similar to an integer literal, has its memory automatically managed by the compiler for you! With an integer, i.e. a fixed size piece of data, the compiler can pretty easily manage it. But strings are a variable-byte beast which the compiler tames by tossing into a chunk of memory, and giving you a pointer to it.

This form points to wherever that string was placed. Typically, that place is in a land faraway from the rest of your program’s memory – read-only memory – for reasons related to performance & safety.
    
    
    [](strings.html#cb119-1)char *s = "Hello, world!";

So, if you try to mutate that string with this:
    
    
    [](strings.html#cb120-1)char *s = "Hello, world!";
    [](strings.html#cb120-2)
    [](strings.html#cb120-3)s[0] = 'z';  // BAD NEWS: tried to mutate a string literal!

The behavior is undefined. Probably, depending on your system, a crash will result.

But declaring it as an array is different. The compiler doesn’t stow those bytes in another part of town, they’re right down the street. This one is a mutable _copy_ of the string – one we can change at will:
    
    
    [](strings.html#cb121-1)char t[] = "Hello, again!";  // t is an array copy of the string 
    [](strings.html#cb121-2)t[0] = 'z'; //  No problem
    [](strings.html#cb121-3)
    [](strings.html#cb121-4)printf("%s\n", t);  // "zello, again!"

So remember: if you have a pointer to a string literal, don’t try to change it! And if you use a string in double quotes to initialize an array, that’s not actually a string literal. 

## 7.5 Getting String Length

You can’t, since C doesn’t track it for you. And when I say “can’t”, I actually mean “can”[64](function-specifiers-alignment-specifiersoperators.html#fn64). There’s a function in `<string.h>` called `strlen()` that can be used to compute the length of any string in bytes[65](function-specifiers-alignment-specifiersoperators.html#fn65).
    
    
    [](strings.html#cb122-1)#include <stdio.h>
    [](strings.html#cb122-2)#include <string.h>
    [](strings.html#cb122-3)
    [](strings.html#cb122-4)int main(void)
    [](strings.html#cb122-5){
    [](strings.html#cb122-6)    char *s = "Hello, world!";
    [](strings.html#cb122-7)
    [](strings.html#cb122-8)    printf("The string is %zu bytes long.\n", strlen(s));
    [](strings.html#cb122-9)}

The `strlen()` function returns type `size_t`, which is an integer type so you can use it for integer math. We print `size_t` with `%zu`.

The above program prints:
    
    
    [](strings.html#cb123-1)The string is 13 bytes long.

Great! So it _is_ possible to get the string length! 

But… if C doesn’t track the length of the string anywhere, how does it know how long the string is?

## 7.6 String Termination

C does strings a little differently than many programming languages, and in fact differently than almost every modern programming language.

When you’re making a new language, you have basically two options for storing a string in memory:

  1. Store the bytes of the string along with a number indicating the length of the string.

  2. Store the bytes of the string, and mark the end of the string with a special byte called the _terminator_.




If you want strings longer than 255 characters, option 1 requires at least two bytes to store the length. Whereas option 2 only requires one byte to terminate the string. So a bit of savings there.

Of course, these days it seems ridiculous to worry about saving a byte (or 3—lots of languages will happily let you have strings that are 4 gigabytes in length). But back in the day, it was a bigger deal.

So C took approach #2. In C, a “string” is defined by two basic characteristics:

  * A pointer to the first character in the string.
  * A zero-valued byte (or `NUL` character[66](function-specifiers-alignment-specifiersoperators.html#fn66)) somewhere in memory after the pointer that indicates the end of the string.



A `NUL` character can be written in C code as `\0`, though you don’t often have to do this.

When you include a string in double quotes in your code, the `NUL` character is automatically, implicitly included.
    
    
    [](strings.html#cb124-1)char *s = "Hello!";  // Actually "Hello!\0" behind the scenes

So with this in mind, let’s write our own `strlen()` function that counts `char`s in a string until it finds a `NUL`.

The procedure is to look down the string for a single `NUL` character, counting as we go[67](function-specifiers-alignment-specifiersoperators.html#fn67):
    
    
    [](strings.html#cb125-1)int my_strlen(char *s)
    [](strings.html#cb125-2){
    [](strings.html#cb125-3)    int count = 0;
    [](strings.html#cb125-4)
    [](strings.html#cb125-5)    while (s[count] != '\0')  // Single quotes for single char
    [](strings.html#cb125-6)        count++;
    [](strings.html#cb125-7)
    [](strings.html#cb125-8)    return count;
    [](strings.html#cb125-9)}

And that’s basically how the built-in `strlen()` gets the job done. 

## 7.7 Copying a String

You can’t copy a string through the assignment operator (`=`). All that does is make a copy of the pointer to the first character… so you end up with two pointers to the same string:
    
    
    [](strings.html#cb126-1)#include <stdio.h>
    [](strings.html#cb126-2)
    [](strings.html#cb126-3)int main(void)
    [](strings.html#cb126-4){
    [](strings.html#cb126-5)    char s[] = "Hello, world!";
    [](strings.html#cb126-6)    char *t;
    [](strings.html#cb126-7)
    [](strings.html#cb126-8)    // This makes a copy of the pointer, not a copy of the string!
    [](strings.html#cb126-9)    t = s;
    [](strings.html#cb126-10)
    [](strings.html#cb126-11)    // We modify t
    [](strings.html#cb126-12)    t[0] = 'z';
    [](strings.html#cb126-13)
    [](strings.html#cb126-14)    // But printing s shows the modification!
    [](strings.html#cb126-15)    // Because t and s point to the same string!
    [](strings.html#cb126-16)
    [](strings.html#cb126-17)    printf("%s\n", s);  // "zello, world!"
    [](strings.html#cb126-18)}

If you want to make a copy of a string, you have to copy it a byte at a time—this means that you’re going to take the individual bytes of the string from one place in memory and duplicate them somewhere else in memory. This is made easier with the `strcpy()` function.[68](function-specifiers-alignment-specifiersoperators.html#fn68)

Before you copy the string, make sure you have room to copy it into, i.e. the destination array that’s going to hold the characters needs to be at least as long as the string you’re copying.
    
    
    [](strings.html#cb127-1)#include <stdio.h>
    [](strings.html#cb127-2)#include <string.h>
    [](strings.html#cb127-3)
    [](strings.html#cb127-4)int main(void)
    [](strings.html#cb127-5){
    [](strings.html#cb127-6)    char s[] = "Hello, world!";
    [](strings.html#cb127-7)    char t[100];  // Each char is one byte, so plenty of room
    [](strings.html#cb127-8)
    [](strings.html#cb127-9)    // This makes a copy of the string!
    [](strings.html#cb127-10)    strcpy(t, s);
    [](strings.html#cb127-11)
    [](strings.html#cb127-12)    // We modify t
    [](strings.html#cb127-13)    t[0] = 'z';
    [](strings.html#cb127-14)
    [](strings.html#cb127-15)    // And s remains unaffected because it's a different string
    [](strings.html#cb127-16)    printf("%s\n", s);  // "Hello, world!"
    [](strings.html#cb127-17)
    [](strings.html#cb127-18)    // But t has been changed
    [](strings.html#cb127-19)    printf("%s\n", t);  // "zello, world!"
    [](strings.html#cb127-20)}

Notice with `strcpy()`, the destination pointer is the first argument, and the source pointer is the second. A mnemonic I use to remember this is that it’s the order you would have put `t` and `s` if an assignment `=` worked for strings, with the source on the right and the destination on the left. 

* * *

[Prev](arrays.html) | [Contents](index.html) | [Next](structs.html)
