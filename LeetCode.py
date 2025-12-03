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

