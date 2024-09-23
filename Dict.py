# What is a Dictionary in Python?
# Explanation:
# A dictionary in Python is an unordered, mutable collection of key-value pairs. Unlike lists, which are indexed by position, dictionaries are indexed by keys. Keys must be unique and immutable, while values can be of any data type.
# Syntax of a dictionary
dictionary_name = {
    "key1": "value1",
    "key2": "value2"
}
# 1) Creating Dictionaries
# Code Example:
# Creating an empty dictionary
empty_dict = {}

# Creating a dictionary with key-value pairs
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}
# Printing the dictionary
print(student)  # Output: {'name': 'Alice', 'age': 22, 'major': 'Computer Science'}

# 2) Accessing Dictionary Values
# Explanation:
# You can access dictionary values by referencing their keys inside square brackets [].
# Code Example:
# # Accessing dictionary values
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}
# Accessing values using keys
print(student["name"])  # Output: Alice
print(student["age"])   # Output: 22

# 3) Adding, Updating, and Removing Key-Value Pairs
# Code Example:

#Adding a new key-value pair
student = {
    "name": "Alice",
    "age": 22
}
student["major"] = "Computer Science"
print(student)  # Output: {'name': 'Alice', 'age': 22, 'major': 'Computer Science'}

# Updating an existing key-value pair
student["age"] = 23
print(student)  # Output: {'name': 'Alice', 'age': 23, 'major': 'Computer Science'}

# Removing a key-value pair using del
del student["age"]
print(student)  # Output: {'name': 'Alice', 'major': 'Computer Science'}


# 4) Common Dictionary Methods
# Explanation:
# Here are some common dictionary methods:

# keys(): Returns all the keys in the dictionary.
# values(): Returns all the values in the dictionary.
# items(): Returns all key-value pairs as tuples.
# get(key): Safely gets a value for a key, returns None if the key doesn’t exist.
# pop(key): Removes the key-value pair and returns its value.
# Code Example:
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}

# Getting all keys
print(student.keys())  # Output: dict_keys(['name', 'age', 'major'])

# Getting all values
print(student.values())  # Output: dict_values(['Alice', 22, 'Computer Science'])

# Getting all key-value pairs
print(student.items())  # Output: dict_items([('name', 'Alice'), ('age', 22), ('major', 'Computer Science')])

# Using get() method to safely access a value
print(student.get("name"))  # Output: Alice
print(student.get("GPA", "Not Available"))  # Output: Not Available

# 5) Looping Through a Dictionary
# Explanation:
# You can loop through a dictionary in several ways:
#
# Loop through keys.
# Loop through values.
# Loop through both keys and values (using items()).
# Code Example:
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}

# Looping through keys
for key in student:
    print(key)

# Looping through values
for value in student.values():
    print(value)

# Looping through both keys and values
for key, value in student.items():
    print(f"{key}: {value}")

# 6) Nested Dictionaries
# Explanation:
# A dictionary can contain another dictionary as a value. This allows for more complex data structures, similar to JSON objects.
# Code Example:

# Nested dictionary example
students = {
    "student1": {
        "name": "Alice",
        "age": 22
    },
    "student2": {
        "name": "Bob",
        "age": 23
    }
}

# Accessing a nested dictionary
print(students["student1"]["name"])  # Output: Alice

# 7) Dictionary Comprehension
# Explanation:
# Like list comprehensions, Python supports dictionary comprehensions to create dictionaries dynamically.
# Code Example:

# Create a dictionary of squares using dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    
# Summary:
# Creating Dictionaries: Initialize dictionaries with key-value pairs.
# Accessing Dictionary Values: Use keys to access dictionary values.
# Adding, Updating, and Removing: Modify dictionaries by adding, updating, or deleting key-value pairs.
# Dictionary Methods: Use methods like keys(), values(), items(), and get().
# Looping: Iterate over keys, values, or key-value pairs in a dictionary.
# Nested Dictionaries: Use dictionaries inside dictionaries for complex data structures.
# Dictionary Comprehension: Use comprehensions to create dictionaries dynamically.


