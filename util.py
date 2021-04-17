def intersection(list1, list2):
  return [value for value in list1 if value in list2]

def equivalentLists(list1, list2):
  for value in list1:
    if value not in list2:
      return False

  for value in list2:
    if value not in list1:
      return False

  return True

def isSublist(list1, list2):
  for value in list1:
    if value not in list2:
      return False

  return True

def hasAtLeastOneElement(list1, list2):
  for value in list1:
    if value in list2:
      return True
      
  return False