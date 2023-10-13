#!/usr/bin/python3
def roman_to_int(roman_string):
    """Convert roman numbers to integer"""
    num = 0

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    ro_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    size = len(roman_string)
    rnum = roman_string

    for idx in range(size):
        if ro_dict.get(rnum[idx], 0) == 0:
            return 0

        if (size - 1) != idx and ro_dict[rnum[idx + 1]] > ro_dict[rnum[idx]]:
            num += ro_dict[roman_string[idx]] * -1
        else:
            num += ro_dict[roman_string[idx]]

    return num
