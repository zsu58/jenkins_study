import sys

def hello(name="World"):
  return f"Hello {name}!"

if __name__ == "__main__":
  if len(sys.argv) > 1:
    print(hello(sys.argv[1]))
  else:
    print(hello())