[Prev](fixed-width-integer-types.html) | [Contents](index.html) | [Next](multithreading.html)

* * *

# 38 Date and Time Functionality

> “Time is an illusion. Lunchtime doubly so.”  
>  —Ford Prefect, The Hitchhikers Guide to the Galaxy

This isn’t too complex, but it can be a little intimidating at first, both with the different types available and the way we can convert between them.

Mix in GMT (UTC) and local time and we have all the _Usual Fun_ ™ one gets with times and dates.

And of course never forget the golden rule of dates and times: _Never attempt to write your own date and time functionality. Only use what the library gives you._

Time is too complex for mere mortal programmers to handle correctly. Seriously, we all owe a point to everyone who worked on any date and time library, so put that in your budget.

## 38.1 Quick Terminology and Information

Just a couple quick terms in case you don’t have them down.

  * **UTC** : Coordinated Universal Time is a universally[191](function-specifiers-alignment-specifiersoperators.html#fn191) agreed upon, absolute time. Everyone on the planet thinks it’s the same time right now in UTC… even though they have different local times.

  * **GMT** : Greenwich Mean Time, effectively the same as UTC[192](function-specifiers-alignment-specifiersoperators.html#fn192). You probably want to say UTC, or “universal time”. If you’re talking specifically about the GMT time zone, say GMT. Confusingly, many of C’s UTC functions predate UTC and still refer to Greenwich Mean Time. When you see that, know that C means UTC.

  * **Local time** : what time it is where the computer running the program is located. This is described as an offset from UTC. Although there are many time zones in the world, most computers do work in either local time or UTC.




As a general rule, if you are describing an event that happens one time, like a log entry, or a rocket launch, or when pointers finally clicked for you, use UTC.

On the other hand, if it’s something that happens the same time _in every time zone_ , like New Year’s Eve or dinner time, use local time.

Since a lot of languages are only good at converting between UTC and local time, you can cause yourself a lot of pain by choosing to store your dates in the wrong form. (Ask me how I know.)

## 38.2 Date Types

There are two[193](function-specifiers-alignment-specifiersoperators.html#fn193) main types in C when it comes to dates: `time_t` and `struct tm`.

The spec doesn’t actually say much about them:

  * `time_t`: a real type capable of holding a time. So by the spec, this could be a floating type or integer type. In POSIX (Unix-likes), it’s an integer. This holds _calendar time_. Which you can think of as UTC time.

  * `struct tm`: holds the components of a calendar time. This is a _broken-down time_ , i.e. the components of the time, like hour, minute, second, day, month, year, etc.




On a lot of systems, `time_t` represents the number of seconds since [_Epoch_](https://en.wikipedia.org/wiki/Unix_time)[ 194](function-specifiers-alignment-specifiersoperators.html#fn194). Epoch is in some ways the start of time from the computer’s perspective, which is commonly January 1, 1970 UTC. `time_t` can go negative to represent times before Epoch. Windows behaves the same way as Unix from what I can tell.

And what’s in a `struct tm`? The following fields:
    
    
    [](date-and-time-functionality.html#cb729-1)struct tm {
    [](date-and-time-functionality.html#cb729-2)    int tm_sec;    // seconds after the minute -- [0, 60]
    [](date-and-time-functionality.html#cb729-3)    int tm_min;    // minutes after the hour -- [0, 59]
    [](date-and-time-functionality.html#cb729-4)    int tm_hour;   // hours since midnight -- [0, 23]
    [](date-and-time-functionality.html#cb729-5)    int tm_mday;   // day of the month -- [1, 31]
    [](date-and-time-functionality.html#cb729-6)    int tm_mon;    // months since January -- [0, 11]
    [](date-and-time-functionality.html#cb729-7)    int tm_year;   // years since 1900
    [](date-and-time-functionality.html#cb729-8)    int tm_wday;   // days since Sunday -- [0, 6]
    [](date-and-time-functionality.html#cb729-9)    int tm_yday;   // days since January 1 -- [0, 365]
    [](date-and-time-functionality.html#cb729-10)    int tm_isdst;  // Daylight Saving Time flag
    [](date-and-time-functionality.html#cb729-11)};

Note that everything is zero-based except the day of the month.

It’s important to know that you can put any values in these types you want. There are functions to help get the time _now_ , but the types hold _a_ time, not _the_ time.

So the question becomes: “How do you initialize data of these types, and how do you convert between them?”

## 38.3 Initialization and Conversion Between Types

First, you can get the current time and store it in a `time_t` with the `time()` function.
    
    
    [](date-and-time-functionality.html#cb730-1)time_t now;  // Variable to hold the time now
    [](date-and-time-functionality.html#cb730-2)
    [](date-and-time-functionality.html#cb730-3)now = time(NULL);  // You can get it like this...
    [](date-and-time-functionality.html#cb730-4)
    [](date-and-time-functionality.html#cb730-5)time(&now);        // ...or this. Same as the previous line.

Great! You have a variable that gets you the time now.

Amusingly, there’s only one portable way to print out what’s in a `time_t`, and that’s the rarely-used `ctime()` function that prints the value in local time:
    
    
    [](date-and-time-functionality.html#cb731-1)now = time(NULL);
    [](date-and-time-functionality.html#cb731-2)printf("%s", ctime(&now));

This returns a string with a very specific form that includes a newline at the end:
    
    
    [](date-and-time-functionality.html#cb732-1)Sun Feb 28 18:47:25 2021

So that’s kind of inflexible. If you want more control, you should convert that `time_t` into a `struct tm`.

### 38.3.1 Converting `time_t` to `struct tm`

There are two amazing ways to do this conversion:

  * `localtime()`: this function converts a `time_t` to a `struct tm` in local time.



  * `gmtime()`: this function converts a `time_t` to a `struct tm` in UTC. (See ye olde GMT creeping into that function name?)



Let’s see what time it is now by printing out a `struct tm` with the `asctime()` function:
    
    
    [](date-and-time-functionality.html#cb733-1)printf("Local: %s", asctime(localtime(&now)));
    [](date-and-time-functionality.html#cb733-2)printf("  UTC: %s", asctime(gmtime(&now)));

Output (I’m in the Pacific Standard Time zone):
    
    
    [](date-and-time-functionality.html#cb734-1)Local: Sun Feb 28 20:15:27 2021
    [](date-and-time-functionality.html#cb734-2)  UTC: Mon Mar  1 04:15:27 2021

Once you have your `time_t` in a `struct tm`, it opens all kinds of doors. You can print out the time in a variety of ways, figure out which day of the week a date is, and so on. Or convert it back into a `time_t`.

More on that soon!

### 38.3.2 Converting `struct tm` to `time_t`

If you want to go the other way, you can use `mktime()` to get that information.

`mktime()` sets the values of `tm_wday` and `tm_yday` for you, so don’t bother filling them out because they’ll just be overwritten.

Also, you can set `tm_isdst` to `-1` to have it make the determination for you. Or you can manually set it to true or false.
    
    
    [](date-and-time-functionality.html#cb735-1)// Don't be tempted to put leading zeros on these numbers (unless you
    [](date-and-time-functionality.html#cb735-2)// mean for them to be in octal)!
    [](date-and-time-functionality.html#cb735-3)
    [](date-and-time-functionality.html#cb735-4)struct tm some_time = {
    [](date-and-time-functionality.html#cb735-5)    .tm_year=82,   // years since 1900
    [](date-and-time-functionality.html#cb735-6)    .tm_mon=3,     // months since January -- [0, 11]
    [](date-and-time-functionality.html#cb735-7)    .tm_mday=12,   // day of the month -- [1, 31]
    [](date-and-time-functionality.html#cb735-8)    .tm_hour=12,   // hours since midnight -- [0, 23]
    [](date-and-time-functionality.html#cb735-9)    .tm_min=0,     // minutes after the hour -- [0, 59]
    [](date-and-time-functionality.html#cb735-10)    .tm_sec=4,     // seconds after the minute -- [0, 60]
    [](date-and-time-functionality.html#cb735-11)    .tm_isdst=-1,  // Daylight Saving Time flag
    [](date-and-time-functionality.html#cb735-12)};
    [](date-and-time-functionality.html#cb735-13)
    [](date-and-time-functionality.html#cb735-14)time_t some_time_epoch;
    [](date-and-time-functionality.html#cb735-15)
    [](date-and-time-functionality.html#cb735-16)some_time_epoch = mktime(&some_time);
    [](date-and-time-functionality.html#cb735-17)
    [](date-and-time-functionality.html#cb735-18)printf("%s", ctime(&some_time_epoch));
    [](date-and-time-functionality.html#cb735-19)printf("Is DST: %d\n", some_time.tm_isdst);

Output:
    
    
    [](date-and-time-functionality.html#cb736-1)Mon Apr 12 12:00:04 1982
    [](date-and-time-functionality.html#cb736-2)Is DST: 0

When you manually load a `struct tm` like that, it should be in local time. `mktime()` will convert that local time into a `time_t` calendar time.

Weirdly, however, the standard doesn’t give us a way to load up a `struct tm` with a UTC time and convert that to a `time_t`. If you want to do that with Unix-likes, try the non-standard `timegm()`. On Windows, `_mkgmtime()`.

## 38.4 Formatted Date Output

We’ve already seen a couple ways to print formatted date output to the screen. With `time_t` we can use `ctime()`, and with `struct tm` we can use `asctime()`.
    
    
    [](date-and-time-functionality.html#cb737-1)time_t now = time(NULL);
    [](date-and-time-functionality.html#cb737-2)struct tm *local = localtime(&now);
    [](date-and-time-functionality.html#cb737-3)struct tm *utc = gmtime(&now);
    [](date-and-time-functionality.html#cb737-4)
    [](date-and-time-functionality.html#cb737-5)printf("Local time: %s", ctime(&now));     // Local time with time_t
    [](date-and-time-functionality.html#cb737-6)printf("Local time: %s", asctime(local));  // Local time with struct tm
    [](date-and-time-functionality.html#cb737-7)printf("UTC       : %s", asctime(utc));    // UTC with a struct tm

But what if I told you, dear reader, that there’s a way to have much more control over how the date was printed?

Sure, we could fish individual fields out of the `struct tm`, but there’s a great function called `strftime()` that will do a lot of the hard work for you. It’s like `printf()`, except for dates!

Let’s see some examples. In each of these, we pass in a destination buffer, a maximum number of characters to write, and then a format string (in the style of—but not the same as—`printf()`) which tells `strftime()` which components of a `struct tm` to print and how.

You can add other constant characters to include in the output in the format string, as well, just like with `printf()`.

We get a `struct tm` in this case from `localtime()`, but any source works fine.
    
    
    [](date-and-time-functionality.html#cb738-1)#include <stdio.h>
    [](date-and-time-functionality.html#cb738-2)#include <time.h>
    [](date-and-time-functionality.html#cb738-3)
    [](date-and-time-functionality.html#cb738-4)int main(void)
    [](date-and-time-functionality.html#cb738-5){
    [](date-and-time-functionality.html#cb738-6)    char s[128];
    [](date-and-time-functionality.html#cb738-7)    time_t now = time(NULL);
    [](date-and-time-functionality.html#cb738-8)
    [](date-and-time-functionality.html#cb738-9)    // %c: print date as per current locale
    [](date-and-time-functionality.html#cb738-10)    strftime(s, sizeof s, "%c", localtime(&now));
    [](date-and-time-functionality.html#cb738-11)    puts(s);   // Sun Feb 28 22:29:00 2021
    [](date-and-time-functionality.html#cb738-12)
    [](date-and-time-functionality.html#cb738-13)    // %A: full weekday name
    [](date-and-time-functionality.html#cb738-14)    // %B: full month name
    [](date-and-time-functionality.html#cb738-15)    // %d: day of the month
    [](date-and-time-functionality.html#cb738-16)    strftime(s, sizeof s, "%A, %B %d", localtime(&now));
    [](date-and-time-functionality.html#cb738-17)    puts(s);   // Sunday, February 28
    [](date-and-time-functionality.html#cb738-18)
    [](date-and-time-functionality.html#cb738-19)    // %I: hour (12 hour clock)
    [](date-and-time-functionality.html#cb738-20)    // %M: minute
    [](date-and-time-functionality.html#cb738-21)    // %S: second
    [](date-and-time-functionality.html#cb738-22)    // %p: AM or PM
    [](date-and-time-functionality.html#cb738-23)    strftime(s, sizeof s, "It's %I:%M:%S %p", localtime(&now));
    [](date-and-time-functionality.html#cb738-24)    puts(s);   // It's 10:29:00 PM
    [](date-and-time-functionality.html#cb738-25)
    [](date-and-time-functionality.html#cb738-26)    // %F: ISO 8601 yyyy-mm-dd
    [](date-and-time-functionality.html#cb738-27)    // %T: ISO 8601 hh:mm:ss
    [](date-and-time-functionality.html#cb738-28)    // %z: ISO 8601 time zone offset
    [](date-and-time-functionality.html#cb738-29)    strftime(s, sizeof s, "ISO 8601: %FT%T%z", localtime(&now));
    [](date-and-time-functionality.html#cb738-30)    puts(s);   // ISO 8601: 2021-02-28T22:29:00-0800
    [](date-and-time-functionality.html#cb738-31)}

There are a _ton_ of date printing format specifiers for `strftime()`, so be sure to check them out in the [`strftime()` reference page](https://beej.us/guide/bgclr/html/split/time.html#man-strftime)[195](function-specifiers-alignment-specifiersoperators.html#fn195).

## 38.5 More Resolution with `timespec_get()`

You can get the number of seconds and nanoseconds since Epoch with `timespec_get()`.

Maybe.

Implementations might not have nanosecond resolution (that’s one billionth of a second) so who knows how many significant places you’ll get, but give it a shot and see.

`timespec_get()` takes two arguments. One is a pointer to a `struct timespec` to hold the time information. And the other is the `base`, which the spec lets you set to `TIME_UTC` indicating that you’re interested in seconds since Epoch. (Other implementations might give you more options for the `base`.)

And the structure itself has two fields:
    
    
    [](date-and-time-functionality.html#cb739-1)struct timespec {
    [](date-and-time-functionality.html#cb739-2)    time_t tv_sec;   // Seconds
    [](date-and-time-functionality.html#cb739-3)    long   tv_nsec;  // Nanoseconds (billionths of a second)
    [](date-and-time-functionality.html#cb739-4)};

Here’s an example where we get the time and print it out both as integer values and also a floating value:
    
    
    [](date-and-time-functionality.html#cb740-1)struct timespec ts;
    [](date-and-time-functionality.html#cb740-2)
    [](date-and-time-functionality.html#cb740-3)timespec_get(&ts, TIME_UTC);
    [](date-and-time-functionality.html#cb740-4)
    [](date-and-time-functionality.html#cb740-5)printf("%ld s, %ld ns\n", ts.tv_sec, ts.tv_nsec);
    [](date-and-time-functionality.html#cb740-6)
    [](date-and-time-functionality.html#cb740-7)double float_time = ts.tv_sec + ts.tv_nsec/1000000000.0;
    [](date-and-time-functionality.html#cb740-8)printf("%f seconds since epoch\n", float_time);

Example output:
    
    
    [](date-and-time-functionality.html#cb741-1)1614581530 s, 806325800 ns
    [](date-and-time-functionality.html#cb741-2)1614581530.806326 seconds since epoch

`struct timespec` also makes an appearance in a number of the threading functions that need to be able to specify time with that resolution.

## 38.6 Differences Between Times

One quick note about getting the difference between two `time_t`s: since the spec doesn’t dictate how that type represents a time, you might not be able to simply subtract two `time_t`s and get anything sensible[196](function-specifiers-alignment-specifiersoperators.html#fn196).

Luckily you can use `difftime()` to compute the difference in seconds between two dates.

In the following example, we have two events that occur some time apart, and we use `difftime()` to compute the difference.
    
    
    [](date-and-time-functionality.html#cb742-1)#include <stdio.h>
    [](date-and-time-functionality.html#cb742-2)#include <time.h>
    [](date-and-time-functionality.html#cb742-3)
    [](date-and-time-functionality.html#cb742-4)int main(void)
    [](date-and-time-functionality.html#cb742-5){
    [](date-and-time-functionality.html#cb742-6)    struct tm time_a = {
    [](date-and-time-functionality.html#cb742-7)        .tm_year=82,   // years since 1900
    [](date-and-time-functionality.html#cb742-8)        .tm_mon=3,     // months since January -- [0, 11]
    [](date-and-time-functionality.html#cb742-9)        .tm_mday=12,   // day of the month -- [1, 31]
    [](date-and-time-functionality.html#cb742-10)        .tm_hour=4,    // hours since midnight -- [0, 23]
    [](date-and-time-functionality.html#cb742-11)        .tm_min=00,    // minutes after the hour -- [0, 59]
    [](date-and-time-functionality.html#cb742-12)        .tm_sec=04,    // seconds after the minute -- [0, 60]
    [](date-and-time-functionality.html#cb742-13)        .tm_isdst=-1,  // Daylight Saving Time flag
    [](date-and-time-functionality.html#cb742-14)    };
    [](date-and-time-functionality.html#cb742-15)
    [](date-and-time-functionality.html#cb742-16)    struct tm time_b = {
    [](date-and-time-functionality.html#cb742-17)        .tm_year=120,  // years since 1900
    [](date-and-time-functionality.html#cb742-18)        .tm_mon=10,    // months since January -- [0, 11]
    [](date-and-time-functionality.html#cb742-19)        .tm_mday=15,   // day of the month -- [1, 31]
    [](date-and-time-functionality.html#cb742-20)        .tm_hour=16,   // hours since midnight -- [0, 23]
    [](date-and-time-functionality.html#cb742-21)        .tm_min=27,    // minutes after the hour -- [0, 59]
    [](date-and-time-functionality.html#cb742-22)        .tm_sec=00,    // seconds after the minute -- [0, 60]
    [](date-and-time-functionality.html#cb742-23)        .tm_isdst=-1,  // Daylight Saving Time flag
    [](date-and-time-functionality.html#cb742-24)    };
    [](date-and-time-functionality.html#cb742-25)
    [](date-and-time-functionality.html#cb742-26)    time_t cal_a = mktime(&time_a);
    [](date-and-time-functionality.html#cb742-27)    time_t cal_b = mktime(&time_b);
    [](date-and-time-functionality.html#cb742-28)
    [](date-and-time-functionality.html#cb742-29)    double diff = difftime(cal_b, cal_a);
    [](date-and-time-functionality.html#cb742-30)
    [](date-and-time-functionality.html#cb742-31)    double years = diff / 60 / 60 / 24 / 365.2425;  // close enough
    [](date-and-time-functionality.html#cb742-32)
    [](date-and-time-functionality.html#cb742-33)    printf("%f seconds (%f years) between events\n", diff, years);
    [](date-and-time-functionality.html#cb742-34)}

Output:
    
    
    [](date-and-time-functionality.html#cb743-1)1217996816.000000 seconds (38.596783 years) between events

And there you have it! Remember to use `difftime()` to take the time difference. Even though you can just subtract on a POSIX system, might as well stay portable.

* * *

[Prev](fixed-width-integer-types.html) | [Contents](index.html) | [Next](multithreading.html)
