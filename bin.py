# LC 704 — Binary Search
# Given a sorted array nums and a target, return the index of target or -1 if not found.
from codecs import make_identity_dict


def bin(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (r - l) // 2 + l
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

# Input:
nums1 = [-1,0,3,5,9,12]
target1 = 9
# Output: 4

# Input:
nums2 = [-1,0,3,5,9,12]
target2 = 2
# Output: -1
print(bin(nums1,target1))
print(bin(nums2,target2))


def slide_bin(nums, t):
    l, r = 0, len(nums) -1
    while l <= r:
        mid = (l + r)//2
        if t == nums[mid]:
            return True
        # first half is sorted
        elif nums[l] < nums[mid]:
            if nums[l] <= t < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # second half is sorted
        else:
            if nums[mid] < t <= nums[r]:
                l = mid + 1
            else:
                r = mid -1
    return False


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(slide_bin(nums,target))

 # LC 153 — Find Minimum in Rotated Sorted ArrayLC 153 — Find Minimum in Rotated Sorted Array
# Given a rotated sorted array, find the minimum element.
# Hint: the minimum is always at the rotation point — where the array "drops".
# If nums[mid] > nums[r], the drop is in the right half.
# Otherwise it's in the left half (or mid itself).

def min_bin(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        # first half is sorted
        if nums[mid] < nums[r]:
            r = mid
        else:
            l = mid + 1
    return nums[l]


print(min_bin([3, 4, 5, 1, 2]))
# [3, 4, 5, 1, 2] → 1


def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) -1
    while l <= r:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        elif nums[l] < nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[r] >= target > nums[mid]:
                l = mid + 1
            else:
                r = mid -1
    return -1

