# Example file for Advanced Python by Joe Marini


# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# the enumerate function
for ind,day in enumerate(days):
  print(f'{day} -> {daysFr[ind]}')

for ind,day in enumerate(days,start=1):
  print(f'[{ind}] day')

# use zip to combine sequences
for en,fr in zip(days,daysFr):
  print(f'{en} -> {fr}')

# use enumerate and zip together
for ind, (en, fr) in enumerate(zip(days,daysFr),start=1):
  print(f'[{ind}] {en} -> {fr}')

# use zip_longest
import itertools

seq1 = ["A","B","C","D","E","F"]
seq2 = [1, 2, 3, 4]
seq3 = "xyz"
    
result = itertools.zip_longest(seq1,seq2,seq3,fillvalue='N/A')
print(list(result))