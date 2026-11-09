import classes_for_mini_project.class_Employee as e



class Manager(e.Employee):

    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.salary =  self.salary + bonus

    def title(self):
        return "Manager"

    def monthly_cost(self):
        return self.salary

    
