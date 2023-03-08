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
     # Iterate List - Approach 1
    print("Approach 1 ----- Printing list type using range for...loop")
    for i in listObject:
        print(i)
    
    # Iterate List- Approach 2
    print("Approach 2 ----- Printing list type using range for...loop length")
    lengthListObject = len(listObject)
    for i in range(lengthListObject):
        print(listObject[i])
    
    # Iterate List While Loop - Approach 3
    print("Approach 3 ----- Printing list type using range while...loop length")
    index = 0 
    while index < lengthListObject:
        print(listObject[index])
        index += 1

    # Iterate List Using List Comprehensive Loop - Approach 4
    print("Approach 4 ----- Printing list type using list comprehensive loop")
    [print(i) for i  in listObject]

    # Iterate List Using Enumerate - Approach 5
    print("Approach 5 ----- Printing List Enumerate")
    for i,v in enumerate(listObject):
        print(i," ",v)
ListTypes()

def TupleTypes():
    print('\n\n\n')
    tupleObject = ('harry',786,2.24,'potter')
    tupleObjectMini = ('Serious','Black')
    print("TupleObject:",tupleObject)
    print("TupleObject[0]",tupleObject[0])
    print("TupleObject[1:3]",tupleObject[1:3])
    print("tupleObject * tupleObjectMini",tupleObject + tupleObjectMini)
    
    # Iterate Tuple - Approach 1
    print("Approach 1 ----- Printing tuple type using range for...loop")
    for i in tupleObject:
        print(i)
    
    # Iterate Tuple - Approach 2
    print("Approach 2 ----- Printing tuple type using range for...loop length")
    lengthTupleObject = len(tupleObject)
    for i in range(lengthTupleObject):
        print(tupleObject[i])
    
    # Iterate Tuple While Loop - Approach 3
    print("Approach 3 ----- Printing tuple type using range while...loop length")
    index = 0 
    while index < lengthTupleObject:
        print(tupleObject[index])
        index += 1

    # Iterate Tuple Using List Comprehensive Loop - Approach 4
    print("Approach 4 ----- Printing tuple type using list comprehensive loop")
    [print(i) for i  in tupleObject]

    # Iterate Tuple Using Enumerate - Approach 5
    print("Approach 5 ----- Printing tuple Enumerate")
    for i,v in enumerate(tupleObject):
        print(i," ",v)
TupleTypes()

def DictionaryTypes():
    dictionaryObject = {}
    dictionaryObject['one'] = "One"
    dictionaryObject[1] = 1
    print("DictionaryObject",dictionaryObject)
    
    # Approach 1 : Iterating over dictionary
    print("# Approach 1 : Iterating over dictionary")
    for key in dictionaryObject:
        print("Key: ",key," Value:",dictionaryObject[key])
    
    # Approach 2 : Iterate using items()
    print("# Approach 2 : Iterate using items()")
    for item in dictionaryObject.items():
        print(item)

    # Approach 2 : Iterate using items()
    print("# Approach 3 : Iterate using keys()")
    
    for value in dictionaryObject.keys():
        print(value)
DictionaryTypes()