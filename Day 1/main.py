###
#   Advent of Code
#   Day 1
###

def main():
    importedFile = open("input.txt", 'r')
    sum = 0
    elfs = []
    for line in importedFile:
        if line != "\n":
            sum += int(line.strip("\n"))
        else:
            elfs.append(sum)
            sum = 0
    print(max(elfs), elfs.index(max(elfs)))

if __name__ == '__main__':
    main()
