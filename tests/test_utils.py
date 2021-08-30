import pytest
from babysitter.utils import regex_finder

def test_regex_finder_pass():
    str_with_words = "This test will return words"
    pattern = ["test", "words", "void"]
    results = regex_finder(str_with_words, pattern)

    assert results == ['test', 'words']

def test_regex_finder_empty():
    text = "This test will be empty"
    pattern = ["no", "yes", "filler"]
    results = regex_finder(text, pattern)

    assert results == []

def test_regex_finder_multiple_words():
    text = "This will contain multiple words"
    pattern = ["yes", "contain multiple words"]
    results = regex_finder(text, pattern)
    assert results == ["contain multiple words"]