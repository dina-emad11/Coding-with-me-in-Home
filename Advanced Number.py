num = int(input("Enter your number: "))
if num >0:
    if num % 2 == 0:
        print("The Number is positive and even")
    else:
        print("The Number is positive and odd")
elif num == 0:
    print("The Number is ZERO")
else:
    print("The Number is Negative")
