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
    for c in row[start:]:
        if c.isdecimal():
            end += 1
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
    span = find_number_span(row, coord[1])

    number_coords = []
    for column in list(range(span[0], span[1])):
        number_coords.append((coord[0], column))

    for t in TRANSFORM:
        for column in list(range(span[0], span[1])):
            adjacent = (coord[0] + t[0], column + t[1])
            if adjacent in number_coords:
                # This is part of the number
                continue
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
    checked_coords = []
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if not lines[r][c].isdecimal():
                # Not a number!
                continue
            if (r, c) in checked_coords:
                # We already checked this!
                continue
            span = find_number_span(lines[r], c)
            for column in list(range(span[0], span[1])):
                checked_coords.append((r, column))

            adjacent = find_adjacent_coords(lines, (r, c))
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

    print(f"Sum of part numbers: {sum}")
