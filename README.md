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

### Variables
  - No such datatypes are there. Python automatically infers them like in Go we've `:=`.
  
      ```
      counter = 100          # Creates an integer variable
      miles   = 1000.0       # Creates a floating point variable
      name    = "Zara Ali"   # Creates a string variable
      ```
  - We can delete the variable as well.
      ```
        del counter
      ```
  - If we try to print the variable `counter` then it will present the error
      ```
      100
      Traceback (most recent call last):
        File "main.py", line 7, in <module>
          print (counter)
      NameError: name 'counter' is not defined
      ```
   - Multiple variable assignment.
     ```
         a = b = c = 100

          print (a)
          print (b)
          print (c)
     ``` 
  - Python Global Variable<br/>
      ```
        x = 5
        y = 10
        def sum():
           sum = x + y
           return sum
        print(sum())
      ```
  
