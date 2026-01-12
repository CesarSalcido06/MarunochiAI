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
