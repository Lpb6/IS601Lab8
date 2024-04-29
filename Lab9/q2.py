def is_palindrome(filename):
    with open(filename, 'r') as file:
        num = int(file.read().strip())

    with open(filename, "w") as file:
        temp = num
        reversed = 0
        while temp > 0:
            remainder = temp % 10
            reversed = (reversed * 10) +remainder
            temp = temp // 10
        if num == reversed:
            file.write(f"{num} is a palindrome")
        else:
            file.write(f"{num} is not a palindrome")

def main():
    filename = input("Enter the filename: ")
    is_palindrome(filename)
        

if __name__ == "__main__":
    main()