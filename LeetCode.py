"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

def reversre():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    num1 = 0
    num2 = 0
    addedValue = 0
    for d in l1[::-1]:
        num1 = num1 * 10 + d 
        
    for j in reversed(l2):
        num2 = num2 * 10 + j 
    
    addedValue = num1 + num2
    output = []
    for i in str(addedValue):
        output.insert(0, int(i))
        
    return output

# bb =  reversre()
# print(bb)
    
"""
Given a string s, find the length of the longest substring without duplicate characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length, char_set



# sst = "abcabcbb"
# print(lengthOfLongestSubstring(sst))

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
def sorrrter(nums1, nums2):
    new = nums1 + nums2
    new.sort()
    if len(new) % 2 == 0 :
        idx = len(new) // 2
        return (new[idx-1] + new[idx]) / 2
    elif len(new) % 2 == 1 :
        idx = (len(new) + 1)// 2
        return new[idx-1]
    
    
nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10,11,12,13,14,15]
# print(sorrrter(nums1, nums2))


"""
Longest Palindromic Substring
Attempted
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""


def palindorm(lsst):
    var = {}
    for i in range(0, len(lsst)):
        for j in range(0, len(lsst)+1):
            print(lsst[i:j])
            if lsst[i:j] == lsst[i:j][::-1] and len(lsst[i:j]) > 1 :
                var.update({len(lsst[i:j]) : lsst[i:j]})

    pp = { i for i, val in var.items()}

    return var.get(max(pp)) if pp else lsst[0]

# ll = "ac"
# print(palindorm(ll))


"""
Reverse Integer
Topics
premium lock icon
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""

x = -1533463745348

def reverint(x):
    var = ""
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    if x > 0:
        var = int(str(x)[::-1])
        if int(var) < INT_MIN or int(var) > INT_MAX:
            return 0
    else:
        var = int("-" + str(abs(x))[::-1])
        
    if int(var) < INT_MIN or int(var) > INT_MAX:
        return 0
    
    return int(var)
    
# print(int(reverint(x)))


"""
Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
"""
def isPalindrome(x: int) -> bool:
        x = str(x)
        return True if x == x[::-1] and x[0] not in ["+", "-"] else False

"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
"""

def myAtoi(s: str) -> int:
        
        fun = ""
        idx = 0
        s = s.strip()
        if not s:
            return 0
        result = 0
        if s[0] in ["+", "-"]:
            fun += s[0]
            idx += 1
        
        if s[0].isalpha():
            return 0

        while idx < len(s) and s[idx].isnumeric():
            result = result * 10 + int(s[idx])
            idx += 1

        result = int(fun + str(result)) 
    #  checking 32 Bit or not  
        mini , maxi = -2**31, 2**31 - 1

        if result > maxi:  
            return maxi
        if result < mini:  
            return mini
        
        return int(result)

"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
"""

import re

def isMatch(self, s: str, p: str) -> bool:
        pat = f"^{p}$"
        return bool(re.match(pat, s))





    