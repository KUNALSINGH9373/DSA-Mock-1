#!/usr/bin/env python
# coding: utf-8

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# 
# Example 1:
# Input: s = "leetcode"
# Output: 0
# 
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# 
# Example 3:
# Input: s = "aabb"
# Output: -1
# 
# Constraints:
# a. 1 <= s.length <= 10^5
# b. s consists of only lowercase English letters.

# In[1]:


def firstUniqChar(s):
    char_count = {}
    
    # Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the index of the first non-repeating character
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i
    
    return -1

# Test the function with the provided examples
s1 = "leetcode"
print(firstUniqChar(s1))  # Output: 0

s2 = "loveleetcode"
print(firstUniqChar(s2))  # Output: 2

s3 = "aabb"
print(firstUniqChar(s3))  # Output: -1


# The above solution uses a dictionary char_count to count the occurrences of each character in the string s. It then iterates through the string and checks the count of each character. The first character with a count of 1 is considered the first non-repeating character, and its index is returned. If no non-repeating character is found, -1 is returned.

# In[ ]:




