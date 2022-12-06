import os


def main():
    filename = "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        data = f.read().splitlines()

    max_cals = 0
    cur_max = 0
    elf_index = 0
    for entry in data:
        if entry != "":
            cur_max += int(entry)
        else:
            if cur_max > max_cals:
                max_cals = cur_max
                elf_index += 1
            cur_max = 0

    print(f"Max Cals: {max_cals}")
    print(f"Eating Elf: {elf_index}")

if __name__ == "__main__":
    main()
