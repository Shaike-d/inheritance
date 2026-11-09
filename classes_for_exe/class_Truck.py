import classes_for_exe.class_Vehicle as v

class Truck(v.Vehicle):
    load_kg = 0

    def __init__(self,brand,max_weight):
        super().__init__(brand,6)
        self.max_weight = max_weight

    def load(self,weight):
        if (Truck.load_kg+weight) > self.max_weight:
            raise ValueError(f"overloaded: max {self.max_weight} kg")
        Truck.load_kg += weight



