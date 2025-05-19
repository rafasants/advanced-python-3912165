# Example file for Advanced Python by Joe Marini
# Itertools: chain, chain.from_iterable

import itertools


# chain() creates a single iterable from multiple
x = itertools.chain(["ABC"], '123', '!@#')
for ind, item in enumerate(x,start=1):
  print(f"[{ind}]: {item}") 

# make a prepend function
def prepend(value_to_prepend, iterable):
  return itertools.chain([value_to_prepend], iterable)

for ind, item in enumerate(prepend("Xyz!", "Bcde"),start=1):
  print(f"[{ind}]: {item}") 

# chain.from_iterable is an alternate usage of chain
s1 = "ABCDEFG"
s2 = [1,2,3,4,5]
s3 = ['$','%','@','&']

result = itertools.chain.from_iterable([s1,s2,s3])
for ind, item in enumerate(result,start=1):
  print(f"[{ind}]: {item}") 

