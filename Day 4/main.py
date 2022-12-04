###
#   Advent of Code
#   Day 4
###

def main():
    importedFile = open("input.txt", 'r')
    lines = importedFile.readlines()
    sum = 0
    for line in lines:
        split = line.split(',')
        aStart, aFinish, bStart, bFinish = int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1]), int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1])
        if (aStart >= bStart and aFinish <= bFinish) or (aStart <= bStart and aFinish >= bFinish):
            sum +=1
    print(sum)



if __name__ == "__main__":
    main()