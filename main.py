import random

# elemento
# deve gerar um elemento com genes
def generateElement(quantityGenes: int): 
  element = []
  for count in range(quantityGenes):
    element.append(int(random.random() * 2))
  return element

# Função objetivo
# deve converter um elemento com genes binarios em um valor decimal, 
# sendo o primeiro gene o bit de sinal (positivo ou negativo)
def objectiveFunction(element: list):
  binaryValue = ""
  
  sign = "-" if element[0] == 1 else "" 
  unsignedElement = element[1:len(element)]
  
  for gene in unsignedElement:
    binaryValue += str(gene)
    
  fitness = int(sign + binaryValue, 2)
  
  return fitness
    
# população
# deve gerar uma população de elementos
def generatePopulation(quantityElements: int):
    population = []
    for count in range(quantityElements):
      element = generateElement(10)
      population.append([element, objectiveFunction(element)])
    return population
  

def introducePopulation(population: list):
  for chromosome in population:
    print("cromossomo: ", chromosome[0])
    print("fitness: ", chromosome[1])
    print("---------------------------")
    
    
# -----------------------------------------------------------------
population = generatePopulation(10)
introducePopulation(population)


