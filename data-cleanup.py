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
    cleaned_names = []

    messy_names = [
        "  alice ",
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
        c = n.strip().title()
        if c not in cleaned_names:
            cleaned_names.append(c)

    cleaned_names.sort()
    print("Cleaned and Sorted Names:")
    for c in cleaned_names:
        print(c)


if __name__ == "__main__":
    cls()
    main()
