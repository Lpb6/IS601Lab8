# create a program that reads integers finds the largest and counts its occurences
def function():
    largestNum = 0
    counter = 0
    number = int(input("Enter an integer (type 0 to end): "))
    numbers = [number]
    while number != 0:
        number = int(input("Enter an integer (type 0 to end): "))
        numbers.append(number)
    numbers.pop()
    for i in numbers:
        if i > largestNum:
            largestNum = i
    for i in numbers:
        if i == largestNum:
            counter += 1
    print(f"The largest number is {largestNum} and it occurs {counter} times")

function()