def transform_text(txt):
    vowel_map = {
        'a': 'i',
        'e': 'o',
        'i': 'u',
        'o': 'a',
        'u': 'e'
    }

    def transform_word(word):
        return ''.join(vowel_map.get(char, char) for char in word)

    words = txt.split()
    transformed_words = [transform_word(word) for word in words]
    return ' '.join(transformed_words)

# Example usage:
# txt = "animals occupdi villages are very important for the ecosystem"
# result = transform_text(txt)
# print(result)
def Human(txt):
    vowel_map = {
            'a': 'i',
            'e': 'o',
            'i': 'u',
            'o': 'a',
            'u': 'e'
        }
    out = []
    for i in txt:
        var = vowel_map.get(i, i)
        out.append(var)

    print(''.join(out))
# Human(txt)

def buble_sort(lstt):
    
    for i in range(0,len(lstt) -1):
        for j in range(0, len(lstt) -i - 1):
            if lstt[j] > lstt[j + 1]:
                lstt[j], lstt[j + 1] = lstt[j + 1], lstt[j]
    print(lstt)

# lstt = [12, 23, 1, 43, 21]
# buble_sort(lstt)


# import re

# def using_re(txt):
#     pattern ='\d{9}'
#     pattern = '\((\d{3})\)-(\d{3})-(\d{4})'

#     var = re.findall(pattern, txt)
#     print(var)

# txt1 = """Hello my Number is 123456789 and my friend's number is 987654321 our us number is (123)-456-7890"""
# using_re(txt1)


# secound largest number 
def sec_large():
    var = [21,23,1,43,42]
    fir = sec = float("-inf")
    for i in var:
        if i > fir:
            sec = fir
            sec = i
        elif fir > i > sec:
            sec = i
    return sec


"""
Palindrome Check: Write a function is_palindrome(s) that returns True if string s reads
the same forwards and backwards, ignoring case and non-alphabetic characters. 
Example: is_palindrome("A man a plan a canal Panama") → True
"""

def Palindrome(inputvariable):

    strvar = "".join(i for i in inputvariable.lower() if i.isalpha())
    return strvar == strvar[::-1]

# print(Palindrome("A man a plan a canal Panama"))


"""
Factorial Calculation: Implement factorial(n) using recursion or iteration to compute n! for non-negative integer n. 
Example: factorial(5) → 120.
"""
def factorial(n):
    if n == 0 or n ==1:
        return 1
    return n * factorial(n-1)

# print(factorial(5))


"""
Vowel Counter: Create count_vowels(s) to return the number of vowels (a,e,i,o,u) in string s, case-insensitive.
 Example: count_vowels("Hello World")
"""

def vowel_counter(inputString):
    vowel = "aeiou"

    return sum( 1 for coun in inputString if coun.lower() in vowel)

# print(vowel_counter("Hello World"))


"""
Even/Odd Checker: Define is_even(num) returning True if num is even. Example: is_even(4) 
"""
# def EvenOdd(num):
#     return f"{num} is even number " if num % 2 == 0 else f"{num} is odd number"

EvenOdd = lambda num : f"{num} is even number " if num % 2 == 0 else f"{num} is odd number"
# print(EvenOdd(10))


"""
Max of Three: Write max_of_three(a, b, c) returning the largest value. Example: max_of_three(1, 2, 3) → 3.​
"""
max_thre = lambda maxx : max(maxx)
# num_var23 = [1,3,4,8,9]
# print(max_thre(num_var23))

def max_three(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    return c
   
# print(max_three(8,9, 2))

"""
# Compute sum of all elements in a list without built-in sum(). 
# Example: [1,2,3] → 6.
"""
# from functools import reduce
# val =[1,2,3]
# var = reduce(lambda x, y : x + y, val)

def countss(val):
    counter =  val[0]
    for i in range(0, len(val) -1):
        counter += val[i+1]
    return counter
    
# val =[4,2,3,1]
# print(countss(val))


"""
Reverse Array: Reverse a list in place without slicing. 
Example: [1,2,3] → [3,2,1].
"""

def without_splicing(var):
    new_List= []
    for i in range(len(var)):
        new_List.insert(0, var[i])
    return new_List
    
# inn = [1, 2, 3, 4]   
# print(inn[::-1])   
# print(without_splicing(inn))

"""
# Character Frequency: Count occurrences of each character in a string using dict. 
# Example: "hello" → {'h':1, 'e':1, 'l':2, 'o':1}
"""
instr = "Hello"
vav = { j : instr.count(j) for i, j in enumerate(instr)}
# print(vav)


"""
Second Largest: Find second largest number in an array. Handle duplicates and edge cases.
"""

def SecLarge(lst_var):
    for i in range(0, len(lst_var) - 1):
        for j in range(0, len(lst_var) -i - 1):
            if lst_var[j] < lst_var[j + 1]:
                lst_var[j] , lst_var[j + 1] =  lst_var[j + 1], lst_var[j]
    return lst_var

# lst_var = [34,84,2,3,4,5,89,32]
# print(SecLarge(lst_var)[1])

"""
decorator
"""

def outter(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception  as e:
            print(f"getting Error form this function {func.__name__} \n Error {e}")
    return inner

@outter
def main(aurg):
    raise "aurg error"

main("Hello")