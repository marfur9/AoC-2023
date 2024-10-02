inputfile = open('Day1/example2.txt', 'r')

sum = 0
valid = ['1','2','3','4','5','6','7','8','9']

for line in inputfile:
    firstNum = 99
    lastNum = 99
    for char in line:
        if char in valid and firstNum==99:
            firstNum = int(char)
            lastNum = int(char)
        elif char in valid:
            lastNum = int(char)
    finalNum = str(firstNum)+str(lastNum)
    sum = sum + int(finalNum)

print(sum)
