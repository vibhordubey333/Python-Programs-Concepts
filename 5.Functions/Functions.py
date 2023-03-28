# Function without arguments
def Function():
    print("Normal function.")
Function()

#Function with arguements
def FunctionWithArguments(args_1,args_2):
    print("Function With Argument:  Args-1",args_1," Args-2",args_2)
FunctionWithArguments("Hello",3)

#Default arguements: A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument. The following example gives an idea on default arguments, it prints default age if it is not passed −
def DefaultFunctions(name,age = 35):
    print("Functions:",name,age)    

DefaultFunctions(name="Sita Ram")
DefaultFunctions(age = 50, name = "Hare Ram")

# Variable arguements: When not aware how many arguements will be incoming.
def VariadicFunctions(*arg):
    print("Variadic Functions:")
    for a in arg:
        print(a)
    #print("Variadic Functions: Elements at index 2 is:"+args[2])

VariadicFunctions('A','B','C')

