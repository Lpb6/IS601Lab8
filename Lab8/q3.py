# create a function that computes the sum of the digits in an integer
def sum(number):
    total = 0
    numStr = str(number)
    for i in numStr:
        total += int(i)
    return total

number =  111222
print(f"The sum of the digits of '{number}' is: {sum(number)}")