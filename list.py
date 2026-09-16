#A list in Python is a collection used to store multiple values in a single variable.

#1. Creating a list
numbers = [10, 20, 30, 40, 50]
print(numbers)

# A list can contain different data types:
mixed_list = [10, "Hello", 3.14, True]
print(mixed_list)

#2. Lists are ordered and indexed
#Python list indexing starts from 0:
numbers = [10, 20, 30, 40, 50]
print(numbers[0])  # 10
print(numbers[2])  # 30
print(numbers[4])  # 50

#3. Lists are mutable
#Mutable means you can change the values after creating the list.
numbers = [10, 20, 30]
numbers[1] = 25
print(numbers)

#4. Adding elements
#append()
#Adds one element to the end:
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

#insert()
#Adds an element at a specific position:
numbers.insert(1, 15)
print(numbers)

#5. Removing elements
numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)

#You can also use pop(): This removes the last element.
numbers.pop()
print(numbers)

#6. Loop through a list
employees = ["John", "David", "Smith"]
for emp in employees:
    print(emp)

#7. List with duplicate values
#Lists allow duplicates:
numbers = [10, 20, 20, 30, 30, 30]
print(numbers)