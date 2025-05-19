# Example file for Advanced Python by Joe Marini
# Sequence comparisons

import itertools


# define some lists
seq1 = [1, 2, 3, 6, 10, 15, 34, 56]
seq2 = [1, 2, 5, 7, 9, 18, 22, 38, 91]

# define a tuple
seq3 = (1, 2, 3, 6, 10, 15, 34, 56)

# compare the sequences
print(seq1 == seq2)
print(seq1 > seq2)
print(seq1 < seq2)

print("*"*50)

# sequences that have equal values but different number of items:
seq4 = [10, 20, 30]
seq5 = [10, 20, 30, 40, 50]

print(seq5 > seq4)
print("*"*50)

# Sequences must be of the same type to be compared
print(seq1 == seq3)
print(tuple(seq1) == seq3)
print("*"*50)

# use the all() function to compare two arbitrary sequences
result = all(x == y for x,y in zip(seq1,seq3))
result = all(x == y for x,y in itertools.zip_longest(seq1,seq3))
print(result)