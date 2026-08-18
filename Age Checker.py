name = input("Please enter your name: ")
year = input("Please enter your year: ")

age = 2026 - int(year)
if age >= 18:
    print("Hello",name,"you are",age,"years old.")
else:
    print("Sorry, you are under 18")
