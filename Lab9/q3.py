def is_anagram(filename):
    with open(filename, 'r') as file:
        string = file.read().strip()
    with open(filename, "w") as file:
        reversed = ''
        for i in string:
            reversed = i + reversed
        if reversed.lower() == string.lower():
            file.write(f"{string} is an anagram")
        else:
            file.write(f"{string} is not an anagram")

def main():
    filename = input("Enter the filename: ")
    is_anagram(filename)
        

if __name__ == "__main__":
    main()