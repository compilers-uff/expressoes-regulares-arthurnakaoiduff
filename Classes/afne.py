"""
Afne(
  [self.firstValue, self.secondValue], 
  ["q0", "q1", "q2", "qf"], 
  {
    "q0": [("a", ["q1", "q2"]), ("b", ["q3"])], 
    "q1": [("EPSILON", ["q2"])],
    "q2": [(self.secondValue, ["qf"])]
  }, 
  "q0",
  ["qf"]
)
"""

class Afne:
  def __init__(self, alphabet, states, transictionFunctions, initialState, finalStates):
    self.alphabet = alphabet
    self.states = states
    self.transictionFunctions = transictionFunctions
    self.initialState = initialState
    self.finalStates = finalStates

  def __str__(self):
    return "Alfabeto: " + str(self.alphabet) + "\nEstados: " + str(self.states) + "\nTransições: " + str(self.transictionFunctions) + "\nEstado Inicial: " + str(self.initialState) + "\nEstado Final: " + str(self.finalStates) + "\n"

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
