"""
Merge Sort
==========
Implementation of merge sort algorithm

Author:
=======
Suresh Sarda
"""
from unittest import TestCase


def merge_sorted_lists(l1, l2):
    if not l1:
        return l2

    if not l2:
        return l1

    assert len(l1) >= 1
    assert len(l2) >= 1

    l = []

    while l1 and l2:
        l.append(l1.pop(0) if l1[0] < l2[0] else l2.pop(0))

    if l1:
        assert not l2
        l.extend(l1)

    if l2:
        assert not l1
        l.extend(l2)

    return l


def merge_sort(l):
    if l == None:
        raise ValueError('NoneType attribute is not iterable')

    if (len(l)) <= 1:
        return l

    left = l[:len(l) / 2]
    right = l[len(l) / 2:]

    return merge_sorted_lists(merge_sort(left), merge_sort(right))


class TestMergeSort(TestCase):
    def test_sorted_empty_list_merging(self):
        """
        Test that when empty lists are returned, no exceptions are raised and an empty list is returned
        :return:
        """
        l1 = []
        l2 = []
        l = merge_sorted_lists(l1, l2)
        self.assertEqual(l, [])

    def test_sorted_list_are_merged_correctly(self):
        test_lists = [
            ([1, 2], [], [1, 2]),
            ([], [1, 2, 3], [1, 2, 3]),
            ([1], [1], [1, 1]),
            ([1], [2], [1, 2]),
            ([1], [2, 2], [1, 2, 2]),
            ([1, 3], [2, 2], [1, 2, 2, 3]),
            ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
            ([1, 4, 9], [3, 7, 8, 8, 9], [1, 3, 4, 7, 8, 8, 9, 9]),

        ]
        for l1, l2, result in test_lists:
            l = merge_sorted_lists(l1, l2)
            self.assertEqual(l, result)

    def test_merge_sort(self):

        test_cases = [
            [],
            [None],
            [2],
            [2, 5, 1, 0, 9, 11, 3],
            [2, 1, 1],
            [3, 4, 5],
            [3, 4, 5, 0],
            [0, 3, 3]
        ]
        for tc in test_cases:
            self.assertEqual(merge_sort(tc), sorted(tc))


if __name__ == '__main__':
    tc = TestMergeSort()
    tc.run()
