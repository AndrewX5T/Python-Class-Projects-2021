# Andrew Hein
# Advanced Programming - Week 8
# 2021/3/15
# emp_test.py

from emp import Employee

employees = [
    Employee("Susan Meyers", 47899, "Accounting", "Vice President"),
    Employee("Mark Jones", 39119, "IT", "Programmer"),
    Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
]

for num in range(0, len(employees)):
    print("Employee {}:\n{}\n".format(
        num + 1, employees[num]))
