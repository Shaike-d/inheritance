# import classes_for_mini_project.__init__ as c
import classes_for_mini_project.class_Intern as i
import classes_for_mini_project.class_Manager as m
import classes_for_mini_project.class_Employee as e


def main():
    staff = [e.Employee("Dana", 12000),
            m.Manager("Avi", 20000, 3000),
            i.Intern("Noa", 6000, 6),
            ]
    for person in staff:
        print(person.describe())
    try:
        i.Intern("Tom", 5000, 0)
    except ValueError as error:
        print("error:", error)
    total = 0
    for person in staff:
        total = total + person.monthly_cost()
    print("Total monthly cost:", total)









if __name__ == "__main__":
    main()