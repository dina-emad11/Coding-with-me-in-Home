degree = int(input("Enter your degree: "))
if 0<= degree <=100:
    if degree >= 90:
        print("A")
    elif degree >= 80:
        print("B")
    elif degree >= 70:
        print("C")
    elif degree < 70:
        print("F")
if degree > 85:
    print("Eligible for a scholarship!")
else:
    print("Invalid degree! Please enter a degree between 0 and 100.")
