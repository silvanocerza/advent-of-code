from pathlib import Path


def check_card(card: str):
    (winning_numbers, numbers) = card.split(":")[-1].split("|")
    winning_numbers = [int(n) for n in winning_numbers.strip().split(" ") if n]
    numbers = [int(n) for n in numbers.strip().split(" ") if n]
    matches = 0
    for w in winning_numbers:
        if w in numbers:
            matches += 1
    return matches


def process_cards(cards: list):
    bucket = {i: [c] for i, c in enumerate(cards)}

    for card_id in bucket.keys():
        for card in bucket[card_id]:
            matches = check_card(card)
            for match in range(matches):
                card_id_won = card_id + match + 1
                bucket[card_id_won].append(bucket[card_id_won][0])

    return sum((len(c) for c in bucket.values()))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    lines = Path(args.filename).read_text().splitlines()

    cards_won = process_cards(lines)

    print(f"You won a total of: {cards_won} cards")
