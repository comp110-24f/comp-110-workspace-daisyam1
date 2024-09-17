"""CQ00: Functions"""

__author__ = "730740592"


def mimic(message: str) -> str:
    """Repeat input"""
    return message


def main() -> None:
    """Print mimic message"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
