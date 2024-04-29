# display all numbers from 100 to 1000 that are divisible by 5 and 6
def displayNums():
    numList = []
    for i in range(100,1001):
        if i % 5 == 0 and i % 6 == 0:
            numList.append(i)
    print(numList)

displayNums()