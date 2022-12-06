import os


def main():
    filename = "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        data = f.read().splitlines()

    cur_max = 0
    elf_cals = []
    for entry in data:
        if entry != "":
            cur_max += int(entry)
        else:
            elf_cals.append(cur_max)
            cur_max = 0

    elf_cals.sort(reverse=True)
    print(elf_cals)

    max_cals = sum(elf_cals[:3])

    print(f"Max Cals: {max_cals}")

if __name__ == "__main__":
    main()
