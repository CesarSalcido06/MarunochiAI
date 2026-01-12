[Prev](multifile-projects.html) | [Contents](index.html) | [Next](the-c-preprocessor.html)

* * *

# 18 The Outside Environment

When you run a program, it’s actually you talking to the shell, saying, “Hey, please run this thing.” And the shell says, “Sure,” and then tells the operating system, “Hey, could you please make a new process and run this thing?” And if all goes well, the OS complies and your program runs.

But there’s a whole world outside your program in the shell that can be interacted with from within C. We’ll look at a few of those in this chapter.

## 18.1 Command Line Arguments

Many command line utilities accept _command line arguments_. For example, if we want to see all files that end in `.txt`, we can type something like this on a Unix-like system:
    
    
    [](the-outside-environment.html#cb305-1)ls *.txt

(or `dir` instead of `ls` on a Windows system).

In this case, the command is `ls`, but it arguments are all all files that end with `.txt`[120](function-specifiers-alignment-specifiersoperators.html#fn120).

So how can we see what is passed into program from the command line?

Say we have a program called `add` that adds all numbers passed on the command line and prints the result:
    
    
    [](the-outside-environment.html#cb306-1)./add 10 30 5
    [](the-outside-environment.html#cb306-2)45

That’s gonna pay the bills for sure!

But seriously, this is a great tool for seeing how to get those arguments from the command line and break them down.

First, let’s see how to get them at all. For this, we’re going to need a new `main()`!

Here’s a program that prints out all the command line arguments. For example, if we name the executable `foo`, we can run it like this:
    
    
    [](the-outside-environment.html#cb307-1)./foo i like turtles

and we’ll see this output:
    
    
    [](the-outside-environment.html#cb308-1)arg 0: ./foo
    [](the-outside-environment.html#cb308-2)arg 1: i
    [](the-outside-environment.html#cb308-3)arg 2: like
    [](the-outside-environment.html#cb308-4)arg 3: turtles

It’s a little weird, because the zeroth argument is the name of the executable, itself. But that’s just something to get used to. The arguments themselves follow directly.

Source:
    
    
    [](the-outside-environment.html#cb309-1)#include <stdio.h>
    [](the-outside-environment.html#cb309-2)
    [](the-outside-environment.html#cb309-3)int main(int argc, char *argv[])
    [](the-outside-environment.html#cb309-4){
    [](the-outside-environment.html#cb309-5)    for (int i = 0; i < argc; i++) {
    [](the-outside-environment.html#cb309-6)        printf("arg %d: %s\n", i, argv[i]);
    [](the-outside-environment.html#cb309-7)    }
    [](the-outside-environment.html#cb309-8)}

Whoa! What’s going on with the `main()` function signature? What’s `argc` and `argv`[121](function-specifiers-alignment-specifiersoperators.html#fn121) (pronounced _arg-cee_ and _arg-vee_)?

Let’s start with the easy one first: `argc`. This is the _argument count_ , including the program name, itself. If you think of all the arguments as an array of strings, which is exactly what they are, then you can think of `argc` as the length of that array, which is exactly what it is.

And so what we’re doing in that loop is going through all the `argv`s and printing them out one at a time, so for a given input:
    
    
    [](the-outside-environment.html#cb310-1)./foo i like turtles

we get a corresponding output:
    
    
    [](the-outside-environment.html#cb311-1)arg 0: ./foo
    [](the-outside-environment.html#cb311-2)arg 1: i
    [](the-outside-environment.html#cb311-3)arg 2: like
    [](the-outside-environment.html#cb311-4)arg 3: turtles

With that in mind, we should be good to go with our adder program.

Our plan:

  * Look at all the command line arguments (past `argv[0]`, the program name)
  * Convert them to integers
  * Add them to a running total
  * Print the result



Let’s get to it!
    
    
    [](the-outside-environment.html#cb312-1)#include <stdio.h>
    [](the-outside-environment.html#cb312-2)#include <stdlib.h>
    [](the-outside-environment.html#cb312-3)
    [](the-outside-environment.html#cb312-4)int main(int argc, char **argv)
    [](the-outside-environment.html#cb312-5){
    [](the-outside-environment.html#cb312-6)    int total = 0;
    [](the-outside-environment.html#cb312-7)
    [](the-outside-environment.html#cb312-8)    for (int i = 1; i < argc; i++) {  // Start at 1, the first argument
    [](the-outside-environment.html#cb312-9)        int value = atoi(argv[i]);    // Use strtol() for better error handling
    [](the-outside-environment.html#cb312-10)
    [](the-outside-environment.html#cb312-11)        total += value;
    [](the-outside-environment.html#cb312-12)    }
    [](the-outside-environment.html#cb312-13)
    [](the-outside-environment.html#cb312-14)    printf("%d\n", total);
    [](the-outside-environment.html#cb312-15)}

Sample runs:
    
    
    [](the-outside-environment.html#cb313-1)$ ./add
    [](the-outside-environment.html#cb313-2)0
    [](the-outside-environment.html#cb313-3)$ ./add 1
    [](the-outside-environment.html#cb313-4)1
    [](the-outside-environment.html#cb313-5)$ ./add 1 2
    [](the-outside-environment.html#cb313-6)3
    [](the-outside-environment.html#cb313-7)$ ./add 1 2 3
    [](the-outside-environment.html#cb313-8)6
    [](the-outside-environment.html#cb313-9)$ ./add 1 2 3 4
    [](the-outside-environment.html#cb313-10)10

Of course, it might puke if you pass in a non-integer, but hardening against that is left as an exercise to the reader.

### 18.1.1 The Last `argv` is `NULL`

One bit of fun trivia about `argv` is that after the last string is a pointer to `NULL`.

That is:
    
    
    [](the-outside-environment.html#cb314-1)argv[argc] == NULL

is always true!

This might seem pointless, but it turns out to be useful in a couple places; we’ll take a look at one of those right now.

### 18.1.2 The Alternate: `char **argv`

Remember that when you call a function, C doesn’t differentiate between array notation and pointer notation in the function signature.

That is, these are the same:
    
    
    [](the-outside-environment.html#cb315-1)void foo(char a[])
    [](the-outside-environment.html#cb315-2)void foo(char *a)

Now, it’s been convenient to think of `argv` as an array of strings, i.e. an array of `char*`s, so this made sense:
    
    
    [](the-outside-environment.html#cb316-1)int main(int argc, char *argv[])

but because of the equivalence, you could also write:
    
    
    [](the-outside-environment.html#cb317-1)int main(int argc, char **argv)

Yeah, that’s a pointer to a pointer, all right! If it makes it easier, think of it as a pointer to a string. But really, it’s a pointer to a value that points to a `char`.

Also recall that these are equivalent:
    
    
    [](the-outside-environment.html#cb318-1)argv[i]
    [](the-outside-environment.html#cb318-2)*(argv + i)

which means you can do pointer arithmetic on `argv`.

So an alternate way to consume the command line arguments might be to just walk along the `argv` array by bumping up a pointer until we hit that `NULL` at the end.

Let’s modify our adder to do that:
    
    
    [](the-outside-environment.html#cb319-1)#include <stdio.h>
    [](the-outside-environment.html#cb319-2)#include <stdlib.h>
    [](the-outside-environment.html#cb319-3)
    [](the-outside-environment.html#cb319-4)int main(int argc, char **argv)
    [](the-outside-environment.html#cb319-5){
    [](the-outside-environment.html#cb319-6)    int total = 0;
    [](the-outside-environment.html#cb319-7)    
    [](the-outside-environment.html#cb319-8)    // Cute trick to get the compiler to stop warning about the
    [](the-outside-environment.html#cb319-9)    // unused variable argc:
    [](the-outside-environment.html#cb319-10)    (void)argc;
    [](the-outside-environment.html#cb319-11)
    [](the-outside-environment.html#cb319-12)    for (char **p = argv + 1; *p != NULL; p++) {
    [](the-outside-environment.html#cb319-13)        int value = atoi(*p);  // Use strtol() for better error handling
    [](the-outside-environment.html#cb319-14)
    [](the-outside-environment.html#cb319-15)        total += value;
    [](the-outside-environment.html#cb319-16)    }
    [](the-outside-environment.html#cb319-17)
    [](the-outside-environment.html#cb319-18)    printf("%d\n", total);
    [](the-outside-environment.html#cb319-19)}

Personally, I use array notation to access `argv`, but have seen this style floating around, as well.

### 18.1.3 Fun Facts

Just a few more things about `argc` and `argv`.

  * Some environments might not set `argv[0]` to the program name. If it’s not available, `argv[0]` will be an empty string. I’ve never seen this happen.

  * The spec is actually pretty liberal with what an implementation can do with `argv` and where those values come from. But every system I’ve been on works the same way, as we’ve discussed in this section.

  * You can modify `argc`, `argv`, or any of the strings that `argv` points to. (Just don’t make those strings longer than they already are!)

  * On some Unix-like systems, modifying the string `argv[0]` results in the output of `ps` changing[122](function-specifiers-alignment-specifiersoperators.html#fn122).

Normally, if you have a program called `foo` that you’ve run with `./foo`, you might see this in the output of `ps`:
        
        [](the-outside-environment.html#cb320-1) 4078 tty1     S      0:00 ./foo

But if you modify `argv[0]` like so, being careful that the new string `"Hi! "` is the same length as the old one `"./foo"`:
        
        [](the-outside-environment.html#cb321-1)strcpy(argv[0], "Hi!  ");

and then run `ps` while the program `./foo` is still executing, we’ll see this instead:
        
        [](the-outside-environment.html#cb322-1) 4079 tty1     S      0:00 Hi!  

This behavior is not in the spec and is highly system-dependent.




## 18.2 Exit Status

Did you notice that the function signatures for `main()` have it returning type `int`? What’s that all about? It has to do with a thing called the _exit status_ , which is an integer that can be returned to the program that launched yours to let it know how things went.

Now, there are a number of ways a program can exit in C, including `return`ing from `main()`, or calling one of the `exit()` variants.

All of these methods accept an `int` as an argument.

Side note: did you see that in basically all my examples, even though `main()` is supposed to return an `int`, I don’t actually `return` anything? In any other function, this would be illegal, but there’s a special case in C: if execution reaches the end of `main()` without finding a `return`, it automatically does a `return 0`. 

But what does the `0` mean? What other numbers can we put there? And how are they used?

The spec is both clear and vague on the matter, as is common. Clear because it spells out what you can do, but vague in that it doesn’t particularly limit it, either.

Nothing for it but to _forge ahead_ and figure it out!

Let’s get [Inception](https://en.wikipedia.org/wiki/Inception)[123](function-specifiers-alignment-specifiersoperators.html#fn123) for a second: turns out that when you run your program, _you’re running it from another program_.

Usually this other program is some kind of [shell](https://en.wikipedia.org/wiki/Shell_\(computing\))[124](function-specifiers-alignment-specifiersoperators.html#fn124) that doesn’t do much on its own except launch other programs.

But this is a multi-phase process, especially visible in command-line shells:

  1. The shell launches your program
  2. The shell typically goes to sleep (for command-line shells)
  3. Your program runs
  4. Your program terminates
  5. The shell wakes up and waits for another command



Now, there’s a little piece of communication that takes place between steps 4 and 5: the program can return a _status value_ that the shell can interrogate. Typically, this value is used to indicate the success or failure of your program, and, if a failure, what type of failure.

This value is what we’ve been `return`ing from `main()`. That’s the status.

Now, the C spec allows for two different status values, which have macro names defined in `<stdlib.h>`:

Status | Description  
---|---  
`EXIT_SUCCESS` or `0` | Program terminated successfully.  
`EXIT_FAILURE` | Program terminated with an error.  
  
Let’s write a short program that multiplies two numbers from the command line. We’ll require that you specify exactly two values. If you don’t, we’ll print an error message, and exit with an error status.
    
    
    [](the-outside-environment.html#cb323-1)#include <stdio.h>
    [](the-outside-environment.html#cb323-2)#include <stdlib.h>
    [](the-outside-environment.html#cb323-3)
    [](the-outside-environment.html#cb323-4)int main(int argc, char **argv)
    [](the-outside-environment.html#cb323-5){
    [](the-outside-environment.html#cb323-6)    if (argc != 3) {
    [](the-outside-environment.html#cb323-7)        printf("usage: mult x y\n");
    [](the-outside-environment.html#cb323-8)        return EXIT_FAILURE;   // Indicate to shell that it didn't work
    [](the-outside-environment.html#cb323-9)    }
    [](the-outside-environment.html#cb323-10)
    [](the-outside-environment.html#cb323-11)    printf("%d\n", atoi(argv[1]) * atoi(argv[2]));
    [](the-outside-environment.html#cb323-12)
    [](the-outside-environment.html#cb323-13)    return 0;  // same as EXIT_SUCCESS, everything was good.
    [](the-outside-environment.html#cb323-14)}

Now if we try to run this, we get the expected effect until we specify exactly the right number of command-line arguments:
    
    
    [](the-outside-environment.html#cb324-1)$ ./mult
    [](the-outside-environment.html#cb324-2)usage: mult x y
    [](the-outside-environment.html#cb324-3)
    [](the-outside-environment.html#cb324-4)$ ./mult 3 4 5
    [](the-outside-environment.html#cb324-5)usage: mult x y
    [](the-outside-environment.html#cb324-6)
    [](the-outside-environment.html#cb324-7)$ ./mult 3 4
    [](the-outside-environment.html#cb324-8)12

But that doesn’t really show the exit status that we returned, does it? We can get the shell to print it out, though. Assuming you’re running Bash or another POSIX shell, you can use `echo $?` to see it[125](function-specifiers-alignment-specifiersoperators.html#fn125).

Let’s try:
    
    
    [](the-outside-environment.html#cb325-1)$ ./mult
    [](the-outside-environment.html#cb325-2)usage: mult x y
    [](the-outside-environment.html#cb325-3)$ echo $?
    [](the-outside-environment.html#cb325-4)1
    [](the-outside-environment.html#cb325-5)
    [](the-outside-environment.html#cb325-6)$ ./mult 3 4 5
    [](the-outside-environment.html#cb325-7)usage: mult x y
    [](the-outside-environment.html#cb325-8)$ echo $?
    [](the-outside-environment.html#cb325-9)1
    [](the-outside-environment.html#cb325-10)
    [](the-outside-environment.html#cb325-11)$ ./mult 3 4
    [](the-outside-environment.html#cb325-12)12
    [](the-outside-environment.html#cb325-13)$ echo $?
    [](the-outside-environment.html#cb325-14)0

Interesting! We see that on my system, `EXIT_FAILURE` is `1`. The spec doesn’t spell this out, so it could be any number. But try it; it’s probably `1` on your system, too.

### 18.2.1 Other Exit Status Values

The status `0` most definitely means success, but what about all the other integers, even negative ones?

Here we’re going off the C spec and into Unix land. In general, while `0` means success, a positive non-zero number means failure. So you can only have one type of success, and multiple types of failure. Bash says the exit code should be between 0 and 255, though a number of codes are reserved.

In short, if you want to indicate different error exit statuses in a Unix environment, you can start with `1` and work your way up.

On Linux, if you try any code outside the range 0-255, it will bitwise AND the code with `0xff`, effectively clamping it to that range.

You can script the shell to later use these status codes to make decisions about what to do next.

## 18.3 Environment Variables

Before I get into this, I need to warn you that C doesn’t specify what an environment variable is. So I’m going to describe the environment variable system that works on every major platform I’m aware of.

Basically, the environment is the program that’s going to run your program, e.g. the bash shell. And it might have some bash variables defined. In case you didn’t know, the shell can make its own variables. Each shell is different, but in bash you can just type `set` and it’ll show you all of them.

Here’s an excerpt from the 61 variables that are defined in my bash shell:
    
    
    [](the-outside-environment.html#cb326-1)HISTFILE=/home/beej/.bash_history
    [](the-outside-environment.html#cb326-2)HISTFILESIZE=500
    [](the-outside-environment.html#cb326-3)HISTSIZE=500
    [](the-outside-environment.html#cb326-4)HOME=/home/beej
    [](the-outside-environment.html#cb326-5)HOSTNAME=FBILAPTOP
    [](the-outside-environment.html#cb326-6)HOSTTYPE=x86_64
    [](the-outside-environment.html#cb326-7)IFS=$' \t\n'

Notice they are in the form of key/value pairs. For example, one key is `HOSTTYPE` and its value is `x86_64`. From a C perspective, all values are strings, even if they’re numbers[126](function-specifiers-alignment-specifiersoperators.html#fn126).

So, _anyway_! Long story short, it’s possible to get these values from inside your C program.

Let’s write a program that uses the standard `getenv()` function to look up a value that you set in the shell.

`getenv()` will return a pointer to the value string, or else `NULL` if the environment variable doesn’t exist.
    
    
    [](the-outside-environment.html#cb327-1)#include <stdio.h>
    [](the-outside-environment.html#cb327-2)#include <stdlib.h>
    [](the-outside-environment.html#cb327-3)
    [](the-outside-environment.html#cb327-4)int main(void)
    [](the-outside-environment.html#cb327-5){
    [](the-outside-environment.html#cb327-6)    char *val = getenv("FROTZ");  // Try to get the value
    [](the-outside-environment.html#cb327-7)
    [](the-outside-environment.html#cb327-8)    // Check to make sure it exists
    [](the-outside-environment.html#cb327-9)    if (val == NULL) {
    [](the-outside-environment.html#cb327-10)        printf("Cannot find the FROTZ environment variable\n");
    [](the-outside-environment.html#cb327-11)        return EXIT_FAILURE;
    [](the-outside-environment.html#cb327-12)    }
    [](the-outside-environment.html#cb327-13)
    [](the-outside-environment.html#cb327-14)    printf("Value: %s\n", val);
    [](the-outside-environment.html#cb327-15)}

If I run this directly, I get this:
    
    
    [](the-outside-environment.html#cb328-1)$ ./foo
    [](the-outside-environment.html#cb328-2)Cannot find the FROTZ environment variable

which makes sense, since I haven’t set it yet.

In bash, I can set it to something with[127](function-specifiers-alignment-specifiersoperators.html#fn127):
    
    
    [](the-outside-environment.html#cb329-1)$ export FROTZ="C is awesome!"

Then if I run it, I get:
    
    
    [](the-outside-environment.html#cb330-1)$ ./foo
    [](the-outside-environment.html#cb330-2)Value: C is awesome!

In this way, you can set up data in environment variables, and you can get it in your C code and modify your behavior accordingly.

### 18.3.1 Setting Environment Variables

This isn’t standard, but a lot of systems provide ways to set environment variables.

If on a Unix-like, look up the documentation for `putenv()`, `setenv()`, and `unsetenv()`. On Windows, see `_putenv()`.

### 18.3.2 Unix-like Alternative Environment Variables

If you’re on a Unix-like system, odds are you have another couple ways of getting access to environment variables. Note that although the spec points this out as a common extension, it’s not truly part of the C standard. It is, however, part of the POSIX standard.

One of these is a variable called `environ` that must be declared like so:
    
    
    [](the-outside-environment.html#cb331-1)extern char **environ;

It’s an array of strings terminated with a `NULL` pointer.

You should declare it yourself before you use it, or you might find it in the non-standard `<unistd.h>` header file.

Each string is in the form `"key=value"` so you’ll have to split it and parse it yourself if you want to get the keys and values out.

Here’s an example of looping through and printing out the environment variables a couple different ways:
    
    
    [](the-outside-environment.html#cb332-1)#include <stdio.h>
    [](the-outside-environment.html#cb332-2)
    [](the-outside-environment.html#cb332-3)extern char **environ;  // MUST be extern AND named "environ"
    [](the-outside-environment.html#cb332-4)
    [](the-outside-environment.html#cb332-5)int main(void)
    [](the-outside-environment.html#cb332-6){
    [](the-outside-environment.html#cb332-7)    for (char **p = environ; *p != NULL; p++) {
    [](the-outside-environment.html#cb332-8)        printf("%s\n", *p);
    [](the-outside-environment.html#cb332-9)    }
    [](the-outside-environment.html#cb332-10)
    [](the-outside-environment.html#cb332-11)    // Or you could do this:
    [](the-outside-environment.html#cb332-12)    for (int i = 0; environ[i] != NULL; i++) {
    [](the-outside-environment.html#cb332-13)        printf("%s\n", environ[i]);
    [](the-outside-environment.html#cb332-14)    }
    [](the-outside-environment.html#cb332-15)}

For a bunch of output that looks like this:
    
    
    [](the-outside-environment.html#cb333-1)SHELL=/bin/bash
    [](the-outside-environment.html#cb333-2)COLORTERM=truecolor
    [](the-outside-environment.html#cb333-3)TERM_PROGRAM_VERSION=1.53.2
    [](the-outside-environment.html#cb333-4)LOGNAME=beej
    [](the-outside-environment.html#cb333-5)HOME=/home/beej
    [](the-outside-environment.html#cb333-6)... etc ...

Use `getenv()` if at all possible because it’s more portable. But if you have to iterate over environment variables, using `environ` might be the way to go.

Another non-standard way to get the environment variables is as a parameter to `main()`. It works much the same way, but you avoid needing to add your `extern` `environ` variable. [Not even the POSIX spec supports this](https://pubs.opengroup.org/onlinepubs/9699919799/functions/exec.html)[128](function-specifiers-alignment-specifiersoperators.html#fn128) as far as I can tell, but it’s common in Unix land.
    
    
    [](the-outside-environment.html#cb334-1)#include <stdio.h>
    [](the-outside-environment.html#cb334-2)
    [](the-outside-environment.html#cb334-3)int main(int argc, char **argv, char **env)  // <-- env!
    [](the-outside-environment.html#cb334-4){
    [](the-outside-environment.html#cb334-5)    (void)argc; (void)argv;  // Suppress unused warnings
    [](the-outside-environment.html#cb334-6)
    [](the-outside-environment.html#cb334-7)    for (char **p = env; *p != NULL; p++) {
    [](the-outside-environment.html#cb334-8)        printf("%s\n", *p);
    [](the-outside-environment.html#cb334-9)    }
    [](the-outside-environment.html#cb334-10)
    [](the-outside-environment.html#cb334-11)    // Or you could do this:
    [](the-outside-environment.html#cb334-12)    for (int i = 0; env[i] != NULL; i++) {
    [](the-outside-environment.html#cb334-13)        printf("%s\n", env[i]);
    [](the-outside-environment.html#cb334-14)    }
    [](the-outside-environment.html#cb334-15)}

Just like using `environ` but _even less portable_. It’s good to have goals.

* * *

[Prev](multifile-projects.html) | [Contents](index.html) | [Next](the-c-preprocessor.html)
