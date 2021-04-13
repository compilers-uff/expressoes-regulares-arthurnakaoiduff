import sys
from mainFunctions import *

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
