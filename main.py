import random

# Para tornar o cálculo com números com sinal mais simples os números negativos são representados de uma forma especial: em complemento para 2. O complemento para dois de um número binário é formado invertendo todos os bits de 0 para 1 e de um para 0 (complemento para 1) e somando 1 ao resultado.

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
    fitness = []
    for count in range(quantityElements):
        element = generateElement(10)
        population.append(element)
        fitness.append(objectiveFunction(element))
    return population


def introducePopulation(population: list):
    for chromosome in population:
        print("cromossomo: ", chromosome[0])
        print("fitness: ", chromosome[1])
        print("---------------------------")


def gerar_lista_pares(populacao: list):
    quantidade_metade = round(len(populacao) / 2)

    metade_individuos1 = populacao[:quantidade_metade]
    metade_individuos2 = populacao[quantidade_metade:len(populacao)]

    return metade_individuos1, metade_individuos2


def cruzar_pares(populacao1: list, populacao2: list):
    filhos1 = populacao1 + populacao2
    filhos2 = populacao2 + populacao1

    return filhos1, filhos2

# def aplica_selecao(pais, filhos, tipo, fitness_pais, fitness_filhos):
#   if tipo == 'nao_elitista':
#     pais = filhos
#     fitness_pais = fitness_filhos

#   return pais, fitness_pais


# def cruzamento_pais(mae,pai):
#   s = random.randint(0, len(mae) -1)
#   filho1 = mae[0:s] + pai[s:]
#   filho2 = pai[0:s] + mae[s:]

#   return filho1,filho2

# def cruzarpopulacao():
#   par1,par2 = pares_cruzamento(populacao)
#   nova_pop = cruzar_pares(par1,par2)

#   nova_pop = nova_pop[:len(populacao)]
#   return nova_pop

# def mutacao(individuo):
#   x = random.randint(1, len(individuo) - 1)
#   individuo[x] = 1 - individuo[x]
#   return individuo

# def mutacao_populacao(populacao, fator_mutacao):
#   for i in populacao:
#     x = random.random()

#     if x < fator_mutacao:
#       i = mutacao(i)
#   return populacao


# -----------------------------------------------------------------
# fitnessList = []
populacao1 = generatePopulation(4)

par1, par2 = gerar_lista_pares(populacao1)
filho1, filho2 = cruzar_pares(par1, par2)
# print(teste)

# n_geracoes = 3
# for i in range(n_geracoes):
#   ger_z = cruzar_pop(populacao_inicial)

#   ger_z = mutacao_populacao(ger_z, 0.7)

# for element in population:
#   fitnessList.append(element[1])

# print(fitnessList)
# introducePopulation(population)
