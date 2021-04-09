from util import *
from utilTransiction import *
from utilMatrix import *

class Afd:
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

  def compare(self, afd):
    if not equivalentLists(self.alphabet, afd.alphabet):
      return False
    
    if not equivalentLists(self.states, afd.states):
      return False

    if not compareTransictions(self.transictionFunctions, afd.transictionFunctions):
      return False

    if self.initialState != afd.initialState:
      return False

    if not equivalentLists(self.finalStates, afd.finalStates):
      return False

    return True
  
  def minimize(self):
    # Garantindo pre requisitos
    self.minimizePrerequisiteInaccessibleStates()
    self.minimizePrerequisiteTransformTransictionFunctionsInTotal()

    # Construir tabela (matriz) de estados
    matrix = {}
    matrixList = {}

    for i in range(1, len(self.states)):
      for j in range(0, i):
        if self.states[i] not in list(matrix):
          matrix[self.states[i]] = {self.states[j]: False}
          matrixList[self.states[i]] = {self.states[j]: []}
        else:
          matrix[self.states[i]][self.states[j]] = False
          matrixList[self.states[i]][self.states[j]] = []

    # Marcar estados do tipo { final, nao final }
    for i in range(1, len(self.states)):
      for j in range(0, i):
        if ((self.states[i] in self.finalStates) != (self.states[j] in self.finalStates)): # Se um dos estados eh final e o outro nao
          setMatrixElement(matrix, self.states[i], self.states[j], True)

    # Marcar estados nao equivalentes
    for i in range(1, len(self.states)):
      for j in range(0, i):
        state1 = self.states[i]
        state2 = self.states[j]
        if matrix[state1][state2] == False:
          for letter in self.alphabet:
            isThereTransiction1 = isThereTransiction(self.transictionFunctions[state1], letter)
            isThereTransiction2 = isThereTransiction(self.transictionFunctions[state2], letter)
            transiction1 = self.transictionFunctions[state1][isThereTransiction1[1]]
            transiction2 = self.transictionFunctions[state2][isThereTransiction2[1]]
            
            #Condicoes
            if transiction1[1][0] != transiction2[1][0]: # Se os estados alvos das transicoes sao diferentes, entao...
              if getMatrixElement(matrix, transiction1[1][0], transiction2[1][0]) == False: # Se o par de transicoes nao estao marcados...
                appendMatrixElement(matrixList, transiction1[1][0], transiction2[1][0], (state1, state2))
              else: # Se as transicoes estao marcadas, entao deve-se marcar os estados em questao, pois nao sao equivalentes
                setMatrixElement(matrix, state1, state2, True)
                
                # Marcar pares que estao na lista...
                queue = [] + getMatrixElement(matrixList, state1, state2)
                queueAlreadyVisited = []

                while(len(queue) > 0 and not isSublist(queue, queueAlreadyVisited)):
                  pair = queue.pop(0)
                  queueAlreadyVisited.append(pair)

                  if getMatrixElement(matrix, pair[0], pair[1]) == False:
                    setMatrixElement(matrix, pair[0], pair[1], True)
                    queue += [pair for pair in getMatrixElement(matrixList, pair[0], pair[1]) if pair not in queue and pair not in queueAlreadyVisited]



            # Se as transicoes sao iguais, entao eles sao equivalentes e nao devem ser marcados

    # Unificacao dos estados equivalentes
    changeElements = []
    for i in range(1, len(self.states)):
      for j in range(0, i):
        if getMatrixElement(matrix, self.states[i], self.states[j]) == False:
          newNameState = self.states[i] + self.states[j]

          self.transictionFunctions[newNameState] = self.transictionFunctions[self.states[i]] # Adicionando nova transicao com o novo estado
          self.states.append(newNameState) # Adicionando o novo estado aos estados

          # Para toda transicao que tenha os estados substituidos como "alvo", substituir para o novo nome do estado
          for state in self.transictionFunctions.keys():
            self.transictionFunctions[state] = [(transiction1, [newNameState]) if transiction2[0] == self.states[i] or transiction2[0] == self.states[j] else (transiction1, transiction2) for transiction1, transiction2 in self.transictionFunctions[state]]

          # Adicionando elementos para serem apagados depois...
          changeElements.append((self.states[i], self.states[j], newNameState))

          if self.states[i] in self.finalStates and self.states[j] in self.finalStates: # Se os estados são finais
            self.finalStates.append(newNameState)

          if self.initialState == self.states[i] or self.initialState == self.states[j]: # Se algum dos estados é inicial
            self.initialState = newNameState

    for element in changeElements:
      if element[0] in self.transictionFunctions.keys(): 
        del self.transictionFunctions[element[0]] 
      if element[1] in self.transictionFunctions.keys():
        del self.transictionFunctions[element[1]] 
      if element[0] in self.states:
        self.states.remove(element[0]) 
      if element[1] in self.states:
        self.states.remove(element[1]) 
      if element[0] in self.finalStates:
        self.finalStates.remove(element[0]) 
      if element[1] in self.finalStates:
        self.finalStates.remove(element[1]) 
    
    # Descobrindo estados inuteis
    statesNotUseless = []

    for state in self.states:
      queue = [state]
      queueAlreadyVisited = []
      if state in self.finalStates:
        isUseless = False
        statesNotUseless.append(state)
      else:
        isUseless = True

      while(len(queue) > 0 and not isSublist(queue, queueAlreadyVisited) and isUseless):
        stateVisiting = queue.pop(0)
        queueAlreadyVisited.append(stateVisiting)

        if stateVisiting in statesNotUseless:
          break

        for transiction in self.transictionFunctions[stateVisiting]:
          if transiction[1][0] in self.finalStates:
            if state not in statesNotUseless:
              statesNotUseless.append(state) 
            isUseless = False
            break
          else:
            if transiction[1][0] not in queue and transiction[1][0] not in queueAlreadyVisited:
              queue.append(transiction[1][0])
    
    uselessStates = [state for state in self.states if state not in statesNotUseless]

    # Removendo estados inuteis
    self.states = [state for state in self.states if state not in uselessStates]

    for uselessState in uselessStates:
      del self.transictionFunctions[uselessState]

    for state in list(self.transictionFunctions)[:]:
      for transiction in self.transictionFunctions[state][:]:
        if transiction[1][0] in uselessStates:
          self.transictionFunctions[state].remove(transiction)
          if len(self.transictionFunctions[state]) == 0:
            del self.transictionFunctions[state]

    return self

  def minimizePrerequisiteInaccessibleStates(self):
    queue = [self.initialState]
    queueAlreadyVisited = []

    # Descobrindo os estados inacessiveis
    while(len(queue) > 0 and not isSublist(queue, queueAlreadyVisited)):
      state = queue.pop(0) # Retirando um estado da fila para fazer a leitura
      queueAlreadyVisited.append(state) # Adicionando estados na lista dos ja visitados

      if state in self.transictionFunctions.keys():
        for transiction in self.transictionFunctions[state]:
          if transiction[1][0] not in queue and transiction[1][0] not in queueAlreadyVisited:
            queue.append(transiction[1][0])
    
    inaccessibleStates = [state for state in self.states if state not in queueAlreadyVisited]
    
    # Apagando os estados inacessiveis das funcoes de transicao
    for state in list(self.transictionFunctions): # Para cada estado que esteja nas funcoes de transicao
      if state in inaccessibleStates: # Se a funcao de transicao visitada eh inacessivel
        del self.transictionFunctions[state]
      else: # Se a funcao de transicao visitada NAO eh inacessivel, deve-se percorrer se ela tem alguma transicao para outro estado inacessivel
        for transiction in self.transictionFunctions[state][:]: # Para cada transicao no estado
          if transiction[1][0] in inaccessibleStates: # Se o estado da transicao eh inacessivel
            if len(self.transictionFunctions[state]) == 1:
              del self.transictionFunctions[state]
            else:
              self.transictionFunctions[state].remove(transiction)


    # Apagando os estados inacessiveis dos estados
    self.states = [state for state in self.states if state not in inaccessibleStates]

    # Apagando os estados inacessiveis dos estados finais
    self.finalStates = [finalState for finalState in self.finalStates if finalState not in inaccessibleStates]

    return self
  
  def minimizePrerequisiteTransformTransictionFunctionsInTotal(self):
    # Adicionando o estado nao final "d"
    self.states.append("d")

    # Incluindo transicoes nao previstas para "d"
    for state in self.states:
      if state in self.transictionFunctions.keys():
        for letter in self.alphabet:
          if not isThereTransiction(self.transictionFunctions[state], letter)[0]:
            self.transictionFunctions[state].append((letter, ["d"]))
      else:
        self.transictionFunctions[state] = [(letter, ["d"]) for letter in self.alphabet]

    # Para todas as letras do alfabeto, gerar uma transicao para o proprio "d"
    self.transictionFunctions["d"] = [(letter, ["d"]) for letter in self.alphabet]

    return self

  def accepted(self, word):
    word = list(word)
    state = self.initialState

    while(len(word) > 0 and state != None):
      letter = word.pop(0)

      if state in self.transictionFunctions.keys():
        itTransiction = isThereTransiction(self.transictionFunctions[state], letter)
        if itTransiction[0]:
          state = self.transictionFunctions[state][itTransiction[1]][1][0]
        else:
          state = None
      else:
        state = None

    if state in self.finalStates and len(word) == 0:
      return True
    else:
      return False