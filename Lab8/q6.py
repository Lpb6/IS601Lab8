# return true if list is already sorted in increasing order
def is_sorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

# array = [1,2,3,4,7,6]
# print(is_sorted(array))
array = []
while True:
    number = input("Enter a number to add to the list(press enter to finish): ")
    if number == '':
        break
    else:
        array.append(int(number))
if is_sorted(array):
    print("The list is sorted")
else:
    print("The list is not already sorted")