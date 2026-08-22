num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))
num3 = float(input("Enter number 3:"))

if num1==num2==num3:
    print("All Numbers are Equal",num1)
elif num1 > num2 and num1 > num3:
    print(num1,"Number 1 is the Largest.")
elif num2 > num1 and num2 > num3:
    print(num2,"Number 2 is the Largest.")
elif num3 > num1 and num3 > num2:
    print(num3,"Number 3 is the Largest.")
