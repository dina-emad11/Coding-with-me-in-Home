numbers = input("Enter numbers separated by space: ").split()
newNumber = []

for x in numbers:
    newNumber.append(int(x))
total = 0
count = 0
for num in newNumber:
    total += num
    count += 1
average = total/count
print("Average: ",average)
