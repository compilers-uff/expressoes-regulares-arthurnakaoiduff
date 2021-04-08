import sys
from Classes.afne import *
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

if(sys.argv[1] == "-f"):
  filename = sys.argv[2]
  file = open(filename, 'r')
  ers = file.readlines()
  word = sys.argv[3]

else:
  ers = [sys.argv[1]]
  word = sys.argv[2]

# Tratando a expressao regular
for i in range(len(ers)):
  ers[i] = ers[i].replace(" ", "") # Retirando os espaços vazios
  ers[i] = ers[i].replace("\n", "") # Retirando as quebras de linha

for er in ers:
  if afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word):
    print("match(", er, ", '", word, "') == OK", sep="") 
  else: 
    print("match(", er, ", '", word, "') == Not OK", sep="") 
