class  Human:
    def __init__(self, name, age, gender) -> None:
        self. name = name
        self.age =  age
        self.gender = gender

    def speak(self):
        print("I am speaking")

class Student(Human):
    def __init__(self, name, age, gender, studies) -> None:
        super().__init__(name, age, gender)
        self.studies = studies

    def __str__(self):
        return "I am learning"
    

class Worker(Human):
    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age, gender)
        self.work = True
    
    
    def job_description(self):
        return "Stam"
    

class Simple(Worker):
    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age, gender)
        self.job = "simple worker"
    
    def job_description(self):
        return "hard"

class Manager(Worker):
    def __init__(self):
        self.job = "manager"


    def job_description(self):
        return "sababa"



if __name__ == '__main__':
    s1 = Simple("yaacov", "41", "Man")
    print(s1.job_description())
    print(f"age: {s1.age}")
    m2 =Manager()
    print(m2.job_description())

    stud1 = Student("math")

