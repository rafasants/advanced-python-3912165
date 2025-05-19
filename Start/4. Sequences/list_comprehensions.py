# Example file for Advanced Python by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Perform a mapping and filter function on a list using built-in functions
evenSquared = list(map(lambda e: e**2, filter(lambda e: e>4 and e<16, evens)))
print(evenSquared)

# Derive a new list of numbers frm a given list
evenSquared = [e**2 for e in evens if e>4 and e<16]
print(evenSquared)