# Example file for Advanced Python by Joe Marini
# Itertools: count, cycle, accumulate


import itertools

names = ["Joe", "Jane", "Jim"]

# cycle iterator can be used to cycle over a collection infinitely
cycler = itertools.cycle(names)
max_loop = 10
for ind,_ in enumerate(range(max_loop),start=1):
  value = next(cycler)
  print(f'[{ind}] Name: {value}')

# use count to create a simple counter
my_counter = itertools.count(100,10)

print(next(my_counter))
print(next(my_counter))
print(next(my_counter))
print(next(my_counter))

# accumulate creates an iterator that accumulates values
vals = [10,20,30,40,50,40,30]
my_accum = itertools.accumulate(vals)
print(list(my_accum))

# Passing the max function as argument to stop accumulating when it reaches the maximum value
my_accum_limit_50 = itertools.accumulate(vals, max)
print(list(my_accum_limit_50))

# amortize a loan over a set number of payments for a 2000 loan at 4%
payments = [100, 125, 200, 105, 100, 120, 110, 130, 150, 100, 110, 120]
interest_rate = 1.04
update = lambda balance,payment: round(balance * interest_rate) - payment
balances = itertools.accumulate(payments, update, initial=2_000)
print(list(balances))


# 2000 + 4% = 2080 - 100 = 1980
# 1980 + 4% = 2059 - 125 = 1934
# 1934 + 4% = 2011 - 200 = 1811
# ...
