def find_target_bin(nums, target):
    l = 0
    r = len(nums) -1
    while l <= r:
        mid = (r+l) // 2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            r = mid -1
        else :
            l = mid + 1
    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(find_target_bin(nums,target))
