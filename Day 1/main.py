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
    #Part 1 Answer
    print("The elf with the most calories is number", elfs.index(max(elfs)), "and they have", max(elfs), "calories.")
    #Part 2 Answer
    topThree = 0
    for x in range (0,3,1):
        topThree += max(elfs)
        elfs.pop(elfs.index(max(elfs)))
    print("Combined, the top three elves have", topThree, "calories.")


if __name__ == '__main__':
    main()
