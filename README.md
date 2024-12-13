# 🛠️ Method of Successive Subtraction 
## 🗺️ Overview

This Python code implements the integer square root algorithm (also known as the integer square root or floor square root method) using an odd number series approach. The algorithm works by subtracting increasing odd numbers from the input number. The number of subtraction steps it takes to reduce the input to zero (or just below zero) corresponds to the integer square root of the number. This is a simple integer square root algorithm that works by iterative subtraction of odd numbers, avoiding floating-point calculations.
<br />

## 🚀 How to run
### 1. Clone Project
``` bash
git clone https://github.com/RushilMahadevu/python-layout-sss.git
```

### 2. Change Directory
``` bash
cd python-layout-sss
```

### 3. Run
``` bash
python3 main.py
```

<br />

## 📝 How does the Algorithm Work

Start with subnum = 1
Repeatedly subtract successive odd numbers (1, 3, 5, 7, ...) from the input number
Count the number of subtractions
If the final subtraction reduces the number exactly to zero, the count is the square root
If the number becomes negative, it`s not a perfect square

### For example:
* For 16: 16 - 1 = 15, 15 - 3 = 12, 12 - 5 = 7, 7 - 7 = 0 (4 steps = √16)
<br /><br />
* For 15: Would stop at a negative number (not a perfect square)

## 🤗 Credits
The relationship between square numbers and the sum of odd numbers was known to Indian mathematicians like **Aryabhata** and **Brahmagupta**. The observation that a square number can be decomposed into a sum of consecutive odd numbers (for example, 16 = 1 + 3 + 5 + 7) was utilized in their mathematical works.
<br /><br />
Aryabhata: https://en.wikipedia.org/wiki/Aryabhatiya
<br /><br />
Brahmagupta: https://en.wikipedia.org/wiki/Brahmagupta
