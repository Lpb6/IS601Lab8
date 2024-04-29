# find the smallest element in a list of float values
def find_smallest(array):
    min_value = array[0]
    for i in range(len(array)):
        if array[i] < min_value:
            min_value = array[i]
    return min_value

array = []
while True:
    number = input("Enter a number to add to list(Press Enter to end): ")
    if number =='':
        break
    else:
        array.append(float(number))

print("The smallest value is: " + str(find_smallest(array)))