import os


def cls():

    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    Inputs:
        none

    Returns:
        the list without extra spaces, duplicates, and with all names in title case.

    """
    cleaned_names = set()

    messy_names = [
        "  alice ",
        "x",
        "Bob",
        " charlie",
        "Alice",
        "BOB ",
        "eve  ",
        " Eve",
        "eve",
        " xavier",
        "albee",
        "a",
        "bib",
    ]

    # Remove spaces
    for n in messy_names:
        cleaned_names.add(n.strip().title())

    sorted_cleaned_names = sorted(cleaned_names)
    print("Cleaned and Sorted Names:")
    for c in sorted_cleaned_names:
        print(c)


if __name__ == "__main__":
    cls()
    main()
