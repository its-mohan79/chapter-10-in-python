class employee:
    language = "py"  #this is a class attribute
    salary =120000


mohan = employee()
mohan.name = "mohan"  #this is an instance attribute
print(mohan.name, mohan.language, mohan.salary)


rohan = employee()
rohan.name = "rohan roro robison"
print(rohan.name, rohan.salary, rohan.language)


#here name is instance attribute and salary and language
#attributes as they directly belong to the class
