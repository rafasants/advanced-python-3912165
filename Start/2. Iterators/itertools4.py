# Example file for Advanced Python by Joe Marini
# Itertools: combinations and permutations

import itertools


# product() produces the cartesian product of input iterables
cards = "A23456789TJQK"
suits = "SCHD"

# Without product()
deck = []
for c in cards:
  for s in suits:
    deck.append((c,s))
print(len(deck), "Cards.")
print(deck)

# With product()
deck = list(itertools.product(cards, suits))
print(len(deck), "Cards.")
print(deck)

# permutations() creates tuples of a given length with no repeated elements
teams = ("A","B","C","D")

# Without permutations()
# Each Team will play twice
result = []
for t in teams:
  for o in teams:
    if t != o:
      result.append((t,o))

print(len(result), "Games")
print(result)

# With permutations()
result = list(itertools.permutations(teams, 2))
print(len(result), "Games")
print(result)

# combinations() will create combinations of a given length with no repeats
# the order of the elements does not matter, even if the order differs, the combination will be considered repeated.
c = list(itertools.combinations(teams,3))
print("Possible combinations (without repeating elements):")
print(c)

# combinations_with_replacement() will create combinations of a given length with repeats
# Allow repeats
cwr = list(itertools.combinations_with_replacement(teams, 3))
print("Possible combinations (repeating elements):")
print(cwr)