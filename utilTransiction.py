from util import *

def isThereTransiction(arrayTransictions, letter):
  for i, transiction in enumerate(arrayTransictions):
    if transiction[0] == letter:
      return (True, i)
  
  return (False, -1)

def compareTransictions(transictions1, transictions2):
  def transictionInTransictions(transiction, transictions):
    for t in transictions:
      if t[0] == transiction[0]:
        if not equivalentLists(t[1], transiction[1]):
          return False
    
    return True

  for state in transictions1.keys():
    for transiction1 in transictions1[state]:
      if state in transictions2:
        if not transictionInTransictions(transiction1, transictions2[state]):
          return False
      else:
        return False

  for state in transictions2.keys():
    for transiction2 in transictions2[state]:
      if state in transictions1:
        if not transictionInTransictions(transiction2, transictions1[state]):
          return False
      else:
        return False

  return True