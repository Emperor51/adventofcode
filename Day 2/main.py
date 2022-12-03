###
#   Advent of Code
#   Day 2
###

score = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

def main():
    importedFile = open("input.txt", 'r')
    lines = importedFile.readlines()

    total = 0

    for line in lines:
        total += winOrLose(line[0], line [2])
        total += score[line[2]]

    # Part 1 Answer
    print(total)


def winOrLose(player1, player2):
    if player1 == 'A' and player2 == 'Y':         # Rock vs Paper
        return 6
    elif player1 == 'B' and player2 == 'Z':       # Paper vs Scissors
        return 6
    elif player1 == 'C' and player2 == 'X':       # Scissors vs Rock
        return 6
    elif ord(player1) == (ord(player2) - 23):   # Draw
        return 3
    else:                                       # Loss
        return 0


if __name__ == '__main__':
    main()
