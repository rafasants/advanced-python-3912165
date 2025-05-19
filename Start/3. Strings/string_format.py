# Example file for Advanced Python by Joe Marini
# Formatting output strings

# Basic formatting - center(), ljust(), rjust()
width = 40
print("center".center(width,'-'))
print("left".ljust(width,'-'))
print("right".rjust(width,'-'))

print('*'*50)
# Formatting strings with format specification codes
# Format spec is: [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["."precision][type]
val1 = 1234.5678
val2 = 10987.65
val3 = 12.99
val4 = -280.7

# Specify a precision and type
print(f"{val1:.2f}")  # 2 decimal places
print(f"{val2:.2e}")  # cientific notation
print(f"{val3:.2f}")      #
print(f"{val4:.2e}")      #
print('*'*50)

# Use alignment and width and leading zeros
# < is left align, > is right align, ^ is centered
print(f"{val1:_>50.2f}")  # Right Align, using '_' as the fill character
print(f"{val2:#<50.2e}")  # Left Align, using '#' as the fill character
print(f"{val3:-^50.2f}")  # Center Align, using '-' as the fill character
print(f"{1.1:>050.2f}")   # Right Align, using leading zeros
print(f"{1:02d}")         # Formats the number 1 as a zero-padded and 2-digit decimal integer
print('*'*50)

# Use a grouping option and +/- signs
print(f"{val1:^+50.2f}")  # Will always print either + or - sign in front of the number
print(f"{val2:^-50.2f}")  # Will only print the - sign in front of NEGATIVE numbers
print(f"{val3:^-50.2f}")  # Will only print the - sign in front of NEGATIVE numbers
print(f"{val4:^-50.2f}")  # Will only print the - sign in front of NEGATIVE numbers

# Grouping
print(f"{val2:<+50,.2f}")  # Thousands are separated bt the comma character.
print(f"{val2:<+50_.2f}")  # Thousands are separated bt the underscore character.

print('*'*50)

# Create format specifiers dynamically
width = 10
precision = 2

# With hardcoded value
format_spec = f"{123.456:{width}.{precision}f}"
print(format_spec)

# With dynamic value
format_spec = "{val:@^{width}.{precision}f}".format(val=val2, width=30, precision=2)
print(format_spec)