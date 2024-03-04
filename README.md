<div align="center">
    <img src="logo.svg" alt="Logo">
    <h1 style="color:lightyellow;">⭐️ ALGOHUB - HUB OF ALGORITHMS ⭐️</h1>
    <h2 style="color:lightskyblue;">All algorithms implemented in PYTHON</h2>
</div>

<div align="center">
    <img src="coverage.svg" alt="coverage">
    <img src="https://img.shields.io/badge/build-pending-yellow.svg" alt="pending">
</div>

<div align="center">
    <img src="https://img.shields.io/badge/license-All%20Rights%20Reserved-lightgrey.svg" alt="License">
    <img src="https://img.shields.io/badge/Welcome-We%20are%20Glad%20You're%20Here-pink" alt="welcome">
</div>
<div>
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#about">About</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#documentation">Documentation</a></li>
        <li><a href="#quality">Code quality</a></li>
        <li><a href="#data">Data</a></li>
        <li><a href="#usage">Example usage</a></li>
        <li><a href="#algorithms">Algorithms</a></li>
        <ul>
        <li><a href="#numbers">Numbers</a></li>
        <li><a href="#math">Math</a></li>
        <li><a href="#strings">Strings</a></li>
        <li><a href="#ciphers">Ciphers</a></li>
        <li><a href="#sorting">Sorting</a></li>
        </ul>
    </ul>
</div>

<div>
<h2 id="about">

## About

<font size="+1">
This repository contains a collection of algorithms written in Python. You can find algorithms for handling numbers, 
including ciphers, strings and for sorting data. 
It is wise to learn and implement them in your projects 
💯<br>
</font>
</h2>
</div>

<div>
<h2 id="installation">

## Installation

<font size="+1">
To install this library and access algorithms, you can use pip:<br>
<br>

```
pip install algohub
```

</font>
</h2>
</div>


<div>
<h2 id="documentation">

## Documenation

<font size="+1"> 
Comprehensive documentation available at this link: <br>
<a href="https://ursmal1948.github.io/algorithms_hub/" target="_blank">SPHINX DOCUMENTATION</a><br>
<br>

## ‼️ 📄 Feel free to explore detailed README documentation for each package below 📃 ‼️

[NUMBERS](algohub/algorithms/numbers/README.md) <br>
[MATH](algohub/algorithms/math/README.md)<br>
[STRINGS](algohub/algorithms/strings/README.md)<br>
[CIPHERS](algohub/algorithms/ciphers/README.md)<br>
[SORTING](algohub/algorithms/sorting_README.md)
</font>
</h2>
</div>
<div>
<h2 id="quality">

## Code Quality Checks

<font size="+1">
<h3>
Pylint Rating <br>
</h3>
<h4>
Measures quality of code and its adherence to coding standards and best practices.
<br>
My score:
</h4>
<br>

```
Your code has been rated at 9.81/10 (previous run: 9.81/10, +0.00)
```

<h3>
Mypy<br>
</h3>
<h4>
Analyzes code to verify that the actual usage of variables, function arguments
and return values matches the type specified in the annotations (type hints).
Overall the code demonstrates high compatibility with type annotations.
</h4>
</font>
</h2>
</div>

<div>
<h2 id="data">

## Data

<font size="+1">
Except for algorithms in package there is also a data package. It consists of many
useful functions for retrieving the data from user, random number generation and
data validation. Feel free to explore it!
<br>
<br>
Example usage

```
from algohub.algorithms.data.validation import does_string_match_regex
```

```
pattern = r'^[A-Z]{3};[a-z]+;\d$'
text = "ULA;developer;2"
text_2 = "KLAUDIA;developer;3"

result = does_string_match_regex(text, pattern)
result_2 = does_string_match_regex(text_2, pattern)

print(f'Text {text} matches regex: {result}')       # True
print(f'Text {text_2} matches regex: {result_2}')   # False
```

</font>
</h2>
</div>


<div>
<h2 id="usage">

## Example usage of algorithms

<font size="+1">

### Ciphers

```
from algohub.algorithms.ciphers import vigenere
```

```
# Creating an instance of Vigenère square
key = "CAT" 
vigenere_square = VigenereCipher("CAT")
```

```
# Encrypting a text
plaintext = "HOME"
encrypted_text = vigenere_square.encrypt(plaintext) 
print(f'Encrypted: {encrypted_text}')                       # JOFG
```

```
# Decrypting a text
decrypted_text = vigenere_square.decrypt(encrypted_text)
print(f'Decrypted: {decrypted_text}')                       # HOME
```  

<br>

### Strings

```
from algohub.algorithms.strings import string_manipulation
```

