import sys
from Classes.afne import *
from Classes.er import *

if(sys.argv[1] == "-f"):
  filename = sys.argv[2]
  file = open(filename, 'r')
  ers = file.readlines()
  word = sys.argv[3]

else:
  ers = sys.argv[1]
  word = sys.argv[2]

# Tratando a expressao regular
for i in range(len(ers)):
  ers[i] = ers[i].replace(" ", "") # Retirando os espaços vazios
  ers[i] = ers[i].replace("\n", "") # Retirando as quebras de linha

for er in ers:
  er1 = Er.getEr(er)
  print(er1.equivalentAfne(er1.queue.pop(0)).equivalentAfn())
