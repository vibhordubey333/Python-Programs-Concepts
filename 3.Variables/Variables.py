counter = 345
print(counter)
# To delete vairable.
#del counter

# After variable is deleted we'll get 
#print(counter)

# Traceback (most recent call last):
#   File "C:\Users\vibdubey\Downloads\Golang_POC_Personal\Python-Programs-Concepts\3.Variables\Variables.py", line 4, in <module>
#     print(counter)
# NameError: name 'counter' is not defined

# Multiple assignment
a = b = c = 100

print ("a:",a)
print ("b:",b)
print ("c:",c)

globalVariable = 115

def sum():
   #globalVariable = 34 # If uncommented 115 will be overrided with 34
   return globalVariable
print("Sum",sum())