print("Day 1...")

def readfile():

    input_file = open("input.txt", "r")
    left = []
    right = []

    for line in input_file:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))
    input_file.close()

    return left,right

def day1(): 

    left,right = readfile()

    sum = 0
    for x,y in zip(left, right):
        sum += abs(x-y)
    
    return sum

def day2():

    left, right = readfile()
    sum = 0
    for x in left:
        sum += x * right.count(x)
    return sum

print(day1())
print(day2())
