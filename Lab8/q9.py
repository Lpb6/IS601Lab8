# return average of the list
def return_average(array):
    total = 0
    for i in array:
        total += i
    average = total / len(array)
    return average

array = [1,5,2,4]
print(return_average(array))