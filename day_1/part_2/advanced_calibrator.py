from pathlib import Path
import re


DIGITS_REGEX = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
DIGITS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def calibrate(path: Path) -> int:
    result = 0
    with path.open("r") as f:
        # line_n = 1
        for line in f:
            matches = DIGITS_REGEX.findall(line)
            first_digit = (
                DIGITS.index(matches[0]) if matches[0] in DIGITS else matches[0]
            )
            second_digit = (
                DIGITS.index(matches[-1]) if matches[-1] in DIGITS else matches[-1]
            )
            number = f"{first_digit}{second_digit}"
            result += int(number)
            # print(f"{line_n=}")
            # print(f"First: {first_digit}, {matches[0]}")
            # print(f"Second: {second_digit}, {matches[-1]}")
            # input("")
            # line_n += 1
    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    result = calibrate(Path(args.filename))
    print(f"Calibrated: {result}")
