num1=float(input("Enter First Number : "))
operator=input("Choose an operation (+,-,/,*,%) : ")
num2=float(input("Enter Second Number : "))

if operator == "+":
    result=num1+num2
    print(num1,"+",num2,"= ",result)
elif operator == "-":
    result = num1 - num2
    print(num1, "-", num2, "= ", result)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(num1, "/", num2, "= ", result)
    else:
        print("Can’t Division by ZERO")
elif operator == "*":
    result = num1 * num2
    print(num1, "*", num2, "= ", result)
elif operator == "%":
    result = num1 % num2
    print(num1, "%", num2, "= ", result)
else:
    print("Invaild Operation ",operator)
