[Prev](enumerated-types-enum.html) | [Contents](index.html) | [Next](bitwise-operations.html)

* * *

# 23 Pointers III: Pointers to Pointers and More

Here’s where we cover some intermediate and advanced pointer usage. If you don’t have pointers down well, review the previous chapters on [pointers](pointers.html#pointers) and [pointer arithmetic](pointers2.html#pointers2) before starting on this stuff.

## 23.1 Pointers to Pointers

If you can have a pointer to a variable, and a variable can be a pointer, can you have a pointer to a variable that it itself a pointer?

Yes! This is a pointer to a pointer, and it’s held in variable of type pointer-pointer.

Before we tear into that, I want to try for a _gut feel_ for how pointers to pointers work.

Remember that a pointer is just a number. It’s a number that represents an index in computer memory, typically one that holds a value we’re interested in for some reason.

That pointer, which is a number, has to be stored somewhere. And that place is memory, just like everything else[141](function-specifiers-alignment-specifiersoperators.html#fn141).

But because it’s stored in memory, it must have an index it’s stored at, right? The pointer must have an index in memory where it is stored. And that index is a number. It’s the address of the pointer. It’s a pointer to the pointer.

Let’s start with a regular pointer to an `int`, back from the earlier chapters:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb504-1)#include <stdio.h>
    [](pointers-iii-pointers-to-pointers-and-more.html#cb504-2)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb504-3)int main(void)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb504-4){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb504-5)    int x = 3490;  // Type: int
    [](pointers-iii-pointers-to-pointers-and-more.html#cb504-6)    int *p = &x;   // Type: pointer to an int
    [](pointers-iii-pointers-to-pointers-and-more.html#cb504-7)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb504-8)    printf("%d\n", *p);  // 3490
    [](pointers-iii-pointers-to-pointers-and-more.html#cb504-9)}

Straightforward enough, right? We have two types represented: `int` and `int*`, and we set up `p` to point to `x`. Then we can dereference `p` on line 8 and print out the value `3490`.

But, like we said, we can have a pointer to any variable… so does that mean we can have a pointer to `p`?

In other words, what type is this expression?
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb505-1)int x = 3490;  // Type: int
    [](pointers-iii-pointers-to-pointers-and-more.html#cb505-2)int *p = &x;   // Type: pointer to an int
    [](pointers-iii-pointers-to-pointers-and-more.html#cb505-3)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb505-4)&p  // <-- What type is the address of p? AKA a pointer to p?

If `x` is an `int`, then `&x` is a pointer to an `int` that we’ve stored in `p` which is type `int*`. Follow? (Repeat this paragraph until you do!)

And therefore `&p` is a pointer to an `int*`, AKA a “pointer to a pointer to an `int`”. AKA “`int`-pointer-pointer”.

Got it? (Repeat the previous paragraph until you do!)

We write this type with two asterisks: `int **`. Let’s see it in action.
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb506-1)#include <stdio.h>
    [](pointers-iii-pointers-to-pointers-and-more.html#cb506-2)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb506-3)int main(void)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb506-4){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb506-5)    int x = 3490;  // Type: int
    [](pointers-iii-pointers-to-pointers-and-more.html#cb506-6)    int *p = &x;   // Type: pointer to an int
    [](pointers-iii-pointers-to-pointers-and-more.html#cb506-7)    int **q = &p;  // Type: pointer to pointer to int
    [](pointers-iii-pointers-to-pointers-and-more.html#cb506-8)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb506-9)    printf("%d %d\n", *p, **q);  // 3490 3490
    [](pointers-iii-pointers-to-pointers-and-more.html#cb506-10)}

Let’s make up some pretend addresses for the above values as examples and see what these three variables might look like in memory. The address values, below are just made up by me for example purposes:

Variable | Stored at Address | Value Stored There  
---|---|---  
`x` | `28350` | `3490`—the value from the code  
`p` | `29122` | `28350`—the address of `x`!  
`q` | `30840` | `29122`—the address of `p`!  
  
Indeed, let’s try it for real on my computer[142](function-specifiers-alignment-specifiersoperators.html#fn142) and print out the pointer values with `%p` and I’ll do the same table again with actual references (printed in hex).

Variable | Stored at Address | Value Stored There  
---|---|---  
`x` | `0x7ffd96a07b94` | `3490`—the value from the code  
`p` | `0x7ffd96a07b98` | `0x7ffd96a07b94`—the address of `x`!  
`q` | `0x7ffd96a07ba0` | `0x7ffd96a07b98`—the address of `p`!  
  
You can see those addresses are the same except the last byte, so just focus on those.

On my system, `int`s are 4 bytes, which is why we’re seeing the address go up by 4 from `x` to `p`[143](function-specifiers-alignment-specifiersoperators.html#fn143) and then goes up by 8 from `p` to `q`. On my system, all pointers are 8 bytes.

Does it matter if it’s an `int*` or an `int**`? Is one more bytes than the other? Nope! Remember that all pointers are addresses, that is indexes into memory. And on my machine you can represent an index with 8 bytes… doesn’t matter what’s stored at that index.

Now check out what we did there on line 9 of the previous example: we _double dereferenced_ `q` to get back to our `3490`.

This is the important bit about pointers and pointers to pointers:

  * You can get a pointer to anything with `&` (including to a pointer!)
  * You can get the thing a pointer points to with `*` (including a pointer!)



So you can think of `&` as being used to make pointers, and `*` being the inverse—it goes the opposite direction of `&`—to get to the thing pointed to.

In terms of type, each time you `&`, that adds another pointer level to the type.

If you have | Then you run | The result type is  
---|---|---  
`int x` | `&x` | `int *`  
`int *x` | `&x` | `int **`  
`int **x` | `&x` | `int ***`  
`int ***x` | `&x` | `int ****`  
  
And each time you use dereference (`*`), it does the opposite:

If you have | Then you run | The result type is  
---|---|---  
`int ****x` | `*x` | `int ***`  
`int ***x` | `*x` | `int **`  
`int **x` | `*x` | `int *`  
`int *x` | `*x` | `int`  
  
Note that you can use multiple `*`s in a row to quickly dereference, just like we saw in the example code with `**q`, above. Each one strips away one level of indirection.

If you have | Then you run | The result type is  
---|---|---  
`int ****x` | `***x` | `int *`  
`int ***x` | `**x` | `int *`  
`int **x` | `**x` | `int`  
  
In general, `&*E == E`[144](function-specifiers-alignment-specifiersoperators.html#fn144). The dereference “undoes” the address-of.

But `&` doesn’t work the same way—you can only do those one at a time, and have to store the result in an intermediate variable:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb507-1)int x = 3490;     // Type: int
    [](pointers-iii-pointers-to-pointers-and-more.html#cb507-2)int *p = &x;      // Type: int *, pointer to an int
    [](pointers-iii-pointers-to-pointers-and-more.html#cb507-3)int **q = &p;     // Type: int **, pointer to pointer to int
    [](pointers-iii-pointers-to-pointers-and-more.html#cb507-4)int ***r = &q;    // Type: int ***, pointer to pointer to pointer to int
    [](pointers-iii-pointers-to-pointers-and-more.html#cb507-5)int ****s = &r;   // Type: int ****, you get the idea
    [](pointers-iii-pointers-to-pointers-and-more.html#cb507-6)int *****t = &s;  // Type: int *****

### 23.1.1 Pointer Pointers and `const`

If you recall, declaring a pointer like this:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb508-1)int *const p;

means that you can’t modify `p`. Trying to `p++` would give you a compile-time error.

But how does that work with `int **` or `int ***`? Where does the `const` go, and what does it mean?

Let’s start with the simple bit. The `const` right next to the variable name refers to that variable. So if you want an `int***` that you can’t change, you can do this:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb509-1)int ***const p;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb509-2)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb509-3)p++;  // Not allowed

But here’s where things get a little weird.

What if we had this situation:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb510-1)int main(void)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb510-2){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb510-3)    int x = 3490;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb510-4)    int *const p = &x;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb510-5)    int **q = &p;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb510-6)}

When I build that, I get a warning:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb511-1)warning: initialization discards ‘const’ qualifier from pointer target type
    [](pointers-iii-pointers-to-pointers-and-more.html#cb511-2)    7 |     int **q = &p;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb511-3)      |               ^

What’s going on? The compiler is telling us here that we had a variable that was `const`, and we’re assigning its value into another variable that is not `const` in the same way. The “`const`ness” is discarded, which probably isn’t what we wanted to do.

The type of `p` is `int *const p`, and so `&p` is type `int *const *`. And we try to assign that into `q`.

But `q` is `int **`! A type with different `const`ness on the first `*`! So we get a warning that the `const` in `p`’s `int *const *` is being ignored and thrown away.

We can fix that by making sure `q`’s type is at least as `const` as `p`.
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb512-1)int x = 3490;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb512-2)int *const p = &x;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb512-3)int *const *q = &p;

And now we’re happy.

We could make `q` even more `const`. As it is, above, we’re saying, “`q` isn’t itself `const`, but the thing it points to is `const`.” But we could make them both `const`:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb513-1)int x = 3490;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb513-2)int *const p = &x;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb513-3)int *const *const q = &p;  // More const!

And that works, too. Now we can’t modify `q`, or the pointer `q` points to.

## 23.2 Multibyte Values

We kinda hinted at this in a variety of places earlier, but clearly not every value can be stored in a single byte of memory. Things take up multiple bytes of memory (assuming they’re not `char`s). You can tell how many bytes by using `sizeof`. And you can tell which address in memory is the _first_ byte of the object by using the standard `&` operator, which always returns the address of the first byte.

And here’s another fun fact! If you iterate over the bytes of any object, you get its _object representation_. Two things with the same object representation in memory are equal.

If you want to iterate over the object representation, you should do it with pointers to `unsigned char`.

Let’s make our own version of [`memcpy()`](https://beej.us/guide/bgclr/html/split/stringref.html#man-memcpy)[145](function-specifiers-alignment-specifiersoperators.html#fn145) that does exactly this:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-1)void *my_memcpy(void *dest, const void *src, size_t n)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-2){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-3)    // Make local variables for src and dest, but of type unsigned char
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-4)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-5)    const unsigned char *s = src;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-6)    unsigned char *d = dest;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-7)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-8)    while (n-- > 0)   // For the given number of bytes
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-9)        *d++ = *s++;  // Copy source byte to dest byte
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-10)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-11)    // Most copy functions return a pointer to the dest as a convenience
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-12)    // to the caller
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-13)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-14)    return dest;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb514-15)}

