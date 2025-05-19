import itertools

numbers_list = list(range(0,11))

# Creating a sum() function
def sum_numbers(accumulated_value, new_value):
  return accumulated_value + new_value

accumulated_values_list = list(itertools.accumulate(numbers_list, sum_numbers))
print(accumulated_values_list)


###########################################

numbers_list = [0,1,2,3,4,5,5,4,3,2,1,0]

# Return the greater value
def get_max_value(accumulated_value, new_value):
  return new_value if new_value > accumulated_value else accumulated_value

# Only return the maximum value
accumulated_values_list = list(itertools.accumulate(numbers_list, get_max_value))
print(accumulated_values_list)
