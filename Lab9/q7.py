import math
def find_area(filename):
    with open(filename, 'r') as file:
        radius = float(file.read().strip())
    with open(filename, "w") as file:
        area = math.pi * radius**2
        file.write(str(area))
def main():
    filename = input("Enter the filename: ")
    find_area(filename)
        

if __name__ == "__main__":
    main()