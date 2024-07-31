# 15: Write a Python module named file_operations.py
# file_operations.py

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

write_to_file("data.txt", "Hello, world!")
append_to_file("data.txt", "Appending new line")
print(read_file("data.txt"))
