import os


def find_packet_marker(data):
    PACKET_SIZE = 4
    packet_seq = ""

    for index, char in enumerate(data):
        packet_seq += char
        if len(packet_seq) == PACKET_SIZE:
            if len(set(packet_seq)) == PACKET_SIZE:
                break
            else:
                packet_seq = packet_seq[1:]

    print(f"Packet marker found at position {index + 1}")


def main():
    filename = "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        data = f.read().splitlines()

    find_packet_marker(data[0])


if __name__ == "__main__":
    main()
