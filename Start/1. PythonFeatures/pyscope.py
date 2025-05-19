# Example file for Advanced Python by Joe Marini
# Understanding Python scope
from typing import Callable
from functools import wraps

# declare a variable within the global scope
x = 1

# define a local function with a variable "x"
def dummy_function() -> None:
  """Changes and prints the value of the global variable 'x'.

    Returns:
        None
    """
  global x
  x = 255
  print(x)

# Run the test function and observe the two results
dummy_function()
print(x)

x += 5
print(x)
dummy_function()

# Nested functions create inner scopes. These are called closures:
def multiplier_make(factor: int) -> Callable:

  def _multiplier_maker(number: int) -> int:
    return factor * number
  return _multiplier_maker

doubler = multiplier_make(factor=2)
tripler = multiplier_make(factor=3)

print(doubler(100))
print(tripler(25))