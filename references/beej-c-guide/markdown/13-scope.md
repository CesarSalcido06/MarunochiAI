[Prev](manual-memory-allocation.html) | [Contents](index.html) | [Next](types-ii-way-more-types.html)

* * *

# 13 Scope

Scope is all about what variables are visible in what contexts.

## 13.1 Block Scope

This is the scope of almost all the variables devs define. It includes what other languages might call “function scope”, i.e. variables that are declared inside functions.

The basic rule is that if you’ve declared a variable in a block delimited by squirrelly braces, the scope of that variable is that block.

If there’s a block inside a block, then variables declared in the _inner_ block are local to that block, and cannot be seen in the outer scope.

Once a variable’s scope ends, that variable can no longer be referenced, and you can consider its value to be gone into the great [bit bucket](https://en.wikipedia.org/wiki/Bit_bucket)[92](function-specifiers-alignment-specifiersoperators.html#fn92) in the sky.

An example with nested scope:
    
    
    [](scope.html#cb209-1)#include <stdio.h>
    [](scope.html#cb209-2)
    [](scope.html#cb209-3)int main(void)
    [](scope.html#cb209-4){
    [](scope.html#cb209-5)    int a = 12;         // Local to outer block, but visible in inner block
    [](scope.html#cb209-6)
    [](scope.html#cb209-7)    if  (a == 12) {
    [](scope.html#cb209-8)        int b = 99;     // Local to inner block, not visible in outer block
    [](scope.html#cb209-9)
    [](scope.html#cb209-10)        printf("%d %d\n", a, b);  // OK: "12 99"
    [](scope.html#cb209-11)    }
    [](scope.html#cb209-12)
    [](scope.html#cb209-13)    printf("%d\n", a);  // OK, we're still in a's scope
    [](scope.html#cb209-14)
    [](scope.html#cb209-15)    printf("%d\n", b);  // ILLEGAL, out of b's scope
    [](scope.html#cb209-16)}

### 13.1.1 Where To Define Variables

Another fun fact is that you can define variables anywhere in the block, within reason—they have the scope of that block, but cannot be used before they are defined.
    
    
    [](scope.html#cb210-1)#include <stdio.h>
    [](scope.html#cb210-2)
    [](scope.html#cb210-3)int main(void)
    [](scope.html#cb210-4){
    [](scope.html#cb210-5)    int i = 0;
    [](scope.html#cb210-6)
    [](scope.html#cb210-7)    printf("%d\n", i);     // OK: "0"
    [](scope.html#cb210-8)
    [](scope.html#cb210-9)    //printf("%d\n", j);   // ILLEGAL--can't use j before it's defined
    [](scope.html#cb210-10)
    [](scope.html#cb210-11)    int j = 5;
    [](scope.html#cb210-12)
    [](scope.html#cb210-13)    printf("%d %d\n", i, j);   // OK: "0 5"
    [](scope.html#cb210-14)}

Historically, C required all the variables be defined before any code in the block, but this is no longer the case in the C99 standard.

### 13.1.2 Variable Hiding

If you have a variable named the same thing at an inner scope as one at an outer scope, the one at the inner scope takes precedence as long as you’re running in the inner scope. That is, it _hides_ the one at outer scope for the duration of its lifetime.
    
    
    [](scope.html#cb211-1)#include <stdio.h>
    [](scope.html#cb211-2)
    [](scope.html#cb211-3)int main(void)
    [](scope.html#cb211-4){
    [](scope.html#cb211-5)    int i = 10;
    [](scope.html#cb211-6)
    [](scope.html#cb211-7)    {
    [](scope.html#cb211-8)        int i = 20;
    [](scope.html#cb211-9)
    [](scope.html#cb211-10)        printf("%d\n", i);  // Inner scope i, 20 (outer i is hidden)
    [](scope.html#cb211-11)    }
    [](scope.html#cb211-12)
    [](scope.html#cb211-13)    printf("%d\n", i);  // Outer scope i, 10
    [](scope.html#cb211-14)}

You might have noticed in that example that I just threw a block in there at line 7, not so much as a `for` or `if` statement to kick it off! This is perfectly legal. Sometimes a dev will want to group a bunch of local variables together for a quick computation and will do this, but it’s rare to see. 

## 13.2 File Scope

If you define a variable outside of a block, that variable has _file scope_. It’s visible in all functions in the file that come after it, and shared between them. (An exception is if a block defines a variable of the same name, it would hide the one at file scope.)

This is closest to what you would consider to be “global” scope in another language.

For example:
    
    
    [](scope.html#cb212-1)#include <stdio.h>
    [](scope.html#cb212-2)
    [](scope.html#cb212-3)int shared = 10;    // File scope! Visible to the whole file after this!
    [](scope.html#cb212-4)
    [](scope.html#cb212-5)void func1(void)
    [](scope.html#cb212-6){
    [](scope.html#cb212-7)    shared += 100;  // Now shared holds 110
    [](scope.html#cb212-8)}
    [](scope.html#cb212-9)
    [](scope.html#cb212-10)void func2(void)
    [](scope.html#cb212-11){
    [](scope.html#cb212-12)    printf("%d\n", shared);  // Prints "110"
    [](scope.html#cb212-13)}
    [](scope.html#cb212-14)
    [](scope.html#cb212-15)int main(void)
    [](scope.html#cb212-16){
    [](scope.html#cb212-17)    func1();
    [](scope.html#cb212-18)    func2();
    [](scope.html#cb212-19)}

Note that if `shared` were declared at the bottom of the file, it wouldn’t compile. It has to be declared _before_ any functions use it.

There are ways to further modify items at file scope, namely with [static](types-iv-qualifiers-and-specifiers.html#static) and [extern](types-iv-qualifiers-and-specifiers.html#extern), but we’ll talk more about those later. 

## 13.3 `for`-loop Scope

I really don’t know what to call this, as C11 §6.8.5.3¶1 doesn’t give it a proper name. We’ve done it already a few times in this guide, as well. It’s when you declare a variable inside the first clause of a `for`-loop:
    
    
    [](scope.html#cb213-1)for (int i = 0; i < 10; i++)
    [](scope.html#cb213-2)    printf("%d\n", i);
    [](scope.html#cb213-3)
    [](scope.html#cb213-4)printf("%d\n", i);  // ILLEGAL--i is only in scope for the for-loop

In that example, `i`’s lifetime begins the moment it is defined, and continues for the duration of the loop.

If the loop body is enclosed in a block, the variables defined in the `for`-loop are visible from that inner scope.

Unless, of course, that inner scope hides them. This crazy example prints `999` five times:
    
    
    [](scope.html#cb214-1)#include <stdio.h>
    [](scope.html#cb214-2)
    [](scope.html#cb214-3)int main(void)
    [](scope.html#cb214-4){
    [](scope.html#cb214-5)    for (int i = 0; i < 5; i++) {
    [](scope.html#cb214-6)        int i = 999;  // Hides the i in the for-loop scope
    [](scope.html#cb214-7)        printf("%d\n", i);
    [](scope.html#cb214-8)    }
    [](scope.html#cb214-9)}

## 13.4 A Note on Function Scope

The C spec does refer to _function scope_ , but it’s used exclusively with _labels_ , something we haven’t discussed yet. More on that another day. 

* * *

[Prev](manual-memory-allocation.html) | [Contents](index.html) | [Next](types-ii-way-more-types.html)
