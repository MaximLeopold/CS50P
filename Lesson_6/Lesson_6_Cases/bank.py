"""Calculate the payout for a bank greeting."""


def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    """Return the payout associated with greeting as an integer."""
    greeting = greeting.lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
