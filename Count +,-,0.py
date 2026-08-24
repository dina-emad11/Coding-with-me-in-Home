numbers = input("Enter numbers separated by space: ").split()
newList = []

for num in numbers:
    newList.append(int(num))
print("newList ",newList)

positive = 0
negative = 0
zero = 0

for num in newList:
    if num > 0:
        positive+=1
    elif num < 0:
        negative+=1
    else:
        zero+=1
print("Positive: ",positive)
print("Negative: ",negative)
print("Zero: ",zero)

