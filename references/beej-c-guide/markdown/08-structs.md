[Prev](strings.html) | [Contents](index.html) | [Next](file-inputoutput.html)

* * *

# 8 Structs

In C, we have something called a `struct`, which is a user-definable type that holds multiple pieces of data, potentially of different types.

It’s a convenient way to bundle multiple variables into a single one. This can be beneficial for passing variables to functions (so you just have to pass one instead of many), and useful for organizing data and making code more readable.

If you’ve come from another language, you might be familiar with the idea of _classes_ and _objects_. These don’t exist in C, natively[69](function-specifiers-alignment-specifiersoperators.html#fn69). You can think of a `struct` as a class with only data members, and no methods.

## 8.1 Declaring a Struct

You can declare a `struct` in your code like so:
    
    
    [](structs.html#cb128-1)struct car {
    [](structs.html#cb128-2)    char *name;
    [](structs.html#cb128-3)    float price;
    [](structs.html#cb128-4)    int speed;
    [](structs.html#cb128-5)};

This is often done at the global scope outside any functions so that the `struct` is globally available.

When you do this, you’re making a new _type_. The full type name is `struct car`. (Not just `car`—that won’t work.)

There aren’t any variables of that type yet, but we can declare some:
    
    
    [](structs.html#cb129-1)struct car saturn;  // Variable "saturn" of type "struct car"

And now we have an uninitialized variable `saturn`[70](function-specifiers-alignment-specifiersoperators.html#fn70) of type `struct car`.

We should initialize it! But how do we set the values of those individual fields?

Like in many other languages that stole it from C, we’re going to use the dot operator (`.`) to access the individual fields.
    
    
    [](structs.html#cb130-1)saturn.name = "Saturn SL/2";
    [](structs.html#cb130-2)saturn.price = 15999.99;
    [](structs.html#cb130-3)saturn.speed = 175;
    [](structs.html#cb130-4)
    [](structs.html#cb130-5)printf("Name:           %s\n", saturn.name);
    [](structs.html#cb130-6)printf("Price (USD):    %f\n", saturn.price);
    [](structs.html#cb130-7)printf("Top Speed (km): %d\n", saturn.speed);

There on the first lines, we set the values in the `struct car`, and then in the next bit, we print those values out. 

## 8.2 Struct Initializers

That example in the previous section was a little unwieldy. There must be a better way to initialize that `struct` variable!

You can do it with an initializer by putting values in for the fields _in the order they appear in the`struct`_ when you define the variable. (This won’t work after the variable has been defined—it has to happen in the definition).
    
    
    [](structs.html#cb131-1)struct car {
    [](structs.html#cb131-2)    char *name;
    [](structs.html#cb131-3)    float price;
    [](structs.html#cb131-4)    int speed;
    [](structs.html#cb131-5)};
    [](structs.html#cb131-6)
    [](structs.html#cb131-7)// Now with an initializer! Same field order as in the struct declaration:
    [](structs.html#cb131-8)struct car saturn = {"Saturn SL/2", 16000.99, 175};
    [](structs.html#cb131-9)
    [](structs.html#cb131-10)printf("Name:      %s\n", saturn.name);
    [](structs.html#cb131-11)printf("Price:     %f\n", saturn.price);
    [](structs.html#cb131-12)printf("Top Speed: %d km\n", saturn.speed);

The fact that the fields in the initializer need to be in the same order is a little freaky. If someone changes the order in `struct car`, it could break all the other code!

We can be more specific with our initializers:
    
    
    [](structs.html#cb132-1)struct car saturn = {.speed=175, .name="Saturn SL/2"};

Now it’s independent of the order in the `struct` declaration. Which is safer code, for sure.

Similar to array initializers, any missing field designators are initialized to zero (in this case, that would be `.price`, which I’ve omitted). 

## 8.3 Passing Structs to Functions

You can do a couple things to pass a `struct` to a function.

  1. Pass the `struct`.
  2. Pass a pointer to the `struct`.



Recall that when you pass something to a function, a _copy_ of that thing gets made for the function to operate on, whether it’s a copy of a pointer, an `int`, a `struct`, or anything.

There are basically two cases when you’d want to pass a pointer to the `struct`:

  1. You need the function to be able to make changes to the `struct` that was passed in, and have those changes show in the caller.
  2. The `struct` is somewhat large and it’s more expensive to copy that onto the stack than it is to just copy a pointer[71](function-specifiers-alignment-specifiersoperators.html#fn71).



For those two reasons, it’s far more common to pass a pointer to a `struct` to a function, though its by no means illegal to pass the `struct` itself.

Let’s try passing in a pointer, making a function that will allow you to set the `.price` field of the `struct car`:
    
    
    [](structs.html#cb133-1)#include <stdio.h>
    [](structs.html#cb133-2)
    [](structs.html#cb133-3)struct car {
    [](structs.html#cb133-4)    char *name;
    [](structs.html#cb133-5)    float price;
    [](structs.html#cb133-6)    int speed;
    [](structs.html#cb133-7)};
    [](structs.html#cb133-8)
    [](structs.html#cb133-9)int main(void)
    [](structs.html#cb133-10){
    [](structs.html#cb133-11)    struct car saturn = {.speed=175, .name="Saturn SL/2"};
    [](structs.html#cb133-12)
    [](structs.html#cb133-13)    // Pass a pointer to this struct car, along with a new,
    [](structs.html#cb133-14)    // more realistic, price:
    [](structs.html#cb133-15)    set_price(&saturn, 799.99);
    [](structs.html#cb133-16)
    [](structs.html#cb133-17)    printf("Price: %f\n", saturn.price);
    [](structs.html#cb133-18)}

You should be able to come up with the function signature for `set_price()` just by looking at the types of the arguments we have there.

`saturn` is a `struct car`, so `&saturn` must be the address of the `struct car`, AKA a pointer to a `struct car`, namely a `struct car*`.

And `799.99` is a `float`.

So the function declaration must look like this:
    
    
    [](structs.html#cb134-1)void set_price(struct car *c, float new_price)

We just need to write the body. One attempt might be:
    
    
    [](structs.html#cb135-1)void set_price(struct car *c, float new_price) {
    [](structs.html#cb135-2)    c.price = new_price;  // ERROR!!
    [](structs.html#cb135-3)}

That won’t work because the dot operator only works on `struct`s… it doesn’t work on _pointers_ to `struct`s.

Ok, so we can dereference the variable `c` to de-pointer it to get to the `struct` itself. Dereferencing a `struct car*` results in the `struct car` that the pointer points to, which we should be able to use the dot operator on:
    
    
    [](structs.html#cb136-1)void set_price(struct car *c, float new_price) {
    [](structs.html#cb136-2)    (*c).price = new_price;  // Works, but is ugly and non-idiomatic :(
    [](structs.html#cb136-3)}

And that works! But it’s a little clunky to type all those parens and the asterisk. C has some syntactic sugar called the _arrow operator_ that helps with that. 

## 8.4 The Arrow Operator

The arrow operator helps refer to fields in pointers to `struct`s.
    
    
    [](structs.html#cb137-1)void set_price(struct car *c, float new_price) {
    [](structs.html#cb137-2)    // (*c).price = new_price;  // Works, but non-idiomatic :(
    [](structs.html#cb137-3)    //
    [](structs.html#cb137-4)    // The line above is 100% equivalent to the one below:
    [](structs.html#cb137-5)
    [](structs.html#cb137-6)    c->price = new_price;  // That's the one!
    [](structs.html#cb137-7)}

So when accessing fields, when do we use dot and when do we use arrow?

  * If you have a `struct`, use dot (`.`).
  * If you have a pointer to a `struct`, use arrow (`->`). 



## 8.5 Copying and Returning `struct`s

Here’s an easy one for you!

Just assign from one to the other!
    
    
    [](structs.html#cb138-1)struct car a, b;
    [](structs.html#cb138-2)
    [](structs.html#cb138-3)b = a;  // Copy the struct

And returning a `struct` (as opposed to a pointer to one) from a function also makes a similar copy to the receiving variable.

This is not a “deep copy”[72](function-specifiers-alignment-specifiersoperators.html#fn72). All fields are copied as-is, including pointers to things. 

## 8.6 Comparing `struct`s

There’s only one safe way to do it: compare each field one at a time.

You might think you could use [`memcmp()`](https://beej.us/guide/bgclr/html/split/stringref.html#man-strcmp)[73](function-specifiers-alignment-specifiersoperators.html#fn73), but that doesn’t handle the case of the possible [padding bytes](structs-ii-more-fun-with-structs.html#struct-padding-bytes) that might be in there.

If you clear the `struct` to zero first with [`memset()`](https://beej.us/guide/bgclr/html/split/stringref.html#man-memset)[74](function-specifiers-alignment-specifiersoperators.html#fn74), then it _might_ work, though there could be weird elements that [might not compare as you expect](https://stackoverflow.com/questions/141720/how-do-you-compare-structs-for-equality-in-c)[75](function-specifiers-alignment-specifiersoperators.html#fn75). 

* * *

[Prev](strings.html) | [Contents](index.html) | [Next](file-inputoutput.html)
