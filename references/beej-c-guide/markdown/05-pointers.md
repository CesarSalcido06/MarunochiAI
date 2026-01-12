[Prev](functions.html) | [Contents](index.html) | [Next](arrays.html)

* * *

# 5 Pointers—Cower In Fear!

> _“How do you get to Carnegie Hall?”_  
>  _“Practice!”_
> 
> —20th-century joke of unknown origin

Pointers are one of the most feared things in the C language. In fact, they are the one thing that makes this language challenging at all. But why?

Because they, quite honestly, can cause electric shocks to come up through the keyboard and physically _weld_ your arms permanently in place, cursing you to a life at the keyboard in this language from the 70s!

Really? Well, not really. I’m just trying to set you up for success.

Depending on what language you came from, you might already understand the concept of _references_ , where a variable refers to an object of some type.

This is very much the same, except we have to be more explicit with C about when we’re talking about the reference or the thing it refers to.

## 5.1 Memory and Variables

Computer memory holds data of all kinds, right? It’ll hold `float`s, `int`s, or whatever you have. To make memory easy to cope with, each byte of memory is identified by an integer. These integers increase sequentially as you move up through memory[45](function-specifiers-alignment-specifiersoperators.html#fn45). You can think of it as a bunch of numbered boxes, where each box holds a byte[46](function-specifiers-alignment-specifiersoperators.html#fn46) of data. Or like a big array where each element holds a byte, if you come from a language with arrays. The number that represents each box is called its _address_.

Now, not all data types use just a byte. For instance, an `int` is often four bytes, as is a `float`, but it really depends on the system. You can use the `sizeof` operator to determine how many bytes of memory a certain type uses.
    
    
    [](pointers.html#cb66-1)// %zu is the format specifier for type size_t
    [](pointers.html#cb66-2)
    [](pointers.html#cb66-3)printf("an int uses %zu bytes of memory\n", sizeof(int));
    [](pointers.html#cb66-4)
    [](pointers.html#cb66-5)// That prints "4" for me, but can vary by system.

> **Memory Fun Facts** : When you have a data type (like your typical `int`) that uses more than a byte of memory, the bytes that make up the data are always adjacent to one another in memory. Sometimes they’re in the order that you expect, and sometimes they’re not[47](function-specifiers-alignment-specifiersoperators.html#fn47). While C doesn’t guarantee any particular memory order (it’s platform-dependent), it’s still generally possible to write code in a way that’s platform-independent where you don’t have to even consider these pesky byte orderings.

So _anyway_ , if we can get on with it and get a drum roll and some foreboding music playing for the definition of a pointer, _a pointer is a variable that holds an address_. Imagine the classical score from 2001: A Space Odyssey at this point. Ba bum ba bum ba bum BAAAAH!

Ok, so maybe a bit overwrought here, yes? There’s not a lot of mystery about pointers. They are the address of data. Just like an `int` variable can hold the value `12`, a pointer variable can hold the address of data.

This means that all these things mean the same thing, i.e. a number that represents a point in memory:

  * Index into memory (if you’re thinking of memory like a big array)
  * Address
  * Location



I’m going to use these interchangeably. And yes, I just threw _location_ in there because you can never have enough words that mean the same thing.

And a pointer variable holds that address number. Just like a `float` variable might hold `3.14159`.

Imagine you have a bunch of Post-it® notes all numbered in sequence with their address. (The first one is at index numbered `0`, the next at index `1`, and so on.)

In addition to the number representing their positions, you can also write another number of your choice on each. It could be the number of dogs you have. Or the number of moons around Mars…

…Or, _it could be the index of another Post-it note!_

If you have written the number of dogs you have, that’s just a regular variable. But if you wrote the index of another Post-it in there, _that’s a pointer_. It points to the other note!

Another analogy might be with house addresses. You can have a house with certain qualities, yard, metal roof, solar, etc. Or you could have the address of that house. The address isn’t the same as the house itself. One’s a full-blown house, and the other is just a few lines of text. But the address of the house is a _pointer_ to that house. It’s not the house itself, but it tells you where to find it.

And we can do the same thing in the computer with data. You can have a data variable that’s holding some value. And that value is in memory at some address. And you could have a different _pointer variable_ hold the address of that data variable.

It’s not the data variable itself, but, like with a house address, it tells us where to find it.

When we have that, we say we have a “pointer to” that data. And we can follow the pointer to access the data itself.

(Though it doesn’t seem particularly useful yet, this all becomes indispensable when used with function calls. Bear with me until we get there.)

So if we have an `int`, say, and we want a pointer to it, what we want is some way to get the address of that `int`, right? After all, the pointer just holds the _address of_ the data. What operator do you suppose we’d use to find the _address of_ the `int`?

Well, by a shocking surprise that must come as something of a shock to you, gentle reader, we use the `address-of` operator (which happens to be an ampersand: “`&`”)to find the address of the data. Ampersand.

So for a quick example, we’ll introduce a new _format specifier_ for `printf()` so you can print a pointer. You know already how `%d` prints a decimal integer, yes? Well, `%p` prints a pointer. Now, this pointer is going to look like a garbage number (and it might be printed in hexadecimal[48](function-specifiers-alignment-specifiersoperators.html#fn48) instead of decimal), but it is merely the index into memory the data is stored in. (Or the index into memory that the first byte of data is stored in, if the data is multi-byte.) In virtually all circumstances, including this one, the actual value of the number printed is unimportant to you, and I show it here only for demonstration of the `address-of` operator.
    
    
    [](pointers.html#cb67-1)#include <stdio.h>
    [](pointers.html#cb67-2)
    [](pointers.html#cb67-3)int main(void)
    [](pointers.html#cb67-4){
    [](pointers.html#cb67-5)    int i = 10;
    [](pointers.html#cb67-6)
    [](pointers.html#cb67-7)    printf("The value of i is %d\n", i);
    [](pointers.html#cb67-8)    printf("And its address is %p\n", (void *)&i);
    [](pointers.html#cb67-9)}

> **The above code contains a _cast_** where we coerce the type of the expression `&i` to be type `void*`. This is to keep the compiler from throwing a warning here. This is all stuff we haven’t covered yet, so just ignore the `(void*)` in the code above for now and pretend it’s not there.

On my computer, this prints:
    
    
    [](pointers.html#cb68-1)The value of i is 10
    [](pointers.html#cb68-2)And its address is 0x7ffddf7072a4

If you’re curious, that hexadecimal number is 140,727,326,896,068 in decimal (base 10 just like Grandma used to use). That’s the index into memory where the variable `i`’s data is stored. It’s the address of `i`. It’s the location of `i`. It’s a pointer to `i`.

> **Wait—you have 140 terabytes of RAM?** Yes! Don’t you? But I do fib my buns off; of course I don’t (ca. 2024). Modern computers use a miraculous technology called [virtual memory](https://en.wikipedia.org/wiki/Virtual_memory)[49](function-specifiers-alignment-specifiersoperators.html#fn49) that makes processes think they have the entire memory space of your computer to themselves, regardless of how much physical RAM backs it up. So even though the address was that huge number, it’s being mapped to some lower physical memory address by the virtual memory system of my CPU. This particular computer has 16 GB RAM (again, ca. 2024, but I’m running Linux, so that’s plenty). Terabytes of RAM? I’m a teacher, not a dot-com bazillionaire. None of this is anything any of us have to worry about except the part about me not being phenomenally wealthy.

It’s a pointer because it lets you know where `i` is in memory. Like a home address written on a scrap of paper tells you where you can find a particular house, this number indicates to us where in memory we can find the value of `i`. It points to `i`.

Again, we don’t really care what the address’s exact number is, generally. We just care that it’s a pointer to `i`.

## 5.2 Pointer Types

So… this is all well and good. You can now successfully take the address of a variable and print it on the screen. There’s a little something for the ol’ resume, right? Here’s where you grab me by the scruff of the neck and ask politely what the frick pointers are good for.

Excellent question, and we’ll get to that right after these messages from our sponsor.
    
    
    ACME ROBOTIC HOUSING UNIT CLEANING SERVICES. YOUR HOMESTEAD WILL BE
    DRAMATICALLY IMPROVED OR YOU WILL BE TERMINATED. MESSAGE ENDS.

Welcome back to another installment of Beej’s Guide. When we met last we were talking about how to make use of pointers. Well, what we’re going to do is store a pointer off in a variable so that we can use it later. You can identify the _pointer type_ because there’s an asterisk (`*`) before the variable name and after its type:
    
    
    [](pointers.html#cb70-1)int main(void)
    [](pointers.html#cb70-2){
    [](pointers.html#cb70-3)    int i;  // i's type is "int"
    [](pointers.html#cb70-4)    int *p; // p's type is "pointer to an int", or "int-pointer"
    [](pointers.html#cb70-5)}

Hey, so we have here a variable that is a pointer type, and it can point to other `int`s. That is, it can hold the address of other `int`s. We know it points to `int`s, since it’s of type `int*` (read “int-pointer”).

When you do an assignment into a pointer variable, the type of the right hand side of the assignment has to be the same type as the pointer variable. Fortunately for us, when you take the `address-of` a variable, the resultant type is a pointer to that variable type, so assignments like the following are perfect:
    
    
    [](pointers.html#cb71-1)int i;
    [](pointers.html#cb71-2)int *p;  // p is a pointer, but is uninitialized and points to garbage
    [](pointers.html#cb71-3)
    [](pointers.html#cb71-4)p = &i;  // p is assigned the address of i--p now "points to" i

On the left of the assignment, we have a variable of type pointer-to-`int` (`int*`), and on the right side, we have expression of type pointer-to-`int` since `i` is an `int` (because address-of `int` gives you a pointer to `int`). The address of a thing can be stored in a pointer to that thing.

Get it? I know it still doesn’t quite make much sense since you haven’t seen an actual use for the pointer variable, but we’re taking small steps here so that no one gets lost. So now, let’s introduce you to the anti-address-of operator. It’s kind of like what `address-of` would be like in Bizarro World.

## 5.3 Dereferencing

A pointer variable can be thought of as _referring_ to another variable by pointing to it. It’s rare you’ll hear anyone in C land talking about “referring” or “references”, but I bring it up just so that the name of this operator will make a little more sense.

When you have a pointer to a variable (roughly “a reference to a variable”), you can use the original variable through the pointer by _dereferencing_ the pointer. (You can think of this as “de-pointering” the pointer, but no one ever says “de-pointering”.)

Back to our analogy, this is vaguely like looking at a home address and then going to that house.

Now, what do I mean by “get access to the original variable”? Well, if you have a variable called `i`, and you have a pointer to `i` called `p`, you can use the dereferenced pointer `p` _exactly as if it were the original variable`i`_!

You almost have enough knowledge to handle an example. The last tidbit you need to know is actually this: what is the dereference operator? It’s actually called the _indirection operator_ , because you’re accessing values indirectly via the pointer. And it is the asterisk, again: `*`. Now, don’t get this confused with the asterisk you used in the pointer declaration, earlier. They are the same character, but they have different meanings in different contexts[50](function-specifiers-alignment-specifiersoperators.html#fn50).

Here’s a full-blown example:
    
    
    [](pointers.html#cb72-1)#include <stdio.h>
    [](pointers.html#cb72-2)
    [](pointers.html#cb72-3)int main(void)
    [](pointers.html#cb72-4){
    [](pointers.html#cb72-5)    int i;
    [](pointers.html#cb72-6)    int *p;  // this is NOT a dereference--this is a type "int*"
    [](pointers.html#cb72-7)
    [](pointers.html#cb72-8)    p = &i;  // p now points to i, p holds address of i
    [](pointers.html#cb72-9)
    [](pointers.html#cb72-10)    i = 10;  // i is now 10
    [](pointers.html#cb72-11)    *p = 20; // the thing p points to (namely i!) is now 20!!
    [](pointers.html#cb72-12)
    [](pointers.html#cb72-13)    printf("i is %d\n", i);   // prints "20"
    [](pointers.html#cb72-14)    printf("i is %d\n", *p);  // "20"! dereference-p is the same as i!
    [](pointers.html#cb72-15)}

Remember that `p` holds the address of `i`, as you can see where we did the assignment to `p` on line 8. What the indirection operator does is tells the computer to _use the object the pointer points to_ instead of using the pointer itself. In this way, we have turned `*p` into an alias of sorts for `i`.

Great, but _why_? Why do any of this?

## 5.4 Passing Pointers as Arguments

Right about now, you’re thinking that you have an awful lot of knowledge about pointers, but absolutely zero application, right? I mean, what use is `*p` if you could just simply say `i` instead?

Well, my friend, the real power of pointers comes into play when you start passing them to functions. Why is this a big deal? You might recall from before that you could pass all kinds of arguments to functions and they’d be dutifully copied into parameters, and then you could manipulate local copies of those variables from within the function, and then you could return a single value.

What if you wanted to bring back more than one single piece of data from the function? I mean, you can only return one thing, right? What if I answered that question with another question? …Er, two questions?

What happens when you pass a pointer as an argument to a function? Does a copy of the pointer get put into its corresponding parameter? _You bet your sweet peas it does._ Remember how earlier I rambled on and on about how _EVERY SINGLE ARGUMENT_ gets copied into parameters and the function uses a copy of the argument? Well, the same is true here. The function will get a copy of the pointer.

But, and this is the clever part: we will have set up the pointer in advance to point at a variable… and then the function can dereference its copy of the pointer to get back to the original variable! The function can’t see the variable itself, but it can certainly dereference a pointer to that variable!

This is analogous to writing a home address on a piece of paper, and then copying that onto another piece of paper. You now have _two_ pointers to that house, and both are equally good at getting you to the house itself.

In the case of a function call. one of the copies is stored in a pointer variable out in the calling scope, and the other is stored in a pointer variable that is the parameter of the function.

Example! Let’s revisit our old `increment()` function, but this time let’s make it so that it actually increments the value out in the caller.
    
    
    [](pointers.html#cb73-1)#include <stdio.h>
    [](pointers.html#cb73-2)
    [](pointers.html#cb73-3)void increment(int *p)  // note that it accepts a pointer to an int
    [](pointers.html#cb73-4){
    [](pointers.html#cb73-5)    *p = *p + 1;        // add one to the thing p points to
    [](pointers.html#cb73-6)}
    [](pointers.html#cb73-7)
    [](pointers.html#cb73-8)int main(void)
    [](pointers.html#cb73-9){
    [](pointers.html#cb73-10)    int i = 10;
    [](pointers.html#cb73-11)    int *j = &i;  // note the address-of; turns it into a pointer to i
    [](pointers.html#cb73-12)
    [](pointers.html#cb73-13)    printf("i is %d\n", i);        // prints "10"
    [](pointers.html#cb73-14)    printf("i is also %d\n", *j);  // prints "10"
    [](pointers.html#cb73-15)
    [](pointers.html#cb73-16)    increment(j);                  // j is an int*--to i
    [](pointers.html#cb73-17)
    [](pointers.html#cb73-18)    printf("i is %d\n", i);        // prints "11"!
    [](pointers.html#cb73-19)}

Ok! There are a couple things to see here… not the least of which is that the `increment()` function takes an `int*` as an argument. We pass it an `int*` in the call by changing the `int` variable `i` to an `int*` using the `address-of` operator. (Remember, a pointer holds an address, so we make pointers to variables by running them through the `address-of` operator.)

The `increment()` function gets a copy of the pointer. Both the original pointer `j` (in `main()`) and the copy of that pointer `p` (the parameter in `increment()`) point to the same address, namely the one holding the value `i`. (Again, by analogy, like two pieces of paper with the same home address written on them.) Dereferencing either will allow you to modify the original variable `i`! The function can modify a variable in another scope! Rock on!

The above example is often more concisely written in the call just by using address-of right in the argument list:
    
    
    [](pointers.html#cb74-1)printf("i is %d\n", i);  // prints "10"
    [](pointers.html#cb74-2)increment(&i);
    [](pointers.html#cb74-3)printf("i is %d\n", i);  // prints "11"!

As a general rule, if you want the function to modify the thing that you’re passing in such that you see the result, you’ll have to pass a pointer to that thing.

## 5.5 The `NULL` Pointer

Any pointer variable of any pointer type can be set to a special value called `NULL`. This indicates that this pointer doesn’t point to anything.
    
    
    [](pointers.html#cb75-1)int *p;
    [](pointers.html#cb75-2)
    [](pointers.html#cb75-3)p = NULL;

Since it doesn’t point to a value, dereferencing it is undefined behavior, and probably will result in a crash:
    
    
    [](pointers.html#cb76-1)int *p = NULL;
    [](pointers.html#cb76-2)
    [](pointers.html#cb76-3)*p = 12;  // CRASH or SOMETHING PROBABLY BAD. BEST AVOIDED.

Despite being called [the billion dollar mistake by its creator](https://en.wikipedia.org/wiki/Null_pointer#History)[51](function-specifiers-alignment-specifiersoperators.html#fn51), the `NULL` pointer is a good [sentinel value](https://en.wikipedia.org/wiki/Sentinel_value)[52](function-specifiers-alignment-specifiersoperators.html#fn52) and general indicator that a pointer hasn’t yet been initialized.

(Of course, like other variables, the pointer points to garbage unless you explicitly assign it to point to an address or `NULL`.) 

## 5.6 A Note on Declaring Pointers

The syntax for declaring a pointer can get a little weird. Let’s look at this example:
    
    
    [](pointers.html#cb77-1)int a;
    [](pointers.html#cb77-2)int b;

We can condense that into a single line, right?
    
    
    [](pointers.html#cb78-1)int a, b;  // Same thing

So `a` and `b` are both `int`s. No problem.

But what about this?
    
    
    [](pointers.html#cb79-1)int a;
    [](pointers.html#cb79-2)int *p;

Can we make that into one line? We can. But where does the `*` go?

The rule is that the `*` goes in front of any variable that is a pointer type. That is. the `*` is _not_ part of the `int` in this example. it’s a part of variable `p`.

With that in mind, we can write this:
    
    
    [](pointers.html#cb80-1)int a, *p;  // Same thing

It’s important to note that the following line does _not_ declare two pointers:
    
    
    [](pointers.html#cb81-1)int *p, q;  // p is a pointer to an int; q is just an int.

This can be particularly insidious-looking if the programmer writes this following (valid) line of code which is functionally identical to the one above.
    
    
    [](pointers.html#cb82-1)int* p, q;  // p is a pointer to an int; q is just an int.

So take a look at this and determine which variables are pointers and which are not:
    
    
    [](pointers.html#cb83-1)int *a, b, c, *d, e, *f, g, h, *i;

I’ll drop the answer in a footnote[53](function-specifiers-alignment-specifiersoperators.html#fn53).

## 5.7 `sizeof` and Pointers

Just a little bit of syntax here that might be confusing and you might see from time to time.

Recall that `sizeof` operates on the _type_ of the expression.
    
    
    [](pointers.html#cb84-1)int *p;
    [](pointers.html#cb84-2)
    [](pointers.html#cb84-3)// Prints size of an 'int'
    [](pointers.html#cb84-4)printf("%zu\n", sizeof(int));
    [](pointers.html#cb84-5)
    [](pointers.html#cb84-6)// p is type 'int *', so prints size of 'int*'
    [](pointers.html#cb84-7)printf("%zu\n", sizeof p);
    [](pointers.html#cb84-8)
    [](pointers.html#cb84-9)// *p is type 'int', so prints size of 'int'
    [](pointers.html#cb84-10)printf("%zu\n", sizeof *p);

You might see code in the wild with that last `sizeof` in there. Just remember that `sizeof` is all about the type of the expression, not the variables in the expression themselves.

* * *

[Prev](functions.html) | [Contents](index.html) | [Next](arrays.html)
