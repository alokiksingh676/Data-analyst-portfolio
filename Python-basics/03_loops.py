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
