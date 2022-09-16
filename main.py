class Kitty:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def meow(self):
        print("meow")

    def eat(self, food, weight_of_food):
        self.weight+=weight_of_food/10
        print(f"I have eaten {weight_of_food} of {food}")
        print(f"My weight is {self.weight}")

    def run(self, distance):
        if self.weight<2:
            print("I am starving, I can't run")
        else:
            self.weight-=distance/10
            if self.weight<0:
                print("Starved to death")