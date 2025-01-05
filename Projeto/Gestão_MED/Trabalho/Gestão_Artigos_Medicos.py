import FreeSimpleGUI as sg
import json
import mod_ata as mod

dataset = None


menu_layout = [
                [sg.Button('Help', key='-HELP-', size=(10, 1), button_color=("white", "#00143f"))],
                [sg.HorizontalSeparator()],
                [sg.Button('Carregar', key='-CARREGAR-',  size=(10, 1), button_color=("white", "#213462"))],
                [sg.Button('Importar', key='-IMPORTAR-',  size=(10, 1), button_color=("white", "#213462"))],
                [sg.Button('Guardar', key='-GUARDAR-',  size=(10, 1), button_color=("white", "#213462"))],
                [sg.HorizontalSeparator()],
                [sg.Button('Atualizar', key='-ATUALIZAR-',  size=(10, 1), button_color=("white", "#425386"))],
                [sg.Button('Adicionar', key='-ADICIONAR-',  size=(10, 1), button_color=("white", "#425386"))],
                [sg.Button('Remover', key='-REMOVER-',  size=(10, 1), button_color=("white", "#425386"))],
                [sg.Button('Consultar', key='-CONSULTAR-',  size=(10, 1), button_color=("white", "#425386"))],
                [sg.Button('Listar', key='-LISTAR-',  size=(10, 1), button_color=("white", "#425386"))],
                [sg.Button('Analisar', key='-ANALISE-',  size=(10, 1), button_color=("white", "#425386"))],
                [sg.Button('Estatística', key='-ESTATISTICA-',  size=(10, 1), button_color=("white", "#425386"))],
                [sg.HorizontalSeparator()],
                [sg.Button('Sair', key = '-SAIR-',  size=(10, 1), button_color=("white", "#6373a9"))],
            ]

layout1 = [
    [sg.Col(menu_layout,element_justification='center', background_color='#aab6d3'),
    sg.VSep(),
    sg.Col([[sg.Output(size=(60,23), key='-DADOS-')]], element_justification='center', expand_x=True, expand_y=True)
    ]
]

sg.theme('LightBlue2')

window1 = sg.Window('Gestão de artigos médicos', layout1, font = ("Helvetica",24), location=(0,0), finalize=True)

window1['-DADOS-'].update(
    "Bem-vindo à nossa aplicação de Gestão de Artigos Médicos!\n"
    "Com este sistema, é possivel carregar, importar, consultar e gerenciar artigos médicos de forma eficiente.Use o menu à esquerda para navegar entre as opções.\n"
    "Se precisar de ajuda, clique no botão Help.\n"
)


