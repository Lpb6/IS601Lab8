def remove_first(filename, num_chars):
    try:
        with open(filename,"r") as file:
            string = file.read().strip()
        with open(filename,"w") as file:
            new_string = string[int(num_chars):]
            file.write(new_string)
    except Exception as e:
        print(e)

def main():
    filename = input("Enter the filename: ")
    num_characters = input("Enter the number of characters to be removed from the front: ")
    remove_first(filename, num_characters)

if __name__ == "__main__":
    main()