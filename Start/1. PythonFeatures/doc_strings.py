def say_hello(name: str = None) -> str:
  """Prints a greeting message.

    Args:
        name (str, optional): The name to greet. If None, a generic greeting is used.

    Returns:
        None
  """
  return f'Hello {name}' if name else f'Hello World!'

def main():
  greetings = say_hello(name="Rafael")
  print(greetings)
  print("say_hello doc:")
  print(say_hello.__doc__)


main()