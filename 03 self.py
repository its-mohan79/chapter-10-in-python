class employee:
    language = "py"  #this is a class attribute
    salary = 120000

    def getinfo(self):
        print(f" the language is {self.language}. the salary is {self.salary}")



mohan = employee()
mohan.language= "javascript"  #this is an instance attribute

mohan.getinfo()
#employee.getinfo(mohan)
