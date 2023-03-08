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
    
    print("# Manipulating Map items")
    # Manipulating Map items
    for k,v in dictionaryObject.items():
        if isinstance(v,int):
           dictionaryObject[k] = v * 10 # Output: 10 
        elif isinstance(v,str):
           dictionaryObject[k] = v + " HELLO" 
        else:
            print("Type not specified.")
    print("DictionaryObject After Manipulation:",dictionaryObject)
    
    del dictionaryObject['one'] # Deleting Element From Dictionary.
    print("After Deleting Element From Dictionary",dictionaryObject)

DictionaryTypes()