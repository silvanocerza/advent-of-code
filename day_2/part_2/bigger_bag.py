from pathlib import Path
from itertools import accumulate
import operator
from collections import deque


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


def minimum_cubes(game: dict) -> dict:
    sets = game["sets"]
    minimums = {"red": 0, "green": 0, "blue": 0}
    for cubes in sets:
        for cube, count in cubes.items():
            if minimums[cube] < count:
                minimums[cube] = count
    return minimums


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    lines = Path(args.filename).read_text().splitlines()

    games = [game_calculator(l) for l in lines]

    sum = 0
    for game in games:
        cubes = minimum_cubes(game).values()
        sum += deque(accumulate(cubes, func=operator.mul), maxlen=1)[0]

    print(f"Sum of powers of cubes: {sum}")
