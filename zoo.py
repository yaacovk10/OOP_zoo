from enum import Enum


class Menu(Enum):
    ADD = 0
    PRINT = 1
    EXIT = 2

animal_list = []

def display_menu():
    for action in Menu:
        print(f"{action.name} - {action.value}")
    return (Menu(int(input("your selection : "))))

def menu():
    while (True):
        user_selection = display_menu()
        if user_selection == Menu.ADD: add_animal()
        if user_selection == Menu.EXIT: return

def insert_to_class():
    for item in animal_list:
        if item['predator']:
            item = Predator(item['name'])
            print(item.__str__)
        else:
            item = NonPredator(item['name'])
            print(f"{item.__str__}")

def add_animal():
    name = (input("Insert animal name: "))
    pred = (input("Is this animal predator (Y/N) : "))
    animal = {"name":name, "predator" : True if pred=='Y' else False}
    animal_list.append(animal)


class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def __str__(self):
        return f"{self.name}"
    
    def eat(self):
        print(f"{self.name} is eating")
    
class Predator(Animal):
    
    def __init__(self, name) -> None:
        super().__init__(name)
        self.strong = True
    
    def __str__(self):
        return f"{super().__str__()} is a {__class__.__name__}"

    

    
class NonPredator(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.strong = False
    def __str__(self):
        return f"{super().__str__()} is a {__class__.__name__}"
    

if __name__ == '__main__':
    # p1 = Predator("lion")
    # print(p1)

    # n2 = NonPredator("cheep")
    # print(n2)
    menu()
    insert_to_class()
    

    
    

    



