#count occurences of character in string

def countOccurences(str, character):
    count = 0
    for i in str:
        if i.lower() == character.lower():
            count += 1
    return count


str = 'This is a test'
character = 'i'
print(countOccurences(str,character))