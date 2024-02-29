# 🔢 MATH ALGORITHMS 🔢

## Overview

<font size="+1">
Welcome to the "math" package of the "algorithms" library. This package
provides functionalities for dealing with many mathematical issues, like 
calculating factorial, finding root of the function, checking triangle properties and many more.  
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
Once installed, you can import the math package and utilize its functionalities in Python. 
</font>

## Arithmetic algorithms 🧮

<font size="+1">
Arithmetic algorithms module provides essential tools for numerical computations.
It includes functions for binary search, Babylonian sqare root calculation,
binary exponentiation, and both iterative and recursive factorial calculations.
<br>

```
from algorithms.math.arithmetic_algorithms import (
    binary_search,
    babylonian_sqrt
    binary_exponentiation,
    iterative_factorial,
    recursive_factorial,
)
```

#### Binary search

```
numbers = [10, 20, 30, 40, 50]
looked_number = 30
result = binary_search(numbers, looked_number) 

print(f'Index of number {looked_number} in numbers: {result}')   # 2 
```

#### Babylonian square root finder

```
number = 225
square_root = babylonian_sqrt(number)

print(f'Square root of number {number} in equal to: {square_root}')   # 15
```

#### Binary exponentiation

```
number = 4
power = 5
num_raised_to_pow = binary_exponentiation(number, power)

print(f'Number {number} raised to power {power} equals: {num_raised_to_pow}')   # 1025
```  

#### Iterative factorial

```
number = 8
factorial = iterative_factorial(number)

print(f'Factorial of number {number} is equal: {factorial}')                    # 40320
```  

#### Recursive factorial

```
number = 5
factorial = recursive_factorial(number)

print(f'Factorial of number {number} is equal: {factorial}')                    # 120
```  

</font>

## Function algorithms 🧮

<font size="+1">
Arithmetic algorithms module provides essential tools for numerical computations.
It includes functions for binary search, Babylonian sqare root calculation,
binary exponentiation, and both iterative and recursive factorial calculations.
<br>

```
from algorithms.math.function_algorithms import (
    bisection_root_finder,
    quadratic_roots_finder,
    horner_evaluation,
    trapezoidal_integration,
    rectangle_integration
)
```

#### Binary search

```
numbers = [10, 20, 30, 40, 50]
looked_number = 30
result = binary_search(numbers, looked_number) 

print(f'Index of number {looked_number} in numbers: {result}')   # 2 
```

</font>

## Geometric algorithms 📐

<font size="+1">
This module provides essential tools for geometrical computations. It includes functions
to calculate distances between points in a 2-dimensional plane, check if three points
are collinear, verify if given side length can form a valid triangle, and determine if
a triangle with given side lengths is a rectangular triangle.
<br>

```
from algorithms.math.geometric_algorithms import (
    Point,
    distance_between_points,
    are_points_collinear,
    is_triangle_valid,
    is_triangle_rectangular,
)

```

#### Distance between points

```
# Creating two instances of Point class

point_1 = Point(-2, -3)
point_2 = Point(1, 1)
distance = distance_between_points(point_1, point_2)

print(f'Distance between point_1 {point_1} and point_2 {point_2} is equal {distance}')   # 5.0 
```

#### Checking collinearity of 3 points

```
# Creating three instances of Point class

point_1 = Point(-12, -14)
point_2 = Point(10, 30)
point_3 = Point(300, 610)
collinearity_result = are_points_collinear(point_1, point_2, points_3)

print(f'Point_1, point_2 and point_3 are collinear: {collinearity_result}')   # True
```

#### Checking triangle validity

```
a_side = 5
b_side = 10
c_side = 8
# Invalid triangle with c_side_2 
c_side_2 = 3

validity_result = is_triangle_valid(a_side, b_side, c_side)
validity_result_2  = is_triangle_valid(a_side, b_side, c_side_2)

print(f'Triangle with sides {a_side}, {b_side} and {c_side} is a valid triangle: {validity_result}')       # True 
print(f'Triangle with sides {a_side}, {b_side} and {c_side_2} is a valid triangle: {validity_result_2}')   # False 
```

#### Checking if triangle is rectangular

```
a_side = 3
b_side = 4
c_side = 5

d_side = 1
e_side = 1
f_side = 1

result = is_triangle_rectangular(a_side, b_side, c_side)
result_2 = is_triangle_rectangular(d_side, e_side, f_side)

print(f'Triangle with sides {a_side}, {b_side} and {c_side} is rectangular: {result}')      # True
print(f'Triangle with sides {d_side}, {e_side} and {f_side} is rectangular: {result_2}')    # False

```

</font>




