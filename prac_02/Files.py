# 1
name = input("What is your name?")
file = open('name.txt', 'w')
file.write(name)
file.close()
# 2
file = open('name.txt', 'r')
thin = file.read()
print("Your name is"+ thin)
file.close()
# 3
file = open('numbers.txt', 'w')
file.write("17\n42\n400")
file.close()
file = open('numbers.txt', 'r')
num1 = file.readline()
num2 = file.readline()
num3 = int(num1) + int(num2)
print(str(num3))
file.close()
#4
file = open("numbers.txt","r")
total = 0
for line in file:
    number = int(line)
    total += number
print(total)
file.close()
