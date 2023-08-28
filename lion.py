class Lion:
    def __init__(self, age, sex="male") -> None:
        self.age = age
        self.sex  = sex
        pass



    def __str__(self) -> str:
        return f"this is a Lion object from Lion class, age : {self.age}, sex = {self.sex}"

    def cry(self):
        print(f"Lion cry")
    
    def eat(self):
        print ( f"Lion eat")


class Fish:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight
        
    
    def __str__(self) -> str:
        print(self.__class__)
        return f"This is a {self.name} with weight {self.weight}"
    
    def swim(self):
        print ("fish swim")
    
    def eat(self):
        print ("fish eat")

    

if __name__ == '__main__':
    l1= Lion(5)
    print(l1)
    l1.cry()
    l1.eat()

    f1 = Fish("Salmon", "3kg")
    print(f1)
    f1.eat()
    f1.swim()
