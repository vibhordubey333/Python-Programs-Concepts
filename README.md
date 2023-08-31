#### How to run python program ?
`python your_program_name.py`

#### Who created python ?

Guido van Rossum. Development started in December 1989. 
#### Features of python ?

Python is a dynamic, high-level, free open source, and interpreted programming language. It supports object-oriented programming as well as procedural-oriented programming. In Python, we don’t need to declare the type of variable because it is a dynamically typed language. For example, x = 10 Here, x can be anything such as String, int, etc.
Features in Python

There are many features in Python, some of which are discussed below as follows:
**1. Free and Open Source**

Python language is freely available at the official website and you can download it from the given download link below click on the Download Python keyword. Download Python Since it is open-source, this means that source code is also available to the public. So you can download it, use it as well as share it. 
**2. Easy to code**

Python is a high-level programming language. Python is very easy to learn the language as compared to other languages like C, C#, Javascript, Java, etc. It is very easy to code in the Python language and anybody can learn Python basics in a few hours or days. It is also a developer-friendly language. 
**3. Easy to Read**

As you will see, learning Python is quite simple. As was already established, Python’s syntax is really straightforward. The code block is defined by the indentations rather than by semicolons or brackets.
**4. Object-Oriented Language**

One of the key features of Python is Object-Oriented programming. Python supports object-oriented language and concepts of classes, object encapsulation, etc. 
**5. GUI Programming Support**

Graphical User interfaces can be made using a module such as PyQt5, PyQt4, wxPython, or Tk in Python. PyQt5 is the most popular option for creating graphical apps with Python.
**6. High-Level Language**

Python is a high-level language. When we write programs in Python, we do not need to remember the system architecture, nor do we need to manage the memory.
**7. Large Community Support**

Python has gained popularity over the years. Our questions are constantly answered by the enormous StackOverflow community. These websites have already provided answers to many questions about Python, so Python users can consult them as needed.
**8. Easy to Debug**

Excellent information for mistake tracing. You will be able to quickly identify and correct the majority of your program’s issues once you understand how to interpret Python’s error traces. Simply by glancing at the code, you can determine what it is designed to perform.
**9. Python is a Portable language**

Python language is also a portable language. For example, if we have Python code for Windows and if we want to run this code on other platforms such as Linux, Unix, and Mac then we do not need to change it, we can run this code on any platform.
**10. Python is an Integrated language**

Python is also an Integrated language because we can easily integrate Python with other languages like C, C++, etc. 
**11. Interpreted Language:** 

Python is an Interpreted Language because Python code is executed line by line at a time. like other languages C, C++, Java, etc. there is no need to compile Python code this makes it easier to debug our code. The source code of Python is converted into an immediate form called bytecode.
**12. Large Standard Library** 

Python has a large standard library that provides a rich set of modules and functions so you do not have to write your own code for every single thing. There are many libraries present in Python such as regular expressions, unit-testing, web browsers, etc.
**13. Dynamically Typed Language**

Python is a dynamically-typed language. That means the type (for example- int, double, long, etc.) for a variable is decided at run time not in advance because of this feature we don’t need to specify the type of variable.
**14. Frontend and backend development**

With a new project py script, you can run and write Python codes in HTML with the help of some simple tags <py-script>, <py-env>, etc. This will help you do frontend development work in Python like javascript. Backend is the strong forte of Python it’s extensively used for this work cause of its frameworks like Django and Flask.
**15. Allocating Memory Dynamically**

In Python, the variable data type does not need to be specified. The memory is automatically allocated to a variable at runtime when it is given a value. Developers do not need to write int y = 18 if the integer value 15 is set to y. You may just type y=18.


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

#### Difference between Comments and DocStrings ?

![image](https://github.com/vibhordubey333/Python-Programs-Concepts/assets/22407855/4a505f73-730a-47c1-aa58-ef63dc21e3b0)


#### Reference:

0. CheatSheet:
  - https://github.com/peterlamar/python-cp-cheatsheet
1. Python Collection :
  - https://www.w3schools.com/python/python_dictionaries.asp
