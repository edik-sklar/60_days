```
LC 704 — Binary Search
Given a sorted array nums and a target, return the index of target or -1 if not found.
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1

def bin(nums, target):
l, r = 0, len(nums) - 1
mid = r-l//2
while l<= r:

```