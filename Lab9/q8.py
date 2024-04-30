def replaceOccurences(filename,char_to_replace, replace_with):
    try:
        with open(filename, 'r') as file:
            string = file.read().strip()
        with open(filename, "w") as file:
            new_string = ''
            for i in string:
                if i == char_to_replace:
                    new_string = new_string + replace_with
                else:
                    new_string = new_string + i
            file.write(new_string)
    except Exception as e:
        print(e)
def main():
    filename = input("Enter the filename: ")
    char_to_replace = input("Enter the character to replace: ")
    replace_with = input("Enter the character that will replace the old one: ")
    replaceOccurences(filename, char_to_replace, replace_with)
        

if __name__ == "__main__":
    main()