class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def monthly_cost(self):
        return self.salary

    def describe(self):
        return f"{self.name}: {self.salary}"




