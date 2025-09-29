# Simple calculator for solving basic operations

a = float(input("enter first number : "))
b = float(input("enter second number : "))

print('''enter 1 for addition
     enter 2 for substraction
     enter 3 for multiplication
     enter 4 for division''')

n = int(input("enter your choice: "))

if n==1:
    print(f"{a} + {b} = {a+b}")

elif n==2:
    print(f"{a} - {b} = {a-b}")

elif n==3:
    print(f"{a} * {b} = {a*b}")

elif n==4:
    if b != 0:
        print(f"{a} / {b} = {a/b}")
    else:
        print("cannot divided by zero !")

else:
    print("please enter a valid choice:")