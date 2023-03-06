#### Python - Data Types  
# Python has various built-in data types which we will discuss with in this tutorial:
#   - Numeric - int, float, complex
#       - int (signed integers)
#       - long (long integers, they can also be represented in octal and hexadecimal)
#       - float (floating point real values)
#       - complex (complex numbers)
#   - String - str
#   - Sequence - list, tuple, range
#   - Binary - bytes, bytearray, memoryview
#   - Mapping - dict
#   - Boolean - bool
#   - Set - set, frozenset
#   - None - NoneType
def IntegerTypes():
    a = 10
    b = 11
    print("IntegerTypes:",a,b)
    return a,b
print("IntegerTypes",IntegerTypes())

def StringTypes():
    str = "Jupiter"
    str2 = "Mars"
    print("StringTypes:",str[:1]) # J
    print("StringTypes: Multiply String:",str2*3) #MarsMarsMars
    print("StringTypes: ",str+" TEST") # Jupiter TEST
print(StringTypes())

def ListTypes():
    listObject = ['A',343,4.56,50.5]
    tinyListObject = ["Abracadabra","Haku-Na-Matata"]
    print("ListObject",listObject)
    print("TinyListObject:",tinyListObject)
    print("ListObject[0]",listObject[0])
    print("ListObject[1:3]",listObject[1:3])
    print("ListObject 2 times",listObject *2)
    print("Concatenate Two Lists:",listObject+tinyListObject)
ListTypes()