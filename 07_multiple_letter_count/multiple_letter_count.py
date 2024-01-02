def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    freq_dict = {}
    for x in phrase:
        if x in freq_dict:
            freq_dict[x] += 1
        else:
            freq_dict[x] = 1
    return freq_dict