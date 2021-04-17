from Classes.er import *

def erToAFNe(er):
  erInstance = Er.getEr(er)
  return erInstance.equivalentAfne(erInstance.queue.pop(0))

def afneToAFN(Afne):
  return Afne.equivalentAfn()

def afnToAFD(Afn):
  return Afn.equivalentAfd()

def afdToAFDmin(Afd):
  return Afd.minimize()

def match(er, w):
  er_treatted = er.replace(" ", "") # Retirando os espaços vazios
  er_treatted = er_treatted.replace("\n", "") # Retirando as quebras de linha
  er_treatted = er_treatted.replace("'", "") # Retirando as aspas simples
  return afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er_treatted)))).accepted(w)