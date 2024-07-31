# 14: Implement a Python module named string_utils.py
# string_utils.py

def reverse_string(input_string):
    return input_string[::-1]

def capitalize_string(input_string):
    return input_string.capitalize()


print(reverse_string("hello"))
print(capitalize_string("world"))
