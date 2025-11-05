class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def hunt(self):
        print(f"{self.name} the {self.breed} pounces on a laser pointer")

    def knock_off(self, item):
        print(f"{self.name} the {self.breed} casually knocks the {item} off the table")

cat1 = Cat("Garfield", "tabby")
cat2 = Cat("Whiskers", "Persian")
cat3 = Cat("Luna", "Siamese")
cat4 = Cat("Shadow", "Maine Coon")
cat5 = Cat("Mittens", "Ragdoll")

cat1.hunt()
cat1.knock_off("vase")

cat2.knock_off("coffee mug")
cat2.hunt()

cat3.hunt()
cat3.knock_off("laptop")

cat4.knock_off("phone")
cat4.hunt()


cat5.hunt()
cat5.knock_off("tablet")