def factorial(filename):
    with open(filename, 'r') as file:
        num = int(file.read().strip())
    with open(filename, "w") as file:
        multiplier = num-1
        while multiplier > 1:
            num = num * multiplier
            multiplier -= 1
        file.write(str(num))
def main():
    filename = input("Enter the filename: ")
    factorial(filename)
        

if __name__ == "__main__":
    main()