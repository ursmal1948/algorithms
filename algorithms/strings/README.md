# 📝 STRINGS PACKAGE 📝
## Overview
<font size="+1">
This package provides a collection of functions for working with strings.


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
Once installed, you can import the ciphers package and utilize its functionalities in Python projects 
</font>

## Strings Analysis
<font size="+1">
This package contains a set of versatile functions for string analysis. These functions cover serve as 
useful tools for various text analysis tasks such as checking for anagrams or palindromes or detecting
duplicate elements in a list. <br>
Here's how you can use it:
<br>
  
```
from algorithms.strings import string_analysis
```
#### Checking for anagram
```
anagram = string_analysis.is_anagram("meat","team")
print(f'Result: {anagram}') # True
```
#### Checking for pangram
```
pangram = string_analysis.is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(f'Result: {pangram}') # True
```
#### Checking for palindrome
```
palindrome = string_analysis.is_palindrome("KAYAK")
print(f'Palindrome: {palindrome}') # True
```  
#### Checking for potential palindrome
```
potential_palindrome = string_analyis.is_potential_palindrome("AABBCC")
print(f'Potential alindrome: {potential_palindrome}') # True
```
#### Checking for subsequence
```
text = "WORLD"
subsequence = "OD"
result = string_analyis.is_subsequence(text,subsequence)
print(f'Result : {result}') # True
```
#### Checking for substring
```
text = "WORLD"
substring = "ORL"
result = string_analyis.is_substring(text,substring)
print(f'Result : {result}') # True
```

#### Count of substring occurences
```
text = "PAPAYA"
substring = "PA"
result = string_analyis.count_substring_occurences(text,substring)
print(f'Count of substring occurences : {result}') # 2
```
#### Checking for duplicates
```
items = ["apple","banana","grapes","apple"]
result = string_analyis.contains_duplicates(items)
print(f'Items collection contains duplicates : {result}') # True
```
</font>

