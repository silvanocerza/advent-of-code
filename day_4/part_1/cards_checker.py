from pathlib import Path


def check_card(card: str):
    (winning_numbers, numbers) = card.split(":")[-1].split("|")
    winning_numbers = [int(n) for n in winning_numbers.strip().split(" ") if n]
    numbers = [int(n) for n in numbers.strip().split(" ") if n]
    matches = 0
    for w in winning_numbers:
        if w in numbers:
            matches += 1
    if matches == 0:
        return 0
    return 2 ** (matches - 1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    lines = Path(args.filename).read_text().splitlines()

    sum = 0
    for line in lines:
        score = check_card(line)
        sum += score

    print(f"Sum of scores: {sum}")
