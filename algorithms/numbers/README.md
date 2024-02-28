# 🔢 NUMBERS PACKAGE 🔢 
## Overview
<font size="+1">
Welcome to the "numbers" package of the "algorithms" library. This package
provides functionalities for dealing with numbers, including digit operations,
number base conversion and prime numbers. 
</font>

## Installation
<font size="+1">
To install the "algorithms" library and access this package, you can use pip:<br>
<br>
  
```
pip install algorithms
```

</font>

## Usage
<font size="+1">
Once installed, you can import the ciphers package and utilize its functionalities in Python. 
</font>

## Digits
<font size="+1">
Digits module provides functionalities for digits operations, like
getting the digit at the specific position, summing digits of the number
and moving zeroes at the end of the list.
<br>
  
```
from algorithms.numbers import digits
```
#### Digit at specified position
```
number = 532

first_digit = digits.get_digit(number, 0)               
second_digit = digits.get_digit(number, 1)              
third_digit = digits.get_digit(number, 2)               
out_of_range_position = digits.get_digit(number, 5)     

print(f'Digit at first position: {first_digit}')                    # 2
print(f'Digit at second position: {second_digit}')                  # 3
print(f'Digit at third position: {third_digit}')                    # 5
print(f'Digit at out of range position: {out_of_range_position}')   # 0


```
#### Digits sum
```
number = 128
number_2 = -159

digits_sum = digits.sum_digits(number)     
digits_sum_2 = digits.sum_digits(number_2) 

print(f'Digits sum of number: {digits_sum}')      # 11
print(f'Digits sum of number_2: {digits_sum_2}')  # 15
```
#### Moving zeroes
```
numbers = [0, 1, 0, 2, 4, 0, 5]
numbers_with_zeroes_at_the_end = digits.move_zeroes(numbers) 

print(f'Numbers with zeroes at the end: {numbers_with_zeroes_at_the_end}') #  [1, 2, 4, 5, 0, 0, 0] 

```  
</font>
