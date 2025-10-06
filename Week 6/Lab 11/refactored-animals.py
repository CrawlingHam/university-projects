from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, address, email, phone_number):
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.name = name
    
    def __str__(self):
        return (f"{self.name} who lives in {self.address}.\nEmail: {self.email} and Phone: {self.phone_number}")

class Owner(Person):
    def __init__(self, name, address, email, phone_number):
        super().__init__(name, address, email, phone_number)

class Staff(Person):
    def __init__(self, name, id, department, salary, position, address, email, phone_number):
        super().__init__(name, address, email, phone_number)
        self.department = department
        self.position = position
        self.salary = salary
        self.id = id
    
    def work(self):
        print(f"{self.name} is working overtime in the {self.department} department.")

    def get_paid(self):
        print(f"{self.name} is getting paid {self.salary} for the work they did as {self.position}.")

    def clock_out(self):
        print(f"{self.name} is clocking out for the day.")

class Animal(ABC):
    def __init__(self, name, age, breed, owner):
        self.breed = breed
        self.owner = owner
        self.name = name
        self.age = age
    
    def sleep(self):
        print(f"{self.name} is sleeping quietly...")
    
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed, owner)
    
    def speak(self):
        print(f"{self.name} looks at you and barks: Woof Woof!")

class Cat(Animal):
    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed, owner)
    
    def speak(self):
        print(f"{self.name} looks at you, ignores you and keep doing what it was doing before.")

class Rabbit(Animal):
    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed, owner)
    
    def speak(self):
        print(f"{self.name} looks at you and runs away.")

class Rat(Animal):
    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed, owner)
    
    def speak(self):
        print(f"{self.name} looks at you and says: Squeak Squeak!")

def main():
    whiskers_owner = Owner("Whiskers Owner", "Gothenburg", "whiskersowner@unknown.com", "+46 702345678")
    requiem_owner = Owner("Requiem Owner", "Stockholm", "requiemowner@unknown.com", "+46 701234567")
    bidu_owner = Owner("Bidu Owner", "Linköping", "biduowner@unknown.com", "+46 705678901")
    max_owner = Owner("Max Owner", "Uppsala", "maxowner@unknown.com", "+46 704567890")
    tom_owner = Owner("Tom Owner", "Malmö", "tomowner@unknown.com", "+46 703456789")

    whiskers = Cat("Whiskers", 2, "Persian", whiskers_owner)
    tom = Cat("Tom", 3, "Siamese", tom_owner)
    max = Cat("Max", 1, "Tabby", max_owner)

    snowball = Rabbit("Snowball", 1, "Rabbit", None)
    dynamite = Rabbit("Dynamite", 1, "Rabbit", None)
    jack = Rabbit("Jack", 2, "Rabbit", None)
    toby = Rabbit("Toby", 2, "Rabbit", None)
    dash = Rabbit("Dash", 3, "Rabbit", None)

    rat1 = Rat("Rat1", 1, "Rat", None)
    rat2 = Rat("Rat2", 1, "Rat", None)

    requiem = Dog("Requiem", 1, "Golden Retriever", requiem_owner)
    bidu = Dog("Bidu", 3, "Mixed", bidu_owner)

    product_manager = Staff("John Doe", "jM4dw1-03n5dw", "Marketing", 120000, "Product Manager", "Stockholm", "john.doe@example.com", "+46 701234567")
    
    bidu.sleep()
    print()
    requiem.speak()
    print()
    
    whiskers.speak()
    print()
    tom.speak()
    print()
    max.speak()
    print()
    
    snowball.speak()
    print()
    dynamite.speak()
    print()
    jack.speak()
    print()
    toby.speak()
    print()
    dash.speak()
    print()

    rat1.speak()
    print()
    rat2.speak()
    print()

    product_manager.work()
    print()
    product_manager.clock_out()
    print()
    product_manager.get_paid()
    print()

if __name__ == "__main__":
    main()
