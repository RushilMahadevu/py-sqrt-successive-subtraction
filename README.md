# Manual Square Root
## Overview
**NOTE: THIS ALGORITHM WAS NOT MADE BY ME**
<br /><br />
This Python code implements the integer square root algorithm (also known as the integer square root or floor square root method) using an odd number series approach. The algorithm works by subtracting increasing odd numbers from the input number. The number of subtraction steps it takes to reduce the input to zero (or just below zero) corresponds to the integer square root of the number. This is a simple integer square root algorithm that works by iterative subtraction of odd numbers, avoiding floating-point calculations.
<br /><br />
## Here's how the algorithm works!

Start with subnum = 1
Repeatedly subtract successive odd numbers (1, 3, 5, 7, ...) from the input number
Count the number of subtractions
If the final subtraction reduces the number exactly to zero, the count is the square root
If the number becomes negative, it's not a perfect square

### For example:
*For 16: 16 - 1 = 15, 15 - 3 = 12, 12 - 5 = 7, 7 - 7 = 0 (4 steps = √16)
<br /><br />
For 15: Would stop at a negative number (not a perfect square)*
