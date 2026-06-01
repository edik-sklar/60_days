# DAY 1: MORNING ROUTINE (30 min)
# Instructions only - write the code yourself!

# ============================================
# EXERCISE 1: List comprehension
# ============================================
# Create a list of squares for all EVEN numbers from 0 to 20 (inclusive)
# Expected output: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

even_squares = [int(i) ** 2 for i in range(21) if int(i) // 2 == 0 ]
print(even_squares)


# ============================================
# EXERCISE 2: Dictionary comprehension
# ============================================
# Create a dictionary where keys are numbers 1-10 and values are their squares
# Expected output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

num_squares = [{i:i ** 2} for i in range(1, 11)]
print(num_squares)



# ============================================
# EXERCISE 3: enumerate()
# ============================================
# Given the list below, print each fruit with its index
# Expected output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry

fruits = ['apple', 'banana', 'cherry']

for i, v in enumerate(fruits):
    print(f" Index {i}: {v}")

# ============================================
# EXERCISE 4: zip()
# ============================================
# Combine two lists using zip() and print paired elements
# Expected output should show: apple-1, banana-2, cherry-3

fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3]

my_list = list(zip(fruits, numbers))
print(my_list)

# ============================================
# EXERCISE 5: List slicing
# ============================================
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 5a: Reverse the list (print it)

reversed_list = list.reverse(my_list)
# reversed_list = my_list.reverse()
print("my_list after reverse():", my_list)
print("Reversed:", reversed_list)

my_list = [1, 2, 3, 4, 5]
reversed_iterator = reversed(my_list)
reversed_list = list(reversed_iterator)
print(reversed_list) # Output: [5, 4, 3, 2, 1]
print(my_list)      # Output: [1, 2, 3, 4, 5] (original list remains unchanged)

my_string = "hello"
reversed_string = "".join(reversed(my_string))
print(reversed_string) # Output: olleh

# 5b: Get every other element starting from 0 (print it)
every_other = my_list[::2]
print("Every other:", every_other)

# 5c: Get the last 3 elements (print it)
last_three = my_list[-1: -4]
print("Last 3:", last_three)