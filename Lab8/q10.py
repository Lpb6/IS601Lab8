# read 10 numbers and display distinct numbers
def distinct_numbers(array):
    unique_numbers = []
    for i in array:
        if i not in unique_numbers:
            unique_numbers.append(i)
    print(f'There are {len(unique_numbers)} distinct values: {str(unique_numbers)}')


array = []
while len(array) < 10:
    number = int(input("Enter a number to add to the list: "))
    array.append(number)

distinct_numbers(array)
