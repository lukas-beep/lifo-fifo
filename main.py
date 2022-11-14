class LIFO:

  def __init__(self, stack=[]):
    self.stack = stack

  def push_(self, element):
    self.stack.append(element)
    print(self.stack)

  def pop_(self):
    if self.stack != []:
      element = self.stack.pop()
      print(element, "was removed")
      print(self.stack)
      return element
    else:
      print("empty")

  def peek(self):
    if self.stack != []:
      print("\n|-----|")
      for i in self.stack[::-1]:
        print(f"""|  {i}  |
|-----|""")
      print("\n")


class FIFO:

  def __init__(self, stack=[]):
    self.stack = stack

  def push_(self, element):
    self.stack.insert(0, element)
    print(self.stack)

  def pop_(self):
    if self.stack != []:
      element = self.stack.pop()
      print(element, "was removed")
      print(self.stack)
      return element
    else:
      print("empty")

  def peek(self):
    if self.stack != []:
      print("|-----|")
      for i in self.stack[::-1]:
        print(f"""|  {i}  |
|-----|""")


def lifo():
  l = LIFO()
  while 1:
    func = input("do lifo: ")
    f = func.split(" ")
    if f[0] == "p":
      l.push_(f[1])
    elif f[0] == "r":
      l.pop_()
    elif f[0] == "q":
      break
    l.peek()

  print(l.stack)


def fifo():
  l = FIFO()
  while 1:
    func = input("do fifo: ")
    f = func.split(" ")
    if f[0] == "p":
      l.push_(f[1])
    elif f[0] == "r":
      l.pop_()
    elif f[0] == "q":
      break
    l.peek()

  print(l.stack)


lifo()
print("-" * 10)
fifo()
