inputfile = open('Day1/example2.txt', 'r')

sum = 0
valid = {"1":1, "one" : 1,"2":2, "two" : 2,"3":3, "three" : 3,"4":4, "four" : 4,"5":5, "five": 5,"6":6, "six" : 6 ,"7":7, "seven" : 7,"8":8, "eight" : 8, "9":9, "nine" : 9}


for line in inputfile:
    firstNum = 99
    lastNum = 99
    inLine = []
    for number in valid:
        if number in line:
            inLine.append(number)
    print(inLine)
    firstPos = 9999
    lastPos = 0
    for number in inLine:
        if line.count(number)==1:
            if line.find(number) > lastPos:
                lastPos =line.find(number)
                lastNum = valid[number]
            if line.find(number) < firstPos:
                firstPos = line.find(number)
                firstNum = valid[number]
        #else:





    finalNum = str(firstNum)+str(lastNum)
    sum = sum + int(finalNum)

print(sum)