nums = input("Enter a number: ").split()

unique = []

for item in nums:
    if item not in unique:
        unique.append(item)

print("Orignal List ",nums)
print("Modify List ",unique)
