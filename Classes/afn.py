from util import *
from utilTransiction import *

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