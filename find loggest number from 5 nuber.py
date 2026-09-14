a = int(input("number(1):"))
b = int(input("number(2):"))
c = int(input("number(3):"))
d = int(input("number(4):"))
e = int(input("number(5):"))
numbers = [a, b, c, d, e]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
exit = input("press enter to exit")



