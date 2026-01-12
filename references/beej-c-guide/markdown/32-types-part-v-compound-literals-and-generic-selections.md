[Prev](goto.html) | [Contents](index.html) | [Next](arrays-part-ii.html)

* * *

# 32 Types Part V: Compound Literals and Generic Selections

This is the final chapter for types! We’re going to talk about two things:

  * How to have “anonymous” unnamed objects and how that’s useful.
  * How to generate type-dependent code.



They’re not particularly related, but don’t really each warrant their own chapters. So I crammed them in here like a rebel!

## 32.1 Compound Literals

This is a neat feature of the language that allows you to create an object of some type on the fly without ever assigning it to a variable. You can make simple types, arrays, `struct`s, you name it.

One of the main uses for this is passing complex arguments to functions when you don’t want to make a temporary variable to hold the value.

The way you create a compound literal is to put the type name in parentheses, and then put an initializer list after. For example, an unnamed array of `int`s, might look like this:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb634-1)(int []){1,2,3,4}

Now, that line of code doesn’t do anything on its own. It creates an unnamed array of 4 `int`s, and then throws them away without using them.

We could use a pointer to store a reference to the array…
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb635-1)int *p = (int []){1 ,2 ,3 ,4};
    [](types-part-v-compound-literals-and-generic-selections.html#cb635-2)
    [](types-part-v-compound-literals-and-generic-selections.html#cb635-3)printf("%d\n", p[1]);  // 2

But that seems a little like a long-winded way to have an array. I mean, we could have just done this[179](function-specifiers-alignment-specifiersoperators.html#fn179):
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb636-1)int p[] = {1, 2, 3, 4};
    [](types-part-v-compound-literals-and-generic-selections.html#cb636-2)
    [](types-part-v-compound-literals-and-generic-selections.html#cb636-3)printf("%d\n", p[1]);  // 2

So let’s take a look at a more useful example.

### 32.1.1 Passing Unnamed Objects to Functions

Let’s say we have a function to sum an array of `int`s:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb637-1)int sum(int p[], int count)
    [](types-part-v-compound-literals-and-generic-selections.html#cb637-2){
    [](types-part-v-compound-literals-and-generic-selections.html#cb637-3)    int total = 0;
    [](types-part-v-compound-literals-and-generic-selections.html#cb637-4)
    [](types-part-v-compound-literals-and-generic-selections.html#cb637-5)    for (int i = 0; i < count; i++)
    [](types-part-v-compound-literals-and-generic-selections.html#cb637-6)        total += p[i];
    [](types-part-v-compound-literals-and-generic-selections.html#cb637-7)
    [](types-part-v-compound-literals-and-generic-selections.html#cb637-8)    return total;
    [](types-part-v-compound-literals-and-generic-selections.html#cb637-9)}

If we wanted to call it, we’d normally have to do something like this, declaring an array and storing values in it to pass to the function:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb638-1)int a[] = {1, 2, 3, 4};
    [](types-part-v-compound-literals-and-generic-selections.html#cb638-2)
    [](types-part-v-compound-literals-and-generic-selections.html#cb638-3)int s = sum(a, 4);

But unnamed objects give us a way to skip the variable by passing it directly in (parameter names listed above). Check it out—we’re going to replace the variable `a` with an unnamed array that we pass in as the first argument:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb639-1)//                   p[]         count
    [](types-part-v-compound-literals-and-generic-selections.html#cb639-2)//           |-----------------|  |
    [](types-part-v-compound-literals-and-generic-selections.html#cb639-3)int s = sum((int []){1, 2, 3, 4}, 4);

Pretty slick!

### 32.1.2 Unnamed `struct`s

We can do something similar with `struct`s.

First, let’s do things without unnamed objects. We’ll define a `struct` to hold some `x`/`y` coordinates. Then we’ll define one, passing in values into its initializer. Finally, we’ll pass it to a function to print the values:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-1)#include <stdio.h>
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-2)
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-3)struct coord {
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-4)    int x, y;
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-5)};
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-6)
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-7)void print_coord(struct coord c)
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-8){
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-9)    printf("%d, %d\n", c.x, c.y);
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-10)}
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-11)
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-12)int main(void)
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-13){
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-14)    struct coord t = {.x=10, .y=20};
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-15)
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-16)    print_coord(t);   // prints "10, 20"
    [](types-part-v-compound-literals-and-generic-selections.html#cb640-17)}

Straightforward enough?

Let’s modify it to use an unnamed object instead of the variable `t` we’re passing to `print_coord()`.

We’ll just take `t` out of there and replace it with an unnamed `struct`:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb641-7)    //struct coord t = {.x=10, .y=20};
    [](types-part-v-compound-literals-and-generic-selections.html#cb641-8)
    [](types-part-v-compound-literals-and-generic-selections.html#cb641-9)    print_coord((struct coord){.x=10, .y=20});   // prints "10, 20"

Still works!

### 32.1.3 Pointers to Unnamed Objects

You might have noticed in the last example that even through we were using a `struct`, we were passing a copy of the `struct` to `print_coord()` as opposed to passing a pointer to the `struct`.

Turns out, we can just take the address of an unnamed object with `&` like always.

This is because, in general, if an operator would have worked on a variable of that type, you can use that operator on an unnamed object of that type.

Let’s modify the above code so that we pass a pointer to an unnamed object
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-1)#include <stdio.h>
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-2)
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-3)struct coord {
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-4)    int x, y;
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-5)};
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-6)
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-7)void print_coord(struct coord *c)
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-8){
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-9)    printf("%d, %d\n", c->x, c->y);
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-10)}
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-11)
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-12)int main(void)
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-13){
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-14)    //     Note the &
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-15)    //          |
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-16)    print_coord(&(struct coord){.x=10, .y=20});   // prints "10, 20"
    [](types-part-v-compound-literals-and-generic-selections.html#cb642-17)}

Additionally, this can be a nice way to pass even pointers to simple objects:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb643-1)// Pass a pointer to an int with value 3490
    [](types-part-v-compound-literals-and-generic-selections.html#cb643-2)foo(&(int){3490});

Easy as that.

### 32.1.4 Unnamed Objects and Scope

The lifetime of an unnamed object ends at the end of its scope. The biggest way this could bite you is if you make a new unnamed object, get a pointer to it, and then leave the object’s scope. In that case, the pointer will refer to a dead object.

So this is undefined behavior:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb644-1)int *p;
    [](types-part-v-compound-literals-and-generic-selections.html#cb644-2)
    [](types-part-v-compound-literals-and-generic-selections.html#cb644-3){
    [](types-part-v-compound-literals-and-generic-selections.html#cb644-4)    p = &(int){10};
    [](types-part-v-compound-literals-and-generic-selections.html#cb644-5)}
    [](types-part-v-compound-literals-and-generic-selections.html#cb644-6)
    [](types-part-v-compound-literals-and-generic-selections.html#cb644-7)printf("%d\n", *p);  // INVALID: The (int){10} fell out of scope

Likewise, you can’t return a pointer to an unnamed object from a function. The object is deallocated when it falls out of scope:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb645-1)#include <stdio.h>
    [](types-part-v-compound-literals-and-generic-selections.html#cb645-2)
    [](types-part-v-compound-literals-and-generic-selections.html#cb645-3)int *get3490(void)
    [](types-part-v-compound-literals-and-generic-selections.html#cb645-4){
    [](types-part-v-compound-literals-and-generic-selections.html#cb645-5)    // Don't do this
    [](types-part-v-compound-literals-and-generic-selections.html#cb645-6)    return &(int){3490};
    [](types-part-v-compound-literals-and-generic-selections.html#cb645-7)}
    [](types-part-v-compound-literals-and-generic-selections.html#cb645-8)
    [](types-part-v-compound-literals-and-generic-selections.html#cb645-9)int main(void)
    [](types-part-v-compound-literals-and-generic-selections.html#cb645-10){
    [](types-part-v-compound-literals-and-generic-selections.html#cb645-11)    printf("%d\n", *get3490());  // INVALID: (int){3490} fell out of scope
    [](types-part-v-compound-literals-and-generic-selections.html#cb645-12)}

Just think of their scope like that of an ordinary local variable. You can’t return a pointer to a local variable, either.

### 32.1.5 Silly Unnamed Object Example

You can put any type in there and make an unnamed object.

For example, these are effectively equivalent:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb646-1)int x = 3490;
    [](types-part-v-compound-literals-and-generic-selections.html#cb646-2)
    [](types-part-v-compound-literals-and-generic-selections.html#cb646-3)printf("%d\n", x);               // 3490 (variable)
    [](types-part-v-compound-literals-and-generic-selections.html#cb646-4)printf("%d\n", 3490);            // 3490 (constant)
    [](types-part-v-compound-literals-and-generic-selections.html#cb646-5)printf("%d\n", (int){3490});     // 3490 (unnamed object)

That last one is unnamed, but it’s silly. Might as well do the simple one on the line before.

But hopefully that provides a little more clarity on the syntax.

## 32.2 Generic Selections

This is an expression that allows you to select different pieces of code depending on the _type_ of the first argument to the expression.

We’ll look at an example in just a second, but it’s important to know this is processed at compile time, _not at runtime_. There’s no runtime analysis going on here.

The expression begins with `_Generic`, works kinda like a `switch`, and it takes at least two arguments.

The first argument is an expression (or variable[180](function-specifiers-alignment-specifiersoperators.html#fn180)) that has a _type_. All expressions have a type. The remaining arguments to `_Generic` are the cases of what to substitute in for the result of the expression if the first argument is that type.

Wat?

Let’s try it out and see.
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-1)#include <stdio.h>
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-2)
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-3)int main(void)
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-4){
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-5)    int i;
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-6)    float f;
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-7)    char c;
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-8)
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-9)    char *s = _Generic(i,
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-10)                    int: "that variable is an int",
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-11)                    float: "that variable is a float",
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-12)                    default: "that variable is some type"
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-13)                );
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-14)
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-15)    printf("%s\n", s);
    [](types-part-v-compound-literals-and-generic-selections.html#cb647-16)}

Check out the `_Generic` expression starting on line 9.

When the compiler sees it, it looks at the type of the first argument. (In this example, the type of the variable `i`.) It then looks through the cases for something of that type. And then it substitutes the argument in place of the entire `_Generic` expression.

In this case, `i` is an `int`, so it matches that case. Then the string is substituted in for the expression. So the line turns into this when the compiler sees it:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb648-1)    char *s = "that variable is an int";

If the compiler can’t find a type match in the `_Generic`, it looks for the optional `default` case and uses that.

If it can’t find a type match and there’s no `default`, you’ll get a compile error. The first expression **must** match one of the types or `default`.

Because it’s inconvenient to write `_Generic` over and over, it’s often used to make the body of a macro that can be easily repeatedly reused.

Let’s make a macro `TYPESTR(x)` that takes an argument and returns a string with the type of the argument.

So `TYPESTR(1)` will return the string `"int"`, for example.

Here we go:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-1)#include <stdio.h>
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-2)
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-3)#define TYPESTR(x) _Generic((x), \
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-4)                        int: "int", \
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-5)                        long: "long", \
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-6)                        float: "float", \
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-7)                        double: "double", \
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-8)                        default: "something else")
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-9)
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-10)int main(void)
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-11){
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-12)    int i;
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-13)    long l;
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-14)    float f;
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-15)    double d;
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-16)    char c;
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-17)
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-18)    printf("i is type %s\n", TYPESTR(i));
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-19)    printf("l is type %s\n", TYPESTR(l));
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-20)    printf("f is type %s\n", TYPESTR(f));
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-21)    printf("d is type %s\n", TYPESTR(d));
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-22)    printf("c is type %s\n", TYPESTR(c));
    [](types-part-v-compound-literals-and-generic-selections.html#cb649-23)}

This outputs:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb650-1)i is type int
    [](types-part-v-compound-literals-and-generic-selections.html#cb650-2)l is type long
    [](types-part-v-compound-literals-and-generic-selections.html#cb650-3)f is type float
    [](types-part-v-compound-literals-and-generic-selections.html#cb650-4)d is type double
    [](types-part-v-compound-literals-and-generic-selections.html#cb650-5)c is type something else

Which should be no surprise, because, like we said, that code in `main()` is replaced with the following when it is compiled:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb651-1)    printf("i is type %s\n", "int");
    [](types-part-v-compound-literals-and-generic-selections.html#cb651-2)    printf("l is type %s\n", "long");
    [](types-part-v-compound-literals-and-generic-selections.html#cb651-3)    printf("f is type %s\n", "float");
    [](types-part-v-compound-literals-and-generic-selections.html#cb651-4)    printf("d is type %s\n", "double");
    [](types-part-v-compound-literals-and-generic-selections.html#cb651-5)    printf("c is type %s\n", "something else");

And that’s exactly the output we see.

Let’s do one more. I’ve included some macros here so that when you run:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb652-1)int i = 10;
    [](types-part-v-compound-literals-and-generic-selections.html#cb652-2)char *s = "Foo!";
    [](types-part-v-compound-literals-and-generic-selections.html#cb652-3)
    [](types-part-v-compound-literals-and-generic-selections.html#cb652-4)PRINT_VAL(i);
    [](types-part-v-compound-literals-and-generic-selections.html#cb652-5)PRINT_VAL(s);

you get the output:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb653-1)i = 10
    [](types-part-v-compound-literals-and-generic-selections.html#cb653-2)s = Foo!

We’ll have to make use of some macro magic to do that.
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-1)#include <stdio.h>
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-2)#include <string.h>
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-3)
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-4)// Macro that gives back a format specifier for a type
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-5)#define FMTSPEC(x) _Generic((x), \
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-6)                        int: "%d", \
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-7)                        long: "%ld", \
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-8)                        float: "%f", \
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-9)                        double: "%f", \
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-10)                        char *: "%s")
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-11)                        // TODO: add more types
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-12)                        
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-13)// Macro that prints a variable in the form "name = value"
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-14)#define PRINT_VAL(x) do { \
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-15)    char fmt[512]; \
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-16)    snprintf(fmt, sizeof fmt, #x " = %s\n", FMTSPEC(x)); \
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-17)    printf(fmt, (x)); \
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-18)} while(0)
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-19)
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-20)int main(void)
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-21){
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-22)    int i = 10;
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-23)    float f = 3.14159;
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-24)    char *s = "Hello, world!";
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-25)
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-26)    PRINT_VAL(i);
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-27)    PRINT_VAL(f);
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-28)    PRINT_VAL(s);
    [](types-part-v-compound-literals-and-generic-selections.html#cb654-29)}

for the output:
    
    
    [](types-part-v-compound-literals-and-generic-selections.html#cb655-1)i = 10
    [](types-part-v-compound-literals-and-generic-selections.html#cb655-2)f = 3.141590
    [](types-part-v-compound-literals-and-generic-selections.html#cb655-3)s = Hello, world!

We could have crammed that all in one big macro, but I broke it into two to prevent eye bleeding.

* * *

[Prev](goto.html) | [Contents](index.html) | [Next](arrays-part-ii.html)
