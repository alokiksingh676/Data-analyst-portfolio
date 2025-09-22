# loops in python
# For loop
fruits = ["apple", "banana", "cherry"]
print("For loop example:")
for fruit in fruits:
    print("I like", fruit)

for i in range(1 ,5 ) :
    print("number :",i)

# While loop
print("\nWhile loop example:")
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Using break in a loop
print("\nBreak example:")
for num in range(1, 10):
    if num == 5:
        print("Breaking at", num)
        break
    print(num)
    #using continue in loop
for num in range(1, 6):
    if num == 3:
        continue  # skip 3
    if num == 5:
        break     # stop loop at 5
    print(num)

#Nested loops
for i in range(3): 
    for j in range(2): 
        print(f"i={i}, j={j}")
