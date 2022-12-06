import os


def main():
    filename = "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        data = f.read().splitlines()

    print(f"File loaded with data:\n{data}")


if __name__ == "__main__":
    main()
