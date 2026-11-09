import classes_for_exe.class_Employee as e


class Manager(e.Employee):

    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus
        self.salary = salary + bonus
        

    def manage(self,team_members):
        return f"{self.name} manages {team_members} people"



