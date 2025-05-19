from typing import List, Any
from itertools import accumulate, chain, takewhile, dropwhile

def find_largest(numbers: List[List[int]]) -> int:
    """Returns the largest number of all lists

    Args:
    -----
        numbers (List[List[int]]): List of lists of integers
    Returns:
    --------
        int: The Largest Number  
    
    """
    # Create a single list
    single_list: List[Any] = list(chain(*numbers))
    # OR
    single_list: List[Any] = list(chain.from_iterable(numbers))

    # Get the largest number
    x: List[Any] = list(accumulate(single_list,max))
    # OR
    x = max(single_list)

    return x[-1] if isinstance(x, list) else x