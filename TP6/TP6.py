def criarTurma():
    turma = []
    return turma

def inserirTurma(turma, aluno, nome, id):
    turma.append(aluno)
    print(f"O aluno {nome} cujo seu id é {id} foi adicionado à turma.")
    return turma

def listarTurma(turma):
    if not turma:
        print("Não existe uma turma.")
    else:
        print("------------------------------TURMA------------------------------")
        for aluno in turma:
            print(f"Aluno encontrado: Nome do aluno: {aluno[0]} |  Id: {aluno[1]}  | Notas: TPC - {aluno[2][0]} Projeto - {aluno[2][1]} Teste - {aluno[2][2]}")
    return 

def alunoId(turma):
    id = input("Introduza o Id do aluno que quer consultar:")
    aluno_encontrado= False
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
        file.write(f"{aluno[0]} | {aluno[1]} | {aluno[2][0]} # {aluno[2][1]} # {aluno[2][2]} \n")
    file.close() 
    print(f"A turma foi guardada em {nome_ficheiro} com sucesso! ")
    return  

def carregarTurma():
    nome_ficheiro = input("Coloque o nome do ficheiro a que quer aceder: ")
    turma = []
    
    try:
        with open(nome_ficheiro, "r") as file:
            for line in file:
                informações = line.strip().split("|")
                nome, id = informações[0], informações[1]
                notas = informações[2].strip().split("#")
                notaTPC = float(notas[0])
                notaProj = float(notas[1])
                notaTeste = float(notas[2])
                aluno = (nome, id, [notaTPC, notaProj, notaTeste])
                turma.append(aluno)
        print(f"Turma carregada do ficheiro {nome_ficheiro}.")
    except FileNotFoundError:
        print(f"Erro.O ficheiro {nome_ficheiro} não foi encontrado.")
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

turma = [] 
cond = True
while cond:
    menu()
    opção = input("Selecione uma opção: ")
    
    if opção == "1":
        turma = criarTurma()
        print("Turma criada com sucesso!")
        
    elif opção == "2":
        nome = input("Introduza o nome do aluno:")
        id = input("Introduza o Id do aluno:")
        notaTPC = float(input("Introduza a nota que o aluno obteve no TPC:"))
        notaProj = float(input("Introduza a nota que o aluno obteve no projeto:"))
        notaTeste = float(input("Introduza a nota que o aluno obteve no teste:"))
        notas = [notaTPC, notaProj, notaTeste]
        aluno = (nome, id, notas)
        turma = inserirTurma(turma, aluno,nome,id)
            
    elif opção == "3":
        listarTurma(turma)
     
    elif opção == "4":
        if not turma:
            print("Não existe uma turma")

        else:
            alunoId(turma)
   
    elif opção == "8":
        guardarTurma(turma)

    elif opção == "9":
        carregarTurma()

    elif opção == "0":
        print("Muito obrigada por escolher a nossa aplicação. Volte sempre. ")
        cond = False
    
    else:
        print("Escolha uma opção válida.")