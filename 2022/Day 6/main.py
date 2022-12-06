###
#   Advent of Code
#   Day 6
###

def main():
    importedFile = open("input.txt", 'r')
    lines = importedFile.readlines()
    line = lines[0]

    for x in range(0, len(line)-14, 1):
        chars = []
        for y in range(0, 14, 1):
            chars.append(line[(x+y)])
            if len(chars) == len(set(chars)) and len(chars)==14:
                print(x + 14)
                print(chars)
                break






if __name__ == "__main__":
    main()
