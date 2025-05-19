# Example file for Advanced Python by Joe Marini


sample_text = "# The quick brown fox jumps over the lazy dog."

# Using find() to find the first occurrence of a substring
print(f"First occurrence of 'the':", sample_text.find("the"))
print(f"First occurrence of 'The':", sample_text.find("The"))

# Example with optional start and end parameters
print(f"First occurrence of 'brown':", sample_text.find("brown",16,100)) # -1 = Not found
print(f"First occurrence of '#':", sample_text.find("#",0,1))

print("*"*50)
# Using index() to find the first occurrence of a substring (raises ValueError if not found)
try:
  print(f"First occurrence of '!':", sample_text.index("!"))
except ValueError:
  print("'!' was not found")
print("*"*50)

# The 'in' operator can be used for Boolean testing:
print(f"Is 'fox' present: {'fox' in sample_text}")
print("*"*50)
# Using rfind() to find the last occurrence of a substring
print(f"Last occurrence of 'the': {sample_text.rfind('the')}")
print("*"*50)
# Using rindex() to find the last occurrence of a substring (raises ValueError if not found)
print(f"Last occurrence of 'jump': {sample_text.rindex('jump')}")
print("*"*50)
# The replace() function will find content in the string and replace it
modified_sample_text = sample_text.replace("lazy", "tired")
print(modified_sample_text)
print("*"*50)