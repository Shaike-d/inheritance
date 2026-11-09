import classes_for_exe.class_Animal as a


class Dog(a.Animal):

    def fetch(self):
        return f"{self.name} brings back the ball"

