#!/usr/bin/env python
# coding: utf-8

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# Constraints:
# a. 1 <= nums.length <= 10^4
# b. -2^31 <= nums[i] <= 2^31 - 1
# 
# 

# In[1]:


def moveZeroes(nums):
    n = len(nums)
    zero_count = 0  # Count of zeros encountered

    # Iterate through the array and move non-zero elements to the left
    for i in range(n):
        if nums[i] != 0:
            nums[i - zero_count] = nums[i]
        else:
            zero_count += 1

    # Fill the remaining elements with zeros
    for i in range(n - zero_count, n):
        nums[i] = 0

# Test the function with the provided examples
nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
moveZeroes(nums2)
print(nums2)  # Output: [0]


# The above solution uses two pointers to keep track of the non-zero elements and the count of zeros encountered. It iterates through the array, moving non-zero elements to the left while incrementing the count of zeros. Finally, it fills the remaining elements with zeros.

# In[ ]:





# In[ ]:




