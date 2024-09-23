# 1) Creating Lists
# # # # Explanation:
# # # # A list in Python is an ordered, mutable collection of items. Lists can hold different types of data, such as integers, strings, and even other lists.
# # # #
# # # # Code Example:
# Creating lists with different types of data
empty_list = []  # Empty list
numbers = [1, 2, 3, 4, 5]  # List of integers
fruits = ['apple', 'banana', 'cherry']  # List of strings
mixed = [1, "hello", 3.14, True]  # List with mixed data types

print(numbers)  # Output: [1, 2, 3, 4, 5]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(mixed)  # Output: [1, 'hello', 3.14, True]

#
# 2) Indexing and Slicing Lists
# Explanation:
# Indexing allows you to access individual elements in a list. Indexing starts at 0 for the first element.
# Slicing allows you to extract a portion (slice) of the list. You can define a start and an end index.
# Code Example:
# Accessing elements using indexing
fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits[0])  # Output: 'apple'
print(fruits[2])  # Output: 'cherry'

# Negative indexing
print(fruits[-1])  # Output: 'date'

# Slicing a list
print(fruits[1:3])  # Output: ['banana', 'cherry']
print(fruits[:2])  # Output: ['apple', 'banana']
print(fruits[2:])  # Output: ['cherry', 'date']

# 3) Basic List Methods
# Explanation:
# Lists come with several useful methods for manipulating data, such as append(), remove(), and sort().
# Code Example:
# Append an element to a list
fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Remove an element from a list
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry', 'date']

# Sorting a list
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]

# Reversing a list
numbers.reverse()
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]

# 4) Nesting Lists
# Explanation:
# A list can contain other lists as elements, which creates a nested list. These are useful for storing data in a structured way.
# Code Example:
# Creating a nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements from a nested list
print(matrix[0])  # Output: [1, 2, 3]
print(matrix[1][2])  # Output: 6

# 5) Introduction to List Comprehensions
# Explanation:
# List comprehensions provide a concise way to create lists. They consist of brackets containing an expression followed by a for loop, and optionally, conditions.
# Code Example:
# Creating a list of squares using a for loop
squares = []
for x in range(1, 6):
    squares.append(x**2)
print(squares)  # Output: [1, 4, 9, 16, 25]

# Creating a list of squares using list comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# List comprehension with a condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
# Summary:
# Creating Lists: Define lists with various data types.
# Indexing and Slicing: Access individual elements and slices of a list.
# Basic List Methods: Use list methods like append(), remove(), sort(), and reverse().
# Nesting Lists: Create lists inside other lists.
# List Comprehensions: Generate lists concisely using expressions and loops.