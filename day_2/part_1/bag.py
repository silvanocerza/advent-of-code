from pathlib import Path

CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def game_calculator(line: str):
    parts = line.split(":")
    game_id = int(parts[0][5:])
    sets = parts[1].split(";")
    result = {"id": game_id, "sets": []}
    for cubes_set in sets:
        cubes = cubes_set.split(",")
        current_set = {}
        for cube in cubes:
            (number, color) = cube.strip().split(" ")
            current_set[color] = int(number)

        result["sets"].append(current_set)
    return result


def is_valid(game: dict) -> bool:
    sets = game["sets"]
    for cubes in sets:
        current_count = {"red": 0, "green": 0, "blue": 0}
        for cube, count in cubes.items():
            current_count[cube] += count
            if current_count[cube] > CUBES[cube]:
                return False
    return True


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    lines = Path(args.filename).read_text().splitlines()

    games = [game_calculator(l) for l in lines]

    count = 0
    for game in games:
        if is_valid(game):
            count += game["id"]

    print(f"Sum of IDs: {count}")
