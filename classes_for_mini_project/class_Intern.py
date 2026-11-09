import classes_for_mini_project.class_Employee as e

class Intern(e.Employee):

    def __init__(self,name,salary,months):
        super().__init__(name,salary)
        if 1 > months or months > 12:
            raise ValueError("months must be 1-12")
        self.months = months

    def title(self):
        return "Intern"
