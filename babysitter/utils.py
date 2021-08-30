import re

def regex_finder(text: str, patterns: list) -> list:
    """
    used to search string if it contains patterns

    Arguments:

        string: string of text that is to be searched
        patterns: list of patterns to match

    Returns:
        list: if offending words were found, then list will contain offensive words
    """
    pattern_string = '|'.join(patterns)
    pattern_string = pattern_string.lower()

    text = text.lower()

    res = re.findall(pattern_string, text)
    return res
