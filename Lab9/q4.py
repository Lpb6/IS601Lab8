def is_max(filename):
    with open(filename, 'r') as file:
        nums = file.read().strip().split(' ')
    with open(filename, "w") as file:
        max = nums[0]
        for num in nums:
            if num > max:
                max = num
        file.write(f"{max} is max")
def main():
    filename = input("Enter the filename: ")
    is_max(filename)
        

if __name__ == "__main__":
    main()