from um import count


def test_standalone_um():
    assert count("um") == 1
    assert count("hello, um, world") == 1


def test_case_insensitive():
    assert count("Um") == 1
    assert count("UM, uM, um") == 3


def test_um_inside_other_words():
    assert count("yummy") == 0
    assert count("album umbrella") == 0


def test_multiple_with_punctuation():
    assert count("Um, thanks, um...") == 2
    assert count("um? UM! (uM)") == 3


def test_no_um():
    assert count("Hello, world!") == 0
