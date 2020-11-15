import random
import math

def random_walk(M, p):

    posAtual = 0 # posição que se encontra no momento
    custoPosTotal = 0 #soma dos custos de cada posição
    custoPosFinal = 0 #custo referente a posição final

    for i in range(M):
        dx = random.choice([1, 100]) # gerar numero aleatorio 
        dx = dx/100 # divide por 100
        if(dx <= p): #aplica a probabilidade
            posAtual += 1
        else:#aplica a probabilidade
            posAtual += -1
        custoPosTotal += calcularCusto(posAtual)
    i += 1
    if(posAtual != 0):
        custoPosFinal = calcularCusto(posAtual)
    return (posAtual, custoPosTotal, custoPosFinal)

def calcularCusto(posAtual):
    posAtual = posAtual*posAtual
    return(abs(posAtual))

def calcularEstatisticas(vet, tipo):
    media = maxima = numZeros = variancia = 0
    minima = math.inf

    for i in range(len(vet)):
        atual = abs(vet[i])
        if(vet[i] > maxima):
            maxima = atual
        if(vet[i] < minima):
            minima = atual
            if(tipo == 0):
                minima = vet[i]
        if(vet[i] == 0):
            numZeros += 1
        
        if(tipo == 1):
            media += atual
        else:
            media += vet[i]

    media = media/len(vet)

    for i in range(len(vet)):
        atual = vet[i]
        if(tipo == 1):
            atual = abs(atual)
        variancia += (atual - media)**2
    variancia = variancia/(len(vet) -1)

    print("Minimo = ", minima)
    print("Maximo = ", maxima)
    print("Medio = ", round(media, 4))
    print("Variancia = ", round(variancia, 4)) 
    return(numZeros)


vetCustoTotal = []
vetCustoPosFinal = []
vetPosicao = []

print("\n ::::::::::::::::::::::::::: Caminho Bebado ::::::::::::::::::::::::::: \n\n\n\n")

N = int(input("\nInforme o numero de caminhadas: "))
if(N <= 0):
    while(N <= 0):
        print("\n Numero invalido, tente novamente")
        N = int(input("\nInforme o numero de caminhadas: "))
M = int(input("\nInforme o numero de passos: "))
if(M <= 0):
    while(M <= 0):
        print("\n Numero invalido, tente novamente")
        M = int(input("\nInforme o numero de passos: "))

p = float(input("\nInforme valor da probabilidade: "))
if(p > 1 or p < 0):
    
    while(p > 1 or p < 0):
        print("\n Numero invalido, tente novamente")
        p = int(input("\nInforme o valor da probabilidade: "))
       



for i in range(N):
    
    (posAtual, custoPosTotal, custoPosFinal) = random_walk(M, p)
    
    vetPosicao.insert(i, posAtual)
    vetCustoTotal.insert(i, custoPosTotal)
    vetCustoPosFinal.insert(i, custoPosFinal)
   
print("\n\n")
print("\nEstatisticas Referentes a Posicao do Bebado: \n")
print(vetPosicao)
print("\n")
numZeros = calcularEstatisticas(vetPosicao, 0)
print("Num Zeros = ", numZeros)

print("\n\n")
print("\nEstatisticas Referentes ao Custo Total: \n")
print(vetCustoTotal)
print("\n")
calcularEstatisticas(vetCustoTotal, 1)

print("\n\n")
print("\nEstatisticas Referentes ao Custo da Posicao Final: \n")
print(vetCustoPosFinal)
print("\n")
calcularEstatisticas(vetPosicao, 1)
print("\n\n")


