#### Datatypes

Python infers type of a variable dynamically i.e. at run time.

```
    a=10  
    b="Hi Python"  
    c = 10.5  
    print(type(a))  
    print(type(b))  
    print(type(c))  
```
```
Output:
    <type 'int'>
    <type 'str'>
    <type 'float'>
```


#### Standard Data Types

![image](https://github.com/vibhordubey333/Python-Programs-Concepts/assets/22407855/2c34fa4b-29ae-4e28-ac66-db0bdb3c4ae7)<br/>

  -  Numeric: Below example shows the numeric example.
        
        ```
            a = 5  
            print("The type of a", type(a))  
      
            b = 40.5  
            print("The type of b", type(b))  
      
            c = 1+3j  
            print("The type of c", type(c))  
            print(" c is a complex number", isinstance(1+3j,complex))

            Output:        
            The type of a <class 'int'>
            The type of b <class 'float'>
            The type of c <class 'complex'>
            c is complex number: True
        ```
