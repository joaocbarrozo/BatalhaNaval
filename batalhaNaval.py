#Iniciando o jogo
print('Vamos jogar Batalha Naval?')
print('O seu objetivo é afundar o navio inimigo!')
print("O campo de batalha é um tabuleiro 10 X 10, com letras de A a J e números de 1 a 10, e o navio inimigo é um crusador 3 X 1. ")

#Criar todos os possiveis quadrantes do tabuleiro
eixoNum = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
eixoLetra = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
listaQuadrante = []
for x in eixoLetra:
    for y in eixoNum:
        listaQuadrante.append((x, y))

#Definindo uma função que escolhe aleatoriamente uma posição para o navio inimigo
def sorteio():
    global listaQuadrante
    quadrante = quadrante2 = quadrante3 = (0, 0)
    while quadrante not in listaQuadrante or quadrante2 not in listaQuadrante or quadrante3 not in listaQuadrante:
        import random
        num = random.randrange(0,1000) % 10 + 1
        letra = random.randrange(0,1000) % 10 + 1
        posicao = random.randrange(0,1000) % 2
        p2 = 0
        p3 = 0
        dictLetra = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J"}
        if posicao == 0 and num > 5:
            p2 = num - 1
            p3 = num - 2
            quadrante2 = (dictLetra[letra], p2)
            quadrante3 = (dictLetra[letra], p3)
        elif posicao == 0 and num <= 5:
            p2 = num + 1
            p3 = num + 2
            quadrante2 = (dictLetra[letra], p2)
            quadrante3 = (dictLetra[letra], p3)
        elif posicao == 1 and letra > 5:
            p2 = letra - 1
            p3 = letra - 2
            quadrante2 = (dictLetra[p2], num)
            quadrante3 = (dictLetra[p3], num)
        elif posicao == 1 and letra <= 5:
            p2 = letra + 1
            p3 = letra + 2
            quadrante2 = (dictLetra[p2], num)
            quadrante3 = (dictLetra[p3], num)
        letra = dictLetra[letra]
        quadrante = (letra, num)
    listaQuadrante.remove(quadrante)
    listaQuadrante.remove(quadrante2)
    listaQuadrante.remove(quadrante3)
    n = [quadrante, quadrante2, quadrante3]
    return n

#Criando 3 navios

n1 = sorteio()
n2 = sorteio()
n3 = sorteio()
print(n1)
print(n2)
print(n3)
listaCrusador = n1 + n2 + n3
print(len(n1+n2+n3))
print(listaCrusador)
#Interação com o jogador
while len(listaCrusador) > 0:
    print(listaCrusador)
    print(len(listaCrusador))
    jogadorLetra = input("Escolha uma letra entre A e J.").capitalize()
    jogadorNum = int(input("Escolha um número entre 1 e 10."))
    tentativa = (jogadorLetra, jogadorNum)
    print("A sua tentativa é no quadrante", tentativa)
    if tentativa in n1 or tentativa in n2 or tentativa in n3:
        print("Parabéns !!! Você acertou o navio inimigo!")
        if tentativa in n1:
            n1.remove(tentativa)
        elif tentativa in n2:
            n2.remove(tentativa)
        else:
            n3.remove(tentativa)
        listaCrusador = n1 + n2 + n3
    else:
        print("Oh não, você errou! Tente novamente.")

print("Você afundou o navio inimigo e venceu a batalha! Parabéns !!!")
