def is_prime(filename):
    with open(filename, 'r') as file:
        num = int(file.read().strip())

    with open(filename, "w") as file:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    file.write(f"{num} is not a prime number")
                    break
            else:
                file.write(f"{num} is a prime number")
        else:
            file.write(f"{num} is not a prime number")
def main():
    filename = input("Enter the filename: ")
    is_prime(filename)
        

if __name__ == "__main__":
    main()