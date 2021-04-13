# Andrew Hein
# Advanced Programming - Week 8
# 2021/3/15
# emp.py

class Employee:
    def __init__(self, name, id, dept, title):
        self.id = id
        self.name = name
        self.department = dept
        self.jobTitle = title

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_department(self):
        return self.department

    def get_title(self):
        return self.jobTitle

    def __str__(self):
        return "Name: {name}\nID number: {id}\nDepartment: {dept}\nTitle: {title}".format(name=self.get_name(), id=self.get_id(), dept=self.get_department(), title=self.get_title())
