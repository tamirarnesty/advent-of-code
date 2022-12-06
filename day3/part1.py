import os


def letter_value(letter: str) -> int:
    value = ord(letter) - 96
    return value if value > 0 else value + 58


def main():
    filename = "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        data = f.read().splitlines()

    priorities = 0
    for line in data:
        length = len(line)
        middle = length // 2

        compartment1 = line[:middle]
        compartment2 = line[middle:]

        # Find common letter between compartments
        set1 = set(compartment1)
        set2 = set(compartment2)

        diff = list(set1.intersection(set2))[0]
        priorities += letter_value(diff)

    print(f"Sum of priorities: {priorities}")

if __name__ == "__main__":
    main()
