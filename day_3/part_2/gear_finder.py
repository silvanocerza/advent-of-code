from pathlib import Path


IGNORED_CHARS = [
    ".",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]


def find_number_span(row: str, start: int) -> (int, int):
    end = start
    # Find forward
    for c in row[start:]:
        if c.isdecimal():
            end += 1
        else:
            break

    # Find backward
    for c in row[:start][::-1]:
        if c.isdecimal():
            start -= 1
        else:
            break
    return (start, end)


TRANSFORM = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def find_adjacent_coords(matrix: list, coord: (int, int)):
    result = []
    row = matrix[coord[0]]

    for t in TRANSFORM:
        adjacent = (coord[0] + t[0], coord[1] + t[1])
        if -1 in adjacent or adjacent[1] >= len(row) or adjacent[0] >= len(matrix):
            # Out of matrix bounds
            continue
        result.append(adjacent)

    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    lines = Path(args.filename).read_text().splitlines()

    sum = 0
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] != "*":
                # Not a gear!
                continue
            checked_coords = []

            adjacent = find_adjacent_coords(lines, (r, c))

            numbers = []
            for coord in adjacent:
                if not lines[coord[0]][coord[1]].isdecimal():
                    # Not a number
                    continue
                if coord in checked_coords:
                    # We already checked this coord, this digit must be
                    # part of a number that we already found
                    continue

                span = find_number_span(lines[coord[0]], coord[1])
                number = ""
                for column in list(range(span[0], span[1])):
                    number += lines[coord[0]][column]
                    checked_coords.append((coord[0], column))
                numbers.append(int(number))
                checked_coords.append(checked_coords)

            if len(numbers) != 2:
                continue

            sum += numbers[0] * numbers[1]

            is_part_number = False
            for coord in adjacent:
                char = lines[coord[0]][coord[1]]
                if char not in IGNORED_CHARS:
                    is_part_number = True
                    break

            if is_part_number:
                number = ""
                for column in list(range(span[0], span[1])):
                    number += lines[r][column]
                sum += int(number)

    print(f"Sum of part numbers: {sum}")  #
