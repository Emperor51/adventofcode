###
#   Advent of Code
#   Day 2
###

score = {
  "X": 1,
  "Y": 2,
  "Z": 3
}
win = {
  "A": 8,  # win plus Paper
  "B": 9,  # win plus Scissors
  "C": 7   # win plus Rock
}
draw = {
  "A": 4,  # draw plus Rock
  "B": 5,  # draw plus Paper
  "C": 6   # draw plus Scissors
}
lose = {
  "A": 3,  # lose plus Scissors
  "B": 1,  # lose plus Rock
  "C": 2   # lose plug Scissors
}

def main():
    importedFile = open("input.txt", 'r')
    lines = importedFile.readlines()

    totalPt1 = 0
    totalPt2 = 0

    for line in lines:
        totalPt1 += winOrLose(line[0], line [2])
        totalPt1 += score[line[2]]

        totalPt2 += scorePart2(line[0], line [2])

    # Part 1 Answer
    print(totalPt1)

    # Day 2 Answer
    print(totalPt2)
def scorePart2(player1, player2):
    if player2 == 'X': return lose[player1]
    elif player2 == 'Y': return draw[player1]
    elif player2 == 'Z': return win[player1]

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
