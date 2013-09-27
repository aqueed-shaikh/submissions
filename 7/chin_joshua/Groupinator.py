from collections import namedtuple
from csv import reader
from functools import partial
from itertools import chain, groupby, zip_longest
from random import shuffle

_Student=namedtuple('Student','section, period, last, first')

def groupinator(filename, groupsize=4):
    with open(filename) as csvfile:
        return _format(chain.from_iterable(_groupAll(groupsize, _shuffleAll(_partition(_parse(csvfile))))))

def _parse(iterable):
    return map(_Student._make,reader(iterable))

def _partition(iterable):
    return map(lambda x:x[1], groupby(iterable, lambda student:student.period))

def _shuffleAll(iterable):
    return map(_shuffle, iterable)

def _shuffle(sequence):
    x=list(sequence)
    shuffle(x)
    return x

def _groupAll(n, iterable, fillvalue=None):
    return map(partial(_group, n), iterable)

def _group(n, iterable, fillvalue=None):
    return zip_longest(fillvalue=fillvalue, *([iter(iterable)] * n))

def _format(sequence):
    return "".join(chain.from_iterable(_formatGroup(*group) for group in enumerate(sequence,1)))

def _formatGroup(group,students):
    return ("%i,%s,%s\n"%(group,student.last,student.first) for student in students)
