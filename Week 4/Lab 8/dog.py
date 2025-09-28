# Define a class for Dogs:
class Dog:
    # Defines the attributes (properties dogs have) and initializes them:
    # (Attributes are variables that belong to a given class)
    def __init__(self, name, age, breed, adress):
        self.name = name
        self.age = age
        self.breed = breed
        self.adress = adress
    
    # Method example:
    def bark(self):
        print(f"{self.name} looks at you and barks: Woof Woof!")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def barkAt(self, other_dog_name):
        print(f"{self.name} looks at {other_dog_name} and barks: Woof Woof!")


#Create an object from Class Dog:
dog1 = Dog("Bidu", 1, "Mixed", "United Kingdom")

#Create another object from Class Dog:
dog2 = Dog("Pipoca", 5, "German Sheperd", "Germany")

dog3 = Dog("Requiem", 10, "Golden Retriever", "United States")

dog1.bark()
dog1.sleep()
dog1.barkAt(dog2.name)
print(dog1.bark())