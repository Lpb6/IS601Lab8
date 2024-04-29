# reverse a string
def reverse(str):
    string = ''
    for i in str:
        string = i + string
    return string

str = 'This is a test'
print(reverse(str))