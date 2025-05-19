# Example file for Advanced Python by Joe Marini
# Sequences and slicing

from collections import deque

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# assigning sequences
new_names = ["Rafael", "Andy", "Angela", "Stanley"]
names[1:5] = new_names
print(names)

# the del operator works with slices
del names[4:6]
print(names)


# not all sequence types support slicing, however
deque_names = deque(["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"])
