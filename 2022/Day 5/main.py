###
#   Advent of Code
#   Day 5
###

importedFile = open("input.txt", 'r')

lines = importedFile.readlines()

def main():

    answerPart1()
    answerPart2()

def answerPart2():
    crates = horitzontalCrates(vertialCrates())


def answerPart1():
    crates = horitzontalCrates(vertialCrates())

    for x in range(10, len(lines), 1):
        count = int(lines[x].split(' ')[1])
        start = int(lines[x].split(' ')[3])
        stop = int(lines[x].split(' ')[5])
        for y in range(1, count + 1, 1):
            crates[stop - 1].append(crates[start - 1].pop())
    for line in crates:
        print(line[len(line)-1])

def horitzontalCrates(vertCrates):
    crates = []
    for y in range(0, 9, 1):
        temp = []
        #print(y)
        for x in range (0, len(vertCrates), 1):
            if vertCrates[x][y] != ' ':
                temp.append(vertCrates[x][y])
        crates.append(temp[::-1])
    return crates

def vertialCrates():
    # Put crates into a vertical array
    vertCrates = []
    for x in range(0, 8, 1):
        temp = []
        for y in range(1, len(lines[x]), 4):
            temp.append(lines[x][y])
        for z in range(1, 10 - len(temp), 1):
            temp.append(' ')
        vertCrates.append(temp)
    return vertCrates

if __name__ == "__main__":
    main()