numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)

numbers[0]
numbers[-1]
numbers[3]
numbers[:-1]
numbers[3:4]
5 in numbers
7 in numbers
"3" in numbers
numbers + [6, 5, 3]

#1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "Ten"
print(numbers)
#2. Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)
#3.Get all the elements from numbers except the first two (slice)
numbers[2:]
print(numbers[2:])
#4. Check if 9 is an element of numbers
for i in numbers:
    if i==9:
        print("True")