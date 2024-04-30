def adjust_case():
    with open("name.txt","r") as file:
        sentence = file.read().strip()
        segments = sentence.split(' ')
        new_list =[]
        for string1 in segments:
            string = string1
            capitalized_text = string[0].upper() + string[1:]
            new_list.append(capitalized_text)
        new_sentence = ' '.join(new_list)
        print(new_sentence)
adjust_case()


def display_nums():
    for i in range(100,1001):
        if i % 5 == 0 and i % 6 != 0:
            print(i)
        if i % 6 == 0 and i % 5 != 0:
            print(i)
display_nums()