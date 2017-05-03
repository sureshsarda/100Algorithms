"""
Problem Statement
=================

Given a string of 1s and 0s, find the longest sub-string of 1s

Algorithm
=========

Every time we encounter a 1 while traversing the string, start measuring it. Once it is over (0 is found) reset current
values and if this length was greater than the already we found then update the max length found. Otherwise discard
current results


Complexity
==========
O(n)

__author__: Suresh Sarda

"""


def max_sequence(l):
    """
    Find longest sub-sequence of 1s in the given string. 
    :param l: list of 1s and 0s
    :return: length of sequence, start position 
    """

    # Store the max start and length found till now
    max_start = 0
    max_length = 0

    # Store values for current string we are considering
    current_length = 0
    current_start = 0

    l = l + '0'  # To terminate, or we will have to add a if condition after loop
    for index, val in enumerate(l):
        if val == '1':
            if current_length == 0:
                # The first 1 in a new sequence
                current_start = index
            current_length += 1
        else:
            if current_length > max_length:
                # Update max_length and it's start value
                max_length = current_length
                max_start = current_start

            # Reset current for next substring
            current_length = 0
            current_start = 0

    return max_length, max_start


if __name__ == '__main__':
    seq = '101010'
    length, start = max_sequence(seq)
    assert length == 1 and start == 0

    seq = '101011'
    length, start = max_sequence(seq)
    assert length == 2 and start == 4

    seq = ''
    length, start = max_sequence(seq)
    assert length == 0 and start == 0

    seq = '1'
    length, start = max_sequence(seq)
    assert length == 1 and start == 0

    seq = '111'
    length, start = max_sequence(seq)
    assert length == 3 and start == 0

    seq = '1100110011'
    length, start = max_sequence(seq)
    assert length == 2 and start == 0

    seq = '1111001010111010011111000'
    length, start = max_sequence(seq)
    assert length == 5 and start == 17
