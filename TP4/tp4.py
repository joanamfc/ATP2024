import random


def menu():
    print("-------------- MENU --------------")
    opção = int()
    opção = int(input("(1)Criar Lista\n(2)Ler Lista\n(3)Soma\n(4)Média\n(5)Maior\n(6)Menor\n(7)Está ordenada por ordem crescente\n(8)Está ordenada por ordem descrescente\n(9)Procurar um elemento\n(0)Sair "))
    return opção

def criarLista(lista):
    list.clear(lista)
    N = int(input("Insere o número de elementos que terá a tua lista:"))
    i = 0
    while len(lista) < N:
        elem = random.randint(0, 101)
        lista.append(elem)
        i = i + 1
    return lista 

def lerLista(lista):
    list.clear(lista)
    N = int(input("Insira o número de elementos que terá a sua lista:"))
    i = 0
    while len(lista) < N:
        elem = int(input("Introduz o elemento que queres acrescentar na lista:"))
        lista.append(elem)
        i = i + 1
    return lista

def soma(lista):
    soma = 0
    i = 0
    while i < len(lista):
        soma = soma + lista[i]
        i = i + 1
    return soma 

def média(lista):
    média = soma(lista) / len(lista)
    return média

def maior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num 
    return maior 

def menor(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num 
    return menor 

def crescente(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            print("Não, a lista não está apresentada por ordem crescente.")
            return
    print("Sim, a lista está apresentada por ordem crescente.")

def decrescente(lista):
    for i in range(len(lista)-1):
        if lista[i] < lista[i+1]:
            print("Não, a lista não está apresentada por ordem decrescente.")
            return 
    print("Sim, a lista está apresentada por ordem decrescente.")


def procurarelemento(lista):
    elemento = int(input("Introduz o elemento que queres procurar na lista:"))
    if elemento in lista:
        posição = (lista.index(elemento))
        print(f"O elemento {elemento} encontra-se na lista, na posição {posição}.")
    else:
        print(f"O elemento {elemento} não se encontra na lista.")
        print("-1")

def main():
    lista = []
    opção = menu()
    while opção != 0:
        if opção == 1:
            print(criarLista(lista))
            opção = menu()
        elif opção == 2:
            print(lerLista(lista))
            opção = menu()
        elif opção == 3:
            print(soma(lista))
            opção = menu()
        elif opção == 4:
            print(média(lista))
            opção = menu()
        elif opção == 5:
            print(maior(lista))
            opção = menu()
        elif opção == 6:
            print(menor(lista))
            opção = menu()
        elif opção == 7:
            crescente(lista)
            opção = menu()
        elif opção == 8:
            decrescente(lista)
            opção = menu()
        elif opção == 9:
            procurarelemento(lista)
            opção = menu()
        elif opção not in [1,2,3,4,5,6,7,8,9]:
            print("Escolhe uma opção válida.")
            opção = menu()
        
    print(f"Saiu do programa. A lista que ficou guardada foi {lista}")

main()