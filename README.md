#### What is Python ?

Python is a: 
  - **Interpreted:** Python is processed at runtime by the interpreter. You do not need to compile your program before executing it. This is similar to PERL and PHP. 
  - **Interactive:** You can actually sit at a Python prompt and interact with the interpreter directly to write your programs.  
  - **Object-oriented:** Python supports Object-Oriented style or technique of programming that encapsulates code within objects. 
  - **High-level programming language**
  - Python supports multiple programming paradigms, including Procedural, Object Oriented and Functional programming language. 
  - Python design philosophy emphasizes code readability with the use of significant indentation.
  
#### Is Python pure object oriented ?
Python is an object-oriented language, but it is not a pure object-oriented language.

A pure object-oriented language is one that treats everything as an object and has no primitives or non-object types. However, Python does have some non-object types such as integers, floats, and strings. These types are not objects in the sense that they do not have methods or attributes like objects do. However, Python does allow these types to be treated as objects through a process called boxing, which is automatically done by the interpreter.

Python also supports procedural and functional programming paradigms, in addition to object-oriented programming, which further distinguishes it from a pure object-oriented language. However, Python's object-oriented features are robust and are widely used in many applications.<br/>
_source_:  😀 https://chat.openai.com/chat

#### Traits of Python ?
- It supports functional and structured programming methods as well as OOP.
- It can be used as a scripting language or can be compiled to byte-code for building large applications.
- It provides very high-level dynamic data types and supports dynamic type checking.
- It supports automatic garbage collection.
- It can be easily integrated with Golang 😃: C, C++, COM, ActiveX, CORBA, and Java.

#### Comments 
  - Single line comment. Example `# Python is awesome`
  - Multiline comments. Example: <br/>
    ```
    # Sniper Elite 4 
    # Doom
    # Far Cry 6
    ```
  - Docstring: Python docstrings provide a convenient way to provide a help documentation with Python modules, functions, classes, and methods. The docstring is then made available via the __doc__ attribute.<br/>
  ```
  def add(a, b):
    """Function to add the value of a and b"""
    return a+b

print(add.__doc__)
  ```

#### Python - Data Types  
Python has various built-in data types which we will discuss with in this tutorial:
  - Numeric - int, float, complex
      - int (signed integers)
      - long (long integers, they can also be represented in octal and hexadecimal)
      - float (floating point real values)
      - complex (complex numbers)
  - String - str
  - Sequence - list, tuple, range
  - Binary - bytes, bytearray, memoryview
  - Mapping - dict
  - Boolean - bool
  - Set - set, frozenset
  - None - NoneType

#### Python -  Collections(Array)
  _source:_ https://www.w3schools.com/python/python_dictionaries.asp
  There are four collection data types in the Python programming language:
  - **List** is a collection which is ordered and changeable. Allows duplicate members.
  - **Tuple** is a collection which is ordered and unchangeable. Allows duplicate members.
  - **Set** is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
  - **Dictionary** is a collection which is ordered** and changeable. No duplicate members.
  
  ```
  *Set items are unchangeable, but you can remove and/or add items whenever you like.
  **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
  ```
 #### Checking Type In Python:
 
  ```
  for k,v in dictionaryObject.items():
        if isinstance(v,int):
            print("Int")
        elif isinstance(v,str):
            print("String")
        else:
            print("")
  ```

#### Functions:
  - Syntax:
    ```
      def functionname( parameters ):
      "function_docstring"
      function_suite
      return [expression]
    ```
  - Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
  - All arguements in the Python language are pass by reference.
  -

#### Reference:

1. Python Collection :
  - https://www.w3schools.com/python/python_dictionaries.asp