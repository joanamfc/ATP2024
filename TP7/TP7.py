
def criarlista():
 ano = int(input("Introduza o ano:"))
 mês = int(input("Introduza o mês:"))
 dia = int(input("Introduza o dia:"))
 data = (ano,mês,dia)
 temp_min = float(input("Introduza a temperatura mínima que foi registada nesse dia:"))
 temp_max = float(input("Introduza a temperatura máxima que foi registada nesse dia:"))
 prec = float(input("Intoduza a precipitação registada nesse dia:"))
 lista.append((data,temp_min,temp_max,prec))
 print("Operação realizada com sucesso.")


def verlista(tabMeteo):
    print("_________________________________________Meteorologia__________________________________")
    for dia in tabMeteo:
        print(f"Data: {dia[0]}, Temperatura mínima: {dia[1]}, Temperatura máxima: {dia[2]}, Precipitação: {dia[3]}")

def medias(tabMeteo):
    res = []
    for data, min, max, prec in tabMeteo:
        temperaturaMédia = (min + max) / 2
        res.append((data, temperaturaMédia))
    return res

def guardaTabMeteo(t, nome_ficheiro):
    file = open(nome_ficheiro, "w")
    for dia in t:
        data, min, max, prec = dia
        ano, mês, dia = data
        registo = f"{ano}--{mês}--{dia}&{min}&{max}&{prec}\n"
        file.write(registo)
    file.close()
    return

def carregaTabMeteo(nome_ficheiro):
    res = []
    try:
        with open(nome_ficheiro, "r") as file:
            for linha in file:
                linha = linha.strip()
                campos = linha.split("&")
                data, min, max, prec = campos
                ano, mês, dia = data.split("--")
                dia = ((int(ano), int(mês), int(dia)), float(min), float(max), float(prec))
                res.append(dia)
        print("Dados carregados com sucesso.")
    except FileNotFoundError:
        print("Erro. O ficheiro não existe.")
        
    return res

def minChuva(tabMeteo):
    minimo = tabMeteo[0][1]
    for data, min, *_ in lista[1:]:
        if min < minimo:
            minimo = min 
    return minimo

def amplTerm(tabMeteo):
    res = []
    for data, min, max, prec in tabMeteo:
        amplitude = max - min 
        res.append((data, amplitude))
    return res 

def maxChuva(tabMeteo):
    maximo = tabMeteo[0][3]
    data_maxima = tabMeteo[0][0]
    for data, min, max, prec in tabMeteo[1:]:
        if prec > maximo:
            maximo = prec
            data_maxima = data
    return (data_maxima, maximo)

def diasChuvosos(tabMeteo, p):
    res = []
    for dia in tabMeteo:
        if dia[3] > p:
            res.append((dia[0],dia[3]))
    return res

def maxPeriodoCalor(tabMeteo, p):
    consec_local = 0
    consec_max = 0

    for data,min,max,prec in lista:
        if prec < p:
            consec_local += 1
        else:
            if consec_local > consec_max:
                consec_max = consec_local
            consec_local = 0

    if consec_local > consec_max:
        consec_max = consec_local 
    return consec_max 


import matplotlib.pyplot as plt

def grafTabMeteo(t):
    datas = [ f"{data[0]}--{data[1]}--{data[2]}" for data, *_ in t ]
    temps_min = [ min for _, min, *_ in t]
    temps_max = [ max for _,_,max,_ in t]
    precs =   [ prec for _,_,_,prec in t]
    plt.plot(datas,temps_min, label="Temp Mínima")
    plt.plot(datas,temps_max, label="Temp Máxima")
    plt.xlabel("Data")
    plt.ylabel("Temperatura ºC")
    plt.title("Temperatura Mínima e Máxima")
    plt.legend()
    plt.show()
    plt.bar(datas,precs)
    plt.xlabel("Data")
    plt.ylabel("Precipitação mm")
    plt.title("Precipitação")
    plt.show()
    return


def menu():
    print("------------------------------ MENU DE OPÇÕES ------------------------------")
    print("1: Aqui pode inserir a sua lista meterológica.")
    print("2: Nesta opção vai poder ver a sua lista meterológica.")
    print("3: Quer ver a temperatura média de cada dia? Esta é a opção perfeita.")
    print("4: Aqui é possível guardar a tabela meteorológica num ficheiro de texto ")
    print("5: Aqui pode carregar uma tabela meteorológica de um ficheiro de texto")
    print("6: Aqui pode ser a temperatura mais baixa registada.")
    print("7: E a amplitude térmica? Esta é a sua opção.")
    print("8: Quando é que a precipitação registada teve o seu valor máximo? Aqui indicamos o valor de precipitação e a data.")
    print("9: Quer saber em que dias a precipitação foi superior a um determinado valor? Nós ajudamos.")
    print("10: Quer saber o número consecutivo de dias com precipitação abaixo de um determinado limite? Esta é a sua opção.")
    print("11: Nesta opção desenhamos os gráficos")
    print("0: Sair da aplicação.")

lista = []
cond = True
while cond:
    menu()
    opção = input("Selecione uma opção: ")
    if opção == "1":
        criarlista()
    elif opção == "2":
        if len(lista) == 0:
            print("A lista está vazia, tente introduzir os dados primeiro.")
        else:
            verlista(lista)
    elif opção == "3":
        if len(lista) == 0:
            print("A lista está vazia, tente introduzir os dados primeiro.")
        else:
            print(medias(lista))    
    elif opção == "4":
        if len(lista) == 0:
            print("A lista está vazia, tente introduzir os dados primeiro.")
        else:
            nome_ficheiro = input("Coloque o nome do ficheiro a que quer aceder, não se esqueça de colocar, no fim, .txt: ")
            lista = guardaTabMeteo(lista,nome_ficheiro)
            print("Ficheiro texto criado.")
    elif opção == "5":
        nome_ficheiro = input("Coloque o nome do ficheiro a que quer aceder, não se esqueça de colocar, no fim, .txt: ")
        lista = carregaTabMeteo(nome_ficheiro)
    elif opção == "6":
        if len(lista) == 0:
            print("A lista está vazia, tente introduzir os dados primeiro.")
        else:
           print(f"Temperatura mínima: {minChuva(lista)}")
    elif opção == "7":
        if len(lista) == 0:
            print("A lista está vazia, tente introduzir os dados primeiro.")
        else:
            print(amplTerm(lista))
    elif opção == "8":
        if len(lista) == 0:
            print("A lista está vazia, tente introduzir os dados primeiro.")
        else:
            print(maxChuva(lista))
    elif opção == "9":
        p = float(input("Insira o valor de precipitação limite: "))
        print(diasChuvosos(lista, p))
    elif opção == "10":
        if len(lista) == 0:
            print("A lista está vazia, tente introduzir os dados primeiro.")
        else:
            p = float(input("Insira o valor de precipitação limite: "))
            print(maxPeriodoCalor(lista,p))
    elif opção == "11":
        if len(lista) == 0:
            print("A lista está vazia, tente introduzir os dados primeiro.")
        else:
            grafTabMeteo(lista)    
    elif opção =="0":
        print("Muito obrigada por escolher a nossa aplicação. Volte sempre. ")
        cond = False  
    else:
        print("Escolha uma opção válida.")