stop = False
while not stop:
    event1, values1 = window1.read()

    if event1 == "-SAIR-":
        print("A sair....")
        confirmação = sg.popup(
            "Tem a certeza de que deseja sair? \n"
            "Lembre-se que se não tiver salvo os seus dados eles serão perdidos.",
            custom_text=("Sim","Não"),
            title= "Confirmação de saída")
        if confirmação == "Sim" :
            sg.popup("A sair da aplicação...", title="Saída")
            stop = True
        elif confirmação == "Não":
            sg.popup("Encontra-se novamente no menu principal.", title="Menu principal")

    elif event1 == sg.WINDOW_CLOSED:
        print("A sair...")
        stop = True

    elif event1 == '-CARREGAR-':
        print("A carregar...")
        ficheiro = sg.popup_get_file('Selecione o ficheiro JSON', file_types=(('ficheiros JSON','*.json'),), title = "Seleção de ficheiro")
        if ficheiro:
            dataset = mod.carregar_arquivo_json(ficheiro)
            sg.popup(f"Foram carregados {len(dataset)} registos.", title= "Sucesso")
            print(f"Número de registos: {len(dataset)}")
        else:
            sg.popup("Não foi possível carregar o ficheiro", title= "Erro")

    elif event1 == '-IMPORTAR-':
        print("A importar...")
        if dataset is not None:
            ficheiro_novo = sg.popup_get_file('Selecione o ficheiro JSON', file_types=(('ficheiros JSON','*.json'),), title = "Seleção de ficheiro")
            if ficheiro_novo:
                try:
                    novos_registos = mod.carregar_arquivo_json2(ficheiro_novo)
                    dataset = mod.importar_ficheiro(dataset,novos_registos)
                    print("Importação bem sucessida!")
                    print(f"Número de registos: {len(dataset)}")
                except Exception as e:
                    sg.popup("Aconteceu um erro no carregamento do seu ficheiro. Tente novamente.", title = "Erro")
                    print("Importação mal sucessida!")
            else:
                sg.popup("Nenhum ficheiro foi selecionado.", title = "Erro")
        else:
            sg.popup("Por favor, carregue o ficheiro primeiro.", title = "Erro")


    elif event1 == '-GUARDAR-': # Como ficheiro texto ou Json
        print("A guardar... ")
        if dataset:
            escolha = sg.popup("Escolha o formato em que pretende guardar:",
                           custom_text=("Ficheiro Texto","Ficheiro original - JSON"),
                            title= "Salvar como")
            if escolha == "Ficheiro Texto":
                nome_arquivo = sg.popup_get_file("Salvar como Ficheiro Texto", save_as=True, no_window=True, file_types=(('Texto', '*.txt'),), title= "Salvar texto")
                if nome_arquivo:
                    mod.ficheiro_texto(dataset,nome_arquivo)
                    sg.popup("O seu ficheiro foi guardado com sucesso.", title = "Sucesso")
                else:
                    sg.popup("Nenhum arquivo foi selecionado para guardar.", title = "Erro")

            elif escolha == "Ficheiro original - JSON":
                nome_arquivo = sg.popup_get_file("Salvar como Ficheiro JSON", save_as=True, no_window=True, file_types=(('JSON', '*.json'),), title= "Salvar JSON")
                if nome_arquivo:
                    mod.guardar_json(dataset,nome_arquivo)
                    sg.popup("O seu ficheiro foi guardado com sucesso.", title= "Sucesso")
                else:
                    sg.popup("Nenhum arquivo foi selecionado para guardar.", title= "Erro")
            else:
                sg.popup("Selecione uma opção válida.", title= "Erro")
        else:
            sg.popup("Por favor, carregue o ficheiro primeiro.", title = "Erro")
            print("Carregamento não foi bem-sucedido.")


    elif event1 == "-HELP-":
        texto_ajuda = (
            "Carregar: Carrega para memória o dataset que deverá estar guardado num ficheiro de suporte a esta aplicação. \n \n"
            "Importar: Permite adicionar novos registos a partir de um ficheiro externo com a mesma estrutura do ficheiro de suporte da aplicação, atualizando o conjunto de dados existente em memória. \n \n"
            "Guardar: Permite ao utilizador que quando decidir sair da aplicação ou tiver selecionado o armazenamento dos dados, os dados são guardados num ficheiro de suporte. \n \n"
            "Atualizar: Permitir a atualização da informação de uma publicação, nomeadamente a data de publicação, o resumo, palavras-chave, autores e afiliações. \n \n"
            "Adicionar: É possível adicionar novos dados. \n \n"
            "Remover: Pode remover os dados que pretender. \n \n"
            "Consultar: Permite consultar publicações utilizando vários filtros, a consulta pode ser feita por ordem. \n \n"
            "Listar: Permite listar as publicações do dataset.\n \n"
            "Analisar: Permite listar os autores e as palavras-chave. \n \n"
            "Estatística: Permite a observação de relatórios com gráficos segundo o filtro que escolha.\n \n"
            "Sair: Fechar aplicação. \n \n"
        )

        sg.popup_scrolled(
            texto_ajuda,
            title = "Ajuda",
            size = (50,20),
            font = ("Helvetica",12)
        )

    elif event1 == "-REMOVER-":
      print("A remover... ")
      try:
        if dataset is not None:
            mod.interface_remover(dataset,ficheiro)
            print(f"Número de registos: {len(dataset)}")
        else:
            sg.popup("Por favor, carregue o ficheiro primeiro.", title = "Erro")
      except Exception as e:
            None 
        
    elif event1 == "-ATUALIZAR-":
      print("A atualizar... ")
      try:
        if dataset is not None:
            mod.interface_atualizar(dataset,ficheiro)
        else:
            sg.popup("Por favor, carregue o ficheiro primeiro.", title = "Erro")
      except Exception as e:
            None 

    elif event1 == "-ADICIONAR-":
      print("A adicionar... ")
      try:
        if dataset is not None:
            mod.interface_adicionar(dataset,ficheiro)
            print(f"Número de registos: {len(dataset)}")
        else:
            sg.popup("Por favor, carregue o ficheiro primeiro.", title = "Erro")
      except Exception as e:
            None 
    
    elif event1 == "-ESTATISTICA-":
        print("A gerar estatísticas... ")
        if dataset is not None:
            mod.interface_estatistica(dataset)
        else:
            sg.popup("Por favor, carregue o ficheiro primeiro.", title = "Erro")

    
    elif event1 == "-CONSULTAR-":
        print("A consultar...")
        try:
            if dataset is not None:
                mod.interface_consultar(dataset)
            else:
                sg.popup("Por favor, carregue o ficheiro primeiro.", title = "Erro")
        except Exception as e:
            None 
    
    elif event1 == "-LISTAR-":
        print("A listar...")
        try:
            if dataset is not None:
                mod.interface_listar(dataset)
            else:
                sg.popup("Por favor, carregue o ficheiro primeiro.", title = "Erro")
        except Exception as e:
            None 

    
    elif event1 == "-ANALISE-":
        try:
            print("A analisar...")
            if dataset is not None:
                mod.interface_analise(dataset)
            else:
                sg.popup("Por favor, carregue o ficheiro primeiro.", title = "Erro")
        except Exception as e:
            None 
        



