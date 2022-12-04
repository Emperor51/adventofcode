###
#   Advent of Code
#   Day 4
###

def main():
    importedFile = open("input.txt", 'r')
    lines = importedFile.readlines()
    sum = 0

    sum2=0
    for line in lines:
        split = line.split(',')
        aStart, aFinish, bStart, bFinish = int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1]), int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1])
        if (aStart >= bStart and aFinish <= bFinish) or (aStart <= bStart and aFinish >= bFinish):
            sum += 1
        if (aStart >= bStart and aStart <= bFinish) or (aFinish >= bStart and aFinish <= bFinish) \
                or (bStart >= aStart and bStart <= aFinish) or (bFinish >= aStart and bFinish <= aFinish):
            sum2 += 1

    print("Total Contained:", sum)
    print("Total Overlap:", sum2)



if __name__ == "__main__":
    main()