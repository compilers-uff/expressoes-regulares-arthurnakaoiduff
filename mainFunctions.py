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