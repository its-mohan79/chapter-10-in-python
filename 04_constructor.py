class employee:
    language = "python"  #this is a class attribute
    salary = 120000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")

    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")


    @staticmethod
    def greet():
        print("Good morning")

mohan = employee("mohan", 1300000, "javascript")

# mohan.name = "mohan"

print(mohan.name, mohan.salary, mohan.language)

#rohan = employee()