(There are some good examples of post-increment and post-decrement in there for you to study, as well.)

It’s important to note that the version, above, is probably less efficient than the one that comes with your system.

But you can pass pointers to anything into it, and it’ll copy those objects. Could be `int*`, `struct animal*`, or anything.

Let’s do another example that prints out the object representation bytes of a `struct` so we can see if there’s any padding in there and what values it has[146](function-specifiers-alignment-specifiersoperators.html#fn146).
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-1)#include <stdio.h>
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-2)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-3)struct foo {
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-4)    char a;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-5)    int b;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-6)};
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-7)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-8)int main(void)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-9){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-10)    struct foo x = {0x12, 0x12345678};
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-11)    unsigned char *p = (unsigned char *)&x;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-12)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-13)    for (size_t i = 0; i < sizeof x; i++) {
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-14)        printf("%02X\n", p[i]);
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-15)    }
    [](pointers-iii-pointers-to-pointers-and-more.html#cb515-16)}

What we have there is a `struct foo` that’s built in such a way that should encourage a compiler to inject padding bytes (though it doesn’t have to). And then we get an `unsigned char *` to the first byte of the `struct foo` variable `x`.

From there, all we need to know is the `sizeof x` and we can loop through that many bytes, printing out the values (in hex for ease).

Running this gives a bunch of numbers as output. I’ve annotated it below to identify where the values were stored:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb516-1)12  | x.a == 0x12
    [](pointers-iii-pointers-to-pointers-and-more.html#cb516-2)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb516-3)AB  |
    [](pointers-iii-pointers-to-pointers-and-more.html#cb516-4)BF  | padding bytes with "random" value
    [](pointers-iii-pointers-to-pointers-and-more.html#cb516-5)26  |
    [](pointers-iii-pointers-to-pointers-and-more.html#cb516-6)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb516-7)78  | x.b == 0x12345678
    [](pointers-iii-pointers-to-pointers-and-more.html#cb516-8)56  |
    [](pointers-iii-pointers-to-pointers-and-more.html#cb516-9)34  |
    [](pointers-iii-pointers-to-pointers-and-more.html#cb516-10)12  |

On all systems, `sizeof(char)` is 1, and we see that first byte at the top of the output holding the value `0x12` that we stored there.

Then we have some padding bytes—for me, these varied from run to run.

Finally, on my system, `sizeof(int)` is 4, and we can see those 4 bytes at the end. Notice how they’re the same bytes as are in the hex value `0x12345678`, but strangely in reverse order[147](function-specifiers-alignment-specifiersoperators.html#fn147).

So that’s a little peek under the hood at the bytes of a more complex entity in memory.

## 23.3 The `NULL` Pointer and Zero

These things can be used interchangeably:

  * `NULL`
  * `0`
  * `'\0'`
  * `(void *)0`



Personally, I always use `NULL` when I mean `NULL`, but you might see some other variants from time to time. Though `'\0'` (a byte with all bits set to zero) will also compare equal, it’s _weird_ to compare it to a pointer; you should compare `NULL` against the pointer. (Of course, lots of times in string processing, you’re comparing _the thing the pointer points to_ to `'\0'`, and that’s right.)

`0` is called the _null pointer constant_ , and, when compared to or assigned into another pointer, it is converted to a null pointer of the same type.

## 23.4 Pointers as Integers

You can cast pointers to integers and vice-versa (since a pointer is just an index into memory), but you probably only ever need to do this if you’re doing some low-level hardware stuff. The results of such machinations are implementation-defined, so they aren’t portable. And _weird things_ could happen.

C does make one guarantee, though: you can convert a pointer to a `uintptr_t` type and you’ll be able to convert it back to a pointer without losing any data.

`uintptr_t` is defined in `<stdint.h>`[148](function-specifiers-alignment-specifiersoperators.html#fn148).

Additionally, if you feel like being signed, you can use `intptr_t` to the same effect.

## 23.5 Casting Pointers to other Pointers

There’s only one safe pointer conversion:

  1. Converting to `intptr_t` or `uintptr_t`.
  2. Converting to and from `void*`.



TWO! Two safe pointer conversions.

  3. Converting to and from `char*` (or `signed char*`/`unsigned char*`).



THREE! Three safe conversions!

  4. Converting to and from a pointer to a `struct` and a pointer to its first member, and vice-versa.



FOUR! Four safe conversions!

If you cast to a pointer of another type and then access the object it points to, the behavior is undefined due to something called _strict aliasing_.

Plain old _aliasing_ refers to the ability to have more than one way to access the same object. The access points are aliases for each other.

_Strict aliasing_ says you are only allowed to access an object via pointers to _compatible types_ to that object.

For example, this is definitely allowed:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb517-1)int a = 1;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb517-2)int *p = &a;

`p` is a pointer to an `int`, and it points to a compatible type—namely `int`—so we’re golden.

But the following isn’t good because `int` and `float` are not compatible types:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb518-1)int a = 1;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb518-2)float *p = (float *)&a;

Here’s a demo program that does some aliasing. It takes a variable `v` of type `int32_t` and aliases it to a pointer to a `struct words`. That `struct` has two `int16_t`s in it. These types are incompatible, so we’re in violation of strict aliasing rules. The compiler will assume that these two pointers never point to the same object… but we’re making it so they do. Which is naughty of us.

Let’s see if we can break something.
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-1)#include <stdio.h>
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-2)#include <stdint.h>
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-3)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-4)struct words {
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-5)    int16_t v[2];
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-6)};
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-7)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-8)void fun(int32_t *pv, struct words *pw)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-9){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-10)    for (int i = 0; i < 5; i++) {
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-11)        (*pv)++;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-12)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-13)        // Print the 32-bit value and the 16-bit values:
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-14)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-15)        printf("%x, %x-%x\n", *pv, pw->v[1], pw->v[0]);
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-16)    }
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-17)}
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-18)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-19)int main(void)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-20){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-21)    int32_t v = 0x12345678;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-22)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-23)    struct words *pw = (struct words *)&v;  // Violates strict aliasing
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-24)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-25)    fun(&v, pw);
    [](pointers-iii-pointers-to-pointers-and-more.html#cb519-26)}

See how I pass in the two incompatible pointers to `fun()`? One of the types is `int32_t*` and the other is `struct words*`.

But they both point to the same object: the 32-bit value initialized to `0x12345678`.

So if we look at the fields in the `struct words`, we should see the two 16-bit halves of that number. Right?

And in the `fun()` loop, we increment the pointer to the `int32_t`. That’s it. But since the `struct` points to that same memory, it, too, should be updated to the same value.

So let’s run it and get this, with the 32-bit value on the left and the two 16-bit portions on the right. It should match[149](function-specifiers-alignment-specifiersoperators.html#fn149):
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb520-1)12345679, 1234-5679
    [](pointers-iii-pointers-to-pointers-and-more.html#cb520-2)1234567a, 1234-567a
    [](pointers-iii-pointers-to-pointers-and-more.html#cb520-3)1234567b, 1234-567b
    [](pointers-iii-pointers-to-pointers-and-more.html#cb520-4)1234567c, 1234-567c
    [](pointers-iii-pointers-to-pointers-and-more.html#cb520-5)1234567d, 1234-567d

and it does… _UNTIL TOMORROW!_

Let’s try it compiling GCC with `-O3` and `-fstrict-aliasing`:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb521-1)12345679, 1234-5678
    [](pointers-iii-pointers-to-pointers-and-more.html#cb521-2)1234567a, 1234-5679
    [](pointers-iii-pointers-to-pointers-and-more.html#cb521-3)1234567b, 1234-567a
    [](pointers-iii-pointers-to-pointers-and-more.html#cb521-4)1234567c, 1234-567b
    [](pointers-iii-pointers-to-pointers-and-more.html#cb521-5)1234567d, 1234-567c

They’re off by one! But they point to the same memory! How could this be? Answer: it’s undefined behavior to alias memory like that. _Anything is possible_ , except not in a good way.

If your code violates strict aliasing rules, whether it works or not depends on how someone decides to compile it. And that’s a bummer since that’s beyond your control. Unless you’re some kind of omnipotent deity.

Unlikely, sorry.

GCC can be forced to not use the strict aliasing rules with `-fno-strict-aliasing`. Compiling the demo program, above, with `-O3` and this flag causes the output to be as expected.

Lastly, _type punning_ is using pointers of different types to look at the same data. Before strict aliasing, this kind of things was fairly common:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb522-1)int a = 0x12345678;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb522-2)short b = *((short *)&a);   // Violates strict aliasing

If you want to do type punning (relatively) safely, see the section on [Unions and Type Punning](structs-ii-more-fun-with-structs.html#union-type-punning).

## 23.6 Pointer Differences

As you know from the section on pointer arithmetic, you can subtract one pointer from another[150](function-specifiers-alignment-specifiersoperators.html#fn150) to get the difference between them in count of array elements.

Now the _type of that difference_ is something that’s up to the implementation, so it could vary from system to system.

To be more portable, you can store the result in a variable of type `ptrdiff_t` defined in `<stddef.h>`.
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb523-1)int cats[100];
    [](pointers-iii-pointers-to-pointers-and-more.html#cb523-2)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb523-3)int *f = cats + 20;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb523-4)int *g = cats + 60;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb523-5)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb523-6)ptrdiff_t d = g - f;  // difference is 40

And you can print it by prefixing the integer format specifier with `t`:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb524-1)printf("%td\n", d);  // Print decimal: 40
    [](pointers-iii-pointers-to-pointers-and-more.html#cb524-2)printf("%tX\n", d);  // Print hex:     28

## 23.7 Pointers to Functions

Functions are just collections of machine instructions in memory, so there’s no reason we can’t get a pointer to the first instruction of the function.

And then call it.

This can be useful for passing a pointer to a function into another function as an argument. Then the second one could call whatever was passed in.

The tricky part with these, though, is that C needs to know the type of the variable that is the pointer to the function.

And it would really like to know all the details.

Like “this is a pointer to a function that takes two `int` arguments and returns `void`”.

How do you write all that down so you can declare a variable?

Well, it turns out it looks very much like a function prototype, except with some extra parentheses:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb525-1)// Declare p to be a pointer to a function.
    [](pointers-iii-pointers-to-pointers-and-more.html#cb525-2)// This function returns a float, and takes two ints as arguments.
    [](pointers-iii-pointers-to-pointers-and-more.html#cb525-3)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb525-4)float (*p)(int, int);

Also notice that you don’t have to give the parameters names. But you can if you want; they’re just ignored.
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb526-1)// Declare p to be a pointer to a function.
    [](pointers-iii-pointers-to-pointers-and-more.html#cb526-2)// This function returns a float, and takes two ints as arguments.
    [](pointers-iii-pointers-to-pointers-and-more.html#cb526-3)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb526-4)float (*p)(int a, int b);

So now that we know how to declare a variable, how do we know what to assign into it? How do we get the address of a function?

Turns out there’s a shortcut just like with getting a pointer to an array: you can just refer to the bare function name without parens. (You can put an `&` in front of this if you like, but it’s unnecessary and not idiomatic.)

Once you have a pointer to a function, you can call it just by adding parens and an argument list.

Let’s do a simple example where I effectively make an alias for a function by setting a pointer to it. Then we’ll call it.

This code prints out `3490`:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-1)#include <stdio.h>
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-2)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-3)void print_int(int n)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-4){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-5)    printf("%d\n", n);
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-6)}
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-7)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-8)int main(void)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-9){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-10)    // Assign p to point to print_int:
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-11)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-12)    void (*p)(int) = print_int;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-13)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-14)    p(3490);          // Call print_int via the pointer
    [](pointers-iii-pointers-to-pointers-and-more.html#cb527-15)}

Notice how the type of `p` represents the return value and parameter types of `print_int`. It has to, or else C will complain about incompatible pointer types.

One more example here shows how we might pass a pointer to a function as an argument to another function.

We’ll write a function that takes a couple integer arguments, plus a pointer to a function that operates on those two arguments. Then it prints the result.
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-1)#include <stdio.h>
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-2)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-3)int add(int a, int b)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-4){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-5)    return a + b;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-6)}
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-7)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-8)int mult(int a, int b)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-9){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-10)    return a * b;
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-11)}
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-12)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-13)void print_math(int (*op)(int, int), int x, int y)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-14){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-15)    int result = op(x, y);
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-16)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-17)    printf("%d\n", result);
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-18)}
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-19)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-20)int main(void)
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-21){
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-22)    print_math(add, 5, 7);   // 12
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-23)    print_math(mult, 5, 7);  // 35
    [](pointers-iii-pointers-to-pointers-and-more.html#cb528-24)}

Take a moment to digest that. The idea here is that we’re going to pass a pointer to a function to `print_math()`, and it’s going to call that function to do some math.

This way we can change the behavior of `print_math()` by passing another function into it. You can see we do that on lines 22-23 when we pass in pointers to functions `add` and `mult`, respectively.

Now, on line 13, I think we can all agree the function signature of `print_math()` is a sight to behold. And, if you can believe it, this one is actually pretty straight-forward compared to some things you can construct[151](function-specifiers-alignment-specifiersoperators.html#fn151).

But let’s digest it. Turns out there are only three parameters, but they’re a little hard to see:
    
    
    [](pointers-iii-pointers-to-pointers-and-more.html#cb529-1)//                      op             x      y
    [](pointers-iii-pointers-to-pointers-and-more.html#cb529-2)//              |-----------------|  |---|  |---|
    [](pointers-iii-pointers-to-pointers-and-more.html#cb529-3)void print_math(int (*op)(int, int), int x, int y)

The first, `op`, is a pointer to a function that takes two `int`s as arguments and returns an `int`. This matches the signatures for both `add()` and `mult()`.

The second and third, `x` and `y`, are just standard `int` parameters.

Slowly and deliberately let your eyes play over the signature while you identify the working parts. One thing that always stands out for me is the sequence `(*op)(`, the parens and the asterisk. That’s the giveaway it’s a pointer to a function.

Finally, jump back to the _Pointers II_ chapter for a pointer-to-function [example using the built-in `qsort()`](pointers2.html#qsort-example).

* * *

[Prev](enumerated-types-enum.html) | [Contents](index.html) | [Next](bitwise-operations.html)