```
compressed_string = string_manipulation.compress("ABCABa")
print(f'Compression: {compressed_string}') # A2B2C1a1
```

<br>

### Numbers

```
from algohub.algorithms.numbers.num_base_conversion import any_to_decimal, decimal_to_any
```

#### Decimal to binary conversion

```
decimal_number = 10
binary_number = decimal_to_any(decimal_number, 2)

print(f'Binary representation of {decimal_number}: {binary_number}')    # "1010"
```

#### Octal to decimal conversion

```
octal_number = '144'
decimal_number = any_to_decimal(octal_number, 8)

print(f'Decimal representation of {octal_number}: {decimal_number}')     # 100
```

</font>
</h2>
</div>

<div>
<h2 id="algorithms">
<h2 align="center">OVERVIEW OF ALGORITHMS</h2>
<font size="+1">
</font>
</h2>
</div>

<div>
    <h2 id="numbers">Numbers</h2>
    <h3>
    Digits 
<ul style="margin-bottom: 10px; font-weight: 300;">
        <li>
        get_digits
        </li>
        <li>sum_digits</li>    
        <li>move_zeroes
</li>
</ul>
    </h3>
 <h3>
    Divisors
<ul style="margin-bottom: 10px; font-weight: 300;">
         <li>count_divisors</li>
        <li>count_common_divisors</li>
        <li>sum_divisors</li>
</ul>
    </h3>
 <h3>
    Primes
<ul style="margin-bottom: 10px; font-weight: 300;">
        <li>Eratosthenes Sieve</li>   
        <li>is_prime_basic</li>   
        <li>get_prime_factors</li>   
        <li>is_perfect_number</li>   

</ul>
    </h3>
 <h3>
    Number base conversion
<ul style="margin-bottom: 10px; font-weight: 300;">
        <li>decimal_to_any & any_to_decimal</li>
        <li>decimal_to_hexadecimal & hexadecimal_to_decimal</li>
        <li>binary_to_hexadecimal & hexadecimal_to_binary</li>    
        <li>binary_to_octal & octal_to_binary</li>    
        <li>octal_to_hexadecimal & hexadecimal_to_octal</li>    

</ul>
    </h3>
<h2 id="math">Math</h2>
<h3>
    Arithmetic algorithms
<ul style="margin-bottom: 10px; font-weight: 300;">
        <li>binary_search</li>
        <li>babylonian_sqrt</li>    
        <li>binary_exponentiation</li> 
        <li>iterative_factorial</li> 
        <li>recursive_factorial</li>
</ul>
    </h3>
<h3>
    Function algorithms
<ul style="margin-bottom: 10px; font-weight: 300;">
        <li>bisection_root</li>
        <li>quadratic_roots</li>    
        <li>horner_evaluation</li>  
        <li>trapezoidal_integration</li>  
        <li>rectangular_integration</li> 
</ul>
    </h3>
<h3>
    Geometric algorithms
<ul style="margin-bottom: 10px; font-weight: 300;">
        <li>distane_between_points</li>
        <li>are_points_collinear</li>   
        <li>is_triangle_valid</li>   
        <li>is_triangle_rectangular</li>
</ul>
    </h3>

<h2 id="strings">Strings</h2>
<h3>
String analysis
<ul style="margin-bottom: 10px; font-weight: 300;">
        <li>is_anagram</li>
        <li>is_pangram</li>
        <li>is_palindrome</li>
        <li>is_subsequence</li>
        <li>count_substring_occurences</li>
        <li>contains_duplicates</li>
</ul>
    </h3>
<h3>
    String manipulation
<ul style="margin-bottom: 10px; font-weight: 300;">
        <li>reverse</li>
        <li>compress</li>
        <li>custom_join</li>
        <li>lower</li>
        <li>upper</li>
</ul>
    </h3>
<h3>
    Custom string sorting
<ul style="margin-bottom: 10px; font-weight: 300;">
        <li>sort_items</li>
        <li>compare_vowels_count</li>
        <li>compare_chars_sum</li>
</ul>
    </h3>
<h2 id="ciphers">Ciphers</h2>
<h3>
<ul style="margin-bottom: 10px; font-weight: 300;">
        <li>caesar_cipher</li>
        <li>vigenere_cipher</li>
        <li>morse_code</li>
</ul>
</h3>
<h2 id="sorting">Sorting</h2>
<h3>

<ul style="margin-bottom: 10px; font-weight: 300;">
        <li>quick_sort</li>
        <li>bubble_sort</li>
        <li>merge_sort</li>
        <li>selection_sort</li>
</ul>
</h3>

</div>
