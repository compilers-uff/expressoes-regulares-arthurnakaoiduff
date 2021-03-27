from Classes.afne import *

class Er:
  def __init__(self, queue):
    self.queue = queue

  def transformAfne(self, value):
    if value == "*":
      return Afne.getSuccessiveConcatenationAfne(self.transformAfne(self.queue.pop(0)))
      
    elif value == ".":
      return Afne.getConcatenationAfne(self.transformAfne(self.queue.pop(0)), self.transformAfne(self.queue.pop(0)))

    elif value == "+":
      return Afne.getUnionAfne(self.transformAfne(self.queue.pop(0)), self.transformAfne(self.queue.pop(0)))

    else:
      return Afne.getSimpleAfne(value)

  def getEr(erString):
    queue = []
    erList = list(erString)
    while(len(erList) != 0):
      symbol = erList.pop(0)

      if symbol == "*":
        queue.append(symbol)
      elif symbol == "+" or symbol == ".":
        queue.append(symbol)
      elif symbol == "(":
        pass
      elif symbol == ")":
        pass
      elif symbol == ",":
        pass
      else:
        queue.append(symbol)

    return Er(queue)