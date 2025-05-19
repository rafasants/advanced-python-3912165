
def print_special_names():

  # __name__ is the name of the module
  print("Module name:", __name__)

  # __file__ contains the path to the file from which the module was loaded
  print("File Path:", __file__)

  # __package__ indicates the package that the module belongs to.
  print("Package:", __package__)

if __name__ == "__main__":
  print("This code is being run directly.")
  print_special_names()