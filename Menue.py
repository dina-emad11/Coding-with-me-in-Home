print("pizza = 150LE")
print("burger = 100LE")
print("chicken = 180LE")
print("pasta = 120LE")
meal = input("Enter your meal:")
if meal == "pizza":
  price = 150
elif meal == "burger":
  price = 100
elif meal == "chiken":
  price = 180
elif meal == "pasta":
  price = 120
else:
  print("Invalide")
qntity = int(input("Enter the qntity:"))
total = qntity*price
print(total)
delivery = input("Do you want delivery:")
if delivery == "yes":
  total = total+50
else:
  total = total
print(total)
if total >=500 :
  discount=total*0.20
elif total>=300:
  discount=total*0.10
else:
  discount=0
print(discount)
print(total-discount)
