# Example file for Advanced Python by Joe Marini
# Working with basic iterators

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# use regular interation over the days
for d in days:
    print(d)

# use iter() to create an iterator over a collection
# the next() function retrieves the next value from an iterator
week_days = iter(zip(days,daysFr))
try:
    print(next(week_days))
    print(next(week_days))
    print(next(week_days))
    print(next(week_days))
    print(next(week_days))
    print(next(week_days))
    print(next(week_days))
    print(next(week_days))
    print(next(week_days))
except StopIteration:
    pass


# iterate using a function and a sentinel
file_path = r"/workspaces/advanced-python-3912165/Start/2. Iterators/testfile.txt"
with open(file_path, 'r', newline='') as fp:
    for line in iter(fp.readline,''):
        print(line,sep='')