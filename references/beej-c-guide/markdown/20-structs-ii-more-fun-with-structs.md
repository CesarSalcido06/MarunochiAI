[Prev](the-c-preprocessor.html) | [Contents](index.html) | [Next](characters-and-strings-ii.html)

* * *

# 20 `struct`s II: More Fun with `struct`s

Turns out there’s a lot more you can do with `struct`s than we’ve talked about, but it’s just a big pile of miscellaneous things. So we’ll throw them in this chapter.

If you’re good with `struct` basics, you can round out your knowledge here.

## 20.1 Initializers of Nested `struct`s and Arrays

Remember how you could [initialize structure members along these lines](structs.html#struct-initializers)?
    
    
    [](structs-ii-more-fun-with-structs.html#cb427-1)struct foo x = {.a=12, .b=3.14};

Turns out we have more power in these initializers than we’d originally shared. Exciting!

For one thing, if you have a nested substructure like the following, you can initialize members of that substructure by following the variable names down the line:
    
    
    [](structs-ii-more-fun-with-structs.html#cb428-1)struct foo x = {.a.b.c=12};

Let’s look at an example:
    
    
    [](structs-ii-more-fun-with-structs.html#cb429-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb429-2)
    [](structs-ii-more-fun-with-structs.html#cb429-3)struct cabin_information {
    [](structs-ii-more-fun-with-structs.html#cb429-4)    int window_count;
    [](structs-ii-more-fun-with-structs.html#cb429-5)    int o2level;
    [](structs-ii-more-fun-with-structs.html#cb429-6)};
    [](structs-ii-more-fun-with-structs.html#cb429-7)
    [](structs-ii-more-fun-with-structs.html#cb429-8)struct spaceship {
    [](structs-ii-more-fun-with-structs.html#cb429-9)    char *manufacturer;
    [](structs-ii-more-fun-with-structs.html#cb429-10)    struct cabin_information ci;
    [](structs-ii-more-fun-with-structs.html#cb429-11)};
    [](structs-ii-more-fun-with-structs.html#cb429-12)
    [](structs-ii-more-fun-with-structs.html#cb429-13)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb429-14){
    [](structs-ii-more-fun-with-structs.html#cb429-15)    struct spaceship s = {
    [](structs-ii-more-fun-with-structs.html#cb429-16)        .manufacturer="General Products",
    [](structs-ii-more-fun-with-structs.html#cb429-17)        .ci.window_count = 8,   // <-- NESTED INITIALIZER!
    [](structs-ii-more-fun-with-structs.html#cb429-18)        .ci.o2level = 21
    [](structs-ii-more-fun-with-structs.html#cb429-19)    };
    [](structs-ii-more-fun-with-structs.html#cb429-20)
    [](structs-ii-more-fun-with-structs.html#cb429-21)    printf("%s: %d seats, %d%% oxygen\n",
    [](structs-ii-more-fun-with-structs.html#cb429-22)        s.manufacturer, s.ci.window_count, s.ci.o2level);
    [](structs-ii-more-fun-with-structs.html#cb429-23)}

Check out lines 16-17! That’s where we’re initializing members of the `struct cabin_information` in the definition of `s`, our `struct spaceship`.

And here is another option for that same initializer—this time we’ll do something more standard-looking, but either approach works:
    
    
    [](structs-ii-more-fun-with-structs.html#cb430-15)    struct spaceship s = {
    [](structs-ii-more-fun-with-structs.html#cb430-16)        .manufacturer="General Products",
    [](structs-ii-more-fun-with-structs.html#cb430-17)        .ci={
    [](structs-ii-more-fun-with-structs.html#cb430-18)            .window_count = 8,
    [](structs-ii-more-fun-with-structs.html#cb430-19)            .o2level = 21
    [](structs-ii-more-fun-with-structs.html#cb430-20)        }
    [](structs-ii-more-fun-with-structs.html#cb430-21)    };

Now, as if the above information isn’t spectacular enough, we can also mix in array initializers in there, too.

Let’s change this up to get an array of passenger information in there, and we can check out how the initializers work in there, too.
    
    
    [](structs-ii-more-fun-with-structs.html#cb431-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb431-2)
    [](structs-ii-more-fun-with-structs.html#cb431-3)struct passenger {
    [](structs-ii-more-fun-with-structs.html#cb431-4)    char *name;
    [](structs-ii-more-fun-with-structs.html#cb431-5)    int covid_vaccinated; // Boolean
    [](structs-ii-more-fun-with-structs.html#cb431-6)};
    [](structs-ii-more-fun-with-structs.html#cb431-7)
    [](structs-ii-more-fun-with-structs.html#cb431-8)#define MAX_PASSENGERS 8
    [](structs-ii-more-fun-with-structs.html#cb431-9)
    [](structs-ii-more-fun-with-structs.html#cb431-10)struct spaceship {
    [](structs-ii-more-fun-with-structs.html#cb431-11)    char *manufacturer;
    [](structs-ii-more-fun-with-structs.html#cb431-12)    struct passenger passenger[MAX_PASSENGERS];
    [](structs-ii-more-fun-with-structs.html#cb431-13)};
    [](structs-ii-more-fun-with-structs.html#cb431-14)
    [](structs-ii-more-fun-with-structs.html#cb431-15)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb431-16){
    [](structs-ii-more-fun-with-structs.html#cb431-17)    struct spaceship s = {
    [](structs-ii-more-fun-with-structs.html#cb431-18)        .manufacturer="General Products",
    [](structs-ii-more-fun-with-structs.html#cb431-19)        .passenger = {
    [](structs-ii-more-fun-with-structs.html#cb431-20)            // Initialize a field at a time
    [](structs-ii-more-fun-with-structs.html#cb431-21)            [0].name = "Gridley, Lewis",
    [](structs-ii-more-fun-with-structs.html#cb431-22)            [0].covid_vaccinated = 0,
    [](structs-ii-more-fun-with-structs.html#cb431-23)
    [](structs-ii-more-fun-with-structs.html#cb431-24)            // Or all at once
    [](structs-ii-more-fun-with-structs.html#cb431-25)            [7] = {.name="Brown, Teela", .covid_vaccinated=1},
    [](structs-ii-more-fun-with-structs.html#cb431-26)        }
    [](structs-ii-more-fun-with-structs.html#cb431-27)    };
    [](structs-ii-more-fun-with-structs.html#cb431-28)
    [](structs-ii-more-fun-with-structs.html#cb431-29)    printf("Passengers for %s ship:\n", s.manufacturer);
    [](structs-ii-more-fun-with-structs.html#cb431-30)
    [](structs-ii-more-fun-with-structs.html#cb431-31)    for (int i = 0; i < MAX_PASSENGERS; i++)
    [](structs-ii-more-fun-with-structs.html#cb431-32)        if (s.passenger[i].name != NULL)
    [](structs-ii-more-fun-with-structs.html#cb431-33)            printf("    %s (%svaccinated)\n",
    [](structs-ii-more-fun-with-structs.html#cb431-34)                s.passenger[i].name,
    [](structs-ii-more-fun-with-structs.html#cb431-35)                s.passenger[i].covid_vaccinated? "": "not ");
    [](structs-ii-more-fun-with-structs.html#cb431-36)}

## 20.2 Anonymous `struct`s

These are “the `struct` with no name”. We also mention these in the [`typedef`](typedef-making-new-types.html#typedef-struct) section, but we’ll refresh here.

Here’s a regular `struct`:
    
    
    [](structs-ii-more-fun-with-structs.html#cb432-1)struct animal {
    [](structs-ii-more-fun-with-structs.html#cb432-2)    char *name;
    [](structs-ii-more-fun-with-structs.html#cb432-3)    int leg_count, speed;
    [](structs-ii-more-fun-with-structs.html#cb432-4)};

And here’s the anonymous equivalent:
    
    
    [](structs-ii-more-fun-with-structs.html#cb433-1)struct {              // <-- No name!
    [](structs-ii-more-fun-with-structs.html#cb433-2)    char *name;
    [](structs-ii-more-fun-with-structs.html#cb433-3)    int leg_count, speed;
    [](structs-ii-more-fun-with-structs.html#cb433-4)};

Okaaaaay. So we have a `struct`, but it has no name, so we have no way of using it later? Seems pretty pointless.

Admittedly, in that example, it is. But we can still make use of it a couple ways.

One is rare, but since the anonymous `struct` represents a type, we can just put some variable names after it and use them.
    
    
    [](structs-ii-more-fun-with-structs.html#cb434-1)struct {                   // <-- No name!
    [](structs-ii-more-fun-with-structs.html#cb434-2)    char *name;
    [](structs-ii-more-fun-with-structs.html#cb434-3)    int leg_count, speed;
    [](structs-ii-more-fun-with-structs.html#cb434-4)} a, b, c;                 // 3 variables of this struct type
    [](structs-ii-more-fun-with-structs.html#cb434-5)
    [](structs-ii-more-fun-with-structs.html#cb434-6)a.name = "antelope";
    [](structs-ii-more-fun-with-structs.html#cb434-7)c.leg_count = 4;           // for example

But that’s still not that useful.

Far more common is use of anonymous `struct`s with a `typedef` so that we can use it later (e.g. to pass variables to functions).
    
    
    [](structs-ii-more-fun-with-structs.html#cb435-1)typedef struct {                   // <-- No name!
    [](structs-ii-more-fun-with-structs.html#cb435-2)    char *name;
    [](structs-ii-more-fun-with-structs.html#cb435-3)    int leg_count, speed;
    [](structs-ii-more-fun-with-structs.html#cb435-4)} animal;                          // New type: animal
    [](structs-ii-more-fun-with-structs.html#cb435-5)
    [](structs-ii-more-fun-with-structs.html#cb435-6)animal a, b, c;
    [](structs-ii-more-fun-with-structs.html#cb435-7)
    [](structs-ii-more-fun-with-structs.html#cb435-8)a.name = "antelope";
    [](structs-ii-more-fun-with-structs.html#cb435-9)c.leg_count = 4;           // for example

Personally, I don’t use many anonymous `struct`s. I think it’s more pleasant to see the entire `struct animal` before the variable name in a declaration.

But that’s just, like, my opinion, man.

## 20.3 Self-Referential `struct`s

For any graph-like data structure, it’s useful to be able to have pointers to the connected nodes/vertices. But this means that in the definition of a node, you need to have a pointer to a node. It’s chicken and eggy!

But it turns out you can do this in C with no problem whatsoever.

For example, here’s a linked list node:
    
    
    [](structs-ii-more-fun-with-structs.html#cb436-1)struct node {
    [](structs-ii-more-fun-with-structs.html#cb436-2)    int data;
    [](structs-ii-more-fun-with-structs.html#cb436-3)    struct node *next;
    [](structs-ii-more-fun-with-structs.html#cb436-4)};

It’s important to note that `next` is a pointer. This is what allows the whole thing to even build. Even though the compiler doesn’t know what the entire `struct node` looks like yet, all pointers are the same size.

Here’s a cheesy linked list program to test it out:
    
    
    [](structs-ii-more-fun-with-structs.html#cb437-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb437-2)#include <stdlib.h>
    [](structs-ii-more-fun-with-structs.html#cb437-3)
    [](structs-ii-more-fun-with-structs.html#cb437-4)struct node {
    [](structs-ii-more-fun-with-structs.html#cb437-5)    int data;
    [](structs-ii-more-fun-with-structs.html#cb437-6)    struct node *next;
    [](structs-ii-more-fun-with-structs.html#cb437-7)};
    [](structs-ii-more-fun-with-structs.html#cb437-8)
    [](structs-ii-more-fun-with-structs.html#cb437-9)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb437-10){
    [](structs-ii-more-fun-with-structs.html#cb437-11)    struct node *head;
    [](structs-ii-more-fun-with-structs.html#cb437-12)
    [](structs-ii-more-fun-with-structs.html#cb437-13)    // Hackishly set up a linked list (11)->(22)->(33)
    [](structs-ii-more-fun-with-structs.html#cb437-14)    head = malloc(sizeof(struct node));
    [](structs-ii-more-fun-with-structs.html#cb437-15)    head->data = 11;
    [](structs-ii-more-fun-with-structs.html#cb437-16)    head->next = malloc(sizeof(struct node));
    [](structs-ii-more-fun-with-structs.html#cb437-17)    head->next->data = 22;
    [](structs-ii-more-fun-with-structs.html#cb437-18)    head->next->next = malloc(sizeof(struct node));
    [](structs-ii-more-fun-with-structs.html#cb437-19)    head->next->next->data = 33;
    [](structs-ii-more-fun-with-structs.html#cb437-20)    head->next->next->next = NULL;
    [](structs-ii-more-fun-with-structs.html#cb437-21)
    [](structs-ii-more-fun-with-structs.html#cb437-22)    // Traverse it
    [](structs-ii-more-fun-with-structs.html#cb437-23)    for (struct node *cur = head; cur != NULL; cur = cur->next) {
    [](structs-ii-more-fun-with-structs.html#cb437-24)        printf("%d\n", cur->data);
    [](structs-ii-more-fun-with-structs.html#cb437-25)    }
    [](structs-ii-more-fun-with-structs.html#cb437-26)}

Running that prints:
    
    
    [](structs-ii-more-fun-with-structs.html#cb438-1)11
    [](structs-ii-more-fun-with-structs.html#cb438-2)22
    [](structs-ii-more-fun-with-structs.html#cb438-3)33

## 20.4 Flexible Array Members

Back in the good old days, when people carved C code out of wood, some folks thought would be neat if they could allocate `struct`s that had variable length arrays at the end of them.

I want to be clear that the first part of the section is the old way of doing things, and we’re going to do things the new way after that.

For example, maybe you could define a `struct` for holding strings and the length of that string. It would have a length and an array to hold the data. Maybe something like this:
    
    
    [](structs-ii-more-fun-with-structs.html#cb439-1)struct len_string {
    [](structs-ii-more-fun-with-structs.html#cb439-2)    int length;
    [](structs-ii-more-fun-with-structs.html#cb439-3)    char data[8];
    [](structs-ii-more-fun-with-structs.html#cb439-4)};

But that has `8` hardcoded as the maximum length of a string, and that’s not much. What if we did something _clever_ and just `malloc()`d some extra space at the end after the struct, and then let the data overflow into that space?

Let’s do that, and then allocate another 40 bytes on top of it:
    
    
    [](structs-ii-more-fun-with-structs.html#cb440-1)struct len_string *s = malloc(sizeof *s + 40);

Because `data` is the last field of the `struct`, if we overflow that field, it runs out into space that we already allocated! For this reason, this trick only works if the short array is the _last_ field in the `struct`.
    
    
    [](structs-ii-more-fun-with-structs.html#cb441-1)// Copy more than 8 bytes!
    [](structs-ii-more-fun-with-structs.html#cb441-2)
    [](structs-ii-more-fun-with-structs.html#cb441-3)strcpy(s->data, "Hello, world!");  // Won't crash. Probably.

In fact, there was a common compiler workaround for doing this, where you’d allocate a zero length array at the end:
    
    
    [](structs-ii-more-fun-with-structs.html#cb442-1)struct len_string {
    [](structs-ii-more-fun-with-structs.html#cb442-2)    int length;
    [](structs-ii-more-fun-with-structs.html#cb442-3)    char data[0];
    [](structs-ii-more-fun-with-structs.html#cb442-4)};

And then every extra byte you allocated was ready for use in that string.

Because `data` is the last field of the `struct`, if we overflow that field, it runs out into space that we already allocated!
    
    
    [](structs-ii-more-fun-with-structs.html#cb443-1)// Copy more than 8 bytes!
    [](structs-ii-more-fun-with-structs.html#cb443-2)
    [](structs-ii-more-fun-with-structs.html#cb443-3)strcpy(s->data, "Hello, world!");  // Won't crash. Probably.

But, of course, actually accessing the data beyond the end of that array is undefined behavior! In these modern times, we no longer deign to resort to such savagery.

Luckily for us, we can still get the same effect with C99 and later, but now it’s legal.

Let’s just change our above definition to have no size for the array[135](function-specifiers-alignment-specifiersoperators.html#fn135):
    
    
    [](structs-ii-more-fun-with-structs.html#cb444-1)struct len_string {
    [](structs-ii-more-fun-with-structs.html#cb444-2)    int length;
    [](structs-ii-more-fun-with-structs.html#cb444-3)    char data[];
    [](structs-ii-more-fun-with-structs.html#cb444-4)};

Again, this only works if the flexible array member is the _last_ field in the `struct`.

And then we can allocate all the space we want for those strings by `malloc()`ing larger than the `struct len_string`, as we do in this example that makes a new `struct len_string` from a C string:
    
    
    [](structs-ii-more-fun-with-structs.html#cb445-1)struct len_string *len_string_from_c_string(char *s)
    [](structs-ii-more-fun-with-structs.html#cb445-2){
    [](structs-ii-more-fun-with-structs.html#cb445-3)    int len = strlen(s);
    [](structs-ii-more-fun-with-structs.html#cb445-4)
    [](structs-ii-more-fun-with-structs.html#cb445-5)    // Allocate "len" more bytes than we'd normally need
    [](structs-ii-more-fun-with-structs.html#cb445-6)    struct len_string *ls = malloc(sizeof *ls + len);
    [](structs-ii-more-fun-with-structs.html#cb445-7)
    [](structs-ii-more-fun-with-structs.html#cb445-8)    ls->length = len;
    [](structs-ii-more-fun-with-structs.html#cb445-9)
    [](structs-ii-more-fun-with-structs.html#cb445-10)    // Copy the string into those extra bytes
    [](structs-ii-more-fun-with-structs.html#cb445-11)    memcpy(ls->data, s, len);
    [](structs-ii-more-fun-with-structs.html#cb445-12)
    [](structs-ii-more-fun-with-structs.html#cb445-13)    return ls;
    [](structs-ii-more-fun-with-structs.html#cb445-14)}

## 20.5 Padding Bytes

Beware that C is allowed to add padding bytes within or after a `struct` as it sees fit. You can’t trust that they will be directly adjacent in memory[136](function-specifiers-alignment-specifiersoperators.html#fn136).

Let’s take a look at this program. We output two numbers. One is the sum of the `sizeof`s the individual field types. The other is the `sizeof` the entire `struct`.

One would expect them to be the same. The size of the total is the size of the sum of its parts, right?
    
    
    [](structs-ii-more-fun-with-structs.html#cb446-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb446-2)
    [](structs-ii-more-fun-with-structs.html#cb446-3)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb446-4)    int a;
    [](structs-ii-more-fun-with-structs.html#cb446-5)    char b;
    [](structs-ii-more-fun-with-structs.html#cb446-6)    int c;
    [](structs-ii-more-fun-with-structs.html#cb446-7)    char d;
    [](structs-ii-more-fun-with-structs.html#cb446-8)};
    [](structs-ii-more-fun-with-structs.html#cb446-9)
    [](structs-ii-more-fun-with-structs.html#cb446-10)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb446-11){
    [](structs-ii-more-fun-with-structs.html#cb446-12)    printf("%zu\n", sizeof(int) + sizeof(char) + sizeof(int) + sizeof(char));
    [](structs-ii-more-fun-with-structs.html#cb446-13)    printf("%zu\n", sizeof(struct foo));
    [](structs-ii-more-fun-with-structs.html#cb446-14)}

But on my system, this outputs:
    
    
    [](structs-ii-more-fun-with-structs.html#cb447-1)10
    [](structs-ii-more-fun-with-structs.html#cb447-2)16

They’re not the same! The compiler has added 6 bytes of padding to help it be more performant. Maybe you got different output with your compiler, but unless you’re forcing it, you can’t be sure there’s no padding.

## 20.6 `offsetof`

In the previous section, we saw that the compiler could inject padding bytes at will inside a structure.

What if we needed to know where those were? We can measure it with `offsetof`, defined in `<stddef.h>`.

Let’s modify the code from above to print the offsets of the individual fields in the `struct`:
    
    
    [](structs-ii-more-fun-with-structs.html#cb448-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb448-2)#include <stddef.h>
    [](structs-ii-more-fun-with-structs.html#cb448-3)
    [](structs-ii-more-fun-with-structs.html#cb448-4)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb448-5)    int a;
    [](structs-ii-more-fun-with-structs.html#cb448-6)    char b;
    [](structs-ii-more-fun-with-structs.html#cb448-7)    int c;
    [](structs-ii-more-fun-with-structs.html#cb448-8)    char d;
    [](structs-ii-more-fun-with-structs.html#cb448-9)};
    [](structs-ii-more-fun-with-structs.html#cb448-10)
    [](structs-ii-more-fun-with-structs.html#cb448-11)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb448-12){
    [](structs-ii-more-fun-with-structs.html#cb448-13)    printf("%zu\n", offsetof(struct foo, a));
    [](structs-ii-more-fun-with-structs.html#cb448-14)    printf("%zu\n", offsetof(struct foo, b));
    [](structs-ii-more-fun-with-structs.html#cb448-15)    printf("%zu\n", offsetof(struct foo, c));
    [](structs-ii-more-fun-with-structs.html#cb448-16)    printf("%zu\n", offsetof(struct foo, d));
    [](structs-ii-more-fun-with-structs.html#cb448-17)}

For me, this outputs:
    
    
    [](structs-ii-more-fun-with-structs.html#cb449-1)0
    [](structs-ii-more-fun-with-structs.html#cb449-2)4
    [](structs-ii-more-fun-with-structs.html#cb449-3)8
    [](structs-ii-more-fun-with-structs.html#cb449-4)12

indicating that we’re using 4 bytes for each of the fields. It’s a little weird, because `char` is only 1 byte, right? The compiler is putting 3 padding bytes after each `char` so that all the fields are 4 bytes long. Presumably this will run faster on my CPU.

## 20.7 Fake OOP

There’s a slightly abusive thing that’s sort of OOP-like that you can do with `struct`s.

Since the pointer to the `struct` is the same as a pointer to the first element of the `struct`, you can freely cast a pointer to the `struct` to a pointer to the first element.

What this means is that we can set up a situation like this:
    
    
    [](structs-ii-more-fun-with-structs.html#cb450-1)struct parent {
    [](structs-ii-more-fun-with-structs.html#cb450-2)    int a, b;
    [](structs-ii-more-fun-with-structs.html#cb450-3)};
    [](structs-ii-more-fun-with-structs.html#cb450-4)
    [](structs-ii-more-fun-with-structs.html#cb450-5)struct child {
    [](structs-ii-more-fun-with-structs.html#cb450-6)    struct parent super;  // MUST be first
    [](structs-ii-more-fun-with-structs.html#cb450-7)    int c, d;
    [](structs-ii-more-fun-with-structs.html#cb450-8)};

Then we are able to pass a pointer to a `struct child` to a function that expects either that _or_ a pointer to a `struct parent`!

Because `struct parent super` is the first item in the `struct child`, a pointer to any `struct child` is the same as a pointer to that `super` field[137](function-specifiers-alignment-specifiersoperators.html#fn137).

Let’s set up an example here. We’ll make `struct`s as above, but then we’ll pass a pointer to a `struct child` to a function that needs a pointer to a `struct parent`… and it’ll still work.
    
    
    [](structs-ii-more-fun-with-structs.html#cb451-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb451-2)
    [](structs-ii-more-fun-with-structs.html#cb451-3)struct parent {
    [](structs-ii-more-fun-with-structs.html#cb451-4)    int a, b;
    [](structs-ii-more-fun-with-structs.html#cb451-5)};
    [](structs-ii-more-fun-with-structs.html#cb451-6)
    [](structs-ii-more-fun-with-structs.html#cb451-7)struct child {
    [](structs-ii-more-fun-with-structs.html#cb451-8)    struct parent super;  // MUST be first
    [](structs-ii-more-fun-with-structs.html#cb451-9)    int c, d;
    [](structs-ii-more-fun-with-structs.html#cb451-10)};
    [](structs-ii-more-fun-with-structs.html#cb451-11)
    [](structs-ii-more-fun-with-structs.html#cb451-12)// Making the argument `void*` so we can pass any type into it
    [](structs-ii-more-fun-with-structs.html#cb451-13)// (namely a struct parent or struct child)
    [](structs-ii-more-fun-with-structs.html#cb451-14)void print_parent(void *p)
    [](structs-ii-more-fun-with-structs.html#cb451-15){
    [](structs-ii-more-fun-with-structs.html#cb451-16)    // Expects a struct parent--but a struct child will also work
    [](structs-ii-more-fun-with-structs.html#cb451-17)    // because the pointer points to the struct parent in the first
    [](structs-ii-more-fun-with-structs.html#cb451-18)    // field:
    [](structs-ii-more-fun-with-structs.html#cb451-19)    struct parent *self = p;
    [](structs-ii-more-fun-with-structs.html#cb451-20)
    [](structs-ii-more-fun-with-structs.html#cb451-21)    printf("Parent: %d, %d\n", self->a, self->b);
    [](structs-ii-more-fun-with-structs.html#cb451-22)}
    [](structs-ii-more-fun-with-structs.html#cb451-23)
    [](structs-ii-more-fun-with-structs.html#cb451-24)void print_child(struct child *self)
    [](structs-ii-more-fun-with-structs.html#cb451-25){
    [](structs-ii-more-fun-with-structs.html#cb451-26)    printf("Child: %d, %d\n", self->c, self->d);
    [](structs-ii-more-fun-with-structs.html#cb451-27)}
    [](structs-ii-more-fun-with-structs.html#cb451-28)
    [](structs-ii-more-fun-with-structs.html#cb451-29)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb451-30){
    [](structs-ii-more-fun-with-structs.html#cb451-31)    struct child c = {.super.a=1, .super.b=2, .c=3, .d=4};
    [](structs-ii-more-fun-with-structs.html#cb451-32)
    [](structs-ii-more-fun-with-structs.html#cb451-33)    print_child(&c);
    [](structs-ii-more-fun-with-structs.html#cb451-34)    print_parent(&c);  // Also works even though it's a struct child!
    [](structs-ii-more-fun-with-structs.html#cb451-35)}

See what we did on the last line of `main()`? We called `print_parent()` but passed a `struct child*` as the argument! Even though `print_parent()` needs the argument to point to a `struct parent`, we’re _getting away with it_ because the first field in the `struct child` is a `struct parent`.

Again, this works because a pointer to a `struct` has the same value as a pointer to the first field in that `struct`.

This all hinges on this part of the spec:

> **§6.7.2.1¶15** […] A pointer to a structure object, suitably converted, points to its initial member […], and vice versa.

and

> **§6.5¶7** An object shall have its stored value accessed only by an lvalue expression that has one of the following types:
> 
>   * a type compatible with the effective type of the object
>   * […]
> 


and my assumption that “suitably converted” means “cast to the effective type of the initial member”.

## 20.8 Bit-Fields

In my experience, these are rarely used, but you might see them out there from time to time, especially in lower-level applications that pack bits together into larger spaces.

Let’s take a look at some code to demonstrate a use case:
    
    
    [](structs-ii-more-fun-with-structs.html#cb452-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb452-2)
    [](structs-ii-more-fun-with-structs.html#cb452-3)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb452-4)    unsigned int a;
    [](structs-ii-more-fun-with-structs.html#cb452-5)    unsigned int b;
    [](structs-ii-more-fun-with-structs.html#cb452-6)    unsigned int c;
    [](structs-ii-more-fun-with-structs.html#cb452-7)    unsigned int d;
    [](structs-ii-more-fun-with-structs.html#cb452-8)};
    [](structs-ii-more-fun-with-structs.html#cb452-9)
    [](structs-ii-more-fun-with-structs.html#cb452-10)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb452-11){
    [](structs-ii-more-fun-with-structs.html#cb452-12)    printf("%zu\n", sizeof(struct foo));
    [](structs-ii-more-fun-with-structs.html#cb452-13)}

For me, this prints `16`. Which makes sense, since `unsigned`s are 4 bytes on my system.

But what if we knew that all the values that were going to be stored in `a` and `b` could be stored in 5 bits, and the values in `c`, and `d` could be stored in 3 bits? That’s only a total 16 bits. Why have 128 bits reserved for them if we’re only going to use 16?

Well, we can tell C to pretty-please try to pack these values in. We can specify the maximum number of bits that values can take (from 1 up the size of the containing type).

We do this by putting a colon after the field name, followed by the field width in bits.
    
    
    [](structs-ii-more-fun-with-structs.html#cb453-3)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb453-4)    unsigned int a:5;
    [](structs-ii-more-fun-with-structs.html#cb453-5)    unsigned int b:5;
    [](structs-ii-more-fun-with-structs.html#cb453-6)    unsigned int c:3;
    [](structs-ii-more-fun-with-structs.html#cb453-7)    unsigned int d:3;
    [](structs-ii-more-fun-with-structs.html#cb453-8)};

Now when I ask C how big my `struct foo` is, it tells me 4! It was 16 bytes, but now it’s only 4. It has “packed” those 4 values down into 4 bytes, which is a four-fold memory savings.

The tradeoff is, of course, that the 5-bit fields can only hold values from 0-31 and the 3-bit fields can only hold values from 0-7. But life’s all about compromise, after all.

### 20.8.1 Non-Adjacent Bit-Fields

A gotcha: C will only combine **adjacent** bit-fields. If they’re interrupted by non-bit-fields, you get no savings:
    
    
    [](structs-ii-more-fun-with-structs.html#cb454-1)struct foo {            // sizeof(struct foo) == 16 (for me)
    [](structs-ii-more-fun-with-structs.html#cb454-2)    unsigned int a:1;   // since a is not adjacent to c.
    [](structs-ii-more-fun-with-structs.html#cb454-3)    unsigned int b;
    [](structs-ii-more-fun-with-structs.html#cb454-4)    unsigned int c:1;
    [](structs-ii-more-fun-with-structs.html#cb454-5)    unsigned int d;
    [](structs-ii-more-fun-with-structs.html#cb454-6)};

In that example, since `a` is not adjacent to `c`, they are both “packed” in their own `int`s.

So we have one `int` each for `a`, `b`, `c`, and `d`. Since my `int`s are 4 bytes, that’s a grand total of 16 bytes.

A quick rearrangement yields some space savings from 16 bytes down to 12 bytes (on my system):
    
    
    [](structs-ii-more-fun-with-structs.html#cb455-1)struct foo {            // sizeof(struct foo) == 12 (for me)
    [](structs-ii-more-fun-with-structs.html#cb455-2)    unsigned int a:1;
    [](structs-ii-more-fun-with-structs.html#cb455-3)    unsigned int c:1;
    [](structs-ii-more-fun-with-structs.html#cb455-4)    unsigned int b;
    [](structs-ii-more-fun-with-structs.html#cb455-5)    unsigned int d;
    [](structs-ii-more-fun-with-structs.html#cb455-6)};

And now, since `a` is next to `c`, the compiler puts them together into a single `int`.

So we have one `int` for a combined `a` and `c`, and one `int` each for `b` and `d`. For a grand total of 3 `int`s, or 12 bytes.

Put all your bitfields together to get the compiler to combine them.

### 20.8.2 Signed or Unsigned `int`s

If you just declare a bit-field to be `int`, the different compilers will treat it as `signed` or `unsigned`. Just like the situation with `char`.

Be specific about the signedness when using bit-fields.

### 20.8.3 Unnamed Bit-Fields

In some specific circumstances, you might need to reserve some bits for hardware reasons, but not need to use them in code.

For example, let’s say you have a byte where the top 2 bits have a meaning, the bottom 1 bit has a meaning, but the middle 5 bits do not get used by you[138](function-specifiers-alignment-specifiersoperators.html#fn138).

We _could_ do something like this:
    
    
    [](structs-ii-more-fun-with-structs.html#cb456-1)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb456-2)    unsigned char a:2;
    [](structs-ii-more-fun-with-structs.html#cb456-3)    unsigned char dummy:5;
    [](structs-ii-more-fun-with-structs.html#cb456-4)    unsigned char b:1;
    [](structs-ii-more-fun-with-structs.html#cb456-5)};

And that works—in our code we use `a` and `b`, but never `dummy`. It’s just there to eat up 5 bits to make sure `a` and `b` are in the “required” (by this contrived example) positions within the byte.

C allows us a way to clean this up: _unnamed bit-fields_. You can just leave the name (`dummy`) out in this case, and C is perfectly happy for the same effect:
    
    
    [](structs-ii-more-fun-with-structs.html#cb457-1)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb457-2)    unsigned char a:2;
    [](structs-ii-more-fun-with-structs.html#cb457-3)    unsigned char :5;   // <-- unnamed bit-field!
    [](structs-ii-more-fun-with-structs.html#cb457-4)    unsigned char b:1;
    [](structs-ii-more-fun-with-structs.html#cb457-5)};

### 20.8.4 Zero-Width Unnamed Bit-Fields

Some more esoterica out here… Let’s say you were packing bits into an `unsigned int`, and you needed some adjacent bit-fields to pack into the _next_ `unsigned int`.

That is, if you do this:
    
    
    [](structs-ii-more-fun-with-structs.html#cb458-1)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb458-2)    unsigned int a:1;
    [](structs-ii-more-fun-with-structs.html#cb458-3)    unsigned int b:2;
    [](structs-ii-more-fun-with-structs.html#cb458-4)    unsigned int c:3;
    [](structs-ii-more-fun-with-structs.html#cb458-5)    unsigned int d:4;
    [](structs-ii-more-fun-with-structs.html#cb458-6)};

the compiler packs all those into a single `unsigned int`. But what if you needed `a` and `b` in one `int`, and `c` and `d` in a different one?

There’s a solution for that: put an unnamed bit-field of width `0` where you want the compiler to start anew with packing bits in a different `int`:
    
    
    [](structs-ii-more-fun-with-structs.html#cb459-1)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb459-2)    unsigned int a:1;
    [](structs-ii-more-fun-with-structs.html#cb459-3)    unsigned int b:2;
    [](structs-ii-more-fun-with-structs.html#cb459-4)    unsigned int :0;   // <--Zero-width unnamed bit-field
    [](structs-ii-more-fun-with-structs.html#cb459-5)    unsigned int c:3;
    [](structs-ii-more-fun-with-structs.html#cb459-6)    unsigned int d:4;
    [](structs-ii-more-fun-with-structs.html#cb459-7)};

It’s analogous to an explicit page break in a word processor. You’re telling the compiler, “Stop packing bits in this `unsigned`, and start packing them in the next one.”

By adding the zero-width unnamed bit field in that spot, the compiler puts `a` and `b` in one `unsigned int`, and `c` and `d` in another `unsigned int`. Two total, for a size of 8 bytes on my system (`unsigned int`s are 4 bytes each).

## 20.9 Unions

These are basically just like `struct`s, except the fields overlap in memory. The `union` will be only large enough for the largest field, and you can only use one field at a time.

It’s a way to reuse the same memory space for different types of data.

You declare them just like `struct`s, except it’s `union`. Take a look at this:
    
    
    [](structs-ii-more-fun-with-structs.html#cb460-1)union foo {
    [](structs-ii-more-fun-with-structs.html#cb460-2)    int a, b, c, d, e, f;
    [](structs-ii-more-fun-with-structs.html#cb460-3)    float g, h;
    [](structs-ii-more-fun-with-structs.html#cb460-4)    char i, j, k, l;
    [](structs-ii-more-fun-with-structs.html#cb460-5)};

Now, that’s a lot of fields. If this were a `struct`, my system would tell me it took 36 bytes to hold it all.

But it’s a `union`, so all those fields overlap in the same stretch of memory. The biggest one is `int` (or `float`), taking up 4 bytes on my system. And, indeed, if I ask for the `sizeof` the `union foo`, it tells me 4!

The tradeoff is that you can only portably use one of those fields at a time. However…

### 20.9.1 Unions and Type Punning

You can non-portably write to one `union` field and read from another!

Doing so is called [type punning](https://en.wikipedia.org/wiki/Type_punning)[139](function-specifiers-alignment-specifiersoperators.html#fn139), and you’d use it if you really knew what you were doing, typically with some kind of low-level programming.

Since the members of a union share the same memory, writing to one member necessarily affects the others. And if you read from one what was written to another, you get some weird effects.
    
    
    [](structs-ii-more-fun-with-structs.html#cb461-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb461-2)
    [](structs-ii-more-fun-with-structs.html#cb461-3)union foo {
    [](structs-ii-more-fun-with-structs.html#cb461-4)    float b;
    [](structs-ii-more-fun-with-structs.html#cb461-5)    short a;
    [](structs-ii-more-fun-with-structs.html#cb461-6)};
    [](structs-ii-more-fun-with-structs.html#cb461-7)
    [](structs-ii-more-fun-with-structs.html#cb461-8)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb461-9){
    [](structs-ii-more-fun-with-structs.html#cb461-10)    union foo x;
    [](structs-ii-more-fun-with-structs.html#cb461-11)
    [](structs-ii-more-fun-with-structs.html#cb461-12)    x.b = 3.14159;
    [](structs-ii-more-fun-with-structs.html#cb461-13)
    [](structs-ii-more-fun-with-structs.html#cb461-14)    printf("%f\n", x.b);  // 3.14159, fair enough
    [](structs-ii-more-fun-with-structs.html#cb461-15)
    [](structs-ii-more-fun-with-structs.html#cb461-16)    printf("%d\n", x.a);  // But what about this?
    [](structs-ii-more-fun-with-structs.html#cb461-17)}

On my system, this prints out:
    
    
    3.141590
    4048

because under the hood, the object representation for the float `3.14159` was the same as the object representation for the short `4048`. On my system. Your results may vary.

### 20.9.2 Pointers to `union`s

If you have a pointer to a `union`, you can cast that pointer to any of the types of the fields in that `union` and get the values out that way.

In this example, we see that the `union` has `int`s and `float`s in it. And we get pointers to the `union`, but we cast them to `int*` and `float*` types (the cast silences compiler warnings). And then if we dereference those, we see that they have the values we stored directly in the `union`.
    
    
    [](structs-ii-more-fun-with-structs.html#cb463-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb463-2)
    [](structs-ii-more-fun-with-structs.html#cb463-3)union foo {
    [](structs-ii-more-fun-with-structs.html#cb463-4)    int a, b, c, d, e, f;
    [](structs-ii-more-fun-with-structs.html#cb463-5)    float g, h;
    [](structs-ii-more-fun-with-structs.html#cb463-6)    char i, j, k, l;
    [](structs-ii-more-fun-with-structs.html#cb463-7)};
    [](structs-ii-more-fun-with-structs.html#cb463-8)
    [](structs-ii-more-fun-with-structs.html#cb463-9)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb463-10){
    [](structs-ii-more-fun-with-structs.html#cb463-11)    union foo x;
    [](structs-ii-more-fun-with-structs.html#cb463-12)
    [](structs-ii-more-fun-with-structs.html#cb463-13)    int *foo_int_p = (int *)&x;
    [](structs-ii-more-fun-with-structs.html#cb463-14)    float *foo_float_p = (float *)&x;
    [](structs-ii-more-fun-with-structs.html#cb463-15)
    [](structs-ii-more-fun-with-structs.html#cb463-16)    x.a = 12;
    [](structs-ii-more-fun-with-structs.html#cb463-17)    printf("%d\n", x.a);           // 12
    [](structs-ii-more-fun-with-structs.html#cb463-18)    printf("%d\n", *foo_int_p);    // 12, again
    [](structs-ii-more-fun-with-structs.html#cb463-19)
    [](structs-ii-more-fun-with-structs.html#cb463-20)    x.g = 3.141592;
    [](structs-ii-more-fun-with-structs.html#cb463-21)    printf("%f\n", x.g);           // 3.141592
    [](structs-ii-more-fun-with-structs.html#cb463-22)    printf("%f\n", *foo_float_p);  // 3.141592, again
    [](structs-ii-more-fun-with-structs.html#cb463-23)}

The reverse is also true. If we have a pointer to a type inside the `union`, we can cast that to a pointer to the `union` and access its members.
    
    
    [](structs-ii-more-fun-with-structs.html#cb464-1)union foo x;
    [](structs-ii-more-fun-with-structs.html#cb464-2)int *foo_int_p = (int *)&x;             // Pointer to int field
    [](structs-ii-more-fun-with-structs.html#cb464-3)union foo *p = (union foo *)foo_int_p;  // Back to pointer to union
    [](structs-ii-more-fun-with-structs.html#cb464-4)
    [](structs-ii-more-fun-with-structs.html#cb464-5)p->a = 12;  // This line the same as...
    [](structs-ii-more-fun-with-structs.html#cb464-6)x.a = 12;   // this one.

All this just lets you know that, under the hood, all these values in a `union` start at the same place in memory, and that’s the same as where the entire `union` is.

### 20.9.3 Common Initial Sequences in Unions

If you have a `union` of `struct`s, and all those `struct`s begin with a _common initial sequence_ , it’s valid to access members of that sequence from any of the `union` members.

What?

Here are two `struct`s with a common initial sequence:
    
    
    [](structs-ii-more-fun-with-structs.html#cb465-1)struct a {
    [](structs-ii-more-fun-with-structs.html#cb465-2)    int x;     //
    [](structs-ii-more-fun-with-structs.html#cb465-3)    float y;   // Common initial sequence
    [](structs-ii-more-fun-with-structs.html#cb465-4)
    [](structs-ii-more-fun-with-structs.html#cb465-5)    char *p;
    [](structs-ii-more-fun-with-structs.html#cb465-6)};
    [](structs-ii-more-fun-with-structs.html#cb465-7)
    [](structs-ii-more-fun-with-structs.html#cb465-8)struct b {
    [](structs-ii-more-fun-with-structs.html#cb465-9)    int x;     //
    [](structs-ii-more-fun-with-structs.html#cb465-10)    float y;   // Common initial sequence
    [](structs-ii-more-fun-with-structs.html#cb465-11)
    [](structs-ii-more-fun-with-structs.html#cb465-12)    double *p;
    [](structs-ii-more-fun-with-structs.html#cb465-13)    short z;
    [](structs-ii-more-fun-with-structs.html#cb465-14)};

Do you see it? It’s that they start with `int` followed by `float`—that’s the common initial sequence. The members in the sequence of the `struct`s have to be compatible types. And we see that with `x` and `y`, which are `int` and `float` respectively.

Now let’s build a union of these:
    
    
    [](structs-ii-more-fun-with-structs.html#cb466-1)union foo {
    [](structs-ii-more-fun-with-structs.html#cb466-2)    struct a sa;
    [](structs-ii-more-fun-with-structs.html#cb466-3)    struct b sb;
    [](structs-ii-more-fun-with-structs.html#cb466-4)};

What this rule tells us is that we’re guaranteed that the members of the common initial sequences are interchangeable in code. That is:

  * `f.sa.x` is the same as `f.sb.x`.



and

  * `f.sa.y` is the same as `f.sb.y`.



Because fields `x` and `y` are both in the common initial sequence.

Also, the names of the members in the common initial sequence don’t matter—all that matters is that the types are the same.

All together, this allows us a way to safely add some shared information between `struct`s in the `union`. The best example of this is probably using a field to determine the type of `struct` out of all the `struct`s in the `union` that is currently “in use”.

That is, if we weren’t allowed this and we passed the `union` to some function, how would that function know which member of the `union` was the one it should look at?

Take a look at these `struct`s. Note the common initial sequence:
    
    
    [](structs-ii-more-fun-with-structs.html#cb467-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb467-2)
    [](structs-ii-more-fun-with-structs.html#cb467-3)struct common {
    [](structs-ii-more-fun-with-structs.html#cb467-4)    int type;   // common initial sequence
    [](structs-ii-more-fun-with-structs.html#cb467-5)};
    [](structs-ii-more-fun-with-structs.html#cb467-6)
    [](structs-ii-more-fun-with-structs.html#cb467-7)struct antelope {
    [](structs-ii-more-fun-with-structs.html#cb467-8)    int type;   // common initial sequence
    [](structs-ii-more-fun-with-structs.html#cb467-9)
    [](structs-ii-more-fun-with-structs.html#cb467-10)    int loudness;
    [](structs-ii-more-fun-with-structs.html#cb467-11)};
    [](structs-ii-more-fun-with-structs.html#cb467-12)
    [](structs-ii-more-fun-with-structs.html#cb467-13)struct octopus {
    [](structs-ii-more-fun-with-structs.html#cb467-14)    int type;   // common initial sequence
    [](structs-ii-more-fun-with-structs.html#cb467-15)
    [](structs-ii-more-fun-with-structs.html#cb467-16)    int sea_creature;
    [](structs-ii-more-fun-with-structs.html#cb467-17)    float intelligence;
    [](structs-ii-more-fun-with-structs.html#cb467-18)};

Now let’s throw them into a `union`:
    
    
    [](structs-ii-more-fun-with-structs.html#cb468-20)union animal {
    [](structs-ii-more-fun-with-structs.html#cb468-21)    struct common common;
    [](structs-ii-more-fun-with-structs.html#cb468-22)    struct antelope antelope;
    [](structs-ii-more-fun-with-structs.html#cb468-23)    struct octopus octopus;
    [](structs-ii-more-fun-with-structs.html#cb468-24)};

Also, please indulge me these two `#define`s for the demo:
    
    
    [](structs-ii-more-fun-with-structs.html#cb469-26)#define ANTELOPE 1
    [](structs-ii-more-fun-with-structs.html#cb469-27)#define OCTOPUS  2

So far, nothing special has happened here. It seems like the `type` field is completely useless.

But now let’s make a generic function that prints a `union animal`. It has to somehow be able to tell if it’s looking at a `struct antelope` or a `struct octopus`.

Because of the magic of common initial sequences, it can look up the animal type in any of these places for a particular `union animal x`:
    
    
    [](structs-ii-more-fun-with-structs.html#cb470-1)int type = x.common.type;    \\ or...
    [](structs-ii-more-fun-with-structs.html#cb470-2)int type = x.antelope.type;  \\ or...
    [](structs-ii-more-fun-with-structs.html#cb470-3)int type = x.octopus.type;

All those refer to the same value in memory.

And, as you might have guessed, the `struct common` is there so code can agnostically look at the type without mentioning a particular animal.

Let’s look at the code to print a `union animal`:
    
    
    [](structs-ii-more-fun-with-structs.html#cb471-29)void print_animal(union animal *x)
    [](structs-ii-more-fun-with-structs.html#cb471-30){
    [](structs-ii-more-fun-with-structs.html#cb471-31)    switch (x->common.type) {
    [](structs-ii-more-fun-with-structs.html#cb471-32)        case ANTELOPE:
    [](structs-ii-more-fun-with-structs.html#cb471-33)            printf("Antelope: loudness=%d\n", x->antelope.loudness);
    [](structs-ii-more-fun-with-structs.html#cb471-34)            break;
    [](structs-ii-more-fun-with-structs.html#cb471-35)
    [](structs-ii-more-fun-with-structs.html#cb471-36)        case OCTOPUS:
    [](structs-ii-more-fun-with-structs.html#cb471-37)            printf("Octopus : sea_creature=%d\n", x->octopus.sea_creature);
    [](structs-ii-more-fun-with-structs.html#cb471-38)            printf("          intelligence=%f\n", x->octopus.intelligence);
    [](structs-ii-more-fun-with-structs.html#cb471-39)            break;
    [](structs-ii-more-fun-with-structs.html#cb471-40)        
    [](structs-ii-more-fun-with-structs.html#cb471-41)        default:
    [](structs-ii-more-fun-with-structs.html#cb471-42)            printf("Unknown animal type\n");
    [](structs-ii-more-fun-with-structs.html#cb471-43)    }
    [](structs-ii-more-fun-with-structs.html#cb471-44)
    [](structs-ii-more-fun-with-structs.html#cb471-45)}
    [](structs-ii-more-fun-with-structs.html#cb471-46)
    [](structs-ii-more-fun-with-structs.html#cb471-47)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb471-48){
    [](structs-ii-more-fun-with-structs.html#cb471-49)    union animal a = {.antelope.type=ANTELOPE, .antelope.loudness=12};
    [](structs-ii-more-fun-with-structs.html#cb471-50)    union animal b = {.octopus.type=OCTOPUS, .octopus.sea_creature=1,
    [](structs-ii-more-fun-with-structs.html#cb471-51)                                       .octopus.intelligence=12.8};
    [](structs-ii-more-fun-with-structs.html#cb471-52)
    [](structs-ii-more-fun-with-structs.html#cb471-53)    print_animal(&a);
    [](structs-ii-more-fun-with-structs.html#cb471-54)    print_animal(&b);
    [](structs-ii-more-fun-with-structs.html#cb471-55)}

See how on line 29 we’re just passing in the `union`—we have no idea what type of animal `struct` is in use within it.

But that’s OK! Because on line 31 we check the type to see if it’s an antelope or an octopus. And then we can look at the proper `struct` to get the members.

It’s definitely possible to get this same effect using just `struct`s, but you can do it this way if you want the memory-saving effects of a `union`.

## 20.10 Unions and Unnamed Structs

You know how you can have an unnamed `struct`, like this:
    
    
    [](structs-ii-more-fun-with-structs.html#cb472-1)struct {
    [](structs-ii-more-fun-with-structs.html#cb472-2)    int x, y;
    [](structs-ii-more-fun-with-structs.html#cb472-3)} s;

That defines a variable `s` that is of anonymous `struct` type (because the `struct` has no name tag), with members `x` and `y`.

So things like this are valid:
    
    
    [](structs-ii-more-fun-with-structs.html#cb473-1)s.x = 34;
    [](structs-ii-more-fun-with-structs.html#cb473-2)s.y = 90;
    [](structs-ii-more-fun-with-structs.html#cb473-3)
    [](structs-ii-more-fun-with-structs.html#cb473-4)printf("%d %d\n", s.x, s.y);

Turns out you can drop those unnamed `struct`s in `union`s just like you might expect:
    
    
    [](structs-ii-more-fun-with-structs.html#cb474-1)union foo {
    [](structs-ii-more-fun-with-structs.html#cb474-2)    struct {       // unnamed!
    [](structs-ii-more-fun-with-structs.html#cb474-3)        int x, y;
    [](structs-ii-more-fun-with-structs.html#cb474-4)    } a;
    [](structs-ii-more-fun-with-structs.html#cb474-5)
    [](structs-ii-more-fun-with-structs.html#cb474-6)    struct {       // unnamed!
    [](structs-ii-more-fun-with-structs.html#cb474-7)        int z, w;
    [](structs-ii-more-fun-with-structs.html#cb474-8)    } b;
    [](structs-ii-more-fun-with-structs.html#cb474-9)};

And then access them as per normal:
    
    
    [](structs-ii-more-fun-with-structs.html#cb475-1)union foo f;
    [](structs-ii-more-fun-with-structs.html#cb475-2)
    [](structs-ii-more-fun-with-structs.html#cb475-3)f.a.x = 1;
    [](structs-ii-more-fun-with-structs.html#cb475-4)f.a.y = 2;
    [](structs-ii-more-fun-with-structs.html#cb475-5)f.b.z = 3;
    [](structs-ii-more-fun-with-structs.html#cb475-6)f.b.w = 4;

No problem!

## 20.11 Passing and Returning `struct`s and `union`s

You can pass a `struct` or `union` to a function by value (as opposed to a pointer to it)—a copy of that object to the parameter will be made as if by assignment as per usual.

You can also return a `struct` or `union` from a function and it is also passed by value back.
    
    
    [](structs-ii-more-fun-with-structs.html#cb476-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb476-2)
    [](structs-ii-more-fun-with-structs.html#cb476-3)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb476-4)    int x, y;
    [](structs-ii-more-fun-with-structs.html#cb476-5)};
    [](structs-ii-more-fun-with-structs.html#cb476-6)
    [](structs-ii-more-fun-with-structs.html#cb476-7)struct foo f(void)
    [](structs-ii-more-fun-with-structs.html#cb476-8){
    [](structs-ii-more-fun-with-structs.html#cb476-9)    return (struct foo){.x=34, .y=90};
    [](structs-ii-more-fun-with-structs.html#cb476-10)}
    [](structs-ii-more-fun-with-structs.html#cb476-11)
    [](structs-ii-more-fun-with-structs.html#cb476-12)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb476-13){
    [](structs-ii-more-fun-with-structs.html#cb476-14)    struct foo a = f();  // Copy is made
    [](structs-ii-more-fun-with-structs.html#cb476-15)
    [](structs-ii-more-fun-with-structs.html#cb476-16)    printf("%d %d\n", a.x, a.y);
    [](structs-ii-more-fun-with-structs.html#cb476-17)}

Fun fact: if you do this, you can use the `.` operator right off the function call:
    
    
    [](structs-ii-more-fun-with-structs.html#cb477-16)    printf("%d %d\n", f().x, f().y);

(Of course that example calls the function twice, inefficiently.)

And the same holds true for returning pointers to `struct`s and `union`s—just be sure to use the `->` arrow operator in that case.

* * *

[Prev](the-c-preprocessor.html) | [Contents](index.html) | [Next](characters-and-strings-ii.html)
