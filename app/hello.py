import sys

def hello(name="World"):
  return f"Hello {name}!"

if __name__ == "__main__":
  print(hello(sys.argv[1]))