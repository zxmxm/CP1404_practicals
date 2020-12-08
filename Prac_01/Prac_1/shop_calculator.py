num = int(input("Enter the number of the item"))
total_price = 0
while num < 0:
    print("Invalid")
    num = int(input("Enter the number of the item"))
for i in range(num):
    price = float(input("Enter the price of the item"))
    total_price = total_price + price
if total_price >= 100:
    total_price = total_price * 0.9
print("The totle price for " + str(num) + " is " + str(total_price))
