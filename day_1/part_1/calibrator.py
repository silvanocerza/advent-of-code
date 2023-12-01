from pathlib import Path
import re

DIGIT_REGEX = re.compile(r"\d")


def calibrate(path: Path) -> int:
    result = 0
    with path.open("r") as f:
        for line in f:
            matches = DIGIT_REGEX.findall(line)
            result += int(f"{matches[0]}{matches[-1]}")
    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    result = calibrate(Path(args.filename))
    print(f"Calibrated: {result}")
