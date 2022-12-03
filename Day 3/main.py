# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def part1():
    sum = 0
    importedFile = open("text1.txt", 'r')
    for line in importedFile:
        firstpart, secondpart = line[:len(line) // 2], line[len(line) // 2:]
        char = set(firstpart).intersection(secondpart).pop()
        if char.isupper():
            sum = sum + (ord(char)-38)
        else:
            sum=sum + ord(char)-96
    print(sum)

def part2():
    sum = 0
    importedFile = open("text2.txt", 'r')
    lines = importedFile.readlines()
    for x in range(0, len(lines), 3):
        char=set(set(lines[x].strip("\n")).intersection(lines[x+1].strip("\n"))).intersection(lines[x+2].strip("\n")).pop()
        #print(char)
        if char.isupper():
            sum = sum + (ord(char)-38)
        else:
            sum = sum + ord(char)-96
    print(sum)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part1()
    part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
