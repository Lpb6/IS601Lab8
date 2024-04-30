# write function to find fibonacci of a number 
def fibonacci(filename):
    with open(filename, 'r') as file:
        num = int(file.read().strip())
    with open(filename, "w") as file:
        fiboseq = [0,1]
        fibosum = 0
        for i in range(2,num+1):
            fiboseq.append(fiboseq[i-1]+fiboseq[i-2])
        for i in fiboseq:
            fibosum += i
        file.writelines([f'The sum of the sequence is {fibosum}\n',str(fiboseq)])


def main():
    filename = input("Enter the filename: ")
    fibonacci(filename)
        

if __name__ == "__main__":
    main()