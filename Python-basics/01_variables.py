#variables in python 

#numeric variables
Age = 20

#string variable
Name = "Alokik"

#boolean variable
is_student = True

#float variable
Height = 5.9

#printing variables
print("Age:",Age)
print("Name:",Name)
print("Are you a student ? ",is_student)
print("height:",Height)

#printing variables in morden way
print(f"My name is {Name},I am {Age} years old.\n My height is {Height} feet")

#taking user input 
user_name=str(input("Enter your name :"))
user_age=int(input("Enter your age :"))
print(f"hello {user_name},next year you will be {user_age + 1} years old.")
#here i used basic operation on variable

# assigning multiple values at once 
x,y,z=1,2,3
print(f"x={x},y={y},z={z}")

#Type checking and conversion 
name = "Alokik"
age = 20 
print("variable type of name :",type(name))
print("variable type of age :",type(age))
age=str(age)
print("variable type of age after conversion:",type(age))

#swapping of variables
a,b=10,20
print(f"a={a} and b={b} before swapping.")
a,b=b,a
print(f"a={a} and b={b} after swapping.")

#constant (all upper case)
PI=3.141
GRAVITY=9.8
print("Constants:", PI, GRAVITY)

# Dynamic typing
var = 10
print("Dynamic typing: var =", var, "type:", type(var))
var = "Now I’m a string"
print("Dynamic typing: var =", var, "type:", type(var))

#global and local variable
global_var="i am a global variable"
def my_function():
    local_var="i am a local variable"
    print(local_var)
    print(global_var)
my_function()
   
#print(local_var)   thi will throw an error as we do not declare the local_var outside the function

