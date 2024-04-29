# remove duplicates from user entered list
def removeDuplicates(array):
    unique_array = []
    for i in array:
        if i not in unique_array:
            unique_array.append(i)
    return unique_array
array = []
while True:
    number = input("Enter a number to add to list(Press Enter to end): ")
    if number =='':
        break
    else:
        array.append(int(number))

print("The array without duplicates: " + str(removeDuplicates(array)))