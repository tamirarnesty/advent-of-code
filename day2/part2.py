import os

"""
The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round.
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors
the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.
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

    mapping = {
        # Draw
        "AY": "AX",
        "BY": "BY",
        "CY": "CZ",
        # Win
        "AZ": "AY",
        "BZ": "BZ",
        "CZ": "CX",
        # Lose
        "AX": "AZ",
        "BX": "BX",
        "CX": "CY",
    }

    points = []
    for entry in data:
        row = entry[0] + entry[2]
        mapped = mapping[row]
        points.append(matches[mapped])

    print(f"Total for round: {sum(points)}")


if __name__ == "__main__":
    main()
