def search4vowels(phrase: str) -> set:
    """Returns the set of vowels found in 'Phrase"."""
    return set ('aeiou').intersection(set(phrase))

def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Returns the set of 'letters' found in 'phrase'."""
    return set (letters).intersection (set(phrase))