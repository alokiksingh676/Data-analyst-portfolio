# Conditional statements in Python
#simple if statement
age=20
if age >= 18 :
    print("you are eligible to cast vote.")
    
# taking input from user if-else statement.
age=int(input("Enter your age :"))
if age>=18 :
    print("you are eligible to cast vote. ")
else :
    print("you are not eligible.")

# if-elif-else ladder
marks=int(input("Enter your marks:"))
if marks>=90 :
    print("you are awarded with : GRADE A .")
elif marks>=80 :
    print("you are awarded with : GRADE B .")
elif marks>=70 :
    print("you are awarded with : GRADE C .") 
elif marks>=60 :
    print("you are awarded with : GRADE D .")
else :
    print("your score is very low.")
# Nested if
X = 15
if  X>0 :
    if X % 3 == 0 :
        print(f"{X} is a postive number and divisible by 3.")
    else :
        print(f"{X} is a positive integer but not divisible by 3.")
else :
    print(f"{X} is a negative number.")    
