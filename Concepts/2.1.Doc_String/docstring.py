"""
The docstring is an in-built feature of Python, which is used to associate documentation that has been written with Python modules, functions, classes, and methods. It is added right below the functions, modules, or classes to describe what they do. In Python, the docstring is then made available via the Python __doc__ attribute.
"""
def add(a,b):
    # Showing use of doc string to link documentation.
    """Functions to add the value of a and b"""

    return a+b

print(add.__doc__)
print(add(2,3))

""""
python 2.Comments/Comments.py
Functions to add the value of a and b
5
"""
