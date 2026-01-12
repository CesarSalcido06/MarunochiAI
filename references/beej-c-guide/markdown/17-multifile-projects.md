[Prev](types-iv-qualifiers-and-specifiers.html) | [Contents](index.html) | [Next](the-outside-environment.html)

* * *

# 17 Multifile Projects

So far we’ve been looking at toy programs that for the most part fit in a single file. But complex C programs are made up of many files that are all compiled and linked together into a single executable.

In this chapter we’ll check out some of the common patterns and practices for putting together larger projects.

## 17.1 Includes and Function Prototypes

A really common situation is that some of your functions are defined in one file, and you want to call them from another.

This actually works out of the box with a warning… let’s first try it and then look at the right way to fix the warning.

For these examples, we’ll put the filename as the first comment in the source.

To compile them, you’ll need to specify all the sources on the command line:
    
    
    [](multifile-projects.html#cb291-1)# output file   source files
    [](multifile-projects.html#cb291-2)#     v            v
    [](multifile-projects.html#cb291-3)#   |----| |---------|
    [](multifile-projects.html#cb291-4)gcc -o foo foo.c bar.c

In that examples, `foo.c` and `bar.c` get built into the executable named `foo`.

So let’s take a look at the source file `bar.c`:
    
    
    [](multifile-projects.html#cb292-1)// File bar.c
    [](multifile-projects.html#cb292-2)
    [](multifile-projects.html#cb292-3)int add(int x, int y)
    [](multifile-projects.html#cb292-4){
    [](multifile-projects.html#cb292-5)    return x + y;
    [](multifile-projects.html#cb292-6)}

And the file `foo.c` with main in it:
    
    
    [](multifile-projects.html#cb293-1)// File foo.c
    [](multifile-projects.html#cb293-2)
    [](multifile-projects.html#cb293-3)#include <stdio.h>
    [](multifile-projects.html#cb293-4)
    [](multifile-projects.html#cb293-5)int main(void)
    [](multifile-projects.html#cb293-6){
    [](multifile-projects.html#cb293-7)    printf("%d\n", add(2, 3));  // 5!
    [](multifile-projects.html#cb293-8)}

See how from `main()` we call `add()`—but `add()` is in a completely different source file! It’s in `bar.c`, while the call to it is in `foo.c`!

If we build this with:
    
    
    [](multifile-projects.html#cb294-1)gcc -o foo foo.c bar.c

we get this error:
    
    
    [](multifile-projects.html#cb295-1)error: implicit declaration of function 'add' is invalid in C99

(Or you might get a warning. Which you should not ignore. Never ignore warnings in C; address them all.)

If you recall from the [section on prototypes](functions.html#prototypes), implicit declarations are banned in modern C and there’s no legitimate reason to introduce them into new code. We should fix it.

What `implicit declaration` means is that we’re using a function, namely `add()` in this case, without letting C know anything about it ahead of time. C wants to know what it returns, what types it takes as arguments, and things such as that.

We saw how to fix that earlier with a _function prototype_. Indeed, if we add one of those to `foo.c` before we make the call, everything works well:
    
    
    [](multifile-projects.html#cb296-1)// File foo.c
    [](multifile-projects.html#cb296-2)
    [](multifile-projects.html#cb296-3)#include <stdio.h>
    [](multifile-projects.html#cb296-4)
    [](multifile-projects.html#cb296-5)int add(int, int);  // Add the prototype
    [](multifile-projects.html#cb296-6)
    [](multifile-projects.html#cb296-7)int main(void)
    [](multifile-projects.html#cb296-8){
    [](multifile-projects.html#cb296-9)    printf("%d\n", add(2, 3));  // 5!
    [](multifile-projects.html#cb296-10)}

No more error!

But that’s a pain—needing to type in the prototype every time you want to use a function. I mean, we used `printf()` right there and didn’t need to type in a prototype; what gives?

If you remember from what back with `hello.c` at the beginning of the book, _we actually did include the prototype for`printf()`_! It’s in the file `stdio.h`! And we included that with `#include`!

Can we do the same with our `add()` function? Make a prototype for it and put it in a header file?

Sure!

Header files in C have a `.h` extension by default. And they often, but not always, have the same name as their corresponding `.c` file. So let’s make a `bar.h` file for our `bar.c` file, and we’ll stick the prototype in it:
    
    
    [](multifile-projects.html#cb297-1)// File bar.h
    [](multifile-projects.html#cb297-2)
    [](multifile-projects.html#cb297-3)int add(int, int);

And now let’s modify `foo.c` to include that file. Assuming it’s in the same directory, we include it inside double quotes (as opposed to angle brackets):
    
    
    [](multifile-projects.html#cb298-1)// File foo.c
    [](multifile-projects.html#cb298-2)
    [](multifile-projects.html#cb298-3)#include <stdio.h>
    [](multifile-projects.html#cb298-4)
    [](multifile-projects.html#cb298-5)#include "bar.h"  // Include from current directory
    [](multifile-projects.html#cb298-6)
    [](multifile-projects.html#cb298-7)int main(void)
    [](multifile-projects.html#cb298-8){
    [](multifile-projects.html#cb298-9)    printf("%d\n", add(2, 3));  // 5!
    [](multifile-projects.html#cb298-10)}

Notice how we don’t have the prototype in `foo.c` anymore—we included it from `bar.h`. Now _any_ file that wants that `add()` functionality can just `#include "bar.h"` to get it, and you don’t need to worry about typing in the function prototype.

As you might have guessed, `#include` literally includes the named file _right there_ in your source code, just as if you’d typed it in.

And building and running:
    
    
    [](multifile-projects.html#cb299-1)./foo
    [](multifile-projects.html#cb299-2)5

Indeed, we get the result of \\(2+3\\)! Yay!

But don’t crack open your drink of choice quite yet. We’re almost there! There’s just one more piece of boilerplate we have to add.

## 17.2 Dealing with Repeated Includes

It’s not uncommon that a header file will itself `#include` other headers needed for the functionality of its corresponding C files. I mean, why not?

And it could be that you have a header `#include`d multiple times from different places. Maybe that’s no problem, but maybe it would cause compiler errors. And we can’t control how many places `#include` it!

Even, worse we might get into a crazy situation where header `a.h` includes header `b.h`, and `b.h` includes `a.h`! It’s an `#include` infinite cycle!

Trying to build such a thing gives an error:
    
    
    [](multifile-projects.html#cb300-1)error: #include nested depth 200 exceeds maximum of 200

What we need to do is make it so that if a file gets included once, subsequent `#include`s for that file are ignored.

**The stuff that we’re about to do is so common that you should just automatically do it every time you make a header file!**

And the common way to do this is with a preprocessor variable that we set the first time we `#include` the file. And then for subsequent `#include`s, we first check to make sure that the variable isn’t defined.

For that variable name, it’s super common to take the name of the header file, like `bar.h`, make it uppercase, and replace the period with an underscore: `BAR_H`.

So put a check at the very, very top of the file where you see if it’s already been included, and effectively comment the whole thing out if it has.

(Don’t put a leading underscore (because a leading underscore followed by a capital letter is reserved) or a double leading underscore (because that’s also reserved.))
    
    
    [](multifile-projects.html#cb301-1)#ifndef BAR_H   // If BAR_H isn't defined...
    [](multifile-projects.html#cb301-2)#define BAR_H   // Define it (with no particular value)
    [](multifile-projects.html#cb301-3)
    [](multifile-projects.html#cb301-4)// File bar.h
    [](multifile-projects.html#cb301-5)
    [](multifile-projects.html#cb301-6)int add(int, int);
    [](multifile-projects.html#cb301-7)
    [](multifile-projects.html#cb301-8)#endif          // End of the #ifndef BAR_H

This will effectively cause the header file to be included only a single time, no matter how many places try to `#include` it.

## 17.3 `static` and `extern`

When it comes to multifile projects, you can make sure file-scope variables and functions are _not_ visible from other source files with the `static` keyword.

And you can refer to objects in other files with `extern`.

For more info, check out the sections in the book on the [`static`](types-iv-qualifiers-and-specifiers.html#static) and [`extern`](types-iv-qualifiers-and-specifiers.html#extern) storage-class specifiers.

## 17.4 Compiling with Object Files

This isn’t part of the spec, but it’s 99.999% common in the C world.

You can compile C files into an intermediate representation called _object files_. These are compiled machine code that hasn’t been put into an executable yet.

Object files in Windows have a `.OBJ` extension; in Unix-likes, they’re `.o`.

In gcc, we can build some like this, with the `-c` (compile only!) flag:
    
    
    [](multifile-projects.html#cb302-1)gcc -c foo.c     # produces foo.o
    [](multifile-projects.html#cb302-2)gcc -c bar.c     # produces bar.o

And then we can _link_ those together into a single executable:
    
    
    [](multifile-projects.html#cb303-1)gcc -o foo foo.o bar.o

_Voila_ , we’ve produced an executable `foo` from the two object files.

But you’re thinking, why bother? Can’t we just:
    
    
    [](multifile-projects.html#cb304-1)gcc -o foo foo.c bar.c

and kill two [boids](https://en.wikipedia.org/wiki/Boids)[119](function-specifiers-alignment-specifiersoperators.html#fn119) with one stone?

For little programs, that’s fine. I do it all the time.

But for larger programs, we can take advantage of the fact that compiling from source to object files is relatively slow, and linking together a bunch of object files is relatively fast.

This really shows with the `make` utility that only rebuilds sources that are newer than their outputs.

Let’s say you had a thousand C files. You could compile them all to object files to start (slowly) and then combine all those object files into an executable (fast).

Now say you modified just one of those C source files—here’s the magic: _you only have to rebuild that one object file for that source file_! And then you rebuild the executable (fast). All the other C files don’t have to be touched.

In other words, by only rebuilding the object files we need to, we cut down on compilation times radically. (Unless of course you’re doing a “clean” build, in which case all the object files have to be created.)

* * *

[Prev](types-iv-qualifiers-and-specifiers.html) | [Contents](index.html) | [Next](the-outside-environment.html)
