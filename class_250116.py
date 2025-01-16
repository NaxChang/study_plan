class Father:
    def say(self):
        print("yes")


class Mother:
    def say(self):
        print("no")


class Child(Mother, Father):
    pass


child = Child()
child.say()
