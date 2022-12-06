import os

"""
The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round.
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors
R > S
S > P
P > R
"""


def main():
    filename = "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        data = f.read().splitlines()

    # Rules
    matches = {
        "AX": 1 + 3,
        "AY": 2 + 6,
        "AZ": 3 + 0,
        "BX": 1 + 0,
        "BY": 2 + 3,
        "BZ": 3 + 6,
        "CX": 1 + 6,
        "CY": 2 + 0,
        "CZ": 3 + 3,
    }

    points = [matches[entry[0] + entry[2]] for entry in data]

    print(f"Total for round: {sum(points)}")


if __name__ == "__main__":
    main()
