from pycounts_tf import pycounts_tf
from collections import Counter
import os

def test_count_words():
    '''Test word counting from a file.'''
    a=os.getcwd()

    expected = Counter({'insanity':1, 'is':1, 'doing': 1,
                        'the': 1, 'same': 1, 'thing': 1,
                        'over': 2, 'and': 2, 'expecting':1,
                        'different': 1, 'results': 1})
    actual = pycounts_tf.count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"





