# Andrew Hein
# Advanced Programming - Week 8
# 2021/3/15
# emp_sys_test.py

from emp import Employee
import pickle
import sys

# !! Input formats !!
# !! add firstname lastname id dept title
# !! change firstname lastname id dept title
# !! delete firstname lastname
# !! lookup firstname lastname


def mergeFullName(firstName, lastName):
    return f'{firstName} {lastName}'


def f_add(person, employee):
    if person in employees:
        print(f"Cannot add '{person}', already exists")
    else:
        employees[person] = employee
        print(f"Added employee:\n{employee}")


def change(person, employee):
    if person in employees:
        employees[person] = employee
        print(f"Changed employee '{person}' to\n{employee}")
    else:
        f_add(person, employee)


def f_delete(person):
    if person in employees:
        employees.pop(person)
        print(f"Deleted employee '{person}'")
    else:
        print(f"Cannot delete '{person}', does not exist")


def lookup(person):
    if person in employees:
        print(f"'{person}' found:\n{employees[person]}")
    else:
        print(f"Employee '{person}' is not found")


def serializeEmployees():
    outFile = open(readWritePath, "wb")
    pickle.dump(employees, outFile)
    outFile.close()


readWritePath = "employees.pickle"
employees = {}

input = sys.argv[1:]

try:
    # Try to open an existing file
    file = open(readWritePath, "rb")
    employees = pickle.load(file)
    file.close()
except FileNotFoundError:
    # We didn't find the file: initialize a new dictionary
    employees = dict()

# check for each possible command arg
if input[0].lower() == 'add':
    name = mergeFullName(input[1], input[2])
    emp = Employee(name, input[3], input[4], input[5])
    f_add(name, emp)

elif input[0].lower() == 'change':
    name = mergeFullName(input[1], input[2])
    emp = Employee(name, input[3], input[4], input[5])
    change(name, emp)

elif input[0].lower() == 'delete':
    name = mergeFullName(input[1], input[2])
    f_delete(name)

elif input[0].lower() == 'lookup':
    name = mergeFullName(input[1], input[2])
    lookup(name)

serializeEmployees()
