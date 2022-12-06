import os


def letter_value(letter: str) -> int:
    value = ord(letter) - 96
    return value if value > 0 else value + 58

def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)

def main():
    filename = "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        data = f.read().splitlines()

    priorities = 0
    for a, b, c in grouped(data, 3):
        # Find common letter between compartments
        setA = set(a)
        setB = set(b)
        setC = set(c)

        common = list(setA.intersection(setB).intersection(setC))[0]
        priorities += letter_value(common)

    print(f"Sum of priorities: {priorities}")

if __name__ == "__main__":
    main()
