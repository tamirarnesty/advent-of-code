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

        if (range1.start >= range2.start and range1.stop <= range2.stop) or (range2.start >= range1.start and range2.stop <= range1.stop):
            assignments_contained += 1
    
    print(f"{assignments_contained} Assignments Fully Contained In Another")

if __name__ == "__main__":
    main()
