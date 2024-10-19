
def criarTurma():
    turma = []
    return turma


def inserirTurma(turma, aluno, nome, id, notas):
    turma.append(aluno)
    print(f"O aluno {nome} cujo seu id é {id} foi adicionado à turma.")
    return turma

def listarTurma(turma, aluno, notas):
    if not turma:
        print("Não existe uma turma.")
    else:
        print("------------------------------TURMA------------------------------")
        for aluno in turma:
            print(f"Aluno encontrado: Nome do aluno: {aluno[0]} |  Id: {aluno[1]}  | Notas: TPC - {notas[0]} Projeto - {notas[1]} Teste - {notas[2]}")


def alunoId(turma):
    id = input("Introduza o Id do aluno que quer consultar:")
    aluno_encontrado = False
    for aluno in turma:
        if aluno[1] == id:
            print(f"Aluno encontrado: Nome do aluno: {aluno[0]} |  Id: {aluno[1]}  | Notas: TPC - {aluno[2][0]} Projeto - {aluno[2][1]} Teste - {aluno[2][2]}")
            aluno_encontrado = True
    if not aluno_encontrado:
        print("Aluno não encontrado.")
    return


def guardarTurma(turma):
    nome_ficheiro = input("Insira um nome para o ficheiro:")
    file = open(nome_ficheiro,"w")
    for aluno in turma:
        file.write(f"{aluno[0]}|{aluno[1]}|{aluno[2][0]}|{aluno[2][1]}|{aluno[2][2]} \n")
    file.close() 
    print(f"A turma foi guardada em {nome_ficheiro} com sucesso! ")
    return 

def carregarTurma(turma):
    nome_ficheiro = input("Coloque o nome do ficheiro a que quer aceder:")
    turma = []
    file = open(nome_ficheiro,"r")
    for line in file:
        informações = line.strip().split("|")
        nome, id = informações[0], informações[1]
        notas = [float(informações[2]), float(informações[3]), float(informações[4])]
        aluno = (nome, id, notas)
        turma.append(aluno)
        print(f"Turma carregada do ficheiro {nome_ficheiro}.")
    file.close()
    if FileNotFoundError:
        print("Erro. Ficheiro não encontrado")
    return turma


def menu():
    print("------------------------------MENU DE OPÇÕES ------------------------------")
    print("1: Criar uma turma")
    print("2: Inserir um aluno na turma")
    print("3: Listar a turma")
    print("4: Consultar um aluno pelo seu id")
    print("8: Guardar a turma em ficheiro")
    print("9: Carregar uma turma de um ficheiro")
    print("0: Sair da aplicação")
    opção = input("Selecione uma opção: ")
    
    while opção != "0":
        if opção == "1":
            turma = criarTurma()
            print("Turma criada com sucesso!")
            opção = input("Selecione uma opção: ")
        
        elif opção == "2":
            nome = input("Introduza o nome do aluno:")
            id = input("Introduza o Id do aluno:")
            notaTPC = float(input("Introduza a nota que o aluno obteve no TPC:"))
            notaProj = float(input("Introduza a nota que o aluno obteve no projeto:"))
            notaTeste = float(input("Introduza a nota que o aluno obteve no teste:"))
            notas = [notaTPC, notaProj, notaTeste]
            aluno = (nome, id, notas)
            turma = inserirTurma(turma, aluno, nome, id, notas)
            opção = input("Selecione uma opção: ")
            
        elif opção == "3":
            listarTurma(turma, aluno, notas)
            opção = input("Selecione uma opção: ")
            
        elif opção == "4":
            if not turma:
                print("Não existe uma turma")
            else:
                alunoId(turma)
            opção = input("Selecione uma opção: ")
        
        elif opção == "8":
            guardarTurma(turma)
            opção = input("Selecione uma opção: ")
            
        elif opção == "9":
            carregarTurma(turma)
            opção = input("Selecione uma opção: ")
            
        elif opção not in [1,2,3,4,5]:
            print("Escolha uma opção válida.")
            opção = input("Selecione uma opção: ")     
    print("Muito obrigada por escolher a nossa aplicação. Volte sempre. ")


menu()