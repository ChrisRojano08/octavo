from generateProbabilities import GenerateProbabilities
from probabilidades import Probabilidades

genProb = GenerateProbabilities()
probabilidades = Probabilidades()


columnas = genProb.generate()
probabilidades.genProb(columnas)

