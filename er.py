import sys
from mainFunctions import *

'''
Para o algoritmo funcionar, ele limpa as quebras de linha,
espaços em branco e aspas simples.
'''

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
  if match(er, word):
    print("match(", er, ", '", word, "') == OK", sep="") 
  else: 
    print("match(", er, ", '", word, "') == Not OK", sep="") 
