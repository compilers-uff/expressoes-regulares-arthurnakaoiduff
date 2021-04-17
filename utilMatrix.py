from util import *

def getMatrixElement(matrix, state1, state2):
  if state2 in list(matrix[state1]):
    return matrix[state1][state2]
  else:
    return matrix[state2][state1]

def setMatrixElement(matrix, state1, state2, value):
  if state2 in list(matrix[state1]):
    matrix[state1][state2] = value
  else:
    matrix[state2][state1] = value

  return matrix

def appendMatrixElement(matrix, state1, state2, value):
  if state2 in list(matrix[state1]):
    matrix[state1][state2].append(value)
  else:
    matrix[state2][state1].append(value)

  return matrix

def getMatrixElementFecho(matrix, state1, state2):
  if state1 in list(matrix):
    if state2 in list(matrix[state1]):
      return matrix[state1][state2]
  if state2 in list(matrix):
    if state1 in list(matrix[state2]):
      return matrix[state2][state1]

def getFecho(matrix, states, state):
  queue = [state]
  queueAlreadyVisited = []

  while(len(queue) > 0 and not isSublist(queue, queueAlreadyVisited)):
    actualState = queue.pop(0)
    queueAlreadyVisited.append(actualState)

    for eachState in states:
      if eachState != actualState:

        if not getMatrixElementFecho(matrix, actualState, eachState):
          if eachState not in queue and eachState not in queueAlreadyVisited:
            queue.append(eachState) 

  return queueAlreadyVisited