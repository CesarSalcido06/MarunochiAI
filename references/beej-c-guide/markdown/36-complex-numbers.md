[Prev](incomplete-types.html) | [Contents](index.html) | [Next](fixed-width-integer-types.html)

* * *

# 36 Complex Numbers

A tiny primer on [Complex numbers](https://en.wikipedia.org/wiki/Complex_number)[185](function-specifiers-alignment-specifiersoperators.html#fn185) stolen directly from Wikipedia:

> A **complex number** is a number that can be expressed in the form \\(a+bi\\), where \\(a\\) and \\(b\\) are real numbers [i.e. floating point types in C], and \\(i\\) represents the imaginary unit, satisfying the equation \\(i^2=−1\\). Because no real number satisfies this equation, \\(i\\) is called an imaginary number. For the complex number \\(a+bi\\), \\(a\\) is called the **real part** , and \\(b\\) is called the **imaginary part**.

But that’s as far as I’m going to go. We’ll assume that if you’re reading this chapter, you know what a complex number is and what you want to do with them.

And all we need to cover is C’s faculties for doing so.

Turns out, though, that complex number support in a compiler is an _optional_ feature. Not all compliant compilers can do it. And the ones that do, might do it to various degrees of completeness.

You can test if your system supports complex numbers with:
    
    
    [](complex-numbers.html#cb699-1)#ifdef __STDC_NO_COMPLEX__
    [](complex-numbers.html#cb699-2)#error Complex numbers not supported!
    [](complex-numbers.html#cb699-3)#endif

Furthermore, there is a macro that indicates adherence to the ISO 60559 (IEEE 754) standard for floating point math with complex numbers, as well as the presence of the `_Imaginary` type.
    
    
    [](complex-numbers.html#cb700-1)#if __STDC_IEC_559_COMPLEX__ != 1
    [](complex-numbers.html#cb700-2)#error Need IEC 60559 complex support!
    [](complex-numbers.html#cb700-3)#endif

More details on that are spelled out in Annex G in the C11 spec.

## 36.1 Complex Types

To use complex numbers, `#include <complex.h>`.

With that, you get at least two types:
    
    
    [](complex-numbers.html#cb701-1)_Complex
    [](complex-numbers.html#cb701-2)complex

Those both mean the same thing, so you might as well use the prettier `complex`.

You also get some types for imaginary numbers if you implementation is IEC 60559-compliant:
    
    
    [](complex-numbers.html#cb702-1)_Imaginary
    [](complex-numbers.html#cb702-2)imaginary

These also both mean the same thing, so you might as well use the prettier `imaginary`.

You also get values for the imaginary number \\(i\\), itself:
    
    
    [](complex-numbers.html#cb703-1)I
    [](complex-numbers.html#cb703-2)_Complex_I
    [](complex-numbers.html#cb703-3)_Imaginary_I

The macro `I` is set to `_Imaginary_I` (if available), or `_Complex_I`. So just use `I` for the imaginary number.

One aside: I’ve said that if a compiler has `__STDC_IEC_559_COMPLEX__` set to `1`, it must support `_Imaginary` types to be compliant. That’s my read of the spec. However, I don’t know of a single compiler that actually supports `_Imaginary` even though they have `__STDC_IEC_559_COMPLEX__` set. So I’m going to write some code with that type in here I have no way of testing. Sorry!

OK, so now we know there’s a `complex` type, how can we use it?

## 36.2 Assigning Complex Numbers

Since the complex number has a real and imaginary part, but both of them rely on floating point numbers to store values, we need to also tell C what precision to use for those parts of the complex number.

We do that by just pinning a `float`, `double`, or `long double` to the `complex`, either before or after it.

Let’s define a complex number that uses `float` for its components:
    
    
    [](complex-numbers.html#cb704-1)float complex c;   // Spec prefers this way
    [](complex-numbers.html#cb704-2)complex float c;   // Same thing--order doesn't matter

So that’s great for declarations, but how do we initialize them or assign to them?

Turns out we get to use some pretty natural notation. Example!
    
    
    [](complex-numbers.html#cb705-1)double complex x = 5 + 2*I;
    [](complex-numbers.html#cb705-2)double complex y = 10 + 3*I;

For \\(5+2i\\) and \\(10+3i\\), respectively.

## 36.3 Constructing, Deconstructing, and Printing

We’re getting there…

We’ve already seen one way to write a complex number:
    
    
    [](complex-numbers.html#cb706-1)double complex x = 5 + 2*I;

There’s also no problem using other floating point numbers to build it:
    
    
    [](complex-numbers.html#cb707-1)double a = 5;
    [](complex-numbers.html#cb707-2)double b = 2;
    [](complex-numbers.html#cb707-3)double complex x = a + b*I;

There is also a set of macros to help build these. The above code could be written using the `CMPLX()` macro, like so:
    
    
    [](complex-numbers.html#cb708-1)double complex x = CMPLX(5, 2);

As far as I can tell in my research, these are _almost_ equivalent:
    
    
    [](complex-numbers.html#cb709-1)double complex x = 5 + 2*I;
    [](complex-numbers.html#cb709-2)double complex x = CMPLX(5, 2);

But the `CMPLX()` macro will handle negative zeros in the imaginary part correctly every time, whereas the other way might convert them to positive zeros. I _think_[ 186](function-specifiers-alignment-specifiersoperators.html#fn186) This seems to imply that if there’s a chance the imaginary part will be zero, you should use the macro… but someone should correct me on this if I’m mistaken!

The `CMPLX()` macro works on `double` types. There are two other macros for `float` and `long double`: `CMPLXF()` and `CMPLXL()`. (These “f” and “l” suffixes appear in virtually all the complex-number-related functions.)

Now let’s try the reverse: if we have a complex number, how do we break it apart into its real and imaginary parts?

Here we have a couple functions that will extract the real and imaginary parts from the number: `creal()` and `cimag()`:
    
    
    [](complex-numbers.html#cb710-1)double complex x = 5 + 2*I;
    [](complex-numbers.html#cb710-2)double complex y = 10 + 3*I;
    [](complex-numbers.html#cb710-3)
    [](complex-numbers.html#cb710-4)printf("x = %f + %fi\n", creal(x), cimag(x));
    [](complex-numbers.html#cb710-5)printf("y = %f + %fi\n", creal(y), cimag(y));

for the output:
    
    
    [](complex-numbers.html#cb711-1)x = 5.000000 + 2.000000i
    [](complex-numbers.html#cb711-2)y = 10.000000 + 3.000000i

Note that the `i` I have in the `printf()` format string is a literal `i` that gets printed—it’s not part of the format specifier. Both return values from `creal()` and `cimag()` are `double`.

And as usual, there are `float` and `long double` variants of these functions: `crealf()`, `cimagf()`, `creall()`, and `cimagl()`.

## 36.4 Complex Arithmetic and Comparisons

Arithmetic can be performed on complex numbers, though how this works mathematically is beyond the scope of the guide.
    
    
    [](complex-numbers.html#cb712-1)#include <stdio.h>
    [](complex-numbers.html#cb712-2)#include <complex.h>
    [](complex-numbers.html#cb712-3)
    [](complex-numbers.html#cb712-4)int main(void)
    [](complex-numbers.html#cb712-5){
    [](complex-numbers.html#cb712-6)    double complex x = 1 + 2*I;
    [](complex-numbers.html#cb712-7)    double complex y = 3 + 4*I;
    [](complex-numbers.html#cb712-8)    double complex z;
    [](complex-numbers.html#cb712-9)
    [](complex-numbers.html#cb712-10)    z = x + y;
    [](complex-numbers.html#cb712-11)    printf("x + y = %f + %fi\n", creal(z), cimag(z));
    [](complex-numbers.html#cb712-12)
    [](complex-numbers.html#cb712-13)    z = x - y;
    [](complex-numbers.html#cb712-14)    printf("x - y = %f + %fi\n", creal(z), cimag(z));
    [](complex-numbers.html#cb712-15)
    [](complex-numbers.html#cb712-16)    z = x * y;
    [](complex-numbers.html#cb712-17)    printf("x * y = %f + %fi\n", creal(z), cimag(z));
    [](complex-numbers.html#cb712-18)
    [](complex-numbers.html#cb712-19)    z = x / y;
    [](complex-numbers.html#cb712-20)    printf("x / y = %f + %fi\n", creal(z), cimag(z));
    [](complex-numbers.html#cb712-21)}

for a result of:
    
    
    [](complex-numbers.html#cb713-1)x + y = 4.000000 + 6.000000i
    [](complex-numbers.html#cb713-2)x - y = -2.000000 + -2.000000i
    [](complex-numbers.html#cb713-3)x * y = -5.000000 + 10.000000i
    [](complex-numbers.html#cb713-4)x / y = 0.440000 + 0.080000i

You can also compare two complex numbers for equality (or inequality):
    
    
    [](complex-numbers.html#cb714-1)#include <stdio.h>
    [](complex-numbers.html#cb714-2)#include <complex.h>
    [](complex-numbers.html#cb714-3)
    [](complex-numbers.html#cb714-4)int main(void)
    [](complex-numbers.html#cb714-5){
    [](complex-numbers.html#cb714-6)    double complex x = 1 + 2*I;
    [](complex-numbers.html#cb714-7)    double complex y = 3 + 4*I;
    [](complex-numbers.html#cb714-8)
    [](complex-numbers.html#cb714-9)    printf("x == y = %d\n", x == y);  // 0
    [](complex-numbers.html#cb714-10)    printf("x != y = %d\n", x != y);  // 1
    [](complex-numbers.html#cb714-11)}

with the output:
    
    
    [](complex-numbers.html#cb715-1)x == y = 0
    [](complex-numbers.html#cb715-2)x != y = 1

They are equal if both components test equal. Note that as with all floating point, they could be equal if they’re close enough due to rounding error[187](function-specifiers-alignment-specifiersoperators.html#fn187).

## 36.5 Complex Math

But wait! There’s more than just simple complex arithmetic!

Here’s a summary table of all the math functions available to you with complex numbers.

I’m only going to list the `double` version of each function, but for all of them there is a `float` version that you can get by appending `f` to the function name, and a `long double` version that you can get by appending `l`.

For example, the `cabs()` function for computing the absolute value of a complex number also has `cabsf()` and `cabsl()` variants. I’m omitting them for brevity.

### 36.5.1 Trigonometry Functions

Function | Description  
---|---  
`ccos()` | Cosine  
`csin()` | Sine  
`ctan()` | Tangent  
`cacos()` | Arc cosine  
`casin()` | Arc sine  
`catan()` | Play _Settlers of Catan_  
`ccosh()` | Hyperbolic cosine  
`csinh()` | Hyperbolic sine  
`ctanh()` | Hyperbolic tangent  
`cacosh()` | Arc hyperbolic cosine  
`casinh()` | Arc hyperbolic sine  
`catanh()` | Arc hyperbolic tangent  
  
### 36.5.2 Exponential and Logarithmic Functions

Function | Description  
---|---  
`cexp()` | Base-\\(e\\) exponential  
`clog()` | Natural (base-\\(e\\)) logarithm  
  
### 36.5.3 Power and Absolute Value Functions

Function | Description  
---|---  
`cabs()` | Absolute value  
`cpow()` | Power  
`csqrt()` | Square root  
  
### 36.5.4 Manipulation Functions

Function | Description  
---|---  
`creal()` | Return real part  
`cimag()` | Return imaginary part  
`CMPLX()` | Construct a complex number  
`carg()` | Argument/phase angle  
`conj()` | Conjugate[188](function-specifiers-alignment-specifiersoperators.html#fn188)  
`cproj()` | Projection on Riemann sphere  
  
* * *

[Prev](incomplete-types.html) | [Contents](index.html) | [Next](fixed-width-integer-types.html)
