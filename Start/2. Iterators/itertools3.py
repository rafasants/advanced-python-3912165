# Example file for Advanced Python by Joe Marini
# Itertools: dropwhile, takewhile, filterfalse

import itertools
import pprint
from dataclasses import dataclass


vals = [10, 20, 30, 40, 50, 40, 30, 25, 55, 45, 40, 30]

# dropwhile and takewhile will return values until
# a certain condition is met that stops them


# dropwhile() drops values until the predicate expression is True
# It will only start including the values once the expression evaluates to True for the first time.
# The expression is only triggered once!
testFunction = lambda x: x < 45
dw = itertools.dropwhile(testFunction,vals)
print(f'The first number will be greater than 45: {list(dw)}')

# takewhile() is the opposite of dropwhile() - it returns values from
# the iterable while the predicate is True, then stops
# It keeps including the values until the expression evaluates to True.
# Only triggered once
# Stops including the values when the expression/function returns False
tw = itertools.takewhile(testFunction,vals)
print(f'The Last number will be less than 45: {list(tw)}')

# filterfalse() returns elements from the iterable for which the predicate
# function returns False. 
evaluate = lambda x: x <= 5
ff = itertools.filterfalse(evaluate,[1,2,3,4,5,6,7,8,9,10,5])
print(f"Greater than 5:",*ff)

is_even = lambda n: n%2 != 0 
ff = itertools.filterfalse(is_even,[1,2,3,4,5,6,7,8,9,10,5,6])
print(f"Even Numbers:",*ff)

# These functions can work on complex objects
@dataclass
class wcdata:
    game: str
    attendance: int
    team1: str
    team2: str
    score: str

worldcupdata = [
    wcdata("Final", 88966, "Argentina" , "France" , "3 (4) -- 3 (2)" ),
    wcdata("3rd Place", 44137, "Croatia" , "Morocco" , "2 -- 1" ),
    wcdata("Semifinal", 68294, "France" , "Morocco" , "2 -- 0" ),
    wcdata("Semifinal", 88966, "Argentina" , "Croatia" , "3 -- 0" ),
]

# Filter out games which attendance less than 80000
games = itertools.filterfalse(lambda g: g.attendance < 80000, worldcupdata)
pprint.pp(list(games))