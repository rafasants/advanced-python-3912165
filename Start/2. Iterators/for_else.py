# Example file for Advanced Python by Joe Marini
# The for-else loop construct

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# The else clause on a for loop is only executed if the loop completes every iteration
def findname(target):
    for name in names:
        if name == target:
            print("Name found");
            return True
    
    print("Name not found")
    return False

print(findname("Creed"))
print(findname("Tom"))

# Check if a number is prime
def is_prime(number: int) -> bool:

    for i in range (2, number):
        if number % i == 0:
            print(f"{number} is NOT a prime number. ({number} % {i} = {int(number/i)})")
            return False
    print(f"{number} is a prime number")
    return True

is_prime(33)