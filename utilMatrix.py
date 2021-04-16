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