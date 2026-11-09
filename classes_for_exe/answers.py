import classes_for_exe.class_Manager as m
import classes_for_exe.class_Employee as e
import classes_for_exe.class_Dog as d
import classes_for_exe.class_Cat as c
import classes_for_exe.class_Truck as t




def answers():
    for i in range(6):
        if i ==0:
            print("wellcome")
        if i == 1:
            print("answer 1")
            dana = e.Employee("Dana", 12000)
            avi = m.Manager("Avi", 20000,0)
            print(dana.describe())
            print(avi.describe())
            print(avi.manage(5))
        if i == 2:
            print("answer 2")
            print("dog is a animal")
            print("car contains an engine")
            print("SavingAcount is parallel to BankAcount")
            print("There is no connection between a square and a color.")
        if i == 3:
            print("answer 3")
            rex = d.Dog("Rex", 4)
            mitzi = c.Cat("Mitzi", 5)
            print(rex.describe(), "|", rex.fetch())
            print(mitzi.describe(), "|", mitzi.climb())
        if i == 4:
            print("answer 4")
            truck = t.Truck("Volvo", 1000)
            truck.load(600)
            print(truck.brand, truck.wheels, truck.load_kg)
            try:
                truck.load(500)
            except ValueError as error:
                print("error:", error)
        if i == 5:
            print("answer 5")
            print(e.Employee("Dana", 12000).monthly_cost())
            print(m.Manager("Avi", 20000, 3000).monthly_cost())


