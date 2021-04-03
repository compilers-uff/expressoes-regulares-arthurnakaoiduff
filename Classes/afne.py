from Classes.afn import *
from util import *
from utilTransiction import *

class Afne:
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

  @staticmethod
  def getSimpleAfne(symbol):
    initialState = "q0"
    finalState = "qf"

    return Afne(
      [symbol], 
      [initialState, finalState], 
      {
        initialState: [(symbol, [finalState])]
      }, 
      initialState,
      [finalState]
    )


  @staticmethod
  def getUnionAfne(firstAfne, secondAfne):
    initialState = "q0"
    finalState = "qf"

    # Atualizando os estados das AFNEs para nao ter valores duplicados
    firstAfne.changeStates("0")
    secondAfne.changeStates("1")

    alphabet = firstAfne.alphabet

    # Adicionando apenas simbolos unicos ao alfabeto da Uniao
    for symbol in secondAfne.alphabet:
      if symbol not in alphabet:
        alphabet.append(symbol)
  
    # Adicionando os estados eliminando duplicidades de nome
    states = firstAfne.states + secondAfne.states
    states += [initialState, finalState]

    transictionFunctions = {}

    # Copiando transições da primeira AFNE
    for state in firstAfne.transictionFunctions.keys():
      transictionFunctions[state] = firstAfne.transictionFunctions[state]

    # Copiando transições da segunda AFNE
    for state in secondAfne.transictionFunctions.keys():
      transictionFunctions[state] = secondAfne.transictionFunctions[state]

    # Adicionando transições do estado inicial
    transictionFunctions[initialState] = [("EPSILON", [firstAfne.initialState, secondAfne.initialState])]

    # Adicionando transições para o estado final
    for finalStateFirstAfne in firstAfne.finalStates:
      transictionFunctions[finalStateFirstAfne] = [("EPSILON", [finalState])]

    for finalStateSecondAfne in secondAfne.finalStates:
      transictionFunctions[finalStateSecondAfne] = [("EPSILON", [finalState])]

    return Afne(
      alphabet, 
      states, 
      transictionFunctions, 
      initialState,
      [finalState]
    )

  @staticmethod
  def getConcatenationAfne(firstAfne, secondAfne):
    # Atualizando os estados das AFNEs para nao ter valores duplicados
    firstAfne.changeStates("0")
    secondAfne.changeStates("1")

    alphabet = firstAfne.alphabet

    # Adicionando apenas simbolos unicos ao alfabeto da Uniao
    for symbol in secondAfne.alphabet:
      if symbol not in alphabet:
        alphabet.append(symbol)
  
    # Adicionando os estados eliminando duplicidades de nome
    states = firstAfne.states + secondAfne.states

    transictionFunctions = {}

    # Copiando transições da primeira AFNE
    for state in firstAfne.transictionFunctions.keys():
      transictionFunctions[state] = firstAfne.transictionFunctions[state]

    # Copiando transições da segunda AFNE
    for state in secondAfne.transictionFunctions.keys():
      transictionFunctions[state] = secondAfne.transictionFunctions[state]

    # Adicionando transições entre as AFNEs
    for finalState in firstAfne.finalStates:
      transictionFunctions[finalState] = [("EPSILON", [secondAfne.initialState])]

    return Afne(
      alphabet, 
      states, 
      transictionFunctions, 
      firstAfne.initialState,
      secondAfne.finalStates
    )

  @staticmethod
  def getSuccessiveConcatenationAfne(afne):
    initialState = "q0"
    finalState = "qf"

    # Atualizando os estados das AFNEs para nao ter valores duplicados
    afne.changeStates("0")

    # Adicionando o alfabeto
    alphabet = afne.alphabet

    # Adicionando os estados
    states = afne.states
    states += [initialState, finalState]

    transictionFunctions = {}

    # Copiando transições da AFNE
    for state in afne.transictionFunctions.keys():
      transictionFunctions[state] = afne.transictionFunctions[state]

    # Adicionando transições do estado inicial
    transictionFunctions[initialState] = [("EPSILON", [afne.initialState, finalState])]

    # Adicionando transições do estado final da AFNE que sera sucessivamente concatenada
    for finalStateAfne in afne.finalStates:
      transictionFunctions[finalStateAfne] = [("EPSILON", [finalState, afne.initialState])]

    return Afne(
      alphabet, 
      states, 
      transictionFunctions, 
      initialState,
      [finalState]
    )

  def changeStates(self, stringConcat):
    transictionFunctions = {}
    for state in self.transictionFunctions.keys():
      arrayTransictions = []
      for transiction in self.transictionFunctions[state]:
        arrayTransictions.append((transiction[0], list(map(lambda x: x + stringConcat, transiction[1]))))
      transictionFunctions[state + stringConcat] = arrayTransictions

    self.states = list(map(lambda x: x + stringConcat, self.states))
    self.transictionFunctions = transictionFunctions
    self.initialState = self.initialState + stringConcat
    self.finalStates = list(map(lambda x: x + stringConcat, self.finalStates))

  def fechoEpsilon(self, startState):
    queue = [startState]
    alreadyVisited = []

    while(len(queue) != 0 and not isSublist(queue, alreadyVisited)):
      state = queue.pop(0)
      alreadyVisited.append(state)

      queue += [state for state in self.epsilonTransiction(state) if state not in queue and state not in alreadyVisited]
      alreadyVisited += [state for state in self.epsilonTransiction(state) if state not in queue and state not in alreadyVisited]

    return alreadyVisited

  def fechoEpsilonStates(self, states):
    returnStates = []
    
    for state in states:
      for stateFechoEpsilon in self.fechoEpsilon(state):
        if stateFechoEpsilon not in returnStates:
          returnStates.append(stateFechoEpsilon)

    return returnStates

  def epsilonTransiction(self, state):
    if state in self.transictionFunctions.keys():
      for transiction in self.transictionFunctions[state]:
          if transiction[0] == "EPSILON":
            if state not in transiction[1]:
              return transiction[1] + [state]
            else:
              return transiction[1]

    return [state]

  def sigma(self, state, letter):
    if state in self.transictionFunctions.keys():
      for transiction in self.transictionFunctions[state]:
        if transiction[0] == letter:
          return transiction[1]
    return []

  # word é um array para garantir que o simbolo EPSILON seja lido corretamente
  def sigmaExtended(self, states, word):
    if len(word) == 0:
      return self.fechoEpsilonStates(states)
    else:
      lastLetter = word.pop()
      s = self.sigmaExtended(states, word)
      auxStates = []
      for ss in s:
        auxStates += self.sigma(ss, lastLetter)
      return self.fechoEpsilonStates(auxStates)

  # Função que gera um AFN a partir de uma AFNE
  def equivalentAfn(self):
    finalStates = []
    for state in self.states:
      if len(intersection(self.fechoEpsilon(state), self.finalStates)) != 0:
        finalStates.append(state)

    transictionFunctions = {}
    for state in self.transictionFunctions.keys():
      transictionFunctions[state] = []
      for transiction in self.transictionFunctions[state]:
        states = self.sigmaExtended([state], [transiction[0]])
        if transiction[0] == "EPSILON":
          for letter in self.alphabet:
            alreadyExistsTransiction = isThereTransiction(transictionFunctions[state], letter)
            if alreadyExistsTransiction[0]:
              transictionFunctions[state][alreadyExistsTransiction[1]] = (transictionFunctions[state][alreadyExistsTransiction[1]][0], set(transictionFunctions[state][alreadyExistsTransiction[1]][1] + states))
            else:
              transictionFunctions[state].append((letter, states))
        else:
          alreadyExistsTransiction = isThereTransiction(transictionFunctions[state], transiction[0])
          if alreadyExistsTransiction[0]:
            transictionFunctions[state][alreadyExistsTransiction[1]] = (transiction[0], states)
          else:
            transictionFunctions[state].append((transiction[0], states))

    return Afn(
      self.alphabet, 
      self.states, 
      transictionFunctions,
      self.initialState,
      finalStates
    )

  # Funcao que compara duas AFNEs
  def compare(self, afne):
    if not equivalentLists(self.alphabet, afne.alphabet):
      return False
    
    if not equivalentLists(self.states, afne.states):
      return False

    if not compareTransictions(self.transictionFunctions, afne.transictionFunctions):
      return False

    if self.initialState != afne.initialState:
      return False

    if not equivalentLists(self.finalStates, afne.finalStates):
      return False

    return True