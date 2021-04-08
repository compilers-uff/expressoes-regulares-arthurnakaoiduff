from util import *
from utilTransiction import *
from Classes.afd import *

class Afn:
  def __init__(self, alphabet, states, transictionFunctions, initialState, finalStates):
    self.alphabet = alphabet
    self.states = states
    self.transictionFunctions = transictionFunctions
    self.initialState = initialState
    self.finalStates = finalStates

  def __str__(self):
    return (
      "Alfabeto: " 
      + str(self.alphabet) 
      + "\nEstados: " 
      + str(self.states) 
      + "\nTransições: " 
      + self.returnTransictionFunctionPrintable() 
      + "\nEstado Inicial: " 
      + str(self.initialState) 
      + "\nEstado Final: " 
      + str(self.finalStates) 
      + "\n"
    )

  def returnTransictionFunctionPrintable(self):
    string = "\n"
    for state in self.transictionFunctions.keys():
      string += state + "\n    "
      for transiction in self.transictionFunctions[state]:
        if transiction != self.transictionFunctions[state][-1]:
          string += transiction[0] + " -> " + str(transiction[1]) + "\n    "
        else:
          string += transiction[0] + " -> " + str(transiction[1]) + "\n"
    
    return string

  def compare(self, afn):
    if not equivalentLists(self.alphabet, afn.alphabet):
      return False
    
    if not equivalentLists(self.states, afn.states):
      return False

    if not compareTransictions(self.transictionFunctions, afn.transictionFunctions):
      return False

    if self.initialState != afn.initialState:
      return False

    if not equivalentLists(self.finalStates, afn.finalStates):
      return False

    return True

  def equivalentAfd(self):
    transictionFunctions = {}

    queue = [[self.initialState]]
    queueAlreadyProcessed = []

    while(len(queue) != 0 and not isSublist(queue, queueAlreadyProcessed)): # Enquanto nao esgotar a fila
      statesAfd = queue.pop(0) # Retira o primeiro elemento da fila
      queueAlreadyProcessed.append(statesAfd) # Adiciona o elemento que vai ser processado na fila de processados para nao repetir

      for letter in self.alphabet: # Para cada letra no alfabeto
        newStateArray = [] # Array para armazenar todos os estados que os estados atuais chegam
        for stateAfd in statesAfd: # Para cada estado 
          if(stateAfd in self.transictionFunctions.keys()): # Se o estado existe na AFN
            boolean, index = isThereTransiction(self.transictionFunctions[stateAfd], letter) # Descobre se ele tem uma transicao utilizando a letra que estamos percorrendo
            if boolean: # Se ele tem essa transicao
              for state in self.transictionFunctions[stateAfd][index][1]: # Para cada estado que ele consegue chegar
                if state not in newStateArray: # Se o estado ainda nao esta no array de estados alcancados
                  newStateArray.append(state) # Adiciona o estado ao array de estados alcancados
        
        if (len(newStateArray) != 0):
          if "".join(sorted(statesAfd)) in transictionFunctions.keys():
            transictionFunctions["".join(sorted(statesAfd))].append((letter, "".join(sorted(newStateArray))))
          else:
            transictionFunctions["".join(sorted(statesAfd))] = [(letter, "".join(sorted(newStateArray)))]
          
        if newStateArray not in queueAlreadyProcessed and newStateArray not in queue:
          queue.append(newStateArray) 

    states = []
    finalStates = []
    
    for i in range(1, len(self.states) + 1):
      combinations = combination(self.states, i)
      states += list(map(lambda state : "".join(sorted(state)), combinations))
      for arrayState in combinations:
        if hasAtLeastOneElement(arrayState, self.finalStates):
          finalStates.append("".join(sorted(arrayState)))

    return Afd(
      self.alphabet, 
      states, 
      transictionFunctions,
      self.initialState,
      finalStates
    )