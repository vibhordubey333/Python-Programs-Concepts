#Default arguements: A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument. The following example gives an idea on default arguments, it prints default age if it is not passed −
def DefaultFunctions(name,age = 35):
    print("Functions:",name,age)    

DefaultFunctions(name="Sita Ram")
DefaultFunctions(age = 50, name = "Hare Ram")

