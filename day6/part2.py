import os


def find_message_marker(data):
    MESSAGE_SIZE = 14
    message_seq = ""

    for index, char in enumerate(data):
        message_seq += char
        if len(message_seq) == MESSAGE_SIZE:
            if len(set(message_seq)) == MESSAGE_SIZE:
                break
            else:
                message_seq = message_seq[1:]

    print(f"Packet marker found at position {index + 1}")


def main():
    filename = "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        data = f.read().splitlines()

    find_message_marker(data[0])


if __name__ == "__main__":
    main()
