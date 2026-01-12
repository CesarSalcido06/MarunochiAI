# Beej's Guide to C Programming - Complete Reference

Source: https://beej.us/guide/bgc/
Downloaded: 2026-01-11

---

[Prev](index.html) | [Contents](index.html) | [Next](foreword.html)

* * *

# Beej's Guide to C Programming

Brian “Beej Jorgensen” Hall

v0.10.3, Copyright © January 8, 2026

  * [1 Foreword](foreword.html#foreword)
    * [1.1 Audience](foreword.html#audience)
    * [1.2 How to Read This Book](foreword.html#how-to-read-this-book)
    * [1.3 Platform and Compiler](foreword.html#platform-and-compiler)
    * [1.4 Official Homepage](foreword.html#official-homepage)
    * [1.5 Email Policy](foreword.html#email-policy)
    * [1.6 Mirroring](foreword.html#mirroring)
    * [1.7 Note for Translators](foreword.html#note-for-translators)
    * [1.8 Copyright and Distribution](foreword.html#copyright-and-distribution)
    * [1.9 Dedication](foreword.html#dedication)
  * [2 Hello, World!](hello-world.html#hello-world)
    * [2.1 What to Expect from C](hello-world.html#what-to-expect-from-c)
    * [2.2 Hello, World!](hello-world.html#hello-world-1)
    * [2.3 Compilation Details](hello-world.html#compilation-details)
    * [2.4 Building with `gcc`](hello-world.html#building-with-gcc)
    * [2.5 Building with `clang`](hello-world.html#building-with-clang)
    * [2.6 Building from IDEs](hello-world.html#building-from-ides)
    * [2.7 C Versions](hello-world.html#c-versions)
  * [3 Variables and Statements](variables-and-statements.html#variables-and-statements)
    * [3.1 Variables](variables-and-statements.html#variables)
      * [3.1.1 Variable Names](variables-and-statements.html#variable-names)
      * [3.1.2 Variable Types](variables-and-statements.html#variable-types)
      * [3.1.3 Boolean Types](variables-and-statements.html#boolean-types)
    * [3.2 Operators and Expressions](variables-and-statements.html#operators)
      * [3.2.1 Arithmetic](variables-and-statements.html#arithmetic)
      * [3.2.2 Ternary Operator](variables-and-statements.html#ternary-operator)
      * [3.2.3 Pre-and-Post Increment-and-Decrement](variables-and-statements.html#pre-and-post-increment-and-decrement)
      * [3.2.4 The Comma Operator](variables-and-statements.html#the-comma-operator)
      * [3.2.5 Conditional Operators](variables-and-statements.html#conditional-operators)
      * [3.2.6 Boolean Operators](variables-and-statements.html#boolean-operators)
      * [3.2.7 The `sizeof` Operator](variables-and-statements.html#sizeof-operator)
    * [3.3 Flow Control](variables-and-statements.html#flow-control)
      * [3.3.1 The `if`-`else` statement](variables-and-statements.html#ifstat)
      * [3.3.2 The `while` statement](variables-and-statements.html#whilestat)
      * [3.3.3 The `do-while` statement](variables-and-statements.html#dowhilestat)
      * [3.3.4 The `for` statement](variables-and-statements.html#forstat)
      * [3.3.5 The `switch` Statement](variables-and-statements.html#switch-statement)
  * [4 Functions](functions.html#functions)
    * [4.1 Passing by Value](functions.html#passvalue)
    * [4.2 Function Prototypes](functions.html#prototypes)
    * [4.3 Empty Parameter Lists](functions.html#empty-parameter-lists)
  * [5 Pointers—Cower In Fear!](pointers.html#pointers)
    * [5.1 Memory and Variables](pointers.html#ptmem)
    * [5.2 Pointer Types](pointers.html#pttypes)
    * [5.3 Dereferencing](pointers.html#deref)
    * [5.4 Passing Pointers as Arguments](pointers.html#ptpass)
    * [5.5 The `NULL` Pointer](pointers.html#the-null-pointer)
    * [5.6 A Note on Declaring Pointers](pointers.html#a-note-on-declaring-pointers)
    * [5.7 `sizeof` and Pointers](pointers.html#sizeof-and-pointers)
  * [6 Arrays](arrays.html#arrays)
    * [6.1 Easy Example](arrays.html#easy-example)
    * [6.2 Getting the Length of an Array](arrays.html#getting-the-length-of-an-array)
    * [6.3 Array Initializers](arrays.html#array-initializers)
    * [6.4 Out of Bounds!](arrays.html#out-of-bounds)
    * [6.5 Multidimensional Arrays](arrays.html#multidimensional-arrays)
    * [6.6 Arrays and Pointers](arrays.html#arrays-and-pointers)
      * [6.6.1 Getting a Pointer to an Array](arrays.html#getting-a-pointer-to-an-array)
      * [6.6.2 Passing Single Dimensional Arrays to Functions](arrays.html#passing1darrays)
      * [6.6.3 Changing Arrays in Functions](arrays.html#changing-arrays-in-functions)
      * [6.6.4 Passing Multidimensional Arrays to Functions](arrays.html#passing-multidimensional-arrays-to-functions)
  * [7 Strings](strings.html#strings)
    * [7.1 String Literals](strings.html#string-literals)
    * [7.2 String Variables](strings.html#string-variables)
    * [7.3 String Variables as Arrays](strings.html#string-variables-as-arrays)
    * [7.4 String Initializers](strings.html#string-initializers)
    * [7.5 Getting String Length](strings.html#getting-string-length)
    * [7.6 String Termination](strings.html#string-termination)
    * [7.7 Copying a String](strings.html#copying-a-string)
  * [8 Structs](structs.html#structs)
    * [8.1 Declaring a Struct](structs.html#declaring-a-struct)
    * [8.2 Struct Initializers](structs.html#struct-initializers)
    * [8.3 Passing Structs to Functions](structs.html#passing-structs-to-functions)
    * [8.4 The Arrow Operator](structs.html#the-arrow-operator)
    * [8.5 Copying and Returning `struct`s](structs.html#copying-and-returning-structs)
    * [8.6 Comparing `struct`s](structs.html#comparing-structs)
  * [9 File Input/Output](file-inputoutput.html#file-inputoutput)
    * [9.1 The `FILE*` Data Type](file-inputoutput.html#the-file-data-type)
    * [9.2 Reading Text Files](file-inputoutput.html#reading-text-files)
    * [9.3 End of File: `EOF`](file-inputoutput.html#end-of-file-eof)
      * [9.3.1 Reading a Line at a Time](file-inputoutput.html#reading-a-line-at-a-time)
    * [9.4 Formatted Input](file-inputoutput.html#formatted-input)
    * [9.5 Writing Text Files](file-inputoutput.html#writing-text-files)
    * [9.6 Binary File I/O](file-inputoutput.html#binary-file-io)
      * [9.6.1 `struct` and Number Caveats](file-inputoutput.html#struct-and-number-caveats)
  * [10 `typedef`: Making New Types](typedef-making-new-types.html#typedef-making-new-types)
    * [10.1 `typedef` in Theory](typedef-making-new-types.html#typedef-in-theory)
      * [10.1.1 Scoping](typedef-making-new-types.html#scoping)
    * [10.2 `typedef` in Practice](typedef-making-new-types.html#typedef-in-practice)
      * [10.2.1 `typedef` and `struct`s](typedef-making-new-types.html#typedef-struct)
      * [10.2.2 `typedef` and Other Types](typedef-making-new-types.html#typedef-and-other-types)
      * [10.2.3 `typedef` and Pointers](typedef-making-new-types.html#typedef-and-pointers)
      * [10.2.4 `typedef` and Capitalization](typedef-making-new-types.html#typedef-and-capitalization)
    * [10.3 Arrays and `typedef`](typedef-making-new-types.html#arrays-and-typedef)
  * [11 Pointers II: Arithmetic](pointers2.html#pointers2)
    * [11.1 Pointer Arithmetic](pointers2.html#pointer-arithmetic)
      * [11.1.1 Adding to Pointers](pointers2.html#adding-to-pointers)
      * [11.1.2 Changing Pointers](pointers2.html#changing-pointers)
      * [11.1.3 Subtracting Pointers](pointers2.html#subtracting-pointers)
    * [11.2 Array/Pointer Equivalence](pointers2.html#arraypointerequiv)
      * [11.2.1 Array/Pointer Equivalence in Function Calls](pointers2.html#arraypointer-equivalence-in-function-calls)
    * [11.3 `void` Pointers](pointers2.html#void-pointers)
  * [12 Manual Memory Allocation](manual-memory-allocation.html#manual-memory-allocation)
    * [12.1 Allocating and Deallocating, `malloc()` and `free()`](manual-memory-allocation.html#allocating-and-deallocating-malloc-and-free)
    * [12.2 Error Checking](manual-memory-allocation.html#error-checking)
    * [12.3 Allocating Space for an Array](manual-memory-allocation.html#allocating-space-for-an-array)
    * [12.4 An Alternative: `calloc()`](manual-memory-allocation.html#an-alternative-calloc)
    * [12.5 Changing Allocated Size with `realloc()`](manual-memory-allocation.html#changing-allocated-size-with-realloc)
      * [12.5.1 Reading in Lines of Arbitrary Length](manual-memory-allocation.html#reading-in-lines-of-arbitrary-length)
      * [12.5.2 `realloc()` with `NULL`](manual-memory-allocation.html#realloc-with-null)
    * [12.6 Aligned Allocations](manual-memory-allocation.html#aligned-allocations)
  * [13 Scope](scope.html#scope)
    * [13.1 Block Scope](scope.html#block-scope)
      * [13.1.1 Where To Define Variables](scope.html#where-to-define-variables)
      * [13.1.2 Variable Hiding](scope.html#variable-hiding)
    * [13.2 File Scope](scope.html#file-scope)
    * [13.3 `for`-loop Scope](scope.html#for-loop-scope)
    * [13.4 A Note on Function Scope](scope.html#a-note-on-function-scope)
  * [14 Types II: Way More Types!](types-ii-way-more-types.html#types-ii-way-more-types)
    * [14.1 Signed and Unsigned Integers](types-ii-way-more-types.html#signed-and-unsigned-integers)
    * [14.2 Character Types](types-ii-way-more-types.html#character-types)
    * [14.3 More Integer Types: `short`, `long`, `long long`](types-ii-way-more-types.html#more-integer-types-short-long-long-long)
    * [14.4 More Float: `double` and `long double`](types-ii-way-more-types.html#more-float-double-and-long-double)
      * [14.4.1 How Many Decimal Digits?](types-ii-way-more-types.html#how-many-decimal-digits)
      * [14.4.2 Converting to Decimal and Back](types-ii-way-more-types.html#converting-to-decimal-and-back)
    * [14.5 Constant Numeric Types](types-ii-way-more-types.html#constant-numeric-types)
      * [14.5.1 Hexadecimal and Octal](types-ii-way-more-types.html#hexadecimal-and-octal)
      * [14.5.2 Integer Constants](types-ii-way-more-types.html#integer-constants)
      * [14.5.3 Floating Point Constants](types-ii-way-more-types.html#floating-point-constants)
  * [15 Types III: Conversions](types-iii-conversions.html#types-iii-conversions)
    * [15.1 String Conversions](types-iii-conversions.html#string-conversions)
      * [15.1.1 Numeric Value to String](types-iii-conversions.html#numeric-value-to-string)
      * [15.1.2 String to Numeric Value](types-iii-conversions.html#string-to-numeric-value)
    * [15.2 `char` Conversions](types-iii-conversions.html#char-conversions)
    * [15.3 Numeric Conversions](types-iii-conversions.html#numeric-conversions)
      * [15.3.1 Boolean](types-iii-conversions.html#boolean)
      * [15.3.2 Integer to Integer Conversions](types-iii-conversions.html#integer-to-integer-conversions)
      * [15.3.3 Integer and Floating Point Conversions](types-iii-conversions.html#integer-and-floating-point-conversions)
    * [15.4 Implicit Conversions](types-iii-conversions.html#implicit-conversions)
      * [15.4.1 The Integer Promotions](types-iii-conversions.html#integer-promotions)
      * [15.4.2 The Usual Arithmetic Conversions](types-iii-conversions.html#usual-arithmetic-conversions)
      * [15.4.3 `void*`](types-iii-conversions.html#void)
    * [15.5 Explicit Conversions](types-iii-conversions.html#explicit-conversions)
      * [15.5.1 Casting](types-iii-conversions.html#casting)
  * [16 Types IV: Qualifiers and Specifiers](types-iv-qualifiers-and-specifiers.html#types-iv-qualifiers-and-specifiers)
    * [16.1 Type Qualifiers](types-iv-qualifiers-and-specifiers.html#type-qualifiers)
      * [16.1.1 `const`](types-iv-qualifiers-and-specifiers.html#const)
      * [16.1.2 `restrict`](types-iv-qualifiers-and-specifiers.html#restrict)
      * [16.1.3 `volatile`](types-iv-qualifiers-and-specifiers.html#volatile)
      * [16.1.4 `_Atomic`](types-iv-qualifiers-and-specifiers.html#atomic)
    * [16.2 Storage-Class Specifiers](types-iv-qualifiers-and-specifiers.html#storage-class-specifiers)
      * [16.2.1 `auto`](types-iv-qualifiers-and-specifiers.html#auto)
      * [16.2.2 `static`](types-iv-qualifiers-and-specifiers.html#static)
      * [16.2.3 `extern`](types-iv-qualifiers-and-specifiers.html#extern)
      * [16.2.4 `register`](types-iv-qualifiers-and-specifiers.html#register)
      * [16.2.5 `_Thread_local`](types-iv-qualifiers-and-specifiers.html#thread_local)
  * [17 Multifile Projects](multifile-projects.html#multifile-projects)
    * [17.1 Includes and Function Prototypes](multifile-projects.html#includes-func-protos)
    * [17.2 Dealing with Repeated Includes](multifile-projects.html#dealing-with-repeated-includes)
    * [17.3 `static` and `extern`](multifile-projects.html#static-and-extern)
    * [17.4 Compiling with Object Files](multifile-projects.html#compiling-with-object-files)
  * [18 The Outside Environment](the-outside-environment.html#the-outside-environment)
    * [18.1 Command Line Arguments](the-outside-environment.html#command-line-arguments)
      * [18.1.1 The Last `argv` is `NULL`](the-outside-environment.html#the-last-argv-is-null)
      * [18.1.2 The Alternate: `char **argv`](the-outside-environment.html#the-alternate-char-argv)
      * [18.1.3 Fun Facts](the-outside-environment.html#fun-facts)
    * [18.2 Exit Status](the-outside-environment.html#exit-status)
      * [18.2.1 Other Exit Status Values](the-outside-environment.html#other-exit-status-values)
    * [18.3 Environment Variables](the-outside-environment.html#env-var)
      * [18.3.1 Setting Environment Variables](the-outside-environment.html#setting-environment-variables)
      * [18.3.2 Unix-like Alternative Environment Variables](the-outside-environment.html#unix-like-alternative-environment-variables)
  * [19 The C Preprocessor](the-c-preprocessor.html#the-c-preprocessor)
    * [19.1 `#include`](the-c-preprocessor.html#include)
    * [19.2 Simple Macros](the-c-preprocessor.html#simple-macros)
    * [19.3 Conditional Compilation](the-c-preprocessor.html#conditional-compilation)
      * [19.3.1 If Defined, `#ifdef` and `#endif`](the-c-preprocessor.html#if-defined-ifdef-and-endif)
      * [19.3.2 If Not Defined, `#ifndef`](the-c-preprocessor.html#if-not-defined-ifndef)
      * [19.3.3 `#else`](the-c-preprocessor.html#else)
      * [19.3.4 Else-If: `#elifdef`, `#elifndef`](the-c-preprocessor.html#else-if-elifdef-elifndef)
      * [19.3.5 General Conditional: `#if`, `#elif`](the-c-preprocessor.html#general-conditional-if-elif)
      * [19.3.6 Losing a Macro: `#undef`](the-c-preprocessor.html#losing-a-macro-undef)
    * [19.4 Built-in Macros](the-c-preprocessor.html#built-in-macros)
      * [19.4.1 Mandatory Macros](the-c-preprocessor.html#mandatory-macros)
      * [19.4.2 Optional Macros](the-c-preprocessor.html#optional-macros)
    * [19.5 Macros with Arguments](the-c-preprocessor.html#macros-with-arguments)
      * [19.5.1 Macros with One Argument](the-c-preprocessor.html#macros-with-one-argument)
      * [19.5.2 Macros with More than One Argument](the-c-preprocessor.html#macros-with-more-than-one-argument)
      * [19.5.3 Macros with Variable Arguments](the-c-preprocessor.html#macros-with-variable-arguments)
      * [19.5.4 Stringification](the-c-preprocessor.html#stringification)
      * [19.5.5 Concatenation](the-c-preprocessor.html#concatenation)
    * [19.6 Multiline Macros](the-c-preprocessor.html#multiline-macros)
    * [19.7 Example: An Assert Macro](the-c-preprocessor.html#my-assert)
    * [19.8 The `#error` Directive](the-c-preprocessor.html#the-error-directive)
    * [19.9 The `#embed` Directive](the-c-preprocessor.html#the-embed-directive)
      * [19.9.1 `#embed` Parameters](the-c-preprocessor.html#embed-parameters)
      * [19.9.2 The `limit()` Parameter](the-c-preprocessor.html#the-limit-parameter)
      * [19.9.3 The `if_empty` Parameter](the-c-preprocessor.html#the-if_empty-parameter)
      * [19.9.4 The `prefix()` and `suffix()` Parameters](the-c-preprocessor.html#the-prefix-and-suffix-parameters)
      * [19.9.5 The `__has_embed()` Identifier](the-c-preprocessor.html#the-__has_embed-identifier)
      * [19.9.6 Other Parameters](the-c-preprocessor.html#other-parameters)
      * [19.9.7 Embedding Multi-Byte Values](the-c-preprocessor.html#embedding-multi-byte-values)
    * [19.10 The `#pragma` Directive](the-c-preprocessor.html#pragma)
      * [19.10.1 Non-Standard Pragmas](the-c-preprocessor.html#non-standard-pragmas)
      * [19.10.2 Standard Pragmas](the-c-preprocessor.html#standard-pragmas)
      * [19.10.3 `_Pragma` Operator](the-c-preprocessor.html#pragma-operator)
    * [19.11 The `#line` Directive](the-c-preprocessor.html#the-line-directive)
    * [19.12 The Null Directive](the-c-preprocessor.html#the-null-directive)
  * [20 `struct`s II: More Fun with `struct`s](structs-ii-more-fun-with-structs.html#structs-ii-more-fun-with-structs)
    * [20.1 Initializers of Nested `struct`s and Arrays](structs-ii-more-fun-with-structs.html#initializers-of-nested-structs-and-arrays)
    * [20.2 Anonymous `struct`s](structs-ii-more-fun-with-structs.html#anonymous-structs)
    * [20.3 Self-Referential `struct`s](structs-ii-more-fun-with-structs.html#self-referential-structs)
    * [20.4 Flexible Array Members](structs-ii-more-fun-with-structs.html#flexible-array-members)
    * [20.5 Padding Bytes](structs-ii-more-fun-with-structs.html#struct-padding-bytes)
    * [20.6 `offsetof`](structs-ii-more-fun-with-structs.html#offsetof)
    * [20.7 Fake OOP](structs-ii-more-fun-with-structs.html#fake-oop)
    * [20.8 Bit-Fields](structs-ii-more-fun-with-structs.html#bit-fields)
      * [20.8.1 Non-Adjacent Bit-Fields](structs-ii-more-fun-with-structs.html#non-adjacent-bit-fields)
      * [20.8.2 Signed or Unsigned `int`s](structs-ii-more-fun-with-structs.html#signed-or-unsigned-ints)
      * [20.8.3 Unnamed Bit-Fields](structs-ii-more-fun-with-structs.html#unnamed-bit-fields)
      * [20.8.4 Zero-Width Unnamed Bit-Fields](structs-ii-more-fun-with-structs.html#zero-width-unnamed-bit-fields)
    * [20.9 Unions](structs-ii-more-fun-with-structs.html#unions)
      * [20.9.1 Unions and Type Punning](structs-ii-more-fun-with-structs.html#union-type-punning)
      * [20.9.2 Pointers to `union`s](structs-ii-more-fun-with-structs.html#pointers-to-unions)
      * [20.9.3 Common Initial Sequences in Unions](structs-ii-more-fun-with-structs.html#common-initial-sequences-in-unions)
    * [20.10 Unions and Unnamed Structs](structs-ii-more-fun-with-structs.html#unions-and-unnamed-structs)
    * [20.11 Passing and Returning `struct`s and `union`s](structs-ii-more-fun-with-structs.html#passing-and-returning-structs-and-unions)
  * [21 Characters and Strings II](characters-and-strings-ii.html#characters-and-strings-ii)
    * [21.1 Escape Sequences](characters-and-strings-ii.html#escape-sequences)
      * [21.1.1 Frequently-used Escapes](characters-and-strings-ii.html#frequently-used-escapes)
      * [21.1.2 Rarely-used Escapes](characters-and-strings-ii.html#rarely-used-escapes)
      * [21.1.3 Numeric Escapes](characters-and-strings-ii.html#numeric-escapes)
  * [22 Enumerated Types: `enum`](enumerated-types-enum.html#enumerated-types-enum)
    * [22.1 Behavior of `enum`](enumerated-types-enum.html#behavior-of-enum)
      * [22.1.1 Numbering](enumerated-types-enum.html#numbering)
      * [22.1.2 Trailing Commas](enumerated-types-enum.html#trailing-commas)
      * [22.1.3 Scope](enumerated-types-enum.html#scope-1)
      * [22.1.4 Style](enumerated-types-enum.html#style)
    * [22.2 Your `enum` is a Type](enumerated-types-enum.html#your-enum-is-a-type)
  * [23 Pointers III: Pointers to Pointers and More](pointers-iii-pointers-to-pointers-and-more.html#pointers-iii-pointers-to-pointers-and-more)
    * [23.1 Pointers to Pointers](pointers-iii-pointers-to-pointers-and-more.html#pointers-to-pointers)
      * [23.1.1 Pointer Pointers and `const`](pointers-iii-pointers-to-pointers-and-more.html#pointer-pointers-and-const)
    * [23.2 Multibyte Values](pointers-iii-pointers-to-pointers-and-more.html#multibyte-values)
    * [23.3 The `NULL` Pointer and Zero](pointers-iii-pointers-to-pointers-and-more.html#the-null-pointer-and-zero)
    * [23.4 Pointers as Integers](pointers-iii-pointers-to-pointers-and-more.html#pointers-as-integers)
    * [23.5 Casting Pointers to other Pointers](pointers-iii-pointers-to-pointers-and-more.html#casting-pointers-to-other-pointers)
    * [23.6 Pointer Differences](pointers-iii-pointers-to-pointers-and-more.html#ptr_differences)
    * [23.7 Pointers to Functions](pointers-iii-pointers-to-pointers-and-more.html#pointers-to-functions)
  * [24 Bitwise Operations](bitwise-operations.html#bitwise-operations)
    * [24.1 Bitwise AND, OR, XOR, and NOT](bitwise-operations.html#bitwise-and-or-xor-and-not)
    * [24.2 Bitwise Shift](bitwise-operations.html#bitwise-shift)
  * [25 Variadic Functions](variadic-functions.html#variadic-functions)
    * [25.1 Ellipses in Function Signatures](variadic-functions.html#ellipses-in-function-signatures)
    * [25.2 Getting the Extra Arguments](variadic-functions.html#getting-the-extra-arguments)
    * [25.3 `va_list` Functionality](variadic-functions.html#va_list-functionality)
    * [25.4 Library Functions That Use `va_list`s](variadic-functions.html#library-functions-that-use-va_lists)
    * [25.5 Variadic Macro Gotchas](variadic-functions.html#variadic-macro-gotchas)
  * [26 Locale and Internationalization](locale-and-internationalization.html#locale-and-internationalization)
    * [26.1 Setting the Localization, Quick and Dirty](locale-and-internationalization.html#setting-the-localization-quick-and-dirty)
    * [26.2 Getting the Monetary Locale Settings](locale-and-internationalization.html#getting-the-monetary-locale-settings)
      * [26.2.1 Monetary Digit Grouping](locale-and-internationalization.html#monetary-digit-grouping)
      * [26.2.2 Separators and Sign Position](locale-and-internationalization.html#separators-and-sign-position)
      * [26.2.3 Example Values](locale-and-internationalization.html#example-values)
    * [26.3 Localization Specifics](locale-and-internationalization.html#localization-specifics)
  * [27 Unicode, Wide Characters, and All That](unicode-wide-characters-and-all-that.html#unicode-wide-characters-and-all-that)
    * [27.1 What is Unicode?](unicode-wide-characters-and-all-that.html#what-is-unicode)
    * [27.2 Code Points](unicode-wide-characters-and-all-that.html#code-points)
    * [27.3 Encoding](unicode-wide-characters-and-all-that.html#encoding)
    * [27.4 Source and Execution Character Sets](unicode-wide-characters-and-all-that.html#src-exec-charset)
    * [27.5 Unicode in C](unicode-wide-characters-and-all-that.html#unicode-in-c)
    * [27.6 A Quick Note on UTF-8 Before We Swerve into the Weeds](unicode-wide-characters-and-all-that.html#utf8-quick)
    * [27.7 Different Character Types](unicode-wide-characters-and-all-that.html#different-character-types)
      * [27.7.1 Multibyte Characters](unicode-wide-characters-and-all-that.html#multibyte-characters)
      * [27.7.2 Wide Characters](unicode-wide-characters-and-all-that.html#wide-characters)
    * [27.8 Using Wide Characters and `wchar_t`](unicode-wide-characters-and-all-that.html#using-wide-characters-and-wchar_t)
      * [27.8.1 Multibyte to `wchar_t` Conversions](unicode-wide-characters-and-all-that.html#multibyte-to-wchar_t-conversions)
    * [27.9 Wide Character Functionality](unicode-wide-characters-and-all-that.html#wide-character-functionality)
      * [27.9.1 `wint_t`](unicode-wide-characters-and-all-that.html#wint_t)
      * [27.9.2 I/O Stream Orientation](unicode-wide-characters-and-all-that.html#io-stream-orientation)
      * [27.9.3 I/O Functions](unicode-wide-characters-and-all-that.html#io-functions)
      * [27.9.4 Type Conversion Functions](unicode-wide-characters-and-all-that.html#type-conversion-functions)
      * [27.9.5 String and Memory Copying Functions](unicode-wide-characters-and-all-that.html#string-and-memory-copying-functions)
      * [27.9.6 String and Memory Comparing Functions](unicode-wide-characters-and-all-that.html#string-and-memory-comparing-functions)
      * [27.9.7 String Searching Functions](unicode-wide-characters-and-all-that.html#string-searching-functions)
      * [27.9.8 Length/Miscellaneous Functions](unicode-wide-characters-and-all-that.html#lengthmiscellaneous-functions)
      * [27.9.9 Character Classification Functions](unicode-wide-characters-and-all-that.html#character-classification-functions)
    * [27.10 Parse State, Restartable Functions](unicode-wide-characters-and-all-that.html#parse-state-restartable-functions)
    * [27.11 Unicode Encodings and C](unicode-wide-characters-and-all-that.html#unicode-encodings-and-c)
      * [27.11.1 UTF-8](unicode-wide-characters-and-all-that.html#utf-8)
      * [27.11.2 UTF-16, UTF-32, `char16_t`, and `char32_t`](unicode-wide-characters-and-all-that.html#utf-16-utf-32-char16_t-and-char32_t)
      * [27.11.3 Multibyte Conversions](unicode-wide-characters-and-all-that.html#multibyte-conversions)
      * [27.11.4 Third-Party Libraries](unicode-wide-characters-and-all-that.html#utf-3rd-party)
  * [28 Exiting a Program](exiting-a-program.html#exiting-a-program)
    * [28.1 Normal Exits](exiting-a-program.html#normal-exits)
      * [28.1.1 Returning From `main()`](exiting-a-program.html#returning-from-main)
      * [28.1.2 `exit()`](exiting-a-program.html#exit)
      * [28.1.3 Setting Up Exit Handlers with `atexit()`](exiting-a-program.html#setting-up-exit-handlers-with-atexit)
    * [28.2 Quicker Exits with `quick_exit()`](exiting-a-program.html#quicker-exits-with-quick_exit)
    * [28.3 Nuke it from Orbit: `_Exit()`](exiting-a-program.html#nuke-it-from-orbit-_exit)
    * [28.4 Exiting Sometimes: `assert()`](exiting-a-program.html#exiting-sometimes-assert)
    * [28.5 Abnormal Exit: `abort()`](exiting-a-program.html#abnormal-exit-abort)
  * [29 Signal Handling](signal-handling.html#signal-handling)
    * [29.1 What Are Signals?](signal-handling.html#what-are-signals)
    * [29.2 Handling Signals with `signal()`](signal-handling.html#handling-signals-with-signal)
    * [29.3 Writing Signal Handlers](signal-handling.html#writing-signal-handlers)
    * [29.4 What Can We Actually Do?](signal-handling.html#what-can-we-actually-do)
    * [29.5 Friends Don’t Let Friends `signal()`](signal-handling.html#friends-dont-let-friends-signal)
  * [30 Variable-Length Arrays (VLAs)](variable-length-arrays-vlas.html#variable-length-arrays-vlas)
    * [30.1 The Basics](variable-length-arrays-vlas.html#the-basics)
    * [30.2 `sizeof` and VLAs](variable-length-arrays-vlas.html#sizeof-and-vlas)
    * [30.3 Multidimensional VLAs](variable-length-arrays-vlas.html#multidimensional-vlas)
    * [30.4 Passing One-Dimensional VLAs to Functions](variable-length-arrays-vlas.html#passing-one-dimensional-vlas-to-functions)
    * [30.5 Passing Multi-Dimensional VLAs to Functions](variable-length-arrays-vlas.html#passing-multi-dimensional-vlas-to-functions)
      * [30.5.1 Partial Multidimensional VLAs](variable-length-arrays-vlas.html#partial-multidimensional-vlas)
    * [30.6 Compatibility with Regular Arrays](variable-length-arrays-vlas.html#compatibility-with-regular-arrays)
    * [30.7 `typedef` and VLAs](variable-length-arrays-vlas.html#typedef-and-vlas)
    * [30.8 Jumping Pitfalls](variable-length-arrays-vlas.html#jumping-pitfalls)
    * [30.9 General Issues](variable-length-arrays-vlas.html#vla-general-issues)
  * [31 `goto`](goto.html#goto)
    * [31.1 A Simple Example](goto.html#a-simple-example)
    * [31.2 Labeled `continue`](goto.html#labeled-continue)
    * [31.3 Bailing Out](goto.html#bailing-out)
    * [31.4 Labeled `break`](goto.html#labeled-break)
    * [31.5 Multi-level Cleanup](goto.html#multi-level-cleanup)
    * [31.6 Tail Call Optimization](goto.html#tail-call-optimization)
    * [31.7 Restarting Interrupted System Calls](goto.html#restarting-interrupted-system-calls)
    * [31.8 `goto` and Thread Preemption](goto.html#goto-and-thread-preemption)
    * [31.9 `goto` and Variable Scope](goto.html#goto-and-variable-scope)
    * [31.10 `goto` and Variable-Length Arrays](goto.html#goto-and-variable-length-arrays)
  * [32 Types Part V: Compound Literals and Generic Selections](types-part-v-compound-literals-and-generic-selections.html#types-part-v-compound-literals-and-generic-selections)
    * [32.1 Compound Literals](types-part-v-compound-literals-and-generic-selections.html#compound-literals)
      * [32.1.1 Passing Unnamed Objects to Functions](types-part-v-compound-literals-and-generic-selections.html#passing-unnamed-objects-to-functions)
      * [32.1.2 Unnamed `struct`s](types-part-v-compound-literals-and-generic-selections.html#unnamed-structs)
      * [32.1.3 Pointers to Unnamed Objects](types-part-v-compound-literals-and-generic-selections.html#pointers-to-unnamed-objects)
      * [32.1.4 Unnamed Objects and Scope](types-part-v-compound-literals-and-generic-selections.html#unnamed-objects-and-scope)
      * [32.1.5 Silly Unnamed Object Example](types-part-v-compound-literals-and-generic-selections.html#silly-unnamed-object-example)
    * [32.2 Generic Selections](types-part-v-compound-literals-and-generic-selections.html#type-generics)
  * [33 Arrays Part II](arrays-part-ii.html#arrays-part-ii)
    * [33.1 Type Qualifiers for Arrays in Parameter Lists](arrays-part-ii.html#type-qualifiers-for-arrays-in-parameter-lists)
    * [33.2 `static` for Arrays in Parameter Lists](arrays-part-ii.html#static-for-arrays-in-parameter-lists)
    * [33.3 Equivalent Initializers](arrays-part-ii.html#equivalent-initializers)
  * [34 Long Jumps with `setjmp`, `longjmp`](setjmp-longjmp.html#setjmp-longjmp)
    * [34.1 Using `setjmp` and `longjmp`](setjmp-longjmp.html#using-setjmp-and-longjmp)
    * [34.2 Pitfalls](setjmp-longjmp.html#pitfalls)
      * [34.2.1 The Values of Local Variables](setjmp-longjmp.html#the-values-of-local-variables)
      * [34.2.2 How Much State is Saved?](setjmp-longjmp.html#how-much-state-is-saved)
      * [34.2.3 You Can’t Name Anything `setjmp`](setjmp-longjmp.html#you-cant-name-anything-setjmp)
      * [34.2.4 You Can’t `setjmp()` in a Larger Expression](setjmp-longjmp.html#you-cant-setjmp-in-a-larger-expression)
      * [34.2.5 When Can’t You `longjmp()`?](setjmp-longjmp.html#when-cant-you-longjmp)
      * [34.2.6 You Can’t Pass `0` to `longjmp()`](setjmp-longjmp.html#you-cant-pass-0-to-longjmp)
      * [34.2.7 `longjmp()` and Variable Length Arrays](setjmp-longjmp.html#longjmp-and-variable-length-arrays)
  * [35 Incomplete Types](incomplete-types.html#incomplete-types)
    * [35.1 Use Case: Self-Referential Structures](incomplete-types.html#use-case-self-referential-structures)
    * [35.2 Incomplete Type Error Messages](incomplete-types.html#incomplete-type-error-messages)
    * [35.3 Other Incomplete Types](incomplete-types.html#other-incomplete-types)
    * [35.4 Use Case: Arrays in Header Files](incomplete-types.html#use-case-arrays-in-header-files)
    * [35.5 Completing Incomplete Types](incomplete-types.html#completing-incomplete-types)
  * [36 Complex Numbers](complex-numbers.html#complex-numbers)
    * [36.1 Complex Types](complex-numbers.html#complex-types)
    * [36.2 Assigning Complex Numbers](complex-numbers.html#assigning-complex-numbers)
    * [36.3 Constructing, Deconstructing, and Printing](complex-numbers.html#constructing-deconstructing-and-printing)
    * [36.4 Complex Arithmetic and Comparisons](complex-numbers.html#complex-arithmetic-and-comparisons)
    * [36.5 Complex Math](complex-numbers.html#complex-math)
      * [36.5.1 Trigonometry Functions](complex-numbers.html#trigonometry-functions)
      * [36.5.2 Exponential and Logarithmic Functions](complex-numbers.html#exponential-and-logarithmic-functions)
      * [36.5.3 Power and Absolute Value Functions](complex-numbers.html#power-and-absolute-value-functions)
      * [36.5.4 Manipulation Functions](complex-numbers.html#manipulation-functions)
  * [37 Fixed Width Integer Types](fixed-width-integer-types.html#fixed-width-integer-types)
    * [37.1 The Bit-Sized Types](fixed-width-integer-types.html#the-bit-sized-types)
    * [37.2 Maximum Integer Size Type](fixed-width-integer-types.html#maximum-integer-size-type)
    * [37.3 Using Fixed Size Constants](fixed-width-integer-types.html#using-fixed-size-constants)
    * [37.4 Limits of Fixed Size Integers](fixed-width-integer-types.html#limits-of-fixed-size-integers)
    * [37.5 Format Specifiers](fixed-width-integer-types.html#format-specifiers)
  * [38 Date and Time Functionality](date-and-time-functionality.html#date-and-time-functionality)
    * [38.1 Quick Terminology and Information](date-and-time-functionality.html#quick-terminology-and-information)
    * [38.2 Date Types](date-and-time-functionality.html#date-types)
    * [38.3 Initialization and Conversion Between Types](date-and-time-functionality.html#initialization-and-conversion-between-types)
      * [38.3.1 Converting `time_t` to `struct tm`](date-and-time-functionality.html#converting-time_t-to-struct-tm)
      * [38.3.2 Converting `struct tm` to `time_t`](date-and-time-functionality.html#converting-struct-tm-to-time_t)
    * [38.4 Formatted Date Output](date-and-time-functionality.html#formatted-date-output)
    * [38.5 More Resolution with `timespec_get()`](date-and-time-functionality.html#more-resolution-with-timespec_get)
    * [38.6 Differences Between Times](date-and-time-functionality.html#differences-between-times)
  * [39 Multithreading](multithreading.html#multithreading)
    * [39.1 Background](multithreading.html#background)
    * [39.2 Things You Can Do](multithreading.html#things-you-can-do)
    * [39.3 Data Races and the Standard Library](multithreading.html#data-races-and-the-standard-library)
    * [39.4 Creating and Waiting for Threads](multithreading.html#creating-and-waiting-for-threads)
    * [39.5 Detaching Threads](multithreading.html#detaching-threads)
    * [39.6 Thread Local Data](multithreading.html#thread-local-data)
      * [39.6.1 `_Thread_local` Storage-Class](multithreading.html#thread-local)
      * [39.6.2 Another Option: Thread-Specific Storage](multithreading.html#another-option-thread-specific-storage)
    * [39.7 Mutexes](multithreading.html#mutex)
      * [39.7.1 Different Mutex Types](multithreading.html#different-mutex-types)
    * [39.8 Condition Variables](multithreading.html#condition-variables)
      * [39.8.1 Timed Condition Wait](multithreading.html#timed-condition-wait)
      * [39.8.2 Broadcast: Wake Up All Waiting Threads](multithreading.html#broadcast-wake-up-all-waiting-threads)
    * [39.9 Running a Function One Time](multithreading.html#running-a-function-one-time)
  * [40 Atomics](chapter-atomics.html#chapter-atomics)
    * [40.1 Testing for Atomic Support](chapter-atomics.html#testing-for-atomic-support)
    * [40.2 Atomic Variables](chapter-atomics.html#atomic-variables)
    * [40.3 Synchronization](chapter-atomics.html#synchronization)
    * [40.4 Acquire and Release](chapter-atomics.html#acquire-and-release)
    * [40.5 Sequential Consistency](chapter-atomics.html#sequential-consistency)
    * [40.6 Atomic Assignments and Operators](chapter-atomics.html#atomic-assignments-and-operators)
    * [40.7 Library Functions that Automatically Synchronize](chapter-atomics.html#library-functions-that-automatically-synchronize)
    * [40.8 Atomic Type Specifier, Qualifier](chapter-atomics.html#atomic-type-specifier-qualifier)
    * [40.9 Lock-Free Atomic Variables](chapter-atomics.html#lock-free-atomic)
      * [40.9.1 Signal Handlers and Lock-Free Atomics](chapter-atomics.html#signal-handlers-and-lock-free-atomics)
    * [40.10 Atomic Flags](chapter-atomics.html#atomic-flags)
    * [40.11 Atomic `struct`s and `union`s](chapter-atomics.html#atomic-structs-and-unions)
    * [40.12 Atomic Pointers](chapter-atomics.html#atomic-pointers)
    * [40.13 Memory Order](chapter-atomics.html#memory-order)
      * [40.13.1 Sequential Consistency](chapter-atomics.html#sequential-consistency-1)
      * [40.13.2 Acquire](chapter-atomics.html#acquire)
      * [40.13.3 Release](chapter-atomics.html#release)
      * [40.13.4 Consume](chapter-atomics.html#consume)
      * [40.13.5 Acquire/Release](chapter-atomics.html#acquirerelease)
      * [40.13.6 Relaxed](chapter-atomics.html#relaxed)
    * [40.14 Fences](chapter-atomics.html#fences)
    * [40.15 References](chapter-atomics.html#references)
  * [41 Function Specifiers, Alignment Specifiers/Operators](function-specifiers-alignment-specifiersoperators.html#function-specifiers-alignment-specifiersoperators)
    * [41.1 Function Specifiers](function-specifiers-alignment-specifiersoperators.html#function-specifiers)
      * [41.1.1 `inline` for Speed—Maybe](function-specifiers-alignment-specifiersoperators.html#inline-for-speedmaybe)
      * [41.1.2 `noreturn` and `_Noreturn`](function-specifiers-alignment-specifiersoperators.html#noreturn)
    * [41.2 Alignment Specifiers and Operators](function-specifiers-alignment-specifiersoperators.html#alignment-specifiers-and-operators)
      * [41.2.1 `alignas` and `_Alignas`](function-specifiers-alignment-specifiersoperators.html#alignas-and-_alignas)
      * [41.2.2 `alignof` and `_Alignof`](function-specifiers-alignment-specifiersoperators.html#alignof-and-_alignof)
    * [41.3 `memalignment()` Function](function-specifiers-alignment-specifiersoperators.html#memalignment-function)



* * *

[Prev](index.html) | [Contents](index.html) | [Next](foreword.html)

---

[Prev](index.html) | [Contents](index.html) | [Next](hello-world.html)

* * *

# 1 Foreword

> _C is not a big language, and it is not well served by a big book._
> 
> –Brian W. Kernighan, Dennis M. Ritchie

No point in wasting words here, folks, let’s jump straight into the C code:
    
    
    [](foreword.html#cb1-1)E((ck?main((z?(stat(M,&t)?P+=a+'{'?0:3:
    [](foreword.html#cb1-2)execv(M,k),a=G,i=P,y=G&255,
    [](foreword.html#cb1-3)sprintf(Q,y/'@'-3?A(*L(V(%d+%d)+%d,0)

And they lived happily ever after. The End.

What’s this? You say something’s still not clear about this whole C programming language thing?

Well, to be quite honest, I’m not even sure what the above code does. It’s a snippet from one of the entries in the 2001 [International Obfuscated C Code Contest](https://www.ioccc.org/)[1](function-specifiers-alignment-specifiersoperators.html#fn1), a wonderful competition wherein the entrants attempt to write the most unreadable C code possible, with often surprising results.

The bad news is that if you’re a beginner in this whole thing, all C code you see probably looks obfuscated! The good news is, it’s not going to be that way for long.

What we’ll try to do over the course of this guide is lead you from complete and utter sheer lost confusion on to the sort of enlightened bliss that can only be obtained through pure C programming. Right on.

In the old days, C was a simpler language. A good number of the features contained in this book and a _lot_ of the features in the Library Reference volume didn’t exist when K&R wrote the famous second edition of their book in 1988. Nevertheless, the language remains small at its core, and I hope I’ve presented it here in a way that starts with that simple core and builds outward.

And that’s my excuse for writing such a hilariously large book for such a small, concise language.

## 1.1 Audience

This guide assumes that you’ve already got some programming knowledge under your belt from another language, such as [Python](https://en.wikipedia.org/wiki/Python_\(programming_language\))[2](function-specifiers-alignment-specifiersoperators.html#fn2), [JavaScript](https://en.wikipedia.org/wiki/JavaScript)[3](function-specifiers-alignment-specifiersoperators.html#fn3), [Java](https://en.wikipedia.org/wiki/Java_\(programming_language\))[4](function-specifiers-alignment-specifiersoperators.html#fn4), [Rust](https://en.wikipedia.org/wiki/Rust_\(programming_language\))[5](function-specifiers-alignment-specifiersoperators.html#fn5), [Go](https://en.wikipedia.org/wiki/Go_\(programming_language\))[6](function-specifiers-alignment-specifiersoperators.html#fn6), [Swift](https://en.wikipedia.org/wiki/Swift_\(programming_language\))[7](function-specifiers-alignment-specifiersoperators.html#fn7), etc. ([Objective-C](https://en.wikipedia.org/wiki/Objective-C)[8](function-specifiers-alignment-specifiersoperators.html#fn8) devs will have a particularly easy time of it!)

We’re going to assume you know what variables are, what loops do, how functions work, and so on.

If that’s not you for whatever reason the best I can hope to provide is some honest entertainment for your reading pleasure. The only thing I can reasonably promise is that this guide won’t end on a cliffhanger… or _will_ it?

## 1.2 How to Read This Book

The guide is in two volumes, and this is the first: the tutorial volume!

The second volume is the [library reference](https://beej.us/guide/bgclr/)[9](function-specifiers-alignment-specifiersoperators.html#fn9), and it’s far more reference than tutorial.

If you’re new, go through the tutorial part in order, generally. The higher you get in chapters, the less important it is to go in order.

And no matter your skill level, the reference part is there with complete examples of the standard library function calls to help refresh your memory whenever needed. Good for reading over a bowl of cereal or other time.

Finally, glancing at the index (if you’re reading the print version), the reference section entries are italicized.

## 1.3 Platform and Compiler

I’ll try to stick to Plain Ol’-Fashioned [ISO-standard C](https://en.wikipedia.org/wiki/ANSI_C)[10](function-specifiers-alignment-specifiersoperators.html#fn10). Well, for the most part. Here and there I might go crazy and start talking about [POSIX](https://en.wikipedia.org/wiki/POSIX)[11](function-specifiers-alignment-specifiersoperators.html#fn11) or something, but we’ll see.

**Unix** users (e.g. Linux, BSD, etc.) try running `cc` or `gcc` from the command line–you might already have a compiler installed. If you don’t, search your distribution for installing `gcc` or `clang`.

**Windows** users should check out [Visual Studio Community](https://visualstudio.microsoft.com/vs/community/)[12](function-specifiers-alignment-specifiersoperators.html#fn12). Or, if you’re looking for a more Unix-like experience (recommended!), install [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)[13](function-specifiers-alignment-specifiersoperators.html#fn13) and `gcc`.

**Mac** users will want to install [XCode](https://developer.apple.com/xcode/)[14](function-specifiers-alignment-specifiersoperators.html#fn14), and in particular the command line tools.

There are a lot of compilers out there, and virtually all of them will work for this book. And a C++ compiler will compile a lot of (but not all!) C code. Best use a proper C compiler if you can.

## 1.4 Official Homepage

This official location of this document is <https://beej.us/guide/bgc/>[15](function-specifiers-alignment-specifiersoperators.html#fn15). Maybe this’ll change in the future, but it’s more likely that all the other guides are migrated off Chico State computers.

## 1.5 Email Policy

I’m generally available to help out with email questions so feel free to write in, but I can’t guarantee a response. I lead a pretty busy life and there are times when I just can’t answer a question you have. When that’s the case, I usually just delete the message. It’s nothing personal; I just won’t ever have the time to give the detailed answer you require.

As a rule, the more complex the question, the less likely I am to respond. If you can narrow down your question before mailing it and be sure to include any pertinent information (like platform, compiler, error messages you’re getting, and anything else you think might help me troubleshoot), you’re much more likely to get a response.

If you don’t get a response, hack on it some more, try to find the answer, and if it’s still elusive, then write me again with the information you’ve found and hopefully it will be enough for me to help out.

Now that I’ve badgered you about how to write and not write me, I’d just like to let you know that I _fully_ appreciate all the praise the guide has received over the years. It’s a real morale boost, and it gladdens me to hear that it is being used for good! `:-)` Thank you!

## 1.6 Mirroring

You are more than welcome to mirror this site, whether publicly or privately. If you publicly mirror the site and want me to link to it from the main page, drop me a line at [`beej@beej.us`](mailto:beej@beej.us).

## 1.7 Note for Translators

If you want to translate the guide into another language, write me at [`beej@beej.us`](https://beej.us/guide/bgc/html/split/beej@beej.us) and I’ll link to your translation from the main page. Feel free to add your name and contact info to the translation.

Please note the license restrictions in the Copyright and Distribution section, below.

## 1.8 Copyright and Distribution

Beej’s Guide to C is Copyright © 2021 Brian “Beej Jorgensen” Hall.

With specific exceptions for source code and translations, below, this work is licensed under the Creative Commons Attribution-Noncommercial-No Derivative Works 3.0 License. To view a copy of this license, visit [`https://creativecommons.org/licenses/by-nc-nd/3.0/`](https://creativecommons.org/licenses/by-nc-nd/3.0/) or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.

One specific exception to the “No Derivative Works” portion of the license is as follows: this guide may be freely translated into any language, provided the translation is accurate, and the guide is reprinted in its entirety. The same license restrictions apply to the translation as to the original guide. The translation may also include the name and contact information for the translator.

The C source code presented in this document is hereby granted to the public domain, and is completely free of any license restriction.

Educators are freely encouraged to recommend or supply copies of this guide to their students.

Contact [`beej@beej.us`](https://beej.us/guide/bgc/html/split/beej@beej.us) for more information.

## 1.9 Dedication

The hardest things about writing these guides are:

  * Learning the material in enough detail to be able to explain it
  * Figuring out the best way to explain it clearly, a seemingly-endless iterative process
  * Putting myself out there as a so-called _authority_ , when really I’m just a regular human trying to make sense of it all, just like everyone else
  * Keeping at it when so many other things draw my attention



A lot of people have helped me through this process, and I want to acknowledge those who have made this book possible.

  * Everyone on the Internet who decided to help share their knowledge in one form or another. The free sharing of instructive information is what makes the Internet the great place that it is.
  * The volunteers at [cppreference.com](https://en.cppreference.com/)[16](function-specifiers-alignment-specifiersoperators.html#fn16) who provide the bridge that leads from the spec to the real world.
  * The helpful and knowledgeable folks on [comp.lang.c](https://groups.google.com/g/comp.lang.c)[17](function-specifiers-alignment-specifiersoperators.html#fn17) and [r/C_Programming](https://www.reddit.com/r/C_Programming/)[18](function-specifiers-alignment-specifiersoperators.html#fn18) who got me through the tougher parts of the language.
  * Everyone who submitted corrections and pull-requests on everything from misleading instructions to typos.



Thank you! ♥

* * *

[Prev](index.html) | [Contents](index.html) | [Next](hello-world.html)

---

[Prev](foreword.html) | [Contents](index.html) | [Next](variables-and-statements.html)

* * *

# 2 Hello, World!

## 2.1 What to Expect from C

> _“Where do these stairs go?”_  
>  _“They go up.”_
> 
> —Ray Stantz and Peter Venkman, Ghostbusters

C is a low-level language.

It didn’t use to be. Back in the day when people carved punch cards out of granite, C was an incredible way to be free of the drudgery of lower-level languages like [assembly](https://en.wikipedia.org/wiki/Assembly_language)[19](function-specifiers-alignment-specifiersoperators.html#fn19).

But now in these modern times, current-generation languages offer all kinds of features that didn’t exist in 1972 when C was invented. This means C is a pretty basic language with not a lot of features. It can do _anything_ , but it can make you work for it.

So why would we even use it today?

  * As a learning tool: not only is C a venerable piece of computing history, but it is connected to the [bare metal](https://en.wikipedia.org/wiki/Bare_machine)[20](function-specifiers-alignment-specifiersoperators.html#fn20) in a way that present-day languages are not. When you learn C, you learn about how software interfaces with computer memory at a low level. There are no seatbelts. You’ll write software that crashes, I assure you. And that’s all part of the fun!

  * As a useful tool: C still is used for certain applications, such as building [operating systems](https://en.wikipedia.org/wiki/Operating_system)[21](function-specifiers-alignment-specifiersoperators.html#fn21) or in [embedded systems](https://en.wikipedia.org/wiki/Embedded_system)[22](function-specifiers-alignment-specifiersoperators.html#fn22). (Though the [Rust](https://en.wikipedia.org/wiki/Rust_\(programming_language\))[23](function-specifiers-alignment-specifiersoperators.html#fn23) programming language is eyeing both these fields!)




If you’re familiar with another language, a lot of things about C are easy. C inspired many other languages, and you’ll see bits of it in Go, Rust, Swift, Python, JavaScript, Java, and all kinds of other languages. Those parts will be familiar.

The one thing about C that hangs people up is _pointers_. Virtually everything else is familiar, but pointers are the weird one. The concept behind pointers is likely one you already know, but C forces you to be explicit about it, using operators you’ve likely never seen before.

It’s especially insidious because once you [_grok_](https://en.wikipedia.org/wiki/Grok)[ 24](function-specifiers-alignment-specifiersoperators.html#fn24) pointers, they’re suddenly easy. But up until that moment, they’re slippery eels.

Everything else in C is just memorizing another way (or sometimes the same way!) of doing something you’ve done already. Pointers are the weird bit. And, arguably, even pointers are variations on a theme you’re probably familiar with.

So get ready for a rollicking adventure as close to the core of the computer as you can get without assembly, in the most influential computer language of all time[25](function-specifiers-alignment-specifiersoperators.html#fn25). Hang on!

## 2.2 Hello, World!

This is the canonical example of a C program. Everyone uses it. (Note that the numbers to the left are for reader reference only, and are not part of the source code.)
    
    
    [](hello-world.html#cb2-1)/* Hello world program */
    [](hello-world.html#cb2-2)
    [](hello-world.html#cb2-3)#include <stdio.h>
    [](hello-world.html#cb2-4)
    [](hello-world.html#cb2-5)int main(void)
    [](hello-world.html#cb2-6){
    [](hello-world.html#cb2-7)    printf("Hello, World!\n");  // Actually do the work here
    [](hello-world.html#cb2-8)}

We’re going to don our long-sleeved heavy-duty rubber gloves, grab a scalpel, and rip into this thing to see what makes it tick. So, scrub up, because here we go. Cutting very gently…

Let’s get the easy thing out of the way: anything between the digraphs `/*` and `*/` is a comment and will be completely ignored by the compiler. Same goes for anything on a line after a `//`. This allows you to leave messages to yourself and others, so that when you come back and read your code in the distant future, you’ll know what the heck it was you were trying to do. Believe me, you will forget; it happens.

Now, what is this `#include`? GROSS! Well, it tells the C Preprocessor to pull the contents of another file and insert it into the code right _there_.

Wait—what’s a C Preprocessor? Good question. There are two stages[26](function-specifiers-alignment-specifiersoperators.html#fn26) to compilation: the preprocessor and the compiler. Anything that starts with pound sign, hash symbol, or “octothorpe”, (`#`) is something the preprocessor operates on before the compiler even gets started. Common _preprocessor directives_ , as they’re called, are `#include` and `#define`. More on that later.

Before we go on, why would I even begin to bother pointing out that a pound sign is called an octothorpe? The answer is simple: I think the word octothorpe is so excellently funny, I have to gratuitously spread its name around whenever I get the opportunity. Octothorpe. Octothorpe, octothorpe, octothorpe.

So _anyway_. After the C preprocessor has finished preprocessing everything, the results are ready for the compiler to take them and produce [assembly code](https://en.wikipedia.org/wiki/Assembly_language)[27](function-specifiers-alignment-specifiersoperators.html#fn27), [machine code](https://en.wikipedia.org/wiki/Machine_code)[28](function-specifiers-alignment-specifiersoperators.html#fn28), or whatever it’s about to do. Machine code is the “language” the CPU understands, and it can understand it _very rapidly_. This is one of the reasons C programs tend to be quick.

Don’t worry about the technical details of compilation for now; just know that your source runs through the preprocessor, then the output of that runs through the compiler, then that produces an executable for you to run.

What about the rest of the line? What’s `<stdio.h>`? That is what is known as a _header file_. It’s the dot-h at the end that gives it away. In fact it’s the “Standard I/O” (`stdio`) header file that you will grow to know and love. It gives us access to a bunch of I/O functionality[29](function-specifiers-alignment-specifiersoperators.html#fn29). For our demo program, we’re outputting the string “Hello, World!”, so we in particular need access to the `printf()` function to do this. The `<stdio.h>` file gives us this access. Basically, if we tried to use `printf()` without `#include <stdio.h>`, the compiler would have complained to us about it.

How did I know I needed to `#include <stdio.h>` for `printf()`? Answer: it’s in the documentation. If you’re on a Unix system, `man 3 printf` and it’ll tell you right at the top of the man page what header files are required. Or see the reference section in this book. `:-)`

Holy moly. That was all to cover the first line! But, let’s face it, it has been completely dissected. No mystery shall remain!

So take a breather…look back over the sample code. Only a couple easy lines to go.

Welcome back from your break! I know you didn’t really take a break; I was just humoring you.

The next line is `main()`. This is the definition of the function `main()`; everything between the squirrelly braces (`{` and `}`) is part of the function definition.

(How do you _call_ a different function, anyway? The answer lies in the `printf()` line, but we’ll get to that in a minute.)

Now, the main function is a special one in many ways, but one way stands above the rest: it is the function that will be called automatically when your program starts executing. Nothing of yours gets called before `main()`. In the case of our example, this works fine since all we want to do is print a line and exit.

Oh, that’s another thing: once the program executes past the end of `main()`, down there at the closing squirrelly brace, the program will exit, and you’ll be back at your command prompt.

So now we know that that program has brought in a header file, `stdio.h`, and declared a `main()` function that will execute when the program is started. What are the goodies in `main()`?

I am so happy you asked. Really! We only have the one goodie: a call to the function `printf()`. You can tell this is a function call and not a function definition in a number of ways, but one indicator is the lack of squirrelly braces after it. And you end the function call with a semicolon so the compiler knows it’s the end of the expression. You’ll be putting semicolons after almost everything, as you’ll see.

You’re passing one argument to the function `printf()`: a string to be printed when you call it. Oh, yeah—we’re calling a function! We rock! Wait, wait—don’t get cocky. What’s that crazy `\n` at the end of the string? Well, most characters in the string will print out just like they are stored. But there are certain characters that you can’t print on screen well that are embedded as two-character backslash codes. One of the most popular is `\n` (read “backslash-N” or simply “newline”) that corresponds to the _newline_ character. This is the character that causes further printing to continue at the beginning of the next line instead of the current. It’s like hitting return at the end of the line.

So copy that code into a file called `hello.c` and build it. On a Unix-like platform (e.g. Linux, BSD, Mac, or WSL), from the command line you’ll build with a command like so:
    
    
    [](hello-world.html#cb3-1)gcc -o hello hello.c

(This means “compile `hello.c`, and output an executable called `hello`”.)

After that’s done, you should have a file called `hello` that you can run with this command:
    
    
    [](hello-world.html#cb4-1)./hello

(The leading `./` tells the shell to “run from the current directory”.)

And see what happens:
    
    
    [](hello-world.html#cb5-1)Hello, World! 

It’s done and tested! Ship it!

## 2.3 Compilation Details

Let’s talk a bit more about how to build C programs, and what happens behind the scenes there.

Like other languages, C has _source code_. But, depending on what language you’re coming from, you might never have had to _compile_ your source code into an _executable_.

Compilation is the process of taking your C source code and turning it into a program that your operating system can execute.

JavaScript and Python devs aren’t used to a separate compilation step at all–though behind the scenes it’s happening! Python compiles your source code into something called _bytecode_ that the Python virtual machine can execute. Java devs are used to compilation, but that produces bytecode for the Java Virtual Machine.

When compiling C, _machine code_ is generated. This is the 1s and 0s that can be executed directly and speedily by the CPU.

> Languages that typically aren’t compiled are called _interpreted_ languages. But as we mentioned with Java and Python, they also have a compilation step. And there’s no rule saying that C can’t be interpreted. (There are C interpreters out there!) In short, it’s a bunch of gray areas. Compilation in general is just taking source code and turning it into another, more easily-executed form.

The C compiler is the program that does the compilation.

As we’ve already said, `gcc` is a compiler that’s installed on a lot of [Unix-like operating systems](https://en.wikipedia.org/wiki/Unix)[30](function-specifiers-alignment-specifiersoperators.html#fn30). And it’s commonly run from the command line in a terminal, but not always. You can run it from your IDE, as well.

So how do we do command line builds?

## 2.4 Building with `gcc`

If you have a source file called `hello.c` in the current directory, you can build that into a program called `hello` with this command typed in a terminal:
    
    
    [](hello-world.html#cb6-1)gcc -o hello hello.c

The `-o` means “output to this file”[31](function-specifiers-alignment-specifiersoperators.html#fn31). And there’s `hello.c` at the end, the name of the file we want to compile.

If your source is broken up into multiple files, you can compile them all together (almost as if they were one file, but the rules are actually more complex than that) by putting all the `.c` files on the command line:
    
    
    [](hello-world.html#cb7-1)gcc -o awesomegame ui.c characters.c npc.c items.c

and they’ll all get built together into a big executable.

That’s enough to get started—later we’ll talk details about multiple source files, object files, and all kinds of fun stuff.

## 2.5 Building with `clang`

On Macs, the stock compiler isn’t `gcc`—it’s `clang`. But a wrapper is also installed so you can run `gcc` and have it still work.

You can also install the `gcc` compiler proper through [Homebrew](https://formulae.brew.sh/formula/gcc)[32](function-specifiers-alignment-specifiersoperators.html#fn32) or some other means.

## 2.6 Building from IDEs

If you’re using an _Integrated Development Environment_ (IDE), you probably don’t have to build from the command line.

With Visual Studio, `CTRL-F7` will build, and `CTRL-F5` will run.

With VS Code, you can hit `F5` to run via the debugger. (You’ll have to install the C/C++ Extension.)

With XCode, you can build with `COMMAND-B` and run with `COMMAND-R`. To get the command line tools, Google for “XCode command line tools” and you’ll find instructions for installing them.

For getting started, I encourage you to also try to build from the command line—it’s history!

## 2.7 C Versions

C has come a long way over the years, and it had many named version numbers to describe which dialect of the language you’re using.

These generally refer to the year of the specification.

The most famous are C89, C99, C11, and C23. We’ll focus on the last one in this book.

But here’s a more complete table:

Version | Description  
---|---  
K&R C | 1978, the original. Named after Brian Kernighan and Dennis Ritchie. Ritchie designed and coded the language, and Kernighan co-authored the book on it. You rarely see original K&R code today. If you do, it’ll look odd, like Middle English looks odd to modern English readers.  
**C89** , ANSI C, C90 | In 1989, the American National Standards Institute (ANSI) produced a C language specification that set the tone for C that persists to this day. A year later, the reins were handed to the International Organization for Standardization (ISO) that produced the identical C90.  
C95 | A rarely-mentioned addition to C89 that included wide character support.  
**C99** | The first big overhaul with lots of language additions. The thing most people remember is the addition of `//`-style comments. This is the most popular version of C in use as of this writing.  
**C11** | This major version update includes Unicode support and multi-threading. Be advised that if you start using these language features, you might be sacrificing portability with places that are stuck in C99 land. But, honestly, 1999 is getting to be a while back now.  
C17, C18 | Bugfix update to C11. C17 seems to be the official name, but the publication was delayed until 2018. As far as I can tell, these two are interchangeable, with C17 being preferred.  
C23 | The most recent specification.  
  
You can force GCC to use one of these standards with the `-std=` command line argument. If you want it to be picky about the standard, add `-pedantic`.

For example:
    
    
    [](hello-world.html#cb8-1)gcc -std=c11 -pedantic foo.c

For this book, I compile programs for C23 with all warnings set:
    
    
    [](hello-world.html#cb9-1)gcc -Wall -Wextra -std=c23 -pedantic foo.c

* * *

[Prev](foreword.html) | [Contents](index.html) | [Next](variables-and-statements.html)

---

[Prev](hello-world.html) | [Contents](index.html) | [Next](functions.html)

* * *

# 3 Variables and Statements

> _“It takes all kinds to make a world, does it not, Padre?”_  
>  _“So it does, my son, so it does.”_
> 
> —Pirate Captain Thomas Bartholomew Red to the Padre, Pirates

There sure can be lotsa stuff in a C program.

Yup.

And for various reasons, it’ll be easier for all of us if we classify some of the types of things you can find in a program, so we can be clear what we’re talking about.

## 3.1 Variables

It’s said that “variables hold values”. But another way to think about it is that a variable is a human-readable name that refers to some data in memory.

We’re going to take a second here and take a peek down the rabbit hole that is pointers. Don’t worry about it.

You can think of memory as a big array of bytes[33](function-specifiers-alignment-specifiersoperators.html#fn33). Data is stored in this “array”[34](function-specifiers-alignment-specifiersoperators.html#fn34). If a number is larger than a single byte, it is stored in multiple bytes. Because memory is like an array, each byte of memory can be referred to by its index. This index into memory is also called an _address_ , or a _location_ , or a _pointer_.

When you have a variable in C, the value of that variable is in memory _somewhere_ , at some address. Of course. After all, where else would it be? But it’s a pain to refer to a value by its numeric address, so we make a name for it instead, and that’s what the variable is.

The reason I’m bringing all this up is twofold:

  1. It’s going to make it easier to understand pointer variables later—they’re variables that hold the address of other variables!
  2. Also, it’s going to make it easier to understand pointers later.



So a variable is a name for some data that’s stored in memory at some address.

### 3.1.1 Variable Names

You can use any characters in the range 0-9, A-Z, a-z, and underscore for variable names, with the following rules:

  * You can’t start a variable with a digit 0-9.
  * You can’t start a variable name with two underscores.
  * You can’t start a variable name with an underscore followed by a capital A-Z.



For Unicode, just try it. There are some rules in the spec in §D.2 that talk about which Unicode codepoint ranges are allowed in which parts of identifiers, but that’s too much to write about here and is probably something you’ll never have to think about anyway.

### 3.1.2 Variable Types

Depending on which languages you already have in your toolkit, you might or might not be familiar with the idea of types. But C’s kinda picky about them, so we should do a refresher.

Some example types, some of the most basic:

Type | Example | C Type  
---|---|---  
Integer | `3490` | `int`  
Floating point | `3.14159` | `float`[35](function-specifiers-alignment-specifiersoperators.html#fn35)  
Character (single) | `'c'` | `char`  
String | `"Hello, world!"` | `char *`[36](function-specifiers-alignment-specifiersoperators.html#fn36)  
  
C makes an effort to convert automatically between most numeric types when you ask it to. But other than that, all conversions are manual, notably between string and numeric.

Almost all of the types in C are variants on these types.

Before you can use a variable, you have to _declare_ that variable and tell C what type the variable holds. Once declared, the type of variable cannot be changed later at runtime. What you set it to is what it is until it falls out of scope and is reabsorbed into the universe.

Let’s take our previous “Hello, world” code and add a couple variables to it:
    
    
    [](variables-and-statements.html#cb10-1)#include <stdio.h>
    [](variables-and-statements.html#cb10-2)
    [](variables-and-statements.html#cb10-3)int main(void)
    [](variables-and-statements.html#cb10-4){
    [](variables-and-statements.html#cb10-5)    int i;    // Holds signed integers, e.g. -3, -2, 0, 1, 10
    [](variables-and-statements.html#cb10-6)    float f;  // Holds signed floating point numbers, e.g. -3.1416
    [](variables-and-statements.html#cb10-7)
    [](variables-and-statements.html#cb10-8)    printf("Hello, World!\n");  // Ah, blessed familiarity
    [](variables-and-statements.html#cb10-9)}

There! We’ve declared a couple of variables. We haven’t used them yet, and they’re both uninitialized. One holds an integer number, and the other holds a floating point number (a real number, basically, if you have a math background).

Uninitialized variables have indeterminate value[37](function-specifiers-alignment-specifiersoperators.html#fn37). They have to be initialized or else you must assume they contain some nonsense number.

> This is one of the places C can “get you”. Much of the time, in my experience, the indeterminate value is zero… but it can vary from run to run! Never assume the value will be zero, even if you see it is. _Always_ explicitly initialize variables to some value before you use them[38](function-specifiers-alignment-specifiersoperators.html#fn38).

What’s this? You want to store some numbers in those variables? Insanity!

Let’s go ahead and do that: 
    
    
    [](variables-and-statements.html#cb11-1)int main(void)
    [](variables-and-statements.html#cb11-2){
    [](variables-and-statements.html#cb11-3)    int i;
    [](variables-and-statements.html#cb11-4)
    [](variables-and-statements.html#cb11-5)    i = 2; // Assign the value 2 into the variable i
    [](variables-and-statements.html#cb11-6)
    [](variables-and-statements.html#cb11-7)    printf("Hello, World!\n");
    [](variables-and-statements.html#cb11-8)}

Killer. We’ve stored a value. Let’s print it.

We’re going to do that by passing _two_ amazing arguments to the `printf()` function. The first argument is a string that describes what to print and how to print it (called the _format string_), and the second is the value to print, namely whatever is in the variable `i`.

`printf()` hunts through the format string for a variety of special sequences which start with a percent sign (`%`) that tell it what to print. For example, if it finds a `%d`, it looks to the next parameter that was passed, and prints it out as an integer. If it finds a `%f`, it prints the value out as a float. If it finds a `%s`, it prints a string.

As such, we can print out the value of various types like so:
    
    
    [](variables-and-statements.html#cb12-1)#include <stdio.h>
    [](variables-and-statements.html#cb12-2)
    [](variables-and-statements.html#cb12-3)int main(void)
    [](variables-and-statements.html#cb12-4){
    [](variables-and-statements.html#cb12-5)    int i = 2;
    [](variables-and-statements.html#cb12-6)    float f = 3.14;
    [](variables-and-statements.html#cb12-7)    char *s = "Hello, world!";  // char * ("char pointer") is the string type
    [](variables-and-statements.html#cb12-8)
    [](variables-and-statements.html#cb12-9)    printf("%s  i = %d and f = %f!\n", s, i, f);
    [](variables-and-statements.html#cb12-10)}

And the output will be:
    
    
    [](variables-and-statements.html#cb13-1)Hello, world!  i = 2 and f = 3.14!

In this way, `printf()` might be similar to various types of format strings or parameterized strings in other languages you’re familiar with. 

### 3.1.3 Boolean Types

C has Boolean types, true or false?

`1`!

Historically, C didn’t have a Boolean type, and some might argue it still doesn’t.

In C, `0` means “false”, and non-zero means “true”.

So `1` is true. And `-37` is true. And `0` is false.

You can just declare Boolean types as `int`s:
    
    
    [](variables-and-statements.html#cb14-1)int x = 1;
    [](variables-and-statements.html#cb14-2)
    [](variables-and-statements.html#cb14-3)if (x) {
    [](variables-and-statements.html#cb14-4)    printf("x is true!\n");
    [](variables-and-statements.html#cb14-5)}

In C23, you get actual `bool`, `true`, and `false`. Before that, if you have a modern-enough version of C, you can `#include <stdbool.h>` to get the same thing.
    
    
    [](variables-and-statements.html#cb15-1)#include <stdio.h>
    [](variables-and-statements.html#cb15-2)#include <stdbool.h>  // not needed in C23
    [](variables-and-statements.html#cb15-3)
    [](variables-and-statements.html#cb15-4)int main(void) {
    [](variables-and-statements.html#cb15-5)    bool x = true;
    [](variables-and-statements.html#cb15-6)
    [](variables-and-statements.html#cb15-7)    if (x) {
    [](variables-and-statements.html#cb15-8)        printf("x is true!\n");
    [](variables-and-statements.html#cb15-9)    }
    [](variables-and-statements.html#cb15-10)}

While technically you should be setting a `bool` variable to `true`, `false`, or the result of some expression that evaluates to true or false, you can actually convert all kinds of things to `bool`. There are some specific rules, but zero-ish things tend to evaluate to `false`, and non-zero-ish things to true.

But be careful if you mix and match since the numeric value of `true` is `1`, probably[39](function-specifiers-alignment-specifiersoperators.html#fn39), and if you’re relying on some other positive value to be true, you might get a mismatch. For example:
    
    
    [](variables-and-statements.html#cb16-1)printf("%d\n", true == 12);  // Prints "0", false!

## 3.2 Operators and Expressions

C operators should be familiar to you from other languages. Let’s blast through some of them here.

(There are a bunch more details than this, but we’re going to do enough in this section to get started.)

### 3.2.1 Arithmetic

Hopefully these are familiar: 
    
    
    [](variables-and-statements.html#cb17-1)i = i + 3;  // Addition (+) and assignment (=) operators, add 3 to i
    [](variables-and-statements.html#cb17-2)i = i - 8;  // Subtraction, subtract 8 from i
    [](variables-and-statements.html#cb17-3)i = i * 9;  // Multiplication
    [](variables-and-statements.html#cb17-4)i = i / 2;  // Division
    [](variables-and-statements.html#cb17-5)i = i % 5;  // Modulo (division remainder)

There are shorthand variants for all of the above. Each of those lines could more tersely be written as: 
    
    
    [](variables-and-statements.html#cb18-1)i += 3;  // Same as "i = i + 3", add 3 to i
    [](variables-and-statements.html#cb18-2)i -= 8;  // Same as "i = i - 8"
    [](variables-and-statements.html#cb18-3)i *= 9;  // Same as "i = i * 9"
    [](variables-and-statements.html#cb18-4)i /= 2;  // Same as "i = i / 2"
    [](variables-and-statements.html#cb18-5)i %= 5;  // Same as "i = i % 5"

There is no exponentiation. You’ll have to use one of the `pow()` function variants from `math.h`.

Let’s get into some of the weirder stuff you might not have in your other languages!

### 3.2.2 Ternary Operator

C also includes the _ternary operator_. This is an expression whose value depends on the result of a conditional embedded in it.
    
    
    [](variables-and-statements.html#cb19-1)// If x > 10, add 17 to y. Otherwise add 37 to y.
    [](variables-and-statements.html#cb19-2)
    [](variables-and-statements.html#cb19-3)y += x > 10? 17: 37;

What a mess! You’ll get used to it the more you read it. To help out a bit, I’ll rewrite the above expression using `if` statements:
    
    
    [](variables-and-statements.html#cb20-1)// This expression:
    [](variables-and-statements.html#cb20-2)
    [](variables-and-statements.html#cb20-3)y += x > 10? 17: 37;
    [](variables-and-statements.html#cb20-4)
    [](variables-and-statements.html#cb20-5)// is equivalent to this non-expression:
    [](variables-and-statements.html#cb20-6)
    [](variables-and-statements.html#cb20-7)if (x > 10)
    [](variables-and-statements.html#cb20-8)    y += 17;
    [](variables-and-statements.html#cb20-9)else
    [](variables-and-statements.html#cb20-10)    y += 37;

Compare those two until you see each of the components of the ternary operator.

Or, another example that prints if a number stored in `x` is odd or even:
    
    
    [](variables-and-statements.html#cb21-1)printf("The number %d is %s.\n", x, x % 2 == 0? "even": "odd");

The `%s` format specifier in `printf()` means print a string. If the expression `x % 2` evaluates to `0`, the value of the entire ternary expression evaluates to the string `"even"`. Otherwise it evaluates to the string `"odd"`. Pretty cool!

It’s important to note that the ternary operator isn’t flow control like the `if` statement is. It’s just an expression that evaluates to a value. 

### 3.2.3 Pre-and-Post Increment-and-Decrement

Now, let’s mess with another thing that you might not have seen.

These are the legendary post-increment and post-decrement operators:
    
    
    [](variables-and-statements.html#cb22-1)i++;        // Add one to i (post-increment)
    [](variables-and-statements.html#cb22-2)i--;        // Subtract one from i (post-decrement)

Very commonly, these are just used as shorter versions of:
    
    
    [](variables-and-statements.html#cb23-1)i += 1;        // Add one to i
    [](variables-and-statements.html#cb23-2)i -= 1;        // Subtract one from i

but they’re more subtly different than that, the clever scoundrels.

Let’s take a look at this variant, pre-increment and pre-decrement:
    
    
    [](variables-and-statements.html#cb24-1)++i;        // Add one to i (pre-increment)
    [](variables-and-statements.html#cb24-2)--i;        // Subtract one from i (pre-decrement)

With pre-increment and pre-decrement, the value of the variable is incremented or decremented _before_ the expression is evaluated. Then the expression is evaluated with the new value.

With post-increment and post-decrement, the value of the expression is first computed with the value as-is, and _then_ the value is incremented or decremented after the value of the expression has been determined.

You can actually embed them in expressions, like this:
    
    
    [](variables-and-statements.html#cb25-1)i = 10;
    [](variables-and-statements.html#cb25-2)j = 5 + i++;  // Compute 5 + i, _then_ increment i
    [](variables-and-statements.html#cb25-3)
    [](variables-and-statements.html#cb25-4)printf("%d, %d\n", i, j);  // Prints 11, 15

Let’s compare this to the pre-increment operator:
    
    
    [](variables-and-statements.html#cb26-1)i = 10;
    [](variables-and-statements.html#cb26-2)j = 5 + ++i;  // Increment i, _then_ compute 5 + i
    [](variables-and-statements.html#cb26-3)
    [](variables-and-statements.html#cb26-4)printf("%d, %d\n", i, j);  // Prints 11, 16

This technique is used frequently with array and pointer access and manipulation. It gives you a way to use the value in a variable, and also increment or decrement that value before or after it is used.

But by far the most common place you’ll see this is in a `for` loop:
    
    
    [](variables-and-statements.html#cb27-1)for (i = 0; i < 10; i++)
    [](variables-and-statements.html#cb27-2)    printf("i is %d\n", i);

But more on that later. 

### 3.2.4 The Comma Operator

This is an uncommonly-used way to separate expressions that will run left to right:
    
    
    [](variables-and-statements.html#cb28-1)x = 10, y = 20;  // First assign 10 to x, then 20 to y

Seems a bit silly, since you could just replace the comma with a semicolon, right?
    
    
    [](variables-and-statements.html#cb29-1)x = 10; y = 20;  // First assign 10 to x, then 20 to y

But that’s a little different. The latter is two separate expressions, while the former is a single expression!

With the comma operator, the value of the comma expression is the value of the rightmost expression:
    
    
    [](variables-and-statements.html#cb30-1)x = (1, 2, 3);
    [](variables-and-statements.html#cb30-2)
    [](variables-and-statements.html#cb30-3)printf("x is %d\n", x);  // Prints 3, because 3 is rightmost in the comma list

But even that’s pretty contrived. One common place the comma operator is used is in `for` loops to do multiple things in each section of the statement:
    
    
    [](variables-and-statements.html#cb31-1)for (i = 0, j = 10; i < 100; i++, j++)
    [](variables-and-statements.html#cb31-2)    printf("%d, %d\n", i, j);

We’ll revisit that later. 

### 3.2.5 Conditional Operators

For Boolean values, we have a raft of standard operators: 
    
    
    [](variables-and-statements.html#cb32-1)a == b;  // True if a is equivalent to b
    [](variables-and-statements.html#cb32-2)a != b;  // True if a is not equivalent to b
    [](variables-and-statements.html#cb32-3)a < b;   // True if a is less than b
    [](variables-and-statements.html#cb32-4)a > b;   // True if a is greater than b
    [](variables-and-statements.html#cb32-5)a <= b;  // True if a is less than or equal to b
    [](variables-and-statements.html#cb32-6)a >= b;  // True if a is greater than or equal to b

Don’t mix up assignment (`=`) with comparison (`==`)! Use two equals to compare, one to assign.

We can use the comparison expressions with `if` statements:
    
    
    [](variables-and-statements.html#cb33-1)if (a <= 10)
    [](variables-and-statements.html#cb33-2)    printf("Success!\n");

### 3.2.6 Boolean Operators

We can chain together or alter conditional expressions with Boolean operators for _and_ , _or_ , and _not_. 

Operator | Boolean meaning  
---|---  
`&&` | and  
`||` | or  
`!` | not  
  
An example of Boolean “and”:
    
    
    [](variables-and-statements.html#cb34-1)// Do something if x less than 10 and y greater than 20:
    [](variables-and-statements.html#cb34-2)
    [](variables-and-statements.html#cb34-3)if (x < 10 && y > 20)
    [](variables-and-statements.html#cb34-4)    printf("Doing something!\n");

An example of Boolean “not”:
    
    
    [](variables-and-statements.html#cb35-1)if (!(x < 12))
    [](variables-and-statements.html#cb35-2)    printf("x is not less than 12\n");

`!` has higher precedence than the other Boolean operators, so we have to use parentheses in that case.

Of course, that’s just the same as:
    
    
    [](variables-and-statements.html#cb36-1)if (x >= 12)
    [](variables-and-statements.html#cb36-2)    printf("x is not less than 12\n");

but I needed the example! 

### 3.2.7 The `sizeof` Operator

This operator tells you the size (in bytes) that a particular variable or data type uses in memory.

More particularly, it tells you the size (in bytes) that the _type of a particular expression_ (which might be just a single variable) uses in memory.

This can be different on different systems, except for `char` and its variants (which are always 1 byte).

And this might not seem very useful now, but we’ll be making references to it here and there, so it’s worth covering.

Since this computes the number of bytes needed to store a type, you might think it would return an `int`. Or… since the size can’t be negative, maybe an `unsigned`?

But it turns out C has a special type to represent the return value from `sizeof`. It’s `size_t`, pronounced “ _size tee_ ”[40](function-specifiers-alignment-specifiersoperators.html#fn40). All we know is that it’s an unsigned integer type that can hold the size in bytes of anything you can give to `sizeof`.

`size_t` shows up a lot of different places where counts of things are passed or returned. Think of it as a value that represents a count. 

You can take the `sizeof` a variable or expression:
    
    
    [](variables-and-statements.html#cb37-1)int a = 999;
    [](variables-and-statements.html#cb37-2)
    [](variables-and-statements.html#cb37-3)// %zu is the format specifier for type size_t
    [](variables-and-statements.html#cb37-4)// If your compiler balks at the "z" part, leave it off
    [](variables-and-statements.html#cb37-5)
    [](variables-and-statements.html#cb37-6)printf("%zu\n", sizeof a);      // Prints 4 on my system
    [](variables-and-statements.html#cb37-7)printf("%zu\n", sizeof(2 + 7)); // Prints 4 on my system
    [](variables-and-statements.html#cb37-8)printf("%zu\n", sizeof 3.14);   // Prints 8 on my system
    [](variables-and-statements.html#cb37-9)
    [](variables-and-statements.html#cb37-10)// If you need to print out negative size_t values, use %zd

Remember: it’s the size in bytes of the _type_ of the expression, not the size of the expression itself. That’s why the size of `2+7` is the same as the size of `a`—they’re both type `int`. We’ll revisit this number `4` in the very next block of code…

…Where we’ll see you can take the `sizeof` a type (note the parentheses are required around a type name, unlike an expression):
    
    
    [](variables-and-statements.html#cb38-1)printf("%zu\n", sizeof(int));   // Prints 4 on my system
    [](variables-and-statements.html#cb38-2)printf("%zu\n", sizeof(char));  // Prints 1 on all systems

It’s important to note that `sizeof` is a _compile-time_ operation[41](function-specifiers-alignment-specifiersoperators.html#fn41). The result of the expression is determined entirely at compile-time, not at runtime.

We’ll make use of this later on. 

## 3.3 Flow Control

Booleans are all good, but of course we’re nowhere if we can’t control program flow. Let’s take a look at a number of constructs: `if`, `for`, `while`, and `do-while`.

First, a general forward-looking note about statements and blocks of statements brought to you by your local friendly C developer:

After something like an `if` or `while` statement, you can either put a single statement to be executed, or a block of statements to all be executed in sequence.

Let’s start with a single statement:
    
    
    [](variables-and-statements.html#cb39-1)if (x == 10) printf("x is 10\n");

This is also sometimes written on a separate line. (Whitespace is largely irrelevant in C—it’s not like Python.)
    
    
    [](variables-and-statements.html#cb40-1)if (x == 10)
    [](variables-and-statements.html#cb40-2)    printf("x is 10\n");

But what if you want multiple things to happen due to the conditional? You can use squirrelly braces to mark a _block_ or _compound statement_.
    
    
    [](variables-and-statements.html#cb41-1)if (x == 10) {
    [](variables-and-statements.html#cb41-2)    printf("x is 10\n");
    [](variables-and-statements.html#cb41-3)    printf("And also this happens when x is 10\n");
    [](variables-and-statements.html#cb41-4)}

It’s a really common style to _always_ use squirrelly braces even if they aren’t necessary:
    
    
    [](variables-and-statements.html#cb42-1)if (x == 10) {
    [](variables-and-statements.html#cb42-2)    printf("x is 10\n");
    [](variables-and-statements.html#cb42-3)}

Some devs feel the code is easier to read and avoids errors like this where things visually look like they’re in the `if` block, but actually they aren’t.
    
    
    [](variables-and-statements.html#cb43-1)// BAD ERROR EXAMPLE
    [](variables-and-statements.html#cb43-2)
    [](variables-and-statements.html#cb43-3)if (x == 10)
    [](variables-and-statements.html#cb43-4)    printf("This happens if x is 10\n");
    [](variables-and-statements.html#cb43-5)    printf("This happens ALWAYS\n");  // Surprise!! Unconditional!

`while` and `for` and the other looping constructs work the same way as the examples above. If you want to do multiple things in a loop or after an `if`, wrap them up in squirrelly braces.

In other words, the `if` is going to run the one thing after the `if`. And that one thing can be a single statement or a block of statements. 

### 3.3.1 The `if`-`else` statement

We’ve already been using `if` for multiple examples, since it’s likely you’ve seen it in a language before, but here’s another:
    
    
    [](variables-and-statements.html#cb44-1)int i = 10;
    [](variables-and-statements.html#cb44-2)
    [](variables-and-statements.html#cb44-3)if (i > 10) {
    [](variables-and-statements.html#cb44-4)    printf("Yes, i is greater than 10.\n");
    [](variables-and-statements.html#cb44-5)    printf("And this will also print if i is greater than 10.\n");
    [](variables-and-statements.html#cb44-6)}
    [](variables-and-statements.html#cb44-7)
    [](variables-and-statements.html#cb44-8)if (i <= 10) printf("i is less than or equal to 10.\n");

In the example code, the message will print if `i` is greater than 10, otherwise execution continues to the next line. Notice the squirrley braces after the `if` statement; if the condition is true, either the first statement or expression right after the if will be executed, or else the collection of code in the squirlley braces after the `if` will be executed. This sort of _code block_ behavior is common to all statements.

Of course, because C is fun this way, you can also do something if the condition is false with an `else` clause on your `if`:
    
    
    [](variables-and-statements.html#cb45-1)int i = 99;
    [](variables-and-statements.html#cb45-2)
    [](variables-and-statements.html#cb45-3)if (i == 10)
    [](variables-and-statements.html#cb45-4)    printf("i is 10!\n");
    [](variables-and-statements.html#cb45-5)else {
    [](variables-and-statements.html#cb45-6)    printf("i is decidedly not 10.\n");
    [](variables-and-statements.html#cb45-7)    printf("Which irritates me a little, frankly.\n");
    [](variables-and-statements.html#cb45-8)}

And you can even cascade these to test a variety of conditions, like this:
    
    
    [](variables-and-statements.html#cb46-1)int i = 99;
    [](variables-and-statements.html#cb46-2)
    [](variables-and-statements.html#cb46-3)if (i == 10)
    [](variables-and-statements.html#cb46-4)    printf("i is 10!\n");
    [](variables-and-statements.html#cb46-5)
    [](variables-and-statements.html#cb46-6)else if (i == 20)
    [](variables-and-statements.html#cb46-7)    printf("i is 20!\n");
    [](variables-and-statements.html#cb46-8)
    [](variables-and-statements.html#cb46-9)else if (i == 99) {
    [](variables-and-statements.html#cb46-10)    printf("i is 99! My favorite\n");
    [](variables-and-statements.html#cb46-11)    printf("I can't tell you how happy I am.\n");
    [](variables-and-statements.html#cb46-12)    printf("Really.\n");
    [](variables-and-statements.html#cb46-13)}
    [](variables-and-statements.html#cb46-14)    
    [](variables-and-statements.html#cb46-15)else
    [](variables-and-statements.html#cb46-16)    printf("i is some crazy number I've never heard of.\n");

Though if you’re going that route, be sure to check out the [`switch`](variables-and-statements.html#switch-statement) statement for a potentially better solution. The catch is `switch` only works with equality comparisons with constant numbers. The above `if`-`else` cascade could check inequality, ranges, variables, or anything else you can craft in a conditional expression. 

### 3.3.2 The `while` statement

`while` is your average run-of-the-mill looping construct. Do a thing while a condition expression is true.

Let’s do one!
    
    
    [](variables-and-statements.html#cb47-1)// Print the following output:
    [](variables-and-statements.html#cb47-2)//
    [](variables-and-statements.html#cb47-3)//   i is now 0!
    [](variables-and-statements.html#cb47-4)//   i is now 1!
    [](variables-and-statements.html#cb47-5)//   [ more of the same between 2 and 7 ]
    [](variables-and-statements.html#cb47-6)//   i is now 8!
    [](variables-and-statements.html#cb47-7)//   i is now 9!
    [](variables-and-statements.html#cb47-8)
    [](variables-and-statements.html#cb47-9)int i = 0;
    [](variables-and-statements.html#cb47-10)
    [](variables-and-statements.html#cb47-11)while (i < 10) {
    [](variables-and-statements.html#cb47-12)    printf("i is now %d!\n", i);
    [](variables-and-statements.html#cb47-13)    i++;
    [](variables-and-statements.html#cb47-14)}
    [](variables-and-statements.html#cb47-15)
    [](variables-and-statements.html#cb47-16)printf("All done!\n");

That gets you a basic loop. C also has a `for` loop which would have been cleaner for that example.

A not-uncommon use of `while` is for infinite loops where you repeat while true:
    
    
    [](variables-and-statements.html#cb48-1)while (1) {
    [](variables-and-statements.html#cb48-2)    printf("1 is always true, so this repeats forever.\n");
    [](variables-and-statements.html#cb48-3)}

### 3.3.3 The `do-while` statement

So now that we’ve gotten the `while` statement under control, let’s take a look at its closely related cousin, `do-while`.

They are basically the same, except if the loop condition is false on the first pass, `do-while` will execute once, but `while` won’t execute at all. In other words, the test to see whether or not to execute the block happens at the _end_ of the block with `do-while`. It happens at the _beginning_ of the block with `while`.

Let’s see by example:
    
    
    [](variables-and-statements.html#cb49-1)// Using a while statement:
    [](variables-and-statements.html#cb49-2)
    [](variables-and-statements.html#cb49-3)i = 10;
    [](variables-and-statements.html#cb49-4)
    [](variables-and-statements.html#cb49-5)// this is not executed because i is not less than 10:
    [](variables-and-statements.html#cb49-6)while(i < 10) {
    [](variables-and-statements.html#cb49-7)    printf("while: i is %d\n", i);
    [](variables-and-statements.html#cb49-8)    i++;
    [](variables-and-statements.html#cb49-9)}
    [](variables-and-statements.html#cb49-10)
    [](variables-and-statements.html#cb49-11)// Using a do-while statement:
    [](variables-and-statements.html#cb49-12)
    [](variables-and-statements.html#cb49-13)i = 10;
    [](variables-and-statements.html#cb49-14)
    [](variables-and-statements.html#cb49-15)// this is executed once, because the loop condition is not checked until
    [](variables-and-statements.html#cb49-16)// after the body of the loop runs:
    [](variables-and-statements.html#cb49-17)
    [](variables-and-statements.html#cb49-18)do {
    [](variables-and-statements.html#cb49-19)    printf("do-while: i is %d\n", i);
    [](variables-and-statements.html#cb49-20)    i++;
    [](variables-and-statements.html#cb49-21)} while (i < 10);
    [](variables-and-statements.html#cb49-22)
    [](variables-and-statements.html#cb49-23)printf("All done!\n");

Notice that in both cases, the loop condition is false right away. So in the `while`, the loop fails, and the following block of code is never executed. With the `do-while`, however, the condition is checked _after_ the block of code executes, so it always executes at least once. In this case, it prints the message, increments `i`, then fails the condition, and continues to the “All done!” output.

The moral of the story is this: if you want the loop to execute at least once, no matter what the loop condition, use `do-while`.

All these examples might have been better done with a `for` loop. Let’s do something less deterministic—repeat until a certain random number comes up!
    
    
    [](variables-and-statements.html#cb50-1)#include <stdio.h>   // For printf
    [](variables-and-statements.html#cb50-2)#include <stdlib.h>  // For rand
    [](variables-and-statements.html#cb50-3)
    [](variables-and-statements.html#cb50-4)int main(void)
    [](variables-and-statements.html#cb50-5){
    [](variables-and-statements.html#cb50-6)    int r;
    [](variables-and-statements.html#cb50-7)
    [](variables-and-statements.html#cb50-8)    do {
    [](variables-and-statements.html#cb50-9)        r = rand() % 100; // Get a random number between 0 and 99
    [](variables-and-statements.html#cb50-10)        printf("%d\n", r);
    [](variables-and-statements.html#cb50-11)    } while (r != 37);    // Repeat until 37 comes up
    [](variables-and-statements.html#cb50-12)}

Side note: did you run that more than once? If you did, did you notice the same sequence of numbers came up again. And again. And again? This is because `rand()` is a pseudorandom number generator that must be _seeded_ with a different number in order to generate a different sequence. Look up the [`srand()`](https://beej.us/guide/bgclr/html/split/stdlib.html#man-srand)[42](function-specifiers-alignment-specifiersoperators.html#fn42) function for more details. 

### 3.3.4 The `for` statement

Welcome to one of the most popular loops in the world! The `for` loop!

This is a great loop if you know the number of times you want to loop in advance.

You could do the same thing using just a `while` loop, but the `for` loop can help keep the code cleaner.

Here are two pieces of equivalent code—note how the `for` loop is just a more compact representation:
    
    
    [](variables-and-statements.html#cb51-1)// Print numbers between 0 and 9, inclusive...
    [](variables-and-statements.html#cb51-2)
    [](variables-and-statements.html#cb51-3)// Using a while statement:
    [](variables-and-statements.html#cb51-4)
    [](variables-and-statements.html#cb51-5)i = 0;
    [](variables-and-statements.html#cb51-6)while (i < 10) {
    [](variables-and-statements.html#cb51-7)    printf("i is %d\n", i);
    [](variables-and-statements.html#cb51-8)    i++;
    [](variables-and-statements.html#cb51-9)}
    [](variables-and-statements.html#cb51-10)
    [](variables-and-statements.html#cb51-11)// Do the exact same thing with a for-loop:
    [](variables-and-statements.html#cb51-12)
    [](variables-and-statements.html#cb51-13)for (i = 0; i < 10; i++) {
    [](variables-and-statements.html#cb51-14)    printf("i is %d\n", i);
    [](variables-and-statements.html#cb51-15)}

That’s right, folks—they do exactly the same thing. But you can see how the `for` statement is a little more compact and easy on the eyes. (JavaScript users will fully appreciate its C origins at this point.)

It’s split into three parts, separated by semicolons. The first is the initialization, the second is the loop condition, and the third is what should happen at the end of the block if the loop condition is true. All three of these parts are optional.
    
    
    [](variables-and-statements.html#cb52-1)for (initialize things; loop if this is true; do this after each loop)

Note that the loop will not execute even a single time if the loop condition starts off false.

> **`for`-loop fun fact!**
> 
> You can use the comma operator to do multiple things in each clause of the `for` loop!
>     
>     
>     [](variables-and-statements.html#cb53-1)for (i = 0, j = 999; i < 10; i++, j--) {
>     [](variables-and-statements.html#cb53-2)    printf("%d, %d\n", i, j);
>     [](variables-and-statements.html#cb53-3)}

An empty `for` will run forever:
    
    
    [](variables-and-statements.html#cb54-1)for(;;) {  // "forever"
    [](variables-and-statements.html#cb54-2)    printf("I will print this again and again and again\n" );
    [](variables-and-statements.html#cb54-3)    printf("for all eternity until the heat-death of the universe.\n");
    [](variables-and-statements.html#cb54-4)
    [](variables-and-statements.html#cb54-5)    printf("Or until you hit CTRL-C.\n");
    [](variables-and-statements.html#cb54-6)}

### 3.3.5 The `switch` Statement

Depending on what languages you’re coming from, you might or might not be familiar with `switch`, or C’s version might even be more restrictive than you’re used to. This is a statement that allows you to take a variety of actions depending on the value of an integer expression.

Basically, it evaluates an expression to an integer value, jumps to the `case` that corresponds to that value. Execution resumes from that point. If a `break` statement is encountered, then execution jumps out of the `switch`.

Here’s an example where, for a given number of goats, we print out a gut-feel of how many goats that is.
    
    
    [](variables-and-statements.html#cb55-1)#include <stdio.h>
    [](variables-and-statements.html#cb55-2)
    [](variables-and-statements.html#cb55-3)int main(void)
    [](variables-and-statements.html#cb55-4){
    [](variables-and-statements.html#cb55-5)    int goat_count = 2;
    [](variables-and-statements.html#cb55-6)
    [](variables-and-statements.html#cb55-7)    switch (goat_count) {
    [](variables-and-statements.html#cb55-8)        case 0:
    [](variables-and-statements.html#cb55-9)            printf("You have no goats.\n");
    [](variables-and-statements.html#cb55-10)            break;
    [](variables-and-statements.html#cb55-11)
    [](variables-and-statements.html#cb55-12)        case 1:
    [](variables-and-statements.html#cb55-13)            printf("You have a singular goat.\n");
    [](variables-and-statements.html#cb55-14)            break;
    [](variables-and-statements.html#cb55-15)
    [](variables-and-statements.html#cb55-16)        case 2:
    [](variables-and-statements.html#cb55-17)            printf("You have a brace of goats.\n");
    [](variables-and-statements.html#cb55-18)            break;
    [](variables-and-statements.html#cb55-19)
    [](variables-and-statements.html#cb55-20)        default:
    [](variables-and-statements.html#cb55-21)            printf("You have a bona fide plethora of goats!\n");
    [](variables-and-statements.html#cb55-22)            break;
    [](variables-and-statements.html#cb55-23)    }
    [](variables-and-statements.html#cb55-24)}

In that example, the `switch` will jump to the `case 2` and execute from there. When (if) it hits a `break`, it jumps out of the `switch`. 

Also, you might see that `default` label there at the bottom. This is what happens when no cases match.

Every `case`, including `default`, is optional. And they can occur in any order, but it’s really typical for `default`, if any, to be listed last.

So the whole thing acts like an `if`-`else` cascade:
    
    
    [](variables-and-statements.html#cb56-1)if (goat_count == 0)
    [](variables-and-statements.html#cb56-2)    printf("You have no goats.\n");
    [](variables-and-statements.html#cb56-3)else if (goat_count == 1)
    [](variables-and-statements.html#cb56-4)    printf("You have a singular goat.\n");
    [](variables-and-statements.html#cb56-5)else if (goat_count == 2)
    [](variables-and-statements.html#cb56-6)    printf("You have a brace of goats.\n");
    [](variables-and-statements.html#cb56-7)else
    [](variables-and-statements.html#cb56-8)    printf("You have a bona fide plethora of goats!\n");

With some key differences:

  * `switch` is often faster to jump to the correct code (though the spec makes no such guarantee).
  * `if`-`else` can do things like relational conditionals like `<` and `>=` and floating point and other types, while `switch` cannot.



There’s one more neat thing about switch that you sometimes see that is quite interesting: _fall through_.

Remember how `break` causes us to jump out of the switch?

Well, what happens if we _don’t_ `break`?

Turns out we just keep on going into the next `case`! Demo!
    
    
    [](variables-and-statements.html#cb57-1)switch (x) {
    [](variables-and-statements.html#cb57-2)    case 1:
    [](variables-and-statements.html#cb57-3)        printf("1\n");
    [](variables-and-statements.html#cb57-4)        // Fall through!
    [](variables-and-statements.html#cb57-5)    case 2:
    [](variables-and-statements.html#cb57-6)        printf("2\n");
    [](variables-and-statements.html#cb57-7)        break;
    [](variables-and-statements.html#cb57-8)    case 3:
    [](variables-and-statements.html#cb57-9)        printf("3\n");
    [](variables-and-statements.html#cb57-10)        break;
    [](variables-and-statements.html#cb57-11)}

If `x == 1`, this `switch` will first hit `case 1`, it’ll print the `1`, but then it just continues on to the next line of code… which prints `2`!

And then, at last, we hit a `break` so we jump out of the `switch`.

if `x == 2`, then we just hit the `case 2`, print `2`, and `break` as normal.

Not having a `break` is called _fall through_.

ProTip: _ALWAYS_ put a comment in the code where you intend to fall through, like I did above. It will save other programmers from wondering if you meant to do that. 

In fact, this is one of the common places to introduce bugs in C programs: forgetting to put a `break` in your `case`. You gotta do it if you don’t want to just roll into the next case[43](function-specifiers-alignment-specifiersoperators.html#fn43). 

Earlier I said that `switch` works with integer types—keep it that way. Don’t use floating point or string types in there. One loophole-ish thing here is that you can use character types because those are secretly integers themselves. So this is perfectly acceptable:
    
    
    [](variables-and-statements.html#cb58-1)char c = 'b';
    [](variables-and-statements.html#cb58-2)
    [](variables-and-statements.html#cb58-3)switch (c) {
    [](variables-and-statements.html#cb58-4)    case 'a':
    [](variables-and-statements.html#cb58-5)        printf("It's 'a'!\n");
    [](variables-and-statements.html#cb58-6)        break;
    [](variables-and-statements.html#cb58-7)
    [](variables-and-statements.html#cb58-8)    case 'b':
    [](variables-and-statements.html#cb58-9)        printf("It's 'b'!\n");
    [](variables-and-statements.html#cb58-10)        break;
    [](variables-and-statements.html#cb58-11)
    [](variables-and-statements.html#cb58-12)    case 'c':
    [](variables-and-statements.html#cb58-13)        printf("It's 'c'!\n");
    [](variables-and-statements.html#cb58-14)        break;
    [](variables-and-statements.html#cb58-15)}

Finally, you can use `enum`s in `switch` since they are also integer types. But more on that in the `enum` chapter.

* * *

[Prev](hello-world.html) | [Contents](index.html) | [Next](functions.html)

---

[Prev](variables-and-statements.html) | [Contents](index.html) | [Next](pointers.html)

* * *

# 4 Functions

> _“Sir, not in an environment such as this. That’s why I’ve also been programmed for over thirty secondary functions that—”_
> 
> —C3PO, before being rudely interrupted, reporting a now-unimpressive number of additional functions, _Star Wars_ script

Very much like other languages you’re used to, C has the concept of _functions_.

Functions can accept a variety of _arguments_ and return a value. One important thing, though: the arguments and return value types are predeclared—because that’s how C likes it!

Let’s take a look at a function. This is a function that takes an `int` as an argument, and returns an `int`.
    
    
    [](functions.html#cb59-1)#include <stdio.h>
    [](functions.html#cb59-2)
    [](functions.html#cb59-3)int plus_one(int n)  // The "definition"
    [](functions.html#cb59-4){
    [](functions.html#cb59-5)    return n + 1;
    [](functions.html#cb59-6)}
    [](functions.html#cb59-7) 

The `int` before the `plus_one` indicates the return type.

The `int n` indicates that this function takes one `int` argument, stored in _parameter_ `n`. A parameter is a special type of local variable into which the arguments are copied.

I’m going to drive home the point that the arguments are copied into the parameters, here. Lots of things in C are easier to understand if you know that the parameter is a _copy_ of the argument, not the argument itself. More on that in a minute.

Continuing the program down into `main()`, we can see the call to the function, where we assign the return value into local variable `j`:
    
    
    [](functions.html#cb60-8)int main(void)
    [](functions.html#cb60-9){
    [](functions.html#cb60-10)    int i = 10, j;
    [](functions.html#cb60-11)    
    [](functions.html#cb60-12)    j = plus_one(i);  // The "call"
    [](functions.html#cb60-13)
    [](functions.html#cb60-14)    printf("i + 1 is %d\n", j);
    [](functions.html#cb60-15)}

> Before I forget, notice that I defined the function before I used it. If I hadn’t done that, the compiler wouldn’t know about it yet when it compiles `main()` and it would have given an unknown function call error. There is a more proper way to do the above code with _function prototypes_ , but we’ll talk about that later.

Also notice that `main()` is a function!

It returns an `int`.

But what’s this `void` thing? This is a keyword that’s used to indicate that the function accepts no arguments.

You can also return `void` to indicate that you don’t return a value:
    
    
    [](functions.html#cb61-1)#include <stdio.h>
    [](functions.html#cb61-2)
    [](functions.html#cb61-3)// This function takes no arguments and returns no value:
    [](functions.html#cb61-4)
    [](functions.html#cb61-5)void hello(void)
    [](functions.html#cb61-6){
    [](functions.html#cb61-7)    printf("Hello, world!\n");
    [](functions.html#cb61-8)}
    [](functions.html#cb61-9)
    [](functions.html#cb61-10)int main(void)
    [](functions.html#cb61-11){
    [](functions.html#cb61-12)    hello();  // Prints "Hello, world!"
    [](functions.html#cb61-13)}

## 4.1 Passing by Value

I’d mentioned earlier that when you pass an argument to a function, a copy of that argument gets made and stored in the corresponding parameter.

If the argument is a variable, a copy of the value of that variable gets made and stored in the parameter.

More generally, the entire argument expression is evaluated and its value determined. That value is copied to the parameter.

In any case, the value in the parameter is its own thing. It is independent of whatever values or variables you used as arguments when you made the function call.

So let’s look at an example here. Study it and see if you can determine the output before running it:
    
    
    [](functions.html#cb62-1)#include <stdio.h>
    [](functions.html#cb62-2)
    [](functions.html#cb62-3)void increment(int a)
    [](functions.html#cb62-4){
    [](functions.html#cb62-5)    a++;
    [](functions.html#cb62-6)}
    [](functions.html#cb62-7)
    [](functions.html#cb62-8)int main(void)
    [](functions.html#cb62-9){
    [](functions.html#cb62-10)    int i = 10;
    [](functions.html#cb62-11)
    [](functions.html#cb62-12)    increment(i);
    [](functions.html#cb62-13)
    [](functions.html#cb62-14)    printf("i == %d\n", i);  // What does this print?
    [](functions.html#cb62-15)}

At first glance, it looks like `i` is `10`, and we pass it to the function `increment()`. There the value gets incremented, so when we print it, it must be `11`, right?

> _“Get used to disappointment.”_
> 
> —Dread Pirate Roberts, _The Princess Bride_

But it’s not `11`—it prints `10`! How?

It’s all about the fact that the expressions you pass to functions get _copied_ onto their corresponding parameters. The parameter is a copy, not the original.

So `i` is `10` out in `main()`. And we pass it to `increment()`. The corresponding parameter is called `a` in that function.

And the copy happens, as if by assignment. Loosely, `a = i`. So at that point, `a` is `10`. And out in `main()`, `i` is also `10`.

Then we increment `a` to `11`. But we’re not touching `i` at all! It remains `10`.

Finally, the function is complete. All its local variables are discarded (bye, `a`!) and we return to `main()`, where `i` is still `10`.

And we print it, getting `10`, and we’re done.

This is why in the previous example with the `plus_one()` function, we `return`ed the locally modified value so that we could see it again in `main()`.

Seems a little bit restrictive, huh? Like you can only get one piece of data back from a function, is what you’re thinking. There is, however, another way to get data back; C folks call it _passing by reference_ and that’s a story we’ll tell another time.

But no fancy-schmancy name will distract you from the fact that _EVERYTHING_ you pass to a function _WITHOUT EXCEPTION_ is copied into its corresponding parameter, and the function operates on that local copy, _NO MATTER WHAT_. Remember that, even when we’re talking about this so-called passing by reference. 

## 4.2 Function Prototypes

So if you recall back in the ice age a few sections ago, I mentioned that you had to define the function before you used it, otherwise the compiler wouldn’t know about it ahead of time, and would bomb out with an error.

This isn’t quite strictly true. You can notify the compiler in advance that you’ll be using a function of a certain type that has a certain parameter list. That way the function can be defined anywhere (even in a different file), as long as the _function prototype_ has been declared before you call that function.

Fortunately, the function prototype is really quite easy. It’s merely a copy of the first line of the function definition with a semicolon tacked on the end for good measure. For example, this code calls a function that is defined later, because a prototype has been declared first:
    
    
    [](functions.html#cb63-1)#include <stdio.h>
    [](functions.html#cb63-2)
    [](functions.html#cb63-3)int foo(void);  // This is the prototype!
    [](functions.html#cb63-4)
    [](functions.html#cb63-5)int main(void)
    [](functions.html#cb63-6){
    [](functions.html#cb63-7)    int i;
    [](functions.html#cb63-8)    
    [](functions.html#cb63-9)    // We can call foo() here before it's definition because the
    [](functions.html#cb63-10)    // prototype has already been declared, above!
    [](functions.html#cb63-11)
    [](functions.html#cb63-12)    i = foo();
    [](functions.html#cb63-13)    
    [](functions.html#cb63-14)    printf("%d\n", i);  // 3490
    [](functions.html#cb63-15)}
    [](functions.html#cb63-16)
    [](functions.html#cb63-17)int foo(void)  // This is the definition, just like the prototype!
    [](functions.html#cb63-18){
    [](functions.html#cb63-19)    return 3490;
    [](functions.html#cb63-20)}

If you don’t declare your function before you use it (either with a prototype or its definition), you’re performing something called an _implicit declaration_. This was allowed in the first C standard (C89), and that standard has rules about it, but is no longer allowed today. And there is no legitimate reason to rely on it in new code.

You might notice something about the sample code we’ve been using… That is, we’ve been using the good old `printf()` function without defining it or declaring a prototype! How do we get away with this lawlessness? We don’t, actually. There is a prototype; it’s in that header file `stdio.h` that we included with `#include`, remember? So we’re still legit, officer!

## 4.3 Empty Parameter Lists

You might see these from time to time in older code, but you shouldn’t ever code one up in new code. Always use `void` to indicate that a function takes no parameters. There’s never[44](function-specifiers-alignment-specifiersoperators.html#fn44) a reason to skip this in modern code.

If you’re good at just remembering to put `void` in for empty parameter lists in functions and prototypes, you can skip the rest of this section.

There are two contexts for this:

  * Omitting all parameters where the function is defined
  * Omitting all parameters in a prototype



Let’s look at a potential function definition first:
    
    
    [](functions.html#cb64-1)void foo()  // Should really have a `void` in there
    [](functions.html#cb64-2){
    [](functions.html#cb64-3)    printf("Hello, world!\n");
    [](functions.html#cb64-4)}

While the spec spells out that the behavior in this instance is _as-if_ you’d indicated `void` (C11 §6.7.6.3¶14), the `void` type is there for a reason. Use it.

But in the case of a function prototype, there is a _significant_ difference between using `void` and not:
    
    
    [](functions.html#cb65-1)void foo();
    [](functions.html#cb65-2)void foo(void);  // Not the same!

Leaving `void` out of the prototype indicates to the compiler that there is no additional information about the parameters to the function. It effectively turns off all that type checking.

With a prototype **definitely** use `void` when you have an empty parameter list.

* * *

[Prev](variables-and-statements.html) | [Contents](index.html) | [Next](pointers.html)

---

[Prev](functions.html) | [Contents](index.html) | [Next](arrays.html)

* * *

# 5 Pointers—Cower In Fear!

> _“How do you get to Carnegie Hall?”_  
>  _“Practice!”_
> 
> —20th-century joke of unknown origin

Pointers are one of the most feared things in the C language. In fact, they are the one thing that makes this language challenging at all. But why?

Because they, quite honestly, can cause electric shocks to come up through the keyboard and physically _weld_ your arms permanently in place, cursing you to a life at the keyboard in this language from the 70s!

Really? Well, not really. I’m just trying to set you up for success.

Depending on what language you came from, you might already understand the concept of _references_ , where a variable refers to an object of some type.

This is very much the same, except we have to be more explicit with C about when we’re talking about the reference or the thing it refers to.

## 5.1 Memory and Variables

Computer memory holds data of all kinds, right? It’ll hold `float`s, `int`s, or whatever you have. To make memory easy to cope with, each byte of memory is identified by an integer. These integers increase sequentially as you move up through memory[45](function-specifiers-alignment-specifiersoperators.html#fn45). You can think of it as a bunch of numbered boxes, where each box holds a byte[46](function-specifiers-alignment-specifiersoperators.html#fn46) of data. Or like a big array where each element holds a byte, if you come from a language with arrays. The number that represents each box is called its _address_.

Now, not all data types use just a byte. For instance, an `int` is often four bytes, as is a `float`, but it really depends on the system. You can use the `sizeof` operator to determine how many bytes of memory a certain type uses.
    
    
    [](pointers.html#cb66-1)// %zu is the format specifier for type size_t
    [](pointers.html#cb66-2)
    [](pointers.html#cb66-3)printf("an int uses %zu bytes of memory\n", sizeof(int));
    [](pointers.html#cb66-4)
    [](pointers.html#cb66-5)// That prints "4" for me, but can vary by system.

> **Memory Fun Facts** : When you have a data type (like your typical `int`) that uses more than a byte of memory, the bytes that make up the data are always adjacent to one another in memory. Sometimes they’re in the order that you expect, and sometimes they’re not[47](function-specifiers-alignment-specifiersoperators.html#fn47). While C doesn’t guarantee any particular memory order (it’s platform-dependent), it’s still generally possible to write code in a way that’s platform-independent where you don’t have to even consider these pesky byte orderings.

So _anyway_ , if we can get on with it and get a drum roll and some foreboding music playing for the definition of a pointer, _a pointer is a variable that holds an address_. Imagine the classical score from 2001: A Space Odyssey at this point. Ba bum ba bum ba bum BAAAAH!

Ok, so maybe a bit overwrought here, yes? There’s not a lot of mystery about pointers. They are the address of data. Just like an `int` variable can hold the value `12`, a pointer variable can hold the address of data.

This means that all these things mean the same thing, i.e. a number that represents a point in memory:

  * Index into memory (if you’re thinking of memory like a big array)
  * Address
  * Location



I’m going to use these interchangeably. And yes, I just threw _location_ in there because you can never have enough words that mean the same thing.

And a pointer variable holds that address number. Just like a `float` variable might hold `3.14159`.

Imagine you have a bunch of Post-it® notes all numbered in sequence with their address. (The first one is at index numbered `0`, the next at index `1`, and so on.)

In addition to the number representing their positions, you can also write another number of your choice on each. It could be the number of dogs you have. Or the number of moons around Mars…

…Or, _it could be the index of another Post-it note!_

If you have written the number of dogs you have, that’s just a regular variable. But if you wrote the index of another Post-it in there, _that’s a pointer_. It points to the other note!

Another analogy might be with house addresses. You can have a house with certain qualities, yard, metal roof, solar, etc. Or you could have the address of that house. The address isn’t the same as the house itself. One’s a full-blown house, and the other is just a few lines of text. But the address of the house is a _pointer_ to that house. It’s not the house itself, but it tells you where to find it.

And we can do the same thing in the computer with data. You can have a data variable that’s holding some value. And that value is in memory at some address. And you could have a different _pointer variable_ hold the address of that data variable.

It’s not the data variable itself, but, like with a house address, it tells us where to find it.

When we have that, we say we have a “pointer to” that data. And we can follow the pointer to access the data itself.

(Though it doesn’t seem particularly useful yet, this all becomes indispensable when used with function calls. Bear with me until we get there.)

So if we have an `int`, say, and we want a pointer to it, what we want is some way to get the address of that `int`, right? After all, the pointer just holds the _address of_ the data. What operator do you suppose we’d use to find the _address of_ the `int`?

Well, by a shocking surprise that must come as something of a shock to you, gentle reader, we use the `address-of` operator (which happens to be an ampersand: “`&`”)to find the address of the data. Ampersand.

So for a quick example, we’ll introduce a new _format specifier_ for `printf()` so you can print a pointer. You know already how `%d` prints a decimal integer, yes? Well, `%p` prints a pointer. Now, this pointer is going to look like a garbage number (and it might be printed in hexadecimal[48](function-specifiers-alignment-specifiersoperators.html#fn48) instead of decimal), but it is merely the index into memory the data is stored in. (Or the index into memory that the first byte of data is stored in, if the data is multi-byte.) In virtually all circumstances, including this one, the actual value of the number printed is unimportant to you, and I show it here only for demonstration of the `address-of` operator.
    
    
    [](pointers.html#cb67-1)#include <stdio.h>
    [](pointers.html#cb67-2)
    [](pointers.html#cb67-3)int main(void)
    [](pointers.html#cb67-4){
    [](pointers.html#cb67-5)    int i = 10;
    [](pointers.html#cb67-6)
    [](pointers.html#cb67-7)    printf("The value of i is %d\n", i);
    [](pointers.html#cb67-8)    printf("And its address is %p\n", (void *)&i);
    [](pointers.html#cb67-9)}

> **The above code contains a _cast_** where we coerce the type of the expression `&i` to be type `void*`. This is to keep the compiler from throwing a warning here. This is all stuff we haven’t covered yet, so just ignore the `(void*)` in the code above for now and pretend it’s not there.

On my computer, this prints:
    
    
    [](pointers.html#cb68-1)The value of i is 10
    [](pointers.html#cb68-2)And its address is 0x7ffddf7072a4

If you’re curious, that hexadecimal number is 140,727,326,896,068 in decimal (base 10 just like Grandma used to use). That’s the index into memory where the variable `i`’s data is stored. It’s the address of `i`. It’s the location of `i`. It’s a pointer to `i`.

> **Wait—you have 140 terabytes of RAM?** Yes! Don’t you? But I do fib my buns off; of course I don’t (ca. 2024). Modern computers use a miraculous technology called [virtual memory](https://en.wikipedia.org/wiki/Virtual_memory)[49](function-specifiers-alignment-specifiersoperators.html#fn49) that makes processes think they have the entire memory space of your computer to themselves, regardless of how much physical RAM backs it up. So even though the address was that huge number, it’s being mapped to some lower physical memory address by the virtual memory system of my CPU. This particular computer has 16 GB RAM (again, ca. 2024, but I’m running Linux, so that’s plenty). Terabytes of RAM? I’m a teacher, not a dot-com bazillionaire. None of this is anything any of us have to worry about except the part about me not being phenomenally wealthy.

It’s a pointer because it lets you know where `i` is in memory. Like a home address written on a scrap of paper tells you where you can find a particular house, this number indicates to us where in memory we can find the value of `i`. It points to `i`.

Again, we don’t really care what the address’s exact number is, generally. We just care that it’s a pointer to `i`.

## 5.2 Pointer Types

So… this is all well and good. You can now successfully take the address of a variable and print it on the screen. There’s a little something for the ol’ resume, right? Here’s where you grab me by the scruff of the neck and ask politely what the frick pointers are good for.

Excellent question, and we’ll get to that right after these messages from our sponsor.
    
    
    ACME ROBOTIC HOUSING UNIT CLEANING SERVICES. YOUR HOMESTEAD WILL BE
    DRAMATICALLY IMPROVED OR YOU WILL BE TERMINATED. MESSAGE ENDS.

Welcome back to another installment of Beej’s Guide. When we met last we were talking about how to make use of pointers. Well, what we’re going to do is store a pointer off in a variable so that we can use it later. You can identify the _pointer type_ because there’s an asterisk (`*`) before the variable name and after its type:
    
    
    [](pointers.html#cb70-1)int main(void)
    [](pointers.html#cb70-2){
    [](pointers.html#cb70-3)    int i;  // i's type is "int"
    [](pointers.html#cb70-4)    int *p; // p's type is "pointer to an int", or "int-pointer"
    [](pointers.html#cb70-5)}

Hey, so we have here a variable that is a pointer type, and it can point to other `int`s. That is, it can hold the address of other `int`s. We know it points to `int`s, since it’s of type `int*` (read “int-pointer”).

When you do an assignment into a pointer variable, the type of the right hand side of the assignment has to be the same type as the pointer variable. Fortunately for us, when you take the `address-of` a variable, the resultant type is a pointer to that variable type, so assignments like the following are perfect:
    
    
    [](pointers.html#cb71-1)int i;
    [](pointers.html#cb71-2)int *p;  // p is a pointer, but is uninitialized and points to garbage
    [](pointers.html#cb71-3)
    [](pointers.html#cb71-4)p = &i;  // p is assigned the address of i--p now "points to" i

On the left of the assignment, we have a variable of type pointer-to-`int` (`int*`), and on the right side, we have expression of type pointer-to-`int` since `i` is an `int` (because address-of `int` gives you a pointer to `int`). The address of a thing can be stored in a pointer to that thing.

Get it? I know it still doesn’t quite make much sense since you haven’t seen an actual use for the pointer variable, but we’re taking small steps here so that no one gets lost. So now, let’s introduce you to the anti-address-of operator. It’s kind of like what `address-of` would be like in Bizarro World.

## 5.3 Dereferencing

A pointer variable can be thought of as _referring_ to another variable by pointing to it. It’s rare you’ll hear anyone in C land talking about “referring” or “references”, but I bring it up just so that the name of this operator will make a little more sense.

When you have a pointer to a variable (roughly “a reference to a variable”), you can use the original variable through the pointer by _dereferencing_ the pointer. (You can think of this as “de-pointering” the pointer, but no one ever says “de-pointering”.)

Back to our analogy, this is vaguely like looking at a home address and then going to that house.

Now, what do I mean by “get access to the original variable”? Well, if you have a variable called `i`, and you have a pointer to `i` called `p`, you can use the dereferenced pointer `p` _exactly as if it were the original variable`i`_!

You almost have enough knowledge to handle an example. The last tidbit you need to know is actually this: what is the dereference operator? It’s actually called the _indirection operator_ , because you’re accessing values indirectly via the pointer. And it is the asterisk, again: `*`. Now, don’t get this confused with the asterisk you used in the pointer declaration, earlier. They are the same character, but they have different meanings in different contexts[50](function-specifiers-alignment-specifiersoperators.html#fn50).

Here’s a full-blown example:
    
    
    [](pointers.html#cb72-1)#include <stdio.h>
    [](pointers.html#cb72-2)
    [](pointers.html#cb72-3)int main(void)
    [](pointers.html#cb72-4){
    [](pointers.html#cb72-5)    int i;
    [](pointers.html#cb72-6)    int *p;  // this is NOT a dereference--this is a type "int*"
    [](pointers.html#cb72-7)
    [](pointers.html#cb72-8)    p = &i;  // p now points to i, p holds address of i
    [](pointers.html#cb72-9)
    [](pointers.html#cb72-10)    i = 10;  // i is now 10
    [](pointers.html#cb72-11)    *p = 20; // the thing p points to (namely i!) is now 20!!
    [](pointers.html#cb72-12)
    [](pointers.html#cb72-13)    printf("i is %d\n", i);   // prints "20"
    [](pointers.html#cb72-14)    printf("i is %d\n", *p);  // "20"! dereference-p is the same as i!
    [](pointers.html#cb72-15)}

Remember that `p` holds the address of `i`, as you can see where we did the assignment to `p` on line 8. What the indirection operator does is tells the computer to _use the object the pointer points to_ instead of using the pointer itself. In this way, we have turned `*p` into an alias of sorts for `i`.

Great, but _why_? Why do any of this?

## 5.4 Passing Pointers as Arguments

Right about now, you’re thinking that you have an awful lot of knowledge about pointers, but absolutely zero application, right? I mean, what use is `*p` if you could just simply say `i` instead?

Well, my friend, the real power of pointers comes into play when you start passing them to functions. Why is this a big deal? You might recall from before that you could pass all kinds of arguments to functions and they’d be dutifully copied into parameters, and then you could manipulate local copies of those variables from within the function, and then you could return a single value.

What if you wanted to bring back more than one single piece of data from the function? I mean, you can only return one thing, right? What if I answered that question with another question? …Er, two questions?

What happens when you pass a pointer as an argument to a function? Does a copy of the pointer get put into its corresponding parameter? _You bet your sweet peas it does._ Remember how earlier I rambled on and on about how _EVERY SINGLE ARGUMENT_ gets copied into parameters and the function uses a copy of the argument? Well, the same is true here. The function will get a copy of the pointer.

But, and this is the clever part: we will have set up the pointer in advance to point at a variable… and then the function can dereference its copy of the pointer to get back to the original variable! The function can’t see the variable itself, but it can certainly dereference a pointer to that variable!

This is analogous to writing a home address on a piece of paper, and then copying that onto another piece of paper. You now have _two_ pointers to that house, and both are equally good at getting you to the house itself.

In the case of a function call. one of the copies is stored in a pointer variable out in the calling scope, and the other is stored in a pointer variable that is the parameter of the function.

Example! Let’s revisit our old `increment()` function, but this time let’s make it so that it actually increments the value out in the caller.
    
    
    [](pointers.html#cb73-1)#include <stdio.h>
    [](pointers.html#cb73-2)
    [](pointers.html#cb73-3)void increment(int *p)  // note that it accepts a pointer to an int
    [](pointers.html#cb73-4){
    [](pointers.html#cb73-5)    *p = *p + 1;        // add one to the thing p points to
    [](pointers.html#cb73-6)}
    [](pointers.html#cb73-7)
    [](pointers.html#cb73-8)int main(void)
    [](pointers.html#cb73-9){
    [](pointers.html#cb73-10)    int i = 10;
    [](pointers.html#cb73-11)    int *j = &i;  // note the address-of; turns it into a pointer to i
    [](pointers.html#cb73-12)
    [](pointers.html#cb73-13)    printf("i is %d\n", i);        // prints "10"
    [](pointers.html#cb73-14)    printf("i is also %d\n", *j);  // prints "10"
    [](pointers.html#cb73-15)
    [](pointers.html#cb73-16)    increment(j);                  // j is an int*--to i
    [](pointers.html#cb73-17)
    [](pointers.html#cb73-18)    printf("i is %d\n", i);        // prints "11"!
    [](pointers.html#cb73-19)}

Ok! There are a couple things to see here… not the least of which is that the `increment()` function takes an `int*` as an argument. We pass it an `int*` in the call by changing the `int` variable `i` to an `int*` using the `address-of` operator. (Remember, a pointer holds an address, so we make pointers to variables by running them through the `address-of` operator.)

The `increment()` function gets a copy of the pointer. Both the original pointer `j` (in `main()`) and the copy of that pointer `p` (the parameter in `increment()`) point to the same address, namely the one holding the value `i`. (Again, by analogy, like two pieces of paper with the same home address written on them.) Dereferencing either will allow you to modify the original variable `i`! The function can modify a variable in another scope! Rock on!

The above example is often more concisely written in the call just by using address-of right in the argument list:
    
    
    [](pointers.html#cb74-1)printf("i is %d\n", i);  // prints "10"
    [](pointers.html#cb74-2)increment(&i);
    [](pointers.html#cb74-3)printf("i is %d\n", i);  // prints "11"!

As a general rule, if you want the function to modify the thing that you’re passing in such that you see the result, you’ll have to pass a pointer to that thing.

## 5.5 The `NULL` Pointer

Any pointer variable of any pointer type can be set to a special value called `NULL`. This indicates that this pointer doesn’t point to anything.
    
    
    [](pointers.html#cb75-1)int *p;
    [](pointers.html#cb75-2)
    [](pointers.html#cb75-3)p = NULL;

Since it doesn’t point to a value, dereferencing it is undefined behavior, and probably will result in a crash:
    
    
    [](pointers.html#cb76-1)int *p = NULL;
    [](pointers.html#cb76-2)
    [](pointers.html#cb76-3)*p = 12;  // CRASH or SOMETHING PROBABLY BAD. BEST AVOIDED.

Despite being called [the billion dollar mistake by its creator](https://en.wikipedia.org/wiki/Null_pointer#History)[51](function-specifiers-alignment-specifiersoperators.html#fn51), the `NULL` pointer is a good [sentinel value](https://en.wikipedia.org/wiki/Sentinel_value)[52](function-specifiers-alignment-specifiersoperators.html#fn52) and general indicator that a pointer hasn’t yet been initialized.

(Of course, like other variables, the pointer points to garbage unless you explicitly assign it to point to an address or `NULL`.) 

## 5.6 A Note on Declaring Pointers

The syntax for declaring a pointer can get a little weird. Let’s look at this example:
    
    
    [](pointers.html#cb77-1)int a;
    [](pointers.html#cb77-2)int b;

We can condense that into a single line, right?
    
    
    [](pointers.html#cb78-1)int a, b;  // Same thing

So `a` and `b` are both `int`s. No problem.

But what about this?
    
    
    [](pointers.html#cb79-1)int a;
    [](pointers.html#cb79-2)int *p;

Can we make that into one line? We can. But where does the `*` go?

The rule is that the `*` goes in front of any variable that is a pointer type. That is. the `*` is _not_ part of the `int` in this example. it’s a part of variable `p`.

With that in mind, we can write this:
    
    
    [](pointers.html#cb80-1)int a, *p;  // Same thing

It’s important to note that the following line does _not_ declare two pointers:
    
    
    [](pointers.html#cb81-1)int *p, q;  // p is a pointer to an int; q is just an int.

This can be particularly insidious-looking if the programmer writes this following (valid) line of code which is functionally identical to the one above.
    
    
    [](pointers.html#cb82-1)int* p, q;  // p is a pointer to an int; q is just an int.

So take a look at this and determine which variables are pointers and which are not:
    
    
    [](pointers.html#cb83-1)int *a, b, c, *d, e, *f, g, h, *i;

I’ll drop the answer in a footnote[53](function-specifiers-alignment-specifiersoperators.html#fn53).

## 5.7 `sizeof` and Pointers

Just a little bit of syntax here that might be confusing and you might see from time to time.

Recall that `sizeof` operates on the _type_ of the expression.
    
    
    [](pointers.html#cb84-1)int *p;
    [](pointers.html#cb84-2)
    [](pointers.html#cb84-3)// Prints size of an 'int'
    [](pointers.html#cb84-4)printf("%zu\n", sizeof(int));
    [](pointers.html#cb84-5)
    [](pointers.html#cb84-6)// p is type 'int *', so prints size of 'int*'
    [](pointers.html#cb84-7)printf("%zu\n", sizeof p);
    [](pointers.html#cb84-8)
    [](pointers.html#cb84-9)// *p is type 'int', so prints size of 'int'
    [](pointers.html#cb84-10)printf("%zu\n", sizeof *p);

You might see code in the wild with that last `sizeof` in there. Just remember that `sizeof` is all about the type of the expression, not the variables in the expression themselves.

* * *

[Prev](functions.html) | [Contents](index.html) | [Next](arrays.html)

---

[Prev](pointers.html) | [Contents](index.html) | [Next](strings.html)

* * *

# 6 Arrays

> _“Should array indices start at 0 or 1? My compromise of 0.5 was rejected without, I thought, proper consideration.”_
> 
> —Stan Kelly-Bootle, computer scientist

Luckily, C has arrays. I mean, I know it’s considered a low-level language[54](function-specifiers-alignment-specifiersoperators.html#fn54) but it does at least have the concept of arrays built-in. And since a great many languages drew inspiration from C’s syntax, you’re probably already familiar with using `[` and `]` for declaring and using arrays.

But C only _barely_ has arrays! As we’ll find out later, arrays are just syntactic sugar in C—they’re actually all pointers and stuff deep down. _Freak out!_ But for now, let’s just use them as arrays. _Phew_.

## 6.1 Easy Example

Let’s just crank out an example:
    
    
    [](arrays.html#cb85-1)#include <stdio.h>
    [](arrays.html#cb85-2)
    [](arrays.html#cb85-3)int main(void)
    [](arrays.html#cb85-4){
    [](arrays.html#cb85-5)    int i;
    [](arrays.html#cb85-6)    float f[4];  // Declare an array of 4 floats
    [](arrays.html#cb85-7)
    [](arrays.html#cb85-8)    f[0] = 3.14159;  // Indexing starts at 0, of course.
    [](arrays.html#cb85-9)    f[1] = 1.41421;
    [](arrays.html#cb85-10)    f[2] = 1.61803;
    [](arrays.html#cb85-11)    f[3] = 2.71828;
    [](arrays.html#cb85-12)
    [](arrays.html#cb85-13)    // Print them all out:
    [](arrays.html#cb85-14)
    [](arrays.html#cb85-15)    for (i = 0; i < 4; i++) {
    [](arrays.html#cb85-16)        printf("%f\n", f[i]);
    [](arrays.html#cb85-17)    }
    [](arrays.html#cb85-18)}

When you declare an array, you have to give it a size. And the size has to be fixed[55](function-specifiers-alignment-specifiersoperators.html#fn55).

In the above example, we made an array of 4 `float`s. The value in the square brackets in the declaration lets us know that.

Later on in subsequent lines, we access the values in the array, setting them or getting them, again with square brackets. 

Hopefully this looks familiar from languages you already know!

## 6.2 Getting the Length of an Array

You can’t…ish. C doesn’t record this information[56](function-specifiers-alignment-specifiersoperators.html#fn56). You have to manage it separately in another variable.

When I say “can’t”, I actually mean there are some circumstances when you _can_. There is a trick to get the number of elements in an array in the scope in which an array is declared. But, generally speaking, this won’t work the way you want if you pass the array to a function[57](function-specifiers-alignment-specifiersoperators.html#fn57).

Let’s take a look at this trick. The basic idea is that you take the `sizeof` the array, and then divide that by the size of each element to get the length. For example, if an `int` is 4 bytes, and the array is 32 bytes long, there must be room for \\(\frac{32}{4}\\) or \\(8\\) `int`s in there.
    
    
    [](arrays.html#cb86-1)int x[12];  // 12 ints
    [](arrays.html#cb86-2)
    [](arrays.html#cb86-3)printf("%zu\n", sizeof x);     // 48 total bytes
    [](arrays.html#cb86-4)printf("%zu\n", sizeof(int));  // 4 bytes per int
    [](arrays.html#cb86-5)
    [](arrays.html#cb86-6)printf("%zu\n", sizeof x / sizeof(int));  // 48/4 = 12 ints!

If it’s an array of `char`s, then `sizeof` the array _is_ the number of elements, since `sizeof(char)` is defined to be 1. For anything else, you have to divide by the size of each element.

But this trick only works in the scope in which the array was defined. If you pass the array to a function, it doesn’t work. Even if you make it “big” in the function signature:
    
    
    [](arrays.html#cb87-1)void foo(int x[12])
    [](arrays.html#cb87-2){
    [](arrays.html#cb87-3)    printf("%zu\n", sizeof x);     // 8?! What happened to 48?
    [](arrays.html#cb87-4)    printf("%zu\n", sizeof(int));  // 4 bytes per int
    [](arrays.html#cb87-5)
    [](arrays.html#cb87-6)    printf("%zu\n", sizeof x / sizeof(int));  // 8/4 = 2 ints?? WRONG.
    [](arrays.html#cb87-7)}

This is because when you “pass” arrays to functions, you’re only passing a pointer to the first element, and that’s what `sizeof` measures. More on this in the [Passing Single Dimensional Arrays to Functions](arrays.html#passing1darrays) section, below.

One more thing you can do with `sizeof` and arrays is get the size of an array of a fixed number of elements without declaring the array. This is like how you can get the size of an `int` with `sizeof(int)`.

For example, to see how many bytes would be needed for an array of 48 `double`s, you can do this:
    
    
    [](arrays.html#cb88-1)sizeof(double [48]);

## 6.3 Array Initializers

You can initialize an array with constants ahead of time:
    
    
    [](arrays.html#cb89-1)#include <stdio.h>
    [](arrays.html#cb89-2)
    [](arrays.html#cb89-3)int main(void)
    [](arrays.html#cb89-4){
    [](arrays.html#cb89-5)    int i;
    [](arrays.html#cb89-6)    int a[5] = {22, 37, 3490, 18, 95};  // Initialize with these values
    [](arrays.html#cb89-7)
    [](arrays.html#cb89-8)    for (i = 0; i < 5; i++) {
    [](arrays.html#cb89-9)        printf("%d\n", a[i]);
    [](arrays.html#cb89-10)    }
    [](arrays.html#cb89-11)}

You should never have more items in your initializer than there is room for in the array, or the compiler will get cranky:
    
    
    [](arrays.html#cb90-1)foo.c: In function ‘main’:
    [](arrays.html#cb90-2)foo.c:6:39: warning: excess elements in array initializer
    [](arrays.html#cb90-3)    6 |     int a[5] = {22, 37, 3490, 18, 95, 999};
    [](arrays.html#cb90-4)      |                                       ^~~
    [](arrays.html#cb90-5)foo.c:6:39: note: (near initialization for ‘a’)

But (fun fact!) you can have _fewer_ items in your initializer than there is room for in the array. The remaining elements in the array will be automatically initialized with zero. This is true in general for all types of array initializers: if you have an initializer, anything not explicitly set to a value will be set to zero.
    
    
    [](arrays.html#cb91-1)int a[5] = {22, 37, 3490};
    [](arrays.html#cb91-2)
    [](arrays.html#cb91-3)// is the same as:
    [](arrays.html#cb91-4)
    [](arrays.html#cb91-5)int a[5] = {22, 37, 3490, 0, 0};

It’s a common shortcut to see this in an initializer when you want to set an entire array to zero:
    
    
    [](arrays.html#cb92-1)int a[100] = {0};

Which means, “Make the first element zero, and then automatically make the rest zero, as well.”

You can set specific array elements in the initializer, as well, by specifying an index for the value! When you do this, C will happily keep initializing subsequent values for you until the initializer runs out, filling everything else with `0`.

To do this, put the index in square brackets with an `=` after, and then set the value.

Here’s an example where we build an array:
    
    
    [](arrays.html#cb93-1)int a[10] = {0, 11, 22, [5]=55, 66, 77};

Because we listed index 5 as the start for `55`, the resulting data in the array is:
    
    
    [](arrays.html#cb94-1)0 11 22 0 0 55 66 77 0 0

You can put simple constant expressions in there, as well.
    
    
    [](arrays.html#cb95-1)#define COUNT 5
    [](arrays.html#cb95-2)
    [](arrays.html#cb95-3)int a[COUNT] = {[COUNT-3]=3, 2, 1};

which gives us:
    
    
    [](arrays.html#cb96-1)0 0 3 2 1

Lastly, you can also have C compute the size of the array from the initializer, just by leaving the size off:
    
    
    [](arrays.html#cb97-1)int a[3] = {22, 37, 3490};
    [](arrays.html#cb97-2)
    [](arrays.html#cb97-3)// is the same as:
    [](arrays.html#cb97-4)
    [](arrays.html#cb97-5)int a[] = {22, 37, 3490};  // Left the size off!

## 6.4 Out of Bounds!

C doesn’t stop you from accessing arrays out of bounds. It might not even warn you.

Let’s steal the example from above and keep printing off the end of the array. It only has 5 elements, but let’s try to print 10 and see what happens:
    
    
    [](arrays.html#cb98-1)#include <stdio.h>
    [](arrays.html#cb98-2)
    [](arrays.html#cb98-3)int main(void)
    [](arrays.html#cb98-4){
    [](arrays.html#cb98-5)    int i;
    [](arrays.html#cb98-6)    int a[5] = {22, 37, 3490, 18, 95};
    [](arrays.html#cb98-7)
    [](arrays.html#cb98-8)    for (i = 0; i < 10; i++) {  // BAD NEWS: printing too many elements!
    [](arrays.html#cb98-9)        printf("%d\n", a[i]);
    [](arrays.html#cb98-10)    }
    [](arrays.html#cb98-11)}

Running it on my computer prints:
    
    
    [](arrays.html#cb99-1)22
    [](arrays.html#cb99-2)37
    [](arrays.html#cb99-3)3490
    [](arrays.html#cb99-4)18
    [](arrays.html#cb99-5)95
    [](arrays.html#cb99-6)32765
    [](arrays.html#cb99-7)1847052032
    [](arrays.html#cb99-8)1780534144
    [](arrays.html#cb99-9)-56487472
    [](arrays.html#cb99-10)21890

Yikes! What’s that? Well, turns out printing off the end of an array results in what C developers call _undefined behavior_. We’ll talk more about this beast later, but for now it means, “You’ve done something bad, and anything could happen during your program run.”

And by anything, I mean typically things like finding zeroes, finding garbage numbers, or crashing. But really the C spec says in this circumstance the compiler is allowed to emit code that does _anything_[ 58](function-specifiers-alignment-specifiersoperators.html#fn58).

Short version: don’t do anything that causes undefined behavior. Ever[59](function-specifiers-alignment-specifiersoperators.html#fn59). 

## 6.5 Multidimensional Arrays

You can add as many dimensions as you want to your arrays.
    
    
    [](arrays.html#cb100-1)int a[10];
    [](arrays.html#cb100-2)int b[2][7];
    [](arrays.html#cb100-3)int c[4][5][6];

These are stored in memory in [row-major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order)[60](function-specifiers-alignment-specifiersoperators.html#fn60). This means with a 2D array, the first index listed indicates the row, and the second the column.

You can also use initializers on multidimensional arrays by nesting them:
    
    
    [](arrays.html#cb101-1)#include <stdio.h>
    [](arrays.html#cb101-2)
    [](arrays.html#cb101-3)int main(void)
    [](arrays.html#cb101-4){
    [](arrays.html#cb101-5)    int row, col;
    [](arrays.html#cb101-6)
    [](arrays.html#cb101-7)    int a[2][5] = {      // Initialize a 2D array
    [](arrays.html#cb101-8)        {0, 1, 2, 3, 4},
    [](arrays.html#cb101-9)        {5, 6, 7, 8, 9}
    [](arrays.html#cb101-10)    };
    [](arrays.html#cb101-11)
    [](arrays.html#cb101-12)    for (row = 0; row < 2; row++) {
    [](arrays.html#cb101-13)        for (col = 0; col < 5; col++) {
    [](arrays.html#cb101-14)            printf("(%d,%d) = %d\n", row, col, a[row][col]);
    [](arrays.html#cb101-15)        }
    [](arrays.html#cb101-16)    }
    [](arrays.html#cb101-17)}

For output of:
    
    
    [](arrays.html#cb102-1)(0,0) = 0
    [](arrays.html#cb102-2)(0,1) = 1
    [](arrays.html#cb102-3)(0,2) = 2
    [](arrays.html#cb102-4)(0,3) = 3
    [](arrays.html#cb102-5)(0,4) = 4
    [](arrays.html#cb102-6)(1,0) = 5
    [](arrays.html#cb102-7)(1,1) = 6
    [](arrays.html#cb102-8)(1,2) = 7
    [](arrays.html#cb102-9)(1,3) = 8
    [](arrays.html#cb102-10)(1,4) = 9

And you can initialize with explicit indexes:
    
    
    [](arrays.html#cb103-1)// Make a 3x3 identity matrix
    [](arrays.html#cb103-2)
    [](arrays.html#cb103-3)int a[3][3] = {[0][0]=1, [1][1]=1, [2][2]=1};

which builds a 2D array like this:
    
    
    [](arrays.html#cb104-1)1 0 0
    [](arrays.html#cb104-2)0 1 0
    [](arrays.html#cb104-3)0 0 1

## 6.6 Arrays and Pointers

[_Casually_] So… I kinda might have mentioned up there that arrays were pointers, deep down? We should take a shallow dive into that now so that things aren’t completely confusing. Later on, we’ll look at what the real relationship between arrays and pointers is, but for now I just want to look at passing arrays to functions.

### 6.6.1 Getting a Pointer to an Array

I want to tell you a secret. Generally speaking, when a C programmer talks about a pointer to an array, they’re talking about a pointer _to the first element_ of the array[61](function-specifiers-alignment-specifiersoperators.html#fn61).

So let’s get a pointer to the first element of an array.
    
    
    [](arrays.html#cb105-1)#include <stdio.h>
    [](arrays.html#cb105-2)
    [](arrays.html#cb105-3)int main(void)
    [](arrays.html#cb105-4){
    [](arrays.html#cb105-5)    int a[5] = {11, 22, 33, 44, 55};
    [](arrays.html#cb105-6)    int *p;
    [](arrays.html#cb105-7)
    [](arrays.html#cb105-8)    p = &a[0];  // p points to the array
    [](arrays.html#cb105-9)                // Well, to the first element, actually
    [](arrays.html#cb105-10)
    [](arrays.html#cb105-11)    printf("%d\n", *p);  // Prints "11"
    [](arrays.html#cb105-12)}

This is so common to do in C that the language allows us a shorthand:
    
    
    [](arrays.html#cb106-1)p = &a[0];  // p points to the array
    [](arrays.html#cb106-2)
    [](arrays.html#cb106-3)// is the same as:
    [](arrays.html#cb106-4)
    [](arrays.html#cb106-5)p = a;      // p points to the array, but much nicer-looking!

Just referring to the array name in isolation is the same as getting a pointer to the first element of the array! We’re going to use this extensively in the upcoming examples.

But hold on a second—isn’t `p` an `int*`? And `*p` gives us `11`, same as `a[0]`? Yessss. You’re starting to get a glimpse of how arrays and pointers are related in C. (We’ll talk about this a lot more in the [Pointers II](pointers2.html#pointers2) chapter, under [Array/Pointer Equivalence](pointers2.html#arraypointerequiv).) 

### 6.6.2 Passing Single Dimensional Arrays to Functions

Let’s do an example with a single dimensional array. I’m going to write a couple functions that we can pass the array to that do different things.

Prepare for some mind-blowing function signatures!
    
    
    [](arrays.html#cb107-1)#include <stdio.h>
    [](arrays.html#cb107-2)
    [](arrays.html#cb107-3)// Passing as a pointer to the first element
    [](arrays.html#cb107-4)void times2(int *a, int len)
    [](arrays.html#cb107-5){
    [](arrays.html#cb107-6)    for (int i = 0; i < len; i++)
    [](arrays.html#cb107-7)        printf("%d\n", a[i] * 2);
    [](arrays.html#cb107-8)}
    [](arrays.html#cb107-9)
    [](arrays.html#cb107-10)// Same thing, but using array notation
    [](arrays.html#cb107-11)void times3(int a[], int len)
    [](arrays.html#cb107-12){
    [](arrays.html#cb107-13)    for (int i = 0; i < len; i++)
    [](arrays.html#cb107-14)        printf("%d\n", a[i] * 3);
    [](arrays.html#cb107-15)}
    [](arrays.html#cb107-16)
    [](arrays.html#cb107-17)// Same thing, but using array notation with size
    [](arrays.html#cb107-18)void times4(int a[5], int len)
    [](arrays.html#cb107-19){
    [](arrays.html#cb107-20)    for (int i = 0; i < len; i++)
    [](arrays.html#cb107-21)        printf("%d\n", a[i] * 4);
    [](arrays.html#cb107-22)}
    [](arrays.html#cb107-23)
    [](arrays.html#cb107-24)int main(void)
    [](arrays.html#cb107-25){
    [](arrays.html#cb107-26)    int x[5] = {11, 22, 33, 44, 55};
    [](arrays.html#cb107-27)
    [](arrays.html#cb107-28)    times2(x, 5);
    [](arrays.html#cb107-29)    times3(x, 5);
    [](arrays.html#cb107-30)    times4(x, 5);
    [](arrays.html#cb107-31)}

All those methods of listing the array as a parameter in the function are identical.
    
    
    [](arrays.html#cb108-1)void times2(int *a, int len)
    [](arrays.html#cb108-2)void times3(int a[], int len)
    [](arrays.html#cb108-3)void times4(int a[5], int len)

In usage by C regulars, the first is the most common, by far.

And, in fact, in the latter situation, the compiler doesn’t even care what number you pass in (other than it has to be greater than zero[62](function-specifiers-alignment-specifiersoperators.html#fn62)). It doesn’t enforce anything at all.

Now that I’ve said that, the size of the array in the function declaration actually _does_ matter when you’re passing multidimensional arrays into functions, but let’s come back to that. 

### 6.6.3 Changing Arrays in Functions

We’ve said that arrays are just pointers in disguise. This means that if you pass an array to a function, you’re likely passing a pointer to the first element in the array.

But if the function has a pointer to the data, it is able to manipulate that data! So changes that a function makes to an array will be visible back out in the caller.

Here’s an example where we pass a pointer to an array to a function, the function manipulates the values in that array, and those changes are visible out in the caller.
    
    
    [](arrays.html#cb109-1)#include <stdio.h>
    [](arrays.html#cb109-2)
    [](arrays.html#cb109-3)void double_array(int *a, int len)
    [](arrays.html#cb109-4){
    [](arrays.html#cb109-5)    // Multiply each element by 2
    [](arrays.html#cb109-6)    //
    [](arrays.html#cb109-7)    // This doubles the values in x in main() since x and a both point
    [](arrays.html#cb109-8)    // to the same array in memory!
    [](arrays.html#cb109-9)
    [](arrays.html#cb109-10)    for (int i = 0; i < len; i++)
    [](arrays.html#cb109-11)        a[i] *= 2;
    [](arrays.html#cb109-12)}
    [](arrays.html#cb109-13)
    [](arrays.html#cb109-14)int main(void)
    [](arrays.html#cb109-15){
    [](arrays.html#cb109-16)    int x[5] = {1, 2, 3, 4, 5};
    [](arrays.html#cb109-17)
    [](arrays.html#cb109-18)    double_array(x, 5);
    [](arrays.html#cb109-19)
    [](arrays.html#cb109-20)    for (int i = 0; i < 5; i++)
    [](arrays.html#cb109-21)        printf("%d\n", x[i]);  // 2, 4, 6, 8, 10!
    [](arrays.html#cb109-22)}

Even though we passed the array in as parameter `a` which is type `int*`, look at how we access it using array notation with `a[i]`! Whaaaat. This is totally allowed.

Later when we talk about the equivalence between arrays and pointers, we’ll see how this makes a lot more sense. For now, it’s enough to know that functions can make changes to arrays that are visible out in the caller. 

### 6.6.4 Passing Multidimensional Arrays to Functions

The story changes a little when we’re talking about multidimensional arrays. C needs to know all the dimensions (except the first one) so it has enough information to know where in memory to look to find a value.

Here’s an example where we’re explicit with all the dimensions:
    
    
    [](arrays.html#cb110-1)#include <stdio.h>
    [](arrays.html#cb110-2)
    [](arrays.html#cb110-3)void print_2D_array(int a[2][3])
    [](arrays.html#cb110-4){
    [](arrays.html#cb110-5)    for (int row = 0; row < 2; row++) {
    [](arrays.html#cb110-6)        for (int col = 0; col < 3; col++)
    [](arrays.html#cb110-7)            printf("%d ", a[row][col]);
    [](arrays.html#cb110-8)        printf("\n");
    [](arrays.html#cb110-9)    }
    [](arrays.html#cb110-10)}
    [](arrays.html#cb110-11)
    [](arrays.html#cb110-12)int main(void)
    [](arrays.html#cb110-13){
    [](arrays.html#cb110-14)    int x[2][3] = {
    [](arrays.html#cb110-15)        {1, 2, 3},
    [](arrays.html#cb110-16)        {4, 5, 6}
    [](arrays.html#cb110-17)    };
    [](arrays.html#cb110-18)
    [](arrays.html#cb110-19)    print_2D_array(x);
    [](arrays.html#cb110-20)}

But in this case, these two[63](function-specifiers-alignment-specifiersoperators.html#fn63) are equivalent:
    
    
    [](arrays.html#cb111-1)void print_2D_array(int a[2][3])
    [](arrays.html#cb111-2)void print_2D_array(int a[][3])

The compiler really only needs the second dimension so it can figure out how far in memory to skip for each increment of the first dimension. In general, it needs to know all the dimensions except the first one.

Also, remember that the compiler does minimal compile-time bounds checking (if you’re lucky), and C does zero runtime checking of bounds. No seat belts! Don’t crash by accessing array elements out of bounds! 

* * *

[Prev](pointers.html) | [Contents](index.html) | [Next](strings.html)

---

[Prev](arrays.html) | [Contents](index.html) | [Next](structs.html)

* * *

# 7 Strings

Finally! Strings! What could be simpler?

Well, turns out strings aren’t actually strings in C. That’s right! They’re pointers! Of course they are!

Much like arrays, strings in C _barely exist_.

But let’s check it out—it’s not really such a big deal.

## 7.1 String Literals

Before we start, let’s talk about string literals in C. These are sequences of characters in _double_ quotes (`"`). (Single quotes enclose characters, and are a different animal entirely.)

Examples:
    
    
    [](strings.html#cb112-1)"Hello, world!\n"
    [](strings.html#cb112-2)"This is a test."
    [](strings.html#cb112-3)"When asked if this string had quotes in it, she replied, \"It does.\""

The first one has a newline at the end—quite a common thing to see.

The last one has quotes embedded within it, but you see each is preceded by (we say “escaped by”) a backslash (`\`) indicating that a literal quote belongs in the string at this point. This is how the C compiler can tell the difference between printing a double quote and the double quote at the end of the string.

## 7.2 String Variables

Now that we know how to make a string literal, let’s assign it to a variable so we can do something with it.
    
    
    [](strings.html#cb113-1)char *s = "Hello, world!";

Check out that type: pointer to a `char`. The string variable `s` is actually a pointer to the first character in that string, namely the `H`.

And we can print it with the `%s` (for “string”) format specifier:
    
    
    [](strings.html#cb114-1)char *s = "Hello, world!";
    [](strings.html#cb114-2)
    [](strings.html#cb114-3)printf("%s\n", s);  // "Hello, world!"

## 7.3 String Variables as Arrays

Another option is this, nearly equivalent to the above `char*` usage:
    
    
    [](strings.html#cb115-1)char s[14] = "Hello, world!";
    [](strings.html#cb115-2)
    [](strings.html#cb115-3)// or, if we were properly lazy and have the compiler
    [](strings.html#cb115-4)// figure the length for us:
    [](strings.html#cb115-5)
    [](strings.html#cb115-6)char s[] = "Hello, world!";

This means you can use array notation to access characters in a string. Let’s do exactly that to print all the characters in a string on the same line:
    
    
    [](strings.html#cb116-1)#include <stdio.h>
    [](strings.html#cb116-2)
    [](strings.html#cb116-3)int main(void)
    [](strings.html#cb116-4){
    [](strings.html#cb116-5)    char s[] = "Hello, world!";
    [](strings.html#cb116-6)
    [](strings.html#cb116-7)    for (int i = 0; i < 13; i++)
    [](strings.html#cb116-8)        printf("%c", s[i]);
    [](strings.html#cb116-9)    printf("\n");
    [](strings.html#cb116-10)}

Note that we’re using the format specifier `%c` to print a single character.

Also, check this out. The program will still work fine if we change the definition of `s` to be a `char*` type:
    
    
    [](strings.html#cb117-1)#include <stdio.h>
    [](strings.html#cb117-2)
    [](strings.html#cb117-3)int main(void)
    [](strings.html#cb117-4){
    [](strings.html#cb117-5)    char *s = "Hello, world!";   // char* here
    [](strings.html#cb117-6)
    [](strings.html#cb117-7)    for (int i = 0; i < 13; i++)
    [](strings.html#cb117-8)        printf("%c", s[i]);    // But still use arrays here...?
    [](strings.html#cb117-9)    printf("\n");
    [](strings.html#cb117-10)}

And we still can use array notation to get the job done when printing it out! This is surprising, but is still only because we haven’t talked about array/pointer equivalence yet. But this is yet another hint that arrays and pointers are the same thing, deep down. 

## 7.4 String Initializers

We’ve already seen some examples with initializing string variables with string literals:
    
    
    [](strings.html#cb118-1)char *s = "Hello, world!";
    [](strings.html#cb118-2)char t[] = "Hello, again!";

But these two initialization s are subtly different. A string literal, similar to an integer literal, has its memory automatically managed by the compiler for you! With an integer, i.e. a fixed size piece of data, the compiler can pretty easily manage it. But strings are a variable-byte beast which the compiler tames by tossing into a chunk of memory, and giving you a pointer to it.

This form points to wherever that string was placed. Typically, that place is in a land faraway from the rest of your program’s memory – read-only memory – for reasons related to performance & safety.
    
    
    [](strings.html#cb119-1)char *s = "Hello, world!";

So, if you try to mutate that string with this:
    
    
    [](strings.html#cb120-1)char *s = "Hello, world!";
    [](strings.html#cb120-2)
    [](strings.html#cb120-3)s[0] = 'z';  // BAD NEWS: tried to mutate a string literal!

The behavior is undefined. Probably, depending on your system, a crash will result.

But declaring it as an array is different. The compiler doesn’t stow those bytes in another part of town, they’re right down the street. This one is a mutable _copy_ of the string – one we can change at will:
    
    
    [](strings.html#cb121-1)char t[] = "Hello, again!";  // t is an array copy of the string 
    [](strings.html#cb121-2)t[0] = 'z'; //  No problem
    [](strings.html#cb121-3)
    [](strings.html#cb121-4)printf("%s\n", t);  // "zello, again!"

So remember: if you have a pointer to a string literal, don’t try to change it! And if you use a string in double quotes to initialize an array, that’s not actually a string literal. 

## 7.5 Getting String Length

You can’t, since C doesn’t track it for you. And when I say “can’t”, I actually mean “can”[64](function-specifiers-alignment-specifiersoperators.html#fn64). There’s a function in `<string.h>` called `strlen()` that can be used to compute the length of any string in bytes[65](function-specifiers-alignment-specifiersoperators.html#fn65).
    
    
    [](strings.html#cb122-1)#include <stdio.h>
    [](strings.html#cb122-2)#include <string.h>
    [](strings.html#cb122-3)
    [](strings.html#cb122-4)int main(void)
    [](strings.html#cb122-5){
    [](strings.html#cb122-6)    char *s = "Hello, world!";
    [](strings.html#cb122-7)
    [](strings.html#cb122-8)    printf("The string is %zu bytes long.\n", strlen(s));
    [](strings.html#cb122-9)}

The `strlen()` function returns type `size_t`, which is an integer type so you can use it for integer math. We print `size_t` with `%zu`.

The above program prints:
    
    
    [](strings.html#cb123-1)The string is 13 bytes long.

Great! So it _is_ possible to get the string length! 

But… if C doesn’t track the length of the string anywhere, how does it know how long the string is?

## 7.6 String Termination

C does strings a little differently than many programming languages, and in fact differently than almost every modern programming language.

When you’re making a new language, you have basically two options for storing a string in memory:

  1. Store the bytes of the string along with a number indicating the length of the string.

  2. Store the bytes of the string, and mark the end of the string with a special byte called the _terminator_.




If you want strings longer than 255 characters, option 1 requires at least two bytes to store the length. Whereas option 2 only requires one byte to terminate the string. So a bit of savings there.

Of course, these days it seems ridiculous to worry about saving a byte (or 3—lots of languages will happily let you have strings that are 4 gigabytes in length). But back in the day, it was a bigger deal.

So C took approach #2. In C, a “string” is defined by two basic characteristics:

  * A pointer to the first character in the string.
  * A zero-valued byte (or `NUL` character[66](function-specifiers-alignment-specifiersoperators.html#fn66)) somewhere in memory after the pointer that indicates the end of the string.



A `NUL` character can be written in C code as `\0`, though you don’t often have to do this.

When you include a string in double quotes in your code, the `NUL` character is automatically, implicitly included.
    
    
    [](strings.html#cb124-1)char *s = "Hello!";  // Actually "Hello!\0" behind the scenes

So with this in mind, let’s write our own `strlen()` function that counts `char`s in a string until it finds a `NUL`.

The procedure is to look down the string for a single `NUL` character, counting as we go[67](function-specifiers-alignment-specifiersoperators.html#fn67):
    
    
    [](strings.html#cb125-1)int my_strlen(char *s)
    [](strings.html#cb125-2){
    [](strings.html#cb125-3)    int count = 0;
    [](strings.html#cb125-4)
    [](strings.html#cb125-5)    while (s[count] != '\0')  // Single quotes for single char
    [](strings.html#cb125-6)        count++;
    [](strings.html#cb125-7)
    [](strings.html#cb125-8)    return count;
    [](strings.html#cb125-9)}

And that’s basically how the built-in `strlen()` gets the job done. 

## 7.7 Copying a String

You can’t copy a string through the assignment operator (`=`). All that does is make a copy of the pointer to the first character… so you end up with two pointers to the same string:
    
    
    [](strings.html#cb126-1)#include <stdio.h>
    [](strings.html#cb126-2)
    [](strings.html#cb126-3)int main(void)
    [](strings.html#cb126-4){
    [](strings.html#cb126-5)    char s[] = "Hello, world!";
    [](strings.html#cb126-6)    char *t;
    [](strings.html#cb126-7)
    [](strings.html#cb126-8)    // This makes a copy of the pointer, not a copy of the string!
    [](strings.html#cb126-9)    t = s;
    [](strings.html#cb126-10)
    [](strings.html#cb126-11)    // We modify t
    [](strings.html#cb126-12)    t[0] = 'z';
    [](strings.html#cb126-13)
    [](strings.html#cb126-14)    // But printing s shows the modification!
    [](strings.html#cb126-15)    // Because t and s point to the same string!
    [](strings.html#cb126-16)
    [](strings.html#cb126-17)    printf("%s\n", s);  // "zello, world!"
    [](strings.html#cb126-18)}

If you want to make a copy of a string, you have to copy it a byte at a time—this means that you’re going to take the individual bytes of the string from one place in memory and duplicate them somewhere else in memory. This is made easier with the `strcpy()` function.[68](function-specifiers-alignment-specifiersoperators.html#fn68)

Before you copy the string, make sure you have room to copy it into, i.e. the destination array that’s going to hold the characters needs to be at least as long as the string you’re copying.
    
    
    [](strings.html#cb127-1)#include <stdio.h>
    [](strings.html#cb127-2)#include <string.h>
    [](strings.html#cb127-3)
    [](strings.html#cb127-4)int main(void)
    [](strings.html#cb127-5){
    [](strings.html#cb127-6)    char s[] = "Hello, world!";
    [](strings.html#cb127-7)    char t[100];  // Each char is one byte, so plenty of room
    [](strings.html#cb127-8)
    [](strings.html#cb127-9)    // This makes a copy of the string!
    [](strings.html#cb127-10)    strcpy(t, s);
    [](strings.html#cb127-11)
    [](strings.html#cb127-12)    // We modify t
    [](strings.html#cb127-13)    t[0] = 'z';
    [](strings.html#cb127-14)
    [](strings.html#cb127-15)    // And s remains unaffected because it's a different string
    [](strings.html#cb127-16)    printf("%s\n", s);  // "Hello, world!"
    [](strings.html#cb127-17)
    [](strings.html#cb127-18)    // But t has been changed
    [](strings.html#cb127-19)    printf("%s\n", t);  // "zello, world!"
    [](strings.html#cb127-20)}

Notice with `strcpy()`, the destination pointer is the first argument, and the source pointer is the second. A mnemonic I use to remember this is that it’s the order you would have put `t` and `s` if an assignment `=` worked for strings, with the source on the right and the destination on the left. 

* * *

[Prev](arrays.html) | [Contents](index.html) | [Next](structs.html)

---

[Prev](strings.html) | [Contents](index.html) | [Next](file-inputoutput.html)

* * *

# 8 Structs

In C, we have something called a `struct`, which is a user-definable type that holds multiple pieces of data, potentially of different types.

It’s a convenient way to bundle multiple variables into a single one. This can be beneficial for passing variables to functions (so you just have to pass one instead of many), and useful for organizing data and making code more readable.

If you’ve come from another language, you might be familiar with the idea of _classes_ and _objects_. These don’t exist in C, natively[69](function-specifiers-alignment-specifiersoperators.html#fn69). You can think of a `struct` as a class with only data members, and no methods.

## 8.1 Declaring a Struct

You can declare a `struct` in your code like so:
    
    
    [](structs.html#cb128-1)struct car {
    [](structs.html#cb128-2)    char *name;
    [](structs.html#cb128-3)    float price;
    [](structs.html#cb128-4)    int speed;
    [](structs.html#cb128-5)};

This is often done at the global scope outside any functions so that the `struct` is globally available.

When you do this, you’re making a new _type_. The full type name is `struct car`. (Not just `car`—that won’t work.)

There aren’t any variables of that type yet, but we can declare some:
    
    
    [](structs.html#cb129-1)struct car saturn;  // Variable "saturn" of type "struct car"

And now we have an uninitialized variable `saturn`[70](function-specifiers-alignment-specifiersoperators.html#fn70) of type `struct car`.

We should initialize it! But how do we set the values of those individual fields?

Like in many other languages that stole it from C, we’re going to use the dot operator (`.`) to access the individual fields.
    
    
    [](structs.html#cb130-1)saturn.name = "Saturn SL/2";
    [](structs.html#cb130-2)saturn.price = 15999.99;
    [](structs.html#cb130-3)saturn.speed = 175;
    [](structs.html#cb130-4)
    [](structs.html#cb130-5)printf("Name:           %s\n", saturn.name);
    [](structs.html#cb130-6)printf("Price (USD):    %f\n", saturn.price);
    [](structs.html#cb130-7)printf("Top Speed (km): %d\n", saturn.speed);

There on the first lines, we set the values in the `struct car`, and then in the next bit, we print those values out. 

## 8.2 Struct Initializers

That example in the previous section was a little unwieldy. There must be a better way to initialize that `struct` variable!

You can do it with an initializer by putting values in for the fields _in the order they appear in the`struct`_ when you define the variable. (This won’t work after the variable has been defined—it has to happen in the definition).
    
    
    [](structs.html#cb131-1)struct car {
    [](structs.html#cb131-2)    char *name;
    [](structs.html#cb131-3)    float price;
    [](structs.html#cb131-4)    int speed;
    [](structs.html#cb131-5)};
    [](structs.html#cb131-6)
    [](structs.html#cb131-7)// Now with an initializer! Same field order as in the struct declaration:
    [](structs.html#cb131-8)struct car saturn = {"Saturn SL/2", 16000.99, 175};
    [](structs.html#cb131-9)
    [](structs.html#cb131-10)printf("Name:      %s\n", saturn.name);
    [](structs.html#cb131-11)printf("Price:     %f\n", saturn.price);
    [](structs.html#cb131-12)printf("Top Speed: %d km\n", saturn.speed);

The fact that the fields in the initializer need to be in the same order is a little freaky. If someone changes the order in `struct car`, it could break all the other code!

We can be more specific with our initializers:
    
    
    [](structs.html#cb132-1)struct car saturn = {.speed=175, .name="Saturn SL/2"};

Now it’s independent of the order in the `struct` declaration. Which is safer code, for sure.

Similar to array initializers, any missing field designators are initialized to zero (in this case, that would be `.price`, which I’ve omitted). 

## 8.3 Passing Structs to Functions

You can do a couple things to pass a `struct` to a function.

  1. Pass the `struct`.
  2. Pass a pointer to the `struct`.



Recall that when you pass something to a function, a _copy_ of that thing gets made for the function to operate on, whether it’s a copy of a pointer, an `int`, a `struct`, or anything.

There are basically two cases when you’d want to pass a pointer to the `struct`:

  1. You need the function to be able to make changes to the `struct` that was passed in, and have those changes show in the caller.
  2. The `struct` is somewhat large and it’s more expensive to copy that onto the stack than it is to just copy a pointer[71](function-specifiers-alignment-specifiersoperators.html#fn71).



For those two reasons, it’s far more common to pass a pointer to a `struct` to a function, though its by no means illegal to pass the `struct` itself.

Let’s try passing in a pointer, making a function that will allow you to set the `.price` field of the `struct car`:
    
    
    [](structs.html#cb133-1)#include <stdio.h>
    [](structs.html#cb133-2)
    [](structs.html#cb133-3)struct car {
    [](structs.html#cb133-4)    char *name;
    [](structs.html#cb133-5)    float price;
    [](structs.html#cb133-6)    int speed;
    [](structs.html#cb133-7)};
    [](structs.html#cb133-8)
    [](structs.html#cb133-9)int main(void)
    [](structs.html#cb133-10){
    [](structs.html#cb133-11)    struct car saturn = {.speed=175, .name="Saturn SL/2"};
    [](structs.html#cb133-12)
    [](structs.html#cb133-13)    // Pass a pointer to this struct car, along with a new,
    [](structs.html#cb133-14)    // more realistic, price:
    [](structs.html#cb133-15)    set_price(&saturn, 799.99);
    [](structs.html#cb133-16)
    [](structs.html#cb133-17)    printf("Price: %f\n", saturn.price);
    [](structs.html#cb133-18)}

You should be able to come up with the function signature for `set_price()` just by looking at the types of the arguments we have there.

`saturn` is a `struct car`, so `&saturn` must be the address of the `struct car`, AKA a pointer to a `struct car`, namely a `struct car*`.

And `799.99` is a `float`.

So the function declaration must look like this:
    
    
    [](structs.html#cb134-1)void set_price(struct car *c, float new_price)

We just need to write the body. One attempt might be:
    
    
    [](structs.html#cb135-1)void set_price(struct car *c, float new_price) {
    [](structs.html#cb135-2)    c.price = new_price;  // ERROR!!
    [](structs.html#cb135-3)}

That won’t work because the dot operator only works on `struct`s… it doesn’t work on _pointers_ to `struct`s.

Ok, so we can dereference the variable `c` to de-pointer it to get to the `struct` itself. Dereferencing a `struct car*` results in the `struct car` that the pointer points to, which we should be able to use the dot operator on:
    
    
    [](structs.html#cb136-1)void set_price(struct car *c, float new_price) {
    [](structs.html#cb136-2)    (*c).price = new_price;  // Works, but is ugly and non-idiomatic :(
    [](structs.html#cb136-3)}

And that works! But it’s a little clunky to type all those parens and the asterisk. C has some syntactic sugar called the _arrow operator_ that helps with that. 

## 8.4 The Arrow Operator

The arrow operator helps refer to fields in pointers to `struct`s.
    
    
    [](structs.html#cb137-1)void set_price(struct car *c, float new_price) {
    [](structs.html#cb137-2)    // (*c).price = new_price;  // Works, but non-idiomatic :(
    [](structs.html#cb137-3)    //
    [](structs.html#cb137-4)    // The line above is 100% equivalent to the one below:
    [](structs.html#cb137-5)
    [](structs.html#cb137-6)    c->price = new_price;  // That's the one!
    [](structs.html#cb137-7)}

So when accessing fields, when do we use dot and when do we use arrow?

  * If you have a `struct`, use dot (`.`).
  * If you have a pointer to a `struct`, use arrow (`->`). 



## 8.5 Copying and Returning `struct`s

Here’s an easy one for you!

Just assign from one to the other!
    
    
    [](structs.html#cb138-1)struct car a, b;
    [](structs.html#cb138-2)
    [](structs.html#cb138-3)b = a;  // Copy the struct

And returning a `struct` (as opposed to a pointer to one) from a function also makes a similar copy to the receiving variable.

This is not a “deep copy”[72](function-specifiers-alignment-specifiersoperators.html#fn72). All fields are copied as-is, including pointers to things. 

## 8.6 Comparing `struct`s

There’s only one safe way to do it: compare each field one at a time.

You might think you could use [`memcmp()`](https://beej.us/guide/bgclr/html/split/stringref.html#man-strcmp)[73](function-specifiers-alignment-specifiersoperators.html#fn73), but that doesn’t handle the case of the possible [padding bytes](structs-ii-more-fun-with-structs.html#struct-padding-bytes) that might be in there.

If you clear the `struct` to zero first with [`memset()`](https://beej.us/guide/bgclr/html/split/stringref.html#man-memset)[74](function-specifiers-alignment-specifiersoperators.html#fn74), then it _might_ work, though there could be weird elements that [might not compare as you expect](https://stackoverflow.com/questions/141720/how-do-you-compare-structs-for-equality-in-c)[75](function-specifiers-alignment-specifiersoperators.html#fn75). 

* * *

[Prev](strings.html) | [Contents](index.html) | [Next](file-inputoutput.html)

---

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

---

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

---

[Prev](typedef-making-new-types.html) | [Contents](index.html) | [Next](manual-memory-allocation.html)

* * *

# 11 Pointers II: Arithmetic

Time to get more into it with a number of new pointer topics! If you’re not up to speed with pointers, [check out the first section in the guide on the matter](pointers.html#pointers).

## 11.1 Pointer Arithmetic

Turns out you can do math on pointers, notably addition and subtraction.

But what does it mean when you do that?

In short, if you have a pointer to a type, adding one to the pointer moves to the next item of that type directly after it in memory.

It’s **important** to remember that as we move pointers around and look at different places in memory, we need to make sure that we’re always pointing to a valid place in memory before we dereference. If we’re off in the weeds and we try to see what’s there, the behavior is undefined and a crash is a common result.

This is a little chicken-and-eggy with [Array/Pointer Equivalence, below](pointers2.html#arraypointerequiv), but we’re going to give it a shot, anyway.

### 11.1.1 Adding to Pointers

First, let’s take an array of numbers.
    
    
    [](pointers2.html#cb172-1)int a[5] = {11, 22, 33, 44, 55};

Then let’s get a pointer to the first element in that array:
    
    
    [](pointers2.html#cb173-1)int a[5] = {11, 22, 33, 44, 55};
    [](pointers2.html#cb173-2)
    [](pointers2.html#cb173-3)int *p = &a[0];  // Or "int *p = a;" works just as well

Then let’s print the value there by dereferencing the pointer:
    
    
    [](pointers2.html#cb174-1)printf("%d\n", *p);  // Prints 11

Now let’s use pointer arithmetic to print the next element in the array, the one at index 1:
    
    
    [](pointers2.html#cb175-1)printf("%d\n", *(p + 1));  // Prints 22!!

What happened there? C knows that `p` is a pointer to an `int`. So it knows the `sizeof` an `int`[84](function-specifiers-alignment-specifiersoperators.html#fn84) and it knows to skip that many bytes to get to the next `int` after the first one!

In fact, the prior example could be written these two equivalent ways:
    
    
    [](pointers2.html#cb176-1)printf("%d\n", *p);        // Prints 11
    [](pointers2.html#cb176-2)printf("%d\n", *(p + 0));  // Prints 11

because adding `0` to a pointer results in the same pointer.

Let’s think of the upshot here. We can iterate over elements of an array this way instead of using an array:
    
    
    [](pointers2.html#cb177-1)int a[5] = {11, 22, 33, 44, 55};
    [](pointers2.html#cb177-2)
    [](pointers2.html#cb177-3)int *p = &a[0];  // Or "int *p = a;" works just as well
    [](pointers2.html#cb177-4)
    [](pointers2.html#cb177-5)for (int i = 0; i < 5; i++) {
    [](pointers2.html#cb177-6)    printf("%d\n", *(p + i));  // Same as p[i]!
    [](pointers2.html#cb177-7)}

And that works the same as if we used array notation! Oooo! Getting closer to that array/pointer equivalence thing! More on this later in this chapter.

But what’s actually happening, here? How does it work?

Remember from early on that memory is like a big array, where a byte is stored at each array index?

And the array index into memory has a few names:

  * Index into memory
  * Location
  * Address
  * _Pointer!_



So a pointer is an index into memory, somewhere.

For a random example, say that a number 3490 was stored at address (“index”) 23,237,489,202. If we have an `int` pointer to that 3490, that value of that pointer is 23,237,489,202… because the pointer is the memory address. Different words for the same thing.

And now let’s say we have another number, 4096, stored right after the 3490 at address 23,237,489,210 (8 higher than the 3490 because each `int` in this example is 8 bytes long).

If we add `1` to that pointer, it actually jumps ahead `sizeof(int)` bytes to the next `int`. It knows to jump that far ahead because it’s an `int` pointer. If it were a `float` pointer, it’d jump `sizeof(float)` bytes ahead to get to the next float!

So you can look at the next `int`, by adding `1` to the pointer, the one after that by adding `2` to the pointer, and so on.

### 11.1.2 Changing Pointers

We saw how we could add an integer to a pointer in the previous section. This time, let’s _modify the pointer, itself_.

You can just add (or subtract) integer values directly to (or from) any pointer!

Let’s do that example again, except with a couple changes. First, I’m going to add a `999` to the end of our numbers to act as a sentinel value. This will let us know where the end of the data is.
    
    
    [](pointers2.html#cb178-1)int a[] = {11, 22, 33, 44, 55, 999};  // Add 999 here as a sentinel
    [](pointers2.html#cb178-2)
    [](pointers2.html#cb178-3)int *p = &a[0];  // p points to the 11

And we also have `p` pointing to the element at index `0` of `a`, namely `11`, just like before.

Now—let’s start _incrementing_ `p` so that it points at subsequent elements of the array. We’ll do this until `p` points to the `999`; that is, we’ll do it until `*p == 999`:
    
    
    [](pointers2.html#cb179-1)while (*p != 999) {       // While the thing p points to isn't 999
    [](pointers2.html#cb179-2)    printf("%d\n", *p);   // Print it
    [](pointers2.html#cb179-3)    p++;                  // Move p to point to the next int!
    [](pointers2.html#cb179-4)}

Pretty crazy, right?

When we give it a run, first `p` points to `11`. Then we increment `p`, and it points to `22`, and then again, it points to `33`. And so on, until it points to `999` and we quit.

### 11.1.3 Subtracting Pointers

You can subtract a value from a pointer to get to earlier address, as well, just like we were adding to them before.

But we can also subtract two pointers to find the difference between them, e.g. we can calculate how many `int`s there are between two `int*`s. The catch is that this only works within a single array[85](function-specifiers-alignment-specifiersoperators.html#fn85)—if the pointers point to anything else, you get undefined behavior.

Remember how strings are `char*`s in C? Let’s see if we can use this to write another variant of `strlen()` to compute the length of a string that utilizes pointer subtraction.

The idea is that if we have a pointer to the beginning of the string, we can find a pointer to the end of the string by scanning ahead for the `NUL` character.

And if we have a pointer to the beginning of the string, and we computed the pointer to the end of the string, we can just subtract the two pointers to come up with the length!
    
    
    [](pointers2.html#cb180-1)#include <stdio.h>
    [](pointers2.html#cb180-2)
    [](pointers2.html#cb180-3)int my_strlen(char *s)
    [](pointers2.html#cb180-4){
    [](pointers2.html#cb180-5)    // Start scanning from the beginning of the string
    [](pointers2.html#cb180-6)    char *p = s;
    [](pointers2.html#cb180-7)
    [](pointers2.html#cb180-8)    // Scan until we find the NUL character
    [](pointers2.html#cb180-9)    while (*p != '\0')
    [](pointers2.html#cb180-10)        p++;
    [](pointers2.html#cb180-11)
    [](pointers2.html#cb180-12)    // Return the difference in pointers
    [](pointers2.html#cb180-13)    return p - s;
    [](pointers2.html#cb180-14)}
    [](pointers2.html#cb180-15)
    [](pointers2.html#cb180-16)int main(void)
    [](pointers2.html#cb180-17){
    [](pointers2.html#cb180-18)    printf("%d\n", my_strlen("Hello, world!"));  // Prints "13"
    [](pointers2.html#cb180-19)}

Remember that you can only use pointer subtraction between two pointers that point to the same array! 

## 11.2 Array/Pointer Equivalence

We’re finally ready to talk about this! We’ve seen plenty of examples of places where we’ve intermixed array notation, but let’s give out the _fundamental formula of array/pointer equivalence_ :
    
    
    [](pointers2.html#cb181-1)a[b] == *(a + b)

Study that! Those are equivalent and can be used interchangeably!

I’ve oversimplified a bit, because in my above example `a` and `b` can both be expressions, and we might want a few more parentheses to force order of operations in case the expressions are complex.

The spec is specific, as always, declaring (in C11 §6.5.2.1¶2):

> `E1[E2]` is identical to `(*((E1)+(E2)))`

but that’s a little harder to grok. Just make sure you include parentheses if the expressions are complicated so all your math happens in the right order.

This means we can _decide_ if we’re going to use array or pointer notation for any array or pointer (assuming it points to an element of an array).

Let’s use an array and pointer with both array and pointer notation:
    
    
    [](pointers2.html#cb182-1)#include <stdio.h>
    [](pointers2.html#cb182-2)
    [](pointers2.html#cb182-3)int main(void)
    [](pointers2.html#cb182-4){
    [](pointers2.html#cb182-5)    int a[] = {11, 22, 33, 44, 55};
    [](pointers2.html#cb182-6)
    [](pointers2.html#cb182-7)    int *p = a;  // p points to the first element of a, 11
    [](pointers2.html#cb182-8)
    [](pointers2.html#cb182-9)    // Print all elements of the array a variety of ways:
    [](pointers2.html#cb182-10)
    [](pointers2.html#cb182-11)    for (int i = 0; i < 5; i++)
    [](pointers2.html#cb182-12)        printf("%d\n", a[i]);      // Array notation with a
    [](pointers2.html#cb182-13)
    [](pointers2.html#cb182-14)    for (int i = 0; i < 5; i++)
    [](pointers2.html#cb182-15)        printf("%d\n", p[i]);      // Array notation with p
    [](pointers2.html#cb182-16)
    [](pointers2.html#cb182-17)    for (int i = 0; i < 5; i++)
    [](pointers2.html#cb182-18)        printf("%d\n", *(a + i));  // Pointer notation with a
    [](pointers2.html#cb182-19)
    [](pointers2.html#cb182-20)    for (int i = 0; i < 5; i++)
    [](pointers2.html#cb182-21)        printf("%d\n", *(p + i));  // Pointer notation with p
    [](pointers2.html#cb182-22)
    [](pointers2.html#cb182-23)    for (int i = 0; i < 5; i++)
    [](pointers2.html#cb182-24)        printf("%d\n", *(p++));    // Moving pointer p
    [](pointers2.html#cb182-25)        //printf("%d\n", *(a++));    // Moving array variable a--ERROR!
    [](pointers2.html#cb182-26)}

So you can see that in general, if you have an array variable, you can use pointer or array notion to access elements. Same with a pointer variable.

The one big difference is that you can _modify_ a pointer to point to a different address, but you can’t do that with an array variable.  In other words, you can’t assign into an array variable at all—only into individual elements of that array.

If you really want to copy one array to another, you have to use a function like `memcpy()` (or a loop) to make that happen.

### 11.2.1 Array/Pointer Equivalence in Function Calls

This is where you’ll encounter this concept the most, for sure.

If you have a function that takes a pointer argument, e.g.:
    
    
    [](pointers2.html#cb183-1)int my_strlen(char *s)

this means you can pass either an array or a pointer to this function and have it work!
    
    
    [](pointers2.html#cb184-1)char s[] = "Antelopes";
    [](pointers2.html#cb184-2)char *t = "Wombats";
    [](pointers2.html#cb184-3)
    [](pointers2.html#cb184-4)printf("%d\n", my_strlen(s));  // Works!
    [](pointers2.html#cb184-5)printf("%d\n", my_strlen(t));  // Works, too!

And it’s also why these two function signatures are equivalent:
    
    
    [](pointers2.html#cb185-1)int my_strlen(char *s)    // Works!
    [](pointers2.html#cb185-2)int my_strlen(char s[])   // Works, too!

## 11.3 `void` Pointers

You’ve already seen the `void` keyword used with functions that indicates no parameters or no return value, but this is an entirely separate, unrelated animal.

A `void*` is definitely a pointer to an existing _thing_. But the `void` part of it indicates that we don’t know the _type_ of the thing. And sometimes, believe it or not, that’s really useful. It enables us to write code that’s a little more type-agnostic, which is some nice flexibility to have in a typed language like C.

There are basically two use cases for this—let’s check them out and see if we can demystify it a bit.

  1. A function is going to operate on something byte-by-byte. For example, `memcpy()` copies bytes of memory from one pointer to another, but those pointers can point to any type. `memcpy()` takes advantage of the fact that if you iterate through `char*`s, you’re iterating through the bytes of an object no matter what type the object is. More on this in the [Multibyte Values](pointers-iii-pointers-to-pointers-and-more.html#multibyte-values) subsection.

  2. Another function is calling a function you passed to it (a callback), and it’s passing you data. You know the type of the data, but the function calling you doesn’t. So it passes you `void*`s—’cause it doesn’t know the type—and you convert those to the type you need. The built-in [`qsort()`](https://beej.us/guide/bgclr/html/split/stdlib.html#man-qsort)[86](function-specifiers-alignment-specifiersoperators.html#fn86) and [`bsearch()`](https://beej.us/guide/bgclr/html/split/stdlib.html#man-bsearch)[87](function-specifiers-alignment-specifiersoperators.html#fn87) use this technique.




Let’s look at an example, the built-in `memcpy()` function:
    
    
    [](pointers2.html#cb186-1)void *memcpy(void *s1, void *s2, size_t n);

This function copies `n` bytes of memory starting from address `s2` into the memory starting at address `s1`.

But look! `s1` and `s2` are `void*`s! Why? What does it mean? Let’s run more examples to see.

For instance, we could copy a string with `memcpy()` (though `strcpy()` is more appropriate for strings):
    
    
    [](pointers2.html#cb187-1)#include <stdio.h>
    [](pointers2.html#cb187-2)#include <string.h>
    [](pointers2.html#cb187-3)
    [](pointers2.html#cb187-4)int main(void)
    [](pointers2.html#cb187-5){
    [](pointers2.html#cb187-6)    char s[] = "Goats!";
    [](pointers2.html#cb187-7)    char t[100];
    [](pointers2.html#cb187-8)
    [](pointers2.html#cb187-9)    memcpy(t, s, 7);  // Copy 7 bytes--including the NUL terminator!
    [](pointers2.html#cb187-10)
    [](pointers2.html#cb187-11)    printf("%s\n", t);  // "Goats!"
    [](pointers2.html#cb187-12)}

Or we can copy some `int`s:
    
    
    [](pointers2.html#cb188-1)#include <stdio.h>
    [](pointers2.html#cb188-2)#include <string.h>
    [](pointers2.html#cb188-3)
    [](pointers2.html#cb188-4)int main(void)
    [](pointers2.html#cb188-5){
    [](pointers2.html#cb188-6)    int a[] = {11, 22, 33};
    [](pointers2.html#cb188-7)    int b[3];
    [](pointers2.html#cb188-8)
    [](pointers2.html#cb188-9)    memcpy(b, a, 3 * sizeof(int));  // Copy 3 ints of data
    [](pointers2.html#cb188-10)
    [](pointers2.html#cb188-11)    printf("%d\n", b[1]);  // 22
    [](pointers2.html#cb188-12)}

That one’s a little wild—you see what we did there with `memcpy()`? We copied the data from `a` to `b`, but we had to specify how many _bytes_ to copy, and an `int` is more than one byte.

OK, then—how many bytes does an `int` take? Answer: depends on the system. But we can tell how many bytes any type takes with the `sizeof` operator.

So there’s the answer: an `int` takes `sizeof(int)` bytes of memory to store.

And if we have 3 of them in our array, like we did in that example, the entire space used for the 3 `int`s must be `3 * sizeof(int)`.

(In the string example, earlier, it would have been more technically accurate to copy `7 * sizeof(char)` bytes. But `char`s are always one byte large, by definition, so that just devolves into `7 * 1`.)

We could even copy a `float` or a `struct` with `memcpy()`! (Though this is abusive—we should just use `=` for that):
    
    
    [](pointers2.html#cb189-1)struct antelope my_antelope;
    [](pointers2.html#cb189-2)struct antelope my_clone_antelope;
    [](pointers2.html#cb189-3)
    [](pointers2.html#cb189-4)// ...
    [](pointers2.html#cb189-5)
    [](pointers2.html#cb189-6)memcpy(&my_clone_antelope, &my_antelope, sizeof my_antelope);

Look at how versatile `memcpy()` is! If you have a pointer to a source and a pointer to a destination, and you have the number of bytes you want to copy, you can copy _any type of data_.

Imagine if we didn’t have `void*`. We’d have to write specialized `memcpy()` functions for each type:
    
    
    [](pointers2.html#cb190-1)memcpy_int(int *a, int *b, int count);
    [](pointers2.html#cb190-2)memcpy_float(float *a, float *b, int count);
    [](pointers2.html#cb190-3)memcpy_double(double *a, double *b, int count);
    [](pointers2.html#cb190-4)memcpy_char(char *a, char *b, int count);
    [](pointers2.html#cb190-5)memcpy_unsigned_char(unsigned char *a, unsigned char *b, int count);
    [](pointers2.html#cb190-6)
    [](pointers2.html#cb190-7)// etc... blech!

Much better to just use `void*` and have one function that can do it all.

That’s the power of `void*`. You can write a function that doesn’t care about the variable’s type and is still able to do things with it.

But with great power comes great responsibility. Maybe not _that_ great in this case, but there are some limits.

  1. You cannot do pointer arithmetic on a `void*`.
  2. You cannot dereference a `void*`.
  3. You cannot use the arrow operator on a `void*`, since it’s also a dereference.
  4. You cannot use array notation on a `void*`, since it’s also a dereference, as well[88](function-specifiers-alignment-specifiersoperators.html#fn88).



And if you think about it, these rules make sense. All those operations rely on knowing the `sizeof` the type of data pointed to, and with `void*`, we don’t know the size of the data being pointed to—it could be anything!

But wait—if you can’t dereference a `void*` what good can it ever do you?

Like with `memcpy()`, it helps you write generic functions that can handle multiple types of data. But the secret is that, deep down, _you convert the`void*` to another type before you use it_!

And conversion is easy: you can just assign into a variable of the desired type[89](function-specifiers-alignment-specifiersoperators.html#fn89).
    
    
    [](pointers2.html#cb191-1)char a = 'X';  // A single char
    [](pointers2.html#cb191-2)
    [](pointers2.html#cb191-3)void *p = &a;  // p points to the 'X'
    [](pointers2.html#cb191-4)char *q = p;   // q also points to the 'X'
    [](pointers2.html#cb191-5)
    [](pointers2.html#cb191-6)printf("%c\n", *p);  // ERROR--cannot dereference void*!
    [](pointers2.html#cb191-7)printf("%c\n", *q);  // Prints "X"

Let’s write our own `memcpy()` to try this out. We can copy bytes (`char`s), and we know the number of bytes because it’s passed in.
    
    
    [](pointers2.html#cb192-1)void *my_memcpy(void *dest, void *src, int byte_count)
    [](pointers2.html#cb192-2){
    [](pointers2.html#cb192-3)    // Convert void*s to char*s
    [](pointers2.html#cb192-4)    char *s = src, *d = dest;
    [](pointers2.html#cb192-5)
    [](pointers2.html#cb192-6)    // Now that we have char*s, we can dereference and copy them
    [](pointers2.html#cb192-7)    while (byte_count--) {
    [](pointers2.html#cb192-8)        *d++ = *s++;
    [](pointers2.html#cb192-9)    }
    [](pointers2.html#cb192-10)
    [](pointers2.html#cb192-11)    // Most of these functions return the destination, just in case
    [](pointers2.html#cb192-12)    // that's useful to the caller.
    [](pointers2.html#cb192-13)    return dest;
    [](pointers2.html#cb192-14)}

Right there at the beginning, we copy the `void*`s into `char*`s so that we can use them as `char*`s. It’s as easy as that.

Then some fun in a while loop, where we decrement `byte_count` until it becomes false (`0`). Remember that with post-decrement, the value of the expression is computed (for `while` to use) and _then_ the variable is decremented.

And some fun in the copy, where we assign `*d = *s` to copy the byte, but we do it with post-increment so that both `d` and `s` move to the next byte after the assignment is made.

Lastly, most memory and string functions return a copy of a pointer to the destination just in case the caller wants to use it.

Now that we’ve done that, I just want to quickly point out that we can use this technique to iterate over the bytes of _any_ object in C, `float`s, `struct`s, or anything! 

Let’s run one more real-world example with the built-in `qsort()` routine that can sort _anything_ thanks to the magic of `void*`s.

(In the following example, you can ignore the word `const`, which we haven’t covered yet.)
    
    
    [](pointers2.html#cb193-1)#include <stdio.h>
    [](pointers2.html#cb193-2)#include <stdlib.h>
    [](pointers2.html#cb193-3)
    [](pointers2.html#cb193-4)// The type of structure we're going to sort
    [](pointers2.html#cb193-5)struct animal {
    [](pointers2.html#cb193-6)    char *name;
    [](pointers2.html#cb193-7)    int leg_count;
    [](pointers2.html#cb193-8)};
    [](pointers2.html#cb193-9)
    [](pointers2.html#cb193-10)// This is a comparison function called by qsort() to help it determine
    [](pointers2.html#cb193-11)// what exactly to sort by. We'll use it to sort an array of struct
    [](pointers2.html#cb193-12)// animals by leg_count.
    [](pointers2.html#cb193-13)int compar(const void *elem1, const void *elem2)
    [](pointers2.html#cb193-14){
    [](pointers2.html#cb193-15)    // We know we're sorting struct animals, so let's make both
    [](pointers2.html#cb193-16)    // arguments pointers to struct animals
    [](pointers2.html#cb193-17)    const struct animal *animal1 = elem1;
    [](pointers2.html#cb193-18)    const struct animal *animal2 = elem2;
    [](pointers2.html#cb193-19)
    [](pointers2.html#cb193-20)    // Return <0 =0 or >0 depending on whatever we want to sort by.
    [](pointers2.html#cb193-21)
    [](pointers2.html#cb193-22)    // Let's sort ascending by leg_count, so we'll return the difference
    [](pointers2.html#cb193-23)    // in the leg_counts
    [](pointers2.html#cb193-24)    if (animal1->leg_count > animal2->leg_count)
    [](pointers2.html#cb193-25)        return 1;
    [](pointers2.html#cb193-26)    
    [](pointers2.html#cb193-27)    if (animal1->leg_count < animal2->leg_count)
    [](pointers2.html#cb193-28)        return -1;
    [](pointers2.html#cb193-29)
    [](pointers2.html#cb193-30)    return 0;
    [](pointers2.html#cb193-31)}
    [](pointers2.html#cb193-32)
    [](pointers2.html#cb193-33)int main(void)
    [](pointers2.html#cb193-34){
    [](pointers2.html#cb193-35)    // Let's build an array of 4 struct animals with different
    [](pointers2.html#cb193-36)    // characteristics. This array is out of order by leg_count, but
    [](pointers2.html#cb193-37)    // we'll sort it in a second.
    [](pointers2.html#cb193-38)    struct animal a[4] = {
    [](pointers2.html#cb193-39)        {.name="Dog", .leg_count=4},
    [](pointers2.html#cb193-40)        {.name="Monkey", .leg_count=2},
    [](pointers2.html#cb193-41)        {.name="Antelope", .leg_count=4},
    [](pointers2.html#cb193-42)        {.name="Snake", .leg_count=0}
    [](pointers2.html#cb193-43)    };
    [](pointers2.html#cb193-44)
    [](pointers2.html#cb193-45)    // Call qsort() to sort the array. qsort() needs to be told exactly
    [](pointers2.html#cb193-46)    // what to sort this data by, and we'll do that inside the compar()
    [](pointers2.html#cb193-47)    // function.
    [](pointers2.html#cb193-48)    //
    [](pointers2.html#cb193-49)    // This call is saying: qsort array a, which has 4 elements, and
    [](pointers2.html#cb193-50)    // each element is sizeof(struct animal) bytes big, and this is the
    [](pointers2.html#cb193-51)    // function that will compare any two elements.
    [](pointers2.html#cb193-52)    qsort(a, 4, sizeof(struct animal), compar);
    [](pointers2.html#cb193-53)
    [](pointers2.html#cb193-54)    // Print them all out
    [](pointers2.html#cb193-55)    for (int i = 0; i < 4; i++) {
    [](pointers2.html#cb193-56)        printf("%d: %s\n", a[i].leg_count, a[i].name);
    [](pointers2.html#cb193-57)    }
    [](pointers2.html#cb193-58)}

As long as you give `qsort()` a function that can compare two items that you have in your array to be sorted, it can sort anything. And it does this without needing to have the types of the items hardcoded in there anywhere. `qsort()` just rearranges blocks of bytes based on the results of the `compar()` function you passed in. 

* * *

[Prev](typedef-making-new-types.html) | [Contents](index.html) | [Next](manual-memory-allocation.html)

---

[Prev](pointers2.html) | [Contents](index.html) | [Next](scope.html)

* * *

# 12 Manual Memory Allocation

This is one of the big areas where C likely diverges from languages you already know: _manual memory management_.

Other languages uses reference counting, garbage collection, or other means to determine when to allocate new memory for some data—and when to deallocate it when no variables refer to it.

And that’s nice. It’s nice to be able to not worry about it, to just drop all the references to an item and trust that at some point the memory associated with it will be freed.

But C’s not like that, entirely.

Of course, in C, some variables are automatically allocated and deallocated when they come into scope and leave scope. We call these automatic variables. They’re your average run-of-the-mill block scope “local” variables. No problem. 

But what if you want something to persist longer than a particular block? This is where manual memory management comes into play.

You can tell C explicitly to allocate for you a certain number of bytes that you can use as you please. And these bytes will remain allocated until you explicitly free that memory[90](function-specifiers-alignment-specifiersoperators.html#fn90).

It’s important to free the memory you’re done with! If you don’t, we call that a _memory leak_ and your process will continue to reserve that memory until it exits.

_If you manually allocated it, you have to manually free it when you’re done with it._

So how do we do this? We’re going to learn a couple new functions, and make use of the `sizeof` operator to help us learn how many bytes to allocate.

In common C parlance, devs say that automatic local variables are allocated “on the stack”, and manually-allocated memory is “on the heap”. The spec doesn’t talk about either of those things, but all C devs will know what you’re talking about if you bring them up. 

All functions we’re going to learn in this chapter can be found in `<stdlib.h>`.

## 12.1 Allocating and Deallocating, `malloc()` and `free()`

The `malloc()` function accepts a number of bytes to allocate, and returns a void pointer to that block of newly-allocated memory.

Since it’s a `void*`, you can assign it into whatever pointer type you want… normally this will correspond in some way to the number of bytes you’re allocating.

So… how many bytes should I allocate? We can use `sizeof` to help with that. If we want to allocate enough room for a single `int`, we can use `sizeof(int)` and pass that to `malloc()`. 

After we’re done with some allocated memory, we can call `free()` to indicate we’re done with that memory and it can be used for something else. As an argument, you pass the same pointer you got from `malloc()` (or a copy of it). It’s undefined behavior to use a memory region after you `free()` it.

Let’s try. We’ll allocate enough memory for an `int`, and then store something there, and then print it.
    
    
    [](manual-memory-allocation.html#cb194-1)// Allocate space for a single int (sizeof(int) bytes-worth):
    [](manual-memory-allocation.html#cb194-2)
    [](manual-memory-allocation.html#cb194-3)int *p = malloc(sizeof(int));
    [](manual-memory-allocation.html#cb194-4)
    [](manual-memory-allocation.html#cb194-5)*p = 12;  // Store something there
    [](manual-memory-allocation.html#cb194-6)
    [](manual-memory-allocation.html#cb194-7)printf("%d\n", *p);  // Print it: 12
    [](manual-memory-allocation.html#cb194-8)
    [](manual-memory-allocation.html#cb194-9)free(p);  // All done with that memory
    [](manual-memory-allocation.html#cb194-10)
    [](manual-memory-allocation.html#cb194-11)//*p = 3490;  // ERROR: undefined behavior! Use after free()!

Now, in that contrived example, there’s really no benefit to it. We could have just used an automatic `int` and it would have worked. But we’ll see how the ability to allocate memory this way has its advantages, especially with more complex data structures.

One more thing you’ll commonly see takes advantage of the fact that `sizeof` can give you the size of the result type of any constant expression. So you could put a variable name in there, too, and use that. Here’s an example of that, just like the previous one:
    
    
    [](manual-memory-allocation.html#cb195-1)int *p = malloc(sizeof *p);  // *p is an int, so same as sizeof(int)

## 12.2 Error Checking

All the allocation functions return a pointer to the newly-allocated stretch of memory, or `NULL` if the memory cannot be allocated for some reason.

Some OSes like Linux can be configured in such a way that `malloc()` never returns `NULL`, even if you’re out of memory. But despite this, you should always code it up with protections in mind.
    
    
    [](manual-memory-allocation.html#cb196-1)int *x;
    [](manual-memory-allocation.html#cb196-2)
    [](manual-memory-allocation.html#cb196-3)x = malloc(sizeof(int) * 10);
    [](manual-memory-allocation.html#cb196-4)
    [](manual-memory-allocation.html#cb196-5)if (x == NULL) {
    [](manual-memory-allocation.html#cb196-6)    printf("Error allocating 10 ints\n");
    [](manual-memory-allocation.html#cb196-7)    // do something here to handle it
    [](manual-memory-allocation.html#cb196-8)}

Here’s a common pattern that you’ll see, where we do the assignment and the condition on the same line:
    
    
    [](manual-memory-allocation.html#cb197-1)int *x;
    [](manual-memory-allocation.html#cb197-2)
    [](manual-memory-allocation.html#cb197-3)if ((x = malloc(sizeof(int) * 10)) == NULL) {
    [](manual-memory-allocation.html#cb197-4)    printf("Error allocating 10 ints\n");
    [](manual-memory-allocation.html#cb197-5)    // do something here to handle it
    [](manual-memory-allocation.html#cb197-6)}

## 12.3 Allocating Space for an Array

We’ve seen how to allocate space for a single thing; now what about for a bunch of them in an array?

In C, an array is a bunch of the same thing back-to-back in a contiguous stretch of memory.

We can allocate a contiguous stretch of memory—we’ve seen how to do that. If we wanted 3490 bytes of memory, we could just ask for it:
    
    
    [](manual-memory-allocation.html#cb198-1)char *p = malloc(3490);  // Voila

And—indeed!—that’s an array of 3490 `char`s (AKA a string!) since each `char` is 1 byte. In other words, `sizeof(char)` is `1`.

Note: there’s no initialization done on the newly-allocated memory—it’s full of garbage. Clear it with `memset()` if you want to, or see `calloc()`, below.

But we can just multiply the size of the thing we want by the number of elements we want, and then access them using either pointer or array notation. Example!
    
    
    [](manual-memory-allocation.html#cb199-1)#include <stdio.h>
    [](manual-memory-allocation.html#cb199-2)#include <stdlib.h>
    [](manual-memory-allocation.html#cb199-3)
    [](manual-memory-allocation.html#cb199-4)int main(void)
    [](manual-memory-allocation.html#cb199-5){
    [](manual-memory-allocation.html#cb199-6)    // Allocate space for 10 ints
    [](manual-memory-allocation.html#cb199-7)    int *p = malloc(sizeof(int) * 10);
    [](manual-memory-allocation.html#cb199-8)
    [](manual-memory-allocation.html#cb199-9)    // Assign them values 0-45:
    [](manual-memory-allocation.html#cb199-10)    for (int i = 0; i < 10; i++)
    [](manual-memory-allocation.html#cb199-11)        p[i] = i * 5;
    [](manual-memory-allocation.html#cb199-12)
    [](manual-memory-allocation.html#cb199-13)    // Print all values 0, 5, 10, 15, ..., 40, 45
    [](manual-memory-allocation.html#cb199-14)    for (int i = 0; i < 10; i++)
    [](manual-memory-allocation.html#cb199-15)        printf("%d\n", p[i]);
    [](manual-memory-allocation.html#cb199-16)
    [](manual-memory-allocation.html#cb199-17)    // Free the space
    [](manual-memory-allocation.html#cb199-18)    free(p);
    [](manual-memory-allocation.html#cb199-19)}

The key’s in that `malloc()` line. If we know each `int` takes `sizeof(int)` bytes to hold it, and we know we want 10 of them, we can just allocate exactly that many bytes with:
    
    
    [](manual-memory-allocation.html#cb200-1)sizeof(int) * 10

And this trick works for every type. Just pass it to `sizeof` and multiply by the size of the array. 

## 12.4 An Alternative: `calloc()`

This is another allocation function that works similarly to `malloc()`, with two key differences:

  * Instead of a single argument, you pass the size of one element, and the number of elements you wish to allocate. It’s like it’s made for allocating arrays.
  * It clears the memory to zero.



You still use `free()` to deallocate memory obtained through `calloc()`.

Here’s a comparison of `calloc()` and `malloc()`.
    
    
    [](manual-memory-allocation.html#cb201-1)// Allocate space for 10 ints with calloc(), initialized to 0:
    [](manual-memory-allocation.html#cb201-2)int *p = calloc(10, sizeof(int));
    [](manual-memory-allocation.html#cb201-3)
    [](manual-memory-allocation.html#cb201-4)// Allocate space for 10 ints with malloc(), initialized to 0:
    [](manual-memory-allocation.html#cb201-5)int *q = malloc(10 * sizeof(int));
    [](manual-memory-allocation.html#cb201-6)memset(q, 0, 10 * sizeof(int));   // set to 0

Again, the result is the same for both except `malloc()` doesn’t zero the memory by default. 

## 12.5 Changing Allocated Size with `realloc()`

If you’ve already allocated 10 `int`s, but later you decide you need 20, what can you do?

One option is to allocate some new space, and then `memcpy()` the memory over… but it turns out that sometimes you don’t need to move anything. And there’s one function that’s just smart enough to do the right thing in all the right circumstances: `realloc()`.

It takes a pointer to some previously-allocted memory (by `malloc()` or `calloc()`) and a new size for the memory region to be.

It then grows or shrinks that memory, and returns a pointer to it. Sometimes it might return the same pointer (if the data didn’t have to be copied elsewhere), or it might return a different one (if the data did have to be copied).

Be sure when you call `realloc()`, you specify the number of _bytes_ to allocate, and not just the number of array elements! That is:
    
    
    [](manual-memory-allocation.html#cb202-1)num_floats *= 2;
    [](manual-memory-allocation.html#cb202-2)
    [](manual-memory-allocation.html#cb202-3)np = realloc(p, num_floats);  // WRONG: need bytes, not number of elements!
    [](manual-memory-allocation.html#cb202-4)
    [](manual-memory-allocation.html#cb202-5)np = realloc(p, num_floats * sizeof(float));  // Better!

Let’s allocate an array of 20 `float`s, and then change our mind and make it an array of 40.

We’re going to assign the return value of realloc() into another pointer so we can check if it’s NULL. If it’s not, then we can reassign it into our original pointer. (If we just assigned the return value directly into the original pointer, we’d lose that pointer if the function returned `NULL` and we’d have no way to get it back.)
    
    
    [](manual-memory-allocation.html#cb203-1)#include <stdio.h>
    [](manual-memory-allocation.html#cb203-2)#include <stdlib.h>
    [](manual-memory-allocation.html#cb203-3)
    [](manual-memory-allocation.html#cb203-4)int main(void)
    [](manual-memory-allocation.html#cb203-5){
    [](manual-memory-allocation.html#cb203-6)    // Allocate space for 20 floats
    [](manual-memory-allocation.html#cb203-7)    float *p = malloc(sizeof *p * 20);  // sizeof *p same as sizeof(float)
    [](manual-memory-allocation.html#cb203-8)
    [](manual-memory-allocation.html#cb203-9)    // Assign them fractional values 0.0-1.0:
    [](manual-memory-allocation.html#cb203-10)    for (int i = 0; i < 20; i++)
    [](manual-memory-allocation.html#cb203-11)        p[i] = i / 20.0;
    [](manual-memory-allocation.html#cb203-12)
    [](manual-memory-allocation.html#cb203-13)    // But wait! Let's actually make this an array of 40 elements
    [](manual-memory-allocation.html#cb203-14)    float *new_p = realloc(p, sizeof *p * 40);
    [](manual-memory-allocation.html#cb203-15)
    [](manual-memory-allocation.html#cb203-16)    // Check to see if we successfully reallocated
    [](manual-memory-allocation.html#cb203-17)    if (new_p == NULL) {
    [](manual-memory-allocation.html#cb203-18)        printf("Error reallocing\n");
    [](manual-memory-allocation.html#cb203-19)        return 1;
    [](manual-memory-allocation.html#cb203-20)    }
    [](manual-memory-allocation.html#cb203-21)
    [](manual-memory-allocation.html#cb203-22)    // If we did, we can just reassign p
    [](manual-memory-allocation.html#cb203-23)    p = new_p;
    [](manual-memory-allocation.html#cb203-24)
    [](manual-memory-allocation.html#cb203-25)    // And assign the new elements values in the range 1.0-2.0
    [](manual-memory-allocation.html#cb203-26)    for (int i = 20; i < 40; i++)
    [](manual-memory-allocation.html#cb203-27)        p[i] = 1.0 + (i - 20) / 20.0;
    [](manual-memory-allocation.html#cb203-28)
    [](manual-memory-allocation.html#cb203-29)    // Print all values 0.0-2.0 in the 40 elements:
    [](manual-memory-allocation.html#cb203-30)    for (int i = 0; i < 40; i++)
    [](manual-memory-allocation.html#cb203-31)        printf("%f\n", p[i]);
    [](manual-memory-allocation.html#cb203-32)
    [](manual-memory-allocation.html#cb203-33)    // Free the space
    [](manual-memory-allocation.html#cb203-34)    free(p);
    [](manual-memory-allocation.html#cb203-35)}

Notice in there how we took the return value from `realloc()` and reassigned it into the same pointer variable `p` that we passed in. That’s pretty common to do.

Also if line 7 is looking weird, with that `sizeof *p` in there, remember that `sizeof` works on the size of the type of the expression. And the type of `*p` is `float`, so that line is equivalent to `sizeof(float)`.

Finally, it might be a little weird that I don’t have a `free(new_p)` in there anywhere, even though that was the pointer returned by `realloc()`. The reason is that we copy `new_p` into `p` on line 23, so they both have the same value; that is, they both point to the same chunk of memory, and there’s only the one chunk. So when I `free()`, I could actually free either of them for the same effect.

### 12.5.1 Reading in Lines of Arbitrary Length

I want to demonstrate two things with this full-blown example.

  1. Use of `realloc()` to grow a buffer as we read in more data.
  2. Use of `realloc()` to shrink the buffer down to the perfect size after we’ve completed the read.



What we see here is a loop that calls `fgetc()` over and over to append to a buffer until we see that the last character is a newline.

Once it finds the newline, it shrinks the buffer to just the right size and returns it.
    
    
    [](manual-memory-allocation.html#cb204-1)#include <stdio.h>
    [](manual-memory-allocation.html#cb204-2)#include <stdlib.h>
    [](manual-memory-allocation.html#cb204-3)
    [](manual-memory-allocation.html#cb204-4)// Read a line of arbitrary size from a file
    [](manual-memory-allocation.html#cb204-5)//
    [](manual-memory-allocation.html#cb204-6)// Returns a pointer to the line.
    [](manual-memory-allocation.html#cb204-7)// Returns NULL on EOF or error.
    [](manual-memory-allocation.html#cb204-8)//
    [](manual-memory-allocation.html#cb204-9)// It's up to the caller to free() this pointer when done with it.
    [](manual-memory-allocation.html#cb204-10)//
    [](manual-memory-allocation.html#cb204-11)// Note that this strips the newline from the result. If you need
    [](manual-memory-allocation.html#cb204-12)// it in there, probably best to switch this to a do-while.
    [](manual-memory-allocation.html#cb204-13)
    [](manual-memory-allocation.html#cb204-14)char *readline(FILE *fp)
    [](manual-memory-allocation.html#cb204-15){
    [](manual-memory-allocation.html#cb204-16)    int offset = 0;   // Index next char goes in the buffer
    [](manual-memory-allocation.html#cb204-17)    int bufsize = 4;  // Preferably power of 2 initial size
    [](manual-memory-allocation.html#cb204-18)    char *buf;        // The buffer
    [](manual-memory-allocation.html#cb204-19)    int c;            // The character we've read in
    [](manual-memory-allocation.html#cb204-20)
    [](manual-memory-allocation.html#cb204-21)    buf = malloc(bufsize);  // Allocate initial buffer
    [](manual-memory-allocation.html#cb204-22)
    [](manual-memory-allocation.html#cb204-23)    if (buf == NULL)   // Error check
    [](manual-memory-allocation.html#cb204-24)        return NULL;
    [](manual-memory-allocation.html#cb204-25)
    [](manual-memory-allocation.html#cb204-26)    // Main loop--read until newline or EOF
    [](manual-memory-allocation.html#cb204-27)    while (c = fgetc(fp), c != '\n' && c != EOF) {
    [](manual-memory-allocation.html#cb204-28)
    [](manual-memory-allocation.html#cb204-29)        // Check if we're out of room in the buffer accounting
    [](manual-memory-allocation.html#cb204-30)        // for the extra byte for the NUL terminator
    [](manual-memory-allocation.html#cb204-31)        if (offset == bufsize - 1) {  // -1 for the NUL terminator
    [](manual-memory-allocation.html#cb204-32)            bufsize *= 2;  // 2x the space
    [](manual-memory-allocation.html#cb204-33)
    [](manual-memory-allocation.html#cb204-34)            char *new_buf = realloc(buf, bufsize);
    [](manual-memory-allocation.html#cb204-35)
    [](manual-memory-allocation.html#cb204-36)            if (new_buf == NULL) {
    [](manual-memory-allocation.html#cb204-37)                free(buf);   // On error, free and bail
    [](manual-memory-allocation.html#cb204-38)                return NULL;
    [](manual-memory-allocation.html#cb204-39)            }
    [](manual-memory-allocation.html#cb204-40)
    [](manual-memory-allocation.html#cb204-41)            buf = new_buf;  // Successful realloc
    [](manual-memory-allocation.html#cb204-42)        }
    [](manual-memory-allocation.html#cb204-43)
    [](manual-memory-allocation.html#cb204-44)        buf[offset++] = c;  // Add the byte onto the buffer
    [](manual-memory-allocation.html#cb204-45)    }
    [](manual-memory-allocation.html#cb204-46)
    [](manual-memory-allocation.html#cb204-47)    // We hit newline or EOF...
    [](manual-memory-allocation.html#cb204-48)
    [](manual-memory-allocation.html#cb204-49)    // If at EOF and we read no bytes, free the buffer and
    [](manual-memory-allocation.html#cb204-50)    // return NULL to indicate we're at EOF:
    [](manual-memory-allocation.html#cb204-51)    if (c == EOF && offset == 0) {
    [](manual-memory-allocation.html#cb204-52)        free(buf);
    [](manual-memory-allocation.html#cb204-53)        return NULL;
    [](manual-memory-allocation.html#cb204-54)    }
    [](manual-memory-allocation.html#cb204-55)
    [](manual-memory-allocation.html#cb204-56)    // Shrink to fit
    [](manual-memory-allocation.html#cb204-57)    if (offset < bufsize - 1) {  // If we're short of the end
    [](manual-memory-allocation.html#cb204-58)        char *new_buf = realloc(buf, offset + 1); // +1 for NUL terminator
    [](manual-memory-allocation.html#cb204-59)
    [](manual-memory-allocation.html#cb204-60)        // If successful, point buf to new_buf;
    [](manual-memory-allocation.html#cb204-61)        // otherwise we'll just leave buf where it is
    [](manual-memory-allocation.html#cb204-62)        if (new_buf != NULL)
    [](manual-memory-allocation.html#cb204-63)            buf = new_buf;
    [](manual-memory-allocation.html#cb204-64)    }
    [](manual-memory-allocation.html#cb204-65)
    [](manual-memory-allocation.html#cb204-66)    // Add the NUL terminator
    [](manual-memory-allocation.html#cb204-67)    buf[offset] = '\0';
    [](manual-memory-allocation.html#cb204-68)
    [](manual-memory-allocation.html#cb204-69)    return buf;
    [](manual-memory-allocation.html#cb204-70)}
    [](manual-memory-allocation.html#cb204-71)
    [](manual-memory-allocation.html#cb204-72)int main(void)
    [](manual-memory-allocation.html#cb204-73){
    [](manual-memory-allocation.html#cb204-74)    FILE *fp = fopen("foo.txt", "r");
    [](manual-memory-allocation.html#cb204-75)
    [](manual-memory-allocation.html#cb204-76)    char *line;
    [](manual-memory-allocation.html#cb204-77)
    [](manual-memory-allocation.html#cb204-78)    while ((line = readline(fp)) != NULL) {
    [](manual-memory-allocation.html#cb204-79)        printf("%s\n", line);
    [](manual-memory-allocation.html#cb204-80)        free(line);
    [](manual-memory-allocation.html#cb204-81)    }
    [](manual-memory-allocation.html#cb204-82)
    [](manual-memory-allocation.html#cb204-83)    fclose(fp);
    [](manual-memory-allocation.html#cb204-84)}

When growing memory like this, it’s common (though hardly a law) to double the space needed each step just to minimize the number of `realloc()`s that occur.

Finally you might note that `readline()` returns a pointer to a `malloc()`d buffer. As such, it’s up to the caller to explicitly `free()` that memory when it’s done with it.

### 12.5.2 `realloc()` with `NULL`

Trivia time! These two lines are equivalent:
    
    
    [](manual-memory-allocation.html#cb205-1)char *p = malloc(3490);
    [](manual-memory-allocation.html#cb205-2)char *p = realloc(NULL, 3490);

That could be convenient if you have some kind of allocation loop and you don’t want to special-case the first `malloc()`.
    
    
    [](manual-memory-allocation.html#cb206-1)int *p = NULL;
    [](manual-memory-allocation.html#cb206-2)int length = 0;
    [](manual-memory-allocation.html#cb206-3)
    [](manual-memory-allocation.html#cb206-4)while (!done) {
    [](manual-memory-allocation.html#cb206-5)    // Allocate 10 more ints:
    [](manual-memory-allocation.html#cb206-6)    length += 10;
    [](manual-memory-allocation.html#cb206-7)    p = realloc(p, sizeof *p * length);
    [](manual-memory-allocation.html#cb206-8)
    [](manual-memory-allocation.html#cb206-9)    // Do amazing things
    [](manual-memory-allocation.html#cb206-10)    // ...
    [](manual-memory-allocation.html#cb206-11)}

In that example, we didn’t need an initial `malloc()` since `p` was `NULL` to start. 

## 12.6 Aligned Allocations

You probably aren’t going to need to use this.

And I don’t want to get too far off in the weeds talking about it right now, but there’s this thing called _memory alignment_ , which has to do with the memory address (pointer value) being a multiple of a certain number.

For example, a system might require that 16-bit values begin on memory addresses that are multiples of 2. Or that 64-bit values begin on memory addresses that are multiples of 2, 4, or 8, for example. It depends on the CPU.

Some systems require this kind of alignment for fast memory access, or some even for memory access at all.

Now, if you use `malloc()`, `calloc()`, or `realloc()`, C will give you a chunk of memory that’s well-aligned for any value at all, even `struct`s. Works in all cases.

But there might be times that you know that some data can be aligned at a smaller boundary, or must be aligned at a larger one for some reason. I imagine this is more common with embedded systems programming.

In those cases, you can specify an alignment with `aligned_alloc()`.

The alignment is an integer power of two greater than zero, so `2`, `4`, `8`, `16`, etc. and you give that to `aligned_alloc()` before the number of bytes you’re interested in.

The other restriction is that the number of bytes you allocate needs to be a multiple of the alignment. But this might be changing. See [C Defect Report 460](http://www.open-std.org/jtc1/sc22/wg14/www/docs/summary.htm#dr_460)[91](function-specifiers-alignment-specifiersoperators.html#fn91)

Let’s do an example, allocating on a 64-byte boundary:
    
    
    [](manual-memory-allocation.html#cb207-1)#include <stdio.h>
    [](manual-memory-allocation.html#cb207-2)#include <stdlib.h>
    [](manual-memory-allocation.html#cb207-3)#include <string.h>
    [](manual-memory-allocation.html#cb207-4)
    [](manual-memory-allocation.html#cb207-5)int main(void)
    [](manual-memory-allocation.html#cb207-6){
    [](manual-memory-allocation.html#cb207-7)    // Allocate 256 bytes aligned on a 64-byte boundary
    [](manual-memory-allocation.html#cb207-8)    char *p = aligned_alloc(64, 256);  // 256 == 64 * 4
    [](manual-memory-allocation.html#cb207-9)
    [](manual-memory-allocation.html#cb207-10)    // Copy a string in there and print it
    [](manual-memory-allocation.html#cb207-11)    strcpy(p, "Hello, world!");
    [](manual-memory-allocation.html#cb207-12)    printf("%s\n", p);
    [](manual-memory-allocation.html#cb207-13)
    [](manual-memory-allocation.html#cb207-14)    // Free the space
    [](manual-memory-allocation.html#cb207-15)    free(p);
    [](manual-memory-allocation.html#cb207-16)}

I want to throw a note here about `realloc()` and `aligned_alloc()`. `realloc()` doesn’t have any alignment guarantees, so if you need to get some aligned reallocated space, you’ll have to do it the hard way with `memcpy()`. 

Here’s a non-standard `aligned_realloc()` function, if you need it:
    
    
    [](manual-memory-allocation.html#cb208-1)void *aligned_realloc(void *ptr, size_t old_size, size_t alignment, size_t size)
    [](manual-memory-allocation.html#cb208-2){
    [](manual-memory-allocation.html#cb208-3)    char *new_ptr = aligned_alloc(alignment, size);
    [](manual-memory-allocation.html#cb208-4)
    [](manual-memory-allocation.html#cb208-5)    if (new_ptr == NULL)
    [](manual-memory-allocation.html#cb208-6)        return NULL;
    [](manual-memory-allocation.html#cb208-7)
    [](manual-memory-allocation.html#cb208-8)    size_t copy_size = old_size < size? old_size: size;  // get min
    [](manual-memory-allocation.html#cb208-9)
    [](manual-memory-allocation.html#cb208-10)    if (ptr != NULL)
    [](manual-memory-allocation.html#cb208-11)        memcpy(new_ptr, ptr, copy_size);
    [](manual-memory-allocation.html#cb208-12)
    [](manual-memory-allocation.html#cb208-13)    free(ptr);
    [](manual-memory-allocation.html#cb208-14)
    [](manual-memory-allocation.html#cb208-15)    return new_ptr;
    [](manual-memory-allocation.html#cb208-16)}

Note that it _always_ copies data, taking time, while real `realloc()` will avoid that if it can. So this is hardly efficient. Avoid needing to reallocate custom-aligned data. 

* * *

[Prev](pointers2.html) | [Contents](index.html) | [Next](scope.html)

---

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

---

[Prev](scope.html) | [Contents](index.html) | [Next](types-iii-conversions.html)

* * *

# 14 Types II: Way More Types!

We’re used to `char`, `int`, and `float` types, but it’s now time to take that stuff to the next level and see what else we have out there in the types department!

## 14.1 Signed and Unsigned Integers

So far we’ve used `int` as a _signed_ type, that is, a value that can be either negative or positive. But C also has specific _unsigned_ integer types that can only hold positive numbers.

These types are prefaced by the keyword `unsigned`.
    
    
    [](types-ii-way-more-types.html#cb215-1)int a;           // signed
    [](types-ii-way-more-types.html#cb215-2)signed int a;    // signed
    [](types-ii-way-more-types.html#cb215-3)signed a;        // signed, "shorthand" for "int" or "signed int", rare
    [](types-ii-way-more-types.html#cb215-4)unsigned int b;  // unsigned
    [](types-ii-way-more-types.html#cb215-5)unsigned c;      // unsigned, shorthand for "unsigned int"

Why? Why would you decide you only wanted to hold positive numbers?

Answer: you can get larger numbers in an unsigned variable than you can in a signed ones.

But why is that?

You can think of integers being represented by a certain number of _bits_[ 93](function-specifiers-alignment-specifiersoperators.html#fn93). On my computer, an `int` is represented by 64 bits.

And each permutation of bits that are either `1` or `0` represents a number. We can decide how to divvy up these numbers.

With signed numbers, we use (roughly) half the permutations to represent negative numbers, and the other half to represent positive numbers.

With unsigned, we use _all_ the permutations to represent positive numbers.

On my computer with 64-bit `int`s using [two’s complement](https://en.wikipedia.org/wiki/Two%27s_complement)[94](function-specifiers-alignment-specifiersoperators.html#fn94) to represent unsigned numbers, I have the following limits on integer range:

Type | Minimum | Maximum  
---|---|---  
`int` | `-9,223,372,036,854,775,808` | `9,223,372,036,854,775,807`  
`unsigned int` | `0` | `18,446,744,073,709,551,615`  
  
Notice that the largest positive `unsigned int` is approximately twice as large as the largest positive `int`. So you can get some flexibility there. 

## 14.2 Character Types

Remember `char`? The type we can use to hold a single character?
    
    
    [](types-ii-way-more-types.html#cb216-1)char c = 'B';
    [](types-ii-way-more-types.html#cb216-2)
    [](types-ii-way-more-types.html#cb216-3)printf("%c\n", c);  // "B"

I have a shocker for you: it’s actually an integer.
    
    
    [](types-ii-way-more-types.html#cb217-1)char c = 'B';
    [](types-ii-way-more-types.html#cb217-2)
    [](types-ii-way-more-types.html#cb217-3)// Change this from %c to %d:
    [](types-ii-way-more-types.html#cb217-4)printf("%d\n", c);  // 66 (!!)

Deep down, `char` is just a small `int`, namely an integer that uses just a single byte of space, limiting its range to…

Here the C spec gets just a little funky. It assures us that a `char` is a single byte, i.e. `sizeof(char) == 1`. But then in C11 §3.6¶3 it goes out of its way to say:

> A byte is composed of a contiguous sequence of bits, _the number of which is implementation-defined._

Wait—what? Some of you might be used to the notion that a byte is 8 bits, right? I mean, that’s what it is, right? And the answer is, “Almost certainly.”[95](function-specifiers-alignment-specifiersoperators.html#fn95) But C is an old language, and machines back in the day had, shall we say, a more _relaxed_ opinion over how many bits were in a byte. And through the years, C has retained this flexibility.

But assuming your bytes in C are 8 bits, like they are for virtually all machines in the world that you’ll ever see, the range of a `char` is…

—So before I can tell you, it turns out that `char`s might be signed or unsigned depending on your compiler. Unless you explicitly specify.

In many cases, just having `char` is fine because you don’t care about the sign of the data. But if you need signed or unsigned `char`s, you _must_ be specific:
    
    
    [](types-ii-way-more-types.html#cb218-1)char a;           // Could be signed or unsigned
    [](types-ii-way-more-types.html#cb218-2)signed char b;    // Definitely signed
    [](types-ii-way-more-types.html#cb218-3)unsigned char c;  // Definitely unsigned

OK, now, finally, we can figure out the range of numbers if we assume that a `char` is 8 bits and your system uses the virtually universal two’s complement representation for signed and unsigned[96](function-specifiers-alignment-specifiersoperators.html#fn96).

So, assuming those constraints, we can finally figure our ranges:

`char` type | Minimum | Maximum  
---|---|---  
`signed char` | `-128` | `127`  
`unsigned char` | `0` | `255`  
  
And the ranges for `char` are implementation-defined. 

Let me get this straight. `char` is actually a number, so can we do math on it?

Yup! Just remember to keep things in the range of a `char`!
    
    
    [](types-ii-way-more-types.html#cb219-1)#include <stdio.h>
    [](types-ii-way-more-types.html#cb219-2)
    [](types-ii-way-more-types.html#cb219-3)int main(void)
    [](types-ii-way-more-types.html#cb219-4){
    [](types-ii-way-more-types.html#cb219-5)    char a = 10, b = 20;
    [](types-ii-way-more-types.html#cb219-6)
    [](types-ii-way-more-types.html#cb219-7)    printf("%d\n", a + b);  // 30!
    [](types-ii-way-more-types.html#cb219-8)}

What about those constant characters in single quotes, like `'B'`? How does that have a numeric value?

The spec is also hand-wavey here, since C isn’t designed to run on a single type of underlying system.

But let’s just assume for the moment that your character set is based on [ASCII](https://en.wikipedia.org/wiki/ASCII)[97](function-specifiers-alignment-specifiersoperators.html#fn97) for at least the first 128 characters. In that case, the character constant will be converted to a `char` whose value is the same as the ASCII value of the character.

That was a mouthful. Let’s just have an example:
    
    
    [](types-ii-way-more-types.html#cb220-1)#include <stdio.h>
    [](types-ii-way-more-types.html#cb220-2)
    [](types-ii-way-more-types.html#cb220-3)int main(void)
    [](types-ii-way-more-types.html#cb220-4){
    [](types-ii-way-more-types.html#cb220-5)    char a = 10;
    [](types-ii-way-more-types.html#cb220-6)    char b = 'B';  // ASCII value 66
    [](types-ii-way-more-types.html#cb220-7)
    [](types-ii-way-more-types.html#cb220-8)    printf("%d\n", a + b);  // 76!
    [](types-ii-way-more-types.html#cb220-9)}

This depends on your execution environment and the [character set used](https://en.wikipedia.org/wiki/List_of_information_system_character_sets)[98](function-specifiers-alignment-specifiersoperators.html#fn98). One of the most popular character sets today is [Unicode](https://en.wikipedia.org/wiki/Unicode)[99](function-specifiers-alignment-specifiersoperators.html#fn99) (which is a superset of ASCII), so for your basic 0-9, A-Z, a-z and punctuation, you’ll almost certainly get the ASCII values out of them. 

## 14.3 More Integer Types: `short`, `long`, `long long`

So far we’ve just generally been using two integer types:

  * `char`
  * `int`



and we recently learned about the unsigned variants of the integer types. And we learned that `char` was secretly a small `int` in disguise. So we know the `int`s can come in multiple bit sizes.

But there are a couple more integer types we should look at, and the minimum ranges they can hold. (Your implementation probably has wider ranges than the spec requires, but the ranges here are the ones you can be **certain** are portably available.)

The header file `<limits.h>` defines macros that hold the ranges for various types; rely on that to be sure, and _never hardcode or assume these values_.

These additional types are `short int`, `long int`, and `long long int`. Commonly, when using these types, C developers leave the `int` part off (e.g. `long long`), and the compiler is perfectly happy.
    
    
    [](types-ii-way-more-types.html#cb221-1)// These two lines are equivalent:
    [](types-ii-way-more-types.html#cb221-2)long long int x;
    [](types-ii-way-more-types.html#cb221-3)long long x;
    [](types-ii-way-more-types.html#cb221-4)
    [](types-ii-way-more-types.html#cb221-5)// And so are these:
    [](types-ii-way-more-types.html#cb221-6)short int x;
    [](types-ii-way-more-types.html#cb221-7)short x;

Let’s take a look at the integer data types and sizes in ascending order, grouped by signedness. Again, these minimum and maximum limits are what you are portably guaranteed by the spec; your system probably has wider ranges.

Type | Minimum Bytes | Minimum Value | Maximum Value  
---|---|---|---  
`char` | 1 | -128 or 0 | 127 or 255[100](function-specifiers-alignment-specifiersoperators.html#fn100)  
`signed char` | 1 | -128 | 127  
`short` | 2 | -32768 | 32767  
`int` | 2 | -32768 | 32767  
`long` | 4 | -2147483648 | 2147483647  
`long long` | 8 | -9223372036854775808 | 9223372036854775807  
`unsigned char` | 1 | 0 | 255  
`unsigned short` | 2 | 0 | 65535  
`unsigned int` | 2 | 0 | 65535  
`unsigned long` | 4 | 0 | 4294967295  
`unsigned long long` | 8 | 0 | 18446744073709551615  
  
There is no `long long long` type. You can’t just keep adding `long`s like that. Don’t be silly.

> Two’s complement fans might have noticed something funny about those numbers. Why does, for example, the `signed char` stop at -127 instead of -128? Remember: these are only the minimums required by the spec. Some number representations (like [sign and magnitude](https://en.wikipedia.org/wiki/Signed_number_representations#Signed_magnitude_representation)[101](function-specifiers-alignment-specifiersoperators.html#fn101)) top off at ±127.

Let’s run the same table on my 64-bit, two’s complement system and see what comes out:

Type | My Bytes | Minimum Value | Maximum Value  
---|---|---|---  
`char` | 1 | -128 | 127[102](function-specifiers-alignment-specifiersoperators.html#fn102)  
`signed char` | 1 | -128 | 127  
`short` | 2 | -32768 | 32767  
`int` | 4 | -2147483648 | 2147483647  
`long` | 8 | -9223372036854775808 | 9223372036854775807  
`long long` | 8 | -9223372036854775808 | 9223372036854775807  
`unsigned char` | 1 | 0 | 255  
`unsigned short` | 2 | 0 | 65535  
`unsigned int` | 4 | 0 | 4294967295  
`unsigned long` | 8 | 0 | 18446744073709551615  
`unsigned long long` | 8 | 0 | 18446744073709551615  
  
That’s a little more sensible, but we can see how my system has larger limits than the minimums in the specification.

So what are the macros in `<limits.h>`?

Type | Min Macro | Max Macro  
---|---|---  
`char` | `CHAR_MIN` | `CHAR_MAX`  
`signed char` | `SCHAR_MIN` | `SCHAR_MAX`  
`short` | `SHRT_MIN` | `SHRT_MAX`  
`int` | `INT_MIN` | `INT_MAX`  
`long` | `LONG_MIN` | `LONG_MAX`  
`long long` | `LLONG_MIN` | `LLONG_MAX`  
`unsigned char` | `0` | `UCHAR_MAX`  
`unsigned short` | `0` | `USHRT_MAX`  
`unsigned int` | `0` | `UINT_MAX`  
`unsigned long` | `0` | `ULONG_MAX`  
`unsigned long long` | `0` | `ULLONG_MAX`  
  
Notice there’s a way hidden in there to determine if a system uses signed or unsigned `char`s. If `CHAR_MAX == UCHAR_MAX`, it must be unsigned.

Also notice there’s no minimum macro for the `unsigned` variants—they’re just `0`. 

## 14.4 More Float: `double` and `long double`

Let’s see what the spec has to say about floating point numbers in §5.2.4.2.2¶1-2:

> The following parameters are used to define the model for each floating-point type:
> 
> Parameter | Definition  
> ---|---  
> \\(s\\) | sign (\\(\pm1\\))  
> \\(b\\) | base or radix of exponent representation (an integer \\(> 1\\))  
> \\(e\\) | exponent (an integer between a minimum \\(e_{min}\\) and a maximum \\(e_{max}\\))  
> \\(p\\) | precision (the number of base-\\(b\\) digits in the significand)  
> \\(f_k\\) | nonnegative integers less than \\(b\\) (the significand digits)  
>   
> A _floating-point number_ (\\(x\\)) is defined by the following model:
>
>> \\(x=sb^e\sum\limits_{k=1}^p f_kb^{-k},\\) \\(e_{min}\le e\le e_{max}\\)

I hope that cleared it right up for you.

Okay, fine. Let’s step back a bit and see what’s practical.

Note: we refer to a bunch of macros in this section. They can be found in the header `<float.h>`.

Floating point number are encoded in a specific sequence of bits ([IEEE-754 format](https://en.wikipedia.org/wiki/IEEE_754)[103](function-specifiers-alignment-specifiersoperators.html#fn103) is tremendously popular) in bytes.

Diving in a bit more, the number is basically represented as the _significand_ (which is the number part—the significant digits themselves, also sometimes referred to as the _mantissa_) and the _exponent_ , which is what power to raise the digits to. Recall that a negative exponent can make a number smaller.

Imagine we’re using \\(10\\) as a number to raise by an exponent. We could represent the following numbers by using a significand of \\(12345\\), and exponents of \\(-3\\), \\(4\\), and \\(0\\) to encode the following floating point values:

\\(12345\times10^{-3}=12.345\\)

\\(12345\times10^4=123450000\\)

\\(12345\times10^0=12345\\)

For all those numbers, the significand stays the same. The only difference is the exponent.

On your machine, the base for the exponent is probably \\(2\\), not \\(10\\), since computers like binary. You can check it by printing the `FLT_RADIX` macro.

So we have a number that’s represented by a number of bytes, encoded in some way. Because there are a limited number of bit patterns, a limited number of floating point numbers can be represented.

But more particularly, only a certain number of significant decimal digits can be represented accurately.

How can you get more? You can use larger data types!

And we have a couple of them. We know about `float` already, but for more precision we have `double`. And for even more precision, we have `long double` (unrelated to `long int` except by name).

The spec doesn’t go into how many bytes of storage each type should take, but on my system, we can see the relative size increases:

Type | `sizeof`  
---|---  
`float` | 4  
`double` | 8  
`long double` | 16  
  
So each of the types (on my system) uses those additional bits for more precision.

But _how much_ precision are we talking, here? How many decimal numbers can be represented by these values?

Well, C provides us with a bunch of macros in `<float.h>` to help us figure that out.

It gets a little wonky if you are using a base-2 (binary) system for storing the numbers (which is virtually everyone on the planet, probably including you), but bear with me while we figure it out. 

### 14.4.1 How Many Decimal Digits?

The million dollar question is, “How many significant decimal digits can I store in a given floating point type so that I get out the same decimal number when I print it?”

The number of decimal digits you can store in a floating point type and surely get the same number back out when you print it is given by these macros:

Type | Decimal Digits You Can Store | Minimum  
---|---|---  
`float` | `FLT_DIG` | 6  
`double` | `DBL_DIG` | 10  
`long double` | `LDBL_DIG` | 10  
  
On my system, `FLT_DIG` is 6, so I can be sure that if I print out a 6 digit `float`, I’ll get the same thing back. (It could be more digits—some numbers will come back correctly with more digits. But 6 is definitely coming back.)

For example, printing out `float`s following this pattern of increasing digits, we apparently make it to 8 digits before something goes wrong, but after that we’re back to 7 correct digits.
    
    
    [](types-ii-way-more-types.html#cb222-1)0.12345
    [](types-ii-way-more-types.html#cb222-2)0.123456
    [](types-ii-way-more-types.html#cb222-3)0.1234567
    [](types-ii-way-more-types.html#cb222-4)0.12345678
    [](types-ii-way-more-types.html#cb222-5)0.123456791  <-- Things start going wrong
    [](types-ii-way-more-types.html#cb222-6)0.1234567910

Let’s do another demo. In this code we’ll have two `float`s that both hold numbers that have `FLT_DIG` significant decimal digits[104](function-specifiers-alignment-specifiersoperators.html#fn104). Then we add those together, for what should be 12 significant decimal digits. But that’s more than we can store in a `float` and correctly recover as a string—so we see when we print it out, things start going wrong after the 7th significant digit.
    
    
    [](types-ii-way-more-types.html#cb223-1)#include <stdio.h>
    [](types-ii-way-more-types.html#cb223-2)#include <float.h>
    [](types-ii-way-more-types.html#cb223-3)
    [](types-ii-way-more-types.html#cb223-4)int main(void)
    [](types-ii-way-more-types.html#cb223-5){
    [](types-ii-way-more-types.html#cb223-6)    // Both these numbers have 6 significant digits, so they can be
    [](types-ii-way-more-types.html#cb223-7)    // stored accurately in a float:
    [](types-ii-way-more-types.html#cb223-8)
    [](types-ii-way-more-types.html#cb223-9)    float f = 3.14159f;
    [](types-ii-way-more-types.html#cb223-10)    float g = 0.00000265358f;
    [](types-ii-way-more-types.html#cb223-11)
    [](types-ii-way-more-types.html#cb223-12)    printf("%.5f\n", f);   // 3.14159       -- correct!
    [](types-ii-way-more-types.html#cb223-13)    printf("%.11f\n", g);  // 0.00000265358 -- correct!
    [](types-ii-way-more-types.html#cb223-14)
    [](types-ii-way-more-types.html#cb223-15)    // Now add them up
    [](types-ii-way-more-types.html#cb223-16)    f += g;                // 3.14159265358 is what f _should_ be
    [](types-ii-way-more-types.html#cb223-17)
    [](types-ii-way-more-types.html#cb223-18)    printf("%.11f\n", f);  // 3.14159274101 -- wrong!
    [](types-ii-way-more-types.html#cb223-19)}

(The above code has an `f` after the numeric constants—this indicates that the constant is type `float`, as opposed to the default of `double`. More on this later.)

Remember that `FLT_DIG` is the safe number of digits you can store in a `float` and retrieve correctly.

Sometimes you might get one or two more out of it. But sometimes you’ll only get `FLT_DIG` digits back. The sure thing: if you store any number of digits up to and including `FLT_DIG` in a `float`, you’re sure to get them back correctly.

So that’s the story. `FLT_DIG`. The End.

…Or is it?

### 14.4.2 Converting to Decimal and Back

But storing a base 10 number in a floating point number and getting it back out is only half the story.

Turns out floating point numbers can encode numbers that require more decimal places to print out completely. It’s just that your big decimal number might not map to one of those numbers.

That is, when you look at floating point numbers from one to the next, there’s a gap. If you try to encode a decimal number in that gap, it’ll use the closest floating point number. That’s why you can only encode `FLT_DIG` for a `float`.

But what about those floating point numbers that _aren’t_ in the gap? How many places do you need to print those out accurately?

Another way to phrase this question is for any given floating point number, how many decimal digits do I have to preserve if I want to convert the decimal number back into an identical floating point number? That is, how many digits do I have to print in base 10 to recover **all** the digits in base 2 in the original number?

Sometimes it might only be a few. But to be sure, you’ll want to convert to decimal with a certain safe number of decimal places. That number is encoded in the following macros:

Macro | Description  
---|---  
`FLT_DECIMAL_DIG` | Number of decimal digits encoded in a `float`.  
`DBL_DECIMAL_DIG` | Number of decimal digits encoded in a `double`.  
`LDBL_DECIMAL_DIG` | Number of decimal digits encoded in a `long double`.  
`DECIMAL_DIG` | Same as the widest encoding, `LDBL_DECIMAL_DIG`.  
  
Let’s see an example where `DBL_DIG` is 15 (so that’s all we can have in a constant), but `DBL_DECIMAL_DIG` is 17 (so we have to convert to 17 decimal numbers to preserve all the bits of the original `double`).

Let’s assign the 15 significant digit number `0.123456789012345` to `x`, and let’s assign the 1 significant digit number `0.0000000000000006` to `y`.
    
    
    [](types-ii-way-more-types.html#cb224-1)x is exact: 0.12345678901234500    Printed to 17 decimal places
    [](types-ii-way-more-types.html#cb224-2)y is exact: 0.00000000000000060

But let’s add them together. This should give `0.1234567890123456`, but that’s more than `DBL_DIG`, so strange things might happen… let’s look:
    
    
    [](types-ii-way-more-types.html#cb225-1)x + y not quite right: 0.12345678901234559    Should end in 4560!

That’s what we get for printing more than `DBL_DIG`, right? But check this out… that number, above, is exactly representable as it is!

If we assign `0.12345678901234559` (17 digits) to `z` and print it, we get:
    
    
    [](types-ii-way-more-types.html#cb226-1)z is exact: 0.12345678901234559   17 digits correct! More than DBL_DIG!

If we’d truncated `z` down to 15 digits, it wouldn’t have been the same number. That’s why to preserve all the bits of a `double`, we need `DBL_DECIMAL_DIG` and not just the lesser `DBL_DIG`.

All that being said, it’s clear that when we’re messing with decimal numbers in general, it’s not safe to print more than `FLT_DIG`, `DBL_DIG`, or `LDBL_DIG` digits to be sensible in relation to the original base 10 numbers and any subsequent math.

But when converting from `float` to a decimal representation and _back_ to `float`, definitely use `FLT_DECIMAL_DIG` to do that so that all the bits are preserved exactly. 

## 14.5 Constant Numeric Types

When you write down a constant number, like `1234`, it has a type. But what type is it? Let’s look at how C decides what type the constant is, and how to force it to choose a specific type.

### 14.5.1 Hexadecimal and Octal

In addition to good ol’ decimal like Grandma used to bake, C also supports constants of different bases.

If you lead a number with `0x`, it is read as a hex number:
    
    
    [](types-ii-way-more-types.html#cb227-1)int a = 0x1A2B;   // Hexadecimal
    [](types-ii-way-more-types.html#cb227-2)int b = 0x1a2b;   // Case doesn't matter for hex digits
    [](types-ii-way-more-types.html#cb227-3)
    [](types-ii-way-more-types.html#cb227-4)printf("%x", a);  // Print a hex number, "1a2b"

If you lead a number with a `0`, it is read as an octal number:
    
    
    [](types-ii-way-more-types.html#cb228-1)int a = 012;
    [](types-ii-way-more-types.html#cb228-2)
    [](types-ii-way-more-types.html#cb228-3)printf("%o\n", a);  // Print an octal number, "12"

This is particularly problematic for beginner programmers who try to pad decimal numbers on the left with `0` to line things up nice and pretty, inadvertently changing the base of the number:
    
    
    [](types-ii-way-more-types.html#cb229-1)int x = 11111;  // Decimal 11111
    [](types-ii-way-more-types.html#cb229-2)int y = 00111;  // Decimal 73 (Octal 111)
    [](types-ii-way-more-types.html#cb229-3)int z = 01111;  // Decimal 585 (Octal 1111)

#### 14.5.1.1 A Note on Binary

An unofficial extension[105](function-specifiers-alignment-specifiersoperators.html#fn105) in many C compilers allows you to represent a binary number with a `0b` prefix:
    
    
    [](types-ii-way-more-types.html#cb230-1)int x = 0b101010;    // Binary 101010
    [](types-ii-way-more-types.html#cb230-2)
    [](types-ii-way-more-types.html#cb230-3)printf("%d\n", x);   // Prints 42 decimal

There’s no `printf()` format specifier for printing a binary number. You have to do it a character at a time with bitwise operators.

### 14.5.2 Integer Constants

You can force a constant integer to be a certain type by appending a suffix to it that indicates the type.

We’ll do some assignments to demo, but most often devs leave off the suffixes unless needed to be precise. The compiler is pretty good at making sure the types are compatible.
    
    
    [](types-ii-way-more-types.html#cb231-1)int           x = 1234;
    [](types-ii-way-more-types.html#cb231-2)long int      x = 1234L;
    [](types-ii-way-more-types.html#cb231-3)long long int x = 1234LL
    [](types-ii-way-more-types.html#cb231-4)
    [](types-ii-way-more-types.html#cb231-5)unsigned int           x = 1234U;
    [](types-ii-way-more-types.html#cb231-6)unsigned long int      x = 1234UL;
    [](types-ii-way-more-types.html#cb231-7)unsigned long long int x = 1234ULL;

The suffix can be uppercase or lowercase. And the `U` and `L` or `LL` can appear either one first.

Type | Suffix  
---|---  
`int` | None  
`long int` | `L`  
`long long int` | `LL`  
`unsigned int` | `U`  
`unsigned long int` | `UL`  
`unsigned long long int` | `ULL`  
  
I mentioned in the table that “no suffix” means `int`… but it’s actually more complex than that.

So what happens when you have an unsuffixed number like:
    
    
    [](types-ii-way-more-types.html#cb232-1)int x = 1234;

What type is it?

What C will generally do is choose the smallest type from `int` up that can hold the value.

But specifically, that depends on the number’s base (decimal, hex, or octal), as well.

The spec has a great table indicating which type gets used for what unsuffixed value. In fact, I’m just going to copy it wholesale right here.

C11 §6.4.4.1¶5 reads, “The type of an integer constant is the first of the first of the corresponding list in which its value can be represented.”

And then goes on to show this table:

Suffix | Decimal Constant | Octal or Hexadecimal  
Constant  
---|---|---  
none | `int`  
`long int` | `int`  
`unsigned int`  
`long int`  
`unsigned long int`  
`long long int`  
`unsigned long long int`  
  
`u` or `U` | `unsigned int`  
`unsigned long int`  
`unsigned long long int` | `unsigned int`  
`unsigned long int`  
`unsigned long long int`  
  
`l` or `L` | `long int`  
`long long int` | `long int`  
`unsigned long int`  
`long long int`  
`unsigned long long int`  
  
Both `u` or `U`  
and `l` or `L` | `unsigned long int`  
`unsigned long long int` | `unsigned long int`  
`unsigned long long int`  
  
`ll` or `LL` | `long long int` | `long long int`  
`unsigned long long int`  
  
Both `u` or `U`  
and `ll` or `LL` | `unsigned long long int` | `unsigned long long int`  
  
What that’s saying is that, for example, if you specify a number like `123456789U`, first C will see if it can be `unsigned int`. If it doesn’t fit there, it’ll try `unsigned long int`. And then `unsigned long long int`. It’ll use the smallest type that can hold the number.

### 14.5.3 Floating Point Constants

You’d think that a floating point constant like `1.23` would have a default type of `float`, right?

Surprise! Turns out unsuffiexed floating point numbers are type `double`! Happy belated birthday!

You can force it to be of type `float` by appending an `f` (or `F`—it’s case-insensitive). You can force it to be of type `long double` by appending `l` (or `L`).

Type | Suffix  
---|---  
`float` | `F`  
`double` | None  
`long double` | `L`  
  
For example:
    
    
    [](types-ii-way-more-types.html#cb233-1)float x       = 3.14f;
    [](types-ii-way-more-types.html#cb233-2)double x      = 3.14;
    [](types-ii-way-more-types.html#cb233-3)long double x = 3.14L;

This whole time, though, we’ve just been doing this, right?
    
    
    [](types-ii-way-more-types.html#cb234-1)float x = 3.14;

Isn’t the left a `float` and the right a `double`? Yes! But C’s pretty good with automatic numeric conversions, so it’s more common to have an unsuffixed floating point constant than not. More on that later.

#### 14.5.3.1 Scientific Notation

Remember earlier when we talked about how a floating point number can be represented by a significand, base, and exponent?

Well, there’s a common way of writing such a number, shown here followed by it’s more recognizable equivalent which is what you get when you actually run the math:

\\(1.2345\times10^3 = 1234.5\\)

Writing numbers in the form \\(s\times b^e\\) is called [_scientific notation_](https://en.wikipedia.org/wiki/Scientific_notation)[ 106](function-specifiers-alignment-specifiersoperators.html#fn106). In C, these are written using “E notation”, so these are equivalent:

Scientific Notation | E notation  
---|---  
\\(1.2345\times10^{-3}=0.0012345\\) | `1.2345e-3`  
\\(1.2345\times10^8=123450000\\) | `1.2345e+8`  
  
You can print a number in this notation with `%e`:
    
    
    [](types-ii-way-more-types.html#cb235-1)printf("%e\n", 123456.0);  // Prints 1.234560e+05

A couple little fun facts about scientific notation:

  * You don’t have to write them with a single leading digit before the decimal point. Any number of numbers can go in front.
        
        [](types-ii-way-more-types.html#cb236-1)double x = 123.456e+3;  // 123456

However, when you print it, it will change the exponent so there is only one digit in front of the decimal point.

  * The plus can be left off the exponent, as it’s default, but this is uncommon in practice from what I’ve seen.
        
        [](types-ii-way-more-types.html#cb237-1)1.2345e10 == 1.2345e+10

  * You can apply the `F` or `L` suffixes to E-notation constants:
        
        [](types-ii-way-more-types.html#cb238-1)1.2345e10F
        [](types-ii-way-more-types.html#cb238-2)1.2345e10L




#### 14.5.3.2 Hexadecimal Floating Point Constants

But wait, there’s more floating to be done!

Turns out there are hexadecimal floating point constants, as well!

These work similar to decimal floating point numbers, but they begin with a `0x` just like integer numbers.

The catch is that you _must_ specify an exponent, and this exponent produces a power of 2. That is: \\(2^x\\).

And then you use a `p` instead of an `e` when writing the number:

So `0xa.1p3` is \\(10.0625\times2^3 == 80.5\\).

When using floating point hex constants, We can print hex scientific notation with `%a`:
    
    
    [](types-ii-way-more-types.html#cb239-1)double x = 0xa.1p3;
    [](types-ii-way-more-types.html#cb239-2)
    [](types-ii-way-more-types.html#cb239-3)printf("%a\n", x);  // 0x1.42p+6
    [](types-ii-way-more-types.html#cb239-4)printf("%f\n", x);  // 80.500000

* * *

[Prev](scope.html) | [Contents](index.html) | [Next](types-iii-conversions.html)

---

[Prev](types-ii-way-more-types.html) | [Contents](index.html) | [Next](types-iv-qualifiers-and-specifiers.html)

* * *

# 15 Types III: Conversions

In this chapter, we want to talk all about converting from one type to another. C has a variety of ways of doing this, and some might be a little different that you’re used to in other languages.

Before we talk about how to make conversions happen, let’s talk about how they work when they _do_ happen.

## 15.1 String Conversions

Unlike many languages, C doesn’t do string-to-number (and vice-versa) conversions in quite as streamlined a manner as it does numeric conversions.

For these, we’ll have to call functions to do the dirty work.

### 15.1.1 Numeric Value to String

When we want to convert a number to a string, we can use either `sprintf()` (pronounced _SPRINT-f_) or `snprintf()` (_s-n-print-f_)[107](function-specifiers-alignment-specifiersoperators.html#fn107)

These basically work like `printf()`, except they output to a string instead, and you can print that string later, or whatever.

For example, turning part of the value π into a string:
    
    
    [](types-iii-conversions.html#cb240-1)#include <stdio.h>
    [](types-iii-conversions.html#cb240-2)
    [](types-iii-conversions.html#cb240-3)int main(void)
    [](types-iii-conversions.html#cb240-4){
    [](types-iii-conversions.html#cb240-5)    char s[10];
    [](types-iii-conversions.html#cb240-6)    float f = 3.14159;
    [](types-iii-conversions.html#cb240-7)
    [](types-iii-conversions.html#cb240-8)    // Convert "f" to string, storing in "s", writing at most 10 characters
    [](types-iii-conversions.html#cb240-9)    // including the NUL terminator
    [](types-iii-conversions.html#cb240-10)
    [](types-iii-conversions.html#cb240-11)    snprintf(s, 10, "%f", f);
    [](types-iii-conversions.html#cb240-12)
    [](types-iii-conversions.html#cb240-13)    printf("String value: %s\n", s);  // String value: 3.141590
    [](types-iii-conversions.html#cb240-14)}

So you can use `%d` or `%u` like you’re used to for integers.

### 15.1.2 String to Numeric Value

There are a couple families of functions to do this in C. We’ll call these the `atoi` (pronounced _a-to-i_) family and the `strtol` (_stir-to-long_) family.

For basic conversion from a string to a number, try the `atoi` functions from `<stdlib.h>`. These have bad error-handling characteristics (including undefined behavior if you pass in a bad string), so use them carefully.

Function | Description  
---|---  
`atoi` | String to `int`  
`atof` | String to `float`  
`atol` | String to `long int`  
`atoll` | String to `long long int`  
  
Though the spec doesn’t cop to it, the `a` at the beginning of the function stands for [ASCII](https://en.wikipedia.org/wiki/ASCII)[108](function-specifiers-alignment-specifiersoperators.html#fn108), so really `atoi()` is “ASCII-to-integer”, but saying so today is a bit ASCII-centric.

Here’s an example converting a string to a `float`:
    
    
    [](types-iii-conversions.html#cb241-1)#include <stdio.h>
    [](types-iii-conversions.html#cb241-2)#include <stdlib.h>
    [](types-iii-conversions.html#cb241-3)
    [](types-iii-conversions.html#cb241-4)int main(void)
    [](types-iii-conversions.html#cb241-5){
    [](types-iii-conversions.html#cb241-6)    char *pi = "3.14159";
    [](types-iii-conversions.html#cb241-7)    float f;
    [](types-iii-conversions.html#cb241-8)
    [](types-iii-conversions.html#cb241-9)    f = atof(pi);
    [](types-iii-conversions.html#cb241-10)
    [](types-iii-conversions.html#cb241-11)    printf("%f\n", f);
    [](types-iii-conversions.html#cb241-12)}

But, like I said, we get undefined behavior from weird things like this:
    
    
    [](types-iii-conversions.html#cb242-1)int x = atoi("what");  // "What" ain't no number I ever heard of

(When I run that, I get `0` back, but you really shouldn’t count on that in any way. You could get something completely different.)

For better error handling characteristics, let’s check out all those `strtol` functions, also in `<stdlib.h>`. Not only that, but they convert to more types and more bases, too!

Function | Description  
---|---  
`strtol` | String to `long int`  
`strtoll` | String to `long long int`  
`strtoul` | String to `unsigned long int`  
`strtoull` | String to `unsigned long long int`  
`strtof` | String to `float`  
`strtod` | String to `double`  
`strtold` | String to `long double`  
  
These functions all follow a similar pattern of use, and are a lot of people’s first experience with pointers to pointers! But never fret—it’s easier than it looks.

Let’s do an example where we convert a string to an `unsigned long`, discarding error information (i.e. information about bad characters in the input string):
    
    
    [](types-iii-conversions.html#cb243-1)#include <stdio.h>
    [](types-iii-conversions.html#cb243-2)#include <stdlib.h>
    [](types-iii-conversions.html#cb243-3)
    [](types-iii-conversions.html#cb243-4)int main(void)
    [](types-iii-conversions.html#cb243-5){
    [](types-iii-conversions.html#cb243-6)    char *s = "3490";
    [](types-iii-conversions.html#cb243-7)
    [](types-iii-conversions.html#cb243-8)    // Convert string s, a number in base 10, to an unsigned long int.
    [](types-iii-conversions.html#cb243-9)    // NULL means we don't care to learn about any error information.
    [](types-iii-conversions.html#cb243-10)
    [](types-iii-conversions.html#cb243-11)    unsigned long int x = strtoul(s, NULL, 10);
    [](types-iii-conversions.html#cb243-12)
    [](types-iii-conversions.html#cb243-13)    printf("%lu\n", x);  // 3490
    [](types-iii-conversions.html#cb243-14)}

Notice a couple things there. Even though we didn’t deign to capture any information about error characters in the string, `strtoul()` won’t give us undefined behavior; it will just return `0`.

Also, we specified that this was a decimal (base 10) number.

Does this mean we can convert numbers of different bases? Sure! Let’s do binary!
    
    
    [](types-iii-conversions.html#cb244-1)#include <stdio.h>
    [](types-iii-conversions.html#cb244-2)#include <stdlib.h>
    [](types-iii-conversions.html#cb244-3)
    [](types-iii-conversions.html#cb244-4)int main(void)
    [](types-iii-conversions.html#cb244-5){
    [](types-iii-conversions.html#cb244-6)    char *s = "101010";  // What's the meaning of this number?
    [](types-iii-conversions.html#cb244-7)
    [](types-iii-conversions.html#cb244-8)    // Convert string s, a number in base 2, to an unsigned long int.
    [](types-iii-conversions.html#cb244-9)
    [](types-iii-conversions.html#cb244-10)    unsigned long int x = strtoul(s, NULL, 2);
    [](types-iii-conversions.html#cb244-11)
    [](types-iii-conversions.html#cb244-12)    printf("%lu\n", x);  // 42
    [](types-iii-conversions.html#cb244-13)}

OK, that’s all fun and games, but what’s with that `NULL` in there? What’s that for?

That helps us figure out if an error occurred in the processing of the string. It’s a pointer to a pointer to a `char`, which sounds scary, but isn’t once you wrap your head around it.

Let’s do an example where we feed in a deliberately bad number, and we’ll see how `strtol()` lets us know where the first invalid digit is.
    
    
    [](types-iii-conversions.html#cb245-1)#include <stdio.h>
    [](types-iii-conversions.html#cb245-2)#include <stdlib.h>
    [](types-iii-conversions.html#cb245-3)
    [](types-iii-conversions.html#cb245-4)int main(void)
    [](types-iii-conversions.html#cb245-5){
    [](types-iii-conversions.html#cb245-6)    char *s = "34x90";  // "x" is not a valid digit in base 10!
    [](types-iii-conversions.html#cb245-7)    char *badchar;
    [](types-iii-conversions.html#cb245-8)
    [](types-iii-conversions.html#cb245-9)    // Convert string s, a number in base 10, to an unsigned long int.
    [](types-iii-conversions.html#cb245-10)
    [](types-iii-conversions.html#cb245-11)    unsigned long int x = strtoul(s, &badchar, 10);
    [](types-iii-conversions.html#cb245-12)
    [](types-iii-conversions.html#cb245-13)    // It tries to convert as much as possible, so gets this far:
    [](types-iii-conversions.html#cb245-14)
    [](types-iii-conversions.html#cb245-15)    printf("%lu\n", x);  // 34
    [](types-iii-conversions.html#cb245-16)
    [](types-iii-conversions.html#cb245-17)    // But we can see the offending bad character because badchar
    [](types-iii-conversions.html#cb245-18)    // points to it!
    [](types-iii-conversions.html#cb245-19)
    [](types-iii-conversions.html#cb245-20)    printf("Invalid character: %c\n", *badchar);  // "x"
    [](types-iii-conversions.html#cb245-21)}

So there we have `strtoul()` modifying what `badchar` points to in order to show us where things went wrong[109](function-specifiers-alignment-specifiersoperators.html#fn109).

But what if nothing goes wrong? In that case, `badchar` will point to the `NUL` terminator at the end of the string. So we can test for it:
    
    
    [](types-iii-conversions.html#cb246-1)#include <stdio.h>
    [](types-iii-conversions.html#cb246-2)#include <stdlib.h>
    [](types-iii-conversions.html#cb246-3)
    [](types-iii-conversions.html#cb246-4)int main(void)
    [](types-iii-conversions.html#cb246-5){
    [](types-iii-conversions.html#cb246-6)    char *s = "3490";  // "x" is not a valid digit in base 10!
    [](types-iii-conversions.html#cb246-7)    char *badchar;
    [](types-iii-conversions.html#cb246-8)
    [](types-iii-conversions.html#cb246-9)    // Convert string s, a number in base 10, to an unsigned long int.
    [](types-iii-conversions.html#cb246-10)
    [](types-iii-conversions.html#cb246-11)    unsigned long int x = strtoul(s, &badchar, 10);
    [](types-iii-conversions.html#cb246-12)
    [](types-iii-conversions.html#cb246-13)    // Check if things went well
    [](types-iii-conversions.html#cb246-14)
    [](types-iii-conversions.html#cb246-15)    if (*badchar == '\0') {
    [](types-iii-conversions.html#cb246-16)        printf("Success! %lu\n", x);
    [](types-iii-conversions.html#cb246-17)    } else  {
    [](types-iii-conversions.html#cb246-18)        printf("Partial conversion: %lu\n", x);
    [](types-iii-conversions.html#cb246-19)        printf("Invalid character: %c\n", *badchar);
    [](types-iii-conversions.html#cb246-20)    }
    [](types-iii-conversions.html#cb246-21)}

So there you have it. The `atoi()`-style functions are good in a controlled pinch, but the `strtol()`-style functions give you far more control over error handling and the base of the input.

## 15.2 `char` Conversions

What if you have a single character with a digit in it, like `'5'`… Is that the same as the value `5`?

Let’s try it and see.
    
    
    [](types-iii-conversions.html#cb247-1)printf("%d %d\n", 5, '5');

On my UTF-8 system, this prints:
    
    
    [](types-iii-conversions.html#cb248-1)5 53

So… no. And 53? What is that? That’s the UTF-8 (and ASCII) code point for the character symbol `'5'`[110](function-specifiers-alignment-specifiersoperators.html#fn110)

So how do we convert the character `'5'` (which apparently has value 53) into the value `5`?

With one clever trick, that’s how!

The C Standard guarantees that these character will have code points that are in sequence and in this order:
    
    
    [](types-iii-conversions.html#cb249-1)0  1  2  3  4  5  6  7  8  9

Ponder for a second–how can we use that? Spoilers ahead…

Let’s take a look at the characters and their code points in UTF-8:
    
    
    [](types-iii-conversions.html#cb250-1)0  1  2  3  4  5  6  7  8  9
    [](types-iii-conversions.html#cb250-2)48 49 50 51 52 53 54 55 56 57

You see there that `'5'` is `53`, just like we were getting. And `'0'` is `48`.

So we can subtract `'0'` from any digit character to get its numeric value:
    
    
    [](types-iii-conversions.html#cb251-1)char c = '6';
    [](types-iii-conversions.html#cb251-2)
    [](types-iii-conversions.html#cb251-3)int x = c;  // x has value 54, the code point for '6'
    [](types-iii-conversions.html#cb251-4)
    [](types-iii-conversions.html#cb251-5)int y = c - '0'; // y has value 6, just like we want

And we can convert the other way, too, just by adding the value on.
    
    
    [](types-iii-conversions.html#cb252-1)int x = 6;
    [](types-iii-conversions.html#cb252-2)
    [](types-iii-conversions.html#cb252-3)char c = x + '0';  // c has value 54
    [](types-iii-conversions.html#cb252-4)
    [](types-iii-conversions.html#cb252-5)printf("%d\n", c);  // prints 54
    [](types-iii-conversions.html#cb252-6)printf("%c\n", c);  // prints 6 with %c

You might think this is a weird way to do this conversion, and by today’s standards, it certainly is. But back in the olden days when computers were made literally out of wood, this was the method for doing this conversion. And it wasn’t broke, so C never fixed it.

## 15.3 Numeric Conversions

### 15.3.1 Boolean

If you convert a zero to `bool`, the result is `0`. Otherwise it’s `1`.

### 15.3.2 Integer to Integer Conversions

If an integer type is converted to unsigned and doesn’t fit in it, the unsigned result wraps around odometer-style until it fits in the unsigned[111](function-specifiers-alignment-specifiersoperators.html#fn111).

If an integer type is converted to a signed number and doesn’t fit, the result is implementation-defined! Something documented will happen, but you’ll have to look it up[112](function-specifiers-alignment-specifiersoperators.html#fn112)

### 15.3.3 Integer and Floating Point Conversions

If a floating point type is converted to an integer type, the fractional part is discarded with prejudice[113](function-specifiers-alignment-specifiersoperators.html#fn113).

But—and here’s the catch—if the number is too large to fit in the integer, you get undefined behavior. So don’t do that.

Going From integer or floating point to floating point, C makes a best effort to find the closest floating point number to the integer that it can.

Again, though, if the original value can’t be represented, it’s undefined behavior.

## 15.4 Implicit Conversions

These are conversions the compiler does automatically for you when you mix and match types.

### 15.4.1 The Integer Promotions

In a number of places, if an `int` can be used to represent a value from `char` or `short` (signed or unsigned), that value is _promoted_ up to `int`. If it doesn’t fit in an `int`, it’s promoted to `unsigned int`.

This is how we can do something like this:
    
    
    [](types-iii-conversions.html#cb253-1)char x = 10, y = 20;
    [](types-iii-conversions.html#cb253-2)int i = x + y;

In that case, `x` and `y` get promoted to `int` by C before the math takes place.

The integer promotions take place during The Usual Arithmetic Conversions, with variadic functions[114](function-specifiers-alignment-specifiersoperators.html#fn114), unary `+` and `-` operators, or when passing values to functions without prototypes[115](function-specifiers-alignment-specifiersoperators.html#fn115).

### 15.4.2 The Usual Arithmetic Conversions

These are automatic conversions that C does around numeric operations that you ask for. (That’s actually what they’re called, by the way, by C11 §6.3.1.8.) Note that for this section, we’re just talking about numeric types—strings will come later.

These conversions answer questions about what happens when you mix types, like this:
    
    
    [](types-iii-conversions.html#cb254-1)int x = 3 + 1.2;   // Mixing int and double
    [](types-iii-conversions.html#cb254-2)                   // 4.2 is converted to int
    [](types-iii-conversions.html#cb254-3)                   // 4 is stored in x
    [](types-iii-conversions.html#cb254-4)
    [](types-iii-conversions.html#cb254-5)float y = 12 * 2;  // Mixing float and int
    [](types-iii-conversions.html#cb254-6)                   // 24 is converted to float
    [](types-iii-conversions.html#cb254-7)                   // 24.0 is stored in y

Do they become `int`s? Do they become `float`s? How does it work?

Here are the steps, paraphrased for easy consumption.

  1. If one thing in the expression is a floating type, convert the other things to that floating type.

  2. Otherwise, if both types are integer types, perform the integer promotions on each, then make the operand types as big as they need to be hold the common largest value. Sometimes this involves changing signed to unsigned.




If you want to know the gritty details, check out C11 §6.3.1.8. But you probably don’t.

Just generally remember that int types become float types if there’s a floating point type anywhere in there, and the compiler makes an effort to make sure mixed integer types don’t overflow.

Finally, if you convert from one floating point type to another, the compiler will try to make an exact conversion. If it can’t, it’ll do the best approximation it can. If the number is too large to fit in the type you’re converting into, _boom_ : undefined behavior!

### 15.4.3 `void*`

The `void*` type is interesting because it can be converted from or to any pointer type.
    
    
    [](types-iii-conversions.html#cb255-1)int x = 10;
    [](types-iii-conversions.html#cb255-2)
    [](types-iii-conversions.html#cb255-3)void *p = &x;  // &x is type int*, but we store it in a void*
    [](types-iii-conversions.html#cb255-4)
    [](types-iii-conversions.html#cb255-5)int *q = p;    // p is void*, but we store it in an int*

## 15.5 Explicit Conversions

These are conversions from type to type that you have to ask for; the compiler won’t do it for you.

You can convert from one type to another by assigning one type to another with an `=`.

You can also convert explicitly with a _cast_.

### 15.5.1 Casting

You can explicitly change the type of an expression by putting a new type in parentheses in front of it. Some C devs frown on the practice unless absolutely necessary, but it’s likely you’ll come across some C code with these in it.

Let’s do an example where we want to convert an `int` into a `long` so that we can store it in a `long`.

Note: this example is contrived and the cast in this case is completely unnecessary because the `x + 12` expression would automatically be changed to `long int` to match the wider type of `y`.
    
    
    [](types-iii-conversions.html#cb256-1)int x = 10;
    [](types-iii-conversions.html#cb256-2)long int y = (long int)x + 12;

In that example, even those `x` was type `int` before, the expression `(long int)x` has type `long int`. We say, “We cast `x` to `long int`.”

More commonly, you might see a cast being used to convert a `void*` into a specific pointer type so it can be dereferenced.

A callback from the built-in `qsort()` function might display this behavior since it has `void*`s passed into it:
    
    
    [](types-iii-conversions.html#cb257-1)int compar(const void *elem1, const void *elem2)
    [](types-iii-conversions.html#cb257-2){
    [](types-iii-conversions.html#cb257-3)    if (*((const int*)elem2) > *((const int*)elem1)) return 1;
    [](types-iii-conversions.html#cb257-4)    if (*((const int*)elem2) < *((const int*)elem1)) return -1;
    [](types-iii-conversions.html#cb257-5)    return 0;
    [](types-iii-conversions.html#cb257-6)}

But you could also clearly write it with an assignment:
    
    
    [](types-iii-conversions.html#cb258-1)int compar(const void *elem1, const void *elem2)
    [](types-iii-conversions.html#cb258-2){
    [](types-iii-conversions.html#cb258-3)    const int *e1 = elem1;
    [](types-iii-conversions.html#cb258-4)    const int *e2 = elem2;
    [](types-iii-conversions.html#cb258-5)
    [](types-iii-conversions.html#cb258-6)    return *e2 - *e1;
    [](types-iii-conversions.html#cb258-7)}

One place you’ll see casts more commonly is to avoid a warning when printing pointer values with the rarely-used `%p` which gets picky with anything other than a `void*`:
    
    
    [](types-iii-conversions.html#cb259-1)int x = 3490;
    [](types-iii-conversions.html#cb259-2)int *p = &x;
    [](types-iii-conversions.html#cb259-3)
    [](types-iii-conversions.html#cb259-4)printf("%p\n", p);

generates this warning:
    
    
    [](types-iii-conversions.html#cb260-1)warning: format ‘%p’ expects argument of type ‘void *’, but argument
    [](types-iii-conversions.html#cb260-2)         2 has type ‘int *’

You can fix it with a cast:
    
    
    [](types-iii-conversions.html#cb261-1)printf("%p\n", (void *)p);

Another place is with explicit pointer changes, if you don’t want to use an intervening `void*`, but these are also pretty uncommon:
    
    
    [](types-iii-conversions.html#cb262-1)long x = 3490;
    [](types-iii-conversions.html#cb262-2)long *p = &x;
    [](types-iii-conversions.html#cb262-3)unsigned char *c = (unsigned char *)p;

A third place it’s often required is with the character conversion functions in [`<ctype.h>`](https://beej.us/guide/bgclr/html/split/ctype.html)[116](function-specifiers-alignment-specifiersoperators.html#fn116) where you should cast questionably-signed values to `unsigned char` to avoid undefined behavior.

Again, casting is rarely _needed_ in practice. If you find yourself casting, there might be another way to do the same thing, or maybe you’re casting unnecessarily.

Or maybe it is necessary. Personally, I try to avoid it, but am not afraid to use it if I have to.

* * *

[Prev](types-ii-way-more-types.html) | [Contents](index.html) | [Next](types-iv-qualifiers-and-specifiers.html)

---

[Prev](types-iii-conversions.html) | [Contents](index.html) | [Next](multifile-projects.html)

* * *

# 16 Types IV: Qualifiers and Specifiers

Now that we have some more types under our belts, turns out we can give these types some additional attributes that control their behavior. These are the _type qualifiers_ and _storage-class specifiers_.

## 16.1 Type Qualifiers

These are going to allow you to declare constant values, and also to give the compiler optimization hints that it can use.

### 16.1.1 `const`

This is the most common type qualifier you’ll see. It means the variable is constant, and any attempt to modify it will result in a very angry compiler.
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb263-1)const int x = 2;
    [](types-iv-qualifiers-and-specifiers.html#cb263-2)
    [](types-iv-qualifiers-and-specifiers.html#cb263-3)x = 4;  // COMPILER PUKING SOUNDS, can't assign to a constant

You can’t change a `const` value.

Often you see `const` in parameter lists for functions:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb264-1)void foo(const int x)
    [](types-iv-qualifiers-and-specifiers.html#cb264-2){
    [](types-iv-qualifiers-and-specifiers.html#cb264-3)    printf("%d\n", x + 30);  // OK, doesn't modify "x"
    [](types-iv-qualifiers-and-specifiers.html#cb264-4)}

#### 16.1.1.1 `const` and Pointers

This one gets a little funky, because there are two usages that have two meanings when it comes to pointers.

For one thing, we can make it so you can’t change the thing the pointer points to. You do this by putting the `const` up front with the type name (before the asterisk) in the type declaration.
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb265-1)int x[] = {10, 20};
    [](types-iv-qualifiers-and-specifiers.html#cb265-2)const int *p = x; 
    [](types-iv-qualifiers-and-specifiers.html#cb265-3)
    [](types-iv-qualifiers-and-specifiers.html#cb265-4)p++;  // We can modify p, no problem
    [](types-iv-qualifiers-and-specifiers.html#cb265-5)
    [](types-iv-qualifiers-and-specifiers.html#cb265-6)*p = 30; // Compiler error! Can't change what it points to

Somewhat confusingly, these two things are equivalent:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb266-1)const int *p;  // Can't modify what p points to
    [](types-iv-qualifiers-and-specifiers.html#cb266-2)int const *p;  // Can't modify what p points to, just like the previous line

Great, so we can’t change the thing the pointer points to, but we can change the pointer itself. What if we want the other way around? We want to be able to change what the pointer points to, but _not_ the pointer itself?

Just move the `const` after the asterisk in the declaration:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb267-1)int *const p;   // We can't modify "p" with pointer arithmetic
    [](types-iv-qualifiers-and-specifiers.html#cb267-2)
    [](types-iv-qualifiers-and-specifiers.html#cb267-3)p++;  // Compiler error!

But we can modify what they point to:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb268-1)int x = 10;
    [](types-iv-qualifiers-and-specifiers.html#cb268-2)int *const p = &x;
    [](types-iv-qualifiers-and-specifiers.html#cb268-3)
    [](types-iv-qualifiers-and-specifiers.html#cb268-4)*p = 20;   // Set "x" to 20, no problem

You can also make both things `const`:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb269-1)const int *const p;  // Can't modify p or *p!

Finally, if you have multiple levels of indirection, you should `const` the appropriate levels. Just because a pointer is `const`, doesn’t mean the pointer it points to must also be. You can explicitly set them like in the following examples:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb270-1)char **p;
    [](types-iv-qualifiers-and-specifiers.html#cb270-2)p++;     // OK!
    [](types-iv-qualifiers-and-specifiers.html#cb270-3)(*p)++;  // OK!
    [](types-iv-qualifiers-and-specifiers.html#cb270-4)
    [](types-iv-qualifiers-and-specifiers.html#cb270-5)char **const p;
    [](types-iv-qualifiers-and-specifiers.html#cb270-6)p++;     // Error!
    [](types-iv-qualifiers-and-specifiers.html#cb270-7)(*p)++;  // OK!
    [](types-iv-qualifiers-and-specifiers.html#cb270-8)
    [](types-iv-qualifiers-and-specifiers.html#cb270-9)char *const *p;
    [](types-iv-qualifiers-and-specifiers.html#cb270-10)p++;     // OK!
    [](types-iv-qualifiers-and-specifiers.html#cb270-11)(*p)++;  // Error!
    [](types-iv-qualifiers-and-specifiers.html#cb270-12)
    [](types-iv-qualifiers-and-specifiers.html#cb270-13)char *const *const p;
    [](types-iv-qualifiers-and-specifiers.html#cb270-14)p++;     // Error!
    [](types-iv-qualifiers-and-specifiers.html#cb270-15)(*p)++;  // Error!

#### 16.1.1.2 `const` Correctness

One more thing I have to mention is that the compiler will warn on something like this:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb271-1)const int x = 20;
    [](types-iv-qualifiers-and-specifiers.html#cb271-2)int *p = &x;

saying something to the effect of:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb272-1)initialization discards 'const' qualifier from pointer type target

What’s happening there?

Well, we need to look at the types on either side of the assignment:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb273-1)    const int x = 20;
    [](types-iv-qualifiers-and-specifiers.html#cb273-2)    int *p = &x;
    [](types-iv-qualifiers-and-specifiers.html#cb273-3)//    ^       ^
    [](types-iv-qualifiers-and-specifiers.html#cb273-4)//    |       |
    [](types-iv-qualifiers-and-specifiers.html#cb273-5)//  int*    const int*

The compiler is warning us that the value on the right side of the assignment is `const`, but the one of the left is not. And the compiler is letting us know that it is discarding the “const-ness” of the expression on the right.

That is, we _can_ still try to do the following, but it’s just wrong. The compiler will warn, and it’s undefined behavior:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb274-1)const int x = 20;
    [](types-iv-qualifiers-and-specifiers.html#cb274-2)int *p = &x;
    [](types-iv-qualifiers-and-specifiers.html#cb274-3)
    [](types-iv-qualifiers-and-specifiers.html#cb274-4)*p = 40;  // Undefined behavior--maybe it modifies "x", maybe not!
    [](types-iv-qualifiers-and-specifiers.html#cb274-5)
    [](types-iv-qualifiers-and-specifiers.html#cb274-6)printf("%d\n", x);  // 40, if you're lucky

### 16.1.2 `restrict`

TLDR: you never have to use this and you can ignore it every time you see it. If you use it correctly, you will likely realize some performance gain. If you use it incorrectly, you will realize undefined behavior.

`restrict` is a hint to the compiler that a particular piece of memory will only be accessed by one pointer and never another. (That is, there will be no aliasing of the particular object the `restrict` pointer points to.) If a developer declares a pointer to be `restrict` and then accesses the object it points to in another way (e.g. via another pointer), the behavior is undefined.

Basically you’re telling C, “Hey—I guarantee that this one single pointer is the only way I access this memory, and if I’m lying, you can pull undefined behavior on me.”

And C uses that information to perform certain optimizations. For instance, if you’re dereferencing the `restrict` pointer repeatedly in a loop, C might decide to cache the result in a register and only store the final result once the loop completes. If any other pointer referred to that same memory and accessed it in the loop, the results would not be accurate.

(Note that `restrict` has no effect if the object pointed to is never written to. It’s all about optimizations surrounding writes to memory.)

Let’s write a function to swap two variables, and we’ll use the `restrict` keyword to assure C that we’ll never pass in pointers to the same thing. And then let’s blow it and try passing in pointers to the same thing.
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb275-1)void swap(int *restrict a, int *restrict b)
    [](types-iv-qualifiers-and-specifiers.html#cb275-2){
    [](types-iv-qualifiers-and-specifiers.html#cb275-3)    int t;
    [](types-iv-qualifiers-and-specifiers.html#cb275-4)
    [](types-iv-qualifiers-and-specifiers.html#cb275-5)    t = *a;
    [](types-iv-qualifiers-and-specifiers.html#cb275-6)    *a = *b;
    [](types-iv-qualifiers-and-specifiers.html#cb275-7)    *b = t;
    [](types-iv-qualifiers-and-specifiers.html#cb275-8)}
    [](types-iv-qualifiers-and-specifiers.html#cb275-9)
    [](types-iv-qualifiers-and-specifiers.html#cb275-10)int main(void)
    [](types-iv-qualifiers-and-specifiers.html#cb275-11){
    [](types-iv-qualifiers-and-specifiers.html#cb275-12)    int x = 10, y = 20;
    [](types-iv-qualifiers-and-specifiers.html#cb275-13)
    [](types-iv-qualifiers-and-specifiers.html#cb275-14)    swap(&x, &y);  // OK! "a" and "b", above, point to different things
    [](types-iv-qualifiers-and-specifiers.html#cb275-15)
    [](types-iv-qualifiers-and-specifiers.html#cb275-16)    swap(&x, &x);  // Undefined behavior! "a" and "b" point to the same thing
    [](types-iv-qualifiers-and-specifiers.html#cb275-17)}

If we were to take out the `restrict` keywords, above, that would allow both calls to work safely. But then the compiler might not be able to optimize.

`restrict` has block scope, that is, the restriction only lasts for the scope it’s used. If it’s in a parameter list for a function, it’s in the block scope of that function.

If the restricted pointer points to an array, it only applies to the individual objects in the array. Other pointers could read and write from the array as long as they didn’t read or write any of the same elements as the restricted one.

If it’s outside any function in file scope, the restriction covers the entire program.

You’re likely to see this in library functions like `printf()`:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb276-1)int printf(const char * restrict format, ...);

Again, that’s just telling the compiler that inside the `printf()` function, there will be only one pointer that refers to any part of that `format` string.

One last note: if you’re using array notation in your function parameter for some reason instead of pointer notation, you can use `restrict` like so:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb277-1)void foo(int p[restrict])     // With no size
    [](types-iv-qualifiers-and-specifiers.html#cb277-2)
    [](types-iv-qualifiers-and-specifiers.html#cb277-3)void foo(int p[restrict 10])  // Or with a size

But pointer notation would be more common.

### 16.1.3 `volatile`

You’re unlikely to see or need this unless you’re dealing with hardware directly.

`volatile` tells the compiler that a value might change behind its back and should be looked up every time.

An example might be where the compiler is looking in memory at an address that continuously updates behind the scenes, e.g. some kind of hardware timer.

If the compiler decides to optimize that and store the value in a register for a protracted time, the value in memory will update and won’t be reflected in the register.

By declaring something `volatile`, you’re telling the compiler, “Hey, the thing this points at might change at any time for reasons outside this program code.”
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb278-1)volatile int *p;

### 16.1.4 `_Atomic`

This is an optional C feature that we’ll talk about in [the Atomics chapter](chapter-atomics.html#chapter-atomics).

## 16.2 Storage-Class Specifiers

Storage-class specifiers are similar to type quantifiers. They give the compiler more information about the type of a variable.

### 16.2.1 `auto`

You barely ever see this keyword, since `auto` is the default for block scope variables. It’s implied.

These are the same:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb279-1){
    [](types-iv-qualifiers-and-specifiers.html#cb279-2)    int a;         // auto is the default...
    [](types-iv-qualifiers-and-specifiers.html#cb279-3)    auto int a;    // So this is redundant
    [](types-iv-qualifiers-and-specifiers.html#cb279-4)}

The `auto` keyword indicates that this object has _automatic storage duration_. That is, it exists in the scope in which it is defined, and is automatically deallocated when the scope is exited.

One gotcha about automatic variables is that their value is indeterminate until you explicitly initialize them. We say they’re full of “random” or “garbage” data, though neither of those really makes me happy. In any case, you won’t know what’s in it unless you initialize it.

Always initialize all automatic variables before use!

### 16.2.2 `static`

This keyword has two meanings, depending on if the variable is file scope or block scope.

Let’s start with block scope.

#### 16.2.2.1 `static` in Block Scope

In this case, we’re basically saying, “I just want a single instance of this variable to exist, shared between calls.”

That is, its value will persist between calls.

`static` in block scope with an initializer will only be initialized one time on program startup, not each time the function is called.

Let’s do an example:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb280-1)#include <stdio.h>
    [](types-iv-qualifiers-and-specifiers.html#cb280-2)
    [](types-iv-qualifiers-and-specifiers.html#cb280-3)void counter(void)
    [](types-iv-qualifiers-and-specifiers.html#cb280-4){
    [](types-iv-qualifiers-and-specifiers.html#cb280-5)    static int count = 1;  // This is initialized one time
    [](types-iv-qualifiers-and-specifiers.html#cb280-6)
    [](types-iv-qualifiers-and-specifiers.html#cb280-7)    printf("This has been called %d time(s)\n", count);
    [](types-iv-qualifiers-and-specifiers.html#cb280-8)
    [](types-iv-qualifiers-and-specifiers.html#cb280-9)    count++;
    [](types-iv-qualifiers-and-specifiers.html#cb280-10)}
    [](types-iv-qualifiers-and-specifiers.html#cb280-11)
    [](types-iv-qualifiers-and-specifiers.html#cb280-12)int main(void)
    [](types-iv-qualifiers-and-specifiers.html#cb280-13){
    [](types-iv-qualifiers-and-specifiers.html#cb280-14)    counter();  // "This has been called 1 time(s)"
    [](types-iv-qualifiers-and-specifiers.html#cb280-15)    counter();  // "This has been called 2 time(s)"
    [](types-iv-qualifiers-and-specifiers.html#cb280-16)    counter();  // "This has been called 3 time(s)"
    [](types-iv-qualifiers-and-specifiers.html#cb280-17)    counter();  // "This has been called 4 time(s)"
    [](types-iv-qualifiers-and-specifiers.html#cb280-18)}

See how the value of `count` persists between calls?

One thing of note is that `static` block scope variables are initialized to `0` by default.
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb281-1)static int foo;      // Default starting value is `0`...
    [](types-iv-qualifiers-and-specifiers.html#cb281-2)static int foo = 0;  // So the `0` assignment is redundant

Finally, be advised that if you’re writing multithreaded programs, you have to be sure you don’t let multiple threads trample the same variable.

#### 16.2.2.2 `static` in File Scope

When you get out to file scope, outside any blocks, the meaning rather changes.

Variables at file scope already persist between function calls, so that behavior is already there.

Instead what `static` means in this context is that this variable isn’t visible outside of this particular source file. Kinda like “global”, but only in this file.

More on that in the section about building with multiple source files.

### 16.2.3 `extern`

The `extern` storage-class specifier gives us a way to refer to objects in other source files.

Let’s say, for example, the file `bar.c` had the following as its entirety:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb282-1)// bar.c
    [](types-iv-qualifiers-and-specifiers.html#cb282-2)
    [](types-iv-qualifiers-and-specifiers.html#cb282-3)int a = 37;

Just that. Declaring a new `int a` in file scope.

But what if we had another source file, `foo.c`, and we wanted to refer to the `a` that’s in `bar.c`?

It’s easy with the `extern` keyword:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb283-1)// foo.c
    [](types-iv-qualifiers-and-specifiers.html#cb283-2)
    [](types-iv-qualifiers-and-specifiers.html#cb283-3)extern int a;
    [](types-iv-qualifiers-and-specifiers.html#cb283-4)
    [](types-iv-qualifiers-and-specifiers.html#cb283-5)int main(void)
    [](types-iv-qualifiers-and-specifiers.html#cb283-6){
    [](types-iv-qualifiers-and-specifiers.html#cb283-7)    printf("%d\n", a);  // 37, from bar.c!
    [](types-iv-qualifiers-and-specifiers.html#cb283-8)
    [](types-iv-qualifiers-and-specifiers.html#cb283-9)    a = 99;
    [](types-iv-qualifiers-and-specifiers.html#cb283-10)
    [](types-iv-qualifiers-and-specifiers.html#cb283-11)    printf("%d\n", a);  // Same "a" from bar.c, but it's now 99
    [](types-iv-qualifiers-and-specifiers.html#cb283-12)}

We could have also made the `extern int a` in block scope, and it still would have referred to the `a` in `bar.c`:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb284-1)// foo.c
    [](types-iv-qualifiers-and-specifiers.html#cb284-2)
    [](types-iv-qualifiers-and-specifiers.html#cb284-3)int main(void)
    [](types-iv-qualifiers-and-specifiers.html#cb284-4){
    [](types-iv-qualifiers-and-specifiers.html#cb284-5)    extern int a;
    [](types-iv-qualifiers-and-specifiers.html#cb284-6)
    [](types-iv-qualifiers-and-specifiers.html#cb284-7)    printf("%d\n", a);  // 37, from bar.c!
    [](types-iv-qualifiers-and-specifiers.html#cb284-8)
    [](types-iv-qualifiers-and-specifiers.html#cb284-9)    a = 99;
    [](types-iv-qualifiers-and-specifiers.html#cb284-10)
    [](types-iv-qualifiers-and-specifiers.html#cb284-11)    printf("%d\n", a);  // Same "a" from bar.c, but it's now 99
    [](types-iv-qualifiers-and-specifiers.html#cb284-12)}

Now, if `a` in `bar.c` had been marked `static`. this wouldn’t have worked. `static` variables at file scope are not visible outside that file.

A final note about `extern` on functions. For functions, `extern` is the default, so it’s redundant. You can declare a function `static` if you only want it visible in a single source file.

### 16.2.4 `register`

This is a keyword to hint to the compiler that this variable is frequently-used, and should be made as fast as possible to access. The compiler is under no obligation to agree to it.

Now, modern C compiler optimizers are pretty effective at figuring this out themselves, so it’s rare to see these days.

But if you must:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb285-1)#include <stdio.h>
    [](types-iv-qualifiers-and-specifiers.html#cb285-2)
    [](types-iv-qualifiers-and-specifiers.html#cb285-3)int main(void)
    [](types-iv-qualifiers-and-specifiers.html#cb285-4){
    [](types-iv-qualifiers-and-specifiers.html#cb285-5)    register int a;   // Make "a" as fast to use as possible.
    [](types-iv-qualifiers-and-specifiers.html#cb285-6)
    [](types-iv-qualifiers-and-specifiers.html#cb285-7)    for (a = 0; a < 10; a++)
    [](types-iv-qualifiers-and-specifiers.html#cb285-8)        printf("%d\n", a);
    [](types-iv-qualifiers-and-specifiers.html#cb285-9)}

It does come at a price, however. You can’t take the address of a register:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb286-1)register int a;
    [](types-iv-qualifiers-and-specifiers.html#cb286-2)int *p = &a;    // COMPILER ERROR! Can't take address of a register

The same applies to any part of an array:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb287-1)register int a[] = {11, 22, 33, 44, 55};
    [](types-iv-qualifiers-and-specifiers.html#cb287-2)int *p = a;  // COMPILER ERROR! Can't take address of a[0]

Or dereferencing part of an array:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb288-1)register int a[] = {11, 22, 33, 44, 55};
    [](types-iv-qualifiers-and-specifiers.html#cb288-2)
    [](types-iv-qualifiers-and-specifiers.html#cb288-3)int a = *(a + 2);  // COMPILER ERROR! Address of a[0] taken

Interestingly, for the equivalent with array notation, gcc only warns:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb289-1)register int a[] = {11, 22, 33, 44, 55};
    [](types-iv-qualifiers-and-specifiers.html#cb289-2)
    [](types-iv-qualifiers-and-specifiers.html#cb289-3)int a = a[2];  // COMPILER WARNING!

with:
    
    
    [](types-iv-qualifiers-and-specifiers.html#cb290-1)warning: ISO C forbids subscripting ‘register’ array

The fact that you can’t take the address of a register variable frees the compiler up to make optimizations around that assumption if it hasn’t figured them out already. Also adding `register` to a `const` variable prevents one from accidentally passing its pointer to another function that willfully ignore its constness[117](function-specifiers-alignment-specifiersoperators.html#fn117).

A bit of historic backstory, here: deep inside the CPU are little dedicated “variables” called [_registers_](https://en.wikipedia.org/wiki/Processor_register)[ 118](function-specifiers-alignment-specifiersoperators.html#fn118). They are super fast to access compared to RAM, so using them gets you a speed boost. But they’re not in RAM, so they don’t have an associated memory address (which is why you can’t take the address-of or get a pointer to them).

But, like I said, modern compilers are really good at producing optimal code, using registers whenever possible regardless of whether or not you specified the `register` keyword. Not only that, but the spec allows them to just treat it as if you’d typed `auto`, if they want. So no guarantees.

### 16.2.5 `_Thread_local`

When you’re using multiple threads and you have some variables in either global or `static` block scope, this is a way to make sure that each thread gets its own copy of the variable. This’ll help you avoid race conditions and threads stepping on each other’s toes.

If you’re in block scope, you have to use this along with either `extern` or `static`.

Also, if you include `<threads.h>`, you can use the rather more palatable `thread_local` as an alias for the uglier `_Thread_local`.

More information can be found in the [Threads section](multithreading.html#thread-local).

* * *

[Prev](types-iii-conversions.html) | [Contents](index.html) | [Next](multifile-projects.html)

---

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

---

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

---

[Prev](the-outside-environment.html) | [Contents](index.html) | [Next](structs-ii-more-fun-with-structs.html)

* * *

# 19 The C Preprocessor

Before your program gets compiled, it actually runs through a phase called _preprocessing_. It’s almost like there’s a language _on top_ of the C language that runs first. And it outputs the C code, which then gets compiled.

We’ve already seen this to an extent with `#include`! That’s the C Preprocessor! Where it sees that directive, it includes the named file right there, just as if you’d typed it in there. And _then_ the compiler builds the whole thing.

But it turns out it’s a lot more powerful than just being able to include things. You can define _macros_ that are substituted… and even macros that take arguments!

## 19.1 `#include`

Let’s start with the one we’ve already seen a bunch. This is, of course, a way to include other sources in your source. Very commonly used with header files.

While the spec allows for all kinds of behavior with `#include`, we’re going to take a more pragmatic approach and talk about the way it works on every system I’ve ever seen.

We can split header files into two categories: system and local. Things that are built-in, like `stdio.h`, `stdlib.h`, `math.h`, and so on, you can include with angle brackets:
    
    
    [](the-c-preprocessor.html#cb335-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb335-2)#include <stdlib.h>

The angle brackets tell C, “Hey, don’t look in the current directory for this header file—look in the system-wide include directory instead.”

Which, of course, implies that there must be a way to include local files from the current directory. And there is: with double quotes:
    
    
    [](the-c-preprocessor.html#cb336-1)#include "myheader.h"

Or you can very probably look in relative directories using forward slashes and dots, like this:
    
    
    [](the-c-preprocessor.html#cb337-1)#include "mydir/myheader.h"
    [](the-c-preprocessor.html#cb337-2)#include "../someheader.py"

Don’t use a backslash (`\`) for your path separators in your `#include`! It’s undefined behavior! Use forward slash (`/`) only, even on Windows.

In summary, used angle brackets (`<` and `>`) for the system includes, and use double quotes (`"`) for your personal includes.

## 19.2 Simple Macros

A _macro_ is an identifier that gets _expanded_ to another piece of code before the compiler even sees it. Think of it like a placeholder—when the preprocessor sees one of those identifiers, it replaces it with another value that you’ve defined.

We do this with `#define` (often read “pound define”, or perhaps “hash define”, but rarely, if ever, “octothorpe define”). Here’s an example:
    
    
    [](the-c-preprocessor.html#cb338-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb338-2)
    [](the-c-preprocessor.html#cb338-3)#define HELLO "Hello, world"
    [](the-c-preprocessor.html#cb338-4)#define PI 3.14159
    [](the-c-preprocessor.html#cb338-5)
    [](the-c-preprocessor.html#cb338-6)int main(void)
    [](the-c-preprocessor.html#cb338-7){
    [](the-c-preprocessor.html#cb338-8)    printf("%s, %f\n", HELLO, PI);
    [](the-c-preprocessor.html#cb338-9)}

On lines 3 and 4 we defined a couple macros. Wherever these appear elsewhere in the code (line 8), they’ll be substituted with the defined values.

From the C compiler’s perspective, it’s exactly as if we’d written this, instead:
    
    
    [](the-c-preprocessor.html#cb339-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb339-2)
    [](the-c-preprocessor.html#cb339-3)int main(void)
    [](the-c-preprocessor.html#cb339-4){
    [](the-c-preprocessor.html#cb339-5)    printf("%s, %f\n", "Hello, world", 3.14159);
    [](the-c-preprocessor.html#cb339-6)}

See how `HELLO` was replaced with `"Hello, world"` and `PI` was replaced with `3.14159`? From the compiler’s perspective, it’s just like those values had appeared right there in the code.

Note that the macros don’t have a specific type, _per se_. Really all that happens is they get replaced wholesale with whatever they’re `#define`d as. If the resulting C code is invalid, the compiler will puke.

You can also define a macro with no value:
    
    
    [](the-c-preprocessor.html#cb340-1)#define EXTRA_HAPPY

in that case, the macro exists and is defined, but is defined to be nothing. So anyplace it occurs in the text will just be replaced with nothing. We’ll see a use for this later.

It’s conventional to write macro names in `ALL_CAPS` even though that’s not technically required.

Overall, this gives you a way to define constant values that are effectively global and can be used _any_ place. Even in those places where a `const` variable won’t work, e.g. in `switch` `case`s and fixed array lengths.

That said, the debate rages online whether a typed `const` variable is better than `#define` macro in the general case.

It can also be used to replace or modify keywords, a concept completely foreign to `const`, though this practice should be used sparingly.

## 19.3 Conditional Compilation

It’s possible to get the preprocessor to decide whether or not to present certain blocks of code to the compiler, or just remove them entirely before compilation.

We do that by basically wrapping up the code in conditional blocks, similar to `if`-`else` statements.

### 19.3.1 If Defined, `#ifdef` and `#endif`

First of all, let’s try to compile specific code depending on whether or not a macro is even defined.
    
    
    [](the-c-preprocessor.html#cb341-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb341-2)
    [](the-c-preprocessor.html#cb341-3)#define EXTRA_HAPPY
    [](the-c-preprocessor.html#cb341-4)
    [](the-c-preprocessor.html#cb341-5)int main(void)
    [](the-c-preprocessor.html#cb341-6){
    [](the-c-preprocessor.html#cb341-7)
    [](the-c-preprocessor.html#cb341-8)#ifdef EXTRA_HAPPY
    [](the-c-preprocessor.html#cb341-9)    printf("I'm extra happy!\n");
    [](the-c-preprocessor.html#cb341-10)#endif
    [](the-c-preprocessor.html#cb341-11)
    [](the-c-preprocessor.html#cb341-12)    printf("OK!\n");
    [](the-c-preprocessor.html#cb341-13)}

In that example, we define `EXTRA_HAPPY` (to be nothing, but it _is_ defined), then on line 8 we check to see if it is defined with an `#ifdef` directive. If it is defined, the subsequent code will be included up until the `#endif`.

So because it is defined, the code will be included for compilation and the output will be:
    
    
    [](the-c-preprocessor.html#cb342-1)I'm extra happy!
    [](the-c-preprocessor.html#cb342-2)OK!

If we were to comment out the `#define`, like so:
    
    
    [](the-c-preprocessor.html#cb343-1)//#define EXTRA_HAPPY

then it wouldn’t be defined, and the code wouldn’t be included in compilation. And the output would just be:
    
    
    [](the-c-preprocessor.html#cb344-1)OK!

It’s important to remember that these decisions happen at compile time! The code actually gets compiled or removed depending on the condition. This is in contrast to a standard `if` statement that gets evaluated while the program is running.

### 19.3.2 If Not Defined, `#ifndef`

There’s also the negative sense of “if defined”: “if not defined”, or `#ifndef`. We could change the previous example to output different things based on whether or not something was defined:
    
    
    [](the-c-preprocessor.html#cb345-8)#ifdef EXTRA_HAPPY
    [](the-c-preprocessor.html#cb345-9)    printf("I'm extra happy!\n");
    [](the-c-preprocessor.html#cb345-10)#endif
    [](the-c-preprocessor.html#cb345-11)
    [](the-c-preprocessor.html#cb345-12)#ifndef EXTRA_HAPPY
    [](the-c-preprocessor.html#cb345-13)    printf("I'm just regular\n");
    [](the-c-preprocessor.html#cb345-14)#endif

We’ll see a cleaner way to do that in the next section.

Tying it all back in to header files, we’ve seen how we can cause header files to only be included one time by wrapping them in preprocessor directives like this:
    
    
    [](the-c-preprocessor.html#cb346-1)#ifndef MYHEADER_H  // First line of myheader.h
    [](the-c-preprocessor.html#cb346-2)#define MYHEADER_H
    [](the-c-preprocessor.html#cb346-3)
    [](the-c-preprocessor.html#cb346-4)int x = 12;
    [](the-c-preprocessor.html#cb346-5)
    [](the-c-preprocessor.html#cb346-6)#endif  // Last line of myheader.h

This demonstrates how a macro persists across files and multiple `#include`s. If it’s not yet defined, let’s define it and compile the whole header file.

But the next time it’s included, we see that `MYHEADER_H` _is_ defined, so we don’t send the header file to the compiler—it gets effectively removed.

### 19.3.3 `#else`

But that’s not all we can do! There’s also an `#else` that we can throw in the mix.

Let’s mod the previous example:
    
    
    [](the-c-preprocessor.html#cb347-8)#ifdef EXTRA_HAPPY
    [](the-c-preprocessor.html#cb347-9)    printf("I'm extra happy!\n");
    [](the-c-preprocessor.html#cb347-10)#else
    [](the-c-preprocessor.html#cb347-11)    printf("I'm just regular\n");
    [](the-c-preprocessor.html#cb347-12)#endif

Now if `EXTRA_HAPPY` is not defined, it’ll hit the `#else` clause and print:
    
    
    [](the-c-preprocessor.html#cb348-1)I'm just regular

### 19.3.4 Else-If: `#elifdef`, `#elifndef`

This feature is new in C23!

What if you want something more complex, though? Perhaps you need an if-else cascade structure to get your code built right?

Luckily we have these directives at our disposal. We can use `#elifdef` for “else if defined”:
    
    
    [](the-c-preprocessor.html#cb349-1)#ifdef MODE_1
    [](the-c-preprocessor.html#cb349-2)    printf("This is mode 1\n");
    [](the-c-preprocessor.html#cb349-3)#elifdef MODE_2
    [](the-c-preprocessor.html#cb349-4)    printf("This is mode 2\n");
    [](the-c-preprocessor.html#cb349-5)#elifdef MODE_3
    [](the-c-preprocessor.html#cb349-6)    printf("This is mode 3\n");
    [](the-c-preprocessor.html#cb349-7)#else
    [](the-c-preprocessor.html#cb349-8)    printf("This is some other mode\n");
    [](the-c-preprocessor.html#cb349-9)#endif

On the flipside, you can use `#elifndef` for “else if not defined”.

### 19.3.5 General Conditional: `#if`, `#elif`

This works very much like the `#ifdef` and `#ifndef` directives in that you can also have an `#else` and the whole thing wraps up with `#endif`.

The only difference is that the constant expression after the `#if` must evaluate to true (non-zero) for the code in the `#if` to be compiled. So instead of whether or not something is defined, we want an expression that evaluates to true.
    
    
    [](the-c-preprocessor.html#cb350-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb350-2)
    [](the-c-preprocessor.html#cb350-3)#define HAPPY_FACTOR 1
    [](the-c-preprocessor.html#cb350-4)
    [](the-c-preprocessor.html#cb350-5)int main(void)
    [](the-c-preprocessor.html#cb350-6){
    [](the-c-preprocessor.html#cb350-7)
    [](the-c-preprocessor.html#cb350-8)#if HAPPY_FACTOR == 0
    [](the-c-preprocessor.html#cb350-9)    printf("I'm not happy!\n");
    [](the-c-preprocessor.html#cb350-10)#elif HAPPY_FACTOR == 1
    [](the-c-preprocessor.html#cb350-11)    printf("I'm just regular\n");
    [](the-c-preprocessor.html#cb350-12)#else
    [](the-c-preprocessor.html#cb350-13)    printf("I'm extra happy!\n");
    [](the-c-preprocessor.html#cb350-14)#endif
    [](the-c-preprocessor.html#cb350-15)
    [](the-c-preprocessor.html#cb350-16)    printf("OK!\n");
    [](the-c-preprocessor.html#cb350-17)}

Again, for the unmatched `#if` clauses, the compiler won’t even see those lines. For the above code, after the preprocessor gets finished with it, all the compiler sees is:
    
    
    [](the-c-preprocessor.html#cb351-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb351-2)
    [](the-c-preprocessor.html#cb351-3)int main(void)
    [](the-c-preprocessor.html#cb351-4){
    [](the-c-preprocessor.html#cb351-5)
    [](the-c-preprocessor.html#cb351-6)    printf("I'm just regular\n");
    [](the-c-preprocessor.html#cb351-7)
    [](the-c-preprocessor.html#cb351-8)    printf("OK!\n");
    [](the-c-preprocessor.html#cb351-9)}

One hackish thing this is used for is to comment out large numbers of lines quickly[129](function-specifiers-alignment-specifiersoperators.html#fn129).

If you put an `#if 0` (“if false”) at the front of the block to be commented out and an `#endif` at the end, you can get this effect:
    
    
    [](the-c-preprocessor.html#cb352-1)#if 0
    [](the-c-preprocessor.html#cb352-2)    printf("All this code"); /* is effectively */
    [](the-c-preprocessor.html#cb352-3)    printf("commented out"); // by the #if 0
    [](the-c-preprocessor.html#cb352-4)#endif

What if you’re on a pre-C23 compiler and you don’t have `#elifdef` or `#elifndef` directive support? How can we get the same effect with `#if`? That is, what if I wanted this:
    
    
    [](the-c-preprocessor.html#cb353-1)#ifdef FOO
    [](the-c-preprocessor.html#cb353-2)    x = 2;
    [](the-c-preprocessor.html#cb353-3)#elifdef BAR  // POTENTIAL ERROR: Not supported before C23
    [](the-c-preprocessor.html#cb353-4)    x = 3;
    [](the-c-preprocessor.html#cb353-5)#endif

How could I do it?

Turns out there’s a preprocessor operator called `defined` that we can use with an `#if` statement.

These are equivalent:
    
    
    [](the-c-preprocessor.html#cb354-1)#ifdef FOO
    [](the-c-preprocessor.html#cb354-2)#if defined FOO
    [](the-c-preprocessor.html#cb354-3)#if defined(FOO)   // Parentheses optional

As are these:
    
    
    [](the-c-preprocessor.html#cb355-1)#ifndef FOO
    [](the-c-preprocessor.html#cb355-2)#if !defined FOO
    [](the-c-preprocessor.html#cb355-3)#if !defined(FOO)   // Parentheses optional

Notice how we can use the standard logical NOT operator (`!`) for “not defined”.

So now we’re back in `#if` land and we can use `#elif` with impunity!

This broken code:
    
    
    [](the-c-preprocessor.html#cb356-1)#ifdef FOO
    [](the-c-preprocessor.html#cb356-2)    x = 2;
    [](the-c-preprocessor.html#cb356-3)#elifdef BAR  // POTENTIAL ERROR: Not supported before C23
    [](the-c-preprocessor.html#cb356-4)    x = 3;
    [](the-c-preprocessor.html#cb356-5)#endif

can be replaced with:
    
    
    [](the-c-preprocessor.html#cb357-1)#if defined FOO
    [](the-c-preprocessor.html#cb357-2)    x = 2;
    [](the-c-preprocessor.html#cb357-3)#elif defined BAR
    [](the-c-preprocessor.html#cb357-4)    x = 3;
    [](the-c-preprocessor.html#cb357-5)#endif

### 19.3.6 Losing a Macro: `#undef`

If you’ve defined something but you don’t need it any longer, you can undefine it with `#undef`.
    
    
    [](the-c-preprocessor.html#cb358-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb358-2)
    [](the-c-preprocessor.html#cb358-3)int main(void)
    [](the-c-preprocessor.html#cb358-4){
    [](the-c-preprocessor.html#cb358-5)#define GOATS
    [](the-c-preprocessor.html#cb358-6)
    [](the-c-preprocessor.html#cb358-7)#ifdef GOATS
    [](the-c-preprocessor.html#cb358-8)    printf("Goats detected!\n");  // prints
    [](the-c-preprocessor.html#cb358-9)#endif
    [](the-c-preprocessor.html#cb358-10)
    [](the-c-preprocessor.html#cb358-11)#undef GOATS  // Make GOATS no longer defined
    [](the-c-preprocessor.html#cb358-12)
    [](the-c-preprocessor.html#cb358-13)#ifdef GOATS
    [](the-c-preprocessor.html#cb358-14)    printf("Goats detected, again!\n"); // doesn't print
    [](the-c-preprocessor.html#cb358-15)#endif
    [](the-c-preprocessor.html#cb358-16)}

## 19.4 Built-in Macros

The standard defines a lot of built-in macros that you can test and use for conditional compilation. Let’s look at those here.

### 19.4.1 Mandatory Macros

These are all defined:

Macro | Description  
---|---  
`__DATE__` | The date of compilation—like when you’re compiling this file—in `Mmm dd yyyy` format  
`__TIME__` | The time of compilation in `hh:mm:ss` format  
`__FILE__` | A string containing this file’s name  
`__LINE__` | The line number of the file this macro appears on  
`__func__` | The name of the function this appears in, as a string[130](function-specifiers-alignment-specifiersoperators.html#fn130)  
`__STDC__` | Defined with `1` if this is a standard C compiler  
`__STDC_HOSTED__` | This will be `1` if the compiler is a _hosted implementation_[ 131](function-specifiers-alignment-specifiersoperators.html#fn131), otherwise `0`  
`__STDC_VERSION__` | This version of C, a constant `long int` in the form `yyyymmL`, e.g. `201710L`  
  
Let’s put these together.
    
    
    [](the-c-preprocessor.html#cb359-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb359-2)
    [](the-c-preprocessor.html#cb359-3)int main(void)
    [](the-c-preprocessor.html#cb359-4){
    [](the-c-preprocessor.html#cb359-5)    printf("This function: %s\n", __func__);
    [](the-c-preprocessor.html#cb359-6)    printf("This file: %s\n", __FILE__);
    [](the-c-preprocessor.html#cb359-7)    printf("This line: %d\n", __LINE__);
    [](the-c-preprocessor.html#cb359-8)    printf("Compiled on: %s %s\n", __DATE__, __TIME__);
    [](the-c-preprocessor.html#cb359-9)    printf("C Version: %ld\n", __STDC_VERSION__);
    [](the-c-preprocessor.html#cb359-10)}

The output on my system is:
    
    
    [](the-c-preprocessor.html#cb360-1)This function: main
    [](the-c-preprocessor.html#cb360-2)This file: foo.c
    [](the-c-preprocessor.html#cb360-3)This line: 7
    [](the-c-preprocessor.html#cb360-4)Compiled on: Nov 23 2020 17:16:27
    [](the-c-preprocessor.html#cb360-5)C Version: 201710

`__FILE__`, `__func__` and `__LINE__` are particularly useful to report error conditions in messages to developers. The `assert()` macro in `<assert.h>` uses these to call out where in the code the assertion failed.

#### 19.4.1.1 `__STDC_VERSION__`s

In case you’re wondering, here are the version numbers for different major releases of the C Language Spec:

Release | ISO/IEC version | `__STDC_VERSION__`  
---|---|---  
C89 | ISO/IEC 9899:1990 | undefined  
**C89** | ISO/IEC 9899:1990/Amd.1:1995 | `199409L`  
**C99** | ISO/IEC 9899:1999 | `199901L`  
**C11** | ISO/IEC 9899:2011/Amd.1:2012 | `201112L`  
  
Note the macro did not exist originally in C89.

Also note that the plan is that the version numbers will strictly increase, so you could always check for, say, “at least C99” with:
    
    
    [](the-c-preprocessor.html#cb361-1)#if __STDC_VERSION__ >= 1999901L

### 19.4.2 Optional Macros

Your implementation might define these, as well. Or it might not.

Macro | Description  
---|---  
`__STDC_ISO_10646__` | If defined, `wchar_t` holds Unicode values, otherwise something else  
`__STDC_MB_MIGHT_NEQ_WC__` | A `1` indicates that the values in multibyte characters might not map equally to values in wide characters  
`__STDC_UTF_16__` | A `1` indicates that the system uses UTF-16 encoding in type `char16_t`  
`__STDC_UTF_32__` | A `1` indicates that the system uses UTF-32 encoding in type `char32_t`  
`__STDC_ANALYZABLE__` | A `1` indicates the code is analyzable[132](function-specifiers-alignment-specifiersoperators.html#fn132)  
`__STDC_IEC_559__` | `1` if IEEE-754 (aka IEC 60559) floating point is supported  
`__STDC_IEC_559_COMPLEX__` | `1` if IEC 60559 complex floating point is supported  
`__STDC_LIB_EXT1__` | `1` if this implementation supports a variety of “safe” alternate standard library functions (they have `_s` suffixes on the name)  
`__STDC_NO_ATOMICS__` | `1` if this implementation does **not** support `_Atomic` or `<stdatomic.h>`  
`__STDC_NO_COMPLEX__` | `1` if this implementation does **not** support complex types or `<complex.h>`  
`__STDC_NO_THREADS__` | `1` if this implementation does **not** support `<threads.h>`  
`__STDC_NO_VLA__` | `1` if this implementation does **not** support variable-length arrays  
  
## 19.5 Macros with Arguments

Macros are more powerful than simple substitution, though. You can set them up to take arguments that are substituted in, as well.

A question often arises for when to use parameterized macros versus functions. Short answer: use functions. But you’ll see lots of macros in the wild and in the standard library. People tend to use them for short, mathy things, and also for features that might change from platform to platform. You can define different keywords for one platform or another.

### 19.5.1 Macros with One Argument

Let’s start with a simple one that squares a number:
    
    
    [](the-c-preprocessor.html#cb362-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb362-2)
    [](the-c-preprocessor.html#cb362-3)#define SQR(x) x * x  // Not quite right, but bear with me
    [](the-c-preprocessor.html#cb362-4)
    [](the-c-preprocessor.html#cb362-5)int main(void)
    [](the-c-preprocessor.html#cb362-6){
    [](the-c-preprocessor.html#cb362-7)    printf("%d\n", SQR(12));  // 144
    [](the-c-preprocessor.html#cb362-8)}

What that’s saying is “everywhere you see `SQR` with some value, replace it with that value times itself”.

So line 7 will be changed to:
    
    
    [](the-c-preprocessor.html#cb363-7)    printf("%d\n", 12 * 12);  // 144

which C comfortably converts to 144.

But we’ve made an elementary error in that macro, one that we need to avoid.

Let’s check it out. What if we wanted to compute `SQR(3 + 4)`? Well, \\(3+4=7\\), so we must want to compute \\(7^2=49\\). That’s it; `49`—final answer.

Let’s drop it in our code and see that we get… 19?
    
    
    [](the-c-preprocessor.html#cb364-7)    printf("%d\n", SQR(3 + 4));  // 19!!??

What happened?

If we follow the macro expansion, we get
    
    
    [](the-c-preprocessor.html#cb365-7)    printf("%d\n", 3 + 4 * 3 + 4);  // 19!

Oops! Since multiplication takes precedence, we do the \\(4\times3=12\\) first, and get \\(3+12+4=19\\). Not what we were after.

So we have to fix this to make it right.

**This is so common that you should automatically do it every time you make a parameterized math macro!**

The fix is easy: just add some parentheses!
    
    
    [](the-c-preprocessor.html#cb366-3)#define SQR(x) (x) * (x)   // Better... but still not quite good enough!

And now our macro expands to:
    
    
    [](the-c-preprocessor.html#cb367-7)    printf("%d\n", (3 + 4) * (3 + 4));  // 49! Woo hoo!

But we actually still have the same problem which might manifest if we have a higher-precedence operator than multiply (`*`) nearby.

So the safe, proper way to put the macro together is to wrap the whole thing in additional parentheses, like so:
    
    
    [](the-c-preprocessor.html#cb368-3)#define SQR(x) ((x) * (x))   // Good!

Just make it a habit to do that when you make a math macro and you can’t go wrong.

### 19.5.2 Macros with More than One Argument

You can stack these things up as much as you want:
    
    
    [](the-c-preprocessor.html#cb369-1)#define TRIANGLE_AREA(w, h) (0.5 * (w) * (h))

Let’s do some macros that solve for \\(x\\) using the quadratic formula. Just in case you don’t have it on the top of your head, it says for equations of the form:

\\(ax^2+bx+c=0\\)

you can solve for \\(x\\) with the quadratic formula:

\\(x=\displaystyle\frac{-b\pm\sqrt{b^2-4ac}}{2a}\\)

Which is crazy. Also notice the plus-or-minus (\\(\pm\\)) in there, indicating that there are actually two solutions.

So let’s make macros for both:
    
    
    [](the-c-preprocessor.html#cb370-1)#define QUADP(a, b, c) ((-(b) + sqrt((b) * (b) - 4 * (a) * (c))) / (2 * (a)))
    [](the-c-preprocessor.html#cb370-2)#define QUADM(a, b, c) ((-(b) - sqrt((b) * (b) - 4 * (a) * (c))) / (2 * (a)))

So that gets us some math. But let’s define one more that we can use as arguments to `printf()` to print both answers.
    
    
    [](the-c-preprocessor.html#cb371-1)//          macro              replacement
    [](the-c-preprocessor.html#cb371-2)//      |-----------| |----------------------------|
    [](the-c-preprocessor.html#cb371-3)#define QUAD(a, b, c) QUADP(a, b, c), QUADM(a, b, c)

That’s just a couple values separated by a comma—and we can use that as a “combined” argument of sorts to `printf()` like this:
    
    
    [](the-c-preprocessor.html#cb372-1)printf("x = %f or x = %f\n", QUAD(2, 10, 5));

Let’s put it together into some code:
    
    
    [](the-c-preprocessor.html#cb373-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb373-2)#include <math.h>  // For sqrt()
    [](the-c-preprocessor.html#cb373-3)
    [](the-c-preprocessor.html#cb373-4)#define QUADP(a, b, c) ((-(b) + sqrt((b) * (b) - 4 * (a) * (c))) / (2 * (a)))
    [](the-c-preprocessor.html#cb373-5)#define QUADM(a, b, c) ((-(b) - sqrt((b) * (b) - 4 * (a) * (c))) / (2 * (a)))
    [](the-c-preprocessor.html#cb373-6)#define QUAD(a, b, c) QUADP(a, b, c), QUADM(a, b, c)
    [](the-c-preprocessor.html#cb373-7)
    [](the-c-preprocessor.html#cb373-8)int main(void)
    [](the-c-preprocessor.html#cb373-9){
    [](the-c-preprocessor.html#cb373-10)    printf("2*x^2 + 10*x + 5 = 0\n");
    [](the-c-preprocessor.html#cb373-11)    printf("x = %f or x = %f\n", QUAD(2, 10, 5));
    [](the-c-preprocessor.html#cb373-12)}

And this gives us the output:
    
    
    [](the-c-preprocessor.html#cb374-1)2*x^2 + 10*x + 5 = 0
    [](the-c-preprocessor.html#cb374-2)x = -0.563508 or x = -4.436492

Plugging in either of those values gives us roughly zero (a bit off because the numbers aren’t exact):

\\(2\times-0.563508^2+10\times-0.563508+5\approx0.000003\\)

### 19.5.3 Macros with Variable Arguments

There’s also a way to have a variable number of arguments passed to a macro, using ellipses (`...`) after the known, named arguments. When the macro is expanded, all of the extra arguments will be in a comma-separated list in the `__VA_ARGS__` macro, and can be replaced from there:
    
    
    [](the-c-preprocessor.html#cb375-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb375-2)
    [](the-c-preprocessor.html#cb375-3)// Combine the first two arguments to a single number,
    [](the-c-preprocessor.html#cb375-4)// then have a commalist of the rest of them:
    [](the-c-preprocessor.html#cb375-5)
    [](the-c-preprocessor.html#cb375-6)#define X(a, b, ...) (10*(a) + 20*(b)), __VA_ARGS__
    [](the-c-preprocessor.html#cb375-7)
    [](the-c-preprocessor.html#cb375-8)int main(void)
    [](the-c-preprocessor.html#cb375-9){
    [](the-c-preprocessor.html#cb375-10)    printf("%d %f %s %d\n", X(5, 4, 3.14, "Hi!", 12));
    [](the-c-preprocessor.html#cb375-11)}

The substitution that takes place on line 10 would be:
    
    
    [](the-c-preprocessor.html#cb376-10)    printf("%d %f %s %d\n", (10*(5) + 20*(4)), 3.14, "Hi!", 12);

for output:
    
    
    [](the-c-preprocessor.html#cb377-1)130 3.140000 Hi! 12

You can also “stringify” `__VA_ARGS__` by putting a `#` in front of it:
    
    
    [](the-c-preprocessor.html#cb378-1)#define X(...) #__VA_ARGS__
    [](the-c-preprocessor.html#cb378-2)
    [](the-c-preprocessor.html#cb378-3)printf("%s\n", X(1,2,3));  // Prints "1, 2, 3"

### 19.5.4 Stringification

Already mentioned, just above, you can turn any argument into a string by preceding it with a `#` in the replacement text.

For example, we could print anything as a string with this macro and `printf()`:
    
    
    [](the-c-preprocessor.html#cb379-1)#define STR(x) #x
    [](the-c-preprocessor.html#cb379-2)
    [](the-c-preprocessor.html#cb379-3)printf("%s\n", STR(3.14159));

In that case, the substitution leads to:
    
    
    [](the-c-preprocessor.html#cb380-1)printf("%s\n", "3.14159");

Let’s see if we can use this to greater effect so that we can pass any `int` variable name into a macro, and have it print out it’s name and value.
    
    
    [](the-c-preprocessor.html#cb381-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb381-2)
    [](the-c-preprocessor.html#cb381-3)#define PRINT_INT_VAL(x) printf("%s = %d\n", #x, x)
    [](the-c-preprocessor.html#cb381-4)
    [](the-c-preprocessor.html#cb381-5)int main(void)
    [](the-c-preprocessor.html#cb381-6){
    [](the-c-preprocessor.html#cb381-7)    int a = 5;
    [](the-c-preprocessor.html#cb381-8)
    [](the-c-preprocessor.html#cb381-9)    PRINT_INT_VAL(a);  // prints "a = 5"
    [](the-c-preprocessor.html#cb381-10)}

On line 9, we get the following macro replacement:
    
    
    [](the-c-preprocessor.html#cb382-9)    printf("%s = %d\n", "a", 5);

### 19.5.5 Concatenation

We can concatenate two arguments together with `##`, as well. Fun times!
    
    
    [](the-c-preprocessor.html#cb383-1)#define CAT(a, b) a ## b
    [](the-c-preprocessor.html#cb383-2)
    [](the-c-preprocessor.html#cb383-3)printf("%f\n", CAT(3.14, 1592));   // 3.141592

## 19.6 Multiline Macros

It’s possible to continue a macro to multiple lines if you escape the newline with a backslash (`\`).

Let’s write a multiline macro that prints numbers from `0` to the product of the two arguments passed in.
    
    
    [](the-c-preprocessor.html#cb384-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb384-2)
    [](the-c-preprocessor.html#cb384-3)#define PRINT_NUMS_TO_PRODUCT(a, b) do { \
    [](the-c-preprocessor.html#cb384-4)    int product = (a) * (b); \
    [](the-c-preprocessor.html#cb384-5)    for (int i = 0; i < product; i++) { \
    [](the-c-preprocessor.html#cb384-6)        printf("%d\n", i); \
    [](the-c-preprocessor.html#cb384-7)    } \
    [](the-c-preprocessor.html#cb384-8)} while(0)
    [](the-c-preprocessor.html#cb384-9)
    [](the-c-preprocessor.html#cb384-10)int main(void)
    [](the-c-preprocessor.html#cb384-11){
    [](the-c-preprocessor.html#cb384-12)    PRINT_NUMS_TO_PRODUCT(2, 4);  // Outputs numbers from 0 to 7
    [](the-c-preprocessor.html#cb384-13)}

A couple things to note there:

  * Escapes at the end of every line except the last one to indicate that the macro continues.
  * The whole thing is wrapped in a `do`-`while(0)` loop with squirrley braces.



The latter point might be a little weird, but it’s all about absorbing the trailing `;` the coder drops after the macro.

At first I thought that just using squirrely braces would be enough, but there’s a case where it fails if the coder puts a semicolon after the macro. Here’s that case:
    
    
    [](the-c-preprocessor.html#cb385-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb385-2)
    [](the-c-preprocessor.html#cb385-3)#define FOO(x) { (x)++; }
    [](the-c-preprocessor.html#cb385-4)
    [](the-c-preprocessor.html#cb385-5)int main(void)
    [](the-c-preprocessor.html#cb385-6){
    [](the-c-preprocessor.html#cb385-7)    int i = 0;
    [](the-c-preprocessor.html#cb385-8)
    [](the-c-preprocessor.html#cb385-9)    if (i == 0)
    [](the-c-preprocessor.html#cb385-10)        FOO(i);
    [](the-c-preprocessor.html#cb385-11)    else
    [](the-c-preprocessor.html#cb385-12)        printf(":-(\n");
    [](the-c-preprocessor.html#cb385-13)
    [](the-c-preprocessor.html#cb385-14)    printf("%d\n", i);
    [](the-c-preprocessor.html#cb385-15)}

Looks simple enough, but it won’t build without a syntax error:
    
    
    [](the-c-preprocessor.html#cb386-1)foo.c:11:5: error: ‘else’ without a previous ‘if’  

Do you see it?

Let’s look at the expansion:
    
    
    [](the-c-preprocessor.html#cb387-1)
    [](the-c-preprocessor.html#cb387-2)    if (i == 0) {
    [](the-c-preprocessor.html#cb387-3)        (i)++;
    [](the-c-preprocessor.html#cb387-4)    };             // <-- Trouble with a capital-T!
    [](the-c-preprocessor.html#cb387-5)
    [](the-c-preprocessor.html#cb387-6)    else
    [](the-c-preprocessor.html#cb387-7)        printf(":-(\n");

The `;` puts an end to the `if` statement, so the `else` is just floating out there illegally[133](function-specifiers-alignment-specifiersoperators.html#fn133).

So wrap that multiline macro with a `do`-`while(0)`.

## 19.7 Example: An Assert Macro

Adding asserts to your code is a good way to catch conditions that you think shouldn’t happen. C provides `assert()` functionality. It checks a condition, and if it’s false, the program bombs out telling you the file and line number on which the assertion failed.

But this is wanting.

  1. First of all, you can’t specify an additional message with the assert.
  2. Secondly, there’s no easy on-off switch for all the asserts.



We can address the first with macros.

Basically, when I have this code:
    
    
    [](the-c-preprocessor.html#cb388-1)ASSERT(x < 20, "x must be under 20");

I want something like this to happen (assuming the `ASSERT()` is on line 220 of `foo.c`):
    
    
    [](the-c-preprocessor.html#cb389-1)if (!(x < 20)) {
    [](the-c-preprocessor.html#cb389-2)    fprintf(stderr, "foo.c:220: assertion x < 20 failed: ");
    [](the-c-preprocessor.html#cb389-3)    fprintf(stderr, "x must be under 20\n");
    [](the-c-preprocessor.html#cb389-4)    exit(1);
    [](the-c-preprocessor.html#cb389-5)}

We can get the filename out of the `__FILE__` macro, and the line number from `__LINE__`. The message is already a string, but `x < 20` is not, so we’ll have to stringify it with `#`. We can make a multiline macro by using backslash escapes at the end of the line.
    
    
    [](the-c-preprocessor.html#cb390-1)#define ASSERT(c, m) \
    [](the-c-preprocessor.html#cb390-2)do { \
    [](the-c-preprocessor.html#cb390-3)    if (!(c)) { \
    [](the-c-preprocessor.html#cb390-4)        fprintf(stderr, __FILE__ ":%d: assertion %s failed: %s\n", \
    [](the-c-preprocessor.html#cb390-5)                        __LINE__, #c, m); \
    [](the-c-preprocessor.html#cb390-6)        exit(1); \
    [](the-c-preprocessor.html#cb390-7)    } \
    [](the-c-preprocessor.html#cb390-8)} while(0)

(It looks a little weird with `__FILE__` out front like that, but remember it is a string literal, and string literals next to each other are automagically concatenated. `__LINE__` on the other hand, it’s just an `int`.)

And that works! If I run this:
    
    
    [](the-c-preprocessor.html#cb391-1)int x = 30;
    [](the-c-preprocessor.html#cb391-2)
    [](the-c-preprocessor.html#cb391-3)ASSERT(x < 20, "x must be under 20");

I get this output:
    
    
    foo.c:23: assertion x < 20 failed: x must be under 20

Very nice!

The only thing left is a way to turn it on and off, and we could do that with conditional compilation.

Here’s the complete example:
    
    
    [](the-c-preprocessor.html#cb393-1)#include <stdio.h>
    [](the-c-preprocessor.html#cb393-2)#include <stdlib.h>
    [](the-c-preprocessor.html#cb393-3)
    [](the-c-preprocessor.html#cb393-4)#define ASSERT_ENABLED 1
    [](the-c-preprocessor.html#cb393-5)
    [](the-c-preprocessor.html#cb393-6)#if ASSERT_ENABLED
    [](the-c-preprocessor.html#cb393-7)#define ASSERT(c, m) \
    [](the-c-preprocessor.html#cb393-8)do { \
    [](the-c-preprocessor.html#cb393-9)    if (!(c)) { \
    [](the-c-preprocessor.html#cb393-10)        fprintf(stderr, __FILE__ ":%d: assertion %s failed: %s\n", \
    [](the-c-preprocessor.html#cb393-11)                        __LINE__, #c, m); \
    [](the-c-preprocessor.html#cb393-12)        exit(1); \
    [](the-c-preprocessor.html#cb393-13)    } \
    [](the-c-preprocessor.html#cb393-14)} while(0)
    [](the-c-preprocessor.html#cb393-15)#else
    [](the-c-preprocessor.html#cb393-16)#define ASSERT(c, m)  // Empty macro if not enabled
    [](the-c-preprocessor.html#cb393-17)#endif
    [](the-c-preprocessor.html#cb393-18)
    [](the-c-preprocessor.html#cb393-19)int main(void)
    [](the-c-preprocessor.html#cb393-20){
    [](the-c-preprocessor.html#cb393-21)    int x = 30;
    [](the-c-preprocessor.html#cb393-22)
    [](the-c-preprocessor.html#cb393-23)    ASSERT(x < 20, "x must be under 20");
    [](the-c-preprocessor.html#cb393-24)}

This has the output:
    
    
    [](the-c-preprocessor.html#cb394-1)foo.c:23: assertion x < 20 failed: x must be under 20

## 19.8 The `#error` Directive

This directive causes the compiler to error out as soon as it sees it.

Commonly, this is used inside a conditional to prevent compilation unless some prerequisites are met:
    
    
    [](the-c-preprocessor.html#cb395-1)#ifndef __STDC_IEC_559__
    [](the-c-preprocessor.html#cb395-2)    #error I really need IEEE-754 floating point to compile. Sorry!
    [](the-c-preprocessor.html#cb395-3)#endif

Some compilers have a non-standard complementary `#warning` directive that will output a warning but not stop compilation, but this is not in the C11 spec.

## 19.9 The `#embed` Directive

New in C23!

And currently not yet working with any of my compilers, so take this section with a grain of salt!

The gist of this is that you can include bytes of a file as integer constants as if you’d typed them in.

For example, if you have a binary file named `foo.bin` that contains four bytes with decimal values 11, 22, 33, and 44, and you do this:
    
    
    [](the-c-preprocessor.html#cb396-1)int a[] = {
    [](the-c-preprocessor.html#cb396-2)#embed "foo.bin"
    [](the-c-preprocessor.html#cb396-3)};

It’ll be just as if you’d typed this:
    
    
    [](the-c-preprocessor.html#cb397-1)int a[] = {11,22,33,44};

This is a really powerful way to initialize an array with binary data without needing to convert it all to code first—the preprocessor does it for you!

A more typical use case might be a file containing a small image to be displayed that you don’t want to load at runtime.

Here’s another example:
    
    
    [](the-c-preprocessor.html#cb398-1)int a[] = {
    [](the-c-preprocessor.html#cb398-2)#embed <foo.bin>
    [](the-c-preprocessor.html#cb398-3)};

If you use angle brackets, the preprocessor looks in a series of implementation-defined places to locate the file, just like `#include` would do. If you use double quotes and the resource is not found, the compiler will try it as if you’d used angle brackets in a last desperate attempt to find the file.

`#embed` works like `#include` in that it effectively pastes values in before the compiler sees them. This means you can use it in all kinds of places:
    
    
    return
    #embed "somevalue.dat"
    ;

or
    
    
    int x =
    #embed "xvalue.dat"
    ;

Now—are these always bytes? Meaning they’ll have values from 0 to 255, inclusive? The answer is definitely by default “yes”, except when it is “no”.

Technically, the elements will be `CHAR_BIT` bits wide. And this is very likely 8 on your system, so you’d get that 0-255 range in your values. (They’ll always be non-negative.)

Also, it’s possible that an implementation might allow this to be overridden in some way, e.g. on the command line or with parameters.

The size of the file in bits must be a multiple of the element size. That is, if each element is 8 bits, the file size (in bits) must be a multiple of 8. In regular everyday usage, this is a confusing way of saying that each file needs to be an integer number of bytes… which of course it is. Honestly, I’m not even sure why I bothered with this paragraph. Read the spec if you’re really that curious.

### 19.9.1 `#embed` Parameters

There are all kinds of parameters you can specify to the `#embed` directive. Here’s an example with the yet-unintroduced `limit()` parameter:
    
    
    [](the-c-preprocessor.html#cb401-1)int a[] = {
    [](the-c-preprocessor.html#cb401-2)#embed "/dev/random" limit(5)
    [](the-c-preprocessor.html#cb401-3)};

But what if you already have `limit` defined somewhere else? Luckily you can put `__` around the keyword and it will work the same way:
    
    
    [](the-c-preprocessor.html#cb402-1)int a[] = {
    [](the-c-preprocessor.html#cb402-2)#embed "/dev/random" __limit__(5)
    [](the-c-preprocessor.html#cb402-3)};

Now… what’s this `limit` thing?

### 19.9.2 The `limit()` Parameter

You can specify a limit on the number of elements to embed with this parameter.

This is a maximum value, not an absolute value. If the file that’s embedded is shorter than the specified limit, only that many bytes will be imported.

The `/dev/random` example above is an example of the motivation for this—in Unix, that’s a _character device file_ that will return an infinite stream of pretty-random numbers.

Embedding an infinite number of bytes is hard on your RAM, so the `limit` parameter gives you a way to stop after a certain number.

Finally, you are allowed to use `#define` macros in your `limit`, in case you were curious.

### 19.9.3 The `if_empty` Parameter

This parameter defines what the embed result should be if the file exists but contains no data. Let’s say that the file `foo.dat` contains a single byte with the value 123. If we do this:
    
    
    [](the-c-preprocessor.html#cb403-1)int x = 
    [](the-c-preprocessor.html#cb403-2)#embed "foo.dat" if_empty(999)
    [](the-c-preprocessor.html#cb403-3);

we’ll get:
    
    
    [](the-c-preprocessor.html#cb404-1)int x = 123;   // When foo.dat contains a 123 byte

But what if the file `foo.dat` is zero bytes long (i.e. contains no data and is empty)? If that’s the case, it would expand to:
    
    
    [](the-c-preprocessor.html#cb405-1)int x = 999;   // When foo.dat is empty

Notably if the `limit` is set to `0`, then the `if_empty` will always be substituted. That is, a zero limit effectively means the file is empty.

This will always emit `x = 999` no matter what’s in `foo.dat`:
    
    
    [](the-c-preprocessor.html#cb406-1)int x = 
    [](the-c-preprocessor.html#cb406-2)#embed "foo.dat" limit(0) if_empty(999)
    [](the-c-preprocessor.html#cb406-3);

### 19.9.4 The `prefix()` and `suffix()` Parameters

This is a way to prepend some data on the embed.

Note that these only affect non-empty data! If the file is empty, neither `prefix` nor `suffix` has any effect.

Here’s an example where we embed three random numbers, but prefix the numbers with `11,` and suffix them with `,99`:
    
    
    [](the-c-preprocessor.html#cb407-1)int x[] = {
    [](the-c-preprocessor.html#cb407-2)#embed "/dev/urandom" limit(3) prefix(11,) suffix(,99)
    [](the-c-preprocessor.html#cb407-3)};

Example result:
    
    
    [](the-c-preprocessor.html#cb408-1)int x[] = {11,135,116,220,99};

There’s no requirement that you use both `prefix` and `suffix`. You can use both, one, the other, or neither.

We can make use of the characteristic that these are only applied to non-empty files to neat effect, as shown in the following example shamelessly stolen from the spec.

Let’s say we have a file `foo.dat` that has some data it in. And we want to use this to initialize an array, and then we want a suffix on the array that is a zero element.

No problem, right?
    
    
    [](the-c-preprocessor.html#cb409-1)int x[] = {
    [](the-c-preprocessor.html#cb409-2)#embed "foo.dat" suffix(,0)
    [](the-c-preprocessor.html#cb409-3)};

If `foo.dat` has 11, 22, and 33 in it, we’d get:
    
    
    [](the-c-preprocessor.html#cb410-1)int x[] = {11,22,33,0};

But wait! What if `foo.dat` is empty? Then we get:
    
    
    [](the-c-preprocessor.html#cb411-1)int x[] = {};

and that’s not good.

But we can fix it like this:
    
    
    [](the-c-preprocessor.html#cb412-1)int x[] = {
    [](the-c-preprocessor.html#cb412-2)#embed "foo.dat" suffix(,)
    [](the-c-preprocessor.html#cb412-3)    0
    [](the-c-preprocessor.html#cb412-4)};

Since the `suffix` parameter is omitted if the file is empty, this would just turn into:
    
    
    [](the-c-preprocessor.html#cb413-1)int x[] = {0};

which is fine.

### 19.9.5 The `__has_embed()` Identifier

This is a great way to test to see if a particular file is available to be embedded, and also whether or not it’s empty.

You use it with the `#if` directive.

Here’s a chunk of code that will get 5 random numbers from the random number generator character device. If that doesn’t exist, it tries to get them from a file `myrandoms.dat`. If that doesn’t exist, it uses some hard-coded values:
    
    
    [](the-c-preprocessor.html#cb414-1)    int random_nums[] = {
    [](the-c-preprocessor.html#cb414-2)#if __has_embed("/dev/urandom")
    [](the-c-preprocessor.html#cb414-3)    #embed "/dev/urandom" limit(5)
    [](the-c-preprocessor.html#cb414-4)#elif __has_embed("myrandoms.dat")
    [](the-c-preprocessor.html#cb414-5)    #embed "myrandoms.dat" limit(5)
    [](the-c-preprocessor.html#cb414-6)#else
    [](the-c-preprocessor.html#cb414-7)    140,178,92,167,120
    [](the-c-preprocessor.html#cb414-8)#endif
    [](the-c-preprocessor.html#cb414-9)    };

Technically, the `__has_embed()` identifier resolves to one of three values:

`__has_embed()` Result | Description  
---|---  
`__STDC_EMBED_NOT_FOUND__` | If the file isn’t found.  
`__STDC_EMBED_FOUND__` | If the file is found and is not empty.  
`__STDC_EMBED_EMPTY` | If the file is found and is empty.  
  
I have good reason to believe that `__STDC_EMBED_NOT_FOUND__` is `0` and the others aren’t zero (because it’s implied in the proposal and it makes logical sense), but I’m having trouble finding that in this version of the draft spec.

TODO

### 19.9.6 Other Parameters

A compiler implementation can define other embed parameters all it wants—look for these non-standard parameters in your compiler’s documentation.

For instance:
    
    
    [](the-c-preprocessor.html#cb415-1)#embed "foo.bin" limit(12) frotz(lamp)

These might commonly have a prefix on them to help with namespacing:
    
    
    [](the-c-preprocessor.html#cb416-1)#embed "foo.bin" limit(12) fmc::frotz(lamp)

It might be sensible to try to detect if these are available before you use them, and luckily we can use `__has_embed` to help us here.

Normally, `__has_embed()` will just tell us if the file is there or not. But—and here’s the fun bit—it will also return false if any additional parameters are also not supported!

So if we give it a file that we _know_ exists as well as a parameter that we want to test for the existence of, it will effectively tell us if that parameter is supported.

What file _always_ exists, though? Turns out we can use the `__FILE__` macro, which expands to the name of the source file that references it! That file _must_ exist, or something is seriously wrong in the chicken-and-egg department.

Let’s test that `frotz` parameter to see if we can use it:
    
    
    [](the-c-preprocessor.html#cb417-1)#if __has_embed(__FILE__ fmc::frotz(lamp))
    [](the-c-preprocessor.html#cb417-2)    puts("fmc::frotz(lamp) is supported!");
    [](the-c-preprocessor.html#cb417-3)#else
    [](the-c-preprocessor.html#cb417-4)    puts("fmc::frotz(lamp) is NOT supported!");
    [](the-c-preprocessor.html#cb417-5)#endif

### 19.9.7 Embedding Multi-Byte Values

What about getting some `int`s in there instead of individual bytes? What about multi-byte values in the embedded file?

This is not something supported by the C23 standard, but there could be implementation extensions defined for it in the future.

## 19.10 The `#pragma` Directive

This is one funky directive, short for “pragmatic”. You can use it to do… well, anything your compiler supports you doing with it.

Basically the only time you’re going to add this to your code is if some documentation tells you to do so.

### 19.10.1 Non-Standard Pragmas

Here’s one non-standard example of using `#pragma` to cause the compiler to execute a `for` loop in parallel with multiple threads (if the compiler supports the [OpenMP](https://www.openmp.org/)[134](function-specifiers-alignment-specifiersoperators.html#fn134) extension):
    
    
    [](the-c-preprocessor.html#cb418-1)#pragma omp parallel for
    [](the-c-preprocessor.html#cb418-2)for (int i = 0; i < 10; i++) { ... }

There are all kinds of `#pragma` directives documented across all four corners of the globe.

All unrecognized `#pragma`s are ignored by the compiler.

### 19.10.2 Standard Pragmas

There are also a few standard ones, and these start with `STDC`, and follow the same form:
    
    
    [](the-c-preprocessor.html#cb419-1)#pragma STDC pragma_name on-off

The `on-off` portion can be either `ON`, `OFF`, or `DEFAULT`.

And the `pragma_name` can be one of these:

Pragma Name | Description  
---|---  
`FP_CONTRACT` | Allow floating point expressions to be contracted into a single operation to avoid rounding errors that might occur from multiple operations.  
`FENV_ACCESS` | Set to `ON` if you plan to access the floating point status flags. If `OFF`, the compiler might perform optimizations that cause the values in the flags to be inconsistent or invalid.  
`CX_LIMITED_RANGE` | Set to `ON` to allow the compiler to skip overflow checks when performing complex arithmetic. Defaults to `OFF`.  
  
For example:
    
    
    [](the-c-preprocessor.html#cb420-1)#pragma STDC FP_CONTRACT OFF
    [](the-c-preprocessor.html#cb420-2)#pragma STDC CX_LIMITED_RANGE ON

As for `CX_LIMITED_RANGE`, the spec points out:

> The purpose of the pragma is to allow the implementation to use the formulas:
> 
> \\((x+iy)\times(u+iv) = (xu-yv)+i(yu+xv)\\)
> 
> \\((x+iy)/(u+iv) = [(xu+yv)+i(yu-xv)]/(u^2+v^2)\\)
> 
> \\(|x+iy|=\sqrt{x^2+y^2}\\)
> 
> where the programmer can determine they are safe.

### 19.10.3 `_Pragma` Operator

This is another way to declare a pragma that you could use in a macro.

These are equivalent:
    
    
    [](the-c-preprocessor.html#cb421-1)#pragma "Unnecessary" quotes
    [](the-c-preprocessor.html#cb421-2)_Pragma("\"Unnecessary\" quotes")

This can be used in a macro, if need be:
    
    
    [](the-c-preprocessor.html#cb422-1)#define PRAGMA(x) _Pragma(#x)

## 19.11 The `#line` Directive

This allows you to override the values for `__LINE__` and `__FILE__`. If you want.

I’ve never wanted to do this, but in K&R2, they write:

> For the benefit of other preprocessors that generate C programs […]

So maybe there’s that.

To override the line number to, say 300:
    
    
    [](the-c-preprocessor.html#cb423-1)#line 300

and `__LINE__` will keep counting up from there.

To override the line number and the filename:
    
    
    [](the-c-preprocessor.html#cb424-1)#line 300 "newfilename"

## 19.12 The Null Directive

A `#` on a line by itself is ignored by the preprocessor. Now, to be entirely honest, I don’t know what the use case is for this.

I’ve seen examples like this:
    
    
    [](the-c-preprocessor.html#cb425-1)#ifdef FOO
    [](the-c-preprocessor.html#cb425-2)    #
    [](the-c-preprocessor.html#cb425-3)#else
    [](the-c-preprocessor.html#cb425-4)    printf("Something");
    [](the-c-preprocessor.html#cb425-5)#endif

which is just cosmetic; the line with the solitary `#` can be deleted with no ill effect.

Or maybe for cosmetic consistency, like this:
    
    
    [](the-c-preprocessor.html#cb426-1)#
    [](the-c-preprocessor.html#cb426-2)#ifdef FOO
    [](the-c-preprocessor.html#cb426-3)    x = 2;
    [](the-c-preprocessor.html#cb426-4)#endif
    [](the-c-preprocessor.html#cb426-5)#
    [](the-c-preprocessor.html#cb426-6)#if BAR == 17
    [](the-c-preprocessor.html#cb426-7)    x = 12;
    [](the-c-preprocessor.html#cb426-8)#endif
    [](the-c-preprocessor.html#cb426-9)#

But, with respect to cosmetics, that’s just ugly.

Another post mentions elimination of comments—that in GCC, a comment after a `#` will not be seen by the compiler. Which I don’t doubt, but the specification doesn’t seem to say this is standard behavior.

My searches for rationale aren’t bearing much fruit. So I’m going to just say this is some good ol’ fashioned C esoterica.

* * *

[Prev](the-outside-environment.html) | [Contents](index.html) | [Next](structs-ii-more-fun-with-structs.html)

---

[Prev](the-c-preprocessor.html) | [Contents](index.html) | [Next](characters-and-strings-ii.html)

* * *

# 20 `struct`s II: More Fun with `struct`s

Turns out there’s a lot more you can do with `struct`s than we’ve talked about, but it’s just a big pile of miscellaneous things. So we’ll throw them in this chapter.

If you’re good with `struct` basics, you can round out your knowledge here.

## 20.1 Initializers of Nested `struct`s and Arrays

Remember how you could [initialize structure members along these lines](structs.html#struct-initializers)?
    
    
    [](structs-ii-more-fun-with-structs.html#cb427-1)struct foo x = {.a=12, .b=3.14};

Turns out we have more power in these initializers than we’d originally shared. Exciting!

For one thing, if you have a nested substructure like the following, you can initialize members of that substructure by following the variable names down the line:
    
    
    [](structs-ii-more-fun-with-structs.html#cb428-1)struct foo x = {.a.b.c=12};

Let’s look at an example:
    
    
    [](structs-ii-more-fun-with-structs.html#cb429-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb429-2)
    [](structs-ii-more-fun-with-structs.html#cb429-3)struct cabin_information {
    [](structs-ii-more-fun-with-structs.html#cb429-4)    int window_count;
    [](structs-ii-more-fun-with-structs.html#cb429-5)    int o2level;
    [](structs-ii-more-fun-with-structs.html#cb429-6)};
    [](structs-ii-more-fun-with-structs.html#cb429-7)
    [](structs-ii-more-fun-with-structs.html#cb429-8)struct spaceship {
    [](structs-ii-more-fun-with-structs.html#cb429-9)    char *manufacturer;
    [](structs-ii-more-fun-with-structs.html#cb429-10)    struct cabin_information ci;
    [](structs-ii-more-fun-with-structs.html#cb429-11)};
    [](structs-ii-more-fun-with-structs.html#cb429-12)
    [](structs-ii-more-fun-with-structs.html#cb429-13)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb429-14){
    [](structs-ii-more-fun-with-structs.html#cb429-15)    struct spaceship s = {
    [](structs-ii-more-fun-with-structs.html#cb429-16)        .manufacturer="General Products",
    [](structs-ii-more-fun-with-structs.html#cb429-17)        .ci.window_count = 8,   // <-- NESTED INITIALIZER!
    [](structs-ii-more-fun-with-structs.html#cb429-18)        .ci.o2level = 21
    [](structs-ii-more-fun-with-structs.html#cb429-19)    };
    [](structs-ii-more-fun-with-structs.html#cb429-20)
    [](structs-ii-more-fun-with-structs.html#cb429-21)    printf("%s: %d seats, %d%% oxygen\n",
    [](structs-ii-more-fun-with-structs.html#cb429-22)        s.manufacturer, s.ci.window_count, s.ci.o2level);
    [](structs-ii-more-fun-with-structs.html#cb429-23)}

Check out lines 16-17! That’s where we’re initializing members of the `struct cabin_information` in the definition of `s`, our `struct spaceship`.

And here is another option for that same initializer—this time we’ll do something more standard-looking, but either approach works:
    
    
    [](structs-ii-more-fun-with-structs.html#cb430-15)    struct spaceship s = {
    [](structs-ii-more-fun-with-structs.html#cb430-16)        .manufacturer="General Products",
    [](structs-ii-more-fun-with-structs.html#cb430-17)        .ci={
    [](structs-ii-more-fun-with-structs.html#cb430-18)            .window_count = 8,
    [](structs-ii-more-fun-with-structs.html#cb430-19)            .o2level = 21
    [](structs-ii-more-fun-with-structs.html#cb430-20)        }
    [](structs-ii-more-fun-with-structs.html#cb430-21)    };

Now, as if the above information isn’t spectacular enough, we can also mix in array initializers in there, too.

Let’s change this up to get an array of passenger information in there, and we can check out how the initializers work in there, too.
    
    
    [](structs-ii-more-fun-with-structs.html#cb431-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb431-2)
    [](structs-ii-more-fun-with-structs.html#cb431-3)struct passenger {
    [](structs-ii-more-fun-with-structs.html#cb431-4)    char *name;
    [](structs-ii-more-fun-with-structs.html#cb431-5)    int covid_vaccinated; // Boolean
    [](structs-ii-more-fun-with-structs.html#cb431-6)};
    [](structs-ii-more-fun-with-structs.html#cb431-7)
    [](structs-ii-more-fun-with-structs.html#cb431-8)#define MAX_PASSENGERS 8
    [](structs-ii-more-fun-with-structs.html#cb431-9)
    [](structs-ii-more-fun-with-structs.html#cb431-10)struct spaceship {
    [](structs-ii-more-fun-with-structs.html#cb431-11)    char *manufacturer;
    [](structs-ii-more-fun-with-structs.html#cb431-12)    struct passenger passenger[MAX_PASSENGERS];
    [](structs-ii-more-fun-with-structs.html#cb431-13)};
    [](structs-ii-more-fun-with-structs.html#cb431-14)
    [](structs-ii-more-fun-with-structs.html#cb431-15)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb431-16){
    [](structs-ii-more-fun-with-structs.html#cb431-17)    struct spaceship s = {
    [](structs-ii-more-fun-with-structs.html#cb431-18)        .manufacturer="General Products",
    [](structs-ii-more-fun-with-structs.html#cb431-19)        .passenger = {
    [](structs-ii-more-fun-with-structs.html#cb431-20)            // Initialize a field at a time
    [](structs-ii-more-fun-with-structs.html#cb431-21)            [0].name = "Gridley, Lewis",
    [](structs-ii-more-fun-with-structs.html#cb431-22)            [0].covid_vaccinated = 0,
    [](structs-ii-more-fun-with-structs.html#cb431-23)
    [](structs-ii-more-fun-with-structs.html#cb431-24)            // Or all at once
    [](structs-ii-more-fun-with-structs.html#cb431-25)            [7] = {.name="Brown, Teela", .covid_vaccinated=1},
    [](structs-ii-more-fun-with-structs.html#cb431-26)        }
    [](structs-ii-more-fun-with-structs.html#cb431-27)    };
    [](structs-ii-more-fun-with-structs.html#cb431-28)
    [](structs-ii-more-fun-with-structs.html#cb431-29)    printf("Passengers for %s ship:\n", s.manufacturer);
    [](structs-ii-more-fun-with-structs.html#cb431-30)
    [](structs-ii-more-fun-with-structs.html#cb431-31)    for (int i = 0; i < MAX_PASSENGERS; i++)
    [](structs-ii-more-fun-with-structs.html#cb431-32)        if (s.passenger[i].name != NULL)
    [](structs-ii-more-fun-with-structs.html#cb431-33)            printf("    %s (%svaccinated)\n",
    [](structs-ii-more-fun-with-structs.html#cb431-34)                s.passenger[i].name,
    [](structs-ii-more-fun-with-structs.html#cb431-35)                s.passenger[i].covid_vaccinated? "": "not ");
    [](structs-ii-more-fun-with-structs.html#cb431-36)}

## 20.2 Anonymous `struct`s

These are “the `struct` with no name”. We also mention these in the [`typedef`](typedef-making-new-types.html#typedef-struct) section, but we’ll refresh here.

Here’s a regular `struct`:
    
    
    [](structs-ii-more-fun-with-structs.html#cb432-1)struct animal {
    [](structs-ii-more-fun-with-structs.html#cb432-2)    char *name;
    [](structs-ii-more-fun-with-structs.html#cb432-3)    int leg_count, speed;
    [](structs-ii-more-fun-with-structs.html#cb432-4)};

And here’s the anonymous equivalent:
    
    
    [](structs-ii-more-fun-with-structs.html#cb433-1)struct {              // <-- No name!
    [](structs-ii-more-fun-with-structs.html#cb433-2)    char *name;
    [](structs-ii-more-fun-with-structs.html#cb433-3)    int leg_count, speed;
    [](structs-ii-more-fun-with-structs.html#cb433-4)};

Okaaaaay. So we have a `struct`, but it has no name, so we have no way of using it later? Seems pretty pointless.

Admittedly, in that example, it is. But we can still make use of it a couple ways.

One is rare, but since the anonymous `struct` represents a type, we can just put some variable names after it and use them.
    
    
    [](structs-ii-more-fun-with-structs.html#cb434-1)struct {                   // <-- No name!
    [](structs-ii-more-fun-with-structs.html#cb434-2)    char *name;
    [](structs-ii-more-fun-with-structs.html#cb434-3)    int leg_count, speed;
    [](structs-ii-more-fun-with-structs.html#cb434-4)} a, b, c;                 // 3 variables of this struct type
    [](structs-ii-more-fun-with-structs.html#cb434-5)
    [](structs-ii-more-fun-with-structs.html#cb434-6)a.name = "antelope";
    [](structs-ii-more-fun-with-structs.html#cb434-7)c.leg_count = 4;           // for example

But that’s still not that useful.

Far more common is use of anonymous `struct`s with a `typedef` so that we can use it later (e.g. to pass variables to functions).
    
    
    [](structs-ii-more-fun-with-structs.html#cb435-1)typedef struct {                   // <-- No name!
    [](structs-ii-more-fun-with-structs.html#cb435-2)    char *name;
    [](structs-ii-more-fun-with-structs.html#cb435-3)    int leg_count, speed;
    [](structs-ii-more-fun-with-structs.html#cb435-4)} animal;                          // New type: animal
    [](structs-ii-more-fun-with-structs.html#cb435-5)
    [](structs-ii-more-fun-with-structs.html#cb435-6)animal a, b, c;
    [](structs-ii-more-fun-with-structs.html#cb435-7)
    [](structs-ii-more-fun-with-structs.html#cb435-8)a.name = "antelope";
    [](structs-ii-more-fun-with-structs.html#cb435-9)c.leg_count = 4;           // for example

Personally, I don’t use many anonymous `struct`s. I think it’s more pleasant to see the entire `struct animal` before the variable name in a declaration.

But that’s just, like, my opinion, man.

## 20.3 Self-Referential `struct`s

For any graph-like data structure, it’s useful to be able to have pointers to the connected nodes/vertices. But this means that in the definition of a node, you need to have a pointer to a node. It’s chicken and eggy!

But it turns out you can do this in C with no problem whatsoever.

For example, here’s a linked list node:
    
    
    [](structs-ii-more-fun-with-structs.html#cb436-1)struct node {
    [](structs-ii-more-fun-with-structs.html#cb436-2)    int data;
    [](structs-ii-more-fun-with-structs.html#cb436-3)    struct node *next;
    [](structs-ii-more-fun-with-structs.html#cb436-4)};

It’s important to note that `next` is a pointer. This is what allows the whole thing to even build. Even though the compiler doesn’t know what the entire `struct node` looks like yet, all pointers are the same size.

Here’s a cheesy linked list program to test it out:
    
    
    [](structs-ii-more-fun-with-structs.html#cb437-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb437-2)#include <stdlib.h>
    [](structs-ii-more-fun-with-structs.html#cb437-3)
    [](structs-ii-more-fun-with-structs.html#cb437-4)struct node {
    [](structs-ii-more-fun-with-structs.html#cb437-5)    int data;
    [](structs-ii-more-fun-with-structs.html#cb437-6)    struct node *next;
    [](structs-ii-more-fun-with-structs.html#cb437-7)};
    [](structs-ii-more-fun-with-structs.html#cb437-8)
    [](structs-ii-more-fun-with-structs.html#cb437-9)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb437-10){
    [](structs-ii-more-fun-with-structs.html#cb437-11)    struct node *head;
    [](structs-ii-more-fun-with-structs.html#cb437-12)
    [](structs-ii-more-fun-with-structs.html#cb437-13)    // Hackishly set up a linked list (11)->(22)->(33)
    [](structs-ii-more-fun-with-structs.html#cb437-14)    head = malloc(sizeof(struct node));
    [](structs-ii-more-fun-with-structs.html#cb437-15)    head->data = 11;
    [](structs-ii-more-fun-with-structs.html#cb437-16)    head->next = malloc(sizeof(struct node));
    [](structs-ii-more-fun-with-structs.html#cb437-17)    head->next->data = 22;
    [](structs-ii-more-fun-with-structs.html#cb437-18)    head->next->next = malloc(sizeof(struct node));
    [](structs-ii-more-fun-with-structs.html#cb437-19)    head->next->next->data = 33;
    [](structs-ii-more-fun-with-structs.html#cb437-20)    head->next->next->next = NULL;
    [](structs-ii-more-fun-with-structs.html#cb437-21)
    [](structs-ii-more-fun-with-structs.html#cb437-22)    // Traverse it
    [](structs-ii-more-fun-with-structs.html#cb437-23)    for (struct node *cur = head; cur != NULL; cur = cur->next) {
    [](structs-ii-more-fun-with-structs.html#cb437-24)        printf("%d\n", cur->data);
    [](structs-ii-more-fun-with-structs.html#cb437-25)    }
    [](structs-ii-more-fun-with-structs.html#cb437-26)}

Running that prints:
    
    
    [](structs-ii-more-fun-with-structs.html#cb438-1)11
    [](structs-ii-more-fun-with-structs.html#cb438-2)22
    [](structs-ii-more-fun-with-structs.html#cb438-3)33

## 20.4 Flexible Array Members

Back in the good old days, when people carved C code out of wood, some folks thought would be neat if they could allocate `struct`s that had variable length arrays at the end of them.

I want to be clear that the first part of the section is the old way of doing things, and we’re going to do things the new way after that.

For example, maybe you could define a `struct` for holding strings and the length of that string. It would have a length and an array to hold the data. Maybe something like this:
    
    
    [](structs-ii-more-fun-with-structs.html#cb439-1)struct len_string {
    [](structs-ii-more-fun-with-structs.html#cb439-2)    int length;
    [](structs-ii-more-fun-with-structs.html#cb439-3)    char data[8];
    [](structs-ii-more-fun-with-structs.html#cb439-4)};

But that has `8` hardcoded as the maximum length of a string, and that’s not much. What if we did something _clever_ and just `malloc()`d some extra space at the end after the struct, and then let the data overflow into that space?

Let’s do that, and then allocate another 40 bytes on top of it:
    
    
    [](structs-ii-more-fun-with-structs.html#cb440-1)struct len_string *s = malloc(sizeof *s + 40);

Because `data` is the last field of the `struct`, if we overflow that field, it runs out into space that we already allocated! For this reason, this trick only works if the short array is the _last_ field in the `struct`.
    
    
    [](structs-ii-more-fun-with-structs.html#cb441-1)// Copy more than 8 bytes!
    [](structs-ii-more-fun-with-structs.html#cb441-2)
    [](structs-ii-more-fun-with-structs.html#cb441-3)strcpy(s->data, "Hello, world!");  // Won't crash. Probably.

In fact, there was a common compiler workaround for doing this, where you’d allocate a zero length array at the end:
    
    
    [](structs-ii-more-fun-with-structs.html#cb442-1)struct len_string {
    [](structs-ii-more-fun-with-structs.html#cb442-2)    int length;
    [](structs-ii-more-fun-with-structs.html#cb442-3)    char data[0];
    [](structs-ii-more-fun-with-structs.html#cb442-4)};

And then every extra byte you allocated was ready for use in that string.

Because `data` is the last field of the `struct`, if we overflow that field, it runs out into space that we already allocated!
    
    
    [](structs-ii-more-fun-with-structs.html#cb443-1)// Copy more than 8 bytes!
    [](structs-ii-more-fun-with-structs.html#cb443-2)
    [](structs-ii-more-fun-with-structs.html#cb443-3)strcpy(s->data, "Hello, world!");  // Won't crash. Probably.

But, of course, actually accessing the data beyond the end of that array is undefined behavior! In these modern times, we no longer deign to resort to such savagery.

Luckily for us, we can still get the same effect with C99 and later, but now it’s legal.

Let’s just change our above definition to have no size for the array[135](function-specifiers-alignment-specifiersoperators.html#fn135):
    
    
    [](structs-ii-more-fun-with-structs.html#cb444-1)struct len_string {
    [](structs-ii-more-fun-with-structs.html#cb444-2)    int length;
    [](structs-ii-more-fun-with-structs.html#cb444-3)    char data[];
    [](structs-ii-more-fun-with-structs.html#cb444-4)};

Again, this only works if the flexible array member is the _last_ field in the `struct`.

And then we can allocate all the space we want for those strings by `malloc()`ing larger than the `struct len_string`, as we do in this example that makes a new `struct len_string` from a C string:
    
    
    [](structs-ii-more-fun-with-structs.html#cb445-1)struct len_string *len_string_from_c_string(char *s)
    [](structs-ii-more-fun-with-structs.html#cb445-2){
    [](structs-ii-more-fun-with-structs.html#cb445-3)    int len = strlen(s);
    [](structs-ii-more-fun-with-structs.html#cb445-4)
    [](structs-ii-more-fun-with-structs.html#cb445-5)    // Allocate "len" more bytes than we'd normally need
    [](structs-ii-more-fun-with-structs.html#cb445-6)    struct len_string *ls = malloc(sizeof *ls + len);
    [](structs-ii-more-fun-with-structs.html#cb445-7)
    [](structs-ii-more-fun-with-structs.html#cb445-8)    ls->length = len;
    [](structs-ii-more-fun-with-structs.html#cb445-9)
    [](structs-ii-more-fun-with-structs.html#cb445-10)    // Copy the string into those extra bytes
    [](structs-ii-more-fun-with-structs.html#cb445-11)    memcpy(ls->data, s, len);
    [](structs-ii-more-fun-with-structs.html#cb445-12)
    [](structs-ii-more-fun-with-structs.html#cb445-13)    return ls;
    [](structs-ii-more-fun-with-structs.html#cb445-14)}

## 20.5 Padding Bytes

Beware that C is allowed to add padding bytes within or after a `struct` as it sees fit. You can’t trust that they will be directly adjacent in memory[136](function-specifiers-alignment-specifiersoperators.html#fn136).

Let’s take a look at this program. We output two numbers. One is the sum of the `sizeof`s the individual field types. The other is the `sizeof` the entire `struct`.

One would expect them to be the same. The size of the total is the size of the sum of its parts, right?
    
    
    [](structs-ii-more-fun-with-structs.html#cb446-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb446-2)
    [](structs-ii-more-fun-with-structs.html#cb446-3)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb446-4)    int a;
    [](structs-ii-more-fun-with-structs.html#cb446-5)    char b;
    [](structs-ii-more-fun-with-structs.html#cb446-6)    int c;
    [](structs-ii-more-fun-with-structs.html#cb446-7)    char d;
    [](structs-ii-more-fun-with-structs.html#cb446-8)};
    [](structs-ii-more-fun-with-structs.html#cb446-9)
    [](structs-ii-more-fun-with-structs.html#cb446-10)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb446-11){
    [](structs-ii-more-fun-with-structs.html#cb446-12)    printf("%zu\n", sizeof(int) + sizeof(char) + sizeof(int) + sizeof(char));
    [](structs-ii-more-fun-with-structs.html#cb446-13)    printf("%zu\n", sizeof(struct foo));
    [](structs-ii-more-fun-with-structs.html#cb446-14)}

But on my system, this outputs:
    
    
    [](structs-ii-more-fun-with-structs.html#cb447-1)10
    [](structs-ii-more-fun-with-structs.html#cb447-2)16

They’re not the same! The compiler has added 6 bytes of padding to help it be more performant. Maybe you got different output with your compiler, but unless you’re forcing it, you can’t be sure there’s no padding.

## 20.6 `offsetof`

In the previous section, we saw that the compiler could inject padding bytes at will inside a structure.

What if we needed to know where those were? We can measure it with `offsetof`, defined in `<stddef.h>`.

Let’s modify the code from above to print the offsets of the individual fields in the `struct`:
    
    
    [](structs-ii-more-fun-with-structs.html#cb448-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb448-2)#include <stddef.h>
    [](structs-ii-more-fun-with-structs.html#cb448-3)
    [](structs-ii-more-fun-with-structs.html#cb448-4)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb448-5)    int a;
    [](structs-ii-more-fun-with-structs.html#cb448-6)    char b;
    [](structs-ii-more-fun-with-structs.html#cb448-7)    int c;
    [](structs-ii-more-fun-with-structs.html#cb448-8)    char d;
    [](structs-ii-more-fun-with-structs.html#cb448-9)};
    [](structs-ii-more-fun-with-structs.html#cb448-10)
    [](structs-ii-more-fun-with-structs.html#cb448-11)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb448-12){
    [](structs-ii-more-fun-with-structs.html#cb448-13)    printf("%zu\n", offsetof(struct foo, a));
    [](structs-ii-more-fun-with-structs.html#cb448-14)    printf("%zu\n", offsetof(struct foo, b));
    [](structs-ii-more-fun-with-structs.html#cb448-15)    printf("%zu\n", offsetof(struct foo, c));
    [](structs-ii-more-fun-with-structs.html#cb448-16)    printf("%zu\n", offsetof(struct foo, d));
    [](structs-ii-more-fun-with-structs.html#cb448-17)}

For me, this outputs:
    
    
    [](structs-ii-more-fun-with-structs.html#cb449-1)0
    [](structs-ii-more-fun-with-structs.html#cb449-2)4
    [](structs-ii-more-fun-with-structs.html#cb449-3)8
    [](structs-ii-more-fun-with-structs.html#cb449-4)12

indicating that we’re using 4 bytes for each of the fields. It’s a little weird, because `char` is only 1 byte, right? The compiler is putting 3 padding bytes after each `char` so that all the fields are 4 bytes long. Presumably this will run faster on my CPU.

## 20.7 Fake OOP

There’s a slightly abusive thing that’s sort of OOP-like that you can do with `struct`s.

Since the pointer to the `struct` is the same as a pointer to the first element of the `struct`, you can freely cast a pointer to the `struct` to a pointer to the first element.

What this means is that we can set up a situation like this:
    
    
    [](structs-ii-more-fun-with-structs.html#cb450-1)struct parent {
    [](structs-ii-more-fun-with-structs.html#cb450-2)    int a, b;
    [](structs-ii-more-fun-with-structs.html#cb450-3)};
    [](structs-ii-more-fun-with-structs.html#cb450-4)
    [](structs-ii-more-fun-with-structs.html#cb450-5)struct child {
    [](structs-ii-more-fun-with-structs.html#cb450-6)    struct parent super;  // MUST be first
    [](structs-ii-more-fun-with-structs.html#cb450-7)    int c, d;
    [](structs-ii-more-fun-with-structs.html#cb450-8)};

Then we are able to pass a pointer to a `struct child` to a function that expects either that _or_ a pointer to a `struct parent`!

Because `struct parent super` is the first item in the `struct child`, a pointer to any `struct child` is the same as a pointer to that `super` field[137](function-specifiers-alignment-specifiersoperators.html#fn137).

Let’s set up an example here. We’ll make `struct`s as above, but then we’ll pass a pointer to a `struct child` to a function that needs a pointer to a `struct parent`… and it’ll still work.
    
    
    [](structs-ii-more-fun-with-structs.html#cb451-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb451-2)
    [](structs-ii-more-fun-with-structs.html#cb451-3)struct parent {
    [](structs-ii-more-fun-with-structs.html#cb451-4)    int a, b;
    [](structs-ii-more-fun-with-structs.html#cb451-5)};
    [](structs-ii-more-fun-with-structs.html#cb451-6)
    [](structs-ii-more-fun-with-structs.html#cb451-7)struct child {
    [](structs-ii-more-fun-with-structs.html#cb451-8)    struct parent super;  // MUST be first
    [](structs-ii-more-fun-with-structs.html#cb451-9)    int c, d;
    [](structs-ii-more-fun-with-structs.html#cb451-10)};
    [](structs-ii-more-fun-with-structs.html#cb451-11)
    [](structs-ii-more-fun-with-structs.html#cb451-12)// Making the argument `void*` so we can pass any type into it
    [](structs-ii-more-fun-with-structs.html#cb451-13)// (namely a struct parent or struct child)
    [](structs-ii-more-fun-with-structs.html#cb451-14)void print_parent(void *p)
    [](structs-ii-more-fun-with-structs.html#cb451-15){
    [](structs-ii-more-fun-with-structs.html#cb451-16)    // Expects a struct parent--but a struct child will also work
    [](structs-ii-more-fun-with-structs.html#cb451-17)    // because the pointer points to the struct parent in the first
    [](structs-ii-more-fun-with-structs.html#cb451-18)    // field:
    [](structs-ii-more-fun-with-structs.html#cb451-19)    struct parent *self = p;
    [](structs-ii-more-fun-with-structs.html#cb451-20)
    [](structs-ii-more-fun-with-structs.html#cb451-21)    printf("Parent: %d, %d\n", self->a, self->b);
    [](structs-ii-more-fun-with-structs.html#cb451-22)}
    [](structs-ii-more-fun-with-structs.html#cb451-23)
    [](structs-ii-more-fun-with-structs.html#cb451-24)void print_child(struct child *self)
    [](structs-ii-more-fun-with-structs.html#cb451-25){
    [](structs-ii-more-fun-with-structs.html#cb451-26)    printf("Child: %d, %d\n", self->c, self->d);
    [](structs-ii-more-fun-with-structs.html#cb451-27)}
    [](structs-ii-more-fun-with-structs.html#cb451-28)
    [](structs-ii-more-fun-with-structs.html#cb451-29)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb451-30){
    [](structs-ii-more-fun-with-structs.html#cb451-31)    struct child c = {.super.a=1, .super.b=2, .c=3, .d=4};
    [](structs-ii-more-fun-with-structs.html#cb451-32)
    [](structs-ii-more-fun-with-structs.html#cb451-33)    print_child(&c);
    [](structs-ii-more-fun-with-structs.html#cb451-34)    print_parent(&c);  // Also works even though it's a struct child!
    [](structs-ii-more-fun-with-structs.html#cb451-35)}

See what we did on the last line of `main()`? We called `print_parent()` but passed a `struct child*` as the argument! Even though `print_parent()` needs the argument to point to a `struct parent`, we’re _getting away with it_ because the first field in the `struct child` is a `struct parent`.

Again, this works because a pointer to a `struct` has the same value as a pointer to the first field in that `struct`.

This all hinges on this part of the spec:

> **§6.7.2.1¶15** […] A pointer to a structure object, suitably converted, points to its initial member […], and vice versa.

and

> **§6.5¶7** An object shall have its stored value accessed only by an lvalue expression that has one of the following types:
> 
>   * a type compatible with the effective type of the object
>   * […]
> 


and my assumption that “suitably converted” means “cast to the effective type of the initial member”.

## 20.8 Bit-Fields

In my experience, these are rarely used, but you might see them out there from time to time, especially in lower-level applications that pack bits together into larger spaces.

Let’s take a look at some code to demonstrate a use case:
    
    
    [](structs-ii-more-fun-with-structs.html#cb452-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb452-2)
    [](structs-ii-more-fun-with-structs.html#cb452-3)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb452-4)    unsigned int a;
    [](structs-ii-more-fun-with-structs.html#cb452-5)    unsigned int b;
    [](structs-ii-more-fun-with-structs.html#cb452-6)    unsigned int c;
    [](structs-ii-more-fun-with-structs.html#cb452-7)    unsigned int d;
    [](structs-ii-more-fun-with-structs.html#cb452-8)};
    [](structs-ii-more-fun-with-structs.html#cb452-9)
    [](structs-ii-more-fun-with-structs.html#cb452-10)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb452-11){
    [](structs-ii-more-fun-with-structs.html#cb452-12)    printf("%zu\n", sizeof(struct foo));
    [](structs-ii-more-fun-with-structs.html#cb452-13)}

For me, this prints `16`. Which makes sense, since `unsigned`s are 4 bytes on my system.

But what if we knew that all the values that were going to be stored in `a` and `b` could be stored in 5 bits, and the values in `c`, and `d` could be stored in 3 bits? That’s only a total 16 bits. Why have 128 bits reserved for them if we’re only going to use 16?

Well, we can tell C to pretty-please try to pack these values in. We can specify the maximum number of bits that values can take (from 1 up the size of the containing type).

We do this by putting a colon after the field name, followed by the field width in bits.
    
    
    [](structs-ii-more-fun-with-structs.html#cb453-3)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb453-4)    unsigned int a:5;
    [](structs-ii-more-fun-with-structs.html#cb453-5)    unsigned int b:5;
    [](structs-ii-more-fun-with-structs.html#cb453-6)    unsigned int c:3;
    [](structs-ii-more-fun-with-structs.html#cb453-7)    unsigned int d:3;
    [](structs-ii-more-fun-with-structs.html#cb453-8)};

Now when I ask C how big my `struct foo` is, it tells me 4! It was 16 bytes, but now it’s only 4. It has “packed” those 4 values down into 4 bytes, which is a four-fold memory savings.

The tradeoff is, of course, that the 5-bit fields can only hold values from 0-31 and the 3-bit fields can only hold values from 0-7. But life’s all about compromise, after all.

### 20.8.1 Non-Adjacent Bit-Fields

A gotcha: C will only combine **adjacent** bit-fields. If they’re interrupted by non-bit-fields, you get no savings:
    
    
    [](structs-ii-more-fun-with-structs.html#cb454-1)struct foo {            // sizeof(struct foo) == 16 (for me)
    [](structs-ii-more-fun-with-structs.html#cb454-2)    unsigned int a:1;   // since a is not adjacent to c.
    [](structs-ii-more-fun-with-structs.html#cb454-3)    unsigned int b;
    [](structs-ii-more-fun-with-structs.html#cb454-4)    unsigned int c:1;
    [](structs-ii-more-fun-with-structs.html#cb454-5)    unsigned int d;
    [](structs-ii-more-fun-with-structs.html#cb454-6)};

In that example, since `a` is not adjacent to `c`, they are both “packed” in their own `int`s.

So we have one `int` each for `a`, `b`, `c`, and `d`. Since my `int`s are 4 bytes, that’s a grand total of 16 bytes.

A quick rearrangement yields some space savings from 16 bytes down to 12 bytes (on my system):
    
    
    [](structs-ii-more-fun-with-structs.html#cb455-1)struct foo {            // sizeof(struct foo) == 12 (for me)
    [](structs-ii-more-fun-with-structs.html#cb455-2)    unsigned int a:1;
    [](structs-ii-more-fun-with-structs.html#cb455-3)    unsigned int c:1;
    [](structs-ii-more-fun-with-structs.html#cb455-4)    unsigned int b;
    [](structs-ii-more-fun-with-structs.html#cb455-5)    unsigned int d;
    [](structs-ii-more-fun-with-structs.html#cb455-6)};

And now, since `a` is next to `c`, the compiler puts them together into a single `int`.

So we have one `int` for a combined `a` and `c`, and one `int` each for `b` and `d`. For a grand total of 3 `int`s, or 12 bytes.

Put all your bitfields together to get the compiler to combine them.

### 20.8.2 Signed or Unsigned `int`s

If you just declare a bit-field to be `int`, the different compilers will treat it as `signed` or `unsigned`. Just like the situation with `char`.

Be specific about the signedness when using bit-fields.

### 20.8.3 Unnamed Bit-Fields

In some specific circumstances, you might need to reserve some bits for hardware reasons, but not need to use them in code.

For example, let’s say you have a byte where the top 2 bits have a meaning, the bottom 1 bit has a meaning, but the middle 5 bits do not get used by you[138](function-specifiers-alignment-specifiersoperators.html#fn138).

We _could_ do something like this:
    
    
    [](structs-ii-more-fun-with-structs.html#cb456-1)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb456-2)    unsigned char a:2;
    [](structs-ii-more-fun-with-structs.html#cb456-3)    unsigned char dummy:5;
    [](structs-ii-more-fun-with-structs.html#cb456-4)    unsigned char b:1;
    [](structs-ii-more-fun-with-structs.html#cb456-5)};

And that works—in our code we use `a` and `b`, but never `dummy`. It’s just there to eat up 5 bits to make sure `a` and `b` are in the “required” (by this contrived example) positions within the byte.

C allows us a way to clean this up: _unnamed bit-fields_. You can just leave the name (`dummy`) out in this case, and C is perfectly happy for the same effect:
    
    
    [](structs-ii-more-fun-with-structs.html#cb457-1)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb457-2)    unsigned char a:2;
    [](structs-ii-more-fun-with-structs.html#cb457-3)    unsigned char :5;   // <-- unnamed bit-field!
    [](structs-ii-more-fun-with-structs.html#cb457-4)    unsigned char b:1;
    [](structs-ii-more-fun-with-structs.html#cb457-5)};

### 20.8.4 Zero-Width Unnamed Bit-Fields

Some more esoterica out here… Let’s say you were packing bits into an `unsigned int`, and you needed some adjacent bit-fields to pack into the _next_ `unsigned int`.

That is, if you do this:
    
    
    [](structs-ii-more-fun-with-structs.html#cb458-1)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb458-2)    unsigned int a:1;
    [](structs-ii-more-fun-with-structs.html#cb458-3)    unsigned int b:2;
    [](structs-ii-more-fun-with-structs.html#cb458-4)    unsigned int c:3;
    [](structs-ii-more-fun-with-structs.html#cb458-5)    unsigned int d:4;
    [](structs-ii-more-fun-with-structs.html#cb458-6)};

the compiler packs all those into a single `unsigned int`. But what if you needed `a` and `b` in one `int`, and `c` and `d` in a different one?

There’s a solution for that: put an unnamed bit-field of width `0` where you want the compiler to start anew with packing bits in a different `int`:
    
    
    [](structs-ii-more-fun-with-structs.html#cb459-1)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb459-2)    unsigned int a:1;
    [](structs-ii-more-fun-with-structs.html#cb459-3)    unsigned int b:2;
    [](structs-ii-more-fun-with-structs.html#cb459-4)    unsigned int :0;   // <--Zero-width unnamed bit-field
    [](structs-ii-more-fun-with-structs.html#cb459-5)    unsigned int c:3;
    [](structs-ii-more-fun-with-structs.html#cb459-6)    unsigned int d:4;
    [](structs-ii-more-fun-with-structs.html#cb459-7)};

It’s analogous to an explicit page break in a word processor. You’re telling the compiler, “Stop packing bits in this `unsigned`, and start packing them in the next one.”

By adding the zero-width unnamed bit field in that spot, the compiler puts `a` and `b` in one `unsigned int`, and `c` and `d` in another `unsigned int`. Two total, for a size of 8 bytes on my system (`unsigned int`s are 4 bytes each).

## 20.9 Unions

These are basically just like `struct`s, except the fields overlap in memory. The `union` will be only large enough for the largest field, and you can only use one field at a time.

It’s a way to reuse the same memory space for different types of data.

You declare them just like `struct`s, except it’s `union`. Take a look at this:
    
    
    [](structs-ii-more-fun-with-structs.html#cb460-1)union foo {
    [](structs-ii-more-fun-with-structs.html#cb460-2)    int a, b, c, d, e, f;
    [](structs-ii-more-fun-with-structs.html#cb460-3)    float g, h;
    [](structs-ii-more-fun-with-structs.html#cb460-4)    char i, j, k, l;
    [](structs-ii-more-fun-with-structs.html#cb460-5)};

Now, that’s a lot of fields. If this were a `struct`, my system would tell me it took 36 bytes to hold it all.

But it’s a `union`, so all those fields overlap in the same stretch of memory. The biggest one is `int` (or `float`), taking up 4 bytes on my system. And, indeed, if I ask for the `sizeof` the `union foo`, it tells me 4!

The tradeoff is that you can only portably use one of those fields at a time. However…

### 20.9.1 Unions and Type Punning

You can non-portably write to one `union` field and read from another!

Doing so is called [type punning](https://en.wikipedia.org/wiki/Type_punning)[139](function-specifiers-alignment-specifiersoperators.html#fn139), and you’d use it if you really knew what you were doing, typically with some kind of low-level programming.

Since the members of a union share the same memory, writing to one member necessarily affects the others. And if you read from one what was written to another, you get some weird effects.
    
    
    [](structs-ii-more-fun-with-structs.html#cb461-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb461-2)
    [](structs-ii-more-fun-with-structs.html#cb461-3)union foo {
    [](structs-ii-more-fun-with-structs.html#cb461-4)    float b;
    [](structs-ii-more-fun-with-structs.html#cb461-5)    short a;
    [](structs-ii-more-fun-with-structs.html#cb461-6)};
    [](structs-ii-more-fun-with-structs.html#cb461-7)
    [](structs-ii-more-fun-with-structs.html#cb461-8)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb461-9){
    [](structs-ii-more-fun-with-structs.html#cb461-10)    union foo x;
    [](structs-ii-more-fun-with-structs.html#cb461-11)
    [](structs-ii-more-fun-with-structs.html#cb461-12)    x.b = 3.14159;
    [](structs-ii-more-fun-with-structs.html#cb461-13)
    [](structs-ii-more-fun-with-structs.html#cb461-14)    printf("%f\n", x.b);  // 3.14159, fair enough
    [](structs-ii-more-fun-with-structs.html#cb461-15)
    [](structs-ii-more-fun-with-structs.html#cb461-16)    printf("%d\n", x.a);  // But what about this?
    [](structs-ii-more-fun-with-structs.html#cb461-17)}

On my system, this prints out:
    
    
    3.141590
    4048

because under the hood, the object representation for the float `3.14159` was the same as the object representation for the short `4048`. On my system. Your results may vary.

### 20.9.2 Pointers to `union`s

If you have a pointer to a `union`, you can cast that pointer to any of the types of the fields in that `union` and get the values out that way.

In this example, we see that the `union` has `int`s and `float`s in it. And we get pointers to the `union`, but we cast them to `int*` and `float*` types (the cast silences compiler warnings). And then if we dereference those, we see that they have the values we stored directly in the `union`.
    
    
    [](structs-ii-more-fun-with-structs.html#cb463-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb463-2)
    [](structs-ii-more-fun-with-structs.html#cb463-3)union foo {
    [](structs-ii-more-fun-with-structs.html#cb463-4)    int a, b, c, d, e, f;
    [](structs-ii-more-fun-with-structs.html#cb463-5)    float g, h;
    [](structs-ii-more-fun-with-structs.html#cb463-6)    char i, j, k, l;
    [](structs-ii-more-fun-with-structs.html#cb463-7)};
    [](structs-ii-more-fun-with-structs.html#cb463-8)
    [](structs-ii-more-fun-with-structs.html#cb463-9)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb463-10){
    [](structs-ii-more-fun-with-structs.html#cb463-11)    union foo x;
    [](structs-ii-more-fun-with-structs.html#cb463-12)
    [](structs-ii-more-fun-with-structs.html#cb463-13)    int *foo_int_p = (int *)&x;
    [](structs-ii-more-fun-with-structs.html#cb463-14)    float *foo_float_p = (float *)&x;
    [](structs-ii-more-fun-with-structs.html#cb463-15)
    [](structs-ii-more-fun-with-structs.html#cb463-16)    x.a = 12;
    [](structs-ii-more-fun-with-structs.html#cb463-17)    printf("%d\n", x.a);           // 12
    [](structs-ii-more-fun-with-structs.html#cb463-18)    printf("%d\n", *foo_int_p);    // 12, again
    [](structs-ii-more-fun-with-structs.html#cb463-19)
    [](structs-ii-more-fun-with-structs.html#cb463-20)    x.g = 3.141592;
    [](structs-ii-more-fun-with-structs.html#cb463-21)    printf("%f\n", x.g);           // 3.141592
    [](structs-ii-more-fun-with-structs.html#cb463-22)    printf("%f\n", *foo_float_p);  // 3.141592, again
    [](structs-ii-more-fun-with-structs.html#cb463-23)}

The reverse is also true. If we have a pointer to a type inside the `union`, we can cast that to a pointer to the `union` and access its members.
    
    
    [](structs-ii-more-fun-with-structs.html#cb464-1)union foo x;
    [](structs-ii-more-fun-with-structs.html#cb464-2)int *foo_int_p = (int *)&x;             // Pointer to int field
    [](structs-ii-more-fun-with-structs.html#cb464-3)union foo *p = (union foo *)foo_int_p;  // Back to pointer to union
    [](structs-ii-more-fun-with-structs.html#cb464-4)
    [](structs-ii-more-fun-with-structs.html#cb464-5)p->a = 12;  // This line the same as...
    [](structs-ii-more-fun-with-structs.html#cb464-6)x.a = 12;   // this one.

All this just lets you know that, under the hood, all these values in a `union` start at the same place in memory, and that’s the same as where the entire `union` is.

### 20.9.3 Common Initial Sequences in Unions

If you have a `union` of `struct`s, and all those `struct`s begin with a _common initial sequence_ , it’s valid to access members of that sequence from any of the `union` members.

What?

Here are two `struct`s with a common initial sequence:
    
    
    [](structs-ii-more-fun-with-structs.html#cb465-1)struct a {
    [](structs-ii-more-fun-with-structs.html#cb465-2)    int x;     //
    [](structs-ii-more-fun-with-structs.html#cb465-3)    float y;   // Common initial sequence
    [](structs-ii-more-fun-with-structs.html#cb465-4)
    [](structs-ii-more-fun-with-structs.html#cb465-5)    char *p;
    [](structs-ii-more-fun-with-structs.html#cb465-6)};
    [](structs-ii-more-fun-with-structs.html#cb465-7)
    [](structs-ii-more-fun-with-structs.html#cb465-8)struct b {
    [](structs-ii-more-fun-with-structs.html#cb465-9)    int x;     //
    [](structs-ii-more-fun-with-structs.html#cb465-10)    float y;   // Common initial sequence
    [](structs-ii-more-fun-with-structs.html#cb465-11)
    [](structs-ii-more-fun-with-structs.html#cb465-12)    double *p;
    [](structs-ii-more-fun-with-structs.html#cb465-13)    short z;
    [](structs-ii-more-fun-with-structs.html#cb465-14)};

Do you see it? It’s that they start with `int` followed by `float`—that’s the common initial sequence. The members in the sequence of the `struct`s have to be compatible types. And we see that with `x` and `y`, which are `int` and `float` respectively.

Now let’s build a union of these:
    
    
    [](structs-ii-more-fun-with-structs.html#cb466-1)union foo {
    [](structs-ii-more-fun-with-structs.html#cb466-2)    struct a sa;
    [](structs-ii-more-fun-with-structs.html#cb466-3)    struct b sb;
    [](structs-ii-more-fun-with-structs.html#cb466-4)};

What this rule tells us is that we’re guaranteed that the members of the common initial sequences are interchangeable in code. That is:

  * `f.sa.x` is the same as `f.sb.x`.



and

  * `f.sa.y` is the same as `f.sb.y`.



Because fields `x` and `y` are both in the common initial sequence.

Also, the names of the members in the common initial sequence don’t matter—all that matters is that the types are the same.

All together, this allows us a way to safely add some shared information between `struct`s in the `union`. The best example of this is probably using a field to determine the type of `struct` out of all the `struct`s in the `union` that is currently “in use”.

That is, if we weren’t allowed this and we passed the `union` to some function, how would that function know which member of the `union` was the one it should look at?

Take a look at these `struct`s. Note the common initial sequence:
    
    
    [](structs-ii-more-fun-with-structs.html#cb467-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb467-2)
    [](structs-ii-more-fun-with-structs.html#cb467-3)struct common {
    [](structs-ii-more-fun-with-structs.html#cb467-4)    int type;   // common initial sequence
    [](structs-ii-more-fun-with-structs.html#cb467-5)};
    [](structs-ii-more-fun-with-structs.html#cb467-6)
    [](structs-ii-more-fun-with-structs.html#cb467-7)struct antelope {
    [](structs-ii-more-fun-with-structs.html#cb467-8)    int type;   // common initial sequence
    [](structs-ii-more-fun-with-structs.html#cb467-9)
    [](structs-ii-more-fun-with-structs.html#cb467-10)    int loudness;
    [](structs-ii-more-fun-with-structs.html#cb467-11)};
    [](structs-ii-more-fun-with-structs.html#cb467-12)
    [](structs-ii-more-fun-with-structs.html#cb467-13)struct octopus {
    [](structs-ii-more-fun-with-structs.html#cb467-14)    int type;   // common initial sequence
    [](structs-ii-more-fun-with-structs.html#cb467-15)
    [](structs-ii-more-fun-with-structs.html#cb467-16)    int sea_creature;
    [](structs-ii-more-fun-with-structs.html#cb467-17)    float intelligence;
    [](structs-ii-more-fun-with-structs.html#cb467-18)};

Now let’s throw them into a `union`:
    
    
    [](structs-ii-more-fun-with-structs.html#cb468-20)union animal {
    [](structs-ii-more-fun-with-structs.html#cb468-21)    struct common common;
    [](structs-ii-more-fun-with-structs.html#cb468-22)    struct antelope antelope;
    [](structs-ii-more-fun-with-structs.html#cb468-23)    struct octopus octopus;
    [](structs-ii-more-fun-with-structs.html#cb468-24)};

Also, please indulge me these two `#define`s for the demo:
    
    
    [](structs-ii-more-fun-with-structs.html#cb469-26)#define ANTELOPE 1
    [](structs-ii-more-fun-with-structs.html#cb469-27)#define OCTOPUS  2

So far, nothing special has happened here. It seems like the `type` field is completely useless.

But now let’s make a generic function that prints a `union animal`. It has to somehow be able to tell if it’s looking at a `struct antelope` or a `struct octopus`.

Because of the magic of common initial sequences, it can look up the animal type in any of these places for a particular `union animal x`:
    
    
    [](structs-ii-more-fun-with-structs.html#cb470-1)int type = x.common.type;    \\ or...
    [](structs-ii-more-fun-with-structs.html#cb470-2)int type = x.antelope.type;  \\ or...
    [](structs-ii-more-fun-with-structs.html#cb470-3)int type = x.octopus.type;

All those refer to the same value in memory.

And, as you might have guessed, the `struct common` is there so code can agnostically look at the type without mentioning a particular animal.

Let’s look at the code to print a `union animal`:
    
    
    [](structs-ii-more-fun-with-structs.html#cb471-29)void print_animal(union animal *x)
    [](structs-ii-more-fun-with-structs.html#cb471-30){
    [](structs-ii-more-fun-with-structs.html#cb471-31)    switch (x->common.type) {
    [](structs-ii-more-fun-with-structs.html#cb471-32)        case ANTELOPE:
    [](structs-ii-more-fun-with-structs.html#cb471-33)            printf("Antelope: loudness=%d\n", x->antelope.loudness);
    [](structs-ii-more-fun-with-structs.html#cb471-34)            break;
    [](structs-ii-more-fun-with-structs.html#cb471-35)
    [](structs-ii-more-fun-with-structs.html#cb471-36)        case OCTOPUS:
    [](structs-ii-more-fun-with-structs.html#cb471-37)            printf("Octopus : sea_creature=%d\n", x->octopus.sea_creature);
    [](structs-ii-more-fun-with-structs.html#cb471-38)            printf("          intelligence=%f\n", x->octopus.intelligence);
    [](structs-ii-more-fun-with-structs.html#cb471-39)            break;
    [](structs-ii-more-fun-with-structs.html#cb471-40)        
    [](structs-ii-more-fun-with-structs.html#cb471-41)        default:
    [](structs-ii-more-fun-with-structs.html#cb471-42)            printf("Unknown animal type\n");
    [](structs-ii-more-fun-with-structs.html#cb471-43)    }
    [](structs-ii-more-fun-with-structs.html#cb471-44)
    [](structs-ii-more-fun-with-structs.html#cb471-45)}
    [](structs-ii-more-fun-with-structs.html#cb471-46)
    [](structs-ii-more-fun-with-structs.html#cb471-47)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb471-48){
    [](structs-ii-more-fun-with-structs.html#cb471-49)    union animal a = {.antelope.type=ANTELOPE, .antelope.loudness=12};
    [](structs-ii-more-fun-with-structs.html#cb471-50)    union animal b = {.octopus.type=OCTOPUS, .octopus.sea_creature=1,
    [](structs-ii-more-fun-with-structs.html#cb471-51)                                       .octopus.intelligence=12.8};
    [](structs-ii-more-fun-with-structs.html#cb471-52)
    [](structs-ii-more-fun-with-structs.html#cb471-53)    print_animal(&a);
    [](structs-ii-more-fun-with-structs.html#cb471-54)    print_animal(&b);
    [](structs-ii-more-fun-with-structs.html#cb471-55)}

See how on line 29 we’re just passing in the `union`—we have no idea what type of animal `struct` is in use within it.

But that’s OK! Because on line 31 we check the type to see if it’s an antelope or an octopus. And then we can look at the proper `struct` to get the members.

It’s definitely possible to get this same effect using just `struct`s, but you can do it this way if you want the memory-saving effects of a `union`.

## 20.10 Unions and Unnamed Structs

You know how you can have an unnamed `struct`, like this:
    
    
    [](structs-ii-more-fun-with-structs.html#cb472-1)struct {
    [](structs-ii-more-fun-with-structs.html#cb472-2)    int x, y;
    [](structs-ii-more-fun-with-structs.html#cb472-3)} s;

That defines a variable `s` that is of anonymous `struct` type (because the `struct` has no name tag), with members `x` and `y`.

So things like this are valid:
    
    
    [](structs-ii-more-fun-with-structs.html#cb473-1)s.x = 34;
    [](structs-ii-more-fun-with-structs.html#cb473-2)s.y = 90;
    [](structs-ii-more-fun-with-structs.html#cb473-3)
    [](structs-ii-more-fun-with-structs.html#cb473-4)printf("%d %d\n", s.x, s.y);

Turns out you can drop those unnamed `struct`s in `union`s just like you might expect:
    
    
    [](structs-ii-more-fun-with-structs.html#cb474-1)union foo {
    [](structs-ii-more-fun-with-structs.html#cb474-2)    struct {       // unnamed!
    [](structs-ii-more-fun-with-structs.html#cb474-3)        int x, y;
    [](structs-ii-more-fun-with-structs.html#cb474-4)    } a;
    [](structs-ii-more-fun-with-structs.html#cb474-5)
    [](structs-ii-more-fun-with-structs.html#cb474-6)    struct {       // unnamed!
    [](structs-ii-more-fun-with-structs.html#cb474-7)        int z, w;
    [](structs-ii-more-fun-with-structs.html#cb474-8)    } b;
    [](structs-ii-more-fun-with-structs.html#cb474-9)};

And then access them as per normal:
    
    
    [](structs-ii-more-fun-with-structs.html#cb475-1)union foo f;
    [](structs-ii-more-fun-with-structs.html#cb475-2)
    [](structs-ii-more-fun-with-structs.html#cb475-3)f.a.x = 1;
    [](structs-ii-more-fun-with-structs.html#cb475-4)f.a.y = 2;
    [](structs-ii-more-fun-with-structs.html#cb475-5)f.b.z = 3;
    [](structs-ii-more-fun-with-structs.html#cb475-6)f.b.w = 4;

No problem!

## 20.11 Passing and Returning `struct`s and `union`s

You can pass a `struct` or `union` to a function by value (as opposed to a pointer to it)—a copy of that object to the parameter will be made as if by assignment as per usual.

You can also return a `struct` or `union` from a function and it is also passed by value back.
    
    
    [](structs-ii-more-fun-with-structs.html#cb476-1)#include <stdio.h>
    [](structs-ii-more-fun-with-structs.html#cb476-2)
    [](structs-ii-more-fun-with-structs.html#cb476-3)struct foo {
    [](structs-ii-more-fun-with-structs.html#cb476-4)    int x, y;
    [](structs-ii-more-fun-with-structs.html#cb476-5)};
    [](structs-ii-more-fun-with-structs.html#cb476-6)
    [](structs-ii-more-fun-with-structs.html#cb476-7)struct foo f(void)
    [](structs-ii-more-fun-with-structs.html#cb476-8){
    [](structs-ii-more-fun-with-structs.html#cb476-9)    return (struct foo){.x=34, .y=90};
    [](structs-ii-more-fun-with-structs.html#cb476-10)}
    [](structs-ii-more-fun-with-structs.html#cb476-11)
    [](structs-ii-more-fun-with-structs.html#cb476-12)int main(void)
    [](structs-ii-more-fun-with-structs.html#cb476-13){
    [](structs-ii-more-fun-with-structs.html#cb476-14)    struct foo a = f();  // Copy is made
    [](structs-ii-more-fun-with-structs.html#cb476-15)
    [](structs-ii-more-fun-with-structs.html#cb476-16)    printf("%d %d\n", a.x, a.y);
    [](structs-ii-more-fun-with-structs.html#cb476-17)}

Fun fact: if you do this, you can use the `.` operator right off the function call:
    
    
    [](structs-ii-more-fun-with-structs.html#cb477-16)    printf("%d %d\n", f().x, f().y);

(Of course that example calls the function twice, inefficiently.)

And the same holds true for returning pointers to `struct`s and `union`s—just be sure to use the `->` arrow operator in that case.

* * *

[Prev](the-c-preprocessor.html) | [Contents](index.html) | [Next](characters-and-strings-ii.html)

---

[Prev](structs-ii-more-fun-with-structs.html) | [Contents](index.html) | [Next](enumerated-types-enum.html)

* * *

# 21 Characters and Strings II

We’ve talked about how `char` types are actually just small integer types… but it’s the same for a character in single quotes.

But a string in double quotes is type `const char *`.

Turns out there are few more types of strings and characters, and it leads down one of the most infamous rabbit holes in the language: the whole multibyte/wide/Unicode/localization thingy.

We’re going to peer into that rabbit hole, but not go in. …Yet!

## 21.1 Escape Sequences

We’re used to strings and characters with regular letters, punctuation, and numbers:
    
    
    [](characters-and-strings-ii.html#cb478-1)char *s = "Hello!";
    [](characters-and-strings-ii.html#cb478-2)char t = 'c';

But what if we want some special characters in there that we can’t type on the keyboard because they don’t exist (e.g. “€”), or even if we want a character that’s a single quote? We clearly can’t do this:
    
    
    [](characters-and-strings-ii.html#cb479-1)char t = ''';

To do these things, we use something called _escape sequences_. These are the backslash character (`\`) followed by another character. The two (or more) characters together have special meaning.

For our single quote character example, we can put an escape (that is, `\`) in front of the central single quote to solve it:
    
    
    [](characters-and-strings-ii.html#cb480-1)char t = '\'';

Now C knows that `\'` means just a regular quote we want to print, not the end of the character sequence.

You can say either “backslash” or “escape” in this context (“escape that quote”) and C devs will know what you’re talking about. Also, “escape” in this context is different than your `Esc` key or the ASCII `ESC` code.

### 21.1.1 Frequently-used Escapes

In my humble opinion, these escape characters make up 99.2%[140](function-specifiers-alignment-specifiersoperators.html#fn140) of all escapes.

Code | Description  
---|---  
`\n` | Newline character—when printing, continue subsequent output on the next line  
`\'` | Single quote—used for a single quote character constant  
`\"` | Double quote—used for a double quote in a string literal  
`\\` | Backslash—used for a literal `\` in a string or character  
  
Here are some examples of the escapes and what they output when printed.
    
    
    [](characters-and-strings-ii.html#cb481-1)printf("Use \\n for newline\n");  // Use \n for newline
    [](characters-and-strings-ii.html#cb481-2)printf("Say \"hello\"!\n");       // Say "hello"!
    [](characters-and-strings-ii.html#cb481-3)printf("%c\n", '\'');             // '

### 21.1.2 Rarely-used Escapes

But there are more escapes! You just don’t see these as often.

Code | Description  
---|---  
`\a` | Alert. This makes the terminal make a sound or flash, or both!  
`\b` | Backspace. Moves the cursor back a character. Doesn’t delete the character.  
`\f` | Formfeed. This moves to the next “page”, but that doesn’t have much modern meaning. On my system, this behaves like `\v`.  
`\r` | Return. Move to the beginning of the same line.  
`\t` | Horizontal tab. Moves to the next horizontal tab stop. On my machine, this lines up on columns that are multiples of 8, but YMMV.  
`\v` | Vertical tab. Moves to the next vertical tab stop. On my machine, this moves to the same column on the next line.  
`\?` | Literal question mark. Sometimes you need this to avoid trigraphs, as shown below.  
  
#### 21.1.2.1 Single Line Status Updates

A use case for `\b` or `\r` is to show status updates that appear on the same line on the screen and don’t cause the display to scroll. Here’s an example that does a countdown from 10. (If your compiler doesn’t support threading, you can use the non-standard POSIX function `sleep()` from `<unistd.h>`—if you’re not on a Unix-like, search for your platform and `sleep` for the equivalent.)
    
    
    [](characters-and-strings-ii.html#cb482-1)#include <stdio.h>
    [](characters-and-strings-ii.html#cb482-2)#include <threads.h>
    [](characters-and-strings-ii.html#cb482-3)
    [](characters-and-strings-ii.html#cb482-4)int main(void)
    [](characters-and-strings-ii.html#cb482-5){
    [](characters-and-strings-ii.html#cb482-6)    for (int i = 10; i >= 0; i--) {
    [](characters-and-strings-ii.html#cb482-7)        printf("\rT minus %d second%s... \b", i, i != 1? "s": "");
    [](characters-and-strings-ii.html#cb482-8)
    [](characters-and-strings-ii.html#cb482-9)        fflush(stdout);  // Force output to update
    [](characters-and-strings-ii.html#cb482-10)
    [](characters-and-strings-ii.html#cb482-11)        // Sleep for 1 second
    [](characters-and-strings-ii.html#cb482-12)        thrd_sleep(&(struct timespec){.tv_sec=1}, NULL);
    [](characters-and-strings-ii.html#cb482-13)    }
    [](characters-and-strings-ii.html#cb482-14)
    [](characters-and-strings-ii.html#cb482-15)    printf("\rLiftoff!             \n");
    [](characters-and-strings-ii.html#cb482-16)}

Quite a few things are happening on line 7. First of all, we lead with a `\r` to get us to the beginning of the current line, then we overwrite whatever’s there with the current countdown. (There’s ternary operator out there to make sure we print `1 second` instead of `1 seconds`.)

Also, there’s a space after the `...` That’s so that we properly overwrite the last `.` when `i` drops from `10` to `9` and we get a column narrower. Try it without the space to see what I mean.

And we wrap it up with a `\b` to back up over that space so the cursor sits at the exact end of the line in an aesthetically-pleasing way.

Note that line 15 also has a lot of spaces at the end to overwrite the characters that were already there from the countdown.

Finally, we have a weird `fflush(stdout)` in there, whatever that means. Short answer is that most terminals are _line buffered_ by default, meaning they don’t actually display anything until a newline character is encountered. Since we don’t have a newline (we just have `\r`), without this line, the program would just sit there until `Liftoff!` and then print everything all in one instant. `fflush()` overrides this behavior and forces output to happen _right now_.

#### 21.1.2.2 The Question Mark Escape

Why bother with this? After all, this works just fine:
    
    
    [](characters-and-strings-ii.html#cb483-1)printf("Doesn't it?\n");

And it works fine with the escape, too:
    
    
    [](characters-and-strings-ii.html#cb484-1)printf("Doesn't it\?\n");   // Note \?

So what’s the point??!

Let’s get more emphatic with another question mark and an exclamation point:
    
    
    [](characters-and-strings-ii.html#cb485-1)printf("Doesn't it??!\n");

When I compile this, I get this warning:
    
    
    [](characters-and-strings-ii.html#cb486-1)foo.c: In function ‘main’:
    [](characters-and-strings-ii.html#cb486-2)foo.c:5:23: warning: trigraph ??! converted to | [-Wtrigraphs]
    [](characters-and-strings-ii.html#cb486-3)    5 |     printf("Doesn't it??!\n");
    [](characters-and-strings-ii.html#cb486-4)      |    

And running it gives this unlikely result:
    
    
    [](characters-and-strings-ii.html#cb487-1)Doesn't it|

So _trigraphs_? What the heck is this??!

I’m sure we’ll revisit this dusty corner of the language later, but the short of it is the compiler looks for certain triplets of characters starting with `??` and it substitutes other characters in their place. So if you’re on some ancient terminal without a pipe symbol (`|`) on the keyboard, you can type `??!` instead.

You can fix this by escaping the second question mark, like so:
    
    
    [](characters-and-strings-ii.html#cb488-1)printf("Doesn't it?\?!\n");

And then it compiles and works as-expected.

These days, of course, no one ever uses trigraphs. But that whole `??!` does sometimes appear if you decide to use it in a string for emphasis.

### 21.1.3 Numeric Escapes

In addition, there are ways to specify numeric constants or other character values inside strings or character constants.

If you know an octal or hexadecimal representation of a byte, you can include that in a string or character constant.

The following table has example numbers, but any hex or octal numbers may be used. Pad with leading zeros if necessary to read the proper digit count.

Code | Description  
---|---  
`\123` | Embed the byte with octal value `123`, 3 digits exactly.  
`\x4D` | Embed the byte with hex value `4D`, 2 digits.  
`\u2620` | Embed the Unicode character at code point with hex value `2620`, 4 digits.  
`\U0001243F` | Embed the Unicode character at code point with hex value `1243F`, 8 digits.  
  
Here’s an example of the less-commonly used octal notation to represent the letter `B` in between `A` and `C`. Normally this would be used for some kind of special unprintable character, but we have other ways to do that, below, and this is just an octal demo:
    
    
    [](characters-and-strings-ii.html#cb489-1)printf("A\102C\n");  // 102 is `B` in ASCII/UTF-8

Note there’s no leading zero on the octal number when you include it this way. But it does need to be three characters, so pad with leading zeros if you need to.

But far more common is to use hex constants these days. Here’s a demo that you shouldn’t use, but it demos embedding the UTF-8 bytes 0xE2, 0x80, and 0xA2 in a string, which corresponds to the Unicode “bullet” character (•).
    
    
    [](characters-and-strings-ii.html#cb490-1)printf("\xE2\x80\xA2 Bullet 1\n");
    [](characters-and-strings-ii.html#cb490-2)printf("\xE2\x80\xA2 Bullet 2\n");
    [](characters-and-strings-ii.html#cb490-3)printf("\xE2\x80\xA2 Bullet 3\n");

Produces the following output if you’re on a UTF-8 console (or probably garbage if you’re not):
    
    
    [](characters-and-strings-ii.html#cb491-1)• Bullet 1
    [](characters-and-strings-ii.html#cb491-2)• Bullet 2
    [](characters-and-strings-ii.html#cb491-3)• Bullet 3

But that’s a crummy way to do Unicode. You can use the escapes `\u` (16-bit) or `\U` (32-bit) to just refer to Unicode by code point number. The bullet is `2022` (hex) in Unicode, so you can do this and get more portable results:
    
    
    [](characters-and-strings-ii.html#cb492-1)printf("\u2022 Bullet 1\n");
    [](characters-and-strings-ii.html#cb492-2)printf("\u2022 Bullet 2\n");
    [](characters-and-strings-ii.html#cb492-3)printf("\u2022 Bullet 3\n");

Be sure to pad `\u` with enough leading zeros to get to four characters, and `\U` with enough to get to eight.

For example, that bullet could be done with `\U` and four leading zeros:
    
    
    [](characters-and-strings-ii.html#cb493-1)printf("\U00002022 Bullet 1\n");

But who has time to be that verbose?

* * *

[Prev](structs-ii-more-fun-with-structs.html) | [Contents](index.html) | [Next](enumerated-types-enum.html)

---

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

---

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

---

[Prev](pointers-iii-pointers-to-pointers-and-more.html) | [Contents](index.html) | [Next](variadic-functions.html)

* * *

# 24 Bitwise Operations

These numeric operations effectively allow you to manipulate individual bits in variables, fitting since C is such a low-level langauge[152](function-specifiers-alignment-specifiersoperators.html#fn152).

If you’re not familiar with bitwise operations, [Wikipedia has a good bitwise article](https://en.wikipedia.org/wiki/Bitwise_operation)[153](function-specifiers-alignment-specifiersoperators.html#fn153).

## 24.1 Bitwise AND, OR, XOR, and NOT

For each of these, the [usual arithmetic conversions](types-iii-conversions.html#usual-arithmetic-conversions) take place on the operands (which in this case must be an integer type), and then the appropriate bitwise operation is performed.

Operation | Operator | Example  
---|---|---  
AND | `&` | `a = b & c`  
OR | `|` | `a = b | c`  
XOR | `^` | `a = b ^ c`  
NOT | `~` | `a = ~c`  
  
Note how they’re similar to the Boolean operators `&&` and `||`.

These have assignment shorthand variants similar to `+=` and `-=`:

Operator | Example | Longhand equivalent  
---|---|---  
`&=` | `a &= c` | `a = a & c`  
`|=` | `a |= c` | `a = a | c`  
`^=` | `a ^= c` | `a = a ^ c`  
  
## 24.2 Bitwise Shift

For these, the [integer promotions](types-iii-conversions.html#integer-promotions) are performed on each operand (which must be an integer type) and then a bitwise shift is executed. The type of the result is the type of the promoted left operand.

New bits are filled with zeros, with a possible exception noted in the implementation-defined behavior, below.

Operation | Operator | Example  
---|---|---  
Shift left | `<<` | `a = b << c`  
Shift right | `>>` | `a = b >> c`  
  
There’s also the same similar shorthand for shifting:

Operator | Example | Longhand equivalent  
---|---|---  
`>>=` | `a >>= c` | `a = a >> c`  
`<<=` | `a <<= c` | `a = a << c`  
  
Watch for undefined behavior: no negative shifts, and no shifts that are larger than the size of the promoted left operand.

Also watch for implementation-defined behavior: if you right-shift a negative number, the results are implementation-defined. (It’s perfectly fine to right-shift a signed `int`, just make sure it’s positive.)

* * *

[Prev](pointers-iii-pointers-to-pointers-and-more.html) | [Contents](index.html) | [Next](variadic-functions.html)

---

[Prev](bitwise-operations.html) | [Contents](index.html) | [Next](locale-and-internationalization.html)

* * *

# 25 Variadic Functions

_Variadic_ is a fancy word for functions that take arbitrary numbers of arguments.

A regular function takes a specific number of arguments, for example:
    
    
    [](variadic-functions.html#cb530-1)int add(int x, int y)
    [](variadic-functions.html#cb530-2){
    [](variadic-functions.html#cb530-3)    return x + y;
    [](variadic-functions.html#cb530-4)}

You can only call that with exactly two arguments which correspond to parameters `x` and `y`.
    
    
    [](variadic-functions.html#cb531-1)add(2, 3);
    [](variadic-functions.html#cb531-2)add(5, 12);

But if you try it with more, the compiler won’t let you:
    
    
    [](variadic-functions.html#cb532-1)add(2, 3, 4);  // ERROR
    [](variadic-functions.html#cb532-2)add(5);        // ERROR

Variadic functions get around this limitation to a certain extent.

We’ve already seen a famous example in `printf()`! You can pass all kinds of things to it.
    
    
    [](variadic-functions.html#cb533-1)printf("Hello, world!\n");
    [](variadic-functions.html#cb533-2)printf("The number is %d\n", 2);
    [](variadic-functions.html#cb533-3)printf("The number is %d and pi is %f\n", 2, 3.14159);

It seems to not care how many arguments you give it!

Well, that’s not entirely true. Zero arguments will give you an error:
    
    
    [](variadic-functions.html#cb534-1)printf();  // ERROR

This leads us to one of the limitations of variadic functions in C: they must have at least one argument.

But aside from that, they’re pretty flexible, even allows arguments to have different types just like `printf()` does.

Let’s see how they work!

## 25.1 Ellipses in Function Signatures

So how does it work, syntactically?

What you do is put all the arguments that _must_ be passed first (and remember there has to be at least one) and after that, you put `...`. Just like this:
    
    
    [](variadic-functions.html#cb535-1)void func(int a, ...)   // Literally 3 dots here

Here’s some code to demo that:
    
    
    [](variadic-functions.html#cb536-1)#include <stdio.h>
    [](variadic-functions.html#cb536-2)
    [](variadic-functions.html#cb536-3)void func(int a, ...)
    [](variadic-functions.html#cb536-4){
    [](variadic-functions.html#cb536-5)    printf("a is %d\n", a);  // Prints "a is 2"
    [](variadic-functions.html#cb536-6)}
    [](variadic-functions.html#cb536-7)
    [](variadic-functions.html#cb536-8)int main(void)
    [](variadic-functions.html#cb536-9){
    [](variadic-functions.html#cb536-10)    func(2, 3, 4, 5, 6);
    [](variadic-functions.html#cb536-11)}

So, great, we can get that first argument that’s in variable `a`, but what about the rest of the arguments? How do you get to them?

Here’s where the fun begins!

## 25.2 Getting the Extra Arguments

You’re going to want to include `<stdarg.h>` to make any of this work.

First things first, we’re going to use a special variable of type `va_list` (variable argument list) to keep track of which variable we’re accessing at a time.

The idea is that we first start processing arguments with a call to `va_start()`, process each argument in turn with `va_arg()`, and then, when done, wrap it up with `va_end()`.

When you call `va_start()`, you need to pass in the _last named parameter_ (the one just before the `...`) so it knows where to start looking for the additional arguments.

And when you call `va_arg()` to get the next argument, you have to tell it the type of argument to get next.

Here’s a demo that adds together an arbitrary number of integers. The first argument is the number of integers to add together. We’ll make use of that to figure out how many times we have to call `va_arg()`.
    
    
    [](variadic-functions.html#cb537-1)#include <stdio.h>
    [](variadic-functions.html#cb537-2)#include <stdarg.h>
    [](variadic-functions.html#cb537-3)
    [](variadic-functions.html#cb537-4)int add(int count, ...)
    [](variadic-functions.html#cb537-5){
    [](variadic-functions.html#cb537-6)    int total = 0;
    [](variadic-functions.html#cb537-7)    va_list va;
    [](variadic-functions.html#cb537-8)
    [](variadic-functions.html#cb537-9)    va_start(va, count);   // Start with arguments after "count"
    [](variadic-functions.html#cb537-10)
    [](variadic-functions.html#cb537-11)    for (int i = 0; i < count; i++) {
    [](variadic-functions.html#cb537-12)        int n = va_arg(va, int);   // Get the next int
    [](variadic-functions.html#cb537-13)
    [](variadic-functions.html#cb537-14)        total += n;
    [](variadic-functions.html#cb537-15)    }
    [](variadic-functions.html#cb537-16)
    [](variadic-functions.html#cb537-17)    va_end(va);  // All done
    [](variadic-functions.html#cb537-18)
    [](variadic-functions.html#cb537-19)    return total;
    [](variadic-functions.html#cb537-20)}
    [](variadic-functions.html#cb537-21)
    [](variadic-functions.html#cb537-22)int main(void)
    [](variadic-functions.html#cb537-23){
    [](variadic-functions.html#cb537-24)    printf("%d\n", add(4, 6, 2, -4, 17));  // 6 + 2 - 4 + 17 = 21
    [](variadic-functions.html#cb537-25)    printf("%d\n", add(2, 22, 44));        // 22 + 44 = 66
    [](variadic-functions.html#cb537-26)}

(Note that when `printf()` is called, it uses the number of `%d`s (or whatever) in the format string to know how many more arguments there are!)

If the syntax of `va_arg()` is looking strange to you (because of that loose type name floating around in there), you’re not alone. These are implemented with preprocessor macros in order to get all the proper magic in there.

## 25.3 `va_list` Functionality

What is that `va_list` variable we’re using up there? It’s an opaque variable[154](function-specifiers-alignment-specifiersoperators.html#fn154) that holds information about which argument we’re going to get next with `va_arg()`. You see how we just call `va_arg()` over and over? The `va_list` variable is a placeholder that’s keeping track of progress so far.

But we have to initialize that variable to some sensible value. That’s where `va_start()` comes into play.

When we called `va_start(va, count)`, above, we were saying, “Initialize the `va` variable to point to the variable argument _immediately after_ `count`.”

And that’s _why_ we need to have at least one named variable in our argument list[155](function-specifiers-alignment-specifiersoperators.html#fn155).

Once you have that pointer to the initial parameter, you can easily get subsequent argument values by calling `va_arg()` repeatedly. When you do, you have to pass in your `va_list` variable (so it can keep on keeping track of where you are), as well as the type of argument you’re about to copy off.

It’s up to you as a programmer to figure out which type you’re going to pass to `va_arg()`. In the above example, we just did `int`s. But in the case of `printf()`, it uses the format specifier to determine which type to pull off next.

And when you’re done, call `va_end()` to wrap it up. You **must** (the spec says) call this on a particular `va_list` variable before you decide to call either `va_start()` or `va_copy()` on it again. I know we haven’t talked about `va_copy()` yet.

So the standard progression is:

  * `va_start()` to initialize your `va_list` variable
  * Repeatedly `va_arg()` to get the values
  * `va_end()` to deinitialize your `va_list` variable



I also mentioned `va_copy()` up there; it makes a copy of your `va_list` variable in the exact same state. That is, if you haven’t started with `va_arg()` with the source variable, the new one won’t be started, either. If you’ve consumed 5 variables with `va_arg()` so far, the copy will also reflect that.

`va_copy()` can be useful if you need to scan ahead through the arguments but need to also remember your current place.

## 25.4 Library Functions That Use `va_list`s

One of the other uses for these is pretty cool: writing your own custom `printf()` variant. It would be a pain to have to handle all those format specifiers right? All zillion of them?

Luckily, there are `printf()` variants that accept a working `va_list` as an argument. You can use these to wrap up and make your own custom `printf()`s!

These functions start with the letter `v`, such as `vprintf()`, `vfprintf()`, `vsprintf()`, and `vsnprintf()`. Basically all your `printf()` golden oldies except with a `v` in front.

Let’s make a function `my_printf()` that works just like `printf()` except it takes an extra argument up front.
    
    
    [](variadic-functions.html#cb538-1)#include <stdio.h>
    [](variadic-functions.html#cb538-2)#include <stdarg.h>
    [](variadic-functions.html#cb538-3)
    [](variadic-functions.html#cb538-4)int my_printf(int serial, const char *format, ...)
    [](variadic-functions.html#cb538-5){
    [](variadic-functions.html#cb538-6)    va_list va;
    [](variadic-functions.html#cb538-7)    int rv;
    [](variadic-functions.html#cb538-8)
    [](variadic-functions.html#cb538-9)    // Do my custom work
    [](variadic-functions.html#cb538-10)    printf("The serial number is: %d\n", serial);
    [](variadic-functions.html#cb538-11)
    [](variadic-functions.html#cb538-12)    // Then pass the rest off to vprintf()
    [](variadic-functions.html#cb538-13)    va_start(va, format);
    [](variadic-functions.html#cb538-14)    rv = vprintf(format, va);
    [](variadic-functions.html#cb538-15)    va_end(va);
    [](variadic-functions.html#cb538-16)
    [](variadic-functions.html#cb538-17)    return rv;
    [](variadic-functions.html#cb538-18)}
    [](variadic-functions.html#cb538-19)
    [](variadic-functions.html#cb538-20)int main(void)
    [](variadic-functions.html#cb538-21){
    [](variadic-functions.html#cb538-22)    int x = 10;
    [](variadic-functions.html#cb538-23)    float y = 3.2;
    [](variadic-functions.html#cb538-24)
    [](variadic-functions.html#cb538-25)    my_printf(3490, "x is %d, y is %f\n", x, y);
    [](variadic-functions.html#cb538-26)}

See what we did there? On lines 12-14 we started a new `va_list` variable, and then just passed it right into `vprintf()`. And it knows just want to do with it, because it has all the `printf()` smarts built-in.

We still have to call `va_end()` when we’re done, though, so don’t forget that!

## 25.5 Variadic Macro Gotchas

Like I’ve mentioned, `va_start()` and `va_end()` could be macros. One of the consequences of this might be that they could potentially introduce a new local scope. (That is, if `va_start()` has `{` and `va_end()` contains `}`.)

So we need to watch out for potential scoping issues. Take the following example:
    
    
    [](variadic-functions.html#cb539-1)va_start(va, format);          // may contain {
    [](variadic-functions.html#cb539-2)int rv = vprintf(format, va);
    [](variadic-functions.html#cb539-3)va_end(va);                    // may contain }
    [](variadic-functions.html#cb539-4)
    [](variadic-functions.html#cb539-5)return rv;

If `va_start()` opens a new scope, `rv` will be local to that scope and then the `return` statement will fail. But this will insidiously only happen on compilers that happen to do that with the `va` macros.

* * *

[Prev](bitwise-operations.html) | [Contents](index.html) | [Next](locale-and-internationalization.html)

---

[Prev](variadic-functions.html) | [Contents](index.html) | [Next](unicode-wide-characters-and-all-that.html)

* * *

# 26 Locale and Internationalization

_Localization_ is the process of making your app ready to work well in different locales (or countries).

As you might know, not everyone uses the same character for decimal points or for thousands separators… or for currency.

These locales have names, and you can select one to use. For example, a US locale might write a number like:

100,000.00

Whereas in Brazil, the same might be written with the commas and decimal points swapped:

100.000,00

Makes it easier to write your code so it ports to other nationalities with ease!

Well, sort of. Turns out C only has one built-in locale, and it’s limited. The spec really leaves a lot of ambiguity here; it’s hard to be completely portable.

But we’ll do our best!

## 26.1 Setting the Localization, Quick and Dirty

For these calls, include `<locale.h>`.

There is basically one thing you can portably do here in terms of declaring a specific locale. This is likely what you want to do if you’re going to do locale anything:
    
    
    [](locale-and-internationalization.html#cb540-1)setlocale(LC_ALL, "");  // Use this environment's locale for everything

You’ll want to call that so that the program gets initialized with your current locale.

Getting into more details, there is one more thing you can do and stay portable:
    
    
    [](locale-and-internationalization.html#cb541-1)setlocale(LC_ALL, "C");  // Use the default C locale

but that’s called by default every time your program starts, so there’s not much need to do it yourself.

In that second string, you can specify any locale supported by your system. This is completely system-dependent, so it will vary. On my system, I can specify this:
    
    
    [](locale-and-internationalization.html#cb542-1)setlocale(LC_ALL, "en_US.UTF-8");  // Non-portable!

And that’ll work. But it’s only portable to systems which have that exact same name for that exact same locale, and you can’t guarantee it.

By passing in an empty string (`""`) for the second argument, you’re telling C, “Hey, figure out what the current locale on this system is so I don’t have to tell you.”

## 26.2 Getting the Monetary Locale Settings

Because moving green pieces of paper around promises to be the key to happiness[156](function-specifiers-alignment-specifiersoperators.html#fn156), let’s talk about monetary locale. When you’re writing portable code, you have to know what to type for cash, right? Whether that’s “$”, “€”, “¥”, or “£”.

How can you write that code without going insane? Luckily, once you call `setlocale(LC_ALL, "")`, you can just look these up with a call to `localeconv()`:
    
    
    [](locale-and-internationalization.html#cb543-1)struct lconv *x = localeconv();

This function returns a pointer to a statically-allocated `struct lconv` that has all that juicy information you’re looking for.

Here are the fields of `struct lconv` and their meanings.

First, some conventions. An `_p_` means “positive”, and `_n_` means “negative”, and `int_` means “international”. Though a lot of these are type `char` or `char*`, most (or the strings they point to) are actually treated as integers[157](function-specifiers-alignment-specifiersoperators.html#fn157).

Before we go further, know that `CHAR_MAX` (from `<limits.h>`) is the maximum value that can be held in a `char`. And that many of the following `char` values use that to indicate the value isn’t available in the given locale.

Field | Description  
---|---  
`char *mon_decimal_point` | Decimal pointer character for money, e.g. `"."`.  
`char *mon_thousands_sep` | Thousands separator character for money, e.g. `","`.  
`char *mon_grouping` | Grouping description for money (see below).  
`char *positive_sign` | Positive sign for money, e.g. `"+"` or `""`.  
`char *negative_sign` | Negative sign for money, e.g. `"-"`.  
`char *currency_symbol` | Currency symbol, e.g. `"$"`.  
`char frac_digits` | When printing monetary amounts, how many digits to print past the decimal point, e.g. `2`.  
`char p_cs_precedes` | `1` if the `currency_symbol` comes before the value for a non-negative monetary amount, `0` if after.  
`char n_cs_precedes` | `1` if the `currency_symbol` comes before the value for a negative monetary amount, `0` if after.  
`char p_sep_by_space` | Determines the separation of the `currency symbol` from the value for non-negative amounts (see below).  
`char n_sep_by_space` | Determines the separation of the `currency symbol` from the value for negative amounts (see below).  
`char p_sign_posn` | Determines the `positive_sign` position for non-negative values.  
`char n_sign_posn` | Determines the `positive_sign` position for negative values.  
`char *int_curr_symbol` | International currency symbol, e.g. `"USD "`.  
`char int_frac_digits` | International value for `frac_digits`.  
`char int_p_cs_precedes` | International value for `p_cs_precedes`.  
`char int_n_cs_precedes` | International value for `n_cs_precedes`.  
`char int_p_sep_by_space` | International value for `p_sep_by_space`.  
`char int_n_sep_by_space` | International value for `n_sep_by_space`.  
`char int_p_sign_posn` | International value for `p_sign_posn`.  
`char int_n_sign_posn` | International value for `n_sign_posn`.  
  
### 26.2.1 Monetary Digit Grouping

OK, this is a trippy one. `mon_grouping` is a `char*`, so you might be thinking it’s a string. But in this case, no, it’s really an array of `char`s. It should always end either with a `0` or `CHAR_MAX`.

These values describe how to group sets of numbers in currency to the _left_ of the decimal (the whole number part).

For example, we might have:
    
    
    [](locale-and-internationalization.html#cb544-1)  2   1   0
    [](locale-and-internationalization.html#cb544-2) --- --- ---
    [](locale-and-internationalization.html#cb544-3)$100,000,000.00

These are groups of three. Group 0 (just left of the decimal) has 3 digits. Group 1 (next group to the left) has 3 digits, and the last one also has 3.

So we could describe these groups, from the right (the decimal) to the left with a bunch of integer values representing the group sizes:
    
    
    [](locale-and-internationalization.html#cb545-1)3 3 3

And that would work for values up to $100,000,000.

But what if we had more? We could keep adding `3`s…
    
    
    [](locale-and-internationalization.html#cb546-1)3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3

but that’s crazy. Luckily, we can specify `0` to indicate that the previous group size repeats:
    
    
    [](locale-and-internationalization.html#cb547-1)3 0

Which means to repeat every 3. That would handle $100, $1,000, $10,000, $10,000,000, $100,000,000,000, and so on.

You can go legitimately crazy with these to indicate some weird groupings.

For example:
    
    
    [](locale-and-internationalization.html#cb548-1)4 3 2 1 0

would indicate:
    
    
    [](locale-and-internationalization.html#cb549-1)$1,0,0,0,0,00,000,0000.00

One more value that can occur is `CHAR_MAX`. This indicates that no more grouping should occur, and can appear anywhere in the array, including the first value.
    
    
    [](locale-and-internationalization.html#cb550-1)3 2 CHAR_MAX

would indicate:
    
    
    [](locale-and-internationalization.html#cb551-1)100000000,00,000.00

for example.

And simply having `CHAR_MAX` in the first array position would tell you there was to be no grouping at all.

### 26.2.2 Separators and Sign Position

All the `sep_by_space` variants deal with spacing around the currency sign. Valid values are:

Value | Description  
---|---  
`0` | No space between currency symbol and value.  
`1` | Separate the currency symbol (and sign, if any) from the value with a space.  
`2` | Separate the sign symbol from the currency symbol (if adjacent) with a space, otherwise separate the sign symbol from the value with a space.  
  
The `sign_posn` variants are determined by the following values:

Value | Description  
---|---  
`0` | Put parens around the value and the currency symbol.  
`1` | Put the sign string in front of the currency symbol and value.  
`2` | Put the sign string after the currency symbol and value.  
`3` | Put the sign string directly in front of the currency symbol.  
`4` | Put the sign string directly behind the currency symbol.  
  
### 26.2.3 Example Values

When I get the values on my system, this is what I see (grouping string displayed as individual byte values):
    
    
    [](locale-and-internationalization.html#cb552-1)mon_decimal_point  = "."
    [](locale-and-internationalization.html#cb552-2)mon_thousands_sep  = ","
    [](locale-and-internationalization.html#cb552-3)mon_grouping       = 3 3 0
    [](locale-and-internationalization.html#cb552-4)positive_sign      = ""
    [](locale-and-internationalization.html#cb552-5)negative_sign      = "-"
    [](locale-and-internationalization.html#cb552-6)currency_symbol    = "$"
    [](locale-and-internationalization.html#cb552-7)frac_digits        = 2
    [](locale-and-internationalization.html#cb552-8)p_cs_precedes      = 1
    [](locale-and-internationalization.html#cb552-9)n_cs_precedes      = 1
    [](locale-and-internationalization.html#cb552-10)p_sep_by_space     = 0
    [](locale-and-internationalization.html#cb552-11)n_sep_by_space     = 0
    [](locale-and-internationalization.html#cb552-12)p_sign_posn        = 1
    [](locale-and-internationalization.html#cb552-13)n_sign_posn        = 1
    [](locale-and-internationalization.html#cb552-14)int_curr_symbol    = "USD "
    [](locale-and-internationalization.html#cb552-15)int_frac_digits    = 2
    [](locale-and-internationalization.html#cb552-16)int_p_cs_precedes  = 1
    [](locale-and-internationalization.html#cb552-17)int_n_cs_precedes  = 1
    [](locale-and-internationalization.html#cb552-18)int_p_sep_by_space = 1
    [](locale-and-internationalization.html#cb552-19)int_n_sep_by_space = 1
    [](locale-and-internationalization.html#cb552-20)int_p_sign_posn    = 1
    [](locale-and-internationalization.html#cb552-21)int_n_sign_posn    = 1

## 26.3 Localization Specifics

Notice how we passed the macro `LC_ALL` to `setlocale()` earlier… this hints that there might be some variant that allows you to be more precise about which _parts_ of the locale you’re setting.

Let’s take a look at the values you can see for these:

Macro | Description  
---|---  
`LC_ALL` | Set all of the following to the given locale.  
`LC_COLLATE` | Controls the behavior of the `strcoll()` and `strxfrm()` functions.  
`LC_CTYPE` | Controls the behavior of the character-handling functions[158](function-specifiers-alignment-specifiersoperators.html#fn158).  
`LC_MONETARY` | Controls the values returned by `localeconv()`.  
`LC_NUMERIC` | Controls the decimal point for the `printf()` family of functions.  
`LC_TIME` | Controls time formatting of the `strftime()` and `wcsftime()` time and date printing functions.  
  
It’s pretty common to see `LC_ALL` being set, but, hey, at least you have options.

Also I should point out that `LC_CTYPE` is one of the biggies because it ties into wide characters, a significant can of worms that we’ll talk about later.

* * *

[Prev](variadic-functions.html) | [Contents](index.html) | [Next](unicode-wide-characters-and-all-that.html)

---

[Prev](locale-and-internationalization.html) | [Contents](index.html) | [Next](exiting-a-program.html)

* * *

# 27 Unicode, Wide Characters, and All That

Before we begin, note that this is an active area of language development in C as it works to get past some, erm, _growing pains_. Now that C23 has come out, updates here are probable.

Most people are basically interested in the deceptively simple question, “How do I use such-and-such character set in C?” We’ll get to that. But as we’ll see, it might already work on your system. Or you might have to punt to a third-party library.

We’re going to talk about a lot of things this chapter—some are platform agnostic, and some are C-specific.

Let’s get an outline first of what we’re going to look at:

  * Unicode background
  * Character encoding background
  * Source and Execution character Sets
  * Using Unicode and UTF-8
  * Using other character types like `wchar_t`, `char16_t`, and `char32_t`



Let’s dive in!

## 27.1 What is Unicode?

Back in the day, it was popular in the US and much of the world to use a 7-bit or 8-bit encoding for characters in memory. This meant we could have 128 or 256 characters (including non-printable characters) total. That was fine for a US-centric world, but it turns out there are actually other alphabets out there—who knew? Chinese has over 50,000 characters, and that’s not fitting in a byte.

So people came up with all kinds of alternate ways to represent their own custom character sets. And that was fine, but turned into a compatibility nightmare.

To escape it, Unicode was invented. One character set to rule them all. It extends off into infinity (effectively) so we’ll never run out of space for new characters. It has Chinese, Latin, Greek, cuneiform, chess symbols, emojis… just about everything, really! And more is being added all the time!

## 27.2 Code Points

I want to talk about two concepts here. It’s confusing because they’re both numbers… different numbers for the same thing. But bear with me.

Let’s loosely define _code point_ to mean a numeric value representing a character. (Code points can also represent unprintable control characters, but just assume I mean something like the letter “B” or the character “π”.)

Each code point represents a unique character. And each character has a unique numeric code point associated with it.

For example, in Unicode, the numeric value 66 represents “B”, and 960 represents “π”. Other character mappings that aren’t Unicode use different values, potentially, but let’s forget them and concentrate on Unicode, the future!

So that’s one thing: there’s a number that represents each character. In Unicode, these numbers run from 0 to over 1 million.

Got it?

Because we’re about to flip the table a little.

## 27.3 Encoding

If you recall, an 8-bit byte can hold values from 0-255, inclusive. That’s great for “B” which is 66—that fits in a byte. But “π” is 960, and that doesn’t fit in a byte! We need another byte. How do we store all that in memory? Or what about bigger numbers, like 195,024? That’s going to need a number of bytes to hold.

The Big Question: how are these numbers represented in memory? This is what we call the _encoding_ of the characters.

So we have two things: one is the code point which tells us effectively the serial number of a particular character. And we have the encoding which tells us how we’re going to represent that number in memory.

There are plenty of encodings. You can make up your own right now, if you want[159](function-specifiers-alignment-specifiersoperators.html#fn159). But we’re going to look at some really common encodings that are in use with Unicode.

Encoding | Description  
---|---  
UTF-8 | A byte-oriented encoding that uses a variable number of bytes per character. This is the one to use.  
UTF-16 | A 16-bit per character[160](function-specifiers-alignment-specifiersoperators.html#fn160) encoding.  
UTF-32 | A 32-bit per character encoding.  
  
With UTF-16 and UTF-32, the byte order matters, so you might see UTF-16BE for big-endian and UTF-16LE for little-endian. Same for UTF-32. Technically, if unspecified, you should assume big-endian. But since Windows uses UTF-16 extensively and is little-endian, sometimes that is assumed[161](function-specifiers-alignment-specifiersoperators.html#fn161).

Let’s look at some examples. I’m going to write the values in hex because that’s exactly two digits per 8-bit byte, and it makes it easier to see how things are arranged in memory.

Character | Code Point | UTF-16BE | UTF-32BE | UTF-16LE | UTF-32LE | UTF-8 |   
---|---|---|---|---|---|---|---  
`A` | 41 | 0041 | 00000041 | 4100 | 41000000 | 41 |   
`B` | 42 | 0042 | 00000042 | 4200 | 42000000 | 42 |   
`~` | 7E | 007E | 0000007E | 7E00 | 7E000000 | 7E |   
`π` | 3C0 | 03C0 | 000003C0 | C003 | C0030000 | CF80 |   
`€` | 20AC | 20AC | 000020AC | AC20 | AC200000 | E282AC |   
  
Look in there for the patterns. Note that UTF-16BE and UTF-32BE are simply the code point represented directly as 16- and 32-bit values[162](function-specifiers-alignment-specifiersoperators.html#fn162).

Little-endian is the same, except the bytes are in little-endian order.

Then we have UTF-8 at the end. First you might notice that the single-byte code points are represented as a single byte. That’s nice. You might also notice that different code points take different number of bytes. This is a variable-width encoding.

So as soon as we get above a certain value, UTF-8 starts using additional bytes to store the values. And they don’t appear to correlate with the code point value, either.

[The details of UTF-8 encoding](https://en.wikipedia.org/wiki/UTF-8)[163](function-specifiers-alignment-specifiersoperators.html#fn163) are beyond the scope of this guide, but it’s enough to know that it has a variable number of bytes per code point, and those byte values don’t match up with the code point _except for the first 128 code points_. If you really want to learn more, [Computerphile has a great UTF-8 video with Tom Scott](https://www.youtube.com/watch?v=MijmeoH9LT4)[164](function-specifiers-alignment-specifiersoperators.html#fn164).

That last bit is a neat thing about Unicode and UTF-8 from a North American perspective: it’s backward compatible with 7-bit ASCII encoding! So if you’re used to ASCII, UTF-8 is the same! Every ASCII-encoded document is also UTF-8 encoded! (But not the other way around, obviously.)

It’s probably that last point more than any other that is driving UTF-8 to take over the world.

## 27.4 Source and Execution Character Sets

When programming in C, there are (at least) three character sets that are in play:

  * The one that your code exists on disk as.
  * The one the compiler translates that into just as compilation begins (the _source character set_). This might be the same as the one on disk, or it might not.
  * The one the compiler translates the source character set into for execution (the _execution character set_). This might be the same as the source character set, or it might not.



Your compiler probably has options to select these character sets at build-time.

The basic character set for both source and execution will contain the following characters:
    
    
    [](unicode-wide-characters-and-all-that.html#cb553-1)A B C D E F G H I J K L M
    [](unicode-wide-characters-and-all-that.html#cb553-2)N O P Q R S T U V W X Y Z
    [](unicode-wide-characters-and-all-that.html#cb553-3)a b c d e f g h i j k l m
    [](unicode-wide-characters-and-all-that.html#cb553-4)n o p q r s t u v w x y z
    [](unicode-wide-characters-and-all-that.html#cb553-5)0 1 2 3 4 5 6 7 8 9
    [](unicode-wide-characters-and-all-that.html#cb553-6)! " # % & ' ( ) * + , - . / :
    [](unicode-wide-characters-and-all-that.html#cb553-7); < = > ? [ \ ] ^ _ { | } ~
    [](unicode-wide-characters-and-all-that.html#cb553-8)space tab vertical-tab
    [](unicode-wide-characters-and-all-that.html#cb553-9)form-feed end-of-line

Those are the characters you can use in your source and remain 100% portable.

The execution character set will additionally have characters for alert (bell/flash), backspace, carriage return, and newline.

But most people don’t go to that extreme and freely use their extended character sets in source and executable, especially now that Unicode and UTF-8 are getting more common. I mean, the basic character set doesn’t even allow for `@`, `$`, or ```!

Notably, it’s a pain (though possible with escape sequences) to enter Unicode characters using only the basic character set.

## 27.5 Unicode in C

Before I get into encoding in C, let’s talk about Unicode from a code point standpoint. There is a way in C to specify Unicode characters and these will get translated by the compiler into the execution character set[165](function-specifiers-alignment-specifiersoperators.html#fn165).

So how do we do it?

How about the euro symbol, code point 0x20AC. (I’ve written it in hex because both ways of representing it in C require hex.) How can we put that in our C code?

Use the `\u` escape to put it in a string, e.g. `"\u20AC"` (case for the hex doesn’t matter). You must put **exactly four** hex digits after the `\u`, padding with leading zeros if necessary.

Here’s an example:
    
    
    [](unicode-wide-characters-and-all-that.html#cb554-1)char *s = "\u20AC1.23";
    [](unicode-wide-characters-and-all-that.html#cb554-2)
    [](unicode-wide-characters-and-all-that.html#cb554-3)printf("%s\n", s);  // €1.23

So `\u` works for 16-bit Unicode code points, but what about ones bigger than 16 bits? For that, we need capitals: `\U`.

For example:
    
    
    [](unicode-wide-characters-and-all-that.html#cb555-1)char *s = "\U0001D4D1";
    [](unicode-wide-characters-and-all-that.html#cb555-2)
    [](unicode-wide-characters-and-all-that.html#cb555-3)printf("%s\n", s);  // Prints a mathematical letter "B"

It’s the same as `\u`, just with 32 bits instead of 16. These are equivalent:
    
    
    [](unicode-wide-characters-and-all-that.html#cb556-1)\u03C0
    [](unicode-wide-characters-and-all-that.html#cb556-2)\U000003C0

Again, these are translated into the execution character set during compilation. They represent Unicode code points, not any specific encoding. Furthermore, if a Unicode code point is not representable in the execution character set, the compiler can do whatever it wants with it.

Now, you might wonder why you can’t just do this:
    
    
    [](unicode-wide-characters-and-all-that.html#cb557-1)char *s = "€1.23";
    [](unicode-wide-characters-and-all-that.html#cb557-2)
    [](unicode-wide-characters-and-all-that.html#cb557-3)printf("%s\n", s);  // €1.23

And you probably can, given a modern compiler. The source character set will be translated for you into the execution character set by the compiler. But compilers are free to puke out if they find any characters that aren’t included in their extended character set, and the € symbol certainly isn’t in the basic character set.

Caveat from the spec: you can’t use `\u` or `\U` to encode any code points below 0xA0 except for 0x24 (`$`), 0x40 (`@`), and 0x60 (```)—yes, those are precisely the trio of common punctuation marks missing from the basic character set. Apparently this restriction is relaxed in the upcoming version of the spec.

Finally, you can also use these in identifiers in your code, with some restrictions. But I don’t want to get into that here. We’re all about string handling in this chapter.

And that’s about it for Unicode in C (except encoding).

## 27.6 A Quick Note on UTF-8 Before We Swerve into the Weeds

It could be that your source file on disk, the extended source characters, and the extended execution characters are all in UTF-8 format. And the libraries you use expect UTF-8. This is the glorious future of UTF-8 everywhere.

If that’s the case, and you don’t mind being non-portable to systems that aren’t like that, then just run with it. Stick Unicode characters in your source and data at will. Use regular C strings and be happy.

A lot of things will just work (albeit non-portably) because UTF-8 strings can safely be NUL-terminated just like any other C string. But maybe losing portability in exchange for easier character handling is a tradeoff that’s worth it to you.

There are some caveats, however:

  * Things like `strlen()` report the number of bytes in a string, not the number of characters, necessarily. (The `mbstowcs()` returns the number of characters in a string when you convert it to wide characters. POSIX extends this so you can pass `NULL` for the first argument if you just want the character count.)

  * The following won’t work properly with characters of more than one byte: `strtok()`, `strchr()` (use `strstr()` instead), `strspn()`-type functions, `toupper()`, `tolower()`, `isalpha()`-type functions, and probably more. Beware anything that operates on bytes.

  * `printf()` variants allow for a way to only print so many bytes of a string[166](function-specifiers-alignment-specifiersoperators.html#fn166). You want to make certain you print the correct number of bytes to end on a character boundary.

  * If you want to `malloc()` space for a string, or declare an array of `char`s for one, be aware that the maximum size could be more than you were expecting. Each character could take up to `MB_LEN_MAX` bytes (from `<limits.h>`)—except characters in the basic character set which are guaranteed to be one byte.




And probably others I haven’t discovered. Let me know what pitfalls there are out there…

## 27.7 Different Character Types

I want to introduce more character types. We’re used to `char`, right?

But that’s too easy. Let’s make things a lot more difficult! Yay!

### 27.7.1 Multibyte Characters

First of all, I want to potentially change your thinking about what a string (array of `char`s) is. These are _multibyte strings_ made up of _multibyte characters_.

That’s right—your run-of-the-mill string of characters is multibyte. When someone says “C string”, they mean “C multibyte string”.

Even if a particular character in the string is only a single byte, or if a string is made up of only single characters, it’s known as a multibyte string.

For example:
    
    
    [](unicode-wide-characters-and-all-that.html#cb558-1)char c[128] = "Hello, world!";  // Multibyte string

What we’re saying here is that a particular character that’s not in the basic character set could be composed of multiple bytes. Up to `MB_LEN_MAX` of them (from `<limits.h>`). Sure, it only looks like one character on the screen, but it could be multiple bytes.

You can throw Unicode values in there, as well, as we saw earlier:
    
    
    [](unicode-wide-characters-and-all-that.html#cb559-1)char *s = "\u20AC1.23";
    [](unicode-wide-characters-and-all-that.html#cb559-2)
    [](unicode-wide-characters-and-all-that.html#cb559-3)printf("%s\n", s);  // €1.23

But here we’re getting into some weirdness, because check this out:
    
    
    [](unicode-wide-characters-and-all-that.html#cb560-1)char *s = "\u20AC1.23";  // €1.23
    [](unicode-wide-characters-and-all-that.html#cb560-2)
    [](unicode-wide-characters-and-all-that.html#cb560-3)printf("%zu\n", strlen(s));  // 7!

The string length of `"€1.23"` is `7`?! Yes! Well, on my system, yes! Remember that `strlen()` returns the number of bytes in the string, not the number of characters. (When we get to “wide characters”, coming up, we’ll see a way to get the number of characters in the string.)

Note that while C allows individual multibyte `char` constants (as opposed to `char*`), the behavior of these varies by implementation and your compiler might warn on it.

GCC, for example, warns of multi-character character constants for the following two lines (and, on my system, prints out the UTF-8 encoding):
    
    
    [](unicode-wide-characters-and-all-that.html#cb561-1)printf("%x\n", '€');
    [](unicode-wide-characters-and-all-that.html#cb561-2)printf("%x\n", '\u20ac');

### 27.7.2 Wide Characters

If you’re not a multibyte character, then you’re a _wide character_.

A wide character is a single value that can uniquely represent any character in the current locale. It’s analogous to Unicode code points. But it might not be. Or it might be.

Basically, where multibyte character strings are arrays of bytes, wide character strings are arrays of _characters_. So you can start thinking on a character-by-character basis rather than a byte-by-byte basis (the latter of which gets all messy when characters start taking up variable numbers of bytes).

Wide characters can be represented by a number of types, but the big standout one is `wchar_t`. It’s the main one. It’s like `char`, except wide.

You might be wondering if you can’t tell if it’s Unicode or not, how does that allow you much flexibility in terms of writing code? `wchar_t` opens some of those doors, as there are a rich set of functions you can use to deal with `wchar_t` strings (like getting the length, etc.) without caring about the encoding.

## 27.8 Using Wide Characters and `wchar_t`

Time for a new type: `wchar_t`. This is the main wide character type. Remember how a `char` is only one byte? And a byte’s not enough to represent all characters, potentially? Well, this one is enough.

To use `wchar_t`, include `<wchar.h>`.

How many bytes big is it? Well, it’s not totally clear. Could be 16 bits. Could be 32 bits.

But wait, you’re saying—if it’s only 16 bits, it’s not big enough to hold all the Unicode code points, is it? You’re right—it’s not. The spec doesn’t require it to be. It just has to be able to represent all the characters in the current locale.

This can cause grief with Unicode on platforms with 16-bit `wchar_t`s (ahem—Windows). But that’s out of scope for this guide.

You can declare a string or character of this type with the `L` prefix, and you can print them with the `%ls` (“ell ess”) format specifier. Or print an individual `wchar_t` with `%lc`.
    
    
    [](unicode-wide-characters-and-all-that.html#cb562-1)wchar_t *s = L"Hello, world!";
    [](unicode-wide-characters-and-all-that.html#cb562-2)wchar_t c = L'B';
    [](unicode-wide-characters-and-all-that.html#cb562-3)
    [](unicode-wide-characters-and-all-that.html#cb562-4)printf("%ls %lc\n", s, c);

Now—are those characters stored as Unicode code points, or not? Depends on the implementation. But you can test if they are with the macro `__STDC_ISO_10646__`. If this is defined, the answer is, “It’s Unicode!”

More detailedly, the value in that macro is an integer in the form `yyyymm` that lets you know what Unicode standard you can rely on—whatever was in effect on that date.

But how do you use them?

### 27.8.1 Multibyte to `wchar_t` Conversions

So how do we get from the byte-oriented standard strings to the character-oriented wide strings and back?

We can use a couple string conversion functions to make this happen.

First, some naming conventions you’ll see in these functions:

  * `mb`: multibyte
  * `wc`: wide character
  * `mbs`: multibyte string
  * `wcs`: wide character string



So if we want to convert a multibyte string to a wide character string, we can call the `mbstowcs()`. And the other way around: `wcstombs()`.

Conversion Function | Description  
---|---  
`mbtowc()` | Convert a multibyte character to a wide character.  
`wctomb()` | Convert a wide character to a multibyte character.  
`mbstowcs()` | Convert a multibyte string to a wide string.  
`wcstombs()` | Convert a wide string to a multibyte string.  
  
Let’s do a quick demo where we convert a multibyte string to a wide character string, and compare the string lengths of the two using their respective functions.
    
    
    [](unicode-wide-characters-and-all-that.html#cb563-1)#include <stdio.h>
    [](unicode-wide-characters-and-all-that.html#cb563-2)#include <stdlib.h>
    [](unicode-wide-characters-and-all-that.html#cb563-3)#include <wchar.h>
    [](unicode-wide-characters-and-all-that.html#cb563-4)#include <string.h>
    [](unicode-wide-characters-and-all-that.html#cb563-5)#include <locale.h>
    [](unicode-wide-characters-and-all-that.html#cb563-6)
    [](unicode-wide-characters-and-all-that.html#cb563-7)int main(void)
    [](unicode-wide-characters-and-all-that.html#cb563-8){
    [](unicode-wide-characters-and-all-that.html#cb563-9)    // Get out of the C locale to one that likely has the euro symbol
    [](unicode-wide-characters-and-all-that.html#cb563-10)    setlocale(LC_ALL, "");
    [](unicode-wide-characters-and-all-that.html#cb563-11)
    [](unicode-wide-characters-and-all-that.html#cb563-12)    // Original multibyte string with a euro symbol (Unicode point 20ac)
    [](unicode-wide-characters-and-all-that.html#cb563-13)    char *mb_string = "The cost is \u20ac1.23";  // €1.23
    [](unicode-wide-characters-and-all-that.html#cb563-14)    size_t mb_len = strlen(mb_string);
    [](unicode-wide-characters-and-all-that.html#cb563-15)
    [](unicode-wide-characters-and-all-that.html#cb563-16)    // Wide character array that will hold the converted string
    [](unicode-wide-characters-and-all-that.html#cb563-17)    wchar_t wc_string[128];  // Holds up to 128 wide characters
    [](unicode-wide-characters-and-all-that.html#cb563-18)
    [](unicode-wide-characters-and-all-that.html#cb563-19)    // Convert the MB string to WC; this returns the number of wide chars
    [](unicode-wide-characters-and-all-that.html#cb563-20)    size_t wc_len = mbstowcs(wc_string, mb_string, 128);
    [](unicode-wide-characters-and-all-that.html#cb563-21)
    [](unicode-wide-characters-and-all-that.html#cb563-22)    // Print result--note the %ls for wide char strings
    [](unicode-wide-characters-and-all-that.html#cb563-23)    printf("multibyte: \"%s\" (%zu bytes)\n", mb_string, mb_len);
    [](unicode-wide-characters-and-all-that.html#cb563-24)    printf("wide char: \"%ls\" (%zu characters)\n", wc_string, wc_len);
    [](unicode-wide-characters-and-all-that.html#cb563-25)}

On my system, this outputs:
    
    
    [](unicode-wide-characters-and-all-that.html#cb564-1)multibyte: "The cost is €1.23" (19 bytes)
    [](unicode-wide-characters-and-all-that.html#cb564-2)wide char: "The cost is €1.23" (17 characters)

(Your system might vary on the number of bytes depending on your locale.)

One interesting thing to note is that `mbstowcs()`, in addition to converting the multibyte string to wide, returns the length (in characters) of the wide character string. On POSIX-compliant systems, you can take advantage of a special mode where it _only_ returns the length-in-characters of a given multibyte string: you just pass `NULL` to the destination, and `0` to the maximum number of characters to convert (this value is ignored).

(In the code below, I’m using my extended source character set—you might have to replace those with `\u` escapes.)
    
    
    [](unicode-wide-characters-and-all-that.html#cb565-1)setlocale(LC_ALL, "");
    [](unicode-wide-characters-and-all-that.html#cb565-2)
    [](unicode-wide-characters-and-all-that.html#cb565-3)// The following string has 7 characters
    [](unicode-wide-characters-and-all-that.html#cb565-4)size_t len_in_chars = mbstowcs(NULL, "§¶°±π€•", 0);
    [](unicode-wide-characters-and-all-that.html#cb565-5)
    [](unicode-wide-characters-and-all-that.html#cb565-6)printf("%zu", len_in_chars);  // 7

Again, that’s a non-portable POSIX extension.

And, of course, if you want to convert the other way, it’s `wcstombs()`.

## 27.9 Wide Character Functionality

Once we’re in wide character land, we have all kinds of functionality at our disposal. I’m just going to summarize a bunch of the functions here, but basically what we have here are the wide character versions of the multibyte string functions that we’re used to. (For example, we know `strlen()` for multibyte strings; there’s a `wcslen()` for wide character strings.)

### 27.9.1 `wint_t`

A lot of these functions use a `wint_t` to hold single characters, whether they are passed in or returned.

It is related to `wchar_t` in nature. A `wint_t` is an integer that can represent all values in the extended character set, and also a special end-of-file character, `WEOF`.

This is used by a number of single-character-oriented wide character functions.

### 27.9.2 I/O Stream Orientation

The tl;dr here is to not mix and match byte-oriented functions (like `fprintf()`) with wide-oriented functions (like `fwprintf()`). Decide if a stream will be byte-oriented or wide-oriented and stick with those types of I/O functions.

In more detail: streams can be either byte-oriented or wide-oriented. When a stream is first created, it has no orientation, but the first read or write will set the orientation.

If you first use a wide operation (like `fwprintf()`) it will orient the stream wide.

If you first use a byte operation (like `fprintf()`) it will orient the stream by bytes.

You can manually set an unoriented stream one way or the other with a call to `fwide()`. You can use that same function to get the orientation of a stream.

If you need to change the orientation mid-flight, you can do it with `freopen()`.

### 27.9.3 I/O Functions

Typically include `<stdio.h>` and `<wchar.h>` for these.

I/O Function | Description  
---|---  
`wprintf()` | Formatted console output.  
`wscanf()` | Formatted console input.  
`getwchar()` | Character-based console input.  
`putwchar()` | Character-based console output.  
`fwprintf()` | Formatted file output.  
`fwscanf()` | Formatted file input.  
`fgetwc()` | Character-based file input.  
`fputwc()` | Character-based file output.  
`fgetws()` | String-based file input.  
`fputws()` | String-based file output.  
`swprintf()` | Formatted string output.  
`swscanf()` | Formatted string input.  
`vfwprintf()` | Variadic formatted file output.  
`vfwscanf()` | Variadic formatted file input.  
`vswprintf()` | Variadic formatted string output.  
`vswscanf()` | Variadic formatted string input.  
`vwprintf()` | Variadic formatted console output.  
`vwscanf()` | Variadic formatted console input.  
`ungetwc()` | Push a wide character back on an output stream.  
`fwide()` | Get or set stream multibyte/wide orientation.  
  
### 27.9.4 Type Conversion Functions

Typically include `<wchar.h>` for these.

Conversion Function | Description  
---|---  
`wcstod()` | Convert string to `double`.  
`wcstof()` | Convert string to `float`.  
`wcstold()` | Convert string to `long double`.  
`wcstol()` | Convert string to `long`.  
`wcstoll()` | Convert string to `long long`.  
`wcstoul()` | Convert string to `unsigned long`.  
`wcstoull()` | Convert string to `unsigned long long`.  
  
### 27.9.5 String and Memory Copying Functions

Typically include `<wchar.h>` for these.

Copying Function | Description  
---|---  
`wcscpy()` | Copy string.  
`wcsncpy()` | Copy string, length-limited.  
`wmemcpy()` | Copy memory.  
`wmemmove()` | Copy potentially-overlapping memory.  
`wcscat()` | Concatenate strings.  
`wcsncat()` | Concatenate strings, length-limited.  
  
### 27.9.6 String and Memory Comparing Functions

Typically include `<wchar.h>` for these.

Comparing Function | Description  
---|---  
`wcscmp()` | Compare strings lexicographically.  
`wcsncmp()` | Compare strings lexicographically, length-limited.  
`wcscoll()` | Compare strings in dictionary order by locale.  
`wmemcmp()` | Compare memory lexicographically.  
`wcsxfrm()` | Transform strings into versions such that `wcscmp()` behaves like `wcscoll()`[167](function-specifiers-alignment-specifiersoperators.html#fn167).  
  
### 27.9.7 String Searching Functions

Typically include `<wchar.h>` for these.

Searching Function | Description  
---|---  
`wcschr()` | Find a character in a string.  
`wcsrchr()` | Find a character in a string from the back.  
`wmemchr()` | Find a character in memory.  
`wcsstr()` | Find a substring in a string.  
`wcspbrk()` | Find any of a set of characters in a string.  
`wcsspn()` | Find length of substring including any of a set of characters.  
`wcscspn()` | Find length of substring before any of a set of characters.  
`wcstok()` | Find tokens in a string.  
  
### 27.9.8 Length/Miscellaneous Functions

Typically include `<wchar.h>` for these.

Length/Misc Function | Description  
---|---  
`wcslen()` | Return the length of the string.  
`wmemset()` | Set characters in memory.  
`wcsftime()` | Formatted date and time output.  
  
### 27.9.9 Character Classification Functions

Include `<wctype.h>` for these.

Length/Misc Function | Description  
---|---  
`iswalnum()` | True if the character is alphanumeric.  
`iswalpha()` | True if the character is alphabetic.  
`iswblank()` | True if the character is blank (space-ish, but not a newline).  
`iswcntrl()` | True if the character is a control character.  
`iswdigit()` | True if the character is a digit.  
`iswgraph()` | True if the character is printable (except space).  
`iswlower()` | True if the character is lowercase.  
`iswprint()` | True if the character is printable (including space).  
`iswpunct()` | True if the character is punctuation.  
`iswspace()` | True if the character is whitespace.  
`iswupper()` | True if the character is uppercase.  
`iswxdigit()` | True if the character is a hex digit.  
`towlower()` | Convert character to lowercase.  
`towupper()` | Convert character to uppercase.  
  
## 27.10 Parse State, Restartable Functions

We’re going to get a little bit into the guts of multibyte conversion, but this is a good thing to understand, conceptually.

Imagine how your program takes a sequence of multibyte characters and turns them into wide characters, or vice-versa. It might, at some point, be partway through parsing a character, or it might have to wait for more bytes before it makes the determination of the final value.

This parse state is stored in an opaque variable of type `mbstate_t` and is used every time conversion is performed. That’s how the conversion functions keep track of where they are mid-work.

And if you change to a different character sequence mid-stream, or try to seek to a different place in your input sequence, it could get confused over that.

Now you might want to call me on this one: we just did some conversions, above, and I never mentioned any `mbstate_t` anywhere.

That’s because the conversion functions like `mbstowcs()`, `wctomb()`, etc. each have their own `mbstate_t` variable that they use. There’s only one per function, though, so if you’re writing multithreaded code, they’re not safe to use.

Fortunately, C defines _restartable_ versions of these functions where you can pass in your own `mbstate_t` on per-thread basis if you need to. If you’re doing multithreaded stuff, use these!

Quick note on initializing an `mbstate_t` variable: just `memset()` it to zero. There is no built-in function to force it to be initialized.
    
    
    [](unicode-wide-characters-and-all-that.html#cb566-1)mbstate_t mbs;
    [](unicode-wide-characters-and-all-that.html#cb566-2)
    [](unicode-wide-characters-and-all-that.html#cb566-3)// Set the state to the initial state
    [](unicode-wide-characters-and-all-that.html#cb566-4)memset(&mbs, 0, sizeof mbs);

Here is a list of the restartable conversion functions—note the naming convension of putting an “`r`” after the “from” type:

  * `mbrtowc()`—multibyte to wide character
  * `wcrtomb()`—wide character to multibyte
  * `mbsrtowcs()`—multibyte string to wide character string
  * `wcsrtombs()`—wide character string to multibyte string



These are really similar to their non-restartable counterparts, except they require you pass in a pointer to your own `mbstate_t` variable. And also they modify the source string pointer (to help you out if invalid bytes are found), so it might be useful to save a copy of the original.

Here’s the example from earlier in the chapter reworked to pass in our own `mbstate_t`.
    
    
    [](unicode-wide-characters-and-all-that.html#cb567-1)#include <stdio.h>
    [](unicode-wide-characters-and-all-that.html#cb567-2)#include <stdlib.h>
    [](unicode-wide-characters-and-all-that.html#cb567-3)#include <stddef.h>
    [](unicode-wide-characters-and-all-that.html#cb567-4)#include <wchar.h>
    [](unicode-wide-characters-and-all-that.html#cb567-5)#include <string.h>
    [](unicode-wide-characters-and-all-that.html#cb567-6)#include <locale.h>
    [](unicode-wide-characters-and-all-that.html#cb567-7)
    [](unicode-wide-characters-and-all-that.html#cb567-8)int main(void)
    [](unicode-wide-characters-and-all-that.html#cb567-9){
    [](unicode-wide-characters-and-all-that.html#cb567-10)    // Get out of the C locale to one that likely has the euro symbol
    [](unicode-wide-characters-and-all-that.html#cb567-11)    setlocale(LC_ALL, "");
    [](unicode-wide-characters-and-all-that.html#cb567-12)
    [](unicode-wide-characters-and-all-that.html#cb567-13)    // Original multibyte string with a euro symbol (Unicode point 20ac)
    [](unicode-wide-characters-and-all-that.html#cb567-14)    char *mb_string = "The cost is \u20ac1.23";  // €1.23
    [](unicode-wide-characters-and-all-that.html#cb567-15)    size_t mb_len = strlen(mb_string);
    [](unicode-wide-characters-and-all-that.html#cb567-16)
    [](unicode-wide-characters-and-all-that.html#cb567-17)    // Wide character array that will hold the converted string
    [](unicode-wide-characters-and-all-that.html#cb567-18)    wchar_t wc_string[128];  // Holds up to 128 wide characters
    [](unicode-wide-characters-and-all-that.html#cb567-19)
    [](unicode-wide-characters-and-all-that.html#cb567-20)    // Set up the conversion state
    [](unicode-wide-characters-and-all-that.html#cb567-21)    mbstate_t mbs;
    [](unicode-wide-characters-and-all-that.html#cb567-22)    memset(&mbs, 0, sizeof mbs);  // Initial state
    [](unicode-wide-characters-and-all-that.html#cb567-23)
    [](unicode-wide-characters-and-all-that.html#cb567-24)    // mbsrtowcs() modifies the input pointer to point at the first
    [](unicode-wide-characters-and-all-that.html#cb567-25)    // invalid character, or NULL if successful. Let's make a copy of
    [](unicode-wide-characters-and-all-that.html#cb567-26)    // the pointer for mbsrtowcs() to mess with so our original is
    [](unicode-wide-characters-and-all-that.html#cb567-27)    // unchanged.
    [](unicode-wide-characters-and-all-that.html#cb567-28)    //
    [](unicode-wide-characters-and-all-that.html#cb567-29)    // This example will probably be successful, but we check farther
    [](unicode-wide-characters-and-all-that.html#cb567-30)    // down to see.
    [](unicode-wide-characters-and-all-that.html#cb567-31)    const char *invalid = mb_string;
    [](unicode-wide-characters-and-all-that.html#cb567-32)
    [](unicode-wide-characters-and-all-that.html#cb567-33)    // Convert the MB string to WC; this returns the number of wide chars
    [](unicode-wide-characters-and-all-that.html#cb567-34)    size_t wc_len = mbsrtowcs(wc_string, &invalid, 128, &mbs);
    [](unicode-wide-characters-and-all-that.html#cb567-35)
    [](unicode-wide-characters-and-all-that.html#cb567-36)    if (invalid == NULL) {
    [](unicode-wide-characters-and-all-that.html#cb567-37)        printf("No invalid characters found\n");
    [](unicode-wide-characters-and-all-that.html#cb567-38)
    [](unicode-wide-characters-and-all-that.html#cb567-39)        // Print result--note the %ls for wide char strings
    [](unicode-wide-characters-and-all-that.html#cb567-40)        printf("multibyte: \"%s\" (%zu bytes)\n", mb_string, mb_len);
    [](unicode-wide-characters-and-all-that.html#cb567-41)        printf("wide char: \"%ls\" (%zu characters)\n", wc_string, wc_len);
    [](unicode-wide-characters-and-all-that.html#cb567-42)    } else {
    [](unicode-wide-characters-and-all-that.html#cb567-43)        ptrdiff_t offset = invalid - mb_string;
    [](unicode-wide-characters-and-all-that.html#cb567-44)        printf("Invalid character at offset %td\n", offset);
    [](unicode-wide-characters-and-all-that.html#cb567-45)    }
    [](unicode-wide-characters-and-all-that.html#cb567-46)}

For the conversion functions that manage their own state, you can reset their internal state to the initial one by passing in `NULL` for their `char*` arguments, for example:
    
    
    [](unicode-wide-characters-and-all-that.html#cb568-1)mbstowcs(NULL, NULL, 0);   // Reset the parse state for mbstowcs()
    [](unicode-wide-characters-and-all-that.html#cb568-2)mbstowcs(dest, src, 100);  // Parse some stuff

For I/O, each wide stream manages its own `mbstate_t` and uses that for input and output conversions as it goes.

And some of the byte-oriented I/O functions like `printf()` and `scanf()` keep their own internal state while doing their work.

Finally, these restartable conversion functions do actually have their own internal state if you pass in `NULL` for the `mbstate_t` parameter. This makes them behave more like their non-restartable counterparts.

## 27.11 Unicode Encodings and C

In this section, we’ll see what C can (and can’t) do when it comes to three specific Unicode encodings: UTF-8, UTF-16, and UTF-32.

### 27.11.1 UTF-8

To refresh before this section, read the [UTF-8 quick note, above](unicode-wide-characters-and-all-that.html#utf8-quick).

Aside from that, what are C’s UTF-8 capabilities?

Well, not much, unfortunately.

You can tell C that you specifically want a string literal to be UTF-8 encoded, and it’ll do it for you. You can prefix a string with `u8`:
    
    
    [](unicode-wide-characters-and-all-that.html#cb569-1)char *s = u8"Hello, world!";
    [](unicode-wide-characters-and-all-that.html#cb569-2)
    [](unicode-wide-characters-and-all-that.html#cb569-3)printf("%s\n", s);   // Hello, world!--if you can output UTF-8

Now, can you put Unicode characters in there?
    
    
    [](unicode-wide-characters-and-all-that.html#cb570-1)char *s = u8"€123";

Sure! If the extended source character set supports it. (gcc does.)

What if it doesn’t? You can specify a Unicode code point with your friendly neighborhood `\u` and `\U`, [as noted above](unicode-wide-characters-and-all-that.html#unicode-in-c).

But that’s about it. There’s no portable way in the standard library to take arbirary input and turn it into UTF-8 unless your locale is UTF-8. Or to parse UTF-8 unless your locale is UTF-8.

So if you want to do it, either be in a UTF-8 locale and:
    
    
    [](unicode-wide-characters-and-all-that.html#cb571-1)setlocale(LC_ALL, "");

or figure out a UTF-8 locale name on your local machine and set it explicitly like so:
    
    
    [](unicode-wide-characters-and-all-that.html#cb572-1)setlocale(LC_ALL, "en_US.UTF-8");  // Non-portable name

Or use a [third-party library](unicode-wide-characters-and-all-that.html#utf-3rd-party).

### 27.11.2 UTF-16, UTF-32, `char16_t`, and `char32_t`

`char16_t` and `char32_t` are a couple other potentially wide character types with sizes of 16 bits and 32 bits, respectively. Not necessarily wide, because if they can’t represent every character in the current locale, they lose their wide character nature. But the spec refers them as “wide character” types all over the place, so there we are.

These are here to make things a little more Unicode-friendly, potentially.

To use, include `<uchar.h>`. (That’s “u”, not “w”.)

This header file doesn’t exist on OS X—bummer. If you just want the types, you can:
    
    
    [](unicode-wide-characters-and-all-that.html#cb573-1)#include <stdint.h>
    [](unicode-wide-characters-and-all-that.html#cb573-2)
    [](unicode-wide-characters-and-all-that.html#cb573-3)typedef int_least16_t char16_t;
    [](unicode-wide-characters-and-all-that.html#cb573-4)typedef int_least32_t char32_t;

But if you also want the functions, that’s all on you.

Assuming you’re still good to go, you can declare a string or character of these types with the `u` and `U` prefixes:
    
    
    [](unicode-wide-characters-and-all-that.html#cb574-1)char16_t *s = u"Hello, world!";
    [](unicode-wide-characters-and-all-that.html#cb574-2)char16_t c = u'B';
    [](unicode-wide-characters-and-all-that.html#cb574-3)
    [](unicode-wide-characters-and-all-that.html#cb574-4)char32_t *t = U"Hello, world!";
    [](unicode-wide-characters-and-all-that.html#cb574-5)char32_t d = U'B';

Now—are values in these stored in UTF-16 or UTF-32? Depends on the implementation.

But you can test to see if they are. If the macros `__STDC_UTF_16__` or `__STDC_UTF_32__` are defined (to `1`) it means the types hold UTF-16 or UTF-32, respectively.

If you’re curious, and I know you are, the values, if UTF-16 or UTF-32, are stored in the native endianess. That is, you should be able to compare them straight up to Unicode code point values:
    
    
    [](unicode-wide-characters-and-all-that.html#cb575-1)char16_t pi = u"\u03C0";  // pi symbol
    [](unicode-wide-characters-and-all-that.html#cb575-2)
    [](unicode-wide-characters-and-all-that.html#cb575-3)#if __STDC_UTF_16__
    [](unicode-wide-characters-and-all-that.html#cb575-4)pi == 0x3C0;  // Always true
    [](unicode-wide-characters-and-all-that.html#cb575-5)#else
    [](unicode-wide-characters-and-all-that.html#cb575-6)pi == 0x3C0;  // Probably not true
    [](unicode-wide-characters-and-all-that.html#cb575-7)#endif

### 27.11.3 Multibyte Conversions

You can convert from your multibyte encoding to `char16_t` or `char32_t` with a number of helper functions.

(Like I said, though, the result might not be UTF-16 or UTF-32 unless the corresponding macro is set to `1`.)

All of these functions are restartable (i.e. you pass in your own `mbstate_t`), and all of them operate character by character[168](function-specifiers-alignment-specifiersoperators.html#fn168).

Conversion Function | Description  
---|---  
`mbrtoc16()` | Convert a multibyte character to a `char16_t` character.  
`mbrtoc32()` | Convert a multibyte character to a `char32_t` character.  
`c16rtomb()` | Convert a `char16_t` character to a multibyte character.  
`c32rtomb()` | Convert a `char32_t` character to a multibyte character.  
  
### 27.11.4 Third-Party Libraries

For heavy-duty conversion between different specific encodings, there are a couple mature libraries worth checking out. Note that I haven’t used either of these.

  * [iconv](https://en.wikipedia.org/wiki/Iconv)[169](function-specifiers-alignment-specifiersoperators.html#fn169)—Internationalization Conversion, a common POSIX-standard API available on the major platforms.
  * [ICU](http://site.icu-project.org/)[170](function-specifiers-alignment-specifiersoperators.html#fn170)—International Components for Unicode. At least one blogger found this easy to use.



If you have more noteworthy libraries, let me know.

* * *

[Prev](locale-and-internationalization.html) | [Contents](index.html) | [Next](exiting-a-program.html)

---

[Prev](unicode-wide-characters-and-all-that.html) | [Contents](index.html) | [Next](signal-handling.html)

* * *

# 28 Exiting a Program

Turns out there are a lot of ways to do this, and even ways to set up “hooks” so that a function runs when a program exits.

In this chapter we’ll dive in and check them out.

We already covered the meaning of the exit status code in the [Exit Status](the-outside-environment.html#exit-status) section, so jump back there and review if you have to.

All the functions in this section are in `<stdlib.h>`.

## 28.1 Normal Exits

We’ll start with the regular ways to exit a program, and then jump to some of the rarer, more esoteric ones.

When you exit a program normally, all open I/O streams are flushed and temporary files removed. Basically it’s a nice exit where everything gets cleaned up and handled. It’s what you want to do almost all the time unless you have reasons to do otherwise.

### 28.1.1 Returning From `main()`

If you’ve noticed, `main()` has a return type of `int`… and yet I’ve rarely, if ever, been `return`ing anything from `main()` at all.

This is because for `main()` only (and I can’t stress enough this special case _only_ applies to `main()` and no other functions anywhere) has an _implicit_ `return 0` if you fall off the end.

You can explicitly `return` from `main()` any time you want, and some programmers feel it’s more _Right_ to always have a `return` at the end of `main()`. But if you leave it off, C will put one there for you.

So… here are the `return` rules for `main()`:

  * You can return an exit status from `main()` with a `return` statement. `main()` is the only function with this special behavior. Using `return` in any other function just returns from that function to the caller.
  * If you don’t explicitly `return` and just fall off the end of `main()`, it’s just as if you’d returned `0` or `EXIT_SUCCESS`.



### 28.1.2 `exit()`

This one has also made an appearance a few times. If you call `exit()` from anywhere in your program, it will exit at that point.

The argument you pass to `exit()` is the exit status.

### 28.1.3 Setting Up Exit Handlers with `atexit()`

You can register functions to be called when a program exits whether by returning from `main()` or calling the `exit()` function.

A call to `atexit()` with the handler function name will get it done. You can register multiple exit handlers, and they’ll be called in the reverse order of registration.

Here’s an example:
    
    
    [](exiting-a-program.html#cb576-1)#include <stdio.h>
    [](exiting-a-program.html#cb576-2)#include <stdlib.h>
    [](exiting-a-program.html#cb576-3)
    [](exiting-a-program.html#cb576-4)void on_exit_1(void)
    [](exiting-a-program.html#cb576-5){
    [](exiting-a-program.html#cb576-6)    printf("Exit handler 1 called!\n");
    [](exiting-a-program.html#cb576-7)}
    [](exiting-a-program.html#cb576-8)
    [](exiting-a-program.html#cb576-9)void on_exit_2(void)
    [](exiting-a-program.html#cb576-10){
    [](exiting-a-program.html#cb576-11)    printf("Exit handler 2 called!\n");
    [](exiting-a-program.html#cb576-12)}
    [](exiting-a-program.html#cb576-13)
    [](exiting-a-program.html#cb576-14)int main(void)
    [](exiting-a-program.html#cb576-15){
    [](exiting-a-program.html#cb576-16)    atexit(on_exit_1);
    [](exiting-a-program.html#cb576-17)    atexit(on_exit_2);
    [](exiting-a-program.html#cb576-18)    
    [](exiting-a-program.html#cb576-19)    printf("About to exit...\n");
    [](exiting-a-program.html#cb576-20)}

And the output is:
    
    
    [](exiting-a-program.html#cb577-1)About to exit...
    [](exiting-a-program.html#cb577-2)Exit handler 2 called!
    [](exiting-a-program.html#cb577-3)Exit handler 1 called!

## 28.2 Quicker Exits with `quick_exit()`

This is similar to a normal exit, except:

  * Open files might not be flushed.
  * Temporary files might not be removed.
  * `atexit()` handlers won’t be called.



But there is a way to register exit handlers: call `at_quick_exit()` analogously to how you’d call `atexit()`.
    
    
    [](exiting-a-program.html#cb578-1)#include <stdio.h>
    [](exiting-a-program.html#cb578-2)#include <stdlib.h>
    [](exiting-a-program.html#cb578-3)
    [](exiting-a-program.html#cb578-4)void on_quick_exit_1(void)
    [](exiting-a-program.html#cb578-5){
    [](exiting-a-program.html#cb578-6)    printf("Quick exit handler 1 called!\n");
    [](exiting-a-program.html#cb578-7)}
    [](exiting-a-program.html#cb578-8)
    [](exiting-a-program.html#cb578-9)void on_quick_exit_2(void)
    [](exiting-a-program.html#cb578-10){
    [](exiting-a-program.html#cb578-11)    printf("Quick exit handler 2 called!\n");
    [](exiting-a-program.html#cb578-12)}
    [](exiting-a-program.html#cb578-13)
    [](exiting-a-program.html#cb578-14)void on_exit(void)
    [](exiting-a-program.html#cb578-15){
    [](exiting-a-program.html#cb578-16)    printf("Normal exit--I won't be called!\n");
    [](exiting-a-program.html#cb578-17)}
    [](exiting-a-program.html#cb578-18)
    [](exiting-a-program.html#cb578-19)int main(void)
    [](exiting-a-program.html#cb578-20){
    [](exiting-a-program.html#cb578-21)    at_quick_exit(on_quick_exit_1);
    [](exiting-a-program.html#cb578-22)    at_quick_exit(on_quick_exit_2);
    [](exiting-a-program.html#cb578-23)
    [](exiting-a-program.html#cb578-24)    atexit(on_exit);  // This won't be called
    [](exiting-a-program.html#cb578-25)
    [](exiting-a-program.html#cb578-26)    printf("About to quick exit...\n");
    [](exiting-a-program.html#cb578-27)
    [](exiting-a-program.html#cb578-28)    quick_exit(0);
    [](exiting-a-program.html#cb578-29)}

Which gives this output:
    
    
    [](exiting-a-program.html#cb579-1)About to quick exit...
    [](exiting-a-program.html#cb579-2)Quick exit handler 2 called!
    [](exiting-a-program.html#cb579-3)Quick exit handler 1 called!

It works just like `exit()`/`atexit()`, except for the fact that file flushing and cleanup might not be done.

## 28.3 Nuke it from Orbit: `_Exit()`

Calling `_Exit()` exits immediately, period. No on-exit callback functions are executed. Files won’t be flushed. Temp files won’t be removed.

Use this if you have to exit _right fargin’ now_.

## 28.4 Exiting Sometimes: `assert()`

The `assert()` statement is used to insist that something be true, or else the program will exit.

Devs often use an assert to catch Should-Never-Happen type errors.
    
    
    [](exiting-a-program.html#cb580-1)#define PI 3.14159
    [](exiting-a-program.html#cb580-2)
    [](exiting-a-program.html#cb580-3)assert(PI > 3);   // Sure enough, it is, so carry on

versus:
    
    
    [](exiting-a-program.html#cb581-1)goats -= 100;
    [](exiting-a-program.html#cb581-2)
    [](exiting-a-program.html#cb581-3)assert(goats >= 0);  // Can't have negative goats

In that case, if I try to run it and `goats` falls under `0`, this happens:
    
    
    [](exiting-a-program.html#cb582-1)goat_counter: goat_counter.c:8: main: Assertion `goats >= 0' failed.
    [](exiting-a-program.html#cb582-2)Aborted

and I’m dropped back to the command line.

This isn’t very user-friendly, so it’s only used for things the user will never see. And often people [write their own assert macros that can more easily be turned off](the-c-preprocessor.html#my-assert).

## 28.5 Abnormal Exit: `abort()`

You can use this if something has gone horribly wrong and you want to indicate as much to the outside environment. This also won’t necessarily clean up any open files, etc.

I’ve rarely seen this used.

Some foreshadowing about _signals_ : this actually works by raising a `SIGABRT` which will end the process.

What happens after that is up to the system, but on Unix-likes, it was common to [dump core](https://en.wikipedia.org/wiki/Core_dump)[171](function-specifiers-alignment-specifiersoperators.html#fn171) as the program terminated.

* * *

[Prev](unicode-wide-characters-and-all-that.html) | [Contents](index.html) | [Next](signal-handling.html)

---

[Prev](exiting-a-program.html) | [Contents](index.html) | [Next](variable-length-arrays-vlas.html)

* * *

# 29 Signal Handling

Before we start, I’m just going to advise you to generally ignore this entire chapter and use your OS’s (very likely) superior signal handling functions. Unix-likes have the `sigaction()` family of functions, and Windows has… whatever it does[172](function-specifiers-alignment-specifiersoperators.html#fn172).

With that out of the way, what are signals?

## 29.1 What Are Signals?

A _signal_ is _raised_ on a variety of external events. Your program can be configured to be interrupted to _handle_ the signal, and, optionally, continue where it left off once the signal has been handled.

Think of it like a function that’s automatically called when one of these external events occurs.

What are these events? On your system, there are probably a lot of them, but in the C spec there are just a few:

Signal | Description  
---|---  
`SIGABRT` | Abnormal termination—what happens when `abort()` is called.  
`SIGFPE` | Floating point exception.  
`SIGILL` | Illegal instruction.  
`SIGINT` | Interrupt—usually the result of `CTRL-C` being hit.  
`SIGSEGV` | “Segmentation Violation”: invalid memory access.  
`SIGTERM` | Termination requested.  
  
You can set up your program to ignore, handle, or allow the default action for each of these by using the `signal()` function.

## 29.2 Handling Signals with `signal()`

The `signal()` call takes two parameters: the signal in question, and an action to take when that signal is raised.

The action can be one of three things:

  * A pointer to a handler function.
  * `SIG_IGN` to ignore the signal.
  * `SIG_DFL` to restore the default handler for the signal.



Let’s write a program that you can’t `CTRL-C` out of. (Don’t fret—in the following program, you can also hit `RETURN` and it’ll exit.)
    
    
    [](signal-handling.html#cb583-1)#include <stdio.h>
    [](signal-handling.html#cb583-2)#include <signal.h>
    [](signal-handling.html#cb583-3)
    [](signal-handling.html#cb583-4)int main(void)
    [](signal-handling.html#cb583-5){
    [](signal-handling.html#cb583-6)    char s[1024];
    [](signal-handling.html#cb583-7)
    [](signal-handling.html#cb583-8)    signal(SIGINT, SIG_IGN);    // Ignore SIGINT, caused by ^C
    [](signal-handling.html#cb583-9)
    [](signal-handling.html#cb583-10)    printf("Try hitting ^C... (hit RETURN to exit)\n");
    [](signal-handling.html#cb583-11)
    [](signal-handling.html#cb583-12)    // Wait for a line of input so the program doesn't just exit
    [](signal-handling.html#cb583-13)    fgets(s, sizeof s, stdin);
    [](signal-handling.html#cb583-14)}

Check out line 8—we tell the program to ignore `SIGINT`, the interrupt signal that’s raised when `CTRL-C` is hit. No matter how much you hit it, the signal remains ignored. If you comment out line 8, you’ll see you can `CTRL-C` with impunity and quit the program on the spot.

## 29.3 Writing Signal Handlers

I mentioned you could also write a handler function that gets called when the signal is raised.

These are pretty straightforward, are also very capability-limited when it comes to the spec.

Before we start, let’s look at the function prototype for the `signal()` call:
    
    
    [](signal-handling.html#cb584-1)void (*signal(int sig, void (*func)(int)))(int);

Pretty easy to read, right?

_WRONG!_ `:)`

Let’s take a moment to take it apart for practice.

`signal()` takes two arguments: an integer `sig` representing the signal, and a pointer `func` to the handler (the handler returns `void` and takes an `int` as an argument), highlighted below:
    
    
    [](signal-handling.html#cb585-1)                sig          func
    [](signal-handling.html#cb585-2)              |-----|  |---------------|
    [](signal-handling.html#cb585-3)void (*signal(int sig, void (*func)(int)))(int);

Basically, we’re going to pass in the signal number we’re interested in catching, and we’re going to pass a pointer to a function of the form:
    
    
    [](signal-handling.html#cb586-1)void f(int x);

that will do the actual catching.

Now—what about the rest of that prototype? It’s basically all the return type. See, `signal()` will return whatever you passed as `func` on success… so that means it’s returning a pointer to a function that returns `void` and takes an `int` as an argument.
    
    
    [](signal-handling.html#cb587-1)returned
    [](signal-handling.html#cb587-2)function    indicates we're              and
    [](signal-handling.html#cb587-3)returns     returning a                  that function
    [](signal-handling.html#cb587-4)void        pointer to function          takes an int
    [](signal-handling.html#cb587-5)|--|        |                                   |---|
    [](signal-handling.html#cb587-6)void       (*signal(int sig, void (*func)(int)))(int);

Also, it can return `SIG_ERR` in case of an error.

Let’s do an example where we make it so you have to hit `CTRL-C` twice to exit.

I want to be clear that this program engages in undefined behavior in a couple ways. But it’ll probably work for you, and it’s hard to come up with portable non-trivial demos.
    
    
    [](signal-handling.html#cb588-1)#include <stdio.h>
    [](signal-handling.html#cb588-2)#include <stdlib.h>
    [](signal-handling.html#cb588-3)#include <signal.h>
    [](signal-handling.html#cb588-4)
    [](signal-handling.html#cb588-5)int count = 0;
    [](signal-handling.html#cb588-6)
    [](signal-handling.html#cb588-7)void sigint_handler(int signum)
    [](signal-handling.html#cb588-8){
    [](signal-handling.html#cb588-9)    // The compiler is allowed to run:
    [](signal-handling.html#cb588-10)    //
    [](signal-handling.html#cb588-11)    //   signal(signum, SIG_DFL)
    [](signal-handling.html#cb588-12)    //
    [](signal-handling.html#cb588-13)    // when the handler is called. So we reset the handler here:
    [](signal-handling.html#cb588-14)    signal(SIGINT, sigint_handler);
    [](signal-handling.html#cb588-15)
    [](signal-handling.html#cb588-16)    (void)signum;   // Get rid of unused variable warning
    [](signal-handling.html#cb588-17)
    [](signal-handling.html#cb588-18)    count++;                       // Undefined behavior
    [](signal-handling.html#cb588-19)    printf("Count: %d\n", count);  // Undefined behavior
    [](signal-handling.html#cb588-20)
    [](signal-handling.html#cb588-21)    if (count == 2) {
    [](signal-handling.html#cb588-22)        printf("Exiting!\n");      // Undefined behavior
    [](signal-handling.html#cb588-23)        exit(0);
    [](signal-handling.html#cb588-24)    }
    [](signal-handling.html#cb588-25)}
    [](signal-handling.html#cb588-26)
    [](signal-handling.html#cb588-27)int main(void)
    [](signal-handling.html#cb588-28){
    [](signal-handling.html#cb588-29)    signal(SIGINT, sigint_handler);
    [](signal-handling.html#cb588-30)
    [](signal-handling.html#cb588-31)    printf("Try hitting ^C...\n");
    [](signal-handling.html#cb588-32)
    [](signal-handling.html#cb588-33)    for(;;);  // Wait here forever
    [](signal-handling.html#cb588-34)}

One of the things you’ll notice is that on line 14 we reset the signal handler. This is because C has the option of resetting the signal handler to its `SIG_DFL` behavior before running your custom handler. In other words, it could be a one-off. So we reset it first thing so that we handle it again for the next one.

We’re ignoring the return value from `signal()` in this case. If we’d set it to a different handler earlier, it would return a pointer to that handler, which we could get like this:
    
    
    [](signal-handling.html#cb589-1)// old_handler is type "pointer to function that takes a single
    [](signal-handling.html#cb589-2)// int parameter and returns void":
    [](signal-handling.html#cb589-3)
    [](signal-handling.html#cb589-4)void (*old_handler)(int);
    [](signal-handling.html#cb589-5)
    [](signal-handling.html#cb589-6)old_handler = signal(SIGINT, sigint_handler);

That said, I’m not sure of a common use case for this. But if you need the old handler for some reason, you can get it that way.

Quick note on line 16—that’s just to tell the compiler to not warn that we’re not using this variable. It’s like saying, “I know I’m not using it; you don’t have to warn me.”

And lastly you’ll see that I’ve marked undefined behavior in a couple places. More on that in the next section.

## 29.4 What Can We Actually Do?

Turns out we’re pretty limited in what we can and can’t do in our signal handlers. This is one of the reasons why I say you shouldn’t even bother with this and instead use your OS’s signal handling instead (e.g. `sigaction()` for Unix-like systems).

Wikipedia goes so far as to say the only really portable thing you can do is call `signal()` with `SIG_IGN` or `SIG_DFL` and that’s it.

Here’s what we **can’t** portably do:

  * Call any standard library function. 
    * Like `printf()`, for example.
    * I think it’s probably safe to call restartable/reentrant functions, but the spec doesn’t allow that liberty.
  * Get or set values from a local `static`, file scope, or thread-local variable. 
    * Unless it’s a lock-free atomic object or…
    * You’re assigning into a variable of type `volatile sig_atomic_t`.



That last bit–`sig_atomic_t`–is your ticket to getting data out of a signal handler. (Unless you want to use lock-free atomic objects, which is outside the scope of this section[173](function-specifiers-alignment-specifiersoperators.html#fn173).) It’s an integer type that might or might not be signed. And it’s bounded by what you can put in there.

You can look at the minimum and maximum allowable values in the macros `SIG_ATOMIC_MIN` and `SIG_ATOMIC_MAX`[174](function-specifiers-alignment-specifiersoperators.html#fn174).

Confusingly, the spec also says you can’t refer “to any object with static or thread storage duration that is not a lock-free atomic object other than by assigning a value to an object declared as `volatile sig_atomic_t` […]”

My read on this is that you can’t read or write anything that’s not a lock-free atomic object. Also you can assign to an object that’s `volatile sig_atomic_t`.

But can you read from it? I honestly don’t see why not, except that the spec is very pointed about mentioning assigning into. But if you have to read it and make any kind of decision based on it, you might be opening up room for some kind of race conditions.

With that in mind, we can rewrite our “hit `CTRL-C` twice to exit” code to be a little more portable, albeit less verbose on the output.

Let’s change our `SIGINT` handler to do nothing except increment a value that’s of type `volatile sig_atomic_t`. So it’ll count the number of `CTRL-C`s that have been hit.

Then in our main loop, we’ll check to see if that counter is over `2`, then bail out if it is.
    
    
    [](signal-handling.html#cb590-1)#include <stdio.h>
    [](signal-handling.html#cb590-2)#include <signal.h>
    [](signal-handling.html#cb590-3)
    [](signal-handling.html#cb590-4)volatile sig_atomic_t count = 0;
    [](signal-handling.html#cb590-5)
    [](signal-handling.html#cb590-6)void sigint_handler(int signum)
    [](signal-handling.html#cb590-7){
    [](signal-handling.html#cb590-8)    (void)signum;                    // Unused variable warning
    [](signal-handling.html#cb590-9)
    [](signal-handling.html#cb590-10)    signal(SIGINT, sigint_handler);  // Reset signal handler
    [](signal-handling.html#cb590-11)
    [](signal-handling.html#cb590-12)    count++;                         // Undefined behavior
    [](signal-handling.html#cb590-13)}
    [](signal-handling.html#cb590-14)
    [](signal-handling.html#cb590-15)int main(void)
    [](signal-handling.html#cb590-16){
    [](signal-handling.html#cb590-17)    signal(SIGINT, sigint_handler);
    [](signal-handling.html#cb590-18)
    [](signal-handling.html#cb590-19)    printf("Hit ^C twice to exit.\n");
    [](signal-handling.html#cb590-20)
    [](signal-handling.html#cb590-21)    while(count < 2);
    [](signal-handling.html#cb590-22)}

Undefined behavior again? It’s my read that this is, because we have to read the value in order to increment and store it.

If we only want to postpone the exit by one hitting of `CTRL-C`, we can do that without too much trouble. But any more postponement would require some ridiculous function chaining.

What we’ll do is handle it once, and the handler will reset the signal to its default behavior (that is, to exit):
    
    
    [](signal-handling.html#cb591-1)#include <stdio.h>
    [](signal-handling.html#cb591-2)#include <signal.h>
    [](signal-handling.html#cb591-3)
    [](signal-handling.html#cb591-4)void sigint_handler(int signum)
    [](signal-handling.html#cb591-5){
    [](signal-handling.html#cb591-6)    (void)signum;                      // Unused variable warning
    [](signal-handling.html#cb591-7)    signal(SIGINT, SIG_DFL);           // Reset signal handler
    [](signal-handling.html#cb591-8)}
    [](signal-handling.html#cb591-9)
    [](signal-handling.html#cb591-10)int main(void)
    [](signal-handling.html#cb591-11){
    [](signal-handling.html#cb591-12)    signal(SIGINT, sigint_handler);
    [](signal-handling.html#cb591-13)
    [](signal-handling.html#cb591-14)    printf("Hit ^C twice to exit.\n");
    [](signal-handling.html#cb591-15)
    [](signal-handling.html#cb591-16)    while(1);
    [](signal-handling.html#cb591-17)}

Later when we look at lock-free atomic variables, we’ll see a way to fix the `count` version (assuming lock-free atomic variables are available on your particular system).

This is why at the beginning, I was suggesting checking out your OS’s built-in signal system as a probably-superior alternative.

## 29.5 Friends Don’t Let Friends `signal()`

Again, use your OS’s built-in signal handling or the equivalent. It’s not in the spec, not as portable, but probably is far more capable. Plus your OS probably has a number of signals defined that aren’t in the C spec. And it’s difficult to write portable code using `signal()` anyway.

* * *

[Prev](exiting-a-program.html) | [Contents](index.html) | [Next](variable-length-arrays-vlas.html)

---

[Prev](signal-handling.html) | [Contents](index.html) | [Next](goto.html)

* * *

# 30 Variable-Length Arrays (VLAs)

C provides a way for you to declare an array whose size is determined at runtime. This gives you the benefits of dynamic runtime sizing like you get with `malloc()`, but without needing to worry about `free()`ing the memory after.

Now, a lot of people don’t like VLAs. They’ve been banned from the Linux kernel, for example. We’ll dig into more of that rationale [later](variable-length-arrays-vlas.html#vla-general-issues).

This is an optional feature of the language. The macro `__STDC_NO_VLA__` is set to `1` if VLAs are _not_ present. (They were mandatory in C99, and then became optional in C11.)
    
    
    [](variable-length-arrays-vlas.html#cb592-1)#if __STDC_NO_VLA__ == 1
    [](variable-length-arrays-vlas.html#cb592-2)   #error Sorry, need VLAs for this program!
    [](variable-length-arrays-vlas.html#cb592-3)#endif

But since neither GCC nor Clang bother to define this macro, you may get limited mileage from this.

Let’s dive in first with an example, and then we’ll look for the devil in the details.

## 30.1 The Basics

A normal array is declared with a constant size, like this:
    
    
    [](variable-length-arrays-vlas.html#cb593-1)int v[10];

But with VLAs, we can use a size determined at runtime to set the array, like this:
    
    
    [](variable-length-arrays-vlas.html#cb594-1)int n = 10;
    [](variable-length-arrays-vlas.html#cb594-2)int v[n];

Now, that looks like the same thing, and in many ways is, but this gives you the flexibility to compute the size you need, and then get an array of exactly that size.

Let’s ask the user to input the size of the array, and then store the index-times-10 in each of those array elements:
    
    
    [](variable-length-arrays-vlas.html#cb595-1)#include <stdio.h>
    [](variable-length-arrays-vlas.html#cb595-2)
    [](variable-length-arrays-vlas.html#cb595-3)int main(void)
    [](variable-length-arrays-vlas.html#cb595-4){
    [](variable-length-arrays-vlas.html#cb595-5)    int n;
    [](variable-length-arrays-vlas.html#cb595-6)    char buf[32];
    [](variable-length-arrays-vlas.html#cb595-7)
    [](variable-length-arrays-vlas.html#cb595-8)    printf("Enter a number: "); fflush(stdout);
    [](variable-length-arrays-vlas.html#cb595-9)    fgets(buf, sizeof buf, stdin);
    [](variable-length-arrays-vlas.html#cb595-10)    n = strtoul(buf, NULL, 10);
    [](variable-length-arrays-vlas.html#cb595-11)
    [](variable-length-arrays-vlas.html#cb595-12)    int v[n];
    [](variable-length-arrays-vlas.html#cb595-13)
    [](variable-length-arrays-vlas.html#cb595-14)    for (int i = 0; i < n; i++)
    [](variable-length-arrays-vlas.html#cb595-15)        v[i] = i * 10;
    [](variable-length-arrays-vlas.html#cb595-16)
    [](variable-length-arrays-vlas.html#cb595-17)    for (int i = 0; i < n; i++)
    [](variable-length-arrays-vlas.html#cb595-18)        printf("v[%d] = %d\n", i, v[i]);
    [](variable-length-arrays-vlas.html#cb595-19)}

(On line 7, I have an `fflush()` that should force the line to output even though I don’t have a newline at the end.)

Line 12 is where we declare the VLA—once execution gets past that line, the size of the array is set to whatever `n` was at that moment. The array length can’t be changed later.

You can put an expression in the brackets, as well:
    
    
    [](variable-length-arrays-vlas.html#cb596-1)int v[x * 100];

Some restrictions:

  * You can’t declare a VLA at file scope, and you can’t make a `static` one in block scope[175](function-specifiers-alignment-specifiersoperators.html#fn175).
  * You can’t use an initializer list to initialize the array.



Also, entering a negative value for the size of the array invokes undefined behavior—in this universe, anyway.

## 30.2 `sizeof` and VLAs

We’re used to `sizeof` giving us the size in bytes of any particular object, including arrays. And VLAs are no exception.

The main difference is that `sizeof` on a VLA is executed at _runtime_ , whereas on a non-variably-sized variable it is computed at _compile time_.

But the usage is the same.

You can even compute the number of elements in a VLA with the usual array trick:
    
    
    [](variable-length-arrays-vlas.html#cb597-1)size_t num_elems = sizeof v / sizeof v[0];

There’s a subtle and correct implication from the above line: pointer arithmetic works just like you’d expect for a regular array. So go ahead and use it to your heart’s content:
    
    
    [](variable-length-arrays-vlas.html#cb598-1)#include <stdio.h>
    [](variable-length-arrays-vlas.html#cb598-2)
    [](variable-length-arrays-vlas.html#cb598-3)int main(void)
    [](variable-length-arrays-vlas.html#cb598-4){
    [](variable-length-arrays-vlas.html#cb598-5)    int n = 5;
    [](variable-length-arrays-vlas.html#cb598-6)    int v[n];
    [](variable-length-arrays-vlas.html#cb598-7)
    [](variable-length-arrays-vlas.html#cb598-8)    int *p = v;
    [](variable-length-arrays-vlas.html#cb598-9)
    [](variable-length-arrays-vlas.html#cb598-10)    *(p+2) = 12;
    [](variable-length-arrays-vlas.html#cb598-11)    printf("%d\n", v[2]);  // 12
    [](variable-length-arrays-vlas.html#cb598-12)
    [](variable-length-arrays-vlas.html#cb598-13)    p[3] = 34;
    [](variable-length-arrays-vlas.html#cb598-14)    printf("%d\n", v[3]);  // 34
    [](variable-length-arrays-vlas.html#cb598-15)}

Like with regular arrays, you can use parentheses with `sizeof()` to get the size of a would-be VLA without actually declaring one:
    
    
    [](variable-length-arrays-vlas.html#cb599-1)int x = 12;
    [](variable-length-arrays-vlas.html#cb599-2)
    [](variable-length-arrays-vlas.html#cb599-3)printf("%zu\n", sizeof(int [x]));  // Prints 48 on my system

## 30.3 Multidimensional VLAs

You can go ahead and make all kinds of VLAs with one or more dimensions set to a variable
    
    
    [](variable-length-arrays-vlas.html#cb600-1)int w = 10;
    [](variable-length-arrays-vlas.html#cb600-2)int h = 20;
    [](variable-length-arrays-vlas.html#cb600-3)
    [](variable-length-arrays-vlas.html#cb600-4)int x[h][w];
    [](variable-length-arrays-vlas.html#cb600-5)int y[5][w];
    [](variable-length-arrays-vlas.html#cb600-6)int z[10][w][20];

Again, you can navigate these just like you would a regular array.

## 30.4 Passing One-Dimensional VLAs to Functions

Passing single-dimensional VLAs into a function can be no different than passing a regular array in. You just go for it.
    
    
    [](variable-length-arrays-vlas.html#cb601-1)#include <stdio.h>
    [](variable-length-arrays-vlas.html#cb601-2)
    [](variable-length-arrays-vlas.html#cb601-3)int sum(int count, int *v)
    [](variable-length-arrays-vlas.html#cb601-4){
    [](variable-length-arrays-vlas.html#cb601-5)    int total = 0;
    [](variable-length-arrays-vlas.html#cb601-6)
    [](variable-length-arrays-vlas.html#cb601-7)    for (int i = 0; i < count; i++)
    [](variable-length-arrays-vlas.html#cb601-8)        total += v[i];
    [](variable-length-arrays-vlas.html#cb601-9)
    [](variable-length-arrays-vlas.html#cb601-10)    return total;
    [](variable-length-arrays-vlas.html#cb601-11)}
    [](variable-length-arrays-vlas.html#cb601-12)
    [](variable-length-arrays-vlas.html#cb601-13)int main(void)
    [](variable-length-arrays-vlas.html#cb601-14){
    [](variable-length-arrays-vlas.html#cb601-15)    int x[5];   // Standard array
    [](variable-length-arrays-vlas.html#cb601-16)
    [](variable-length-arrays-vlas.html#cb601-17)    int a = 5;
    [](variable-length-arrays-vlas.html#cb601-18)    int y[a];   // VLA
    [](variable-length-arrays-vlas.html#cb601-19)
    [](variable-length-arrays-vlas.html#cb601-20)    for (int i = 0; i < a; i++)
    [](variable-length-arrays-vlas.html#cb601-21)        x[i] = y[i] = i + 1;
    [](variable-length-arrays-vlas.html#cb601-22)
    [](variable-length-arrays-vlas.html#cb601-23)    printf("%d\n", sum(5, x));
    [](variable-length-arrays-vlas.html#cb601-24)    printf("%d\n", sum(a, y));
    [](variable-length-arrays-vlas.html#cb601-25)}

But there’s a bit more to it than that. You can also let C know that the array is a specific VLA size by passing that in first and then giving that dimension in the parameter list:
    
    
    [](variable-length-arrays-vlas.html#cb602-1)int sum(int count, int v[count])
    [](variable-length-arrays-vlas.html#cb602-2){
    [](variable-length-arrays-vlas.html#cb602-3)    // ...
    [](variable-length-arrays-vlas.html#cb602-4)}

Incidentally, there are a couple ways of listing a prototype for the above function; one of them involves an `*` if you don’t want to specifically name the value in the VLA. It just indicates that the type is a VLA as opposed to a regular pointer.

VLA prototypes:
    
    
    [](variable-length-arrays-vlas.html#cb603-1)void do_something(int count, int v[count]);  // With names
    [](variable-length-arrays-vlas.html#cb603-2)void do_something(int, int v[*]);            // Without names

Again, that `*` thing only works with the prototype—in the function itself, you’ll have to put the explicit size.

Now— _let’s get multidimensional_! This is where the fun begins.

## 30.5 Passing Multi-Dimensional VLAs to Functions

Same thing as we did with the second form of one-dimensional VLAs, above, but this time we’re passing in two dimensions and using those.

In the following example, we build a multiplication table matrix of a variable width and height, and then pass it to a function to print it out.
    
    
    [](variable-length-arrays-vlas.html#cb604-1)#include <stdio.h>
    [](variable-length-arrays-vlas.html#cb604-2)
    [](variable-length-arrays-vlas.html#cb604-3)void print_matrix(int h, int w, int m[h][w])
    [](variable-length-arrays-vlas.html#cb604-4){
    [](variable-length-arrays-vlas.html#cb604-5)    for (int row = 0; row < h; row++) {
    [](variable-length-arrays-vlas.html#cb604-6)        for (int col = 0; col < w; col++)
    [](variable-length-arrays-vlas.html#cb604-7)            printf("%2d ", m[row][col]);
    [](variable-length-arrays-vlas.html#cb604-8)        printf("\n");
    [](variable-length-arrays-vlas.html#cb604-9)    }
    [](variable-length-arrays-vlas.html#cb604-10)}
    [](variable-length-arrays-vlas.html#cb604-11)
    [](variable-length-arrays-vlas.html#cb604-12)int main(void)
    [](variable-length-arrays-vlas.html#cb604-13){
    [](variable-length-arrays-vlas.html#cb604-14)    int rows = 4;
    [](variable-length-arrays-vlas.html#cb604-15)    int cols = 7;
    [](variable-length-arrays-vlas.html#cb604-16)
    [](variable-length-arrays-vlas.html#cb604-17)    int matrix[rows][cols];
    [](variable-length-arrays-vlas.html#cb604-18)
    [](variable-length-arrays-vlas.html#cb604-19)    for (int row = 0; row < rows; row++)
    [](variable-length-arrays-vlas.html#cb604-20)        for (int col = 0; col < cols; col++)
    [](variable-length-arrays-vlas.html#cb604-21)            matrix[row][col] = row * col;
    [](variable-length-arrays-vlas.html#cb604-22)
    [](variable-length-arrays-vlas.html#cb604-23)    print_matrix(rows, cols, matrix);
    [](variable-length-arrays-vlas.html#cb604-24)}

### 30.5.1 Partial Multidimensional VLAs

You can have some of the dimensions fixed and some variable. Let’s say we have a record length fixed at 5 elements, but we don’t know how many records there are.
    
    
    [](variable-length-arrays-vlas.html#cb605-1)#include <stdio.h>
    [](variable-length-arrays-vlas.html#cb605-2)
    [](variable-length-arrays-vlas.html#cb605-3)void print_records(int count, int record[count][5])
    [](variable-length-arrays-vlas.html#cb605-4){
    [](variable-length-arrays-vlas.html#cb605-5)    for (int i = 0; i < count; i++) {
    [](variable-length-arrays-vlas.html#cb605-6)        for (int j = 0; j < 5; j++)
    [](variable-length-arrays-vlas.html#cb605-7)            printf("%2d ", record[i][j]);
    [](variable-length-arrays-vlas.html#cb605-8)        printf("\n");
    [](variable-length-arrays-vlas.html#cb605-9)    }
    [](variable-length-arrays-vlas.html#cb605-10)}
    [](variable-length-arrays-vlas.html#cb605-11)
    [](variable-length-arrays-vlas.html#cb605-12)int main(void)
    [](variable-length-arrays-vlas.html#cb605-13){
    [](variable-length-arrays-vlas.html#cb605-14)    int rec_count = 3;
    [](variable-length-arrays-vlas.html#cb605-15)    int records[rec_count][5];
    [](variable-length-arrays-vlas.html#cb605-16)
    [](variable-length-arrays-vlas.html#cb605-17)    // Fill with some dummy data
    [](variable-length-arrays-vlas.html#cb605-18)    for (int i = 0; i < rec_count; i++)
    [](variable-length-arrays-vlas.html#cb605-19)        for (int j = 0; j < 5; j++)
    [](variable-length-arrays-vlas.html#cb605-20)            records[i][j] = (i+1)*(j+2);
    [](variable-length-arrays-vlas.html#cb605-21)
    [](variable-length-arrays-vlas.html#cb605-22)    print_records(rec_count, records);
    [](variable-length-arrays-vlas.html#cb605-23)}

## 30.6 Compatibility with Regular Arrays

Because VLAs are just like regular arrays in memory, it’s perfectly permissible to pass them interchangeably… as long as the dimensions match.

For example, if we have a function that specifically wants a \\(3\times5\\) array, we can still pass a VLA into it.
    
    
    [](variable-length-arrays-vlas.html#cb606-1)int foo(int m[5][3]) {...}
    [](variable-length-arrays-vlas.html#cb606-2)
    [](variable-length-arrays-vlas.html#cb606-3)\\ ...
    [](variable-length-arrays-vlas.html#cb606-4)
    [](variable-length-arrays-vlas.html#cb606-5)int w = 3, h = 5;
    [](variable-length-arrays-vlas.html#cb606-6)int matrix[h][w];
    [](variable-length-arrays-vlas.html#cb606-7)
    [](variable-length-arrays-vlas.html#cb606-8)foo(matrix);   // OK!

Likewise, if you have a VLA function, you can pass a regular array into it:
    
    
    [](variable-length-arrays-vlas.html#cb607-1)int foo(int h, int w, int m[h][w]) {...}
    [](variable-length-arrays-vlas.html#cb607-2)
    [](variable-length-arrays-vlas.html#cb607-3)\\ ...
    [](variable-length-arrays-vlas.html#cb607-4)
    [](variable-length-arrays-vlas.html#cb607-5)int matrix[3][5];
    [](variable-length-arrays-vlas.html#cb607-6)
    [](variable-length-arrays-vlas.html#cb607-7)foo(3, 5, matrix);   // OK!

Beware, though: if your dimensions mismatch, you’re going to have some undefined behavior going on, likely.

## 30.7 `typedef` and VLAs

You can `typedef` a VLA, but the behavior might not be as you expect.

Basically, `typedef` makes a new type with the values as they existed the moment the `typedef` was executed.

So it’s not a `typedef` of a VLA so much as a new fixed size array type of the dimensions at the time.
    
    
    [](variable-length-arrays-vlas.html#cb608-1)#include <stdio.h>
    [](variable-length-arrays-vlas.html#cb608-2)
    [](variable-length-arrays-vlas.html#cb608-3)int main(void)
    [](variable-length-arrays-vlas.html#cb608-4){
    [](variable-length-arrays-vlas.html#cb608-5)    int w = 10;
    [](variable-length-arrays-vlas.html#cb608-6)
    [](variable-length-arrays-vlas.html#cb608-7)    typedef int goat[w];
    [](variable-length-arrays-vlas.html#cb608-8)
    [](variable-length-arrays-vlas.html#cb608-9)    // goat is an array of 10 ints
    [](variable-length-arrays-vlas.html#cb608-10)    goat x;
    [](variable-length-arrays-vlas.html#cb608-11)
    [](variable-length-arrays-vlas.html#cb608-12)    // Init with squares of numbers
    [](variable-length-arrays-vlas.html#cb608-13)    for (int i = 0; i < w; i++)
    [](variable-length-arrays-vlas.html#cb608-14)        x[i] = i*i;
    [](variable-length-arrays-vlas.html#cb608-15)
    [](variable-length-arrays-vlas.html#cb608-16)    // Print them
    [](variable-length-arrays-vlas.html#cb608-17)    for (int i = 0; i < w; i++)
    [](variable-length-arrays-vlas.html#cb608-18)        printf("%d\n", x[i]);
    [](variable-length-arrays-vlas.html#cb608-19)
    [](variable-length-arrays-vlas.html#cb608-20)    // Now let's change w...
    [](variable-length-arrays-vlas.html#cb608-21)
    [](variable-length-arrays-vlas.html#cb608-22)    w = 20;
    [](variable-length-arrays-vlas.html#cb608-23)
    [](variable-length-arrays-vlas.html#cb608-24)    // But goat is STILL an array of 10 ints, because that was the
    [](variable-length-arrays-vlas.html#cb608-25)    // value of w when the typedef executed.
    [](variable-length-arrays-vlas.html#cb608-26)}

So it acts like an array of fixed size.

But you still can’t use an initializer list on it.

## 30.8 Jumping Pitfalls

You have to watch out when using `goto` near VLAs because a lot of things aren’t legal.

And when you’re using `longjmp()` there’s a case where you could leak memory with VLAs.

But both of these things we’ll cover in their respective chapters.

## 30.9 General Issues

VLAs have been banned from the Linux kernel for a few reasons:

  * Lots of places they were used should have just been fixed-size.
  * The code behind VLAs is slower (to a degree that most people wouldn’t notice, but makes a difference in an operating system).
  * VLAs are not supported to the same degree by all C compilers.
  * Stack size is limited, and VLAs go on the stack. If some code accidentally (or maliciously) passes a large value into a kernel function that allocates a VLA, _Bad Things_ ™ could happen.



Other folks online point out that there’s no way to detect a VLA’s failure to allocate, and programs that suffered such problems would likely just crash. While fixed-size arrays also have the same issue, it’s far more likely that someone accidentally make a _VLA Of Unusual Size_ than somehow accidentally declare a fixed-size, say, 30 megabyte array.

* * *

[Prev](signal-handling.html) | [Contents](index.html) | [Next](goto.html)

---

[Prev](variable-length-arrays-vlas.html) | [Contents](index.html) | [Next](types-part-v-compound-literals-and-generic-selections.html)

* * *

# 31 `goto`

The `goto` statement is universally revered and can be here presented without contest.

Just kidding! Over the years, there has been a lot of back-and-forth over whether or not (often not) `goto` is [considered harmful](https://en.wikipedia.org/wiki/Goto#Criticism)[176](function-specifiers-alignment-specifiersoperators.html#fn176).

In this programmer’s opinion, you should use whichever constructs leads to the _best_ code, factoring in maintainability and speed. And sometimes this might be `goto`!

In this chapter, we’ll see how `goto` works in C, and then check out some of the common cases where it is used[177](function-specifiers-alignment-specifiersoperators.html#fn177).

## 31.1 A Simple Example

In this example, we’re going to use `goto` to skip a line of code and jump to a _label_. The label is the identifier that can be a `goto` target—it ends with a colon (`:`).
    
    
    [](goto.html#cb609-1)#include <stdio.h>
    [](goto.html#cb609-2)
    [](goto.html#cb609-3)int main(void)
    [](goto.html#cb609-4){
    [](goto.html#cb609-5)    printf("One\n");
    [](goto.html#cb609-6)    printf("Two\n");
    [](goto.html#cb609-7)
    [](goto.html#cb609-8)    goto skip_3;
    [](goto.html#cb609-9)
    [](goto.html#cb609-10)    printf("Three\n");
    [](goto.html#cb609-11)
    [](goto.html#cb609-12)skip_3:
    [](goto.html#cb609-13)
    [](goto.html#cb609-14)    printf("Five!\n");
    [](goto.html#cb609-15)}

The output is:
    
    
    [](goto.html#cb610-1)One
    [](goto.html#cb610-2)Two
    [](goto.html#cb610-3)Five!

`goto` sends execution jumping to the specified label, skipping everything in between.

You can jump forward or backward with `goto`.
    
    
    [](goto.html#cb611-1)infinite_loop:
    [](goto.html#cb611-2)    print("Hello, world!\n");
    [](goto.html#cb611-3)    goto infinite_loop;

Labels are skipped over during execution. The following will print all three numbers in order just as if the labels weren’t there:
    
    
    [](goto.html#cb612-1)    printf("Zero\n");
    [](goto.html#cb612-2)label_1:
    [](goto.html#cb612-3)label_2:
    [](goto.html#cb612-4)    printf("One\n");
    [](goto.html#cb612-5)label_3:
    [](goto.html#cb612-6)    printf("Two\n");
    [](goto.html#cb612-7)label_4:
    [](goto.html#cb612-8)    printf("Three\n");

As you’ve noticed, it’s common convention to justify the labels all the way on the left. This increases readability because a reader can quickly scan to find the destination.

Labels have _function scope_. That is, no matter how many levels deep in blocks they appear, you can still `goto` them from anywhere in the function.

It also means you can only `goto` labels that are in the same function as the `goto` itself. Labels in other functions are out of scope from `goto`’s perspective. And it means you can use the same label name in two functions—just not the same label name in the same function.

## 31.2 Labeled `continue`

In some languages, you can actually specify a label for a `continue` statement. C doesn’t allow it, but you can easily use `goto` instead.

To show the issue, check out `continue` in this nested loop:
    
    
    [](goto.html#cb613-1)for (int i = 0; i < 3; i++) {
    [](goto.html#cb613-2)    for (int j = 0; j < 3; j++) {
    [](goto.html#cb613-3)        printf("%d, %d\n", i, j);
    [](goto.html#cb613-4)        continue;   // Always goes to next j
    [](goto.html#cb613-5)    }
    [](goto.html#cb613-6)}

As we see, that `continue`, like all `continues`, goes to the next iteration of the nearest enclosing loop. What if we want to `continue` in the next loop out, the loop with `i`?

Well, we can `break` to get back to the outer loop, right?
    
    
    [](goto.html#cb614-1)for (int i = 0; i < 3; i++) {
    [](goto.html#cb614-2)    for (int j = 0; j < 3; j++) {
    [](goto.html#cb614-3)        printf("%d, %d\n", i, j);
    [](goto.html#cb614-4)        break;     // Gets us to the next iteration of i
    [](goto.html#cb614-5)    }
    [](goto.html#cb614-6)}

That gets us two levels of nested loop. But then if we nest another loop, we’re out of options. What about this, where we don’t have any statement that will get us out to the next iteration of `i`?
    
    
    [](goto.html#cb615-1)for (int i = 0; i < 3; i++) {
    [](goto.html#cb615-2)    for (int j = 0; j < 3; j++) {
    [](goto.html#cb615-3)        for (int k = 0; k < 3; k++) {
    [](goto.html#cb615-4)            printf("%d, %d, %d\n", i, j, k);
    [](goto.html#cb615-5)
    [](goto.html#cb615-6)            continue;  // Gets us to the next iteration of k
    [](goto.html#cb615-7)            break;     // Gets us to the next iteration of j
    [](goto.html#cb615-8)            ????;      // Gets us to the next iteration of i???
    [](goto.html#cb615-9)
    [](goto.html#cb615-10)        }
    [](goto.html#cb615-11)    }
    [](goto.html#cb615-12)}

The `goto` statement offers us a way!
    
    
    [](goto.html#cb616-1)    for (int i = 0; i < 3; i++) {
    [](goto.html#cb616-2)        for (int j = 0; j < 3; j++) {
    [](goto.html#cb616-3)            for (int k = 0; k < 3; k++) {
    [](goto.html#cb616-4)                printf("%d, %d, %d\n", i, j, k);
    [](goto.html#cb616-5)
    [](goto.html#cb616-6)                goto continue_i;   // Now continuing the i loop!!
    [](goto.html#cb616-7)            }
    [](goto.html#cb616-8)        }
    [](goto.html#cb616-9)continue_i: ;
    [](goto.html#cb616-10)    }

We have a `;` at the end there—that’s because you can’t have a label pointing to the plain end of a compound statement (or before a variable declaration).

## 31.3 Bailing Out

When you’re super nested in the middle of some code, you can use `goto` to get out of it in a manner that’s often cleaner than nesting more `if`s and using flag variables.
    
    
    [](goto.html#cb617-1)    // Pseudocode
    [](goto.html#cb617-2)
    [](goto.html#cb617-3)    for(...) {
    [](goto.html#cb617-4)        for (...) {
    [](goto.html#cb617-5)            while (...) {
    [](goto.html#cb617-6)                do {
    [](goto.html#cb617-7)                    if (some_error_condition)
    [](goto.html#cb617-8)                        goto bail;
    [](goto.html#cb617-9)
    [](goto.html#cb617-10)                } while(...);
    [](goto.html#cb617-11)            }
    [](goto.html#cb617-12)        }
    [](goto.html#cb617-13)    }
    [](goto.html#cb617-14)
    [](goto.html#cb617-15)bail:
    [](goto.html#cb617-16)    // Cleanup here

Without `goto`, you’d have to check an error condition flag in all of the loops to get all the way out.

## 31.4 Labeled `break`

This is a very similar situation to how `continue` only continues the innermost loop. `break` also only breaks out of the innermost loop.
    
    
    [](goto.html#cb618-1)    for (int i = 0; i < 3; i++) {
    [](goto.html#cb618-2)        for (int j = 0; j < 3; j++) {
    [](goto.html#cb618-3)            printf("%d, %d\n", i, j);
    [](goto.html#cb618-4)            break;   // Only breaks out of the j loop
    [](goto.html#cb618-5)        }
    [](goto.html#cb618-6)    }
    [](goto.html#cb618-7)
    [](goto.html#cb618-8)    printf("Done!\n");

But we can use `goto` to break farther:
    
    
    [](goto.html#cb619-1)    for (int i = 0; i < 3; i++) {
    [](goto.html#cb619-2)        for (int j = 0; j < 3; j++) {
    [](goto.html#cb619-3)            printf("%d, %d\n", i, j);
    [](goto.html#cb619-4)            goto break_i;   // Now breaking out of the i loop!
    [](goto.html#cb619-5)        }
    [](goto.html#cb619-6)    }
    [](goto.html#cb619-7)
    [](goto.html#cb619-8)break_i:
    [](goto.html#cb619-9)
    [](goto.html#cb619-10)    printf("Done!\n");

## 31.5 Multi-level Cleanup

If you’re calling multiple functions to initialize multiple systems and one of them fails, you should only de-initialize the ones that you’ve gotten to so far.

Let’s do a fake example where we start initializing systems and checking to see if any returns an error (we’ll use `-1` to indicate an error). If one of them does, we have to shutdown only the systems we’ve initialized so far.
    
    
    [](goto.html#cb620-1)    if (init_system_1() == -1)
    [](goto.html#cb620-2)        goto shutdown;
    [](goto.html#cb620-3)
    [](goto.html#cb620-4)    if (init_system_2() == -1)
    [](goto.html#cb620-5)        goto shutdown_1;
    [](goto.html#cb620-6)
    [](goto.html#cb620-7)    if (init_system_3() == -1)
    [](goto.html#cb620-8)        goto shutdown_2;
    [](goto.html#cb620-9)
    [](goto.html#cb620-10)    if (init_system_4() == -1)
    [](goto.html#cb620-11)        goto shutdown_3;
    [](goto.html#cb620-12)
    [](goto.html#cb620-13)    do_main_thing();   // Run our program
    [](goto.html#cb620-14)
    [](goto.html#cb620-15)    shutdown_system4();
    [](goto.html#cb620-16)
    [](goto.html#cb620-17)shutdown_3:
    [](goto.html#cb620-18)    shutdown_system3();
    [](goto.html#cb620-19)
    [](goto.html#cb620-20)shutdown_2:
    [](goto.html#cb620-21)    shutdown_system2();
    [](goto.html#cb620-22)
    [](goto.html#cb620-23)shutdown_1:
    [](goto.html#cb620-24)    shutdown_system1();
    [](goto.html#cb620-25)
    [](goto.html#cb620-26)shutdown:
    [](goto.html#cb620-27)    print("All subsystems shut down.\n");

Note that we’re shutting down in the reverse order that we initialized the subsystems. So if subsystem 4 fails to start up, it will shut down 3, 2, then 1 in that order.

## 31.6 Tail Call Optimization

Kinda. For recursive functions only.

If you’re unfamiliar, [Tail Call Optimization (TCO)](https://en.wikipedia.org/wiki/Tail_call)[178](function-specifiers-alignment-specifiersoperators.html#fn178) is a way to not waste stack space when calling other functions under very specific circumstances. Unfortunately the details are beyond the scope of this guide.

But if you have a recursive function you know can be optimized in this way, you can make use of this technique. (Note that you can’t tail call other functions due to the function scope of labels.)

Let’s do a straightforward example, factorial.

Here’s a recursive version that’s not TCO, but it can be!
    
    
    [](goto.html#cb621-1)#include <stdio.h>
    [](goto.html#cb621-2)#include <complex.h>
    [](goto.html#cb621-3)
    [](goto.html#cb621-4)int factorial(int n, int a)
    [](goto.html#cb621-5){
    [](goto.html#cb621-6)    if (n == 0)
    [](goto.html#cb621-7)        return a;
    [](goto.html#cb621-8)
    [](goto.html#cb621-9)    return factorial(n - 1, a * n);
    [](goto.html#cb621-10)}
    [](goto.html#cb621-11)
    [](goto.html#cb621-12)int main(void)
    [](goto.html#cb621-13){
    [](goto.html#cb621-14)    for (int i = 0; i < 8; i++)
    [](goto.html#cb621-15)        printf("%d! == %ld\n", i, factorial(i, 1));
    [](goto.html#cb621-16)}

To make it happen, you can replace the call with two steps:

  1. Set the values of the parameters to what they’d be on the next call.
  2. `goto` a label on the first line of the function.



Let’s try it:
    
    
    [](goto.html#cb622-1)#include <stdio.h>
    [](goto.html#cb622-2)
    [](goto.html#cb622-3)int factorial(int n, int a)
    [](goto.html#cb622-4){
    [](goto.html#cb622-5)tco:  // add this
    [](goto.html#cb622-6)
    [](goto.html#cb622-7)    if (n == 0)
    [](goto.html#cb622-8)        return a;
    [](goto.html#cb622-9)
    [](goto.html#cb622-10)    // replace return by setting new parameter values and
    [](goto.html#cb622-11)    // goto-ing the beginning of the function
    [](goto.html#cb622-12)
    [](goto.html#cb622-13)    //return factorial(n - 1, a * n);
    [](goto.html#cb622-14)
    [](goto.html#cb622-15)    int next_n = n - 1;  // See how these match up with
    [](goto.html#cb622-16)    int next_a = a * n;  // the recursive arguments, above?
    [](goto.html#cb622-17)
    [](goto.html#cb622-18)    n = next_n;   // Set the parameters to the new values
    [](goto.html#cb622-19)    a = next_a;
    [](goto.html#cb622-20)
    [](goto.html#cb622-21)    goto tco;   // And repeat!
    [](goto.html#cb622-22)}
    [](goto.html#cb622-23)
    [](goto.html#cb622-24)int main(void)
    [](goto.html#cb622-25){
    [](goto.html#cb622-26)    for (int i = 0; i < 8; i++)
    [](goto.html#cb622-27)        printf("%d! == %d\n", i, factorial(i, 1));
    [](goto.html#cb622-28)}

I used temporary variables up there to set the next values of the parameters before jumping to the start of the function. See how they correspond to the recursive arguments that were in the recursive call?

Now, why use temp variables? I could have done this instead:
    
    
    [](goto.html#cb623-1)    a *= n;
    [](goto.html#cb623-2)    n -= 1;
    [](goto.html#cb623-3)
    [](goto.html#cb623-4)    goto tco;

and that actually works just fine. But if I carelessly reverse those two lines of code:
    
    
    [](goto.html#cb624-1)    n -= 1;  // BAD NEWS
    [](goto.html#cb624-2)    a *= n;

—now we’re in trouble. We modified `n` before using it to modify `a`. That’s Bad because that’s not how it works when you call recursively. Using the temporary variables avoids this problem even if you’re not looking out for it. And the compiler likely optimizes them out, anyway.

## 31.7 Restarting Interrupted System Calls

This is outside the spec, but commonly seen in Unix-like systems.

Certain long-lived system calls might return an error if they’re interrupted by a signal, and `errno` will be set to `EINTR` to indicate the syscall was doing fine; it was just interrupted.

In those cases, it’s really common for the programmer to want to restart the call and try it again.
    
    
    [](goto.html#cb625-1)retry:
    [](goto.html#cb625-2)    byte_count = read(0, buf, sizeof(buf) - 1);  // Unix read() syscall
    [](goto.html#cb625-3)
    [](goto.html#cb625-4)    if (byte_count == -1) {            // An error occurred...
    [](goto.html#cb625-5)        if (errno == EINTR) {          // But it was just interrupted
    [](goto.html#cb625-6)            printf("Restarting...\n");
    [](goto.html#cb625-7)            goto retry;
    [](goto.html#cb625-8)        }

Many Unix-likes have an `SA_RESTART` flag you can pass to `sigaction()` to request the OS automatically restart any slow syscalls instead of failing with `EINTR`.

Again, this is Unix-specific and is outside the C standard.

That said, it’s possible to use a similar technique any time any function should be restarted.

## 31.8 `goto` and Thread Preemption

This example is ripped directly from [_Operating Systems: Three Easy Pieces_](http://www.ostep.org/), another excellent book from like-minded authors who also feel that quality books should be free to download. Not that I’m opinionated, or anything.
    
    
    [](goto.html#cb626-1)retry:
    [](goto.html#cb626-2)
    [](goto.html#cb626-3)    pthread_mutex_lock(L1);
    [](goto.html#cb626-4)
    [](goto.html#cb626-5)    if (pthread_mutex_trylock(L2) != 0) {
    [](goto.html#cb626-6)        pthread_mutex_unlock(L1);
    [](goto.html#cb626-7)        goto retry;
    [](goto.html#cb626-8)    }
    [](goto.html#cb626-9)
    [](goto.html#cb626-10)    save_the_day();
    [](goto.html#cb626-11)
    [](goto.html#cb626-12)    pthread_mutex_unlock(L2);
    [](goto.html#cb626-13)    pthread_mutex_unlock(L1);

There the thread happily acquires the mutex `L1`, but then potentially fails to get the second resource guarded by mutex `L2` (if some other uncooperative thread holds it, say). If our thread can’t get the `L2` lock, it unlocks `L1` and then uses `goto` to cleanly retry.

We hope our heroic thread eventually manages to acquire both mutexes and save the day, all while avoiding evil deadlock.

## 31.9 `goto` and Variable Scope

We’ve already seen that labels have function scope, but weird things can happen if we jump past some variable initialization.

Look at this example where we jump from a place where the variable `x` is out of scope into the middle of its scope (in the block).
    
    
    [](goto.html#cb627-1)    goto label;
    [](goto.html#cb627-2)
    [](goto.html#cb627-3)    {
    [](goto.html#cb627-4)        int x = 12345;
    [](goto.html#cb627-5)
    [](goto.html#cb627-6)label:
    [](goto.html#cb627-7)        printf("%d\n", x);
    [](goto.html#cb627-8)    }

This will compile and run, but gives me a warning:
    
    
    [](goto.html#cb628-1)warning: ‘x’ is used uninitialized in this function

And then it prints out `0` when I run it (your mileage may vary).

Basically what has happened is that we jumped into `x`’s scope (so it was OK to reference it in the `printf()`) but we jumped over the line that actually initialized it to `12345`. So the value was indeterminate.

The fix is, of course, to get the initialization _after_ the label one way or another.
    
    
    [](goto.html#cb629-1)    goto label;
    [](goto.html#cb629-2)
    [](goto.html#cb629-3)    {
    [](goto.html#cb629-4)        int x;
    [](goto.html#cb629-5)
    [](goto.html#cb629-6)label:
    [](goto.html#cb629-7)        x = 12345;
    [](goto.html#cb629-8)        printf("%d\n", x);
    [](goto.html#cb629-9)    }

Let’s look at one more example.
    
    
    [](goto.html#cb630-1)    {
    [](goto.html#cb630-2)        int x = 10;
    [](goto.html#cb630-3)
    [](goto.html#cb630-4)label:
    [](goto.html#cb630-5)
    [](goto.html#cb630-6)        printf("%d\n", x);
    [](goto.html#cb630-7)    }
    [](goto.html#cb630-8)
    [](goto.html#cb630-9)    goto label;

What happens here?

The first time through the block, we’re good. `x` is `10` and that’s what prints.

But after the `goto`, we’re jumping into the scope of `x`, but past its initialization. Which means we can still print it, but the value is indeterminate (since it hasn’t been reinitialized).

On my machine, it prints `10` again (to infinity), but that’s just luck. It could print any value after the `goto` since `x` is uninitialized.

## 31.10 `goto` and Variable-Length Arrays

When it comes to VLAs and `goto`, there’s one rule: you can’t jump from outside the scope of a VLA into the scope of that VLA.

If I try to do this:
    
    
    [](goto.html#cb631-1)    int x = 10;
    [](goto.html#cb631-2)
    [](goto.html#cb631-3)    goto label;
    [](goto.html#cb631-4)
    [](goto.html#cb631-5)    {
    [](goto.html#cb631-6)        int v[x];
    [](goto.html#cb631-7)
    [](goto.html#cb631-8)label:
    [](goto.html#cb631-9)
    [](goto.html#cb631-10)        printf("Hi!\n");
    [](goto.html#cb631-11)    }

I get an error:
    
    
    [](goto.html#cb632-1)error: jump into scope of identifier with variably modified type

You can jump in ahead of the VLA declaration, like this:
    
    
    [](goto.html#cb633-1)    int x = 10;
    [](goto.html#cb633-2)
    [](goto.html#cb633-3)    goto label;
    [](goto.html#cb633-4)
    [](goto.html#cb633-5)    {
    [](goto.html#cb633-6)label:  ;
    [](goto.html#cb633-7)        int v[x];
    [](goto.html#cb633-8)
    [](goto.html#cb633-9)        printf("Hi!\n");
    [](goto.html#cb633-10)    }

Because that way the VLA gets allocated properly before its inevitable deallocation once it falls out of scope.

* * *

[Prev](variable-length-arrays-vlas.html) | [Contents](index.html) | [Next](types-part-v-compound-literals-and-generic-selections.html)

---

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

---

[Prev](types-part-v-compound-literals-and-generic-selections.html) | [Contents](index.html) | [Next](setjmp-longjmp.html)

* * *

# 33 Arrays Part II

We’re going to go over a few extra misc things this chapter concerning arrays.

  * Type qualifiers with array parameters
  * The `static` keyword with array parameters
  * Partial multi-dimensional array initializers



They’re not super-commonly seen, but we’ll peek at them since they’re part of the newer spec.

## 33.1 Type Qualifiers for Arrays in Parameter Lists

If you recall from earlier, these two things are equivalent in function parameter lists:
    
    
    [](arrays-part-ii.html#cb656-1)int func(int *p) {...}
    [](arrays-part-ii.html#cb656-2)int func(int p[]) {...}

And you might also recall that you can add type qualifiers to a pointer variable like so:
    
    
    [](arrays-part-ii.html#cb657-1)int *const p;
    [](arrays-part-ii.html#cb657-2)int *volatile p;
    [](arrays-part-ii.html#cb657-3)int *const volatile p;
    [](arrays-part-ii.html#cb657-4)// etc.

But how can we do that when we’re using array notation in your parameter list?

Turns out it goes in the brackets. And you can put the optional count after. The two following lines are equivalent:
    
    
    [](arrays-part-ii.html#cb658-1)int func(int *const volatile p) {...}
    [](arrays-part-ii.html#cb658-2)int func(int p[const volatile]) {...}
    [](arrays-part-ii.html#cb658-3)int func(int p[const volatile 10]) {...}

If you have a multidimensional array, you need to put the type qualifiers in the first set of brackets.

## 33.2 `static` for Arrays in Parameter Lists

Similarly, you can use the keyword static in the array in a parameter list.

This is something I’ve never seen in the wild. It is **always** followed by a dimension:
    
    
    [](arrays-part-ii.html#cb659-1)int func(int p[static 4]) {...}

What this means, in the above example, is the compiler is going to assume that any array you pass to the function will be _at least_ 4 elements.

Anything else is undefined behavior.
    
    
    [](arrays-part-ii.html#cb660-1)int func(int p[static 4]) {...}
    [](arrays-part-ii.html#cb660-2)
    [](arrays-part-ii.html#cb660-3)int main(void)
    [](arrays-part-ii.html#cb660-4){
    [](arrays-part-ii.html#cb660-5)    int a[] = {11, 22, 33, 44};
    [](arrays-part-ii.html#cb660-6)    int b[] = {11, 22, 33, 44, 55};
    [](arrays-part-ii.html#cb660-7)    int c[] = {11, 22};
    [](arrays-part-ii.html#cb660-8)
    [](arrays-part-ii.html#cb660-9)    func(a);  // OK! a is 4 elements, the minimum
    [](arrays-part-ii.html#cb660-10)    func(b);  // OK! b is at least 4 elements
    [](arrays-part-ii.html#cb660-11)    func(c);  // Undefined behavior! c is under 4 elements!
    [](arrays-part-ii.html#cb660-12)}

This basically sets the minimum size array you can have.

Important note: there is nothing in the compiler that prohibits you from passing in a smaller array. The compiler probably won’t warn you, and it won’t detect it at runtime.

By putting `static` in there, you’re saying, “I double secret PROMISE that I will never pass in a smaller array than this.” And the compiler says, “Yeah, fine,” and trusts you to not do it.

And then the compiler can make certain code optimizations, safe in the knowledge that you, the programmer, will always do the right thing.

## 33.3 Equivalent Initializers

C is a little bit, shall we say, _flexible_ when it comes to array initializers.

We’ve already seen some of this, where any missing values are replaced with zero.

For example, we can initialize a 5 element array to `1,2,0,0,0` with this:
    
    
    [](arrays-part-ii.html#cb661-1)int a[5] = {1, 2};

Or set an array entirely to zero with:
    
    
    [](arrays-part-ii.html#cb662-1)int a[5] = {0};

But things get interesting when initializing multidimensional arrays.

Let’s make an array of 3 rows and 2 columns:
    
    
    [](arrays-part-ii.html#cb663-1)int a[3][2];

Let’s write some code to initialize it and print the result:
    
    
    [](arrays-part-ii.html#cb664-1)#include <stdio.h>
    [](arrays-part-ii.html#cb664-2)
    [](arrays-part-ii.html#cb664-3)int main(void)
    [](arrays-part-ii.html#cb664-4){
    [](arrays-part-ii.html#cb664-5)    int a[3][2] = {
    [](arrays-part-ii.html#cb664-6)        {1, 2},
    [](arrays-part-ii.html#cb664-7)        {3, 4},
    [](arrays-part-ii.html#cb664-8)        {5, 6}
    [](arrays-part-ii.html#cb664-9)    };
    [](arrays-part-ii.html#cb664-10)
    [](arrays-part-ii.html#cb664-11)    for (int row = 0; row < 3; row++) {
    [](arrays-part-ii.html#cb664-12)        for (int col = 0; col < 2; col++)
    [](arrays-part-ii.html#cb664-13)            printf("%d ", a[row][col]);
    [](arrays-part-ii.html#cb664-14)        printf("\n");
    [](arrays-part-ii.html#cb664-15)    }
    [](arrays-part-ii.html#cb664-16)}

And when we run it, we get the expected:
    
    
    [](arrays-part-ii.html#cb665-1)1 2
    [](arrays-part-ii.html#cb665-2)3 4
    [](arrays-part-ii.html#cb665-3)5 6

Let’s leave off some of the initializer elements and see they get set to zero:
    
    
    [](arrays-part-ii.html#cb666-1)    int a[3][2] = {
    [](arrays-part-ii.html#cb666-2)        {1, 2},
    [](arrays-part-ii.html#cb666-3)        {3},    // Left off the 4!
    [](arrays-part-ii.html#cb666-4)        {5, 6}
    [](arrays-part-ii.html#cb666-5)    };

which produces:
    
    
    [](arrays-part-ii.html#cb667-1)1 2
    [](arrays-part-ii.html#cb667-2)3 0
    [](arrays-part-ii.html#cb667-3)5 6

Now let’s leave off the entire last middle element:
    
    
    [](arrays-part-ii.html#cb668-1)    int a[3][2] = {
    [](arrays-part-ii.html#cb668-2)        {1, 2},
    [](arrays-part-ii.html#cb668-3)        // {3, 4},   // Just cut this whole thing out
    [](arrays-part-ii.html#cb668-4)        {5, 6}
    [](arrays-part-ii.html#cb668-5)    };

And now we get this, which might not be what you expect:
    
    
    [](arrays-part-ii.html#cb669-1)1 2
    [](arrays-part-ii.html#cb669-2)5 6
    [](arrays-part-ii.html#cb669-3)0 0

But if you stop to think about it, we only provided enough initializers for two rows, so they got used for the first two rows. And the remaining elements were initialized to zero.

So far so good. Generally, if we leave off parts of the initializer, the compiler sets the corresponding elements to `0`.

But let’s get _crazy_.
    
    
    [](arrays-part-ii.html#cb670-1)    int a[3][2] = { 1, 2, 3, 4, 5, 6 };

What—? That’s a 2D array, but it only has a 1D initializer!

Turns out that’s legal (though GCC will warn about it with the proper warnings turned on).

Basically, what it does is starts filling in elements in row 0, then row 1, then row 2 from left to right.

So when we print, it prints in order:
    
    
    [](arrays-part-ii.html#cb671-1)1 2
    [](arrays-part-ii.html#cb671-2)3 4
    [](arrays-part-ii.html#cb671-3)5 6

If we leave some off:
    
    
    [](arrays-part-ii.html#cb672-1)    int a[3][2] = { 1, 2, 3 };

they fill with `0`:
    
    
    [](arrays-part-ii.html#cb673-1)1 2
    [](arrays-part-ii.html#cb673-2)3 0
    [](arrays-part-ii.html#cb673-3)0 0

So if you want to fill the whole array with `0`, then go ahead and:
    
    
    [](arrays-part-ii.html#cb674-1)    int a[3][2] = {0};

But my recommendation is if you have a 2D array, use a 2D initializer. It just makes the code more readable. (Except for initializing the whole array with `0`, in which case it’s idiomatic to use `{0}` no matter the dimension of the array.)

* * *

[Prev](types-part-v-compound-literals-and-generic-selections.html) | [Contents](index.html) | [Next](setjmp-longjmp.html)

---

[Prev](arrays-part-ii.html) | [Contents](index.html) | [Next](incomplete-types.html)

* * *

# 34 Long Jumps with `setjmp`, `longjmp`

We’ve already seen `goto`, which jumps in function scope. But `longjmp()` allows you to jump back to an earlier point in execution, back to a function that called this one.

There are a lot of limitations and caveats, but this can be a useful function for bailing out from deep in the call stack back up to an earlier state.

In my experience, this is very rarely-used functionality.

## 34.1 Using `setjmp` and `longjmp`

The dance we’re going to do here is to basically put a bookmark in execution with `setjmp()`. Later on, we’ll call `longjmp()` and it’ll jump back to the earlier point in execution where we set the bookmark with `setjmp()`.

And it can do this even if you’ve called subfunctions.

Here’s a quick demo where we call into functions a couple levels deep and then bail out of it.

We’re going to use a file scope variable `env` to keep the _state_ of things when we call `setjmp()` so we can restore them when we call `longjmp()` later. This is the variable in which we remember our “place”.

The variable `env` is of type `jmp_buf`, an opaque type declared in `<setjmp.h>`.
    
    
    [](setjmp-longjmp.html#cb675-1)#include <stdio.h>
    [](setjmp-longjmp.html#cb675-2)#include <setjmp.h>
    [](setjmp-longjmp.html#cb675-3)
    [](setjmp-longjmp.html#cb675-4)jmp_buf env;
    [](setjmp-longjmp.html#cb675-5)
    [](setjmp-longjmp.html#cb675-6)void depth2(void)
    [](setjmp-longjmp.html#cb675-7){
    [](setjmp-longjmp.html#cb675-8)    printf("Entering depth 2\n");
    [](setjmp-longjmp.html#cb675-9)    longjmp(env, 3490);           // Bail out
    [](setjmp-longjmp.html#cb675-10)    printf("Leaving depth 2\n");  // This won't happen
    [](setjmp-longjmp.html#cb675-11)}
    [](setjmp-longjmp.html#cb675-12)
    [](setjmp-longjmp.html#cb675-13)void depth1(void)
    [](setjmp-longjmp.html#cb675-14){
    [](setjmp-longjmp.html#cb675-15)    printf("Entering depth 1\n");
    [](setjmp-longjmp.html#cb675-16)    depth2();
    [](setjmp-longjmp.html#cb675-17)    printf("Leaving depth 1\n");  // This won't happen
    [](setjmp-longjmp.html#cb675-18)}
    [](setjmp-longjmp.html#cb675-19)
    [](setjmp-longjmp.html#cb675-20)int main(void)
    [](setjmp-longjmp.html#cb675-21){
    [](setjmp-longjmp.html#cb675-22)    switch (setjmp(env)) {
    [](setjmp-longjmp.html#cb675-23)      case 0:
    [](setjmp-longjmp.html#cb675-24)          printf("Calling into functions, setjmp() returned 0\n");
    [](setjmp-longjmp.html#cb675-25)          depth1();
    [](setjmp-longjmp.html#cb675-26)          printf("Returned from functions\n");  // This won't happen
    [](setjmp-longjmp.html#cb675-27)          break;
    [](setjmp-longjmp.html#cb675-28)
    [](setjmp-longjmp.html#cb675-29)      case 3490:
    [](setjmp-longjmp.html#cb675-30)          printf("Bailed back to main, setjmp() returned 3490\n");
    [](setjmp-longjmp.html#cb675-31)          break;
    [](setjmp-longjmp.html#cb675-32)    }
    [](setjmp-longjmp.html#cb675-33)}

When run, this outputs:
    
    
    [](setjmp-longjmp.html#cb676-1)Calling into functions, setjmp() returned 0
    [](setjmp-longjmp.html#cb676-2)Entering depth 1
    [](setjmp-longjmp.html#cb676-3)Entering depth 2
    [](setjmp-longjmp.html#cb676-4)Bailed back to main, setjmp() returned 3490

If you try to take that output and match it up with the code, it’s clear there’s some really _funky_ stuff going on.

One of the most notable things is that `setjmp()` returns _twice_. What the actual frank? What is this sorcery?!

So here’s the deal: if `setjmp()` returns `0`, it means that you’ve successfully set the “bookmark” at that point.

If it returns non-zero, it means you’ve just returned to the “bookmark” set earlier. (And the value returned is the one you pass to `longjmp()`.)

This way you can tell the difference between setting the bookmark and returning to it later.

So when the code, above, calls `setjmp()` the first time, `setjmp()` _stores_ the state in the `env` variable and returns `0`. Later when we call `longjmp()` with that same `env`, it restores the state and `setjmp()` returns the value `longjmp()` was passed.

## 34.2 Pitfalls

Under the hood, this is pretty straightforward. Typically the _stack pointer_ keeps track of the locations in memory that local variables are stored, and the _program counter_ keeps track of the address of the currently-executing instruction[181](function-specifiers-alignment-specifiersoperators.html#fn181).

So if we want to jump back to an earlier function, it’s basically only a matter of restoring the stack pointer and program counter to the values kept in the `jmp_buf` variable, and making sure the return value is set correctly. And then execution will resume there.

But a variety of factors confound this, making a significant number of undefined behavior traps.

### 34.2.1 The Values of Local Variables

If you want the values of automatic (non-`static` and non-`extern`) local variables to persist in the function that called `setjmp()` after a `longjmp()` happens, you must declare those variables to be `volatile`.

Technically, they only have to be `volatile` if they change between the time `setjmp()` is called and `longjmp()` is called[182](function-specifiers-alignment-specifiersoperators.html#fn182).

For example, if we run this code:
    
    
    [](setjmp-longjmp.html#cb677-1)int x = 20;
    [](setjmp-longjmp.html#cb677-2)
    [](setjmp-longjmp.html#cb677-3)if (setjmp(env) == 0) {
    [](setjmp-longjmp.html#cb677-4)    x = 30;
    [](setjmp-longjmp.html#cb677-5)}

and then later `longjmp()` back, the value of `x` will be indeterminate.

If we want to fix this, `x` must be `volatile`:
    
    
    [](setjmp-longjmp.html#cb678-1)volatile int x = 20;
    [](setjmp-longjmp.html#cb678-2)
    [](setjmp-longjmp.html#cb678-3)if (setjmp(env) == 0) {
    [](setjmp-longjmp.html#cb678-4)    x = 30;
    [](setjmp-longjmp.html#cb678-5)}

Now the value will be the correct `30` after a `longjmp()` returns us to this point.

### 34.2.2 How Much State is Saved?

When you `longjmp()`, execution resumes at the point of the corresponding `setjmp()`. And that’s it.

The spec points out that it’s just as if you’d jumped back into the function at that point with local variables set to whatever values they had when the `longjmp()` call was made.

Things that aren’t restored include, paraphrasing the spec:

  * Floating point status flags
  * Open files
  * Any other component of the abstract machine



### 34.2.3 You Can’t Name Anything `setjmp`

You can’t have any `extern` identifiers with the name `setjmp`. Or, if `setjmp` is a macro, you can’t undefine it.

Both are undefined behavior.

### 34.2.4 You Can’t `setjmp()` in a Larger Expression

That is, you can’t do something like this:
    
    
    [](setjmp-longjmp.html#cb679-1)if (x == 12 && setjmp(env) == 0) { ... }

That’s too complex to be allowed by the spec due to the machinations that must occur when unrolling the stack and all that. We can’t `longjmp()` back into some complex expression that’s only been partially executed.

So there are limits on the complexity of that expression.

  * It can be the entire controlling expression of the conditional.
        
        [](setjmp-longjmp.html#cb680-1)if (setjmp(env)) {...}
        
        [](setjmp-longjmp.html#cb681-1)switch (setjmp(env)) {...}

  * It can be part of a relational or equality expression, as long as the other operand is an integer constant. And the whole thing is the controlling expression of the conditional.
        
        [](setjmp-longjmp.html#cb682-1)if (setjmp(env) == 0) {...}

  * The operand to a logical NOT (`!`) operation, being the entire controlling expression.
        
        [](setjmp-longjmp.html#cb683-1)if (!setjmp(env)) {...}

  * A standalone expression, possibly cast to `void`.
        
        [](setjmp-longjmp.html#cb684-1)setjmp(env);
        
        [](setjmp-longjmp.html#cb685-1)(void)setjmp(env);




### 34.2.5 When Can’t You `longjmp()`?

It’s undefined behavior if:

  * You didn’t call `setjmp()` earlier
  * You called `setjmp()` from another thread
  * You called `setjmp()` in the scope of a variable length array (VLA), and execution left the scope of that VLA before `longjmp()` was called.
  * The function containing the `setjmp()` exited before `longjmp()` was called.



On that last one, “exited” includes normal returns from the function, as well as the case if another `longjmp()` jumped back to “earlier” in the call stack than the function in question.

### 34.2.6 You Can’t Pass `0` to `longjmp()`

If you try to pass the value `0` to `longjmp()`, it will silently change that value to `1`.

Since `setjmp()` ultimately returns this value, and having `setjmp()` return `0` has special meaning, returning `0` is prohibited.

### 34.2.7 `longjmp()` and Variable Length Arrays

If you are in scope of a VLA and `longjmp()` out there, the memory allocated to the VLA could leak[183](function-specifiers-alignment-specifiersoperators.html#fn183).

Same thing happens if you `longjmp()` back over any earlier functions that had VLAs still in scope.

This is one thing that really bugged me about VLAs—that you could write perfectly legitimate C code that squandered memory. But, hey—I’m not in charge of the spec.

* * *

[Prev](arrays-part-ii.html) | [Contents](index.html) | [Next](incomplete-types.html)

---

[Prev](setjmp-longjmp.html) | [Contents](index.html) | [Next](complex-numbers.html)

* * *

# 35 Incomplete Types

It might surprise you to learn that this builds without error:
    
    
    [](incomplete-types.html#cb686-1)extern int a[];
    [](incomplete-types.html#cb686-2)
    [](incomplete-types.html#cb686-3)int main(void)
    [](incomplete-types.html#cb686-4){
    [](incomplete-types.html#cb686-5)    struct foo *x;
    [](incomplete-types.html#cb686-6)    union bar *y;
    [](incomplete-types.html#cb686-7)    enum baz *z;
    [](incomplete-types.html#cb686-8)}

We never gave a size for `a`. And we have pointers to `struct`s `foo`, `bar`, and `baz` that never seem to be declared anywhere.

And the only warnings I get are that `x`, `y`, and `z` are unused.

These are examples of _incomplete types_.

An incomplete type is a type the size (i.e. the size you’d get back from `sizeof`) for which is not known. Another way to think of it is a type that you haven’t finished declaring.

You can have a pointer to an incomplete type, but you can’t dereference it or use pointer arithmetic on it. And you can’t `sizeof` it.

So what can you do with it?

## 35.1 Use Case: Self-Referential Structures

I only know of one real use case: forward references to `struct`s or `union`s with self-referential or co-dependent structures. (I’m going to use `struct` for the rest of these examples, but they all apply equally to `union`s, as well.)

Let’s do the classic example first.

But before I do, know this! As you declare a `struct`, the `struct` is incomplete until the closing brace is reached!
    
    
    [](incomplete-types.html#cb687-1)struct antelope {              // struct antelope is incomplete here
    [](incomplete-types.html#cb687-2)    int leg_count;             // Still incomplete
    [](incomplete-types.html#cb687-3)    float stomach_fullness;    // Still incomplete
    [](incomplete-types.html#cb687-4)    float top_speed;           // Still incomplete
    [](incomplete-types.html#cb687-5)    char *nickname;            // Still incomplete
    [](incomplete-types.html#cb687-6)};                             // NOW it's complete.

So what? Seems sane enough.

But what if we’re doing a linked list? Each linked list node needs to have a reference to another node. But how can we create a reference to another node if we haven’t finished even declaring the node yet?

C’s allowance for incomplete types makes it possible. We can’t declare a node, but we _can_ declare a pointer to one, even if it’s incomplete!
    
    
    [](incomplete-types.html#cb688-1)struct node {
    [](incomplete-types.html#cb688-2)    int val;
    [](incomplete-types.html#cb688-3)    struct node *next;  // struct node is incomplete, but that's OK!
    [](incomplete-types.html#cb688-4)};

Even though the `struct node` is incomplete on line 3, we can still declare a pointer to one[184](function-specifiers-alignment-specifiersoperators.html#fn184).

We can do the same thing if we have two different `struct`s that refer to each other:
    
    
    [](incomplete-types.html#cb689-1)struct a {
    [](incomplete-types.html#cb689-2)    struct b *x;  // Refers to a `struct b`
    [](incomplete-types.html#cb689-3)};
    [](incomplete-types.html#cb689-4)
    [](incomplete-types.html#cb689-5)struct b {
    [](incomplete-types.html#cb689-6)    struct a *x;  // Refers to a `struct a`
    [](incomplete-types.html#cb689-7)};

We’d never be able to make that pair of structures without the relaxed rules for incomplete types.

## 35.2 Incomplete Type Error Messages

Are you getting errors like these?
    
    
    [](incomplete-types.html#cb690-1)invalid application of ‘sizeof’ to incomplete type
    [](incomplete-types.html#cb690-2)
    [](incomplete-types.html#cb690-3)invalid use of undefined type
    [](incomplete-types.html#cb690-4)
    [](incomplete-types.html#cb690-5)dereferencing pointer to incomplete type

Most likely culprit: you probably forgot to `#include` the header file that declares the type.

## 35.3 Other Incomplete Types

Declaring a `struct` or `union` with no body makes an incomplete type, e.g. `struct foo;`.

`enums` are incomplete until the closing brace.

`void` is an incomplete type.

Arrays declared `extern` with no size are incomplete, e.g.:
    
    
    [](incomplete-types.html#cb691-1)extern int a[];

If it’s a non-`extern` array with no size followed by an initializer, it’s incomplete until the closing brace of the initializer.

## 35.4 Use Case: Arrays in Header Files

It can be useful to declare incomplete array types in header files. In those cases, the actual storage (where the complete array is declared) should be in a single `.c` file. If you put it in the `.h` file, it will be duplicated every time the header file is included.

So what you can do is make a header file with an incomplete type that refers to the array, like so:
    
    
    [](incomplete-types.html#cb692-1)// File: bar.h
    [](incomplete-types.html#cb692-2)
    [](incomplete-types.html#cb692-3)#ifndef BAR_H
    [](incomplete-types.html#cb692-4)#define BAR_H
    [](incomplete-types.html#cb692-5)
    [](incomplete-types.html#cb692-6)extern int my_array[];  // Incomplete type
    [](incomplete-types.html#cb692-7)
    [](incomplete-types.html#cb692-8)#endif

And the in the `.c` file, actually define the array:
    
    
    [](incomplete-types.html#cb693-1)// File: bar.c
    [](incomplete-types.html#cb693-2)
    [](incomplete-types.html#cb693-3)int my_array[1024];     // Complete type!

Then you can include the header from as many places as you’d like, and every one of those places will refer to the same underlying `my_array`.
    
    
    [](incomplete-types.html#cb694-1)// File: foo.c
    [](incomplete-types.html#cb694-2)
    [](incomplete-types.html#cb694-3)#include <stdio.h>
    [](incomplete-types.html#cb694-4)#include "bar.h"    // includes the incomplete type for my_array
    [](incomplete-types.html#cb694-5)
    [](incomplete-types.html#cb694-6)int main(void)
    [](incomplete-types.html#cb694-7){
    [](incomplete-types.html#cb694-8)    my_array[0] = 10;
    [](incomplete-types.html#cb694-9)
    [](incomplete-types.html#cb694-10)    printf("%d\n", my_array[0]);
    [](incomplete-types.html#cb694-11)}

When compiling multiple files, remember to specify all the `.c` files to the compiler, but not the `.h` files, e.g.:
    
    
    [](incomplete-types.html#cb695-1)gcc -o foo foo.c bar.c

## 35.5 Completing Incomplete Types

If you have an incomplete type, you can complete it by defining the complete `struct`, `union`, `enum`, or array in the same scope.
    
    
    [](incomplete-types.html#cb696-1)struct foo;        // incomplete type
    [](incomplete-types.html#cb696-2)
    [](incomplete-types.html#cb696-3)struct foo *p;     // pointer, no problem
    [](incomplete-types.html#cb696-4)
    [](incomplete-types.html#cb696-5)// struct foo f;   // Error: incomplete type!
    [](incomplete-types.html#cb696-6)
    [](incomplete-types.html#cb696-7)struct foo {
    [](incomplete-types.html#cb696-8)    int x, y, z;
    [](incomplete-types.html#cb696-9)};                 // Now the struct foo is complete!
    [](incomplete-types.html#cb696-10)
    [](incomplete-types.html#cb696-11)struct foo f;      // Success!

Note that though `void` is an incomplete type, there’s no way to complete it. Not that anyone ever thinks of doing that weird thing. But it does explain why you can do this:
    
    
    [](incomplete-types.html#cb697-1)void *p;             // OK: pointer to incomplete type

and not either of these:
    
    
    [](incomplete-types.html#cb698-1)void v;              // Error: declare variable of incomplete type
    [](incomplete-types.html#cb698-2)
    [](incomplete-types.html#cb698-3)printf("%d\n", *p);  // Error: dereference incomplete type

The more you know…

* * *

[Prev](setjmp-longjmp.html) | [Contents](index.html) | [Next](complex-numbers.html)

---

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

---

[Prev](complex-numbers.html) | [Contents](index.html) | [Next](date-and-time-functionality.html)

* * *

# 37 Fixed Width Integer Types

C has all those small, bigger, and biggest integer types like `int` and `long` and all that. And you can look in [the section on limits](types-ii-way-more-types.html#limits-macros) to see what the largest int is with `INT_MAX` and so on.

How big are those types? That is, how many bytes do they take up? We could use `sizeof` to get that answer.

But what if I wanted to go the other way? What if I needed a type that was exactly 32 bits (4 bytes) or at least 16 bits or somesuch?

How can we declare a type that’s a certain size?

The header `<stdint.h>` gives us a way.

## 37.1 The Bit-Sized Types

For both signed and unsigned integers, we can specify a type that is a certain number of bits, with some caveats, of course.

And there are three main classes of these types (in these examples, the `N` would be replaced by a certain number of bits):

  * Integers of exactly a certain size (`intN_t`)
  * Integers that are at least a certain size (`int_leastN_t`)
  * Integers that are at least a certain size and are as fast as possible (`int_fastN_t`)[189](function-specifiers-alignment-specifiersoperators.html#fn189)



How much faster is `fast`? Definitely maybe some amount faster. Probably. The spec doesn’t say how much faster, just that they’ll be the fastest on this architecture. Most C compilers are pretty good, though, so you’ll probably only see this used in places where the most possible speed needs to be guaranteed (rather than just hoping the compiler is producing pretty-dang-fast code, which it is).

Finally, these unsigned number types have a leading `u` to differentiate them.

For example, these types have the corresponding listed meaning:
    
    
    [](fixed-width-integer-types.html#cb716-1)int32_t w;        // w is exactly 32 bits, signed
    [](fixed-width-integer-types.html#cb716-2)uint16_t x;       // x is exactly 16 bits, unsigned
    [](fixed-width-integer-types.html#cb716-3)
    [](fixed-width-integer-types.html#cb716-4)int_least8_t y;   // y is at least 8 bits, signed
    [](fixed-width-integer-types.html#cb716-5)
    [](fixed-width-integer-types.html#cb716-6)uint_fast64_t z;  // z is the fastest representation at least 64 bits, unsigned

The following types are guaranteed to be defined:
    
    
    [](fixed-width-integer-types.html#cb717-1)int_least8_t      uint_least8_t
    [](fixed-width-integer-types.html#cb717-2)int_least16_t     uint_least16_t
    [](fixed-width-integer-types.html#cb717-3)int_least32_t     uint_least32_t
    [](fixed-width-integer-types.html#cb717-4)int_least64_t     uint_least64_t
    [](fixed-width-integer-types.html#cb717-5)
    [](fixed-width-integer-types.html#cb717-6)int_fast8_t       uint_fast8_t
    [](fixed-width-integer-types.html#cb717-7)int_fast16_t      uint_fast16_t
    [](fixed-width-integer-types.html#cb717-8)int_fast32_t      uint_fast32_t
    [](fixed-width-integer-types.html#cb717-9)int_fast64_t      uint_fast64_t

There might be others of different widths, as well, but those are optional.

Hey! Where are the fixed types like `int16_t`? Turns out those are entirely optional…unless certain conditions are met[190](function-specifiers-alignment-specifiersoperators.html#fn190). And if you have an average run-of-the-mill modern computer system, those conditions probably are met. And if they are, you’ll have these types:
    
    
    [](fixed-width-integer-types.html#cb718-1)int8_t      uint8_t
    [](fixed-width-integer-types.html#cb718-2)int16_t     uint16_t
    [](fixed-width-integer-types.html#cb718-3)int32_t     uint32_t
    [](fixed-width-integer-types.html#cb718-4)int64_t     uint64_t

Other variants with different widths might be defined, but they’re optional.

## 37.2 Maximum Integer Size Type

There’s a type you can use that holds the largest representable integers available on the system, both signed and unsigned:
    
    
    [](fixed-width-integer-types.html#cb719-1)intmax_t
    [](fixed-width-integer-types.html#cb719-2)uintmax_t

Use these types when you want to go as big as possible.

Obviously values from any other integer types of the same sign will fit in this type, necessarily.

## 37.3 Using Fixed Size Constants

If you have a constant that you want to have fit in a certain number of bits, you can use these macros to automatically append the proper suffix onto the number (e.g. `22L` or `3490ULL`).
    
    
    [](fixed-width-integer-types.html#cb720-1)INT8_C(x)     UINT8_C(x)
    [](fixed-width-integer-types.html#cb720-2)INT16_C(x)    UINT16_C(x)
    [](fixed-width-integer-types.html#cb720-3)INT32_C(x)    UINT32_C(x)
    [](fixed-width-integer-types.html#cb720-4)INT64_C(x)    UINT64_C(x)
    [](fixed-width-integer-types.html#cb720-5)INTMAX_C(x)   UINTMAX_C(x)

Again, these work only with constant integer values.

For example, we can use one of these to assign constant values like so:
    
    
    [](fixed-width-integer-types.html#cb721-1)uint16_t x = UINT16_C(12);
    [](fixed-width-integer-types.html#cb721-2)intmax_t y = INTMAX_C(3490);

## 37.4 Limits of Fixed Size Integers

We also have some limits defined so you can get the maximum and minimum values for these types:
    
    
    [](fixed-width-integer-types.html#cb722-1)INT8_MAX           INT8_MIN           UINT8_MAX
    [](fixed-width-integer-types.html#cb722-2)INT16_MAX          INT16_MIN          UINT16_MAX
    [](fixed-width-integer-types.html#cb722-3)INT32_MAX          INT32_MIN          UINT32_MAX
    [](fixed-width-integer-types.html#cb722-4)INT64_MAX          INT64_MIN          UINT64_MAX
    [](fixed-width-integer-types.html#cb722-5)
    [](fixed-width-integer-types.html#cb722-6)INT_LEAST8_MAX     INT_LEAST8_MIN     UINT_LEAST8_MAX
    [](fixed-width-integer-types.html#cb722-7)INT_LEAST16_MAX    INT_LEAST16_MIN    UINT_LEAST16_MAX
    [](fixed-width-integer-types.html#cb722-8)INT_LEAST32_MAX    INT_LEAST32_MIN    UINT_LEAST32_MAX
    [](fixed-width-integer-types.html#cb722-9)INT_LEAST64_MAX    INT_LEAST64_MIN    UINT_LEAST64_MAX
    [](fixed-width-integer-types.html#cb722-10)
    [](fixed-width-integer-types.html#cb722-11)INT_FAST8_MAX      INT_FAST8_MIN      UINT_FAST8_MAX
    [](fixed-width-integer-types.html#cb722-12)INT_FAST16_MAX     INT_FAST16_MIN     UINT_FAST16_MAX
    [](fixed-width-integer-types.html#cb722-13)INT_FAST32_MAX     INT_FAST32_MIN     UINT_FAST32_MAX
    [](fixed-width-integer-types.html#cb722-14)INT_FAST64_MAX     INT_FAST64_MIN     UINT_FAST64_MAX
    [](fixed-width-integer-types.html#cb722-15)
    [](fixed-width-integer-types.html#cb722-16)INTMAX_MAX         INTMAX_MIN         UINTMAX_MAX

Note the `MIN` for all the unsigned types is `0`, so, as such, there’s no macro for it.

## 37.5 Format Specifiers

In order to print these types, you need to send the right format specifier to `printf()`. (And the same issue for getting input with `scanf()`.)

But how are you going to know what size the types are under the hood? Luckily, once again, C provides some macros to help with this.

All this can be found in `<inttypes.h>`.

Now, we have a bunch of macros. Like a complexity explosion of macros. So I’m going to stop listing out every one and just put the lowercase letter `n` in the place where you should put `8`, `16`, `32`, or `64` depending on your needs.

Let’s look at the macros for printing signed integers:
    
    
    [](fixed-width-integer-types.html#cb723-1)PRIdn    PRIdLEASTn    PRIdFASTn    PRIdMAX
    [](fixed-width-integer-types.html#cb723-2)PRIin    PRIiLEASTn    PRIiFASTn    PRIiMAX

Look for the patterns there. You can see there are variants for the fixed, least, fast, and max types.

And you also have a lowercase `d` and a lowercase `i`. Those correspond to the `printf()` format specifiers `%d` and `%i`.

So if I have something of type:
    
    
    [](fixed-width-integer-types.html#cb724-1)int_least16_t x = 3490;

I can print that with the equivalent format specifier for `%d` by using `PRIdLEAST16`.

But how? How do we use that macro?

First of all, that macro specifies a string containing the letter or letters `printf()` needs to use to print that type. Like, for example, it could be `"d"` or `"ld"`.

So all we need to do is embed that in our format string to the `printf()` call.

To do this, we can take advantage of a fact about C that you might have forgotten: adjacent string literals are automatically concatenated to a single string. E.g.:
    
    
    [](fixed-width-integer-types.html#cb725-1)printf("Hello, " "world!\n");   // Prints "Hello, world!"

And since these macros are string literals, we can use them like so:
    
    
    [](fixed-width-integer-types.html#cb726-1)#include <stdio.h>
    [](fixed-width-integer-types.html#cb726-2)#include <stdint.h>
    [](fixed-width-integer-types.html#cb726-3)#include <inttypes.h>
    [](fixed-width-integer-types.html#cb726-4)
    [](fixed-width-integer-types.html#cb726-5)int main(void)
    [](fixed-width-integer-types.html#cb726-6){
    [](fixed-width-integer-types.html#cb726-7)    int_least16_t x = 3490;
    [](fixed-width-integer-types.html#cb726-8)
    [](fixed-width-integer-types.html#cb726-9)    printf("The value is %" PRIdLEAST16 "!\n", x);
    [](fixed-width-integer-types.html#cb726-10)}

We also have a pile of macros for printing unsigned types:
    
    
    [](fixed-width-integer-types.html#cb727-1)PRIon    PRIoLEASTn    PRIoFASTn    PRIoMAX
    [](fixed-width-integer-types.html#cb727-2)PRIun    PRIuLEASTn    PRIuFASTn    PRIuMAX
    [](fixed-width-integer-types.html#cb727-3)PRIxn    PRIxLEASTn    PRIxFASTn    PRIxMAX
    [](fixed-width-integer-types.html#cb727-4)PRIXn    PRIXLEASTn    PRIXFASTn    PRIXMAX

In this case, `o`, `u`, `x`, and `X` correspond to the documented format specifiers in `printf()`.

And, as before, the lowercase `n` should be substituted with `8`, `16`, `32`, or `64`.

But just when you think you had enough of the macros, it turns out we have a complete complementary set of them for `scanf()`!
    
    
    [](fixed-width-integer-types.html#cb728-1)SCNdn    SCNdLEASTn    SCNdFASTn    SCNdMAX
    [](fixed-width-integer-types.html#cb728-2)SCNin    SCNiLEASTn    SCNiFASTn    SCNiMAX
    [](fixed-width-integer-types.html#cb728-3)SCNon    SCNoLEASTn    SCNoFASTn    SCNoMAX
    [](fixed-width-integer-types.html#cb728-4)SCNun    SCNuLEASTn    SCNuFASTn    SCNuMAX
    [](fixed-width-integer-types.html#cb728-5)SCNxn    SCNxLEASTn    SCNxFASTn    SCNxMAX

Remember: when you want to print out a fixed size integer type with `printf()` or `scanf()`, grab the correct corresponding format specifer from `<inttypes.h>`.

* * *

[Prev](complex-numbers.html) | [Contents](index.html) | [Next](date-and-time-functionality.html)

---

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

---

[Prev](date-and-time-functionality.html) | [Contents](index.html) | [Next](chapter-atomics.html)

* * *

# 39 Multithreading

C11 introduced, formally, multithreading to the C language. It’s very eerily similar to [POSIX threads](https://en.wikipedia.org/wiki/POSIX_Threads)[197](function-specifiers-alignment-specifiersoperators.html#fn197), if you’ve ever used those.

And if you’ve not, no worries. We’ll talk it through.

Do note, however, that I’m not intending this to be a full-blown classic multithreading how-to[198](function-specifiers-alignment-specifiersoperators.html#fn198); you’ll have to pick up a different very thick book for that, specifically. Sorry!

Threading is an optional feature. If a C11+ compiler defines `__STDC_NO_THREADS__`, threads will **not** be present in the library. Why they decided to go with a negative sense in that macro is beyond me, but there we are.

You can test for it like this:
    
    
    [](multithreading.html#cb744-1)#ifdef __STDC_NO_THREADS__
    [](multithreading.html#cb744-2)#error I need threads to build this program!
    [](multithreading.html#cb744-3)#endif

Also, you might need to specify certain linker options when building. In the case of Unix-likes, try appending a `-lpthreads` to the end of the command line to link the `pthreads` library[199](function-specifiers-alignment-specifiersoperators.html#fn199):
    
    
    [](multithreading.html#cb745-1)gcc -std=c11 -o foo foo.c -lpthreads

If you’re getting linker errors on your system, it could be because the appropriate library wasn’t included.

## 39.1 Background

Threads are a way to have all those shiny CPU cores you paid for do work for you in the same program.

Normally, a C program just runs on a single CPU core. But if you know how to split up the work, you can give pieces of it to a number of threads and have them do the work simultaneously.

Though the spec doesn’t say it, on your system it’s very likely that C (or the OS at its behest) will attempt to balance the threads over all your CPU cores.

And if you have more threads than cores, that’s OK. You just won’t realize all those gains if they’re all trying to compete for CPU time.

## 39.2 Things You Can Do

You can create a thread. It will begin running the function you specify. The parent thread that spawned it will also continue to run.

And you can wait for the thread to complete. This is called _joining_.

Or if you don’t care when the thread completes and don’t want to wait, you can _detach it_.

A thread can explicitly _exit_ , or it can implicitly call it quits by returning from its main function.

A thread can also _sleep_ for a period of time, doing nothing while other threads run.

The `main()` program is a thread, as well.

Additionally, we have thread local storage, mutexes, and conditional variables. But more on those later. Let’s just look at the basics for now.

## 39.3 Data Races and the Standard Library

Some of the functions in the standard library (e.g. `asctime()` and `strtok()`) return or use `static` data elements that aren’t threadsafe. But in general unless it’s said otherwise, the standard library makes an effort to be so[200](function-specifiers-alignment-specifiersoperators.html#fn200).

But keep an eye out. If a standard library function is maintaining state between calls in a variable you don’t own, or if a function is returning a pointer to a thing that you didn’t pass in, it’s not threadsafe.

## 39.4 Creating and Waiting for Threads

Let’s hack something up!

We’ll make some threads (create) and wait for them to complete (join).

We have a tiny bit to understand first, though.

Every single thread is identified by an opaque variable of type `thrd_t`. It’s a unique identifier per thread in your program. When you create a thread, it’s given a new ID.

Also when you make the thread, you have to give it a pointer to a function to run, and a pointer to an argument to pass to it (or `NULL` if you don’t have anything to pass).

The thread will begin execution on the function you specify.

When you want to wait for a thread to complete, you have to specify its thread ID so C knows which one to wait for.

So the basic idea is:

  1. Write a function to act as the thread’s “`main`”. It’s not `main()`-proper, but analogous to it. The thread will start running there.
  2. From the main thread, launch a new thread with `thrd_create()`, and pass it a pointer to the function to run.
  3. In that function, have the thread do whatever it has to do.
  4. Meantimes, the main thread can continue doing whatever _it_ has to do.
  5. When the main thread decides to, it can wait for the child thread to complete by calling `thrd_join()`. Generally you **must** `thrd_join()` the thread to clean up after it or else you’ll leak memory[201](function-specifiers-alignment-specifiersoperators.html#fn201)



`thrd_create()` takes a pointer to the function to run, and it’s of type `thrd_start_t`, which is `int (*)(void *)`. That’s Greek for “a pointer to a function that takes an `void*` as an argument, and returns an `int`.”

Let’s make a thread! We’ll launch it from the main thread with `thrd_create()` to run a function, do some other things, then wait for it to complete with `thrd_join()`. I’ve named the thread’s main function `run()`, but you can name it anything as long as the types match `thrd_start_t`.
    
    
    [](multithreading.html#cb746-1)#include <stdio.h>
    [](multithreading.html#cb746-2)#include <threads.h>
    [](multithreading.html#cb746-3)
    [](multithreading.html#cb746-4)// This is the function the thread will run. It can be called anything.
    [](multithreading.html#cb746-5)//
    [](multithreading.html#cb746-6)// arg is the argument pointer passed to `thrd_create()`.
    [](multithreading.html#cb746-7)//
    [](multithreading.html#cb746-8)// The parent thread will get the return value back from `thrd_join()`'
    [](multithreading.html#cb746-9)// later.
    [](multithreading.html#cb746-10)
    [](multithreading.html#cb746-11)int run(void *arg)
    [](multithreading.html#cb746-12){
    [](multithreading.html#cb746-13)    int *a = arg;  // We'll pass in an int* from thrd_create()
    [](multithreading.html#cb746-14)
    [](multithreading.html#cb746-15)    printf("THREAD: Running thread with arg %d\n", *a);
    [](multithreading.html#cb746-16)
    [](multithreading.html#cb746-17)    return 12;  // Value to be picked up by thrd_join() (chose 12 at random)
    [](multithreading.html#cb746-18)}
    [](multithreading.html#cb746-19)
    [](multithreading.html#cb746-20)int main(void)
    [](multithreading.html#cb746-21){
    [](multithreading.html#cb746-22)    thrd_t t;  // t will hold the thread ID
    [](multithreading.html#cb746-23)    int arg = 3490;
    [](multithreading.html#cb746-24)
    [](multithreading.html#cb746-25)    printf("Launching a thread\n");
    [](multithreading.html#cb746-26)
    [](multithreading.html#cb746-27)    // Launch a thread to the run() function, passing a pointer to 3490
    [](multithreading.html#cb746-28)    // as an argument. Also stored the thread ID in t:
    [](multithreading.html#cb746-29)
    [](multithreading.html#cb746-30)    thrd_create(&t, run, &arg);
    [](multithreading.html#cb746-31)
    [](multithreading.html#cb746-32)    printf("Doing other things while the thread runs\n");
    [](multithreading.html#cb746-33)
    [](multithreading.html#cb746-34)    printf("Waiting for thread to complete...\n");
    [](multithreading.html#cb746-35)
    [](multithreading.html#cb746-36)    int res;  // Holds return value from the thread exit
    [](multithreading.html#cb746-37)
    [](multithreading.html#cb746-38)    // Wait here for the thread to complete; store the return value
    [](multithreading.html#cb746-39)    // in res:
    [](multithreading.html#cb746-40)
    [](multithreading.html#cb746-41)    thrd_join(t, &res);
    [](multithreading.html#cb746-42)
    [](multithreading.html#cb746-43)    printf("Thread exited with return value %d\n", res);
    [](multithreading.html#cb746-44)}

See how we did the `thrd_create()` there to call the `run()` function? Then we did other things in `main()` and then stopped and waited for the thread to complete with `thrd_join()`.

Sample output (yours might vary):
    
    
    [](multithreading.html#cb747-1)Launching a thread
    [](multithreading.html#cb747-2)Doing other things while the thread runs
    [](multithreading.html#cb747-3)Waiting for thread to complete...
    [](multithreading.html#cb747-4)THREAD: Running thread with arg 3490
    [](multithreading.html#cb747-5)Thread exited with return value 12

The `arg` that you pass to the function has to have a lifetime long enough so that the thread can pick it up before it goes away. Also, it needs to not be overwritten by the main thread before the new thread can use it.

Let’s look at an example that launches 5 threads. One thing to note here is how we use an array of `thrd_t`s to keep track of all the thread IDs.
    
    
    [](multithreading.html#cb748-1)#include <stdio.h>
    [](multithreading.html#cb748-2)#include <threads.h>
    [](multithreading.html#cb748-3)
    [](multithreading.html#cb748-4)int run(void *arg)
    [](multithreading.html#cb748-5){
    [](multithreading.html#cb748-6)    int i = *(int*)arg;
    [](multithreading.html#cb748-7)
    [](multithreading.html#cb748-8)    printf("THREAD %d: running!\n", i);
    [](multithreading.html#cb748-9)
    [](multithreading.html#cb748-10)    return i;
    [](multithreading.html#cb748-11)}
    [](multithreading.html#cb748-12)
    [](multithreading.html#cb748-13)#define THREAD_COUNT 5
    [](multithreading.html#cb748-14)
    [](multithreading.html#cb748-15)int main(void)
    [](multithreading.html#cb748-16){
    [](multithreading.html#cb748-17)    thrd_t t[THREAD_COUNT];
    [](multithreading.html#cb748-18)
    [](multithreading.html#cb748-19)    int i;
    [](multithreading.html#cb748-20)
    [](multithreading.html#cb748-21)    printf("Launching threads...\n");
    [](multithreading.html#cb748-22)    for (i = 0; i < THREAD_COUNT; i++)
    [](multithreading.html#cb748-23)
    [](multithreading.html#cb748-24)        // NOTE! In the following line, we pass a pointer to i, 
    [](multithreading.html#cb748-25)        // but each thread sees the same pointer. So they'll
    [](multithreading.html#cb748-26)        // print out weird things as i changes value here in
    [](multithreading.html#cb748-27)        // the main thread! (More in the text, below.)
    [](multithreading.html#cb748-28)
    [](multithreading.html#cb748-29)        thrd_create(t + i, run, &i);
    [](multithreading.html#cb748-30)
    [](multithreading.html#cb748-31)    printf("Doing other things while the thread runs...\n");
    [](multithreading.html#cb748-32)    printf("Waiting for thread to complete...\n");
    [](multithreading.html#cb748-33)
    [](multithreading.html#cb748-34)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb748-35)        int res;
    [](multithreading.html#cb748-36)        thrd_join(t[i], &res);
    [](multithreading.html#cb748-37)
    [](multithreading.html#cb748-38)        printf("Thread %d complete!\n", res);
    [](multithreading.html#cb748-39)    }
    [](multithreading.html#cb748-40)
    [](multithreading.html#cb748-41)    printf("All threads complete!\n");
    [](multithreading.html#cb748-42)}

When I run the threads, I count `i` up from 0 to 4. And pass a pointer to it to `thrd_create()`. This pointer ends up in the `run()` routine where we make a copy of it.

Simple enough? Here’s the output:
    
    
    [](multithreading.html#cb749-1)Launching threads...
    [](multithreading.html#cb749-2)THREAD 2: running!
    [](multithreading.html#cb749-3)THREAD 3: running!
    [](multithreading.html#cb749-4)THREAD 4: running!
    [](multithreading.html#cb749-5)THREAD 2: running!
    [](multithreading.html#cb749-6)Doing other things while the thread runs...
    [](multithreading.html#cb749-7)Waiting for thread to complete...
    [](multithreading.html#cb749-8)Thread 2 complete!
    [](multithreading.html#cb749-9)Thread 2 complete!
    [](multithreading.html#cb749-10)THREAD 5: running!
    [](multithreading.html#cb749-11)Thread 3 complete!
    [](multithreading.html#cb749-12)Thread 4 complete!
    [](multithreading.html#cb749-13)Thread 5 complete!
    [](multithreading.html#cb749-14)All threads complete!

Whaaa—? Where’s `THREAD 0`? And why do we have a `THREAD 5` when clearly `i` is never more than `4` when we call `thrd_create()`? And two `THREAD 2`s? Madness!

This is getting into the fun land of _race conditions_. The main thread is modifying `i` before the thread has a chance to copy it. Indeed, `i` makes it all the way to `5` and ends the loop before the last thread gets a chance to copy it.

We’ve got to have a per-thread variable that we can refer to so we can pass it in as the `arg`.

We could have a big array of them. Or we could `malloc()` space (and free it somewhere—maybe in the thread itself.)

Let’s give that a shot:
    
    
    [](multithreading.html#cb750-1)#include <stdio.h>
    [](multithreading.html#cb750-2)#include <stdlib.h>
    [](multithreading.html#cb750-3)#include <threads.h>
    [](multithreading.html#cb750-4)
    [](multithreading.html#cb750-5)int run(void *arg)
    [](multithreading.html#cb750-6){
    [](multithreading.html#cb750-7)    int i = *(int*)arg;  // Copy the arg
    [](multithreading.html#cb750-8)
    [](multithreading.html#cb750-9)    free(arg);  // Done with this
    [](multithreading.html#cb750-10)
    [](multithreading.html#cb750-11)    printf("THREAD %d: running!\n", i);
    [](multithreading.html#cb750-12)
    [](multithreading.html#cb750-13)    return i;
    [](multithreading.html#cb750-14)}
    [](multithreading.html#cb750-15)
    [](multithreading.html#cb750-16)#define THREAD_COUNT 5
    [](multithreading.html#cb750-17)
    [](multithreading.html#cb750-18)int main(void)
    [](multithreading.html#cb750-19){
    [](multithreading.html#cb750-20)    thrd_t t[THREAD_COUNT];
    [](multithreading.html#cb750-21)
    [](multithreading.html#cb750-22)    int i;
    [](multithreading.html#cb750-23)
    [](multithreading.html#cb750-24)    printf("Launching threads...\n");
    [](multithreading.html#cb750-25)    for (i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb750-26)
    [](multithreading.html#cb750-27)        // Get some space for a per-thread argument:
    [](multithreading.html#cb750-28)
    [](multithreading.html#cb750-29)        int *arg = malloc(sizeof *arg);
    [](multithreading.html#cb750-30)        *arg = i;
    [](multithreading.html#cb750-31)
    [](multithreading.html#cb750-32)        thrd_create(t + i, run, arg);
    [](multithreading.html#cb750-33)    }
    [](multithreading.html#cb750-34)
    [](multithreading.html#cb750-35)    // ...

Notice on lines 27-30 we `malloc()` space for an `int` and copy the value of `i` into it. Each new thread gets its own freshly-`malloc()`d variable and we pass a pointer to that to the `run()` function.

Once `run()` makes its own copy of the `arg` on line 7, it `free()`s the `malloc()`d `int`. And now that it has its own copy, it can do with it what it pleases.

And a run shows the result:
    
    
    [](multithreading.html#cb751-1)Launching threads...
    [](multithreading.html#cb751-2)THREAD 0: running!
    [](multithreading.html#cb751-3)THREAD 1: running!
    [](multithreading.html#cb751-4)THREAD 2: running!
    [](multithreading.html#cb751-5)THREAD 3: running!
    [](multithreading.html#cb751-6)Doing other things while the thread runs...
    [](multithreading.html#cb751-7)Waiting for thread to complete...
    [](multithreading.html#cb751-8)Thread 0 complete!
    [](multithreading.html#cb751-9)Thread 1 complete!
    [](multithreading.html#cb751-10)Thread 2 complete!
    [](multithreading.html#cb751-11)Thread 3 complete!
    [](multithreading.html#cb751-12)THREAD 4: running!
    [](multithreading.html#cb751-13)Thread 4 complete!
    [](multithreading.html#cb751-14)All threads complete!

There we go! Threads 0-4 all in effect!

Your run might vary—how the threads get scheduled to run is beyond the C spec. We see in the above example that thread 4 didn’t even begin until threads 0-1 had completed. Indeed, if I run this again, I likely get different output. We cannot guarantee a thread execution order.

## 39.5 Detaching Threads

If you want to fire-and-forget a thread (i.e. so you don’t have to `thrd_join()` it later), you can do that with `thrd_detach()`.

This removes the parent thread’s ability to get the return value from the child thread, but if you don’t care about that and just want threads to clean up nicely on their own, this is the way to go.

Basically we’re going to do this:
    
    
    [](multithreading.html#cb752-1)thrd_create(&t, run, NULL);
    [](multithreading.html#cb752-2)thrd_detach(t);

where the `thrd_detach()` call is the parent thread saying, “Hey, I’m not going to wait for this child thread to complete with `thrd_join()`. So go ahead and clean it up on your own when it completes.”
    
    
    [](multithreading.html#cb753-1)#include <stdio.h>
    [](multithreading.html#cb753-2)#include <threads.h>
    [](multithreading.html#cb753-3)
    [](multithreading.html#cb753-4)int run(void *arg)
    [](multithreading.html#cb753-5){
    [](multithreading.html#cb753-6)    (void)arg;
    [](multithreading.html#cb753-7)
    [](multithreading.html#cb753-8)    //printf("Thread running! %lu\n", thrd_current()); // non-portable!
    [](multithreading.html#cb753-9)    printf("Thread running!\n");
    [](multithreading.html#cb753-10)
    [](multithreading.html#cb753-11)    return 0;
    [](multithreading.html#cb753-12)}
    [](multithreading.html#cb753-13)
    [](multithreading.html#cb753-14)#define THREAD_COUNT 10
    [](multithreading.html#cb753-15)
    [](multithreading.html#cb753-16)int main(void)
    [](multithreading.html#cb753-17){
    [](multithreading.html#cb753-18)    thrd_t t;
    [](multithreading.html#cb753-19)
    [](multithreading.html#cb753-20)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb753-21)        thrd_create(&t, run, NULL);
    [](multithreading.html#cb753-22)        thrd_detach(t);               // <-- DETACH!
    [](multithreading.html#cb753-23)    }
    [](multithreading.html#cb753-24)
    [](multithreading.html#cb753-25)    // Sleep for a second to let all the threads finish
    [](multithreading.html#cb753-26)    thrd_sleep(&(struct timespec){.tv_sec=1}, NULL);
    [](multithreading.html#cb753-27)}

Note that in this code, we put the main thread to sleep for 1 second with `thrd_sleep()`—more on that later.

Also in the `run()` function, I have a commented-out line in there that prints out the thread ID as an `unsigned long`. This is non-portable, because the spec doesn’t say what type a `thrd_t` is under the hood—it could be a `struct` for all we know. But that line works on my system.

Something interesting I saw when I ran the code, above, and printed out the thread IDs was that some threads had duplicate IDs! This seems like it should be impossible, but C is allowed to _reuse_ thread IDs after the corresponding thread has exited. So what I was seeing was that some threads completed their run before other threads were launched.

## 39.6 Thread Local Data

Threads are interesting because they don’t have their own memory beyond local variables. If you want a `static` variable or file scope variable, all threads will see that same variable.

This can lead to race conditions, where you get _Weird Things_ ™ happening.

Check out this example. We have a `static` variable `foo` in block scope in `run()`. This variable will be visible to all threads that pass through the `run()` function. And the various threads can effectively step on each others toes.

Each thread copies `foo` into a local variable `x` (which is not shared between threads—all the threads have their own call stacks). So they _should_ be the same, right?

And the first time we print them, they are[202](function-specifiers-alignment-specifiersoperators.html#fn202). But then right after that, we check to make sure they’re still the same.

And they _usually_ are. But not always!
    
    
    [](multithreading.html#cb754-1)#include <stdio.h>
    [](multithreading.html#cb754-2)#include <stdlib.h>
    [](multithreading.html#cb754-3)#include <threads.h>
    [](multithreading.html#cb754-4)
    [](multithreading.html#cb754-5)int run(void *arg)
    [](multithreading.html#cb754-6){
    [](multithreading.html#cb754-7)    int n = *(int*)arg;  // Thread number for humans to differentiate
    [](multithreading.html#cb754-8)
    [](multithreading.html#cb754-9)    free(arg);
    [](multithreading.html#cb754-10)
    [](multithreading.html#cb754-11)    static int foo = 10;  // Static value shared between threads
    [](multithreading.html#cb754-12)
    [](multithreading.html#cb754-13)    int x = foo;  // Automatic local variable--each thread has its own
    [](multithreading.html#cb754-14)
    [](multithreading.html#cb754-15)    // We just assigned x from foo, so they'd better be equal here.
    [](multithreading.html#cb754-16)    // (In all my test runs, they were, but even this isn't guaranteed!)
    [](multithreading.html#cb754-17)
    [](multithreading.html#cb754-18)    printf("Thread %d: x = %d, foo = %d\n", n, x, foo);
    [](multithreading.html#cb754-19)
    [](multithreading.html#cb754-20)    // And they should be equal here, but they're not always!
    [](multithreading.html#cb754-21)    // (Sometimes they were, sometimes they weren't!)
    [](multithreading.html#cb754-22)
    [](multithreading.html#cb754-23)    // What happens is another thread gets in and increments foo
    [](multithreading.html#cb754-24)    // right now, but this thread's x remains what it was before!
    [](multithreading.html#cb754-25)
    [](multithreading.html#cb754-26)    if (x != foo) {
    [](multithreading.html#cb754-27)        printf("Thread %d: Craziness! x != foo! %d != %d\n", n, x, foo);
    [](multithreading.html#cb754-28)    }
    [](multithreading.html#cb754-29)
    [](multithreading.html#cb754-30)    foo++;  // Increment shared value
    [](multithreading.html#cb754-31)
    [](multithreading.html#cb754-32)    return 0;
    [](multithreading.html#cb754-33)}
    [](multithreading.html#cb754-34)
    [](multithreading.html#cb754-35)#define THREAD_COUNT 5
    [](multithreading.html#cb754-36)
    [](multithreading.html#cb754-37)int main(void)
    [](multithreading.html#cb754-38){
    [](multithreading.html#cb754-39)    thrd_t t[THREAD_COUNT];
    [](multithreading.html#cb754-40)
    [](multithreading.html#cb754-41)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb754-42)        int *n = malloc(sizeof *n);  // Holds a thread serial number
    [](multithreading.html#cb754-43)        *n = i;
    [](multithreading.html#cb754-44)        thrd_create(t + i, run, n);
    [](multithreading.html#cb754-45)    }
    [](multithreading.html#cb754-46)
    [](multithreading.html#cb754-47)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb754-48)        thrd_join(t[i], NULL);
    [](multithreading.html#cb754-49)    }
    [](multithreading.html#cb754-50)}

Here’s an example output (though this varies from run to run):
    
    
    [](multithreading.html#cb755-1)Thread 0: x = 10, foo = 10
    [](multithreading.html#cb755-2)Thread 1: x = 10, foo = 10
    [](multithreading.html#cb755-3)Thread 1: Craziness! x != foo! 10 != 11
    [](multithreading.html#cb755-4)Thread 2: x = 12, foo = 12
    [](multithreading.html#cb755-5)Thread 4: x = 13, foo = 13
    [](multithreading.html#cb755-6)Thread 3: x = 14, foo = 14

In thread 1, between the two `printf()`s, the value of `foo` somehow changed from `10` to `11`, even though clearly there’s no increment between the `printf()`s!

It was another thread that got in there (probably thread 0, from the look of it) and incremented the value of `foo` behind thread 1’s back!

Let’s solve this problem two different ways. (If you want all the threads to share the variable _and_ not step on each other’s toes, you’ll have to read on to the [mutex](multithreading.html#mutex) section.)

### 39.6.1 `_Thread_local` Storage-Class

First things first, let’s just look at the easy way around this: the `_Thread_local` storage-class.

Basically we’re just going to slap this on the front of our block scope `static` variable and things will work! It tells C that every thread should have its own version of this variable, so none of them step on each other’s toes.

The `<threads.h>` header defines `thread_local` as an alias to `_Thread_local` so your code doesn’t have to look so ugly.

Let’s take the previous example and make `foo` into a `thread_local` variable so that we don’t share that data.
    
    
    [](multithreading.html#cb756-5)int run(void *arg)
    [](multithreading.html#cb756-6){
    [](multithreading.html#cb756-7)    int n = *(int*)arg;  // Thread number for humans to differentiate
    [](multithreading.html#cb756-8)
    [](multithreading.html#cb756-9)    free(arg);
    [](multithreading.html#cb756-10)
    [](multithreading.html#cb756-11)    thread_local static int foo = 10;  // <-- No longer shared!!

And running we get:
    
    
    [](multithreading.html#cb757-1)Thread 0: x = 10, foo = 10
    [](multithreading.html#cb757-2)Thread 1: x = 10, foo = 10
    [](multithreading.html#cb757-3)Thread 2: x = 10, foo = 10
    [](multithreading.html#cb757-4)Thread 4: x = 10, foo = 10
    [](multithreading.html#cb757-5)Thread 3: x = 10, foo = 10

No more weird problems!

One thing: if a `thread_local` variable is block scope, it **must** be `static`. Them’s the rules. (But this is OK because non-`static` variables are per-thread already since each thread has it’s own non-`static` variables.)

A bit of a lie there: block scope `thread_local` variables can also be `extern`.

### 39.6.2 Another Option: Thread-Specific Storage

Thread-specific storage (TSS) is another way of getting per-thread data.

One additional feature is that these functions allow you to specify a destructor that will be called on the data when the TSS variable is deleted. Commonly this destructor is `free()` to automatically clean up `malloc()`d per-thread data. Or `NULL` if you don’t need to destroy anything.

The destructor is type `tss_dtor_t` which is a pointer to a function that returns `void` and takes a `void*` as an argument (the `void*` points to the data stored in the variable). In other words, it’s a `void (*)(void*)`, if that clears it up. Which I admit it probably doesn’t. Check out the example, below.

Generally, `thread_local` is probably your go-to, but if you like the destructor idea, then you can make use of that.

The usage is a bit weird in that we need a variable of type `tss_t` to be alive to represent the value on a per thread basis. Then we initialize it with `tss_create()`. Eventually we get rid of it with `tss_delete()`. Note that calling `tss_delete()` doesn’t run all the destructors—it’s `thrd_exit()` (or returning from the run function) that does that. `tss_delete()` just releases any memory allocated by `tss_create()`. 

In the middle, threads can call `tss_set()` and `tss_get()` to set and get the value.

In the following code, we set up the TSS variable before creating the threads, then clean up after the threads.

In the `run()` function, the threads `malloc()` some space for a string and store that pointer in the TSS variable.

When the thread exits, the destructor function (`free()` in this case) is called for _all_ the threads.
    
    
    [](multithreading.html#cb758-1)#include <stdio.h>
    [](multithreading.html#cb758-2)#include <stdlib.h>
    [](multithreading.html#cb758-3)#include <threads.h>
    [](multithreading.html#cb758-4)
    [](multithreading.html#cb758-5)tss_t str;
    [](multithreading.html#cb758-6)
    [](multithreading.html#cb758-7)void some_function(void)
    [](multithreading.html#cb758-8){
    [](multithreading.html#cb758-9)    // Retrieve the per-thread value of this string
    [](multithreading.html#cb758-10)    char *tss_string = tss_get(str);
    [](multithreading.html#cb758-11)
    [](multithreading.html#cb758-12)    // And print it
    [](multithreading.html#cb758-13)    printf("TSS string: %s\n", tss_string);
    [](multithreading.html#cb758-14)}
    [](multithreading.html#cb758-15)
    [](multithreading.html#cb758-16)int run(void *arg)
    [](multithreading.html#cb758-17){
    [](multithreading.html#cb758-18)    int serial = *(int*)arg;  // Get this thread's serial number
    [](multithreading.html#cb758-19)    free(arg);
    [](multithreading.html#cb758-20)
    [](multithreading.html#cb758-21)    // malloc() space to hold the data for this thread
    [](multithreading.html#cb758-22)    char *s = malloc(64);
    [](multithreading.html#cb758-23)    sprintf(s, "thread %d! :)", serial);  // Happy little string
    [](multithreading.html#cb758-24)
    [](multithreading.html#cb758-25)    // Set this TSS variable to point at the string
    [](multithreading.html#cb758-26)    tss_set(str, s);
    [](multithreading.html#cb758-27)
    [](multithreading.html#cb758-28)    // Call a function that will get the variable
    [](multithreading.html#cb758-29)    some_function();
    [](multithreading.html#cb758-30)
    [](multithreading.html#cb758-31)    return 0;   // Equivalent to thrd_exit(0)
    [](multithreading.html#cb758-32)}
    [](multithreading.html#cb758-33)
    [](multithreading.html#cb758-34)#define THREAD_COUNT 15
    [](multithreading.html#cb758-35)
    [](multithreading.html#cb758-36)int main(void)
    [](multithreading.html#cb758-37){
    [](multithreading.html#cb758-38)    thrd_t t[THREAD_COUNT];
    [](multithreading.html#cb758-39)
    [](multithreading.html#cb758-40)    // Make a new TSS variable, the free() function is the destructor
    [](multithreading.html#cb758-41)    tss_create(&str, free);
    [](multithreading.html#cb758-42)
    [](multithreading.html#cb758-43)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb758-44)        int *n = malloc(sizeof *n);  // Holds a thread serial number
    [](multithreading.html#cb758-45)        *n = i;
    [](multithreading.html#cb758-46)        thrd_create(t + i, run, n);
    [](multithreading.html#cb758-47)    }
    [](multithreading.html#cb758-48)
    [](multithreading.html#cb758-49)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb758-50)        thrd_join(t[i], NULL);
    [](multithreading.html#cb758-51)    }
    [](multithreading.html#cb758-52)
    [](multithreading.html#cb758-53)    // All threads are done, so we're done with this
    [](multithreading.html#cb758-54)    tss_delete(str);
    [](multithreading.html#cb758-55)}

Again, this is kind of a painful way of doing things compared to `thread_local`, so unless you really need that destructor functionality, I’d use that instead.

## 39.7 Mutexes

If you want to only allow a single thread into a critical section of code at a time, you can protect that section with a mutex[203](function-specifiers-alignment-specifiersoperators.html#fn203).

For example, if we had a `static` variable and we wanted to be able to get and set it in two operations without another thread jumping in the middle and corrupting it, we could use a mutex for that.

You can acquire a mutex or release it. If you attempt to acquire the mutex and succeed, you may continue execution. If you attempt and fail (because someone else holds it), you will _block_[ 204](function-specifiers-alignment-specifiersoperators.html#fn204) until the mutex is released.

If multiple threads are blocked waiting for a mutex to be released, one of them will be chosen to run (at random, from our perspective), and the others will continue to sleep.

The gameplan is that first we’ll initialize a mutex variable to make it ready to use with `mtx_init()`.

Then subsequent threads can call `mtx_lock()` and `mtx_unlock()` to get and release the mutex.

When we’re completely done with the mutex, we can destroy it with `mtx_destroy()`, the logical opposite of `mtx_init()`.

First, let’s look at some code that does _not_ use a mutex, and endeavors to print out a shared (`static`) serial number and then increment it. Because we’re not using a mutex over the getting of the value (to print it) and the setting (to increment it), threads might get in each other’s way in that critical section.
    
    
    [](multithreading.html#cb759-1)#include <stdio.h>
    [](multithreading.html#cb759-2)#include <threads.h>
    [](multithreading.html#cb759-3)
    [](multithreading.html#cb759-4)int run(void *arg)
    [](multithreading.html#cb759-5){
    [](multithreading.html#cb759-6)    (void)arg;
    [](multithreading.html#cb759-7)
    [](multithreading.html#cb759-8)    static int serial = 0;   // Shared static variable!
    [](multithreading.html#cb759-9)
    [](multithreading.html#cb759-10)    printf("Thread running! %d\n", serial);
    [](multithreading.html#cb759-11)
    [](multithreading.html#cb759-12)    serial++;
    [](multithreading.html#cb759-13)
    [](multithreading.html#cb759-14)    return 0;
    [](multithreading.html#cb759-15)}
    [](multithreading.html#cb759-16)
    [](multithreading.html#cb759-17)#define THREAD_COUNT 10
    [](multithreading.html#cb759-18)
    [](multithreading.html#cb759-19)int main(void)
    [](multithreading.html#cb759-20){
    [](multithreading.html#cb759-21)    thrd_t t[THREAD_COUNT];
    [](multithreading.html#cb759-22)
    [](multithreading.html#cb759-23)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb759-24)        thrd_create(t + i, run, NULL);
    [](multithreading.html#cb759-25)    }
    [](multithreading.html#cb759-26)
    [](multithreading.html#cb759-27)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb759-28)        thrd_join(t[i], NULL);
    [](multithreading.html#cb759-29)    }
    [](multithreading.html#cb759-30)}

When I run this, I get something that looks like this:
    
    
    [](multithreading.html#cb760-1)Thread running! 0
    [](multithreading.html#cb760-2)Thread running! 0
    [](multithreading.html#cb760-3)Thread running! 0
    [](multithreading.html#cb760-4)Thread running! 3
    [](multithreading.html#cb760-5)Thread running! 4
    [](multithreading.html#cb760-6)Thread running! 5
    [](multithreading.html#cb760-7)Thread running! 6
    [](multithreading.html#cb760-8)Thread running! 7
    [](multithreading.html#cb760-9)Thread running! 8
    [](multithreading.html#cb760-10)Thread running! 9

Clearly multiple threads are getting in there and running the `printf()` before anyone gets a change to update the `serial` variable.

What we want to do is wrap the getting of the variable and setting of it into a single mutex-protected stretch of code.

We’ll add a new variable to represent the mutex of type `mtx_t` in file scope, initialize it, and then the threads can lock and unlock it in the `run()` function.
    
    
    [](multithreading.html#cb761-1)#include <stdio.h>
    [](multithreading.html#cb761-2)#include <threads.h>
    [](multithreading.html#cb761-3)
    [](multithreading.html#cb761-4)mtx_t serial_mtx;     // <-- MUTEX VARIABLE
    [](multithreading.html#cb761-5)
    [](multithreading.html#cb761-6)int run(void *arg)
    [](multithreading.html#cb761-7){
    [](multithreading.html#cb761-8)    (void)arg;
    [](multithreading.html#cb761-9)
    [](multithreading.html#cb761-10)    static int serial = 0;   // Shared static variable!
    [](multithreading.html#cb761-11)
    [](multithreading.html#cb761-12)    // Acquire the mutex--all threads will block on this call until
    [](multithreading.html#cb761-13)    // they get the lock:
    [](multithreading.html#cb761-14)
    [](multithreading.html#cb761-15)    mtx_lock(&serial_mtx);           // <-- ACQUIRE MUTEX
    [](multithreading.html#cb761-16)
    [](multithreading.html#cb761-17)    printf("Thread running! %d\n", serial);
    [](multithreading.html#cb761-18)
    [](multithreading.html#cb761-19)    serial++;
    [](multithreading.html#cb761-20)
    [](multithreading.html#cb761-21)    // Done getting and setting the data, so free the lock. This will
    [](multithreading.html#cb761-22)    // unblock threads on the mtx_lock() call:
    [](multithreading.html#cb761-23)
    [](multithreading.html#cb761-24)    mtx_unlock(&serial_mtx);         // <-- RELEASE MUTEX
    [](multithreading.html#cb761-25)
    [](multithreading.html#cb761-26)    return 0;
    [](multithreading.html#cb761-27)}
    [](multithreading.html#cb761-28)
    [](multithreading.html#cb761-29)#define THREAD_COUNT 10
    [](multithreading.html#cb761-30)
    [](multithreading.html#cb761-31)int main(void)
    [](multithreading.html#cb761-32){
    [](multithreading.html#cb761-33)    thrd_t t[THREAD_COUNT];
    [](multithreading.html#cb761-34)
    [](multithreading.html#cb761-35)    // Initialize the mutex variable, indicating this is a normal
    [](multithreading.html#cb761-36)    // no-frills, mutex:
    [](multithreading.html#cb761-37)
    [](multithreading.html#cb761-38)    mtx_init(&serial_mtx, mtx_plain);        // <-- CREATE MUTEX
    [](multithreading.html#cb761-39)
    [](multithreading.html#cb761-40)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb761-41)        thrd_create(t + i, run, NULL);
    [](multithreading.html#cb761-42)    }
    [](multithreading.html#cb761-43)
    [](multithreading.html#cb761-44)    for (int i = 0; i < THREAD_COUNT; i++) {
    [](multithreading.html#cb761-45)        thrd_join(t[i], NULL);
    [](multithreading.html#cb761-46)    }
    [](multithreading.html#cb761-47)
    [](multithreading.html#cb761-48)    // Done with the mutex, destroy it:
    [](multithreading.html#cb761-49)
    [](multithreading.html#cb761-50)    mtx_destroy(&serial_mtx);                // <-- DESTROY MUTEX
    [](multithreading.html#cb761-51)}

See how on lines 38 and 50 of `main()` we initialize and destroy the mutex.

But each individual thread acquires the mutex on line 15 and releases it on line 24.

In between the `mtx_lock()` and `mtx_unlock()` is the _critical section_ , the area of code where we don’t want multiple threads mucking about at the same time.

And now we get proper output!
    
    
    [](multithreading.html#cb762-1)Thread running! 0
    [](multithreading.html#cb762-2)Thread running! 1
    [](multithreading.html#cb762-3)Thread running! 2
    [](multithreading.html#cb762-4)Thread running! 3
    [](multithreading.html#cb762-5)Thread running! 4
    [](multithreading.html#cb762-6)Thread running! 5
    [](multithreading.html#cb762-7)Thread running! 6
    [](multithreading.html#cb762-8)Thread running! 7
    [](multithreading.html#cb762-9)Thread running! 8
    [](multithreading.html#cb762-10)Thread running! 9

If you need multiple mutexes, no problem: just have multiple mutex variables.

And always remember the Number One Rule of Multiple Mutexes: _Unlock mutexes in the opposite order in which you lock them!_

### 39.7.1 Different Mutex Types

As hinted earlier, we have a few mutex types that you can create with `mtx_init()`. (Some of these types are the result of a bitwise-OR operation, as noted in the table.)

Type | Description  
---|---  
`mtx_plain` | Regular ol’ mutex  
`mtx_timed` | Mutex that supports timeouts  
`mtx_plain|mtx_recursive` | Recursive mutex  
`mtx_timed|mtx_recursive` | Recursive mutex that supports timeouts  
  
“Recursive” means that the holder of a lock can call `mtx_lock()` multiple times on the same lock. (They have to unlock it an equal number of times before anyone else can take the mutex.) This might ease coding from time to time, especially if you call a function that needs to lock the mutex when you already hold the mutex.

And the timeout gives a thread a chance to _try_ to get the lock for a while, but then bail out if it can’t get it in that timeframe.

For a timeout mutex, be sure to create it with `mtx_timed`:
    
    
    [](multithreading.html#cb763-1)mtx_init(&serial_mtx, mtx_timed);

And then when you wait for it, you have to specify a time in UTC when it will unlock[205](function-specifiers-alignment-specifiersoperators.html#fn205).

The function `timespec_get()` from `<time.h>` can be of assistance here. It’ll get you the current time in UTC in a `struct timespec` which is just what we need. In fact, it seems to exist merely for this purpose.

It has two fields: `tv_sec` has the current time in seconds since epoch, and `tv_nsec` has the nanoseconds (billionths of a second) as the “fractional” part.

So you can load that up with the current time, and then add to it to get a specific timeout.

Then call `mtx_timedlock()` instead of `mtx_lock()`. If it returns the value `thrd_timedout`, it timed out.
    
    
    [](multithreading.html#cb764-1)struct timespec timeout;
    [](multithreading.html#cb764-2)
    [](multithreading.html#cb764-3)timespec_get(&timeout, TIME_UTC);  // Get current time
    [](multithreading.html#cb764-4)timeout.tv_sec += 1;               // Timeout 1 second after now
    [](multithreading.html#cb764-5)
    [](multithreading.html#cb764-6)int result = mtx_timedlock(&serial_mtx, &timeout));
    [](multithreading.html#cb764-7)
    [](multithreading.html#cb764-8)if (result == thrd_timedout) {
    [](multithreading.html#cb764-9)    printf("Mutex lock timed out!\n");
    [](multithreading.html#cb764-10)}

Other than that, timed locks are the same as regular locks.

## 39.8 Condition Variables

Condition Variables are the last piece of the puzzle we need to make performant multithreaded applications and to compose more complex multithreaded structures.

A condition variable provides a way for threads to go to sleep until some event on another thread occurs.

In other words, we might have a number of threads that are rearing to go, but they have to wait until some event is true before they continue. Basically they’re being told “wait for it!” until they get notified.

And this works hand-in-hand with mutexes since what we’re going to wait on generally depends on the value of some data, and that data generally needs to be protected by a mutex.

It’s important to note that the condition variable itself isn’t the holder of any particular data from our perspective. It’s merely the variable by which C keeps track of the waiting/not-waiting status of a particular thread or group of threads.

Let’s write a contrived program that reads in groups of 5 numbers from the main thread one at a time. Then, when 5 numbers have been entered, the child thread wakes up, sums up those 5 numbers, and prints the result.

The numbers will be stored in a global, shared array, as will the index into the array of the about-to-be-entered number.

Since these are shared values, we at least have to hide them behind a mutex for both the main and child threads. (The main will be writing data to them and the child will be reading data from them.)

But that’s not enough. The child thread needs to block (“sleep”) until 5 numbers have been read into the array. And then the parent thread needs to wake up the child thread so it can do its work.

And when it wakes up, it needs to be holding that mutex. And it will! When a thread waits on a condition variable, it also acquires a mutex when it wakes up.

All this takes place around an additional variable of type `cnd_t` that is the _condition variable_. We create this variable with the `cnd_init()` function and destroy it when we’re done with it with the `cnd_destroy()` function.

But how’s this all work? Let’s look at the outline of what the child thread will do:

  1. Lock the mutex with `mtx_lock()`
  2. If we haven’t entered all the numbers, wait on the condition variable with `cnd_wait()`
  3. Do the work that needs doing
  4. Unlock the mutex with `mtx_unlock()`



Meanwhile the main thread will be doing this:

  1. Lock the mutex with `mtx_lock()`
  2. Store the recently-read number into the array
  3. If the array is full, signal the child to wake up with `cnd_signal()`
  4. Unlock the mutex with `mtx_unlock()`



If you didn’t skim that too hard (it’s OK—I’m not offended), you might notice something weird: how can the main thread hold the mutex lock and signal the child, if the child has to hold the mutex lock to wait for the signal? They can’t both hold the lock!

And indeed they don’t! There’s some behind-the-scenes magic with condition variables: when you `cnd_wait()`, it releases the mutex that you specify and the thread goes to sleep. And when someone signals that thread to wake up, it reacquires the lock as if nothing had happened.

It’s a little different on the `cnd_signal()` side of things. This doesn’t do anything with the mutex. The signaling thread still must manually release the mutex before the waiting threads can wake up.

One more thing on the `cnd_wait()`. You’ll probably be calling `cnd_wait()` if some condition[206](function-specifiers-alignment-specifiersoperators.html#fn206) is not yet met (e.g. in this case, if not all the numbers have yet been entered). Here’s the deal: this condition should be in a `while` loop, not an `if` statement. Why?

It’s because of a mysterious phenomenon called a _spurious wakeup_. Sometimes, in some implementations, a thread can be woken up out of a `cnd_wait()` sleep for seemingly _no reason_. _[X-Files music]_[ 207](function-specifiers-alignment-specifiersoperators.html#fn207). And so we have to check to see that the condition we need is still actually met when we wake up. And if it’s not, back to sleep with us!

So let’s do this thing! Starting with the main thread:

  * The main thread will set up the mutex and condition variable, and will launch the child thread.

  * Then it will, in an infinite loop, get numbers as input from the console.

  * It will also acquire the mutex to store the inputted number into a global array.

  * When the array has 5 numbers in it, the main thread will signal the child thread that it’s time to wake up and do its work.

  * Then the main thread will unlock the mutex and go back to reading the next number from the console.




Meanwhile, the child thread has been up to its own shenanigans:

  * The child thread grabs the mutex

  * While the condition is not met (i.e. while the shared array doesn’t yet have 5 numbers in it), the child thread sleeps by waiting on the condition variable. When it waits, it implicitly unlocks the mutex.

  * Once the main thread signals the child thread to wake up, it wakes up to do the work and gets the mutex lock back.

  * The child thread sums the numbers and resets the variable that is the index into the array.

  * It then releases the mutex and runs again in an infinite loop.




And here’s the code! Give it some study so you can see where all the above pieces are being handled:
    
    
    [](multithreading.html#cb765-1)#include <stdio.h>
    [](multithreading.html#cb765-2)#include <threads.h>
    [](multithreading.html#cb765-3)
    [](multithreading.html#cb765-4)#define VALUE_COUNT_MAX 5
    [](multithreading.html#cb765-5)
    [](multithreading.html#cb765-6)int value[VALUE_COUNT_MAX];  // Shared global
    [](multithreading.html#cb765-7)int value_count = 0;   // Shared global, too
    [](multithreading.html#cb765-8)
    [](multithreading.html#cb765-9)mtx_t value_mtx;   // Mutex around value
    [](multithreading.html#cb765-10)cnd_t value_cnd;   // Condition variable on value
    [](multithreading.html#cb765-11)
    [](multithreading.html#cb765-12)int run(void *arg)
    [](multithreading.html#cb765-13){
    [](multithreading.html#cb765-14)    (void)arg;
    [](multithreading.html#cb765-15)
    [](multithreading.html#cb765-16)    for (;;) {
    [](multithreading.html#cb765-17)        mtx_lock(&value_mtx);      // <-- GRAB THE MUTEX
    [](multithreading.html#cb765-18)
    [](multithreading.html#cb765-19)        while (value_count < VALUE_COUNT_MAX) {
    [](multithreading.html#cb765-20)            printf("Thread: is waiting\n");
    [](multithreading.html#cb765-21)            cnd_wait(&value_cnd, &value_mtx);  // <-- CONDITION WAIT
    [](multithreading.html#cb765-22)        }
    [](multithreading.html#cb765-23)
    [](multithreading.html#cb765-24)        printf("Thread: is awake!\n");
    [](multithreading.html#cb765-25)
    [](multithreading.html#cb765-26)        int t = 0;
    [](multithreading.html#cb765-27)
    [](multithreading.html#cb765-28)        // Add everything up
    [](multithreading.html#cb765-29)        for (int i = 0; i < VALUE_COUNT_MAX; i++)
    [](multithreading.html#cb765-30)            t += value[i];
    [](multithreading.html#cb765-31)
    [](multithreading.html#cb765-32)        printf("Thread: total is %d\n", t);
    [](multithreading.html#cb765-33)
    [](multithreading.html#cb765-34)        // Reset input index for main thread
    [](multithreading.html#cb765-35)        value_count = 0;
    [](multithreading.html#cb765-36)
    [](multithreading.html#cb765-37)        mtx_unlock(&value_mtx);   // <-- MUTEX UNLOCK
    [](multithreading.html#cb765-38)    }
    [](multithreading.html#cb765-39)
    [](multithreading.html#cb765-40)    return 0;
    [](multithreading.html#cb765-41)}
    [](multithreading.html#cb765-42)
    [](multithreading.html#cb765-43)int main(void)
    [](multithreading.html#cb765-44){
    [](multithreading.html#cb765-45)    thrd_t t;
    [](multithreading.html#cb765-46)
    [](multithreading.html#cb765-47)    // Spawn a new thread
    [](multithreading.html#cb765-48)
    [](multithreading.html#cb765-49)    thrd_create(&t, run, NULL);
    [](multithreading.html#cb765-50)    thrd_detach(t);
    [](multithreading.html#cb765-51)
    [](multithreading.html#cb765-52)    // Set up the mutex and condition variable
    [](multithreading.html#cb765-53)
    [](multithreading.html#cb765-54)    mtx_init(&value_mtx, mtx_plain);
    [](multithreading.html#cb765-55)    cnd_init(&value_cnd);
    [](multithreading.html#cb765-56)
    [](multithreading.html#cb765-57)    for (;;) {
    [](multithreading.html#cb765-58)        int n;
    [](multithreading.html#cb765-59)
    [](multithreading.html#cb765-60)        scanf("%d", &n);
    [](multithreading.html#cb765-61)
    [](multithreading.html#cb765-62)        mtx_lock(&value_mtx);    // <-- LOCK MUTEX
    [](multithreading.html#cb765-63)
    [](multithreading.html#cb765-64)        value[value_count++] = n;
    [](multithreading.html#cb765-65)
    [](multithreading.html#cb765-66)        if (value_count == VALUE_COUNT_MAX) {
    [](multithreading.html#cb765-67)            printf("Main: signaling thread\n");
    [](multithreading.html#cb765-68)            cnd_signal(&value_cnd);  // <-- SIGNAL CONDITION
    [](multithreading.html#cb765-69)        }
    [](multithreading.html#cb765-70)
    [](multithreading.html#cb765-71)        mtx_unlock(&value_mtx);  // <-- UNLOCK MUTEX
    [](multithreading.html#cb765-72)    }
    [](multithreading.html#cb765-73)
    [](multithreading.html#cb765-74)    // Clean up (I know that's an infinite loop above here, but I
    [](multithreading.html#cb765-75)    // want to at least pretend to be proper):
    [](multithreading.html#cb765-76)
    [](multithreading.html#cb765-77)    mtx_destroy(&value_mtx);
    [](multithreading.html#cb765-78)    cnd_destroy(&value_cnd);
    [](multithreading.html#cb765-79)}

And here’s some sample output (individual numbers on lines are my input):
    
    
    [](multithreading.html#cb766-1)Thread: is waiting
    [](multithreading.html#cb766-2)1
    [](multithreading.html#cb766-3)1
    [](multithreading.html#cb766-4)1
    [](multithreading.html#cb766-5)1
    [](multithreading.html#cb766-6)1
    [](multithreading.html#cb766-7)Main: signaling thread
    [](multithreading.html#cb766-8)Thread: is awake!
    [](multithreading.html#cb766-9)Thread: total is 5
    [](multithreading.html#cb766-10)Thread: is waiting
    [](multithreading.html#cb766-11)2
    [](multithreading.html#cb766-12)8
    [](multithreading.html#cb766-13)5
    [](multithreading.html#cb766-14)9
    [](multithreading.html#cb766-15)0
    [](multithreading.html#cb766-16)Main: signaling thread
    [](multithreading.html#cb766-17)Thread: is awake!
    [](multithreading.html#cb766-18)Thread: total is 24
    [](multithreading.html#cb766-19)Thread: is waiting

It’s a common use of condition variables in producer-consumer situations like this. If we didn’t have a way to put the child thread to sleep while it waited for some condition to be met, it would be force to poll which is a big waste of CPU.

### 39.8.1 Timed Condition Wait

There’s a variant of `cnd_wait()` that allows you to specify a timeout so you can stop waiting.

Since the child thread must relock the mutex, this doesn’t necessarily mean that you’ll be popping back to life the instant the timeout occurs; you still must wait for any other threads to release the mutex.

But it does mean that you won’t be waiting until the `cnd_signal()` happens.

To make this work, call `cnd_timedwait()` instead of `cnd_wait()`. If it returns the value `thrd_timedout`, it timed out.

The timestamp is an absolute time in UTC, not a time-from-now. Thankfully the `timespec_get()` function in `<time.h>` seems custom-made for exactly this case.
    
    
    [](multithreading.html#cb767-1)struct timespec timeout;
    [](multithreading.html#cb767-2)
    [](multithreading.html#cb767-3)timespec_get(&timeout, TIME_UTC);  // Get current time
    [](multithreading.html#cb767-4)timeout.tv_sec += 1;               // Timeout 1 second after now
    [](multithreading.html#cb767-5)
    [](multithreading.html#cb767-6)int result = cnd_timedwait(&condition, &mutex, &timeout));
    [](multithreading.html#cb767-7)
    [](multithreading.html#cb767-8)if (result == thrd_timedout) {
    [](multithreading.html#cb767-9)    printf("Condition variable timed out!\n");
    [](multithreading.html#cb767-10)}

### 39.8.2 Broadcast: Wake Up All Waiting Threads

`cnd_signal()` only wakes up one thread to continue working. Depending on how you have your logic done, it might make sense to wake up more than one thread to continue once the condition is met.

Of course only one of them can grab the mutex, but if you have a situation where:

  * The newly-awoken thread is responsible for waking up the next one, and—

  * There’s a chance the spurious-wakeup loop condition will prevent it from doing so, then—




you’ll want to broadcast the wake up so that you’re sure to get at least one of the threads out of that loop to launch the next one.

How, you ask?

Simply use `cnd_broadcast()` instead of `cnd_signal()`. Exact same usage, except `cnd_broadcast()` wakes up **all** the sleeping threads that were waiting on that condition variable.

## 39.9 Running a Function One Time

Let’s say you have a function that _could_ be run by many threads, but you don’t know when, and it’s not work trying to write all that logic.

There’s a way around it: use `call_once()`. Tons of threads could try to run the function, but only the first one counts[208](function-specifiers-alignment-specifiersoperators.html#fn208)

To work with this, you need a special flag variable you declare to keep track of whether or not the thing’s been run. And you need a function to run, which takes no parameters and returns no value.
    
    
    [](multithreading.html#cb768-1)once_flag of = ONCE_FLAG_INIT;  // Initialize it like this
    [](multithreading.html#cb768-2)
    [](multithreading.html#cb768-3)void run_once_function(void)
    [](multithreading.html#cb768-4){
    [](multithreading.html#cb768-5)    printf("I'll only run once!\n");
    [](multithreading.html#cb768-6)}
    [](multithreading.html#cb768-7)
    [](multithreading.html#cb768-8)int run(void *arg)
    [](multithreading.html#cb768-9){
    [](multithreading.html#cb768-10)    (void)arg;
    [](multithreading.html#cb768-11)
    [](multithreading.html#cb768-12)    call_once(&of, run_once_function);
    [](multithreading.html#cb768-13)
    [](multithreading.html#cb768-14)    // ...

In this example, no matter how many threads get to the `run()` function, the `run_once_function()` will only be called a single time.

* * *

[Prev](date-and-time-functionality.html) | [Contents](index.html) | [Next](chapter-atomics.html)

---

[Prev](multithreading.html) | [Contents](index.html) | [Next](function-specifiers-alignment-specifiersoperators.html)

* * *

# 40 Atomics

> _“They tried and failed, all of them?”_  
>  _“Oh, no.” She shook her head. “They tried and died.”_
> 
> —Paul Atreides and The Reverend Mother Gaius Helen Mohiam, _Dune_

This is one of the more challenging aspects of multithreading with C. But we’ll try to take it easy.

Basically, I’ll talk about the more straightforward uses of atomic variables, what they are, and how they work, etc. And I’ll mention some of the more insanely-complex paths that are available to you.

But I won’t go down those paths. Not only am I barely qualified to even write about them, but I figure if you know you need them, you already know more than I do.

But there are some weird things out here even in the basics. So buckle your seatbelts, everyone, ‘cause Kansas is goin’ bye-bye.

## 40.1 Testing for Atomic Support

Atomics are an optional feature. There’s a macro `__STDC_NO_ATOMICS__` that’s `1` if you _don’t_ have atomics.

That macro might not exist pre-C11, so we should test the language version with `__STDC_VERSION__`[209](function-specifiers-alignment-specifiersoperators.html#fn209).
    
    
    [](chapter-atomics.html#cb769-1)#if __STDC_VERSION__ < 201112L || __STDC_NO_ATOMICS__ == 1
    [](chapter-atomics.html#cb769-2)#define HAS_ATOMICS 0
    [](chapter-atomics.html#cb769-3)#else
    [](chapter-atomics.html#cb769-4)#define HAS_ATOMICS 1
    [](chapter-atomics.html#cb769-5)#endif

If those tests pass, then you can safely include `<stdatomic.h>`, the header on which the rest of this chapter is based. But if there is no atomic support, that header might not even exist.

On some systems, you might need to add `-latomic` to the end of your compilation command line to use any functions in the header file.

## 40.2 Atomic Variables

Here’s _part_ of how atomic variables work:

If you have a shared atomic variable and you write to it from one thread, that write will be _all-or-nothing_ in a different thread.

That is, the other thread will see the entire write of, say, a 32-bit value. Not half of it. There’s no way for one thread to interrupt another that is in the _middle_ of an atomic multi-byte write.

It’s almost like there’s a little lock around the getting and setting of that one variable. (And there _might_ be! See [Lock-Free Atomic Variables](chapter-atomics.html#lock-free-atomic), below.)

And on that note, you can get away with never using atomics if you use mutexes to lock your critical sections. It’s just that there are a class of _lock-free data structures_ that always allow other threads to make progress instead of being blocked by a mutex… but these are tough to create correctly from scratch, and are one of the things that are beyond the scope of the guide, sadly.

That’s only part of the story. But it’s the part we’ll start with.

Before we go further, how do you declare a variable to be atomic?

First, include `<stdatomic.h>`.

This gives us types such as `atomic_int`.

And then we can simply declare variables to be of that type.

But let’s do a demo where we have two threads. The first runs for a while and then sets a variable to a specific value, then exits. The other runs until it sees that value get set, and then it exits.
    
    
    [](chapter-atomics.html#cb770-1)#include <stdio.h>
    [](chapter-atomics.html#cb770-2)#include <threads.h>
    [](chapter-atomics.html#cb770-3)#include <stdatomic.h>
    [](chapter-atomics.html#cb770-4)
    [](chapter-atomics.html#cb770-5)atomic_int x;   // THE POWER OF ATOMICS! BWHAHAHA!
    [](chapter-atomics.html#cb770-6)
    [](chapter-atomics.html#cb770-7)int thread1(void *arg)
    [](chapter-atomics.html#cb770-8){
    [](chapter-atomics.html#cb770-9)    (void)arg;
    [](chapter-atomics.html#cb770-10)
    [](chapter-atomics.html#cb770-11)    printf("Thread 1: Sleeping for 1.5 seconds\n");
    [](chapter-atomics.html#cb770-12)    thrd_sleep(&(struct timespec){.tv_sec=1, .tv_nsec=500000000}, NULL);
    [](chapter-atomics.html#cb770-13)
    [](chapter-atomics.html#cb770-14)    printf("Thread 1: Setting x to 3490\n");
    [](chapter-atomics.html#cb770-15)    x = 3490;
    [](chapter-atomics.html#cb770-16)
    [](chapter-atomics.html#cb770-17)    printf("Thread 1: Exiting\n");
    [](chapter-atomics.html#cb770-18)    return 0;
    [](chapter-atomics.html#cb770-19)}
    [](chapter-atomics.html#cb770-20)
    [](chapter-atomics.html#cb770-21)int thread2(void *arg)
    [](chapter-atomics.html#cb770-22){
    [](chapter-atomics.html#cb770-23)    (void)arg;
    [](chapter-atomics.html#cb770-24)
    [](chapter-atomics.html#cb770-25)    printf("Thread 2: Waiting for 3490\n");
    [](chapter-atomics.html#cb770-26)    while (x != 3490) {}  // spin here
    [](chapter-atomics.html#cb770-27)
    [](chapter-atomics.html#cb770-28)    printf("Thread 2: Got 3490--exiting!\n");
    [](chapter-atomics.html#cb770-29)    return 0;
    [](chapter-atomics.html#cb770-30)}
    [](chapter-atomics.html#cb770-31)
    [](chapter-atomics.html#cb770-32)int main(void)
    [](chapter-atomics.html#cb770-33){
    [](chapter-atomics.html#cb770-34)    x = 0;
    [](chapter-atomics.html#cb770-35)
    [](chapter-atomics.html#cb770-36)    thrd_t t1, t2;
    [](chapter-atomics.html#cb770-37)
    [](chapter-atomics.html#cb770-38)    thrd_create(&t1, thread1, NULL);
    [](chapter-atomics.html#cb770-39)    thrd_create(&t2, thread2, NULL);
    [](chapter-atomics.html#cb770-40)
    [](chapter-atomics.html#cb770-41)    thrd_join(t1, NULL);
    [](chapter-atomics.html#cb770-42)    thrd_join(t2, NULL);
    [](chapter-atomics.html#cb770-43)
    [](chapter-atomics.html#cb770-44)    printf("Main    : Threads are done, so x better be 3490\n");
    [](chapter-atomics.html#cb770-45)    printf("Main    : And indeed, x == %d\n", x);
    [](chapter-atomics.html#cb770-46)}

The second thread spins in place, looking at the flag and waiting for it to get set to the value `3490`. And the first one does that.

And I get this output:
    
    
    [](chapter-atomics.html#cb771-1)Thread 1: Sleeping for 1.5 seconds
    [](chapter-atomics.html#cb771-2)Thread 2: Waiting for 3490
    [](chapter-atomics.html#cb771-3)Thread 1: Setting x to 3490
    [](chapter-atomics.html#cb771-4)Thread 1: Exiting
    [](chapter-atomics.html#cb771-5)Thread 2: Got 3490--exiting!
    [](chapter-atomics.html#cb771-6)Main    : Threads are done, so x better be 3490
    [](chapter-atomics.html#cb771-7)Main    : And indeed, x == 3490

Look, ma! We’re accessing a variable from different threads and not using a mutex! And that’ll work every time thanks to the atomic nature of atomic variables.

You might be wondering what happens if that’s a regular non-atomic `int`, instead. Well, on my system it still works… unless I do an optimized build in which case it hangs on thread 2 waiting to see the 3490 to get set[210](function-specifiers-alignment-specifiersoperators.html#fn210).

But that’s just the beginning of the story. The next part is going to require more brain power and has to do with something called _synchronization_.

## 40.3 Synchronization

The next part of our story is all about when certain memory writes in one thread become visible to those in another thread.

You might think, it’s right away, right? But it’s not. A number of things can go wrong. Weirdly wrong.

The compiler might have rearranged memory accesses so that when you think you set a value relative to another might not be true. And even if the compiler didn’t, your CPU might have done it on the fly. Or maybe there’s something else about this architecture that causes writes on one CPU to be delayed before they’re visible on another.

The good news is that we can condense all these potential troubles into one: unsynchronized memory accesses can appear out of order depending on which thread is doing the observing, as if the lines of code themselves had been rearranged.

By way of example, which happens first in the following code, the write to `x` or the write to `y`?
    
    
    [](chapter-atomics.html#cb772-1)int x, y;  // global
    [](chapter-atomics.html#cb772-2)
    [](chapter-atomics.html#cb772-3)// ...
    [](chapter-atomics.html#cb772-4)
    [](chapter-atomics.html#cb772-5)x = 2;
    [](chapter-atomics.html#cb772-6)y = 3;
    [](chapter-atomics.html#cb772-7)
    [](chapter-atomics.html#cb772-8)printf("%d %d\n", x, y);

Answer: we don’t know. The compiler or CPU could silently reverse lines 5 and 6 and we’d be none-the-wiser. The code would run single-threaded _as-if_ it were executed in code order.

In a multithreaded scenario, we might have something like this pseudocode:
    
    
    [](chapter-atomics.html#cb773-1)int x = 0, y = 0;
    [](chapter-atomics.html#cb773-2)
    [](chapter-atomics.html#cb773-3)thread1() {
    [](chapter-atomics.html#cb773-4)    x = 2;
    [](chapter-atomics.html#cb773-5)    y = 3;
    [](chapter-atomics.html#cb773-6)}
    [](chapter-atomics.html#cb773-7)
    [](chapter-atomics.html#cb773-8)thread2() {
    [](chapter-atomics.html#cb773-9)    while (y != 3) {}  // spin
    [](chapter-atomics.html#cb773-10)    printf("x is now %d\n", x);  // 2? ...or 0?
    [](chapter-atomics.html#cb773-11)}

What is the output from thread 2?

Well, if `x` gets assigned `2` _before_ `y` is assigned `3`, then I’d expect the output to be the very sensible:
    
    
    [](chapter-atomics.html#cb774-1)x is now 2 

But something sneaky could rearrange lines 4 and 5 causing us to see the value of `0` for `x` when we print it.

In other words, all bets are off unless we can somehow say, “As of this point, I expect all previous writes in another thread to be visible in this thread.”

Two threads _synchronize_ when they agree on the state of shared memory. As we’ve seen, they’re not always in agreement with the code. So how do they agree?

Using atomic variables can force the agreement[211](function-specifiers-alignment-specifiersoperators.html#fn211). If a thread writes to an atomic variable, it’s saying “anyone who reads this atomic variable in the future will also see all the changes I made to memory (atomic or not) up to and including the atomic variable”.

Or, in more human terms, let’s sit around the conference table and make sure we’re on the same page as to which pieces of shared memory hold what values. You agree that the memory changes that you’d made up-to-and-including the atomic store will be visible to me after I do a load of the same atomic variable.

So we can easily fix our example:
    
    
    [](chapter-atomics.html#cb775-1)int x = 0;
    [](chapter-atomics.html#cb775-2)atomic int y = 0;  // Make y atomic
    [](chapter-atomics.html#cb775-3)
    [](chapter-atomics.html#cb775-4)thread1() {
    [](chapter-atomics.html#cb775-5)    x = 2;
    [](chapter-atomics.html#cb775-6)    y = 3;             // Synchronize on write
    [](chapter-atomics.html#cb775-7)}
    [](chapter-atomics.html#cb775-8)
    [](chapter-atomics.html#cb775-9)thread2() {
    [](chapter-atomics.html#cb775-10)    while (y != 3) {}  // Synchronize on read
    [](chapter-atomics.html#cb775-11)    printf("x is now %d\n", x);  // 2, period.
    [](chapter-atomics.html#cb775-12)}

Because the threads synchronize across `y`, all writes in thread 1 that happened _before_ the write to `y` are visible in thread 2 _after_ the read from `y` (in the `while` loop).

It’s important to note a couple things here:

  1. Nothing sleeps. The synchronization is not a blocking operation. Both threads are running full bore until they exit. Even the one stuck in the spin loop isn’t blocking anyone else from running.

  2. The synchronization happens when one thread reads an atomic variable another thread wrote. So when thread 2 reads `y`, all previous memory writes in thread 1 (namely setting `x`) will be visible in thread 2.

  3. Notice that `x` isn’t atomic. That’s OK because we’re not synchronizing over `x`, and the synchronization over `y` when we write it in thread 1 means that all previous writes—including `x`—in thread 1 will become visible to other threads… if those other threads read `y` to synchronize.




Forcing this synchronization is inefficient and can be a lot slower than just using a regular variable. This is why we don’t use atomics unless we have to for a particular application.

So that’s the basics. Let’s look deeper.

## 40.4 Acquire and Release

More terminology! It’ll pay off to learn this now.

When a thread reads an atomic variable, it is said to be an _acquire_ operation.

When a thread writes an atomic variable, it is said to be a _release_ operation.

What are these? Let’s line them up with terms you already know when it comes to atomic variables:

**Read = Load = Acquire**. Like when you compare an atomic variable or read it to copy it to another value.

**Write = Store = Release**. Like when you assign a value into an atomic variable.

When using atomic variables with these acquire/release semantics, C spells out what can happen when.

Acquire/release form the basis for the synchronization we just talked about.

When a thread acquires an atomic variable, it can see values set in another thread that released that same variable.

In other words:

When a thread reads an atomic variable, it can see values set in another thread that wrote to that same variable.

The synchronization happens across the acquire/release pair.

More details:

With read/load/acquire of a particular atomic variable:

  * All writes (atomic or non-atomic) in another thread that happened before that other thread wrote/stored/released this atomic variable are now visible in this thread.

  * The new value of the atomic variable set by the other thread is also visible in this thread.

  * No reads or writes of any variables/memory in the current thread can be reordered to happen before this acquire.

  * The acquire acts as a one-way barrier when it comes to code reordering; reads and writes in the current thread can be moved down from _before_ the acquire to _after_ it. But, more importantly for synchronization, nothing can move up from _after_ the acquire to _before_ it.




With write/store/release of a particular atomic variable:

  * All writes (atomic or non-atomic) in the current thread that happened before this release become visible to other threads that have read/loaded/acquired the same atomic variable.

  * The value written to this atomic variable by this thread is also visible to other threads.

  * No reads or writes of any variables/memory in the current thread can be reordered to happen after this release.

  * The release acts as a one-way barrier when it comes to code reordering: reads and writes in the current thread can be moved up from _after_ the release to _before_ it. But, more importantly for synchronization, nothing can move down from _before_ the release to _after_ it.




Again, the upshot is synchronization of memory from one thread to another. The second thread can be sure that variables and memory are written in the order the programmer intended.
    
    
    int x, y, z = 0;
    atomic_int a = 0;
    
    thread1() {
        x = 10;
        y = 20;
        a = 999;  // Release
        z = 30;
    }
    
    thread2()
    {
        while (a != 999) { } // Acquire
    
        assert(x == 10);  // never asserts, x is always 10
        assert(y == 20);  // never asserts, y is always 20
    
        assert(z == 0);  // might assert!!
    }

In the above example, `thread2` can be sure of the values in `x` and `y` after it acquires `a` because they were set before `thread1` released the atomic `a`.

But `thread2` can’t be sure of `z`’s value because it happened after the release. Maybe the assignment to `z` got moved before the assignment to `a`.

An important note: releasing one atomic variable has no effect on acquires of different atomic variables. Each variable is isolated from the others.

## 40.5 Sequential Consistency

You hanging in there? We’re through the meat of the simpler usage of atomics. And since we’re not even going to talk about the more complex uses here, you can relax a bit.

_Sequential consistency_ is what’s called a _memory ordering_. There are many memory orderings, but sequential consistency is the sanest[212](function-specifiers-alignment-specifiersoperators.html#fn212) C has to offer. It is also the default. You have to go out of your way to use other memory orderings.

All the stuff we’ve been talking about so far has happened within the realm of sequential consistency.

We’ve talked about how the compiler or CPU can rearrange memory reads and writes in a single thread as long as it follows the _as-if_ rule.

And we’ve seen how we can put the brakes on this behavior by synchronizing over atomic variables.

Let’s formalize just a little more.

If operations are _sequentially consistent_ , it means at the end of the day, when all is said and done, all the threads can kick up their feet, open their beverage of choice, and all agree on the order in which memory changes occurred during the run. And that order is the one specified by the code.

One won’t say, “But didn’t _B_ happen before _A_?” if the rest of them say, “ _A_ definitely happened before _B_ ”. They’re all friends, here.

In particular, within a thread, none of the acquires and releases can be reordered with respect to one another. This is in addition to the rules about what other memory accesses can be reordered around them.

This rule gives an additional level of sanity to the progression of atomic loads/acquires and stores/releases.

Every other memory order in C involves a relaxation of the reordering rules, either for acquires/releases or other memory accesses, atomic or otherwise. You’d do that if you _really_ knew what you were doing and needed the speed boost. _Here be armies of dragons…_

More on that later, but for now, let’s stick to the safe and practical.

## 40.6 Atomic Assignments and Operators

Certain operators on atomic variables are atomic. And others aren’t.

Let’s start with a counter-example:
    
    
    [](chapter-atomics.html#cb777-1)atomic_int x = 0;
    [](chapter-atomics.html#cb777-2)
    [](chapter-atomics.html#cb777-3)thread1() {
    [](chapter-atomics.html#cb777-4)    x = x + 3;  // NOT atomic!
    [](chapter-atomics.html#cb777-5)}

Since there’s a read of `x` on the right hand side of the assignment and a write effectively on the left, these are two operations. Another thread could sneak in the middle and make you unhappy.

But you _can_ use the shorthand `+=` to get an atomic operation:
    
    
    [](chapter-atomics.html#cb778-1)atomic_int x = 0;
    [](chapter-atomics.html#cb778-2)
    [](chapter-atomics.html#cb778-3)thread1() {
    [](chapter-atomics.html#cb778-4)    x += 3;   // ATOMIC!
    [](chapter-atomics.html#cb778-5)}

In that case, `x` will be atomically incremented by `3`—no other thread can jump in the middle.

In particular, the following operators are atomic read-modify-write operations with sequential consistency, so use them with gleeful abandon. (In the example, `a` is atomic.)
    
    
    [](chapter-atomics.html#cb779-1)a++       a--       --a       ++a
    [](chapter-atomics.html#cb779-2)a += b    a -= b    a *= b    a /= b    a %= b
    [](chapter-atomics.html#cb779-3)a &= b    a |= b    a ^= b    a >>= b   a <<= b

## 40.7 Library Functions that Automatically Synchronize

So far we’ve talked about how you can synchronize with atomic variables, but it turns out there are a few library functions that do some limited behind-the-scenes synchronization, themselves.
    
    
    [](chapter-atomics.html#cb780-1)call_once()      thrd_create()       thrd_join()
    [](chapter-atomics.html#cb780-2)mtx_lock()       mtx_timedlock()     mtx_trylock()
    [](chapter-atomics.html#cb780-3)malloc()         calloc()            realloc()
    [](chapter-atomics.html#cb780-4)aligned_alloc()

**`call_once()`** —Synchronizes with all subsequent calls to `call_once()` for a particular flag. This way subsequent calls can rest assured that if another thread sets the flag, they will see it.

**`thrd_create()`** —Synchronizes with the beginning of the new thread. The new thread can be sure it will see all shared memory writes from the parent thread from before the `thrd_create()` call.

**`thrd_join()`** —When a thread dies, it synchronizes with this function. The thread that has called `thrd_join()` can be assured that it can see all the late thread’s shared writes.

**`mtx_lock()`** —Earlier calls to `mtx_unlock()` on the same mutex synchronize on this call. This is the case that most mirrors the acquire/release process we’ve already talked about. `mtx_unlock()` performs a release on the mutex variable, assuring any subsequent thread that makes an acquire with `mtx_lock()` can see all the shared memory changes in the critical section.

**`mtx_timedlock()`** and **`mtx_trylock()`** —Similar to the situation with `mtx_lock()`, if this call succeeds, earlier calls to `mtx_unlock()` synchronize with this one.

**Dynamic Memory Functions** : if you allocate memory, it synchronizes with the previous deallocation of that same memory. And allocations and deallocations of that particular memory region happen in a single total order that all threads can agree upon. I _think_ the idea here is that the deallocation can wipe the region if it chooses, and we want to be sure that a subsequent allocation doesn’t see the non-wiped data. Someone let me know if there’s more to it.

## 40.8 Atomic Type Specifier, Qualifier

Let’s take it down a notch and see what types we have available, and how we can even make new atomic types.

First things first, let’s look at the built-in atomic types and what they are `typedef`’d to. (Spoiler: `_Atomic` is a type qualifier!)

Atomic type | Longhand equivalent  
---|---  
`atomic_bool` | `_Atomic _Bool`  
`atomic_char` | `_Atomic char`  
`atomic_schar` | `_Atomic signed char`  
`atomic_uchar` | `_Atomic unsigned char`  
`atomic_short` | `_Atomic short`  
`atomic_ushort` | `_Atomic unsigned short`  
`atomic_int` | `_Atomic int`  
`atomic_uint` | `_Atomic unsigned int`  
`atomic_long` | `_Atomic long`  
`atomic_ulong` | `_Atomic unsigned long`  
`atomic_llong` | `_Atomic long long`  
`atomic_ullong` | `_Atomic unsigned long long`  
`atomic_char16_t` | `_Atomic char16_t`  
`atomic_char32_t` | `_Atomic char32_t`  
`atomic_wchar_t` | `_Atomic wchar_t`  
`atomic_int_least8_t` | `_Atomic int_least8_t`  
`atomic_uint_least8_t` | `_Atomic uint_least8_t`  
`atomic_int_least16_t` | `_Atomic int_least16_t`  
`atomic_uint_least16_t` | `_Atomic uint_least16_t`  
`atomic_int_least32_t` | `_Atomic int_least32_t`  
`atomic_uint_least32_t` | `_Atomic uint_least32_t`  
`atomic_int_least64_t` | `_Atomic int_least64_t`  
`atomic_uint_least64_t` | `_Atomic uint_least64_t`  
`atomic_int_fast8_t` | `_Atomic int_fast8_t`  
`atomic_uint_fast8_t` | `_Atomic uint_fast8_t`  
`atomic_int_fast16_t` | `_Atomic int_fast16_t`  
`atomic_uint_fast16_t` | `_Atomic uint_fast16_t`  
`atomic_int_fast32_t` | `_Atomic int_fast32_t`  
`atomic_uint_fast32_t` | `_Atomic uint_fast32_t`  
`atomic_int_fast64_t` | `_Atomic int_fast64_t`  
`atomic_uint_fast64_t` | `_Atomic uint_fast64_t`  
`atomic_intptr_t` | `_Atomic intptr_t`  
`atomic_uintptr_t` | `_Atomic uintptr_t`  
`atomic_size_t` | `_Atomic size_t`  
`atomic_ptrdiff_t` | `_Atomic ptrdiff_t`  
`atomic_intmax_t` | `_Atomic intmax_t`  
`atomic_uintmax_t` | `_Atomic uintmax_t`  
  
Use those at will! They’re consistent with the atomic aliases found in C++, if that helps.

But what if you want more?

You can do it either with a type qualifier or type specifier.

First, specifier! It’s the keyword `_Atomic` with a type in parens after[213](function-specifiers-alignment-specifiersoperators.html#fn213)—suitable for use with `typedef`:
    
    
    [](chapter-atomics.html#cb781-1)typedef _Atomic(double) atomic_double;
    [](chapter-atomics.html#cb781-2)
    [](chapter-atomics.html#cb781-3)atomic_double f;

Restrictions on the specifier: the type you’re making atomic can’t be of type array or function, nor can it be atomic or otherwise qualified.

Next, qualifier! It’s the keyword `_Atomic` _without_ a type in parens.

So these do similar things[214](function-specifiers-alignment-specifiersoperators.html#fn214):
    
    
    [](chapter-atomics.html#cb782-1)_Atomic(int) i;   // type specifier
    [](chapter-atomics.html#cb782-2)_Atomic int  j;   // type qualifier

The thing is, you can include other type qualifiers with the latter:
    
    
    [](chapter-atomics.html#cb783-1)_Atomic volatile int k;   // qualified atomic variable

Restrictions on the qualifier: the type you’re making atomic can’t be of type array or function.

## 40.9 Lock-Free Atomic Variables

Hardware architectures are limited in the amount of data they can atomically read and write. It depends on how it’s wired together. And it varies.

If you use an atomic type, you can be assured that accesses to that type will be atomic… but there’s a catch: if the hardware can’t do it, it’s done with a lock, instead.

So the atomic access becomes lock-access-unlock, which is rather slower and has some implications for signal handlers.

[Atomic flags](chapter-atomics.html#atomic-flags), below, is the only atomic type that is guaranteed to be lock-free in all conforming implementations. In typical desktop/laptop computer world, other larger types are likely lock-free.

Luckily, we have a couple ways to determine if a particular type is a lock-free atomic or not.

First of all, some macros—you can use these at compile time with `#if`. They apply to both signed and unsigned types.

Atomic Type | Lock Free Macro  
---|---  
`atomic_bool` | `ATOMIC_BOOL_LOCK_FREE`  
`atomic_char` | `ATOMIC_CHAR_LOCK_FREE`  
`atomic_char16_t` | `ATOMIC_CHAR16_T_LOCK_FREE`  
`atomic_char32_t` | `ATOMIC_CHAR32_T_LOCK_FREE`  
`atomic_wchar_t` | `ATOMIC_WCHAR_T_LOCK_FREE`  
`atomic_short` | `ATOMIC_SHORT_LOCK_FREE`  
`atomic_int` | `ATOMIC_INT_LOCK_FREE`  
`atomic_long` | `ATOMIC_LONG_LOCK_FREE`  
`atomic_llong` | `ATOMIC_LLONG_LOCK_FREE`  
`atomic_intptr_t` | `ATOMIC_POINTER_LOCK_FREE`  
  
These macros can interestingly have _three_ different values:

Value | Meaning  
---|---  
`0` | Never lock-free.  
`1` | _Sometimes_ lock-free.  
`2` | Always lock-free.  
  
Wait—how can something be _sometimes_ lock-free? This just means the answer isn’t known at compile-time, but could later be known at runtime. Maybe the answer varies depending on whether or not you’re running this code on Genuine Intel or AMD, or something like that[215](function-specifiers-alignment-specifiersoperators.html#fn215).

But you can always test at runtime with the `atomic_is_lock_free()` function. This function returns true or false if the particular type is atomic right now.

So why do we care?

Lock-free is faster, so maybe there’s a speed concern that you’d code around another way. Or maybe you need to use an atomic variable in a signal handler.

### 40.9.1 Signal Handlers and Lock-Free Atomics

If you read or write a shared variable (static storage duration or `_Thread_Local`) in a signal handler, it’s undefined behavior [gasp!]… Unless you do one of the following:

  1. Write to a variable of type `volatile sig_atomic_t`.

  2. Read or write a lock-free atomic variable.




As far as I can tell, lock-free atomic variables are one of the few ways you get portably get information out of a signal handler.

The spec is a bit vague, in my read, about the memory order when it comes to acquiring or releasing atomic variables in the signal handler. C++ says, and it makes sense, that such accesses are unsequenced with respect to the rest of the program[216](function-specifiers-alignment-specifiersoperators.html#fn216). The signal can be raised, after all, at any time. So I’m assuming C’s behavior is similar.

## 40.10 Atomic Flags

There’s only one type the standard guarantees will be a lock-free atomic: `atomic_flag`. This is an opaque type for [test-and-set](https://en.wikipedia.org/wiki/Test-and-set)[217](function-specifiers-alignment-specifiersoperators.html#fn217) operations.

It can be either _set_ or _clear_. You can initialize it to clear with:
    
    
    [](chapter-atomics.html#cb784-1)atomic_flag f = ATOMIC_FLAG_INIT;

You can set the flag atomically with `atomic_flag_test_and_set()`, which will set the flag and return its previous status as a `_Bool` (true for set).

You can clear the flag atomically with `atomic_flag_clear()`.

Here’s an example where we init the flag to clear, set it twice, then clear it again.
    
    
    [](chapter-atomics.html#cb785-1)#include <stdio.h>
    [](chapter-atomics.html#cb785-2)#include <stdbool.h>   // Not needed in C23
    [](chapter-atomics.html#cb785-3)#include <stdatomic.h>
    [](chapter-atomics.html#cb785-4)
    [](chapter-atomics.html#cb785-5)atomic_flag f = ATOMIC_FLAG_INIT;
    [](chapter-atomics.html#cb785-6)
    [](chapter-atomics.html#cb785-7)int main(void)
    [](chapter-atomics.html#cb785-8){
    [](chapter-atomics.html#cb785-9)    bool r = atomic_flag_test_and_set(&f);
    [](chapter-atomics.html#cb785-10)    printf("Value was: %d\n", r);           // 0
    [](chapter-atomics.html#cb785-11)
    [](chapter-atomics.html#cb785-12)    r = atomic_flag_test_and_set(&f);
    [](chapter-atomics.html#cb785-13)    printf("Value was: %d\n", r);           // 1
    [](chapter-atomics.html#cb785-14)
    [](chapter-atomics.html#cb785-15)    atomic_flag_clear(&f);
    [](chapter-atomics.html#cb785-16)    r = atomic_flag_test_and_set(&f);
    [](chapter-atomics.html#cb785-17)    printf("Value was: %d\n", r);           // 0
    [](chapter-atomics.html#cb785-18)}

## 40.11 Atomic `struct`s and `union`s

Using the `_Atomic` qualifier or specifier, you can make atomic `struct`s or `union`s! Pretty astounding.

If there’s not a lot of data in there (i.e. a handful of bytes), the resulting atomic type might be lock-free. Test it with `atomic_is_lock_free()`.
    
    
    [](chapter-atomics.html#cb786-1)#include <stdio.h>
    [](chapter-atomics.html#cb786-2)#include <stdatomic.h>
    [](chapter-atomics.html#cb786-3)
    [](chapter-atomics.html#cb786-4)int main(void)
    [](chapter-atomics.html#cb786-5){
    [](chapter-atomics.html#cb786-6)    struct point {
    [](chapter-atomics.html#cb786-7)        float x, y;
    [](chapter-atomics.html#cb786-8)    };
    [](chapter-atomics.html#cb786-9)
    [](chapter-atomics.html#cb786-10)    _Atomic(struct point) p;
    [](chapter-atomics.html#cb786-11)
    [](chapter-atomics.html#cb786-12)    printf("Is lock free: %d\n", atomic_is_lock_free(&p));
    [](chapter-atomics.html#cb786-13)}

Here’s the catch: you can’t access fields of an atomic `struct` or `union`… so what’s the point? Well, you can atomically _copy_ the entire `struct` into a non-atomic variable and then use it. You can atomically copy the other way, too.
    
    
    [](chapter-atomics.html#cb787-1)#include <stdio.h>
    [](chapter-atomics.html#cb787-2)#include <stdatomic.h>
    [](chapter-atomics.html#cb787-3)
    [](chapter-atomics.html#cb787-4)int main(void)
    [](chapter-atomics.html#cb787-5){
    [](chapter-atomics.html#cb787-6)    struct point {
    [](chapter-atomics.html#cb787-7)        float x, y;
    [](chapter-atomics.html#cb787-8)    };
    [](chapter-atomics.html#cb787-9)
    [](chapter-atomics.html#cb787-10)    _Atomic(struct point) p;
    [](chapter-atomics.html#cb787-11)    struct point t;
    [](chapter-atomics.html#cb787-12)
    [](chapter-atomics.html#cb787-13)    p = (struct point){1, 2};  // Atomic copy
    [](chapter-atomics.html#cb787-14)
    [](chapter-atomics.html#cb787-15)    //printf("%f\n", p.x);  // Error
    [](chapter-atomics.html#cb787-16)
    [](chapter-atomics.html#cb787-17)    t = p;   // Atomic copy
    [](chapter-atomics.html#cb787-18)
    [](chapter-atomics.html#cb787-19)    printf("%f\n", t.x);  // OK!
    [](chapter-atomics.html#cb787-20)}

You can also declare a `struct` where individual fields are atomic. It is implementation defined if atomic types are allowed on bitfields.

## 40.12 Atomic Pointers

Just a note here about placement of `_Atomic` when it comes to pointers.

First, pointers to atomics (i.e. the pointer value is not atomic, but the thing it points to is):
    
    
    [](chapter-atomics.html#cb788-1)_Atomic int x;
    [](chapter-atomics.html#cb788-2)_Atomic int *p;  // p is a pointer to an atomic int
    [](chapter-atomics.html#cb788-3)
    [](chapter-atomics.html#cb788-4)p = &x;  // OK!

Second, atomic pointers to non-atomic values (i.e. the pointer value itself is atomic, but the thing it points to is not):
    
    
    [](chapter-atomics.html#cb789-1)int x;
    [](chapter-atomics.html#cb789-2)int * _Atomic p;  // p is an atomic pointer to an int
    [](chapter-atomics.html#cb789-3)
    [](chapter-atomics.html#cb789-4)p = &x;  // OK!

Lastly, atomic pointers to atomic values (i.e. the pointer and the thing it points to are both atomic):
    
    
    [](chapter-atomics.html#cb790-1)_Atomic int x;
    [](chapter-atomics.html#cb790-2)_Atomic int * _Atomic p;  // p is an atomic pointer to an atomic int
    [](chapter-atomics.html#cb790-3)
    [](chapter-atomics.html#cb790-4)p = &x;  // OK!

## 40.13 Memory Order

We’ve already talked about sequential consistency, which is the sensible one of the bunch. But there are a number of other ones:

`memory_order` | Description  
---|---  
`memory_order_seq_cst` | Sequential Consistency  
`memory_order_acq_rel` | Acquire/Release  
`memory_order_release` | Release  
`memory_order_acquire` | Acquire  
`memory_order_consume` | Consume  
`memory_order_relaxed` | Relaxed  
  
You can specify other ones with certain library functions. For example, you can add a value to an atomic variable like this:
    
    
    [](chapter-atomics.html#cb791-1)atomic_int x = 0;
    [](chapter-atomics.html#cb791-2)
    [](chapter-atomics.html#cb791-3)x += 5;  // Sequential consistency, the default

Or you can do the same with this library function:
    
    
    [](chapter-atomics.html#cb792-1)atomic_int x = 0;
    [](chapter-atomics.html#cb792-2)
    [](chapter-atomics.html#cb792-3)atomic_fetch_add(&x, 5);  // Sequential consistency, the default

Or you can do the same thing with an explicit memory ordering:
    
    
    [](chapter-atomics.html#cb793-1)atomic_int x = 0;
    [](chapter-atomics.html#cb793-2)
    [](chapter-atomics.html#cb793-3)atomic_fetch_add_explicit(&x, 5, memory_order_seq_cst);

But what if we didn’t want sequential consistency? And you wanted acquire/release instead for whatever reason? Just name it:
    
    
    [](chapter-atomics.html#cb794-1)atomic_int x = 0;
    [](chapter-atomics.html#cb794-2)
    [](chapter-atomics.html#cb794-3)atomic_fetch_add_explicit(&x, 5, memory_order_acq_rel);

We’ll do a breakdown of the different memory orders, below. Don’t mess with anything other than sequential consistency unless you know what you’re doing. It’s really easy to make mistakes that will cause rare, hard-to-repro failures.

### 40.13.1 Sequential Consistency

  * Load operations acquire (see below).
  * Store operations release (see below).
  * Read-modify-write operations acquire then release.



Also, in order to maintain the total order of acquires and releases, no acquires or releases will be reordered with respect to each other. (The acquire/release rules do not forbid reordering a release followed by an acquire. But the sequentially consistent rules do.)

### 40.13.2 Acquire

This is what happens on a load/read operation on an atomic variable.

  * If another thread released this atomic variable, all the writes that thread did are now visible in this thread.

  * Memory accesses in this thread that happen after this load can’t be reordered before it.




### 40.13.3 Release

This is what happens on a store/write of an atomic variable.

  * If another thread later acquires this atomic variable, all memory writes in this thread before its atomic write become visible to that other thread.

  * Memory accesses in this thread that happen before the release can’t be reordered after it.




### 40.13.4 Consume

This is an odd one, similar to a less-strict version of acquire. It affects memory accesses that are _data dependent_ on the atomic variable.

Being “data dependent” vaguely means that the atomic variable is used in a calculation.

That is, if a thread consumes an atomic variable then all the operations in that thread that go on to use that atomic variable will be able to see the memory writes in the releasing thread.

Compare to acquire where memory writes in the releasing thread will be visible to _all_ operations in the current thread, not just the data-dependent ones.

Also like acquire, there is a restriction on which operations can be reordered _before_ the consume. With acquire, you couldn’t reorder anything before it. With consume, you can’t reorder anything that depends on the loaded atomic value before it.

### 40.13.5 Acquire/Release

This only applies to read-modify-write operations. It’s an acquire and release bundled into one.

  * An acquire happens for the read.
  * A release happens for the write.



### 40.13.6 Relaxed

No rules; it’s anarchy! Everyone can reorder everything everywhere! Dogs and cats living together—mass hysteria!

Actually, there is a rule. Atomic reads and writes are still all-or-nothing. But the operations can be reordered whimsically and there is zero synchronization between threads.

There are a few use cases for this memory order, which you can find with a tiny bit of searching, e.g. simple counters.

And you can use a fence to force synchronization after a bunch of relaxed writes.

## 40.14 Fences

You know how the releases and acquires of atomic variables occur as you read and write them?

Well, it’s possible to do a release or acquire _without_ an atomic variable, as well.

This is called a _fence_. So if you want all the writes in a thread to be visible elsewhere, you can put up a release fence in one thread and an acquire fence in another, just like with how atomic variables work.

Since a consume operation doesn’t really make sense on a fence[218](function-specifiers-alignment-specifiersoperators.html#fn218), `memory_order_consume` is treated as an acquire.

You can put up a fence with any specified order:
    
    
    [](chapter-atomics.html#cb795-1)atomic_thread_fence(memory_order_release);

There’s also a light version of a fence for use with signal handlers, called `atomic_signal_fence()`.

It works just the same way as `atomic_thread_fence()`, except:

  * It only deals with visibility of values within the same thread; there is no synchronization with other threads.

  * No hardware fence instructions are emitted.




If you want to be sure the side effects of non-atomic operations (and relaxed atomic operations) are visible in the signal handler, you can use this fence.

The idea is that the signal handler is executing in _this_ thread, not another, so this is a lighter-weight way of making sure changes outside the signal handler are visible within it (i.e. they haven’t been reordered).

## 40.15 References

If you want to learn more about this stuff, here are some of the things that helped me plow through it:

  * Herb Sutter’s _`atomic<>` Weapons_ talk:

    * [Part 1](https://www.youtube.com/watch?v=A8eCGOqgvH4)[219](function-specifiers-alignment-specifiersoperators.html#fn219)
    * [part 2](https://www.youtube.com/watch?v=KeLBd2EJLOU)[220](function-specifiers-alignment-specifiersoperators.html#fn220)
  * [Jeff Preshing’s materials](https://preshing.com/archives/)[221](function-specifiers-alignment-specifiersoperators.html#fn221), in particular:

    * [An Introduction to Lock-Free Programming](https://preshing.com/20120612/an-introduction-to-lock-free-programming/)[222](function-specifiers-alignment-specifiersoperators.html#fn222)
    * [Acquire and Release Semantics](https://preshing.com/20120913/acquire-and-release-semantics/)[223](function-specifiers-alignment-specifiersoperators.html#fn223)
    * [The _Happens-Before_ Relation](https://preshing.com/20130702/the-happens-before-relation/)[224](function-specifiers-alignment-specifiersoperators.html#fn224)
    * [The _Synchronizes-With_ Relation](https://preshing.com/20130823/the-synchronizes-with-relation/)[225](function-specifiers-alignment-specifiersoperators.html#fn225)
    * [The Purpose of `memory_order_consume` in C++11](https://preshing.com/20140709/the-purpose-of-memory_order_consume-in-cpp11/)[226](function-specifiers-alignment-specifiersoperators.html#fn226)
    * [You Can Do Any Kind of Atomic Read-Modify-Write Operation](https://preshing.com/20150402/you-can-do-any-kind-of-atomic-read-modify-write-operation/)[227](function-specifiers-alignment-specifiersoperators.html#fn227)
  * CPPReference:

    * [Memory Order](https://en.cppreference.com/w/c/atomic/memory_order)[228](function-specifiers-alignment-specifiersoperators.html#fn228)
    * [Atomic Types](https://en.cppreference.com/w/c/language/atomic)[229](function-specifiers-alignment-specifiersoperators.html#fn229)
  * Bruce Dawson’s [Lockless Programming Considerations](https://docs.microsoft.com/en-us/windows/win32/dxtecharts/lockless-programming)[230](function-specifiers-alignment-specifiersoperators.html#fn230)

  * The helpful and knowledgeable folks on [r/C_Programming](https://www.reddit.com/r/C_Programming/)[231](function-specifiers-alignment-specifiersoperators.html#fn231)




* * *

[Prev](multithreading.html) | [Contents](index.html) | [Next](function-specifiers-alignment-specifiersoperators.html)

---

[Prev](chapter-atomics.html) | [Contents](index.html) | [Next](function-specifiers-alignment-specifiersoperators.html)

* * *

# 41 Function Specifiers, Alignment Specifiers/Operators

These don’t see a heck of a lot of use in my experience, but we’ll cover them here for the sake of completeness.

## 41.1 Function Specifiers

When you declare a function, you can give the compiler a couple tips about how the functions could or will be used. This enables or encourages the compiler to make certain optimizations.

### 41.1.1 `inline` for Speed—Maybe

You can declare a function to be inline like this:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb796-1)static inline int add(int x, int y) {
    [](function-specifiers-alignment-specifiersoperators.html#cb796-2)    return x + y;
    [](function-specifiers-alignment-specifiersoperators.html#cb796-3)}

This is meant to encourage the compiler to make this function call as fast as possible. And, historically, one way to do this was _inlining_ , which means that the body of the function would be embedded in its entirety where the call was made. This would avoid all the overhead of setting up the function call and tearing it down at the expense of larger code size as the function was copied all over the place instead of being reused.

The quick-and-dirty things to remember are:

  1. You probably don’t need to use `inline` for speed. Modern compilers know what’s best.

  2. If you do use it for speed, use it with file scope, i.e. `static inline`. This avoids the messy rules of external linkage and inline functions.




Stop reading this section now.

Glutton for punishment, eh?

Let’s try leaving the `static` off.
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb797-1)#include <stdio.h>
    [](function-specifiers-alignment-specifiersoperators.html#cb797-2)
    [](function-specifiers-alignment-specifiersoperators.html#cb797-3)inline int add(int x, int y)
    [](function-specifiers-alignment-specifiersoperators.html#cb797-4){
    [](function-specifiers-alignment-specifiersoperators.html#cb797-5)    return x + y;
    [](function-specifiers-alignment-specifiersoperators.html#cb797-6)}
    [](function-specifiers-alignment-specifiersoperators.html#cb797-7)
    [](function-specifiers-alignment-specifiersoperators.html#cb797-8)int main(void)
    [](function-specifiers-alignment-specifiersoperators.html#cb797-9){
    [](function-specifiers-alignment-specifiersoperators.html#cb797-10)    printf("%d\n", add(1, 2));
    [](function-specifiers-alignment-specifiersoperators.html#cb797-11)}

`gcc` gives a linker error on `add()`[232](function-specifiers-alignment-specifiersoperators.html#fn232). The spec requires that if you have a non-`extern` inline function you must also provide a version with external linkage.

So you’d have to have an `extern` version somewhere else for this to work. If the compiler has both an `inline` function in the current file and an external version of the same function elsewhere, it gets to choose which one to call. So I highly recommend they be the same.

Another thing you can do is to declare the function as `extern inline`. This will attempt to inline in the same file (for speed), but will also create a version with external linkage.

### 41.1.2 `noreturn` and `_Noreturn`

This indicates to the compiler that a particular function will not ever return to its caller, i.e. the program will exit by some mechanism before the function returns.

It allows the compiler to perhaps perform some optimizations around the function call.

It also allows you to indicate to other devs that some program logic depends on a function _not_ returning.

You’ll likely never need to use this, but you’ll see it on some library calls like [`exit()`](https://beej.us/guide/bgclr/html/split/stdlib.html#man-exit)[233](function-specifiers-alignment-specifiersoperators.html#fn233) and [`abort()`](https://beej.us/guide/bgclr/html/split/stdlib.html#man-abort)[234](function-specifiers-alignment-specifiersoperators.html#fn234).

The built-in keyword is `_Noreturn`, but if it doesn’t break your existing code, everyone would recommend including `<stdnoreturn.h>` and using the easier-to-read `noreturn` instead.

It’s undefined behavior if a function specified as `noreturn` actually does return. It’s computationally dishonest, see.

Here’s an example of using `noreturn` correctly:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb798-1)#include <stdio.h>
    [](function-specifiers-alignment-specifiersoperators.html#cb798-2)#include <stdlib.h>
    [](function-specifiers-alignment-specifiersoperators.html#cb798-3)#include <stdnoreturn.h>
    [](function-specifiers-alignment-specifiersoperators.html#cb798-4)
    [](function-specifiers-alignment-specifiersoperators.html#cb798-5)noreturn void foo(void) // This function should never return!
    [](function-specifiers-alignment-specifiersoperators.html#cb798-6){
    [](function-specifiers-alignment-specifiersoperators.html#cb798-7)    printf("Happy days\n");
    [](function-specifiers-alignment-specifiersoperators.html#cb798-8)
    [](function-specifiers-alignment-specifiersoperators.html#cb798-9)    exit(1);            // And it doesn't return--it exits here!
    [](function-specifiers-alignment-specifiersoperators.html#cb798-10)}
    [](function-specifiers-alignment-specifiersoperators.html#cb798-11)
    [](function-specifiers-alignment-specifiersoperators.html#cb798-12)int main(void)
    [](function-specifiers-alignment-specifiersoperators.html#cb798-13){
    [](function-specifiers-alignment-specifiersoperators.html#cb798-14)    foo();
    [](function-specifiers-alignment-specifiersoperators.html#cb798-15)}

If the compiler detects that a `noreturn` function could return, it might warn you, helpfully.

Replacing the `foo()` function with this:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb799-1)noreturn void foo(void)
    [](function-specifiers-alignment-specifiersoperators.html#cb799-2){
    [](function-specifiers-alignment-specifiersoperators.html#cb799-3)    printf("Breakin' the law\n");
    [](function-specifiers-alignment-specifiersoperators.html#cb799-4)}

gets me a warning:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb800-1)foo.c:7:1: warning: function declared 'noreturn' should not return

## 41.2 Alignment Specifiers and Operators

[_Alignment_](https://en.wikipedia.org/wiki/Data_structure_alignment)[ 235](function-specifiers-alignment-specifiersoperators.html#fn235) is all about multiples of addresses on which objects can be stored. Can you store this at any address? Or must it be a starting address that’s divisible by 2? Or 8? Or 16?

If you’re coding up something low-level like a memory allocator that interfaces with your OS, you might need to consider this. Most devs go their careers without using this functionality in C.

### 41.2.1 `alignas` and `_Alignas`

This isn’t a function. Rather, it’s an _alignment specifier_ that you can use with a variable declaration.

The built-in specifier is `_Alignas`, but the header `<stdalign.h>` defines it as `alignas` for something better looking.

If you need your `char` to be aligned like an `int`, you can force it like this when you declare it:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb801-1)char alignas(int) c;

You can also pass a constant value or expression in for the alignment. This has to be something supported by the system, but the spec stops short of dictating what values you can put in there. Small powers of 2 (1, 2, 4, 8, and 16) are generally safe bets.
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb802-1)char alignas(8) c;   // align on 8-byte boundaries

If you want to align at the maximum used alignment by your system, include `<stddef.h>` and use the type `max_align_t`, like so:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb803-1)char alignas(max_align_t) c;

You could potentially _over-align_ by specifying an alignment more than that of `max_align_t`, but whether or not such things are allowed is system dependent.

### 41.2.2 `alignof` and `_Alignof`

This operator will return the address multiple a particular type uses for alignment on this system. For example, maybe `char`s are aligned every 1 address, and `int`s are aligned every 4 addresses.

The built-in operator is `_Alignof`, but the header `<stdalign.h>` defines it as `alignof` if you want to look cooler.

Here’s a program that will print out the alignments of a variety of different types. Again, these will vary from system to system. Note that the type `max_align_t` will give you the maximum alignment used by the system.
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb804-1)#include <stdalign.h>
    [](function-specifiers-alignment-specifiersoperators.html#cb804-2)#include <stdio.h>     // for printf()
    [](function-specifiers-alignment-specifiersoperators.html#cb804-3)#include <stddef.h>    // for max_align_t
    [](function-specifiers-alignment-specifiersoperators.html#cb804-4)
    [](function-specifiers-alignment-specifiersoperators.html#cb804-5)struct t {
    [](function-specifiers-alignment-specifiersoperators.html#cb804-6)    int a;
    [](function-specifiers-alignment-specifiersoperators.html#cb804-7)    char b;
    [](function-specifiers-alignment-specifiersoperators.html#cb804-8)    float c;
    [](function-specifiers-alignment-specifiersoperators.html#cb804-9)};
    [](function-specifiers-alignment-specifiersoperators.html#cb804-10)
    [](function-specifiers-alignment-specifiersoperators.html#cb804-11)int main(void)
    [](function-specifiers-alignment-specifiersoperators.html#cb804-12){
    [](function-specifiers-alignment-specifiersoperators.html#cb804-13)    printf("char       : %zu\n", alignof(char));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-14)    printf("short      : %zu\n", alignof(short));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-15)    printf("int        : %zu\n", alignof(int));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-16)    printf("long       : %zu\n", alignof(long));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-17)    printf("long long  : %zu\n", alignof(long long));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-18)    printf("double     : %zu\n", alignof(double));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-19)    printf("long double: %zu\n", alignof(long double));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-20)    printf("struct t   : %zu\n", alignof(struct t));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-21)    printf("max_align_t: %zu\n", alignof(max_align_t));
    [](function-specifiers-alignment-specifiersoperators.html#cb804-22)}

Output on my system:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb805-1)char       : 1
    [](function-specifiers-alignment-specifiersoperators.html#cb805-2)short      : 2
    [](function-specifiers-alignment-specifiersoperators.html#cb805-3)int        : 4
    [](function-specifiers-alignment-specifiersoperators.html#cb805-4)long       : 8
    [](function-specifiers-alignment-specifiersoperators.html#cb805-5)long long  : 8
    [](function-specifiers-alignment-specifiersoperators.html#cb805-6)double     : 8
    [](function-specifiers-alignment-specifiersoperators.html#cb805-7)long double: 16
    [](function-specifiers-alignment-specifiersoperators.html#cb805-8)struct t   : 16
    [](function-specifiers-alignment-specifiersoperators.html#cb805-9)max_align_t: 16

## 41.3 `memalignment()` Function

New in C23!

(Caveat: none of my compilers support this function yet, so the code is largely untested.)

`alignof` is great if you know the type of your data. But what if you’re _woefully ignorant_ of the type, and only have a pointer to the data?

How could that even happen?

Well, with our good friend the `void*`, of course. We can’t pass that to `alignof`, but what if we need to know the alignment of the thing it points to?

We might want to know this if we’re about to use the memory for something that has significant alignment needs. For example, atomic and floating types often behave badly if misaligned.

So with this function we can check the alignment of some data as long as we have a pointer to that data, even if it’s a `void*`.

Let’s do a quick test to see if a void pointer is well-aligned for use as an atomic type, and, if so, let’s get a variable to use it as that type:
    
    
    [](function-specifiers-alignment-specifiersoperators.html#cb806-1)void foo(void *p)
    [](function-specifiers-alignment-specifiersoperators.html#cb806-2){
    [](function-specifiers-alignment-specifiersoperators.html#cb806-3)    if (memalignment(p) >= alignof(atomic int)) {
    [](function-specifiers-alignment-specifiersoperators.html#cb806-4)        atomic int *i = p;
    [](function-specifiers-alignment-specifiersoperators.html#cb806-5)        do_things(i);
    [](function-specifiers-alignment-specifiersoperators.html#cb806-6)    } else
    [](function-specifiers-alignment-specifiersoperators.html#cb806-7)        puts("This pointer is no good as an atomic int\n");
    [](function-specifiers-alignment-specifiersoperators.html#cb806-8)
    [](function-specifiers-alignment-specifiersoperators.html#cb806-9)...

I suspect you will rarely (to the point of never, likely) need to use this function unless you’re doing some low-level stuff.

And there you have it. Alignment!

* * *

  1. https://www.ioccc.org/[↩︎](foreword.html#fnref1)

  2. https://en.wikipedia.org/wiki/Python_(programming_language)[↩︎](foreword.html#fnref2)

  3. https://en.wikipedia.org/wiki/JavaScript[↩︎](foreword.html#fnref3)

  4. https://en.wikipedia.org/wiki/Java_(programming_language)[↩︎](foreword.html#fnref4)

  5. https://en.wikipedia.org/wiki/Rust_(programming_language)[↩︎](foreword.html#fnref5)

  6. https://en.wikipedia.org/wiki/Go_(programming_language)[↩︎](foreword.html#fnref6)

  7. https://en.wikipedia.org/wiki/Swift_(programming_language)[↩︎](foreword.html#fnref7)

  8. https://en.wikipedia.org/wiki/Objective-C[↩︎](foreword.html#fnref8)

  9. https://beej.us/guide/bgclr/[↩︎](foreword.html#fnref9)

  10. https://en.wikipedia.org/wiki/ANSI_C[↩︎](foreword.html#fnref10)

  11. https://en.wikipedia.org/wiki/POSIX[↩︎](foreword.html#fnref11)

  12. https://visualstudio.microsoft.com/vs/community/[↩︎](foreword.html#fnref12)

  13. https://docs.microsoft.com/en-us/windows/wsl/install-win10[↩︎](foreword.html#fnref13)

  14. https://developer.apple.com/xcode/[↩︎](foreword.html#fnref14)

  15. https://beej.us/guide/bgc/[↩︎](foreword.html#fnref15)

  16. https://en.cppreference.com/[↩︎](foreword.html#fnref16)

  17. https://groups.google.com/g/comp.lang.c[↩︎](foreword.html#fnref17)

  18. https://www.reddit.com/r/C_Programming/[↩︎](foreword.html#fnref18)

  19. https://en.wikipedia.org/wiki/Assembly_language[↩︎](hello-world.html#fnref19)

  20. https://en.wikipedia.org/wiki/Bare_machine[↩︎](hello-world.html#fnref20)

  21. https://en.wikipedia.org/wiki/Operating_system[↩︎](hello-world.html#fnref21)

  22. https://en.wikipedia.org/wiki/Embedded_system[↩︎](hello-world.html#fnref22)

  23. https://en.wikipedia.org/wiki/Rust_(programming_language)[↩︎](hello-world.html#fnref23)

  24. https://en.wikipedia.org/wiki/Grok[↩︎](hello-world.html#fnref24)

  25. I know someone will fight me on that, but it’s gotta be at least in the top three, right?[↩︎](hello-world.html#fnref25)

  26. Well, technically there are more than two, but hey, let’s pretend there are two—ignorance is bliss, right?[↩︎](hello-world.html#fnref26)

  27. https://en.wikipedia.org/wiki/Assembly_language[↩︎](hello-world.html#fnref27)

  28. https://en.wikipedia.org/wiki/Machine_code[↩︎](hello-world.html#fnref28)

  29. Technically, it contains preprocessor directives and function prototypes (more on that later) for common input and output needs.[↩︎](hello-world.html#fnref29)

  30. https://en.wikipedia.org/wiki/Unix[↩︎](hello-world.html#fnref30)

  31. If you don’t give it an output filename, it will export to a file called `a.out` by default—this filename has its roots deep in Unix history.[↩︎](hello-world.html#fnref31)

  32. https://formulae.brew.sh/formula/gcc[↩︎](hello-world.html#fnref32)

  33. A “byte” is typically an 8-bit binary number. Think of it as an integer that can only hold the values from 0 to 255, inclusive. Technically, C allows bytes to be any number of bits and if you want to unambiguously refer to an 8-bit number, you should use the term _octet_. But programmers are going to assume you mean 8-bits when you say “byte” unless you specify otherwise.[↩︎](variables-and-statements.html#fnref33)

  34. I’m seriously oversimplifying how modern memory works, here. But the mental model works, so please forgive me.[↩︎](variables-and-statements.html#fnref34)

  35. I’m lying here a little. Technically `3.14159` is of type `double`, but we’re not there yet and I want you to associate `float` with “Floating Point”, and C will happily coerce that type into a `float`. In short, don’t worry about it until later.[↩︎](variables-and-statements.html#fnref35)

  36. Read this as “pointer to a char” or “char pointer”. “Char” for character. Though I can’t find a study, it seems anecdotally most people pronounce this as “char”, a minority say “car”, and a handful say “care”. We’ll talk more about pointers later.[↩︎](variables-and-statements.html#fnref36)

  37. Colloquially, we say they have “random” values, but they aren’t truly—or even pseudo-truly—random numbers.[↩︎](variables-and-statements.html#fnref37)

  38. This isn’t strictly 100% true. When we get to learning about static storage duration, you’ll find the some variables are initialized to zero automatically. But the safe thing to do is always initialize them.[↩︎](variables-and-statements.html#fnref38)

  39. Technically just one bit of a `char` is used to represent the `bool`, so it can either be zero or one. Except that what goes in the remaining (padding) bits of the `char` is unspecified. For `false`, it must surely be all zero. But for `true`, I’m uncertain that it must all be zero.[↩︎](variables-and-statements.html#fnref39)

  40. The `_t` is short for `type`.[↩︎](variables-and-statements.html#fnref40)

  41. Except for with variable length arrays—but that’s a story for another time.[↩︎](variables-and-statements.html#fnref41)

  42. https://beej.us/guide/bgclr/html/split/stdlib.html#man-srand[↩︎](variables-and-statements.html#fnref42)

  43. This was considered such a hazard that the designers of the Go Programming Language made `break` the default; you have to explicitly use Go’s `fallthrough` statement if you want to fall into the next case.[↩︎](variables-and-statements.html#fnref43)

  44. Never say “never”.[↩︎](functions.html#fnref44)

  45. Typically. I’m sure there are exceptions out there in the dark corridors of computing history.[↩︎](pointers.html#fnref45)

  46. A byte is a number made up of no more than 8 binary digits, or _bits_ for short. This means in decimal digits just like grandma used to use, it can hold an unsigned number between 0 and 255, inclusive.[↩︎](pointers.html#fnref46)

  47. The order that bytes come in is referred to as the _endianness_ of the number. The usual suspects are _big-endian_ (with the most significant byte first) and _little-endian_ (with the most-significant byte last), or, uncommonly now, _mixed-endian_ (with the most-significant bytes somewhere else).[↩︎](pointers.html#fnref47)

  48. That is, base 16 with digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F.[↩︎](pointers.html#fnref48)

  49. https://en.wikipedia.org/wiki/Virtual_memory[↩︎](pointers.html#fnref49)

  50. That’s not all! It’s used in `/*comments*/` and multiplication and in function prototypes with variable length arrays! It’s all the same `*`, but the context gives it different meaning.[↩︎](pointers.html#fnref50)

  51. https://en.wikipedia.org/wiki/Null_pointer#History[↩︎](pointers.html#fnref51)

  52. https://en.wikipedia.org/wiki/Sentinel_value[↩︎](pointers.html#fnref52)

  53. The pointer type variables are `a`, `d`, `f`, and `i`, because those are the ones with `*` in front of them.[↩︎](pointers.html#fnref53)

  54. These days, anyway.[↩︎](arrays.html#fnref54)

  55. Again, not really, but variable-length arrays—of which I’m not really a fan—are a story for another time.[↩︎](arrays.html#fnref55)

  56. Since arrays are just pointers to the first element of the array under the hood, there’s no additional information recording the length.[↩︎](arrays.html#fnref56)

  57. Because when you pass an array to a function, you’re actually just passing a pointer to the first element of that array, not the “entire” array.[↩︎](arrays.html#fnref57)

  58. In the good old MS-DOS days before memory protection was a thing, I was writing some particularly abusive C code that deliberately engaged in all kinds of undefined behavior. But I knew what I was doing, and things were working pretty well. Until I made a misstep that caused a lockup and, as I found upon reboot, nuked all my BIOS settings. That was fun. (Shout-out to @man for those fun times.)[↩︎](arrays.html#fnref58)

  59. There are a lot of things that cause undefined behavior, not just out-of-bounds array accesses. This is what makes the C language so _exciting_.[↩︎](arrays.html#fnref59)

  60. https://en.wikipedia.org/wiki/Row-_and_column-major_order[↩︎](arrays.html#fnref60)

  61. This is technically incorrect, as a pointer to an array and a pointer to the first element of an array have different types. But we can burn that bridge when we get to it.[↩︎](arrays.html#fnref61)

  62. C11 §6.7.6.2¶1 requires it be greater than zero. But you might see code out there with arrays declared of zero length at the end of `struct`s and GCC is particularly lenient about it unless you compile with `-pedantic`. This zero-length array was a hackish mechanism for making variable-length structures. Unfortunately, it’s technically undefined behavior to access such an array even though it basically worked everywhere. C99 codified a well-defined replacement for it called _flexible array members_ , which we’ll chat about later.[↩︎](arrays.html#fnref62)

  63. This is also equivalent: `void print_2D_array(int (*a)[3])`, but that’s more than I want to get into right now.[↩︎](arrays.html#fnref63)

  64. Though it is true that C doesn’t track the length of strings.[↩︎](strings.html#fnref64)

  65. If you’re using the basic character set or an 8-bit character set, you’re used to one character being one byte. This isn’t true in all character encodings, though.[↩︎](strings.html#fnref65)

  66. This is different than the `NULL` pointer, and I’ll abbreviate it `NUL` when talking about the character versus `NULL` for the pointer.[↩︎](strings.html#fnref66)

  67. Later we’ll learn a neater way to do it with pointer arithmetic.[↩︎](strings.html#fnref67)

  68. There’s another function called `strncpy()` that limits the number of bytes copied. Some people say that you should always use `strncpy()` because of the buffer overrun protection. Other people say you should never use `strncpy()` because it won’t necessarily terminate your strings, another grotesque footgun. If you want to be really safe, you can write your own version of `strncpy()` that always terminates the string.[↩︎](strings.html#fnref68)

  69. Although in C individual items in memory like `int`s are referred to as “objects”, they’re not objects in an object-oriented programming sense.[↩︎](structs.html#fnref69)

  70. The Saturn was a popular brand of economy car in the United States until it was put out of business by the 2008 crash, sadly so to us fans.[↩︎](structs.html#fnref70)

  71. A pointer is likely 8 bytes on a 64-bit system.[↩︎](structs.html#fnref71)

  72. A _deep copy_ follows pointer in the `struct` and copies the data they point to, as well. A _shallow copy_ just copies the pointers, but not the things they point to. C doesn’t come with any built-in deep copy functionality.[↩︎](structs.html#fnref72)

  73. https://beej.us/guide/bgclr/html/split/stringref.html#man-strcmp[↩︎](structs.html#fnref73)

  74. https://beej.us/guide/bgclr/html/split/stringref.html#man-memset[↩︎](structs.html#fnref74)

  75. https://stackoverflow.com/questions/141720/how-do-you-compare-structs-for-equality-in-c[↩︎](structs.html#fnref75)

  76. We used to have three different newlines in broad effect: Carriage Return (CR, used on old Macs), Linefeed (LF, used on Unix systems), and Carriage Return/Linefeed (CRLF, used on Windows systems). Thankfully the introduction of OS X, being Unix-based, reduced this number to two.[↩︎](file-inputoutput.html#fnref76)

  77. If the buffer’s not big enough to read in an entire line, it’ll just stop reading mid-line, and the next call to `fgets()` will continue reading the rest of the line.[↩︎](file-inputoutput.html#fnref77)

  78. Normally the second program would read all the bytes at once, and _then_ print them out in a loop. That would be more efficient. But we’re going for demo value, here.[↩︎](file-inputoutput.html#fnref78)

  79. https://en.wikipedia.org/wiki/Hex_dump[↩︎](file-inputoutput.html#fnref79)

  80. https://en.wikipedia.org/wiki/Endianess[↩︎](file-inputoutput.html#fnref80)

  81. And this is why I used individual bytes in my `fwrite()` and `fread()` examples, above, shrewdly.[↩︎](file-inputoutput.html#fnref81)

  82. https://en.wikipedia.org/wiki/Protocol_buffers[↩︎](file-inputoutput.html#fnref82)

  83. We’ll talk more about these later.[↩︎](typedef-making-new-types.html#fnref83)

  84. Recall that the `sizeof` operator tells you the size in bytes of an object in memory.[↩︎](pointers2.html#fnref84)

  85. Or string, which is really an array of `char`s. Somewhat peculiarly, you can also have a pointer that references _one past_ the end of the array without a problem and still do math on it. You just can’t dereference it when it’s out there.[↩︎](pointers2.html#fnref85)

  86. https://beej.us/guide/bgclr/html/split/stdlib.html#man-qsort[↩︎](pointers2.html#fnref86)

  87. https://beej.us/guide/bgclr/html/split/stdlib.html#man-bsearch[↩︎](pointers2.html#fnref87)

  88. Because remember that array notation is just a dereference and some pointer math, and you can’t dereference a `void*`![↩︎](pointers2.html#fnref88)

  89. You can also _cast_ the `void*` to another type, but we haven’t gotten to casts yet.[↩︎](pointers2.html#fnref89)

  90. Or until the program exits, in which case all the memory allocated by it is freed. Asterisk: some systems allow you to allocate memory that persists after a program exits, but it’s system dependent, out of scope for this guide, and you’ll certainly never do it on accident.[↩︎](manual-memory-allocation.html#fnref90)

  91. http://www.open-std.org/jtc1/sc22/wg14/www/docs/summary.htm#dr_460[↩︎](manual-memory-allocation.html#fnref91)

  92. https://en.wikipedia.org/wiki/Bit_bucket[↩︎](scope.html#fnref92)

  93. “Bit” is short for _binary digit_. Binary is just another way of representing numbers. Instead of digits 0-9 like we’re used to, it’s digits 0-1.[↩︎](types-ii-way-more-types.html#fnref93)

  94. https://en.wikipedia.org/wiki/Two%27s_complement[↩︎](types-ii-way-more-types.html#fnref94)

  95. The industry term for a sequence of exactly, indisputably 8 bits is an _octet_.[↩︎](types-ii-way-more-types.html#fnref95)

  96. In general, if you have an \\(n\\) bit two’s complement number, the signed range is \\(-2^{n-1}\\) to \\(2^{n-1}-1\\). And the unsigned range is \\(0\\) to \\(2^n-1\\).[↩︎](types-ii-way-more-types.html#fnref96)

  97. https://en.wikipedia.org/wiki/ASCII[↩︎](types-ii-way-more-types.html#fnref97)

  98. https://en.wikipedia.org/wiki/List_of_information_system_character_sets[↩︎](types-ii-way-more-types.html#fnref98)

  99. https://en.wikipedia.org/wiki/Unicode[↩︎](types-ii-way-more-types.html#fnref99)

  100. Depends on if a `char` defaults to `signed char` or `unsigned char`[↩︎](types-ii-way-more-types.html#fnref100)

  101. https://en.wikipedia.org/wiki/Signed_number_representations#Signed_magnitude_representation[↩︎](types-ii-way-more-types.html#fnref101)

  102. My `char` is signed.[↩︎](types-ii-way-more-types.html#fnref102)

  103. https://en.wikipedia.org/wiki/IEEE_754[↩︎](types-ii-way-more-types.html#fnref103)

  104. This program runs as its comments indicate on a system with `FLT_DIG` of `6` that uses IEEE-754 base-2 floating point numbers. Otherwise, you might get different output.[↩︎](types-ii-way-more-types.html#fnref104)

  105. It’s really surprising to me that C doesn’t have this in the spec yet. In the C99 Rationale document, they write, “A proposal to add binary constants was rejected due to lack of precedent and insufficient utility.” Which seems kind of silly in light of some of the other features they kitchen-sinked in there! I’ll bet one of the next releases has it.[↩︎](types-ii-way-more-types.html#fnref105)

  106. https://en.wikipedia.org/wiki/Scientific_notation[↩︎](types-ii-way-more-types.html#fnref106)

  107. They’re the same except `snprintf()` allows you to specify a maximum number of bytes to output, preventing the overrunning of the end of your string. So it’s safer.[↩︎](types-iii-conversions.html#fnref107)

  108. https://en.wikipedia.org/wiki/ASCII[↩︎](types-iii-conversions.html#fnref108)

  109. We have to pass a pointer to `badchar` to `strtoul()` or it won’t be able to modify it in any way we can see, analogous to why you have to pass a pointer to an `int` to a function if you want that function to be able to change that value of that `int`.[↩︎](types-iii-conversions.html#fnref109)

  110. Each character has a value associated with it for any given character encoding scheme.[↩︎](types-iii-conversions.html#fnref110)

  111. In practice, what’s probably happening on your implementation is that the high-order bits are just being dropped from the result, so a 16-bit number `0x1234` being converted to an 8-bit number ends up as `0x0034`, or just `0x34`.[↩︎](types-iii-conversions.html#fnref111)

  112. Again, in practice, what will likely happen on your system is that the bit pattern for the original will be truncated and then just used to represent the signed number, two’s complement. For example, my system takes an `unsigned char` of `192` and converts it to `signed char` `-64`. In two’s complement, the bit pattern for both these numbers is binary `11000000`.[↩︎](types-iii-conversions.html#fnref112)

  113. Not really—it’s just discarded regularly.[↩︎](types-iii-conversions.html#fnref113)

  114. Functions with a variable number of arguments.[↩︎](types-iii-conversions.html#fnref114)

  115. This is rarely done because the compiler will complain and having a prototype is the _Right Thing_ to do. I think this still works for historic reasons, before prototypes were a thing.[↩︎](types-iii-conversions.html#fnref115)

  116. https://beej.us/guide/bgclr/html/split/ctype.html[↩︎](types-iii-conversions.html#fnref116)

  117. https://gustedt.wordpress.com/2010/08/17/a-common-misconsception-the-register-keyword/[↩︎](types-iv-qualifiers-and-specifiers.html#fnref117)

  118. https://en.wikipedia.org/wiki/Processor_register[↩︎](types-iv-qualifiers-and-specifiers.html#fnref118)

  119. https://en.wikipedia.org/wiki/Boids[↩︎](multifile-projects.html#fnref119)

  120. Historially, MS-DOS and Windows programs would do this differently than Unix. In Unix, the shell would _expand_ the wildcard into all matching files before your program saw it, whereas the Microsoft variants would pass the wildcard expression into the program to deal with. In any case, there are arguments that get passed into the program.[↩︎](the-outside-environment.html#fnref120)

  121. Since they’re just regular parameter names, you don’t actually have to call them `argc` and `argv`. But it’s so very idiomatic to use those names, if you get creative, other C programmers will look at you with a suspicious eye, indeed![↩︎](the-outside-environment.html#fnref121)

  122. `ps`, Process Status, is a Unix command to see what processes are running at the moment.[↩︎](the-outside-environment.html#fnref122)

  123. https://en.wikipedia.org/wiki/Inception[↩︎](the-outside-environment.html#fnref123)

  124. https://en.wikipedia.org/wiki/Shell_(computing)[↩︎](the-outside-environment.html#fnref124)

  125. In Windows `cmd.exe`, type `echo %errorlevel%`. In PowerShell, type `$LastExitCode`.[↩︎](the-outside-environment.html#fnref125)

  126. If you need a numeric value, convert the string with something like `atoi()` or `strtol()`.[↩︎](the-outside-environment.html#fnref126)

  127. In Windows CMD.EXE, use `set FROTZ=value`. In PowerShell, use `$Env:FROTZ=value`.[↩︎](the-outside-environment.html#fnref127)

  128. https://pubs.opengroup.org/onlinepubs/9699919799/functions/exec.html[↩︎](the-outside-environment.html#fnref128)

  129. You can’t always just wrap the code in `/*` `*/` comments because those won’t nest.[↩︎](the-c-preprocessor.html#fnref129)

  130. This isn’t really a macro—it’s technically an identifier. But it’s the only predefined identifier and it feels very macro-like, so I’m including it here. Like a rebel.[↩︎](the-c-preprocessor.html#fnref130)

  131. A hosted implementation basically means you’re running the full C standard, probably on an operating system of some kind. Which you probably are. If you’re running on bare metal in some kind of embedded system, you’re probably on a _standalone implementation_.[↩︎](the-c-preprocessor.html#fnref131)

  132. OK, I know that was a cop-out answer. Basically there’s an optional extension compilers can implement wherein they agree to limit certain types of undefined behavior so that the C code is more amenable to static code analysis. It is unlikely you’ll need to use this.[↩︎](the-c-preprocessor.html#fnref132)

  133. _Breakin’ the law… breakin’ the law…_[↩︎](the-c-preprocessor.html#fnref133)

  134. https://www.openmp.org/[↩︎](the-c-preprocessor.html#fnref134)

  135. Technically we say that it has an _incomplete type_.[↩︎](structs-ii-more-fun-with-structs.html#fnref135)

  136. Though some compilers have options to force this to occur—search for `__attribute__((packed))` to see how to do this with GCC.[↩︎](structs-ii-more-fun-with-structs.html#fnref136)

  137. `super` isn’t a keyword, incidentally. I’m just stealing some OOP terminology.[↩︎](structs-ii-more-fun-with-structs.html#fnref137)

  138. Assuming 8-bit `char`s, i.e. `CHAR_BIT == 8`.[↩︎](structs-ii-more-fun-with-structs.html#fnref138)

  139. https://en.wikipedia.org/wiki/Type_punning[↩︎](structs-ii-more-fun-with-structs.html#fnref139)

  140. I just made up that number, but it’s probably not far off[↩︎](characters-and-strings-ii.html#fnref140)

  141. There’s some devil in the details with values that are stored in registers only, but we can safely ignore that for our purposes here. Also the C spec makes no stance on these “register” things beyond the `register` keyword, the description for which doesn’t mention registers.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref141)

  142. You’re very likely to get different numbers on yours.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref142)

  143. There is absolutely nothing in the spec that says this will always work this way, but it happens to work this way on my system.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref143)

  144. Even if `E` is `NULL`, it turns out, weirdly.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref144)

  145. https://beej.us/guide/bgclr/html/split/stringref.html#man-memcpy[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref145)

  146. Your C compiler is not required to add padding bytes, and the values of any padding bytes that are added are indeterminate.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref146)

  147. This will vary depending on the architecture, but my system is _little endian_ , which means the least-significant byte of the number is stored first. _Big endian_ systems will have the `12` first and the `78` last. But the spec doesn’t dictate anything about this representation.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref147)

  148. It’s an optional feature, so it might not be there—but it probably is.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref148)

  149. I’m printing out the 16-bit values reversed since I’m on a little-endian machine and it makes it easier to read here.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref149)

  150. Assuming they point to the same array object.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref150)

  151. The Go Programming Language drew its type declaration syntax inspiration from the opposite of what C does.[↩︎](pointers-iii-pointers-to-pointers-and-more.html#fnref151)

  152. Not that other languages don’t do this—they do. It is interesting how many modern languages use the same operators for bitwise that C does.[↩︎](bitwise-operations.html#fnref152)

  153. https://en.wikipedia.org/wiki/Bitwise_operation[↩︎](bitwise-operations.html#fnref153)

  154. That is, us lowly developers aren’t supposed to know what’s in there or what it means. The spec doesn’t dictate what it is in detail.[↩︎](variadic-functions.html#fnref154)

  155. Honestly, it would be possible to remove that limitation from the language, but the idea is that the macros `va_start()`, `va_arg()`, and `va_end()` should be able to be written in C. And to make that happen, we need some way to initialize a pointer to the location of the first parameter. And to do that, we need the _name_ of the first parameter. It would require a language extension to make this possible, and so far the committee hasn’t found a rationale for doing so.[↩︎](variadic-functions.html#fnref155)

  156. “This planet has—or rather had—a problem, which was this: most of the people living on it were unhappy for pretty much of the time. Many solutions were suggested for this problem, but most of these were largely concerned with the movement of small green pieces of paper, which was odd because on the whole it wasn’t the small green pieces of paper that were unhappy.” —The Hitchhiker’s Guide to the Galaxy, Douglas Adams[↩︎](locale-and-internationalization.html#fnref156)

  157. Remember that `char` is just a byte-sized integer.[↩︎](locale-and-internationalization.html#fnref157)

  158. Except for `isdigit()` and `isxdigit()`.[↩︎](locale-and-internationalization.html#fnref158)

  159. For example, we could store the code point in a big-endian 32-bit integer. Straightforward! We just invented an encoding! Actually not; that’s what UTF-32BE encoding is. Oh well—back to the grind![↩︎](unicode-wide-characters-and-all-that.html#fnref159)

  160. Ish. Technically, it’s variable width—there’s a way to represent code points higher than \\(2^{16}\\) by putting two UTF-16 characters together.[↩︎](unicode-wide-characters-and-all-that.html#fnref160)

  161. There’s a special character called the _Byte Order Mark_ (BOM), code point 0xFEFF, that can optionally precede the data stream and indicate the endianess. It is not required, however.[↩︎](unicode-wide-characters-and-all-that.html#fnref161)

  162. Again, this is only true in UTF-16 for characters that fit in two bytes.[↩︎](unicode-wide-characters-and-all-that.html#fnref162)

  163. https://en.wikipedia.org/wiki/UTF-8[↩︎](unicode-wide-characters-and-all-that.html#fnref163)

  164. https://www.youtube.com/watch?v=MijmeoH9LT4[↩︎](unicode-wide-characters-and-all-that.html#fnref164)

  165. Presumably the compiler makes the best effort to translate the code point to whatever the output encoding is, but I can’t find any guarantees in the spec.[↩︎](unicode-wide-characters-and-all-that.html#fnref165)

  166. With a format specifier like `"%.12s"`, for example.[↩︎](unicode-wide-characters-and-all-that.html#fnref166)

  167. `wcscoll()` is the same as `wcsxfrm()` followed by `wcscmp()`.[↩︎](unicode-wide-characters-and-all-that.html#fnref167)

  168. Ish—things get funky with multi-`char16_t` UTF-16 encodings.[↩︎](unicode-wide-characters-and-all-that.html#fnref168)

  169. https://en.wikipedia.org/wiki/Iconv[↩︎](unicode-wide-characters-and-all-that.html#fnref169)

  170. http://site.icu-project.org/[↩︎](unicode-wide-characters-and-all-that.html#fnref170)

  171. https://en.wikipedia.org/wiki/Core_dump[↩︎](exiting-a-program.html#fnref171)

  172. Apparently it doesn’t do Unix-style signals at all deep down, and they’re simulated for console apps.[↩︎](signal-handling.html#fnref172)

  173. Confusingly, `sig_atomic_t` predates the lock-free atomics and is not the same thing.[↩︎](signal-handling.html#fnref173)

  174. If `sig_action_t` is signed, the range will be at least `-127` to `127`. If unsigned, at least `0` to `255`.[↩︎](signal-handling.html#fnref174)

  175. This is due to how VLAs are typically allocated on the stack, whereas `static` variables are on the heap. And the whole idea with VLAs is they’ll be automatically dellocated when the stack frame is popped at the end of the function.[↩︎](variable-length-arrays-vlas.html#fnref175)

  176. https://en.wikipedia.org/wiki/Goto#Criticism[↩︎](goto.html#fnref176)

  177. I’d like to point out that using `goto` in all these cases is avoidable. You can use variables and loops instead. It’s just that some people think `goto` produces the _best_ code in those circumstances.[↩︎](goto.html#fnref177)

  178. https://en.wikipedia.org/wiki/Tail_call[↩︎](goto.html#fnref178)

  179. Which isn’t quite the same, since it’s an array, not a pointer to an `int`.[↩︎](types-part-v-compound-literals-and-generic-selections.html#fnref179)

  180. A variable used here _is_ an expression.[↩︎](types-part-v-compound-literals-and-generic-selections.html#fnref180)

  181. Both “stack pointer” and “program counter” are related to the underlying architecture and C implementation, and are not part of the spec.[↩︎](setjmp-longjmp.html#fnref181)

  182. The rationale here is that the program might store a value temporarily in a _CPU register_ while it’s doing work on it. In that timeframe, the register holds the correct value, and the value on the stack might be out of date. Then later the register values would get overwritten and the changes to the variable lost.[↩︎](setjmp-longjmp.html#fnref182)

  183. That is, remain allocated until the program ends with no way to free it.[↩︎](setjmp-longjmp.html#fnref183)

  184. This works because in C, pointers are the same size regardless of the type of data they point to. So the compiler doesn’t need to know the size of the `struct node` at this point; it just needs to know the size of a pointer.[↩︎](incomplete-types.html#fnref184)

  185. https://en.wikipedia.org/wiki/Complex_number[↩︎](complex-numbers.html#fnref185)

  186. This was a harder one to research, and I’ll take any more information anyone can give me. `I` could be defined as `_Complex_I` or `_Imaginary_I`, if the latter exists. `_Imaginary_I` will handle signed zeros, but `_Complex_I` _might_ not. This has implications with branch cuts and other complex-numbery-mathy things. Maybe. Can you tell I’m really getting out of my element here? In any case, the `CMPLX()` macros behave as if `I` were defined as `_Imaginary_I`, with signed zeros, even if `_Imaginary_I` doesn’t exist on the system.[↩︎](complex-numbers.html#fnref186)

  187. The simplicity of this statement doesn’t do justice to the incredible amount of work that goes into simply understanding how floating point actually functions. https://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/[↩︎](complex-numbers.html#fnref187)

  188. This is the only one that doesn’t begin with an extra leading `c`, strangely.[↩︎](complex-numbers.html#fnref188)

  189. Some architectures have different sized data that the CPU and RAM can operate with at a faster rate than others. In those cases, if you need the fastest 8-bit number, it might give you have a 16- or 32-bit type instead because that’s just faster. So with this, you won’t know how big the type is, but it will be least as big as you say.[↩︎](fixed-width-integer-types.html#fnref189)

  190. Namely, the system has 8, 16, 32, or 64 bit integers with no padding that use two’s complement representation, in which case the `intN_t` variant for that particular number of bits _must_ be defined.[↩︎](fixed-width-integer-types.html#fnref190)

  191. On Earth, anyway. Who know what crazy systems they use _out there_ …[↩︎](date-and-time-functionality.html#fnref191)

  192. OK, don’t murder me! GMT is technically a time zone while UTC is a global time system. Also some countries might adjust GMT for daylight saving time, whereas UTC is never adjusted for daylight saving time.[↩︎](date-and-time-functionality.html#fnref192)

  193. Admittedly, there are more than two.[↩︎](date-and-time-functionality.html#fnref193)

  194. https://en.wikipedia.org/wiki/Unix_time[↩︎](date-and-time-functionality.html#fnref194)

  195. https://beej.us/guide/bgclr/html/split/time.html#man-strftime[↩︎](date-and-time-functionality.html#fnref195)

  196. You will on POSIX, where `time_t` is definitely an integer. Unfortunately the entire world isn’t POSIX, so there we are.[↩︎](date-and-time-functionality.html#fnref196)

  197. https://en.wikipedia.org/wiki/POSIX_Threads[↩︎](multithreading.html#fnref197)

  198. I’m more a fan of shared-nothing, myself, and my skills with classic multithreading constructs are rusty, to say the least.[↩︎](multithreading.html#fnref198)

  199. Yes, `pthreads` with a “`p`”. It’s short for POSIX threads, a library that C11 borrowed liberally from for its threads implementation.[↩︎](multithreading.html#fnref199)

  200. Per §7.1.4¶5.[↩︎](multithreading.html#fnref200)

  201. Unless you `thrd_detach()`. More on this later.[↩︎](multithreading.html#fnref201)

  202. Though I don’t think they have to be. It’s just that the threads don’t seem to get rescheduled until some system call like might happen with a `printf()`… which is why I have the `printf()` in there.[↩︎](multithreading.html#fnref202)

  203. Short for “mutual exclusion”, AKA a “lock” on a section of code that only one thread is permitted to execute.[↩︎](multithreading.html#fnref203)

  204. That is, your process will go to sleep.[↩︎](multithreading.html#fnref204)

  205. You might have expected it to be “time from now”, but you’d just like to think that, wouldn’t you![↩︎](multithreading.html#fnref205)

  206. And that’s why they’re called _condition variables_![↩︎](multithreading.html#fnref206)

  207. I’m not saying it’s aliens… but it’s aliens. OK, really more likely another thread might have been woken up and gotten to the work first.[↩︎](multithreading.html#fnref207)

  208. Survival of the fittest! Right? I admit it’s actually nothing like that.[↩︎](multithreading.html#fnref208)

  209. The `__STDC_VERSION__` macro didn’t exist in early C89, so if you’re worried about that, check it with `#ifdef`.[↩︎](chapter-atomics.html#fnref209)

  210. The reason for this is when optimized, my compiler has put the value of `x` in a register to make the `while` loop fast. But the register has no way of knowing that the variable was updated in another thread, so it never sees the `3490`. This isn’t really related to the _all-or-nothing_ part of atomicity, but is more related to the synchronization aspects in the next section.[↩︎](chapter-atomics.html#fnref210)

  211. Until I say otherwise, I’m speaking generally about _sequentially consistent_ operations. More on what that means soon.[↩︎](chapter-atomics.html#fnref211)

  212. Sanest from a programmer perspective.[↩︎](chapter-atomics.html#fnref212)

  213. Apparently C++23 is adding this as a macro.[↩︎](chapter-atomics.html#fnref213)

  214. The spec notes that they might differ in size, representation, and alignment.[↩︎](chapter-atomics.html#fnref214)

  215. I just pulled that example out of nowhere. Maybe it doesn’t matter on Intel/AMD, but it could matter somewhere, dangit![↩︎](chapter-atomics.html#fnref215)

  216. C++ elaborates that if the signal is the result of a call to `raise()`, it is sequenced _after_ the `raise()`.[↩︎](chapter-atomics.html#fnref216)

  217. https://en.wikipedia.org/wiki/Test-and-set[↩︎](chapter-atomics.html#fnref217)

  218. Because consume is all about the operations that are dependent on the value of the acquired atomic variable, and there is no atomic variable with a fence.[↩︎](chapter-atomics.html#fnref218)

  219. https://www.youtube.com/watch?v=A8eCGOqgvH4[↩︎](chapter-atomics.html#fnref219)

  220. https://www.youtube.com/watch?v=KeLBd2EJLOU[↩︎](chapter-atomics.html#fnref220)

  221. https://preshing.com/archives/[↩︎](chapter-atomics.html#fnref221)

  222. https://preshing.com/20120612/an-introduction-to-lock-free-programming/[↩︎](chapter-atomics.html#fnref222)

  223. https://preshing.com/20120913/acquire-and-release-semantics/[↩︎](chapter-atomics.html#fnref223)

  224. https://preshing.com/20130702/the-happens-before-relation/[↩︎](chapter-atomics.html#fnref224)

  225. https://preshing.com/20130823/the-synchronizes-with-relation/[↩︎](chapter-atomics.html#fnref225)

  226. https://preshing.com/20140709/the-purpose-of-memory_order_consume-in-cpp11/[↩︎](chapter-atomics.html#fnref226)

  227. https://preshing.com/20150402/you-can-do-any-kind-of-atomic-read-modify-write-operation/[↩︎](chapter-atomics.html#fnref227)

  228. https://en.cppreference.com/w/c/atomic/memory_order[↩︎](chapter-atomics.html#fnref228)

  229. https://en.cppreference.com/w/c/language/atomic[↩︎](chapter-atomics.html#fnref229)

  230. https://docs.microsoft.com/en-us/windows/win32/dxtecharts/lockless-programming[↩︎](chapter-atomics.html#fnref230)

  231. https://www.reddit.com/r/C_Programming/[↩︎](chapter-atomics.html#fnref231)

  232. Unless you compile with optimizations on (probably)! But I think when it does this, it’s not behaving to spec.[↩︎](function-specifiers-alignment-specifiersoperators.html#fnref232)

  233. https://beej.us/guide/bgclr/html/split/stdlib.html#man-exit[↩︎](function-specifiers-alignment-specifiersoperators.html#fnref233)

  234. https://beej.us/guide/bgclr/html/split/stdlib.html#man-abort[↩︎](function-specifiers-alignment-specifiersoperators.html#fnref234)

  235. https://en.wikipedia.org/wiki/Data_structure_alignment[↩︎](function-specifiers-alignment-specifiersoperators.html#fnref235)




* * *

[Prev](chapter-atomics.html) | [Contents](index.html) | [Next](function-specifiers-alignment-specifiersoperators.html)

