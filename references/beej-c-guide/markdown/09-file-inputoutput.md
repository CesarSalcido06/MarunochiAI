[Prev](structs.html) | [Contents](index.html) | [Next](typedef-making-new-types.html)

* * *

# 9 File Input/Output

We’ve already seen some examples of I/O with `printf()` for doing I/O at the console.

But we’ll push those concepts a little farther this chapter.

## 9.1 The `FILE*` Data Type

When we do any kind of I/O in C, we do so through a piece of data that you get in the form of a `FILE*` type. This `FILE*` holds all the information needed to communicate with the I/O subsystem about which file you have open, where you are in the file, and so on.

The spec refers to these as _streams_ , i.e. a stream of data from a file or from any source. I’m going to use “files” and “streams” interchangeably, but really you should think of a “file” as a special case of a “stream”. There are other ways to stream data into a program than just reading from a file.

We’ll see in a moment how to go from having a filename to getting an open `FILE*` for it, but first I want to mention three streams that are already open for you and ready for use.

`FILE*` name | Description  
---|---  
`stdin` | Standard Input, generally the keyboard by default  
`stdout` | Standard Output, generally the screen by default  
`stderr` | Standard Error, generally the screen by default, as well  
  
We’ve actually been using these implicitly already, it turns out. For example, these two calls are the same:
    
    
    [](file-inputoutput.html#cb139-1)printf("Hello, world!\n");
    [](file-inputoutput.html#cb139-2)fprintf(stdout, "Hello, world!\n");  // printf to a file

But more on that later.

Also you’ll notice that both `stdout` and `stderr` go to the screen. While this seems at first either like an oversight or redundancy, it actually isn’t. Typical operating systems allow you to _redirect_ the output of either of those into different files, and it can be convenient to be able to separate error messages from regular non-error output.

For example, in a POSIX shell (like sh, ksh, bash, zsh, etc.) on a Unix-like system, we could run a program and send just the non-error (`stdout`) output to one file, and all the error (`stderr`) output to another file.
    
    
    [](file-inputoutput.html#cb140-1)./foo > output.txt 2> errors.txt   # This command is Unix-specific

For this reason, you should send serious error messages to `stderr` instead of `stdout`. 

More on how to do that later. 

## 9.2 Reading Text Files

Streams are largely categorized two different ways: _text_ and _binary_.

Text streams are allowed to do significant translation of the data, most notably translations of newlines to their different representations[76](function-specifiers-alignment-specifiersoperators.html#fn76). Text files are logically a sequence of _lines_ separated by newlines. To be portable, your input data should always end with a newline.

But the general rule is that if you’re able to edit the file in a regular text editor, it’s a text file. Otherwise, it’s binary. More on binary later.

So let’s get to work—how do we open a file for reading, and pull data out of it?

Let’s create a file called `hello.txt` that has just this in it:
    
    
    [](file-inputoutput.html#cb141-1)Hello, world!

And let’s write a program to open the file, read a character out of it, and then close the file when we’re done. That’s the game plan!
    
    
    [](file-inputoutput.html#cb142-1)#include <stdio.h>
    [](file-inputoutput.html#cb142-2)
    [](file-inputoutput.html#cb142-3)int main(void)
    [](file-inputoutput.html#cb142-4){
    [](file-inputoutput.html#cb142-5)    FILE *fp;                      // Variable to represent open file
    [](file-inputoutput.html#cb142-6)
    [](file-inputoutput.html#cb142-7)    fp = fopen("hello.txt", "r");  // Open file for reading
    [](file-inputoutput.html#cb142-8)
    [](file-inputoutput.html#cb142-9)    int c = fgetc(fp);             // Read a single character
    [](file-inputoutput.html#cb142-10)    printf("%c\n", c);             // Print char to stdout
    [](file-inputoutput.html#cb142-11)
    [](file-inputoutput.html#cb142-12)    fclose(fp);                    // Close the file when done
    [](file-inputoutput.html#cb142-13)}

See how when we opened the file with `fopen()`, it returned the `FILE*` to us so we could use it later.

(I’m leaving it out for brevity, but `fopen()` will return `NULL` if something goes wrong, like file-not-found, so you should really error check it!)

Also notice the `"r"` that we passed in—this means “open a text stream for reading”. (There are various strings we can pass to `fopen()` with additional meaning, like writing, or appending, and so on.) 

After that, we used the `fgetc()` function to get a character from the stream. You might be wondering why I’ve made `c` an `int` instead of a `char`—hold that thought! 

Finally, we close the stream when we’re done with it. All streams are automatically closed when the program exits, but it’s good form and good housekeeping to explicitly close any files yourself when done with them. 

The `FILE*` keeps track of our position in the file. So subsequent calls to `fgetc()` would get the next character in the file, and then the next, until the end.

But that sounds like a pain. Let’s see if we can make it easier. 

## 9.3 End of File: `EOF`

There is a special character defined as a macro: `EOF`. This is what `fgetc()` will return when the end of the file has been reached and you’ve attempted to read another character.

How about I share that Fun Fact™, now. Turns out `EOF` is the reason why `fgetc()` and functions like it return an `int` instead of a `char`. `EOF` isn’t a character proper, and its value likely falls outside the range of `char`. Since `fgetc()` needs to be able to return any byte **and** `EOF`, it needs to be a wider type that can hold more values. so `int` it is. But unless you’re comparing the returned value against `EOF`, you can know, deep down, it’s a `char`.

All right! Back to reality! We can use this to read the whole file in a loop.
    
    
    [](file-inputoutput.html#cb143-1)#include <stdio.h>
    [](file-inputoutput.html#cb143-2)
    [](file-inputoutput.html#cb143-3)int main(void)
    [](file-inputoutput.html#cb143-4){
    [](file-inputoutput.html#cb143-5)    FILE *fp;
    [](file-inputoutput.html#cb143-6)    int c;
    [](file-inputoutput.html#cb143-7)
    [](file-inputoutput.html#cb143-8)    fp = fopen("hello.txt", "r");
    [](file-inputoutput.html#cb143-9)
    [](file-inputoutput.html#cb143-10)    while ((c = fgetc(fp)) != EOF)
    [](file-inputoutput.html#cb143-11)        printf("%c", c);
    [](file-inputoutput.html#cb143-12)
    [](file-inputoutput.html#cb143-13)    fclose(fp);
    [](file-inputoutput.html#cb143-14)}

(If line 10 is too weird, just break it down starting with the innermost-nested parens. The first thing we do is assign the result of `fgetc()` into `c`, and _then_ we compare _that_ against `EOF`. We’ve just crammed it into a single line. This might look hard to read, but study it—it’s idiomatic C.) 

And running this, we see:
    
    
    [](file-inputoutput.html#cb144-1)Hello, world!

But still, we’re operating a character at a time, and lots of text files make more sense at the line level. Let’s switch to that. 

### 9.3.1 Reading a Line at a Time

So how can we get an entire line at once? `fgets()` to the rescue! For arguments, it takes a pointer to a `char` buffer to hold bytes, a maximum number of bytes to read, and a `FILE*` to read from. It returns `NULL` on end-of-file or error. `fgets()` is even nice enough to NUL-terminate the string when its done[77](function-specifiers-alignment-specifiersoperators.html#fn77).

Let’s do a similar loop as before, except let’s have a multiline file and read it in a line at a time.

Here’s a file `quote.txt`:
    
    
    [](file-inputoutput.html#cb145-1)A wise man can learn more from
    [](file-inputoutput.html#cb145-2)a foolish question than a fool
    [](file-inputoutput.html#cb145-3)can learn from a wise answer.
    [](file-inputoutput.html#cb145-4)                  --Bruce Lee

And here’s some code that reads that file a line at a time and prints out a line number before each one:
    
    
    [](file-inputoutput.html#cb146-1)#include <stdio.h>
    [](file-inputoutput.html#cb146-2)
    [](file-inputoutput.html#cb146-3)int main(void)
    [](file-inputoutput.html#cb146-4){
    [](file-inputoutput.html#cb146-5)    FILE *fp;
    [](file-inputoutput.html#cb146-6)    char s[1024];  // Big enough for any line this program will encounter
    [](file-inputoutput.html#cb146-7)    int linecount = 0;
    [](file-inputoutput.html#cb146-8)
    [](file-inputoutput.html#cb146-9)    fp = fopen("quote.txt", "r");
    [](file-inputoutput.html#cb146-10)
    [](file-inputoutput.html#cb146-11)    while (fgets(s, sizeof s, fp) != NULL) 
    [](file-inputoutput.html#cb146-12)        printf("%d: %s", ++linecount, s);
    [](file-inputoutput.html#cb146-13)
    [](file-inputoutput.html#cb146-14)    fclose(fp);
    [](file-inputoutput.html#cb146-15)}

Which gives the output:
    
    
    [](file-inputoutput.html#cb147-1)1: A wise man can learn more from
    [](file-inputoutput.html#cb147-2)2: a foolish question than a fool
    [](file-inputoutput.html#cb147-3)3: can learn from a wise answer.
    [](file-inputoutput.html#cb147-4)4:                   --Bruce Lee

## 9.4 Formatted Input

You know how you can get formatted output with `printf()` (and, thus, `fprintf()` like we’ll see, below)?

You can do the same thing with `fscanf()`.

> Before we start, you should be advised that using `scanf()`-style functions can be hazardous with untrusted input. If you don’t specify field widths with your `%s`, you could overflow the buffer. Worse, invalid numeric conversion result in undefined behavior. The safe thing to do with untrusted input is to use `%s` with a field width, then use functions like `strtol()` or `strtod()` to do the conversions.

Let’s have a file with a series of data records in it. In this case, whales, with name, length in meters, and weight in tonnes. `whales.txt`:
    
    
    [](file-inputoutput.html#cb148-1)blue 29.9 173
    [](file-inputoutput.html#cb148-2)right 20.7 135
    [](file-inputoutput.html#cb148-3)gray 14.9 41
    [](file-inputoutput.html#cb148-4)humpback 16.0 30

Yes, we could read these with `fgets()` and then parse the string with `sscanf()` (and in that’s more resilient against corrupted files), but in this case, let’s just use `fscanf()` and pull it in directly.

The `fscanf()` function skips leading whitespace when reading, and returns `EOF` on end-of-file or error.
    
    
    [](file-inputoutput.html#cb149-1)#include <stdio.h>
    [](file-inputoutput.html#cb149-2)
    [](file-inputoutput.html#cb149-3)int main(void)
    [](file-inputoutput.html#cb149-4){
    [](file-inputoutput.html#cb149-5)    FILE *fp;
    [](file-inputoutput.html#cb149-6)    char name[1024];  // Big enough for any line this program will encounter
    [](file-inputoutput.html#cb149-7)    float length;
    [](file-inputoutput.html#cb149-8)    int mass;
    [](file-inputoutput.html#cb149-9)
    [](file-inputoutput.html#cb149-10)    fp = fopen("whales.txt", "r");
    [](file-inputoutput.html#cb149-11)
    [](file-inputoutput.html#cb149-12)    while (fscanf(fp, "%s %f %d", name, &length, &mass) != EOF)
    [](file-inputoutput.html#cb149-13)        printf("%s whale, %d tonnes, %.1f meters\n", name, mass, length);
    [](file-inputoutput.html#cb149-14)
    [](file-inputoutput.html#cb149-15)    fclose(fp);
    [](file-inputoutput.html#cb149-16)}

Which gives the result:
    
    
    [](file-inputoutput.html#cb150-1)blue whale, 173 tonnes, 29.9 meters
    [](file-inputoutput.html#cb150-2)right whale, 135 tonnes, 20.7 meters
    [](file-inputoutput.html#cb150-3)gray whale, 41 tonnes, 14.9 meters
    [](file-inputoutput.html#cb150-4)humpback whale, 30 tonnes, 16.0 meters

## 9.5 Writing Text Files

In much the same way we can use `fgetc()`, `fgets()`, and `fscanf()` to read text streams, we can use `fputc()`, `fputs()`, and `fprintf()` to write text streams.

To do so, we have to `fopen()` the file in write mode by passing `"w"` as the second argument. Opening an existing file in `"w"` mode will instantly truncate that file to 0 bytes for a full overwrite.

We’ll put together a simple program that outputs a file `output.txt` using a variety of output functions.
    
    
    [](file-inputoutput.html#cb151-1)#include <stdio.h>
    [](file-inputoutput.html#cb151-2)
    [](file-inputoutput.html#cb151-3)int main(void)
    [](file-inputoutput.html#cb151-4){
    [](file-inputoutput.html#cb151-5)    FILE *fp;
    [](file-inputoutput.html#cb151-6)    int x = 32;
    [](file-inputoutput.html#cb151-7)
    [](file-inputoutput.html#cb151-8)    fp = fopen("output.txt", "w");
    [](file-inputoutput.html#cb151-9)
    [](file-inputoutput.html#cb151-10)    fputc('B', fp);
    [](file-inputoutput.html#cb151-11)    fputc('\n', fp);   // newline
    [](file-inputoutput.html#cb151-12)    fprintf(fp, "x = %d\n", x);
    [](file-inputoutput.html#cb151-13)    fputs("Hello, world!\n", fp);
    [](file-inputoutput.html#cb151-14)
    [](file-inputoutput.html#cb151-15)    fclose(fp);
    [](file-inputoutput.html#cb151-16)}

And this produces a file, `output.txt`, with these contents:
    
    
    [](file-inputoutput.html#cb152-1)B
    [](file-inputoutput.html#cb152-2)x = 32
    [](file-inputoutput.html#cb152-3)Hello, world!

Fun fact: since `stdout` is a file, you could replace line 8 with:
    
    
    [](file-inputoutput.html#cb153-1)fp = stdout;

and the program would have outputted to the console instead of to a file. Try it! 

## 9.6 Binary File I/O

So far we’ve just been talking text files. But there’s that other beast we mentioned early on called _binary_ files, or binary streams.

These work very similarly to text files, except the I/O subsystem doesn’t perform any translations on the data like it might with a text file. With binary files, you get a raw stream of bytes, and that’s all.

The big difference in opening the file is that you have to add a `"b"` to the mode. That is, to read a binary file, open it in `"rb"` mode. To write a file, open it in `"wb"` mode.

Because it’s streams of bytes, and streams of bytes can contain NUL characters, and the NUL character is the end-of-string marker in C, it’s rare that people use the `fprintf()`-and-friends functions to operate on binary files.

Instead the most common functions are `fread()` and `fwrite()`. The functions read and write a specified number of bytes to the stream.

To demo, we’ll write a couple programs. One will write a sequence of byte values to disk all at once. And the second program will read a byte at a time and print them out[78](function-specifiers-alignment-specifiersoperators.html#fn78).
    
    
    [](file-inputoutput.html#cb154-1)#include <stdio.h>
    [](file-inputoutput.html#cb154-2)
    [](file-inputoutput.html#cb154-3)int main(void)
    [](file-inputoutput.html#cb154-4){
    [](file-inputoutput.html#cb154-5)    FILE *fp;
    [](file-inputoutput.html#cb154-6)    unsigned char bytes[6] = {5, 37, 0, 88, 255, 12};
    [](file-inputoutput.html#cb154-7)
    [](file-inputoutput.html#cb154-8)    fp = fopen("output.bin", "wb");  // wb mode for "write binary"!
    [](file-inputoutput.html#cb154-9)
    [](file-inputoutput.html#cb154-10)    // In the call to fwrite, the arguments are:
    [](file-inputoutput.html#cb154-11)    //
    [](file-inputoutput.html#cb154-12)    // * Pointer to data to write
    [](file-inputoutput.html#cb154-13)    // * Size of each "piece" of data
    [](file-inputoutput.html#cb154-14)    // * Count of each "piece" of data
    [](file-inputoutput.html#cb154-15)    // * FILE*
    [](file-inputoutput.html#cb154-16)
    [](file-inputoutput.html#cb154-17)    fwrite(bytes, sizeof(char), 6, fp);
    [](file-inputoutput.html#cb154-18)
    [](file-inputoutput.html#cb154-19)    fclose(fp);
    [](file-inputoutput.html#cb154-20)}

Those two middle arguments to `fwrite()` are pretty odd. But basically what we want to tell the function is, “We have items that are _this_ big, and we want to write _that_ many of them.” This makes it convenient if you have a record of a fixed length, and you have a bunch of them in an array. You can just tell it the size of one record and how many to write.

In the example above, we tell it each record is the size of a `char`, and we have 6 of them.

Running the program gives us a file `output.bin`, but opening it in a text editor doesn’t show anything friendly! It’s binary data—not text. And random binary data I just made up, at that!

If I run it through a [hex dump](https://en.wikipedia.org/wiki/Hex_dump)[79](function-specifiers-alignment-specifiersoperators.html#fn79) program, we can see the output as bytes:
    
    
    [](file-inputoutput.html#cb155-1)05 25 00 58 ff 0c

> Many Unix systems ship with a program called `hexdump` to do this. You can use it like this with the `-C` (“canonical”) switch to get nice output:
>     
>     
>     [](file-inputoutput.html#cb156-1)$ hexdump -C output.bin
>     [](file-inputoutput.html#cb156-2)00000000  05 25 00 58 ff 0c                              |.%.X..|
> 
> The `00000000` is the offset within the file that this line of output starts on. The `05 25 00 58 ff 0c` are the byte values (and this would be longer (up to 16 bytes per line) if there were more bytes in the file). And on the right between the pipe (`|`) symbols is `hexdump`’s best attempt to print out the characters that correspond to those bytes. It prints a period if the character is unprintable. In this case, since we’re just printing random binary data, this part of the output is just garbage. But if we’d printed an ASCII string to the file, we’d see that in there.

And those values in hex do match up to the values (in decimal) that we wrote out.

But now let’s try to read them back in with a different program. This one will open the file for binary reading (`"rb"` mode) and will read the bytes one at a time in a loop.

`fread()` has the neat feature where it returns the number of bytes read, or `0` on EOF. So we can loop until we see that, printing numbers as we go.
    
    
    [](file-inputoutput.html#cb157-1)#include <stdio.h>
    [](file-inputoutput.html#cb157-2)
    [](file-inputoutput.html#cb157-3)int main(void)
    [](file-inputoutput.html#cb157-4){
    [](file-inputoutput.html#cb157-5)    FILE *fp;
    [](file-inputoutput.html#cb157-6)    unsigned char c;
    [](file-inputoutput.html#cb157-7)
    [](file-inputoutput.html#cb157-8)    fp = fopen("output.bin", "rb"); // rb for "read binary"!
    [](file-inputoutput.html#cb157-9)
    [](file-inputoutput.html#cb157-10)    while (fread(&c, sizeof(char), 1, fp) > 0)
    [](file-inputoutput.html#cb157-11)        printf("%d\n", c);
    [](file-inputoutput.html#cb157-12)
    [](file-inputoutput.html#cb157-13)    fclose(fp);
    [](file-inputoutput.html#cb157-14)}

And, running it, we see our original numbers!
    
    
    [](file-inputoutput.html#cb158-1)5
    [](file-inputoutput.html#cb158-2)37
    [](file-inputoutput.html#cb158-3)0
    [](file-inputoutput.html#cb158-4)88
    [](file-inputoutput.html#cb158-5)255
    [](file-inputoutput.html#cb158-6)12

Woo hoo! 

### 9.6.1 `struct` and Number Caveats

As we saw in the `struct`s section, the compiler is free to add padding to a `struct` as it sees fit. And different compilers might do this differently. And the same compiler on different architectures could do it differently. And the same compiler on the same architectures could do it differently.

What I’m getting at is this: it’s not portable to just `fwrite()` an entire `struct` out to a file when you don’t know where the padding will end up. 

How do we fix this? Hold that thought—we’ll look at some ways to do this after looking at another related problem.

Numbers!

Turns out all architectures don’t represent numbers in memory the same way.

Let’s look at a simple `fwrite()` of a 2-byte number. We’ll write it in hex so each byte is clear. The most significant byte will have the value `0x12` and the least significant will have the value `0x34`.
    
    
    [](file-inputoutput.html#cb159-1)unsigned short v = 0x1234;  // Two bytes, 0x12 and 0x34
    [](file-inputoutput.html#cb159-2)
    [](file-inputoutput.html#cb159-3)fwrite(&v, sizeof v, 1, fp);

What ends up in the stream?

Well, it seems like it should be `0x12` followed by `0x34`, right?

But if I run this on my machine and hex dump the result, I get:
    
    
    [](file-inputoutput.html#cb160-1)34 12

They’re reversed! What gives?

This has something to do with what’s called the [_endianess_](https://en.wikipedia.org/wiki/Endianess)[ 80](function-specifiers-alignment-specifiersoperators.html#fn80) of the architecture. Some write the most significant bytes first, and some the least significant bytes first.

This means that if you write a multibyte number out straight from memory, you can’t do it in a portable way[81](function-specifiers-alignment-specifiersoperators.html#fn81).

A similar problem exists with floating point. Most systems use the same format for their floating point numbers, but some do not. No guarantees!

So… how can we fix all these problems with numbers and `struct`s to get our data written in a portable way?

The summary is to _serialize_ the data, which is a general term that means to take all the data and write it out in a format that you control, that is well-known, and programmable to work the same way on all platforms.

As you might imagine, this is a solved problem. There are a bunch of serialization libraries you can take advantage of, such as Google’s [_protocol buffers_](https://en.wikipedia.org/wiki/Protocol_buffers)[ 82](function-specifiers-alignment-specifiersoperators.html#fn82), out there and ready to use. They will take care of all the gritty details for you, and even will allow data from your C programs to interoperate with other languages that support the same serialization methods.

Do yourself and everyone a favor! Serialize your binary data when you write it to a stream! This will keep things nice and portable, even if you transfer data files from one architecture to another. 

* * *

[Prev](structs.html) | [Contents](index.html) | [Next](typedef-making-new-types.html)
