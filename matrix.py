# LC 74 — Search a 2D Matrix
# You're given an m x n matrix where each row is sorted left to right, and the first element of each row is greater than the last element of the previous row. Given a target, return True if it exists in the matrix, False otherwise.
def bin_matrix(matrix, target):
    l = 0
    cu = len(matrix[0])
    ro = len(matrix)
    r = len(matrix[0]) * len(matrix) - 1
    while l <= r:
        mid = (l + r) // 2
        if matrix[mid//cu][mid%cu] == target:
            return True
        elif matrix[mid//cu][mid%cu] < target:
            l = mid + 1
        else:
            r = mid -1
    return False

# brute force, O(mn) instead of O(log(mn))
def two_d_matrix(matrix, target):
    return target in [x for row in matrix for x in row]

# Input:
matrix = [
  [1,  3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
target1 = 3
# Output: True

target2 = 13
# Output: False

print(bin_matrix(matrix,target1))
print(bin_matrix(matrix,target2))

# LC 33 — Search in Rotated Sorted ArrayLC 33 — Search in Rotated Sorted Array
# A sorted array was rotated at some pivot. You don't know where. Find the target and return its index, or -1.

def rotated_list(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        # sorted on the left
        elif nums[l] < nums[mid]:
            # search on the left
            if target < nums[mid]:
                r = mid -1
            else:
                l = mid + 1
        # sorted on the right:
        else:
            # search on the left
            if target < nums[mid]:
                r = mid -1
            # search on the right
            else:
                l = mid + 1
    return -1




# Input:
nums = [4,5,6,7,0,1,2]
target = 0
# Output: 4

# Input:
nums = [4,5,6,7,0,1,2]
target = 3
# Output: -1


# Next: LC 74 — Search a 2D Matrix
# Each row is sorted left to right.
# Last element of each row < first element of next row.
# Find target, return True/False.

# Hint:
# treat the whole matrix as one flat sorted array.
# m rows × n cols = m*n elements.
# Binary search on indices 0 to m*n - 1.
# To convert a flat index mid back to row/col:
# row = mid // n, col = mid % n.

def matrix_bin_search(m, t):
    l, rows, cols = 0, len(matrix), len(matrix[0])
    r = rows * cols - 1
    while l <= r:
        mid = (l+ r)//2
        row = mid // cols
        col = mid % cols
        if target == matrix[row][col]:
            return (row, col)
        elif target < matrix[row][col]:
            r = mid - 1
        else:
            l = mid + 1
    return -1



matrix = [
  [1,  3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
target = 3
# →  True

print(matrix_bin_search(matrix,target))