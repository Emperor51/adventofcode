###
#   Advent of Code
#   Day 7
###

def main():
    importedFile = open("input.txt", 'r')
    lines = importedFile.readlines()

    position = 0
    theArray = []

    for x in range (0, len(lines), 1):
        line = lines[x]
        line = line.strip("\n")

        if line[0] != "$":
            if line[0:3] == "dir":
                # print(str(position), line)
                theArray.append([line])
        elif line == "$ cd ..":
            position = position - 1
        elif line == "$ cd /":
            position = 0
        elif line.__contains__("cd"):
            position += 1
            index = -1
            while index == -1:
                index = findDir(theArray, line)
            print(index)




def findDir(theArray, line):
    for y in range(0, len(theArray), 1):
        try:
            #print(theArray[y])
            (theArray[y].index("dir" + line[4::]))
            return y
        except:
            continue


if __name__ == "__main__":
    main()