[Prev](file-inputoutput.html) | [Contents](index.html) | [Next](pointers2.html)

* * *

# 10 `typedef`: Making New Types

Well, not so much making _new_ types as getting new names for existing types. Sounds kinda pointless on the surface, but we can really use this to make our code cleaner.

## 10.1 `typedef` in Theory

Basically, you take an existing type and you make an alias for it with `typedef`.

Like this:
    
    
    [](typedef-making-new-types.html#cb161-1)typedef int antelope;  // Make "antelope" an alias for "int"
    [](typedef-making-new-types.html#cb161-2)
    [](typedef-making-new-types.html#cb161-3)antelope x = 10;       // Type "antelope" is the same as type "int"

You can take any existing type and do it. You can even make a number of types with a comma list:
    
    
    [](typedef-making-new-types.html#cb162-1)typedef int antelope, bagel, mushroom;  // These are all "int"

That’s really useful, right? That you can type `mushroom` instead of `int`? You must be _super excited_ about this feature!

OK, Professor Sarcasm—we’ll get to some more common applications of this in a moment.

### 10.1.1 Scoping

`typedef` follows regular [scoping rules](scope.html#scope).

For this reason, it’s quite common to find `typedef` at file scope (“global”) so that all functions can use the new types at will.

## 10.2 `typedef` in Practice

So renaming `int` to something else isn’t that exciting. Let’s see where `typedef` commonly makes an appearance.

### 10.2.1 `typedef` and `struct`s

Sometimes a `struct` will be `typedef`’d to a new name so you don’t have to type the word `struct` over and over.
    
    
    [](typedef-making-new-types.html#cb163-1)struct animal {
    [](typedef-making-new-types.html#cb163-2)    char *name;
    [](typedef-making-new-types.html#cb163-3)    int leg_count, speed;
    [](typedef-making-new-types.html#cb163-4)};
    [](typedef-making-new-types.html#cb163-5)
    [](typedef-making-new-types.html#cb163-6)//  original name      new name
    [](typedef-making-new-types.html#cb163-7)//            |         |
    [](typedef-making-new-types.html#cb163-8)//            v         v
    [](typedef-making-new-types.html#cb163-9)//      |-----------| |----|
    [](typedef-making-new-types.html#cb163-10)typedef struct animal animal;
    [](typedef-making-new-types.html#cb163-11)
    [](typedef-making-new-types.html#cb163-12)struct animal y;  // This works
    [](typedef-making-new-types.html#cb163-13)animal z;         // This also works because "animal" is an alias

Personally, I don’t care for this practice. I like the clarity the code has when you add the word `struct` to the type; programmers know what they’re getting. But it’s really common so I’m including it here.

Now I want to run the exact same example in a way that you might commonly see. We’re going to put the `struct animal` _in_ the `typedef`. You can mash it all together like this:
    
    
    [](typedef-making-new-types.html#cb164-1)//  original name
    [](typedef-making-new-types.html#cb164-2)//            |
    [](typedef-making-new-types.html#cb164-3)//            v
    [](typedef-making-new-types.html#cb164-4)//      |-----------|
    [](typedef-making-new-types.html#cb164-5)typedef struct animal {
    [](typedef-making-new-types.html#cb164-6)    char *name;
    [](typedef-making-new-types.html#cb164-7)    int leg_count, speed;
    [](typedef-making-new-types.html#cb164-8)} animal;                         // <-- new name
    [](typedef-making-new-types.html#cb164-9)
    [](typedef-making-new-types.html#cb164-10)struct animal y;  // This works
    [](typedef-making-new-types.html#cb164-11)animal z;         // This also works because "animal" is an alias

That’s exactly the same as the previous example, just more concise.

But that’s not all! There’s another common shortcut that you might see in code using what are called _anonymous structures_[ 83](function-specifiers-alignment-specifiersoperators.html#fn83). It turns out you don’t actually need to name the structure in a variety of places, and with `typedef` is one of them.

Let’s do the same example with an anonymous structure:
    
    
    [](typedef-making-new-types.html#cb165-1)//  Anonymous struct! It has no name!
    [](typedef-making-new-types.html#cb165-2)//         |
    [](typedef-making-new-types.html#cb165-3)//         v
    [](typedef-making-new-types.html#cb165-4)//      |----|
    [](typedef-making-new-types.html#cb165-5)typedef struct {
    [](typedef-making-new-types.html#cb165-6)    char *name;
    [](typedef-making-new-types.html#cb165-7)    int leg_count, speed;
    [](typedef-making-new-types.html#cb165-8)} animal;                         // <-- new name
    [](typedef-making-new-types.html#cb165-9)
    [](typedef-making-new-types.html#cb165-10)//struct animal y;  // ERROR: this no longer works--no such struct!
    [](typedef-making-new-types.html#cb165-11)animal z;           // This works because "animal" is an alias

As another example, we might find something like this:
    
    
    [](typedef-making-new-types.html#cb166-1)typedef struct {
    [](typedef-making-new-types.html#cb166-2)    int x, y;
    [](typedef-making-new-types.html#cb166-3)} point;
    [](typedef-making-new-types.html#cb166-4)
    [](typedef-making-new-types.html#cb166-5)point p = {.x=20, .y=40};
    [](typedef-making-new-types.html#cb166-6)
    [](typedef-making-new-types.html#cb166-7)printf("%d, %d\n", p.x, p.y);  // 20, 40

### 10.2.2 `typedef` and Other Types

It’s not that using `typedef` with a simple type like `int` is completely useless… it helps you abstract the types to make it easier to change them later.

For example, if you have `float` all over your code in 100 zillion places, it’s going to be painful to change them all to `double` if you find you have to do that later for some reason.

But if you prepared a little with:
    
    
    [](typedef-making-new-types.html#cb167-1)typedef float app_float;
    [](typedef-making-new-types.html#cb167-2)
    [](typedef-making-new-types.html#cb167-3)// and
    [](typedef-making-new-types.html#cb167-4)
    [](typedef-making-new-types.html#cb167-5)app_float f1, f2, f3;

Then if later you want to change to another type, like `long double`, you just need to change the `typedef`:
    
    
    [](typedef-making-new-types.html#cb168-1)//        voila!
    [](typedef-making-new-types.html#cb168-2)//      |---------|
    [](typedef-making-new-types.html#cb168-3)typedef long double app_float;
    [](typedef-making-new-types.html#cb168-4)
    [](typedef-making-new-types.html#cb168-5)// and no need to change this line:
    [](typedef-making-new-types.html#cb168-6)
    [](typedef-making-new-types.html#cb168-7)app_float f1, f2, f3;  // Now these are all long doubles

### 10.2.3 `typedef` and Pointers

You can make a type that is a pointer.
    
    
    [](typedef-making-new-types.html#cb169-1)typedef int *intptr;
    [](typedef-making-new-types.html#cb169-2)
    [](typedef-making-new-types.html#cb169-3)int a = 10;
    [](typedef-making-new-types.html#cb169-4)intptr x = &a;  // "intptr" is type "int*"

I really don’t like this practice. It hides the fact that `x` is a pointer type because you don’t see a `*` in the declaration.

IMHO, it’s better to explicitly show that you’re declaring a pointer type so that other devs can clearly see it and don’t mistake `x` for having a non-pointer type.

But at last count, say, 832,007 people had a different opinion. 

### 10.2.4 `typedef` and Capitalization

I’ve seen all kinds of capitalization on `typedef`.
    
    
    [](typedef-making-new-types.html#cb170-1)typedef struct {
    [](typedef-making-new-types.html#cb170-2)    int x, y;
    [](typedef-making-new-types.html#cb170-3)} my_point;          // lower snake case
    [](typedef-making-new-types.html#cb170-4)
    [](typedef-making-new-types.html#cb170-5)typedef struct {
    [](typedef-making-new-types.html#cb170-6)    int x, y;
    [](typedef-making-new-types.html#cb170-7)} MyPoint;          // CamelCase
    [](typedef-making-new-types.html#cb170-8)
    [](typedef-making-new-types.html#cb170-9)typedef struct {
    [](typedef-making-new-types.html#cb170-10)    int x, y;
    [](typedef-making-new-types.html#cb170-11)} Mypoint;          // Leading uppercase
    [](typedef-making-new-types.html#cb170-12)
    [](typedef-making-new-types.html#cb170-13)typedef struct {
    [](typedef-making-new-types.html#cb170-14)    int x, y;
    [](typedef-making-new-types.html#cb170-15)} MY_POINT;          // UPPER SNAKE CASE

The C11 specification doesn’t dictate one way or another, and shows examples in all uppercase and all lowercase.

K&R2 uses leading uppercase predominantly, but show some examples in uppercase and snake case (with `_t`).

If you have a style guide in use, stick with it. If you don’t, grab one and stick with it.

## 10.3 Arrays and `typedef`

The syntax is a little weird, and this is rarely seen in my experience, but you can `typedef` an array of some number of items.
    
    
    [](typedef-making-new-types.html#cb171-1)// Make type five_ints an array of 5 ints
    [](typedef-making-new-types.html#cb171-2)typedef int five_ints[5];
    [](typedef-making-new-types.html#cb171-3)
    [](typedef-making-new-types.html#cb171-4)five_ints x = {11, 22, 33, 44, 55};

I don’t like it because it hides the array nature of the variable, but it’s possible to do. 

* * *

[Prev](file-inputoutput.html) | [Contents](index.html) | [Next](pointers2.html)
