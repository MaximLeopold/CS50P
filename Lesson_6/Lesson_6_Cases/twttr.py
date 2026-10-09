"""Remove vowels from text, much like Twitter's original name, twttr."""


def main():
    text = input("Input: ")
    print("Output:", shorten(text))


def shorten(word):
    """Return word with all uppercase and lowercase vowels omitted."""
    shortened = ""

    for character in word:
        if character.lower() not in "aeiou":
            shortened += character

    return shortened


if __name__ == "__main__":
    main()
