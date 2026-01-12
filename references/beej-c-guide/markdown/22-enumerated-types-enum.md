[Prev](characters-and-strings-ii.html) | [Contents](index.html) | [Next](pointers-iii-pointers-to-pointers-and-more.html)

* * *

# 22 Enumerated Types: `enum`

C offers us another way to have constant integer values by name: `enum`.

For example:
    
    
    [](enumerated-types-enum.html#cb494-1)enum {
    [](enumerated-types-enum.html#cb494-2)  ONE=1,
    [](enumerated-types-enum.html#cb494-3)  TWO=2
    [](enumerated-types-enum.html#cb494-4)};
    [](enumerated-types-enum.html#cb494-5)
    [](enumerated-types-enum.html#cb494-6)printf("%d %d", ONE, TWO);  // 1 2

In some ways, it can be better—or different—than using a `#define`. Key differences:

  * `enum`s can only be integer types.
  * `#define` can define anything at all.
  * `enum`s are often shown by their symbolic identifier name in a debugger.
  * `#define`d numbers just show as raw numbers which are harder to know the meaning of while debugging.



Since they’re integer types, they can be used any place integers can be used, including in array dimensions and `case` statements.

Let’s tear into this more.

## 22.1 Behavior of `enum`

### 22.1.1 Numbering

`enum`s are automatically numbered unless you override them.

They start at `0`, and autoincrement up from there, by default:
    
    
    [](enumerated-types-enum.html#cb495-1)enum {
    [](enumerated-types-enum.html#cb495-2)    SHEEP,  // Value is 0
    [](enumerated-types-enum.html#cb495-3)    WHEAT,  // Value is 1
    [](enumerated-types-enum.html#cb495-4)    WOOD,   // Value is 2
    [](enumerated-types-enum.html#cb495-5)    BRICK,  // Value is 3
    [](enumerated-types-enum.html#cb495-6)    ORE     // Value is 4
    [](enumerated-types-enum.html#cb495-7)};
    [](enumerated-types-enum.html#cb495-8)
    [](enumerated-types-enum.html#cb495-9)printf("%d %d\n", SHEEP, BRICK);  // 0 3

You can force particular integer values, as we saw earlier:
    
    
    [](enumerated-types-enum.html#cb496-1)enum {
    [](enumerated-types-enum.html#cb496-2)  X=2,
    [](enumerated-types-enum.html#cb496-3)  Y=18,
    [](enumerated-types-enum.html#cb496-4)  Z=-2
    [](enumerated-types-enum.html#cb496-5)};

Duplicates are not a problem:
    
    
    [](enumerated-types-enum.html#cb497-1)enum {
    [](enumerated-types-enum.html#cb497-2)  X=2,
    [](enumerated-types-enum.html#cb497-3)  Y=2,
    [](enumerated-types-enum.html#cb497-4)  Z=2
    [](enumerated-types-enum.html#cb497-5)};

if values are omitted, numbering continues counting in the positive direction from whichever value was last specified. For example:
    
    
    [](enumerated-types-enum.html#cb498-1)enum {
    [](enumerated-types-enum.html#cb498-2)  A,    // 0, default starting value
    [](enumerated-types-enum.html#cb498-3)  B,    // 1
    [](enumerated-types-enum.html#cb498-4)  C=4,  // 4, manually set
    [](enumerated-types-enum.html#cb498-5)  D,    // 5
    [](enumerated-types-enum.html#cb498-6)  E,    // 6
    [](enumerated-types-enum.html#cb498-7)  F=3,  // 3, manually set
    [](enumerated-types-enum.html#cb498-8)  G,    // 4
    [](enumerated-types-enum.html#cb498-9)  H     // 5
    [](enumerated-types-enum.html#cb498-10)}

### 22.1.2 Trailing Commas

This is perfectly fine, if that’s your style:
    
    
    [](enumerated-types-enum.html#cb499-1)enum {
    [](enumerated-types-enum.html#cb499-2)  X=2,
    [](enumerated-types-enum.html#cb499-3)  Y=18,
    [](enumerated-types-enum.html#cb499-4)  Z=-2,   // <-- Trailing comma
    [](enumerated-types-enum.html#cb499-5)};

It’s gotten more popular in languages of the recent decades so you might be pleased to see it.

### 22.1.3 Scope

`enum`s scope as you’d expect. If at file scope, the whole file can see it. If in a block, it’s local to that block.

It’s really common for `enum`s to be defined in header files so they can be `#include`d at file scope.

### 22.1.4 Style

As you’ve noticed, it’s common to declare the `enum` symbols in uppercase (with underscores).

This isn’t a requirement, but is a very, very common idiom.

## 22.2 Your `enum` is a Type

This is an important thing to know about `enum`: they’re a type, analogous to how a `struct` is a type.

You can give them a tag name so you can refer to the type later and declare variables of that type.

Now, since `enum`s are integer types, why not just use `int`?

In C, the best reason for this is code clarity–it’s a nice, typed way to describe your thinking in code. C (unlike C++) doesn’t actually enforce any values being in range for a particular `enum`.

Let’s do an example where we declare a variable `r` of type `enum resource` that can hold those values:
    
    
    [](enumerated-types-enum.html#cb500-1)// Named enum, type is "enum resource"
    [](enumerated-types-enum.html#cb500-2)
    [](enumerated-types-enum.html#cb500-3)enum resource {
    [](enumerated-types-enum.html#cb500-4)    SHEEP,
    [](enumerated-types-enum.html#cb500-5)    WHEAT,
    [](enumerated-types-enum.html#cb500-6)    WOOD,
    [](enumerated-types-enum.html#cb500-7)    BRICK,
    [](enumerated-types-enum.html#cb500-8)    ORE
    [](enumerated-types-enum.html#cb500-9)};
    [](enumerated-types-enum.html#cb500-10)
    [](enumerated-types-enum.html#cb500-11)// Declare a variable "r" of type "enum resource"
    [](enumerated-types-enum.html#cb500-12)
    [](enumerated-types-enum.html#cb500-13)enum resource r = BRICK;
    [](enumerated-types-enum.html#cb500-14)
    [](enumerated-types-enum.html#cb500-15)if (r == BRICK) {
    [](enumerated-types-enum.html#cb500-16)    printf("I'll trade you a brick for two sheep.\n");
    [](enumerated-types-enum.html#cb500-17)}

You can also `typedef` these, of course, though I personally don’t like to.
    
    
    [](enumerated-types-enum.html#cb501-1)typedef enum {
    [](enumerated-types-enum.html#cb501-2)    SHEEP,
    [](enumerated-types-enum.html#cb501-3)    WHEAT,
    [](enumerated-types-enum.html#cb501-4)    WOOD,
    [](enumerated-types-enum.html#cb501-5)    BRICK,
    [](enumerated-types-enum.html#cb501-6)    ORE
    [](enumerated-types-enum.html#cb501-7)} RESOURCE;
    [](enumerated-types-enum.html#cb501-8)
    [](enumerated-types-enum.html#cb501-9)RESOURCE r = BRICK;

Another shortcut that’s legal but rare is to declare variables when you declare the `enum`:
    
    
    [](enumerated-types-enum.html#cb502-1)// Declare an enum and some initialized variables of that type:
    [](enumerated-types-enum.html#cb502-2)
    [](enumerated-types-enum.html#cb502-3)enum {
    [](enumerated-types-enum.html#cb502-4)    SHEEP,
    [](enumerated-types-enum.html#cb502-5)    WHEAT,
    [](enumerated-types-enum.html#cb502-6)    WOOD,
    [](enumerated-types-enum.html#cb502-7)    BRICK,
    [](enumerated-types-enum.html#cb502-8)    ORE
    [](enumerated-types-enum.html#cb502-9)} r = BRICK, s = WOOD;

You can also give the `enum` a name so you can use it later, which is probably what you want to do in most cases:
    
    
    [](enumerated-types-enum.html#cb503-1)// Declare an enum and some initialized variables of that type:
    [](enumerated-types-enum.html#cb503-2)
    [](enumerated-types-enum.html#cb503-3)enum resource {   // <-- type is now "enum resource"
    [](enumerated-types-enum.html#cb503-4)    SHEEP,
    [](enumerated-types-enum.html#cb503-5)    WHEAT,
    [](enumerated-types-enum.html#cb503-6)    WOOD,
    [](enumerated-types-enum.html#cb503-7)    BRICK,
    [](enumerated-types-enum.html#cb503-8)    ORE
    [](enumerated-types-enum.html#cb503-9)} r = BRICK, s = WOOD;

In short, `enum`s are a great way to write nice, scoped, typed, clean code.

* * *

[Prev](characters-and-strings-ii.html) | [Contents](index.html) | [Next](pointers-iii-pointers-to-pointers-and-more.html)
