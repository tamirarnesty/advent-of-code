import os
from typing import List


def construct_crate_map(crates: List[str]) -> List:
    """Construct a map of crates, where each crate is a list of items."""
    num_row = crates.pop()
    size = int(max(filter(lambda x: x != "", num_row.split(" "))))

    crates = [l.replace("    ", "-") for l in crates]

    crate_map = [[] for _ in range(size)]
    for row in reversed(crates):
        row.replace("    ", "-")
        stack = 0
        for element in row:
            if element == "-":
                stack += 1
            elif 65 <= ord(element) <= 90:
                crate_map[stack].append(element)
                stack += 1

    return crate_map


def extract_moves(instructions: List[str]) -> List:
    """Extract the moves from the instructions."""
    moves = []
    for procedure in instructions:
        _, count, _, start, _, end = procedure.split(" ")
        moves.append((int(count), int(start), int(end)))

    return moves


def perform_moves(crate_map: List[str], moves: List[tuple]) -> List:
    for move in moves:
        count, start, end = move
        pick = crate_map[start - 1][-count:]

        for crate in pick:
            crate_map[start - 1].pop()
            crate_map[end - 1].append(crate)

    display(crate_map, "2")


def display(stacks, model):
    print("Crates on top after the rearrangement (v" + model + "): ", end="")
    for s in stacks:
        print(s[-1], end="")
    print("")


def main():
    filename = "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        data = f.read().splitlines()

    index_of_split = data.index("")
    instructions = data[index_of_split + 1 :]
    crates = data[:index_of_split]

    crate_map = construct_crate_map(crates)
    moves = extract_moves(instructions)

    perform_moves(crate_map, moves)


if __name__ == "__main__":
    main()
