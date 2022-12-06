import os


def main():
    filename = "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        data = f.read().splitlines()

    assignments_contained = 0
    for line in data:
        pair = line.split(",")

        first = pair[0].split("-")
        second = pair[1].split("-")

        startFirst = int(first[0])
        endFirst = int(first[1])

        startSecond = int(second[0])
        endSecond = int(second[1])

        range1 = range(startFirst, endFirst + 1)
        range2 = range(startSecond, endSecond + 1)

        r1_set = set(range1)
        r2_set = set(range2)

        if r1_set & r2_set:
            assignments_contained += 1
    
    print(f"{assignments_contained} Assignments Overlap")

if __name__ == "__main__":
    main()
