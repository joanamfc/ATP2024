
import FreeSimpleGUI as sg
from random import randint
import numpy as np
import json
import matplotlib.pyplot as plt



# --------------------------------------  ADICIONAR ---------------------------------------------

# -------------- INTERFACE ADICIONAR ----------------------------


def interface_adicionar(dataset,ficheiro):
        sg.theme('LightBlue2')
        layout = [
            [sg.Text('Registo de Publicação', font=('Helvetica', 16, "bold"), justification='center', expand_x=True)],


            [sg.Text('Resumo', size=(15, 1), font=('Helvetica', 12, "bold"))],
            [sg.Multiline(key='-ABSTRATO-', size=(60, 5), expand_x=True)],

            [sg.Text('')],

            [sg.Text('Palavras-Chave:', font=('Helvetica', 12, "bold"), pad=(0, 0)), 
            sg.Text(' adiciona uma de cada vez', font=('Helvetica', 10), pad=(0, 0))],
            [sg.InputText(key='-PALAVRA-', size=(40, 1), expand_x=True, enable_events=True),
            sg.Button('Adicionar', key='-ADICIONAR_PALAVRA-', size=(10, 1)),
            sg.Button('Remover', key='-REMOVER_PALAVRA-', size=(10, 1))],
            [sg.Listbox(values=[], key='-PALAVRAS_LIST-', size=(60, 5), enable_events=True,
                        select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, expand_x=True)],

            [sg.Text('')],

            [sg.Text('Autores:', font=('Helvetica', 12, "bold"), pad=(0, 0)),
            sg.Text(' adiciona um de cada vez', font=('Helvetica', 10), pad=(0, 0))],
            [sg.Text('Nome:', font=('Helvetica', 10)), sg.InputText(key='-NOME-', size=(40, 1), expand_x=True)],
            [sg.Text('Afiliação:', font=('Helvetica', 10)), sg.InputText(key='-AFILIACAO-', size=(40, 1), expand_x=True)],
            [sg.Text('Orcid:', font=('Helvetica', 10)), sg.InputText(key='-ORCID-', size=(40, 1), expand_x=True, enable_events=True)],
            [sg.Button('Adicionar', key='-ADICIONAR_AUTOR-', size=(10, 1), expand_x=True),
            sg.Button('Remover', key='-REMOVER_AUTOR-', size=(10, 1), expand_x=True)],
            [sg.Listbox(values=[], key='-AUTORES_LIST-', size=(60, 5), enable_events=True,
                        select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, expand_x=True)],

            [sg.Text('')],

            [sg.Text('Título:', size=(4, 1), font=('Helvetica', 12, "bold")), sg.InputText(key='-TITULO-', size=(50, 1), expand_x=True)],
            [sg.Text('Data de Publicação:', size=(15, 1), font=('Helvetica', 12, "bold")), sg.Input(key='-DATA-', size=(20, 1), expand_x=True, enable_events=True ),
            sg.CalendarButton('Selecionar', target='-DATA-', format='%Y-%m-%d')],
        
            [sg.Text('')],

            [sg.Button('Salvar', key='-SALVAR-', size=(15, 1), expand_x=True), sg .Button('Cancelar', key='-CANCELAR-', size=(15, 1), expand_x=True)]
        ]

        # Janela
        window = sg.Window('Registo de Publicação', layout, location=(470,0))


        autores = []
        palavras_chave = []


        stop = False
        while not stop:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == '-CANCELAR-':
                stop = True

            elif event == '-PALAVRA-':
                texto_atual = values['-PALAVRA-']
                texto_filtrado = texto_atual.rstrip(",.")
                if texto_filtrado != texto_atual:
                    window['-PALAVRA-'].update(texto_filtrado)
            

            elif event == '-ORCID-' and len(values["-ORCID-"]):
                orcid_text = values["-ORCID-"]
            
                if len(orcid_text) in [4, 9, 14]:  
                    window["-ORCID-"].update(orcid_text + "-")
            
                elif len(orcid_text) > 19:
                    window["-ORCID-"].update(orcid_text[:-1])
                
                elif len(orcid_text) == 19 and orcid_text[-1] not in "0123456789X":
                    window["-ORCID-"].update(orcid_text[:-1])

                elif len(orcid_text) < 19:
                    if "-" in orcid_text:
                        ORCID = orcid_text.split("-")
                        for elem in ORCID:
                            for digito in elem:
                                if digito not in "0123456789":
                                    window["-ORCID-"].update(orcid_text[:-1])
                    else:
                        for digito in orcid_text:
                            if digito not in "0123456789":
                                window["-ORCID-"].update(orcid_text[:-1])

            elif event == "-DATA-":
                data = values["-DATA-"]  

                if len(data) in [4, 7]: 
                    window["-DATA-"].update(data + "-")

                if any(char not in "0123456789-" for char in data):
                    window["-DATA-"].update(data[:-1])

                if len(data) > 10:
                    window["-DATA-"].update(data[:-1])


            elif event == '-ADICIONAR_AUTOR-':
                nome = values['-NOME-']
                afiliacao = values['-AFILIACAO-'] if values['-AFILIACAO-'] else None  
                orcid = values['-ORCID-'] if values['-ORCID-'] else None

                if not nome: 
                    sg.popup_error("Por favor, insira o nome do autor.", title='Erro')
                else:
                    if orcid and len(orcid) < 19:
                        sg.popup_error(f" O ORCID ({orcid}) é invalido. Ele deve conter exatamente 19 caracteres no formato: 0000-0000-0000-0000.", title='Erro')
                    
                    elif orcid and not ORCID_NAME(orcid, nome, dataset):
                        sg.popup_error(f"Esse ORCID já está associado a outro autor! Por favor, tente novamente.", title='Erro')
                    

                    else:
                        autores = criar_autor(nome,autores, afiliacao, orcid)
                        autores_str = mostrar_na_listbox_autores(autores)
                        window['-AUTORES_LIST-'].update(autores_str)
                        # para limpar os campos:
                        window['-NOME-'].update('')
                        window['-AFILIACAO-'].update('')
                        window['-ORCID-'].update('')




            elif event == '-REMOVER_AUTOR-':
                selecionado = values['-AUTORES_LIST-']
                if selecionado:
                    autores = remover_autores(autores, autores_str, selecionado)
                    autores_str = mostrar_na_listbox_autores(autores)
                    window['-AUTORES_LIST-'].update(autores_str)
                else:
                    sg.popup_error("Por favor, selecione um autor para remover.", title='Erro')


            elif event == '-ADICIONAR_PALAVRA-':
                palavra = values['-PALAVRA-']
                if palavra:
                    palavras_chave.append(palavra.strip())
                    window['-PALAVRAS_LIST-'].update(palavras_chave)
                    window['-PALAVRA-'].update('')
                else:
                    sg.popup_error("Por favor, insira uma palavra-chave válida.", title='Erro')

            
            elif event == '-REMOVER_PALAVRA-':
                selecionada = values['-PALAVRAS_LIST-']
                if selecionada:
                    palavras_chave.remove(selecionada[0])
                    window['-PALAVRAS_LIST-'].update(palavras_chave)
                else:
                    sg.popup_error("Por favor, selecione uma palavra-chave para remover.", title='Erro')


            if event == '-SALVAR-':
                titulo = values['-TITULO-']
                data = values['-DATA-']
                abstrato = values['-ABSTRATO-']
        
                if data:
                    d,m,a,f = data_valida(data)

                    dia = int(data.split("-")[2])
                    mes = int(data.split("-")[1])
                    ano = int(data.split("-")[0])
                    

                    if d == False:
                        lista_dias = calendário(ano,mes)
                        sg.popup_error(f"Dia inválido. Por favor, escreva um dia entre {lista_dias[0]} and {lista_dias[-1]}")

                    elif f == False:
                        sg.popup_error(f"Formato inválido! Você digitou: {data}. Por favor, insira a data no formato correto: ano-mês-dia (exemplo: 2023-05-03).", title='Erro')

                    elif m == False:
                        sg.popup_error(f"Mês invalido: {mes}. Por favor, escreva um mês entre 1 e 12.", title='Erro')

                    elif a == False:
                        sg.popup_error(f"Ano inválido: {ano}. Por favor, insira um ano entre 1950 e o ano atual.", title='Erro')

                    else:
                        if not autores:
                            sg.popup_error("Por favor, adicione pelo menos um autor.", title='Erro')
                        elif not titulo:
                            sg.popup_error("Por favor, forneça um título.", title='Erro')
                        elif not abstrato:
                            sg.popup_error("Por favor, forneça um resumo.", title='Erro')
                        else:
                                # Cria e salva o post se tudo estiver ok
                                dataset = criar_post(abstrato, autores, titulo, dataset, palavras_chave, data)

                                try:
                                    with open(ficheiro, "w", encoding="utf-8") as f:
                                        json.dump(dataset, f, ensure_ascii=False, indent=4)
                                    
                                        sg.popup(
                                            "Registo Salvo com Sucesso!",
                                            f"Título: {titulo}",
                                            f"Data: {data}",
                                            f"Resumo: {abstrato}",
                                            f"Palavras-Chave: {criar_palavra_passe(palavras_chave)}",
                                            f"Autores: {', '.join([autor['name'] for autor in autores])}",
                                        )
                                        
                                        print("Publicação fui adicionada com sucesso!")
                                except Exception as e:
                                    sg.popup_error(f"Erro ao salvar no arquivo: {e}")
                                    print("Erro ao adicionadar publicação")
                            
                                stop = True
                else:
                    if not autores:
                        sg.popup_error("Por favor, adicione pelo menos um autor.", title='Erro')
                    elif not titulo:
                        sg.popup_error("Por favor, forneça um título.", title='Erro')
                    elif not abstrato:
                        sg.popup_error("Por favor, forneça um resumo.", title='Erro')
                    else:
                                dataset = criar_post(abstrato, autores, titulo, dataset, palavras_chave, data)

                                try:
                                    with open(ficheiro, "w", encoding="utf-8") as f:
                                        json.dump(dataset, f, ensure_ascii=False, indent=4)
                                    
                                        sg.popup(
                                            "Registo Salvo com Sucesso!",
                                            f"Título: {titulo}",
                                            f"Data: {data}",
                                            f"Resumo: {abstrato}",
                                            f"Palavras-Chave: {criar_palavra_passe(palavras_chave)}",
                                            f"Autores: {', '.join([autor['name'] for autor in autores])}",
                                        )

                                        print("Publicação fui adicionada com sucesso!")

                                except Exception as e:
                                    sg.popup_error(f"Erro ao salvar no arquivo: {e}")
                                    print("Erro ao adicionadar publicação")
                            
                                stop = True

        window.close()

# ------------------ criar autor e adiciona em autores --------------------------------------------------
def criar_autor(nome, autores , afiliação = None, ORCID = None):
    autor = {"name": nome.capitalize()}
    if afiliação:
        autor["affiliation"] = afiliação.capitalize()
    if ORCID:
        autor["ORCID"] = f"https://orcid.org/{ORCID}"

    autores.append(autor)  
    return autores


# -------------- criar a string das palavra-passe --------------------------------------------------------

def criar_palavra_passe(palavras_passes): 
    keywords = ""
    for palavra in palavras_passes:
        keywords = keywords + palavra.capitalize() + "," + " "
    return keywords.strip(", ")


# ------------- doi/pdf/orcid já presentes no dataset ----------------------------------------------------

def numeros_usados(dataset, tipo):
    doi_usados = []
    pdf_usado = []
    orcid_usado = []

    if tipo == "doi":
        for artigo in dataset:
            if "doi" in artigo:
                doi = artigo["doi"] 
                doi_numeros = int(doi.split('.')[-1])
                
                doi_usados.append(doi_numeros)
        return doi_usados

    elif tipo == "pdf":
        for artigo in dataset:
            if "pdf" in artigo:
                pdf = artigo["pdf"]  
                pdf_numeros = int(pdf.split('/')[-1])
                pdf_usado.append(pdf_numeros)
        return pdf_usado

    elif tipo == "orcid":
        for artigo in dataset:
            if "authors" in artigo:
                for autor in artigo["authors"]:
                    if "orcid" in autor:  
                        orcid = autor["orcid"]
                        orcid_numeros = orcid.split('https://orcid.org/')[-1]
                        orcid_usado.append(orcid_numeros)
        return orcid_usado

# ------------- cria link do dataset ----------------------------------------------------

def link_dataset(dataset, criterio):
    cond = True
    while cond:
        if criterio == "doi":
            for artigo in dataset:
                if "doi" in artigo:
                    doi = artigo["doi"] 
                    link = doi[:29]
                    cond = False
        elif criterio == "pdf":
            for artigo in dataset:
                if "pdf" in artigo:
                    pdf = artigo["pdf"] 
                    link = pdf[:72]
                    cond = False
    return link

# ------------- doi/pdf unicos ----------------------------------------------------

def numero_unico(dataset, tipo):
    if tipo == "doi":
        numero3 = randint(10000, 99999)
        doi_usados = numeros_usados(dataset, tipo)
        while numero3 in doi_usados:
            numero3 = randint(10000, 99999)
        return numero3
    elif tipo == "pdf":
        numero4 = randint(10000, 99999)
        pdf_usados = numeros_usados(dataset, tipo)
        while numero4 in pdf_usados:
            numero4 = randint(10000, 99999)
        return numero4

# ------------- criar posts ----------------------------------------------------

def criar_post(abstrato, autores,titulo,dataset, palavras_passes, data):
    novo_registo = {}
    novo_registo["abstract"] = abstrato.capitalize()
    if palavras_passes:
        palavras_chaves = criar_palavra_passe(palavras_passes)
        novo_registo["keywords"] = palavras_chaves
    novo_registo["authors"] = autores

    link_doi = link_dataset(dataset, "doi")
    n_doi = numero_unico(dataset,"doi")
    novo_registo["doi"] = f"{link_doi}{n_doi}"

    link_pdf = link_dataset(dataset, "pdf")
    n_pdf = numero_unico(dataset,"pdf")
    novo_registo["pdf"] = f"{link_pdf}{n_doi}/{n_pdf}"

    if data:
        novo_registo["publish_date"] = data

    novo_registo["title"] = titulo.capitalize()

    novo_registo["url"] = f"{link_pdf}{n_doi}"

    dataset.append(novo_registo)

    return dataset

# ------------- mostar autores em string na listbox ----------------------------------------------------

def mostrar_na_listbox_autores(autores):
    autores_str = []
    for a in autores:
        autor_str = f"Nome: {a['name']},"  
        if "affiliation" in a:  
            autor_str += f" Afiliação: {a['affiliation']},"
        if "ORCID" in a:
            autor_str += f" ORCID: {a['ORCID'][-19:]}"
        autores_str.append(autor_str)

    return autores_str 

# ------------- remover autores na listbox ----------------------------------------------------

def remover_autores(autores, autores_str, selecionados):
    for selecionado in selecionados:
        if selecionado in autores_str:
            posicao = autores_str.index(selecionado)
            autores.remove(autores[posicao])
    return autores


# ------------- ORCID EXISTENTE ----------------------------------------------------


def ORCID_NAME(orcid, nome, dataset):
    for artigo in dataset:
        if "authors" in artigo:
            for autor in artigo["authors"]:
                if "orcid" in autor:
                    autor_orcid = autor["orcid"].split("https://orcid.org/")[-1]
                    if autor_orcid == orcid:
                        if autor["name"] != nome:
                            return False
                        else:
                            return True
    return True 
        


# ------------- DATA VALIDA ----------------------------------------------------

def eh_bissexto(ano):
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def calendário(ano,mes):
        eh_bissexto(ano)
        dias_no_mes = {1: 31,  2: 29 if eh_bissexto(ano) else 28, 3: 31,  4: 30,  5: 31,  6: 30,  7: 31,  8: 31, 9: 30, 10: 31,  11: 30,  12: 31 }
        return [x for x in range(1, dias_no_mes[mes] + 1)]


def data_valida(data):
    VALIDO_D = True 
    VALIDO_M = True 
    VALIDO_A = True  
    VALIDO_F = True  

    if len(data) < 10:
        VALIDO_F = False

    DATA = data.split("-")

    if len(DATA) != 3 or len(DATA[0]) != 4 or len(DATA[1]) != 2 or len(DATA[2]) != 2:
        VALIDO_F = False

    else:
        ano = int(DATA[0])
        mes = int(DATA[1])
        dia = int(DATA[2])


        if ano > 2025 or ano < 1950:
            VALIDO_A = False

        if mes > 12 or mes <= 0:
            VALIDO_M = False

        if VALIDO_A and VALIDO_M:
            lista_dias = calendário(ano, mes)  
            if dia not in lista_dias:
                VALIDO_D = False


    return (VALIDO_D, VALIDO_M, VALIDO_A, VALIDO_F)


# -------------------------------------------- ATUALIZAR -------------------------------------------------------------------

# ---------- ATUIALIZAR INTERFACE ----------------------------

def interface_atualizar(dataset,ficheiro):
        parametros = [
        [sg.Checkbox('Afiliação', default=False, key='-PARAMETRO1-', enable_events=True),
        sg.Checkbox('Autor', default=False, key='-PARAMETRO2-', enable_events=True),
        sg.Checkbox('Data', default=False, key='-PARAMETRO3-', enable_events=True),
        sg.Checkbox('Palavras-chave', default=False, key='-PARAMETRO4-', enable_events=True),
        sg.Checkbox('Título', default=False, key='-PARAMETRO5-', enable_events=True)],
            ]

        campos = [
            [sg.Checkbox('Resumo', default=True, key='-CAMPO_ABSTRACT-', enable_events=True),
            sg.Checkbox('Autor', default=True, key='-CAMPO_AUTOR-', enable_events=True),
            sg.Checkbox('Data', default=True, key='-CAMPO_DATA-', enable_events=True),
            sg.Checkbox('DOI', default=True, key='-CAMPO_DOI-', enable_events=True),
            sg.Checkbox('Palavra-chave', default=True, key='-CAMPO_KEY-', enable_events=True),
            sg.Checkbox('PDF', default=True, key='-CAMPO_PDF-', enable_events=True),
            sg.Checkbox('Título', default=True, key='-CAMPO_TITULO-', enable_events=True),
            sg.Checkbox('URL', default=True, key='-CAMPO_URL-', enable_events=True)]
        ]

        ordenar = [
            [sg.Radio('Não Ordenar', '-ORDENAR-', key='-NAO_ORDENAR-', enable_events=True),
            sg.Radio('Título (A-Z)', '-ORDENAR-', key='-ORDENAR_TITULO_AZ-', enable_events=True),
            sg.Radio('Título (Z-A)', '-ORDENAR-', key='-ORDENAR_TITULO_ZA-', enable_events=True),
            sg.Radio('Data (mais recente para mais antigo)', '-ORDENAR-', key='-ORDENAR_DATA_RA-', enable_events=True),
            sg.Radio('Data (mais antigo para mais recente)', '-ORDENAR-', key='-ORDENAR_DATA_AR-', enable_events=True)],
        ]

        # Layout da janela
        layout = [
            [sg.Frame('Parametros de Pesquisa', parametros, font=('Helvetica', 13))],
            [sg.Text(" ")],
            [sg.Text('Afiliação:', font=('Helvetica', 15)), sg.Input(size=(85, 10), key='-AFILIACAO-'), sg.Button('Carregar Afiliação')],
            [sg.Button('Eliminar Última Afiliacao'), sg.Button('Eliminar Lista de Afiliações')],
            [sg.Text('Nome do Autor:', font=('Helvetica', 15)), sg.Input(size=(79, 10), key='-AUTORES-'), sg.Button('Carregar Autor')],
            [sg.Button('Eliminar Último Autor'), sg.Button('Eliminar Lista de Autores')],
            [sg.Text('Insira o intervalo de datas:', font=('Helvetica', 15))],
            [sg.Input(key='-DATA1-', size=(10, 1), readonly=True), sg.CalendarButton(button_text='Data de início', target='-DATA1-', format='%Y-%m-%d', key='-CALENDAR1-'),
            sg.Input(key='-DATA2-', size=(10, 1), readonly=True), sg.CalendarButton(button_text='Data de fim', target='-DATA2-', format='%Y-%m-%d', key='-CALENDAR2-')],
            [sg.Text('Palavra-chave:', font=('Helvetica', 15)), sg.Input(key='-KEYWORD-', size=(73, 10)), sg.Button('Carregar Palavra-Chave')],
            [sg.Button('Eliminar Última Palavra-Chave'), sg.Button('Eliminar Lista de Palavras-Chave')],
            [sg.Text('Título', font=('Helvetica', 15)), sg.Input(key='-TITULO-', size=(92, 10)), sg.Button('Carregar Título')],
            [sg.Frame('Ordenar Publicações', ordenar, font=('Helvetica', 13))],
            [sg.Button('PESQUISAR')],
            [sg.Text(" ")],
            [sg.Frame('Campos a listar', campos, font=('Helvetica', 13))],
            [sg.Listbox(values=[], size=(114, 10), key='-LISTA_PUBLICACOES-', horizontal_scroll=True, enable_events=True, select_mode=sg.LISTBOX_SELECT_MODE_SINGLE)],
            [sg.Button("Atualizar", key = "-ATUALIZAR-"), sg.Button("Ver Detalhes", key = "-DETALHES-"), sg.Button('GUARDAR'), sg.Button("Sair", key="-SAIR1-")]]



        window = sg.Window('Pesquisar Publicações para atualizar', layout, resizable=True, finalize=True, modal = True)

        # Loop de eventos
        afiliacao = []
        autores = []
        keywords = []
        data_inicio = ''
        data_fim = ''
        publicacoes = []
        titulo = ''
        pub_aux = []

        pesquisar = True
        while pesquisar:
            event, values = window.read()
            if event in [sg.WINDOW_CLOSED, "-SAIR1-"]:
                pesquisar = False
                window.close()

            elif event == 'PESQUISAR' and not values['-PARAMETRO1-'] and not values['-PARAMETRO2-'] and not values['-PARAMETRO3-'] and not values['-PARAMETRO4-'] and not values['-PARAMETRO5-']:
                sg.popup(f"Não selecionou nenhum parâmetro para efetuar a pesquisa", title='Aviso')

            elif event == 'PESQUISAR' and not values['-NAO_ORDENAR-'] and not values['-ORDENAR_DATA_RA-'] and not values['-ORDENAR_DATA_AR-'] and not values['-ORDENAR_TITULO_AZ-'] and not values['-ORDENAR_TITULO_ZA-']:
                sg.popup('Por favor, selecione uma opção de ordenação.', title='Aviso')

            elif event == 'Carregar Afiliação':
                afiliacao.append(values['-AFILIACAO-'])
                sg.popup(f"Inseriu {values['-AFILIACAO-']} aos filtros de pesquisa. Já inseriu {len(afiliacao)} afiliações", title='Aviso')
                window['-AFILIACAO-'].update('')
            elif event == 'Eliminar Última Afiliacao':
                afiliacao = afiliacao[:-1]
            elif event == 'Eliminar Lista de Afiliações':
                afiliacao = []

            elif event == 'Carregar Autor':
                autores.append(values['-AUTORES-'])
                sg.popup(f"Inseriu {values['-AUTORES-']} aos filtros de pesquisa. Já inseriu {len(autores)} autores", title='Aviso')
                window['-AUTORES-'].update('')
            elif event == 'Eliminar Último Autor':
                autores = autores[:-1]
            elif event == 'Eliminar Lista de Autores':
                autores = []

            elif event == 'Carregar Palavra-Chave':
                keywords.append(values['-KEYWORD-'])
                sg.popup(f"Inseriu {values['-KEYWORD-']} aos filtros de pesquisa. Já inseriu {len(keywords)} keywords", title='Aviso')
                window['-KEYWORD-'].update('')
            elif event == 'Eliminar Última Palavra-Chave':
                keywords = keywords[:-1]
            elif event == 'Eliminar Lista de Palavras-Chave':
                keywords = []

            elif event == 'Carregar Título':
                titulo = values['-TITULO-']
                window['-TITULO-'].update('')

            elif event == '-ORDENAR_TITULO_AZ-' and publicacoes != []:
                publicacoes_ordenadas = ordenaTitulo(publicacoes, False)
                titulos_publicacoes = titulos(publicacoes_ordenadas)
                window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
            elif event == '-ORDENAR_TITULO_ZA-' and publicacoes != []:
                publicacoes_ordenadas = ordenaTitulo(publicacoes, True)
                titulos_publicacoes = titulos(publicacoes_ordenadas)
                window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
            elif event == '-ORDENAR_DATA_RA-' and publicacoes != []:
                publicacoes_ordenadas = ordenaData(publicacoes, True)
                titulos_publicacoes = titulos(publicacoes_ordenadas)
                window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
            elif event == '-ORDENAR_DATA_AR-' and publicacoes != []:
                publicacoes_ordenadas = ordenaData(publicacoes, False)
                titulos_publicacoes = titulos(publicacoes_ordenadas)
                window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)

            elif event == 'PESQUISAR':
                cond = True
                parametros_selecionados = True
                info_text = ("- Ver Detalhes: Clique neste botão para visualizar todas as informações sobre o artigo selecionado na lista.\n\n"
                    "- Atualizar: Selecione um artigo da lista e clique neste botão para alterá-lo. \n\n"
                    "- Guardar: Clique neste botão para salvar todos os artigos que estão atualmente exibidos na listbox. Isso garantirá que todos os itens visíveis na listbox sejam armazenados.À frente encontra-se uma caixa de texto para nomear o ficheiro."
                    )

                sg.popup("Instruções para Gerenciamento de Artigos", info_text)

                if values['-PARAMETRO1-']:   #afiliacao
                    if afiliacao != []:
                        afili_publicacoes = consultar_afiliacao(dataset, afiliacao)
                        if afili_publicacoes == []:
                            cond = False
                        else:
                            pub_aux.append(afili_publicacoes)
                    else:
                        sg.popup('Por favor, insira uma afiliação.', title='Aviso')
                        cond = False
                        parametros_selecionados = False

                if values['-PARAMETRO2-'] and cond: #autor
                    if autores != []:
                        autor_publicacoes = consultar_autores(dataset, autores)
                        if autor_publicacoes == []:
                            cond = False
                        else:
                            pub_aux.append(autor_publicacoes)
                    else:
                        sg.popup('Por favor, insira um autor.', title='Aviso')
                        cond = False
                        parametros_selecionados = False

                if values['-PARAMETRO3-'] and cond: #data
                    data_inicio = values['-DATA1-']
                    data_fim = values['-DATA2-']
                    if data_inicio > data_fim:
                        sg.popup('As datas que inseriu não estão válidas', 'Erro')
                        cond = False
                        parametros_selecionados = False
                    elif data_inicio != '' and data_fim != '':
                        data_publicacoes = consultar_data(dataset, data_inicio, data_fim)
                        if data_publicacoes == []:
                            cond = False
                        else:
                            pub_aux.append(data_publicacoes)
                    elif data_inicio == '' and data_fim == '':
                        sg.popup("Não inseriu nenhuma data", title='Aviso')
                        parametros_selecionados = False
                        cond = False
                    elif data_fim == '' or data_inicio == '':
                        sg.popup("Não inseriu uma das datas", title='Aviso')
                        parametros_selecionados = False
                        cond = False

                if values['-PARAMETRO4-'] and cond: #palavra-chave
                    if keywords != []:
                        keywords_publicacoes = consultar_keywords(dataset, keywords)
                        if keywords_publicacoes == []:
                            cond = False
                        else:
                            pub_aux.append(keywords_publicacoes)
                    else:
                        sg.popup('Por favor, insira uma palavra-chave.', title='Aviso')
                        cond = False
                        parametros_selecionados = False

                if values['-PARAMETRO5-'] and cond: #titulo
                    if titulo != '':
                        titulo_publicacoes = consultar_titulo(dataset, titulo)
                        if titulo_publicacoes == []:
                            cond = False
                        else:
                            pub_aux.append(titulo_publicacoes)
                    else:
                        sg.popup('Por favor, insira um titulo.', title='Aviso')
                        cond = False
                        parametros_selecionados = False

                if cond:
                    if len(pub_aux) == 1:
                        publicacoes = pub_aux[0]
                    else:
                        publicacoes = comuns(pub_aux)

                    if publicacoes != []:
                        if values['-NAO_ORDENAR-']:
                            titulos_publicacoes = titulos(publicacoes)
                            window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
                        else:
                            if values['-ORDENAR_DATA_RA-']:
                                publicacoes_ordenadas = ordenaData(publicacoes, True)
                            elif values['-ORDENAR_DATA_AR-']:
                                publicacoes_ordenadas = ordenaData(publicacoes, False)
                            elif values['-ORDENAR_TITULO_AZ-']:
                                publicacoes_ordenadas = ordenaTitulo(publicacoes, False)
                            elif values['-ORDENAR_TITULO_ZA-']:
                                publicacoes_ordenadas = ordenaTitulo(publicacoes, True)
                            titulos_publicacoes = titulos(publicacoes_ordenadas)
                            window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
                    else:
                        cond = False

                if cond == False and parametros_selecionados:
                    sg.popup("Não foram encontradas publicações.", title = 'Aviso')
                    window['-LISTA_PUBLICACOES-'].update([])
                    publicacoes = []


                pub_aux = []

            elif event == 'GUARDAR' and publicacoes != []:
                nome = sg.popup_get_file("Salvar como Ficheiro JSON", save_as=True, no_window=True, file_types=(('JSON', '*.json'),), title= "Salvar JSON")
                guardar_json(publicacoes, nome)
                sg.popup('O ficheiro foi guardado com sucesso')

            elif event == '-DETALHES-' and publicacoes != []:
                publicacao_selecionada = values['-LISTA_PUBLICACOES-']
                if not publicacao_selecionada:
                    sg.popup("Nenhum artigo selecionado. Por favor, selecione um artigo.", title="Erro")
                else:
                    publicacao_selecionada =  values['-LISTA_PUBLICACOES-'][0]
                    publicacao = encontra_publicacao(publicacoes, publicacao_selecionada)
                    abrir_janela_publicacao(publicacao,values['-CAMPO_ABSTRACT-'], values['-CAMPO_AUTOR-'], values['-CAMPO_DATA-'], values['-CAMPO_DOI-'], values['-CAMPO_PDF-'], values['-CAMPO_URL-'], values['-CAMPO_TITULO-'], values['-CAMPO_KEY-'])

            elif event == '-ATUALIZAR-' and publicacoes != []:
                Artigo_selecionado =  values['-LISTA_PUBLICACOES-']
                if not Artigo_selecionado:
                    sg.popup("Nenhum artigo selecionado. Por favor, selecione um artigo.", title="Erro")
                else:
                    Artigo_selecionado =  values['-LISTA_PUBLICACOES-'][0]
                    artigo = encontra_publicacao(publicacoes, Artigo_selecionado)

                    palavras_chave  = artigo.get("keywords", "")
                    if palavras_chave:  
                        palavras_chave = [palavra.strip() for palavra in palavras_chave.split(",")]
                    else:
                        palavras_chave = []

                    autores = artigo.get("authors", [])
                    autores_str = [ f'Nome: {autor.get("name", "N/A")}, Afiliação: {autor.get("affiliation", "N/A")}, ORCID: {autor.get("ORCID", "N/A")[-19:]}'
                        for autor in artigo.get("authors", [])]

                    layout_atualizar = [
                        [sg.Text('Atualização da Publicação', font=('Helvetica', 16, "bold"), justification='center', expand_x=True)],

                        [sg.Text('Resumo', size=(15, 1), font=('Helvetica', 12, "bold"))],
                        [sg.Multiline(default_text=artigo.get("abstract", ""), key='-ABSTRATO-', size=(60, 5), expand_x=True)],

                        [sg.Text('')],

                        [sg.Text('Palavras-Chave:', font=('Helvetica', 12, "bold"), pad=(0, 0)), 
                        sg.Text(' adiciona uma de cada vez', font=('Helvetica', 10), pad=(0, 0))],
                        [sg.InputText( key='-PALAVRA-', size=(40, 1), expand_x=True, enable_events=True),
                        sg.Button('Adicionar', key='-ADICIONAR_PALAVRA-', size=(10, 1)),
                        sg.Button('Remover', key='-REMOVER_PALAVRA-', size=(10, 1))],
                        [sg.Listbox(values=palavras_chave, key='-PALAVRAS_LIST-', size=(60, 5), enable_events=True,
                                    select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, expand_x=True)],

                        [sg.Text('')],

                        [sg.Text('Autores:', font=('Helvetica', 12, "bold"), pad=(0, 0)),
                        sg.Text(' adiciona um de cada vez', font=('Helvetica', 10), pad=(0, 0))],
                        [sg.Text('Nome:', font=('Helvetica', 10)), sg.InputText(key='-NOME-', size=(40, 1), expand_x=True)],
                        [sg.Text('Afiliação:', font=('Helvetica', 10)), sg.InputText(key='-AFILIACAO-', size=(40, 1), expand_x=True)],
                        [sg.Text('Orcid:', font=('Helvetica', 10)), sg.InputText(key='-ORCID-', size=(40, 1), expand_x=True, enable_events=True)],
                        [sg.Button('Adicionar', key='-ADICIONAR_AUTOR-', size=(10, 1), expand_x=True),
                        sg.Button('Remover', key='-REMOVER_AUTOR-', size=(10, 1), expand_x=True)],
                        [sg.Listbox(values=autores_str , key='-AUTORES_LIST-', size=(60, 5), enable_events=True,
                                    select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, expand_x=True, horizontal_scroll=True)],

                        [sg.Text('')],

                        [sg.Text('Título:', size=(4, 1), font=('Helvetica', 12, "bold")), sg.InputText(artigo.get("title",""), key='-TITULO-', size=(50, 1), expand_x=True)],
                        [sg.Text('Data de Publicação:', size=(15, 1), font=('Helvetica', 12, "bold")), sg.Input(artigo.get("publish_date",""), key='-DATA-', size=(20, 1), expand_x=True, enable_events=True ),
                        sg.CalendarButton('Selecionar', target='-DATA-', format='%Y-%m-%d')],
                    
                        [sg.Text('')],

                        [sg.Button('Salvar', key='-SALVAR-', size=(15, 1), expand_x=True), sg .Button('Cancelar', key='-CANCELAR-', size=(15, 1), expand_x=True)]
                    ]

                    # Janela
                    window_atualizar = sg.Window('Atualização de Publicação', layout_atualizar, location=(470,0))

                    stop1 = False
                    while not stop1:
                        event1, values1 = window_atualizar.read()

                        if event1 == sg.WINDOW_CLOSED or event1 == '-CANCELAR-':
                            stop1 = True
                            window_atualizar.close()

                        elif event1 == '-PALAVRA-':
                            texto_atual = values1['-PALAVRA-']
                            texto_filtrado = texto_atual.rstrip(",.")
                            if texto_filtrado != texto_atual:
                                window_atualizar['-PALAVRA-'].update(texto_filtrado)
                        

                        elif event1 == '-ORCID-' and len(values1["-ORCID-"]):
                            orcid_text = values1["-ORCID-"]
                        
                            if len(orcid_text) in [4, 9, 14]:  
                                window_atualizar["-ORCID-"].update(orcid_text + "-")
                        
                            elif len(orcid_text) > 19:
                                window_atualizar["-ORCID-"].update(orcid_text[:-1])
                            
                            elif len(orcid_text) == 19 and orcid_text[-1] not in "0123456789X":
                                window_atualizar["-ORCID-"].update(orcid_text[:-1])

                            elif len(orcid_text) < 19:
                                if "-" in orcid_text:
                                    ORCID = orcid_text.split("-")
                                    for elem in ORCID:
                                        for digito in elem:
                                            if digito not in "0123456789":
                                                window_atualizar["-ORCID-"].update(orcid_text[:-1])
                                else:
                                    for digito in orcid_text:
                                        if digito not in "0123456789":
                                            window_atualizar["-ORCID-"].update(orcid_text[:-1])

                        elif event1 == "-DATA-":
                            data = values1["-DATA-"]  

                            if len(data) in [4, 7]: 
                                window_atualizar["-DATA-"].update(data + "-")

                            if any(char not in "0123456789-" for char in data):
                                window_atualizar["-DATA-"].update(data[:-1])

                            if len(data) > 10:
                                window_atualizar["-DATA-"].update(data[:-1])


                        elif event1 == '-ADICIONAR_AUTOR-':
                            nome = values1['-NOME-']
                            afiliacao = values1['-AFILIACAO-'] if values1['-AFILIACAO-'] else None  
                            orcid = values1['-ORCID-'] if values1['-ORCID-'] else None

                            if not nome: 
                                sg.popup_error("Por favor, insira o nome do autor.", title='Erro')
                            else:
                                if orcid and len(orcid) < 19:
                                    sg.popup_error(f" O ORCID ({orcid}) é invalido. Ele deve conter exatamente 19 caracteres no formato: 0000-0000-0000-0000.", title='Erro')
                                
                                elif orcid and not ORCID_NAME(orcid, nome, dataset):
                                    sg.popup_error(f"Esse ORCID já está associado a outro autor! Por favor, tente novamente.", title='Erro')
                                

                                else:
                                    autores = criar_autor(nome,autores, afiliacao, orcid)
                                    autores_str = mostrar_na_listbox_autores(autores)
                                    window_atualizar['-AUTORES_LIST-'].update(autores_str)
                                    # para limpar os campos:
                                    window_atualizar['-NOME-'].update('')
                                    window_atualizar['-AFILIACAO-'].update('')
                                    window_atualizar['-ORCID-'].update('')


                        elif event1 == '-REMOVER_AUTOR-':
                            selecionado = values1['-AUTORES_LIST-']
                            if selecionado:
                                autores = remover_autores(autores, autores_str, selecionado)
                                autores_str = mostrar_na_listbox_autores(autores)
                                window_atualizar['-AUTORES_LIST-'].update(autores_str)
                            else:
                                sg.popup_error("Por favor, selecione um autor para remover.", title='Erro')


                        elif event1 == '-ADICIONAR_PALAVRA-':
                            palavra = values1['-PALAVRA-']
                            if palavra:
                                palavras_chave.append(palavra.strip())
                                window_atualizar['-PALAVRAS_LIST-'].update(palavras_chave)
                                window_atualizar['-PALAVRA-'].update('')
                            else:
                                sg.popup_error("Por favor, insira uma palavra-chave válida.", title='Erro')

                        
                        elif event1 == '-REMOVER_PALAVRA-':
                            selecionada = values1['-PALAVRAS_LIST-']
                            if selecionada:
                                palavras_chave.remove(selecionada[0])
                                window_atualizar['-PALAVRAS_LIST-'].update(palavras_chave)
                            else:
                                sg.popup_error("Por favor, selecione uma palavra-chave para remover.", title='Erro')


                        elif event1 == '-SALVAR-':
                            titulo = values1['-TITULO-']
                            data = values1['-DATA-']
                            abstrato = values1['-ABSTRATO-']

                            if data:
                                d,m,a,f = data_valida(data)

                                dia = int(data.split("-")[2])
                                mes = int(data.split("-")[1])
                                ano = int(data.split("-")[0])

                                if d == False:
                                    lista_dias = calendário(ano,mes)
                                    sg.popup_error(f"Dia inválido. Por favor, escreva um dia entre {lista_dias[0]} and {lista_dias[-1]}")

                                elif f == False:
                                    sg.popup_error(f"Formato inválido! Você digitou: {data}. Por favor, insira a data no formato correto: ano-mês-dia (exemplo: 2023-05-03).", title='Erro')

                                elif m == False:
                                    sg.popup_error(f"Mês invalido: {mes}. Por favor, escreva um mês entre 1 e 12.", title='Erro')

                                elif a == False:
                                    sg.popup_error(f"Ano inválido: {ano}. Por favor, insira um ano entre 1950 e o ano atual.", title='Erro')

                                else:
                                    if not autores:
                                        sg.popup_error("Por favor, adicione pelo menos um autor.", title='Erro')
                                    elif not titulo:
                                        sg.popup_error("Por favor, forneça um título.", title='Erro')
                                    elif not abstrato:
                                        sg.popup_error("Por favor, forneça um resumo.", title='Erro')
                                    else:
                                                            doi = artigo.get("doi")
                                                            dataset = atualizar_dataset(abstrato, autores, titulo, dataset, palavras_chave, data, doi, artigo)

                                                            try:
                                                                with open(ficheiro, "w", encoding="utf-8") as f:
                                                                    json.dump(dataset, f, ensure_ascii=False, indent=4)
                                                                    print("Publicação atualizada com sucesso!")
                                                                    sg.popup(
                                                                        "Registo Salvo com Sucesso!",
                                                                        f"Título: {titulo}",
                                                                        f"Data: {data}",
                                                                        f"Resumo: {abstrato[:200]}...",
                                                                        f"Palavras-Chave: {criar_palavra_passe(palavras_chave)}",
                                                                        f"Autores: {', '.join([autor['name'] for autor in autores])}",
                                                                    )

                                                            except Exception as e:
                                                                sg.popup_error(f"Erro ao atualizar no arquivo: {e}")
                                                                print("Erro ao atualizar publicação.")

                                                            afiliacao = []
                                                            autores = []
                                                            keywords = []
                                                            data_inicio = ''
                                                            data_fim = ''
                                                            publicacoes = []
                                                            titulo = ''
                                                            pub_aux = []
                                                            window['-LISTA_PUBLICACOES-'].update([])
                                                            stop1 = True
                                                            window_atualizar.close()

                            else:
                                    if not autores:
                                        sg.popup_error("Por favor, adicione pelo menos um autor.", title='Erro')
                                    elif not titulo:
                                        sg.popup_error("Por favor, forneça um título.", title='Erro')
                                    elif not abstrato:
                                        sg.popup_error("Por favor, forneça um resumo.", title='Erro')
                                    else:
                                        doi = artigo.get("doi")
                                        dataset = atualizar_dataset(abstrato, autores, titulo, dataset, palavras_chave, data, doi, artigo)
                                        
                                        try:
                                            with open(ficheiro, "w", encoding="utf-8") as f:
                                                json.dump(dataset, f, ensure_ascii=False, indent=4)
                                                sg.popup(
                                                                        "Registo Salvo com Sucesso!",
                                                                        f"Título: {titulo}",
                                                                        f"Data: {data}",
                                                                        f"Resumo: {abstrato[:200]}...",
                                                                        f"Palavras-Chave: {criar_palavra_passe(palavras_chave)}",
                                                                        f"Autores: {', '.join([autor['name'] for autor in autores])}",
                                                                    )
                                                print("Publicação atualizada com sucesso!")
                                        except Exception as e:
                                                sg.popup_error(f"Erro ao atualizar no arquivo: {e}")
                                                print("Erro ao atualizar publicação.")
                                        
                                        afiliacao = []
                                        autores = []
                                        keywords = []
                                        data_inicio = ''
                                        data_fim = ''
                                        publicacoes = []
                                        titulo = ''
                                        pub_aux = []
                                        window['-LISTA_PUBLICACOES-'].update([])
                                        stop1 = True
                                        window_atualizar.close()






# ------ atualizar o dataset ------------------------

def atualizar_dataset(abstrato, autores, titulo, dataset, palavras_chave, data,doi,artigo):
    dic = {}
    for artigo in dataset:
        if artigo.get("doi") == doi:
            dic["abstract"] = abstrato.capitalize()
            if palavras_chave:
                dic["keywords"] = criar_palavra_passe(palavras_chave)
            dic["authors"] = autores
            if "doi" in artigo:
                dic["doi"] = artigo["doi"]
            if "pdf" in artigo:
                dic["pdf"] = artigo["pdf"]
            if data:
                dic["publish_date"] = data
            dic["title"] = titulo.capitalize()
            if "url" in artigo:
                dic["url"] = artigo["url"]
            dataset.remove(artigo)
            dataset.append(dic)
    return dataset 

# -------------------------------------------- CONSULTAR -------------------------------------------------------------------

def interface_consultar(dataset):
    parametros = [
        [sg.Checkbox('Afiliação', default=False, key='-PARAMETRO1-', enable_events=True),
        sg.Checkbox('Autor', default=False, key='-PARAMETRO2-', enable_events=True),
        sg.Checkbox('Data', default=False, key='-PARAMETRO3-', enable_events=True),
        sg.Checkbox('Palavras-chave', default=False, key='-PARAMETRO4-', enable_events=True),
        sg.Checkbox('Título', default=False, key='-PARAMETRO5-', enable_events=True)],
            ]

    campos = [
            [sg.Checkbox('Resumo', default=True, key='-CAMPO_ABSTRACT-', enable_events=True),
            sg.Checkbox('Autor', default=True, key='-CAMPO_AUTOR-', enable_events=True),
            sg.Checkbox('Data', default=True, key='-CAMPO_DATA-', enable_events=True),
            sg.Checkbox('DOI', default=True, key='-CAMPO_DOI-', enable_events=True),
            sg.Checkbox('Palavra-chave', default=True, key='-CAMPO_KEY-', enable_events=True),
            sg.Checkbox('PDF', default=True, key='-CAMPO_PDF-', enable_events=True),
            sg.Checkbox('Título', default=True, key='-CAMPO_TITULO-', enable_events=True),
            sg.Checkbox('URL', default=True, key='-CAMPO_URL-', enable_events=True)]
        ]

    ordenar = [
            [sg.Radio('Título (A-Z)', '-ORDENAR-', key='-ORDENAR_TITULO_AZ-', enable_events=True),
            sg.Radio('Título (Z-A)', '-ORDENAR-', key='-ORDENAR_TITULO_ZA-', enable_events=True),
            sg.Radio('Data (mais recente para mais antigo)', '-ORDENAR-', key='-ORDENAR_DATA_RA-', enable_events=True),
            sg.Radio('Data (mais antigo para mais recente)', '-ORDENAR-', key='-ORDENAR_DATA_AR-', enable_events=True)],
        ]

        # Layout da janela
    layout = [
            [sg.Frame('Parametros de Pesquisa', parametros, font = ('Helvetica', 13))],
            [sg.Text(" ")],
            [sg.Text('Afiliação:', font = ('Helvetica', 15)), sg.Input(size=(70, 10), key='-AFILIACAO-'), sg.Button('Carregar Afiliação')], 
            [sg.Button('Eliminar Última Afiliacao'), sg.Button('Eliminar Lista de Afiliações')],
            [sg.Text('Nome do Autor:', font = ('Helvetica', 15)), sg.Input(size = (64, 10), key = '-AUTORES-'), sg.Button('Carregar Autor')],
            [sg.Button('Eliminar Último Autor'), sg.Button('Eliminar Lista de Autores')],
            [sg.Text('Insira o intervalo de datas:', font = ('Helvetica', 15))], 
            [sg.Input(key='-DATA1-', size=(10, 1), readonly=True), sg.CalendarButton(button_text='Data de início', target='-DATA1-', format='%Y-%m-%d', key='-CALENDAR1-'), 
            sg.Input(key='-DATA2-', size=(10, 1), readonly=True), sg.CalendarButton(button_text='Data de fim', target='-DATA2-', format='%Y-%m-%d', key='-CALENDAR2-')],
            [sg.Text('Palavra-chave:', font = ('Helvetica', 15)), sg.Input(key= '-KEYWORD-', size=(58, 10)), sg.Button('Carregar Palavra-Chave')],
            [sg.Button('Eliminar Última Palavra-Chave'), sg.Button('Eliminar Lista de Palavras-Chave')],
            [sg.Text('Título', font = ('Helvetica', 15)), sg.Input(key = '-TITULO-', size=(76, 10)), sg.Button('Carregar Título')],
            [sg.Frame('Ordenar Publicações', ordenar, font = ('Helvetica', 13))],
            [sg.Button('PESQUISAR')],
            [sg.Text(" ")],
            [sg.Frame('Campos a listar', campos, font = ('Helvetica', 13))],
            [sg.Listbox(values=[], size=(99, 10), key='-LISTA_PUBLICACOES-', horizontal_scroll=True, enable_events=True)],
            [sg.Button('GUARDAR')],
            [sg.Button("Sair",key = "-SAIR-")]
        ]

    # Criação da janela
    window = sg.Window('Pesquisar Publicações', layout)


    # Loop de eventos
    afiliacao = []
    autores = []
    keywords = []
    data_inicio = ''
    data_fim = ''
    publicacoes = []
    titulo = ''
    pub_aux = []

    pesquisar = True
    while pesquisar:
        event, values = window.read()
        if event in [sg.WINDOW_CLOSED, "-SAIR-"]:
            pesquisar = False

        elif event == 'PESQUISAR' and not values['-PARAMETRO1-'] and not values['-PARAMETRO2-'] and not values['-PARAMETRO3-'] and not values['-PARAMETRO4-'] and not values['-PARAMETRO5-']:
            sg.popup(f"Não selecionou nenhum parâmetro para efetuar a pesquisa", title='Aviso')

        elif event == 'PESQUISAR' and not values['-ORDENAR_DATA_RA-'] and not values['-ORDENAR_DATA_AR-'] and not values['-ORDENAR_TITULO_AZ-'] and not values['-ORDENAR_TITULO_ZA-']:
            sg.popup('Por favor, selecione uma opção de ordenação.', title='Aviso')

        elif event == 'Carregar Afiliação':
            afiliacao.append(values['-AFILIACAO-'])
            sg.popup(f"Inseriu {values['-AFILIACAO-']} aos filtros de pesquisa. Já inseriu {len(afiliacao)} afiliações", title='Aviso')
            window['-AFILIACAO-'].update('')
        elif event == 'Eliminar Última Afiliacao':
            afiliacao = afiliacao[:-1]
        elif event == 'Eliminar Lista de Afiliações':
            afiliacao = []

        elif event == 'Carregar Autor':
            autores.append(values['-AUTORES-'])
            sg.popup(f"Inseriu {values['-AUTORES-']} aos filtros de pesquisa. Já inseriu {len(autores)} autores", title='Aviso')
            window['-AUTORES-'].update('')
        elif event == 'Eliminar Último Autor':
            autores = autores[:-1]
        elif event == 'Eliminar Lista de Autores':
            autores = []

        elif event == 'Carregar Palavra-Chave':
            keywords.append(values['-KEYWORD-'])
            sg.popup(f"Inseriu {values['-KEYWORD-']} aos filtros de pesquisa. Já inseriu {len(keywords)} keywords", title='Aviso')
            window['-KEYWORD-'].update('')
        elif event == 'Eliminar Última Palavra-Chave':
            keywords = keywords[:-1]
        elif event == 'Eliminar Lista de Palavras-Chave':
            keywords = []

        elif event == 'Carregar Título':
            titulo = values['-TITULO-']
            window['-TITULO-'].update('')

        elif event == '-ORDENAR_TITULO_AZ-' and publicacoes != []:
            publicacoes_ordenadas = ordenaTitulo(publicacoes, False)
            titulos_publicacoes = titulos(publicacoes_ordenadas)
            window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
        elif event == '-ORDENAR_TITULO_ZA-' and publicacoes != []:
            publicacoes_ordenadas = ordenaTitulo(publicacoes, True)
            titulos_publicacoes = titulos(publicacoes_ordenadas)
            window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
        elif event == '-ORDENAR_DATA_RA-' and publicacoes != []:
            publicacoes_ordenadas = ordenaData(publicacoes, True)
            titulos_publicacoes = titulos(publicacoes_ordenadas)
            window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
        elif event == '-ORDENAR_DATA_AR-' and publicacoes != []:
            publicacoes_ordenadas = ordenaData(publicacoes, False)
            titulos_publicacoes = titulos(publicacoes_ordenadas)
            window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)

        elif event == 'PESQUISAR':
            cond = True
            parametros_selecionados = True
            if values['-PARAMETRO1-']:   #afiliacao
                if afiliacao != []:
                    afili_publicacoes = consultar_afiliacao(dataset, afiliacao)
                    if afili_publicacoes == []:
                        cond = False
                    else:
                        pub_aux.append(afili_publicacoes)
                else:
                    sg.popup('Por favor, insira uma afiliação.', title='Aviso')
                    cond = False
                    parametros_selecionados = False

            if values['-PARAMETRO2-'] and cond: #autor
                if autores != []:
                    autor_publicacoes = consultar_autores(dataset, autores)
                    if autor_publicacoes == []:
                        cond = False
                    else:
                        pub_aux.append(autor_publicacoes)
                else:
                    sg.popup('Por favor, insira um autor.', title='Aviso')
                    cond = False
                    parametros_selecionados = False

            if values['-PARAMETRO3-'] and cond: #data
                data_inicio = values['-DATA1-']
                data_fim = values['-DATA2-']
                if data_inicio > data_fim:
                    sg.popup('As datas que inseriu não estão válidas', title = 'Erro')
                    cond = False
                    parametros_selecionados = False
                elif data_inicio != '' and data_fim != '':
                    data_publicacoes = consultar_data(dataset, data_inicio, data_fim)
                    if data_publicacoes == []:
                        cond = False
                    else:
                        pub_aux.append(data_publicacoes)
                elif data_inicio == '' and data_fim == '':
                    sg.popup("Não inseriu nenhuma data", title='Aviso')
                    parametros_selecionados = False
                    cond = False
                elif data_fim == '' or data_inicio == '':
                    sg.popup("Não inseriu uma das datas", title='Aviso')
                    parametros_selecionados = False
                    cond = False

            if values['-PARAMETRO4-'] and cond: #palavra-chave
                if keywords != []:
                    keywords_publicacoes = consultar_keywords(dataset, keywords)
                    if keywords_publicacoes == []:
                        cond = False
                    else:
                        pub_aux.append(keywords_publicacoes)
                else:
                    sg.popup('Por favor, insira uma palavra-chave.', title='Aviso')
                    parametros_selecionados = False
                    cond = False

            if values['-PARAMETRO5-'] and cond: #titulo
                if titulo != '':
                    titulo_publicacoes = consultar_titulo(dataset, titulo)
                    if titulo_publicacoes == []:
                        cond = False
                    else:
                        pub_aux.append(titulo_publicacoes)
                else:
                    sg.popup('Por favor, insira um titulo.', title='Aviso')
                    cond = False
                    parametros_selecionados = False

            if cond:
                if len(pub_aux) == 1:
                    publicacoes = pub_aux[0]
                else:
                    publicacoes = comuns(pub_aux)

                if publicacoes != []:
                    if values['-ORDENAR_DATA_RA-']:
                        publicacoes_ordenadas = ordenaData(publicacoes, True)
                    elif values['-ORDENAR_DATA_AR-']:
                        publicacoes_ordenadas = ordenaData(publicacoes, False)
                    elif values['-ORDENAR_TITULO_AZ-']:
                        publicacoes_ordenadas = ordenaTitulo(publicacoes, False)
                    elif values['-ORDENAR_TITULO_ZA-']:
                        publicacoes_ordenadas = ordenaTitulo(publicacoes, True)
                    titulos_publicacoes = titulos(publicacoes_ordenadas)
                    window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
                else:
                    cond = False

            if cond == False and parametros_selecionados:
                sg.popup("Não foram encontradas publicações.", title = 'Aviso')
                window['-LISTA_PUBLICACOES-'].update([])
                publicacoes = []


            pub_aux = []

        elif event == '-LISTA_PUBLICACOES-' and publicacoes != []:
            publicacao_selecionada =  values['-LISTA_PUBLICACOES-'][0]
            publicacao = encontra_publicacao(publicacoes, publicacao_selecionada)
            abrir_janela_publicacao(publicacao,values['-CAMPO_ABSTRACT-'], values['-CAMPO_AUTOR-'], values['-CAMPO_DATA-'], values['-CAMPO_DOI-'], values['-CAMPO_PDF-'], values['-CAMPO_URL-'], values['-CAMPO_TITULO-'], values['-CAMPO_KEY-'])

        elif event == 'GUARDAR' and publicacoes != []:
            nome = sg.popup_get_file("Salvar como Ficheiro JSON", save_as=True, no_window=True, file_types=(('JSON', '*.json'),), title= "Salvar JSON")
            guardar_json(publicacoes, nome)
            sg.popup('O ficheiro foi guardado com sucesso')


    window.close()



def consultar_afiliacao(dataset, afiliacao):
    res = []

    afiliacao = [str.lower() for str in afiliacao]
    for publicacao in dataset:
        aux = []
        listaAutores = publicacao["authors"]
        i = 0
        while i < len(listaAutores) and len(aux) < len(afiliacao):
            autor = listaAutores[i]

            if autor.get("affiliation") is not None:
                afili_autor = autor['affiliation'].lower().split('.')

                for afili in afili_autor:
                    for afili_pesquisa in afiliacao:
                        if afili_pesquisa in afili and afili_pesquisa not in aux:
                            aux.append(afili_pesquisa)
            i = i + 1
        if len(aux) == len(afiliacao):
            res.append(publicacao)

    return res

def consultar_autores(dataset, autores):
    res = []
    autores = [nome.lower() for nome in autores]
    for publicacao in dataset:
        aux = []
        listaAutores = publicacao["authors"]
        i = 0
        nomeAutores = [autor['name'].lower() for autor in listaAutores]
        while i < len(nomeAutores) and len(aux) < len(autores):
            a = 0
            while a < len(autores):
                if autores[a] in nomeAutores[i] and autores[a] not in aux:
                    aux.append(autores[a])
                    a = len(autores)
                a = a + 1
            i = i + 1
        
        if len(aux) == len(autores):
            res.append(publicacao)
    return res

def consultar_data(dataset, data1, data2):
    res = []
    for publicacao in dataset:
        if publicacao.get("publish_date") is not None and publicacao["publish_date"] > data1 and publicacao['publish_date'] < data2:
            res.append(publicacao)
    return res

def consultar_keywords(dataset, keywords):
    res = []
    keywords = [pal.lower() for pal in keywords]
    for publicacao in dataset:
        if publicacao.get("keywords"):
            aux = []
            i = 0
            keywordsPubl = publicacao["keywords"].lower()
            while i < len(keywords) and len(aux) < len(keywords):
                if keywords[i] in keywordsPubl:   
                    aux.append(keywords[i])
                i = i + 1
    
            if len(aux) == len(keywords):
                res.append(publicacao)
            
    return res

def consultar_titulo(dataset, titulo):
    res = []
    for publicacao in dataset:
        if publicacao.get("title") and titulo.lower() in publicacao["title"].lower():
            res.append(publicacao)
    return res




def titulos(publicacoes):
    res = []
    for publicacao in publicacoes:
        if publicacao.get('title') is not None:
            res.append(publicacao['title'])
        else:
            res.append(publicacao['abstract'][:200])
    return res

def encontra_publicacao(lista, titulo):
    i = 0
    cond = True
    res = {}
    while i < len(lista) and cond == True:
        publicacao = lista[i]
        if publicacao.get('title') == titulo or titulo in publicacao.get('abstract'):
            res = publicacao
            cond = False
        i = i + 1
    return res

def ordenaTitulo(publicacoes, decrescente):
    return sorted(publicacoes, key=lambda x: x.get('title', ''), reverse = decrescente)

def ordenaData(publicacoes, decrescente):
    return sorted(publicacoes, key=lambda x: x.get('publish_date', ''), reverse = decrescente)

def comuns(lista_pub):
    res = lista_pub[0]
    for lista in lista_pub[1:]:
        res = [pub for pub in res if pub in lista]

    return res


def guardar_json(lista, nome):
    with open(nome, 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)

#Funções janela
def listaAutores(autores):
    res = []
    for autor in autores:
        if autor.get('name'):
            res.append(autor['name'])
        if autor.get('affiliation'):
            res.append(f"Afiliação: {autor['affiliation']}")
        if autor.get('orcid'):
            res.append(f"Orcid: {autor['orcid']}")
    return res


def abrir_janela_publicacao(publicacao, abstract, autores, data, doi, pdf, url, title, keyword):
    keyword_adicionada = False
    
    layout_publ = []
    if title:
        layout_publ = adicionar_campo(layout_publ, publicacao, 'title', 'Título')
            
    if abstract:
        if publicacao.get('abstract') is not None and publicacao.get('abstract')[:21] != 'Resumo Palavras-chave':
            layout_publ.append([sg.Text("Resumo", font=('Helvetica', 15))])
            layout_publ.append([sg.Multiline(publicacao['abstract'], size=(75, 5), disabled=True, no_scrollbar=False, font=('Helvetica', 13))])
       
        elif publicacao.get('abstract') and publicacao.get('abstract')[:21] == 'Resumo Palavras-chave':
            if publicacao.get('keywords') is None and keyword:
                layout_publ.append([sg.Text('Palavras-chave', font=('Helvetica', 15))])
                layout_publ.append([sg.Text(publicacao['abstract'][23:], size=(72, None), font=('Helvetica', 13))])
                keyword_adicionada = True
        else:
            layout_publ.append([sg.Text("Resumo", font=('Helvetica', 15))])
            layout_publ.append([sg.Text(f'A publicação não apresenta resumo', font=('Helvetica', 11))])
    
    
    if not abstract and publicacao.get('abstract') and publicacao.get('abstract')[:21] == 'Resumo Palavras-chave':
        layout_publ.append([sg.Text('Palavras-chave', font=('Helvetica', 15))])
        layout_publ.append([sg.Text(publicacao['abstract'][23:], size=(75, None), font=('Helvetica', 13))])    
    elif keyword and not keyword_adicionada:
        layout_publ = adicionar_campo(layout_publ, publicacao, 'keywords', 'Palavras-Chave')
    
        
        
    if autores:
        layout_publ.append([sg.Text('Autores', font=('Helvetica', 15))])
        if publicacao.get('authors') is not None:
            autores = listaAutores(publicacao['authors'])
            layout_publ.append([sg.Listbox(values=autores, size=(75, 5), key='-LISTA_AUTORES-', horizontal_scroll=True, font=('Helvetica', 13), enable_events=False)])
            
        else:
                layout_publ.append([sg.Text('A publicação não apresenta autores', font=('Helvetica', 13))])
        
    if data:
        layout_publ = adicionar_campo(layout_publ, publicacao, 'publish_date', 'Data')
        
    if doi:
        layout_publ = adicionar_campo(layout_publ, publicacao, 'doi', 'DOI')
     
    if pdf:
        layout_publ = adicionar_campo(layout_publ, publicacao, 'pdf', 'PDF')
            
    if url:
        layout_publ = adicionar_campo(layout_publ, publicacao, 'url', 'URL')
                    
    layout_publ.append([sg.Button('Fechar')])

    janela_publicacao = sg.Window("Publicação", layout_publ, modal=True, font=('Helvetica', 20), location=(200, 200))  # Modal é uma janela que vai abrir em cima da outra

    stop = False
    while not stop:
        event, _ = janela_publicacao.read()
        if event in [sg.WINDOW_CLOSED, 'Fechar']:
            stop = True

    janela_publicacao.close()



def adicionar_campo(layout, publicacao, campo, titulo):
    layout.append([sg.Text(titulo, font=('Helvetica', 15))])
    if publicacao.get(campo):
        layout.append([sg.Text(publicacao[campo], size=(72, None), font=('Helvetica', 13))])
    else:
        layout.append([sg.Text(f'A publicação não apresenta {titulo.lower()}', font=('Helvetica', 13))])

    return layout


# --------------------------------------------------------  GRAFICOS  ------------------------------------------------------------

# ------------ INTERFACE GRAFICOS ---------------------------------------------

def interface_estatistica(dataset):
    Tipos_graficos = ["Distribuição de publicações por ano","Distribuição de publicações por mês de um determinado ano","Número de publicações por autor (top 20 autores)","Distribuição de publicações de um autor por anos","Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave)","Distribuição de palavras-chave mais frequente por ano"]

    layout = [
        [sg.Text("Selecione o gráfico que quer visualizar:", font=("Helvetica", 16), background_color='#aab6d3')],
        [sg.Combo(values=Tipos_graficos, default_value="Distribuição de publicações por ano", key='-GRAFH-', readonly=True, size=(30, 1),  expand_x=True) ],
        [sg.Button("Confirmar", key = '-CONFIRMAR-'), sg.Button("Sair", key = '-SAIR-')]]


    sg.theme('LightBlue2')


    window = sg.Window("Escolha do Gráfico", layout, size=(600, 100))


    stop = False
    while not stop:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "-SAIR-":
            stop = True
    
        if event == '-CONFIRMAR-':
            selected_grafh = values['-GRAFH-']
            if selected_grafh == Tipos_graficos[0]:
                distribuicao = dataspub(dataset)
                grafico_dataspub(dataset)

            if selected_grafh == Tipos_graficos[1]:
                ano_desejado = sg.popup_get_text(
                    "Digite o ano que deseja analisar:",
                    title="Entrada de texto")
                if ano_desejado != None:  
                    criargrafh(dataset,ano_desejado)


            if selected_grafh == Tipos_graficos[2]:
                grafico_TP20_autores2(dataset)

            if selected_grafh == Tipos_graficos[3]:
                autor_desejado = sg.popup_get_text("Digite o autor que deseja analisar:", title = "Entrada de texto")
                if autor_desejado != None:  
                    grafico1(dataset,autor_desejado)

            if selected_grafh == Tipos_graficos[4]:
                distribuicao_keywords(dataset)

            if selected_grafh == Tipos_graficos[5]:
                ano_desejado = sg.popup_get_text("Digite o ano que deseja analisar:", title = "Entrada de texto")
                if ano_desejado != None:  
                    distribuicao_keywords_ano(dataset,ano_desejado)


    window.close()

# ---------- Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave) ---------------------

def distribuicao_keywords(dataset):
    keywords_cont = {}
    for publicacao in dataset:
        keywords = publicacao.get("keywords")
        if keywords:
            for keyword in keywords.split(', '):
                if keywords_cont.get(keyword):
                    keywords_cont[keyword] = keywords_cont[keyword] + 1
                else:
                    keywords_cont[keyword] = 1

    keywords_ord = sorted(list(keywords_cont.items()), key = lambda x : x[1], reverse = True)
    distrib = dict(keywords_ord[:20])

    
    x = list(distrib.keys())
    y = list(distrib.values())

    plt.xlabel('Frequência')
    plt.ylabel('Keywords')
    plt.title('Top 20 Palavras-Chave')

    cores = ['Navy','RoyalBlue', 'SteelBlue']
    plt.barh(x,y, color = cores)
    plt.show()


# --------------- Distribuição de palavras-chave mais frequente por ano ---------------

def distribuicao_keywords_ano(data, anoPesquisa):
    keywords_cont = {}
    for publicacao in data:
        keywords = publicacao.get('keywords')
        publish_date = publicacao.get('publish_date')
        if publish_date and keywords:
            date = publish_date.split('-')
            if date[0] == anoPesquisa:
                for keyword in keywords.split(', '):
                    if keywords_cont.get(keyword):
                        keywords_cont[keyword] = keywords_cont[keyword] + 1
                    else:
                        keywords_cont[keyword] = 1

    if keywords_cont != {}:
        keywords_ord = sorted(list(keywords_cont.items()), key = lambda x : x[1], reverse = True)

        if len(keywords_ord) >= 20:
            top = dict(keywords_ord[:20])
            x = list(top.keys())
            y = list(top.values())

            plt.xlabel('Frequência')
            plt.ylabel('Keywords')
            plt.title(f"Top 20 Palavras-Chave de {anoPesquisa}")


            cores = ['Navy','RoyalBlue', 'SteelBlue']
            plt.barh(x,y, color = cores)
            plt.show()

        else:
            top = dict(keywords_ord)
            x = list(top.keys())
            y = list(top.values())

            plt.xlabel('Frequência')
            plt.ylabel('Keywords')
            plt.title(f"Top {len(top)} Palavras-Chave de {anoPesquisa}")

            cores = ['Navy','RoyalBlue', 'SteelBlue']
            plt.barh(x,y, color = cores)
            plt.show()

    else:
        return sg.popup(f"Não existem publicações no ano {anoPesquisa} com keywords", title="Erro")


# ---------------- Número de publicações por autor (top 20 autores) -------------------------------------

def conta_publicações_autor_top20(dataset):
    dic = {}
    for artigo in dataset:
        if "authors" in artigo:
            for author in artigo["authors"]:
                if author["name"] not in dic:
                    dic[author["name"]] = 1
                else:
                    dic[author["name"]] += 1
    lista = sorted(dic.items(), key=lambda par: par[1],reverse = True)
    return lista[:20]

# CRIAR GRAFICOS
def grafico_TP20_autores2(dataset):
    lista = conta_publicações_autor_top20(dataset)
    if lista == None:
        return 
    else:
        x = [autor for autor,n in lista]
        y = [n for autor,n in lista]

        plt.figure(figsize=(12, 6)) 
        plt.barh(x, y,color='skyblue') 
        plt.xlabel("Autores")
        plt.ylabel("Número de publicações")
        plt.title("Top 20 Autores por número de Publicações")
        cores = ['Navy','RoyalBlue', 'SteelBlue']
        plt.barh(x,y, color = cores)
        plt.show()

# ------------- Distribuição de publicações de autores por ano -----------------

# para caso o nome estiver em diversos autores
def escolha_autor(possiveis_autores):
    layout = [
        [sg.Text("Selecione o autor desejado:")],
        [sg.Listbox( values=possiveis_autores, size=(50, 10),select_mode='single', key='autor')],
        [sg.Button("Confirmar", key = "-CONFIRMAR-"), sg.Button("Cancelar", key = "-CANCELAR-")]
    ]

    window_lista = sg.Window("Escolha do Autor", layout)

    autor = None
    stop = False
    while not stop:
        event, values = window_lista.read()
        if event == sg.WINDOW_CLOSED or event == "-CANCELAR-":
            stop = True
            window_lista.close()
        if event == "-CONFIRMAR-":
            autor_selecionado = values['autor']
            if autor_selecionado:  
                autor = autor_selecionado[0]  
                stop = True
        window_lista.close()
        return autor

def distribuicao_autor_ano(dataset, autor):
    dic = {}
    autores_correspondentes = []
    for artigo in dataset:
        if "authors" in artigo:
            for author in artigo["authors"]:
                if autor.strip().lower() in author["name"].strip().lower():
                    if author["name"] not in autores_correspondentes:
                        autores_correspondentes.append(author["name"])

    if len(autores_correspondentes) == 0:
        sg.popup(f"Não existe nenhum artigo com este(a) autor(a): {autor}", title="Erro")
        return None
    elif len(autores_correspondentes) > 1:
        autor_selecionado = escolha_autor(autores_correspondentes)
        if not autor_selecionado:
            return None
    else:
        autor_selecionado = autores_correspondentes[0]  

    for artigo in dataset:
        if "authors" in artigo:
            for author in artigo["authors"]:
                if author["name"] == autor_selecionado:
                    if "publish_date" in artigo:
                        data = artigo["publish_date"][:4]
                        if data not in dic:
                            dic[data] = 1
                        else:
                            dic[data] += 1

    if len(dic) == 0:
        sg.popup(f"Artigos associados ao autor(a) {autor_selecionado} não possuem data de publicação", title="Erro")

    lista = sorted(dic.items(), key=lambda par: par[0])
    return lista

# CRIAR GRAFICOS
def grafico1(dataset, autor):
    lista = distribuicao_autor_ano(dataset, autor)
    if not lista:
        return None
    else:
        ano = [ano for ano, n in lista]
        numero_publicacoes = [n for ano, n in lista]
        nome_formatado = autor.title()

        plt.figure(figsize=(8, 8))
        plt.plot(ano, numero_publicacoes, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
        plt.xlabel("Anos")
        plt.ylabel("Número de publicações")
        plt.title(f"Distribuição de Publicações por Ano do(a) autor(a) {nome_formatado}", fontsize=14)
        plt.show()

# ----------- Distribuição de publicações por ano ---------------

def dataspub(dataset):
    distrib = {}
    for artigo in dataset:
        if "publish_date" in artigo:
            data = artigo["publish_date"]
            ano = data[:4]
            if ano not in distrib:
                distrib[ano] = 1
            else:
                distrib[ano] = distrib[ano] + 1
    return distrib

# CRIAR GRAFICOS
def grafico_dataspub(dataset):
    distribuicao = dataspub(dataset)
    datas = sorted(distribuicao.keys())
    valores = [distribuicao[ano] for ano in datas]

    colors = ['Navy', 'RoyalBlue', 'SteelBlue'] * (len(datas) // 3 + 1)  
    plt.figure(figsize=(10, 6))
    bars = plt.bar(datas, valores, color=colors[:len(datas)])

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.3, int(yval), ha='center', va='bottom', fontsize=10)

    plt.title('Distribuição de Publicações por Ano', fontsize=14)
    plt.xlabel('Ano de Publicação', fontsize=12)
    plt.ylabel('Número de Publicações', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.tight_layout()

    plt.show()

# --------------- Distribuição de publicações por mês de um determinado ano --------------

def meseano(ata_médica,ano_desejado):
  distrib = {}
  for artigo in ata_médica:
    if "publish_date" in artigo:
      data = artigo["publish_date"]
      ano = data[:4]
      if ano == ano_desejado:
        mes = int(data[5:7])
        if mes not in distrib:
          distrib[mes] = 1
        else:
          distrib[mes] = distrib[mes] + 1
  return distrib

# CRIAR GRAFICOS
def criargrafh(ata_médica,ano_desejado):
    distribuicao = meseano(ata_médica,ano_desejado)
    if len(distribuicao) == 0:
        sg.popup(f"Não existe nenhum artigo correspondente ao ano {ano_desejado}", title = "Erro")
    else:
        meses = [i for i in range (1,13)]
        nomes_mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        valores = [distribuicao.get(mes, 0) for mes in meses]

        cores = ['Navy', 'RoyalBlue', 'SteelBlue'] * (len(meses) // 3 + 1)  # Repetir as cores conforme necessário
        plt.figure(figsize=(10, 6))
        bars = plt.bar(nomes_mes, valores, color=cores[:len(meses)])

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, int(yval), ha='center', va='bottom', fontsize=10)

        plt.title(f"Distribuição de Publicações por meses do ano {ano_desejado}", fontsize=14)
        plt.xlabel('Mês', fontsize=12)
        plt.ylabel('Número de Publicações', fontsize=12)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.tight_layout()

        plt.show()


# --------------------------------------------- REMOVER -------------------------------------------------------------------

# ---------------- interface remover ------------------------

def interface_remover(dataset,ficheiro):
    parametros = [
    [sg.Checkbox('Afiliação', default=False, key='-PARAMETRO1-', enable_events=True),
     sg.Checkbox('Autor', default=False, key='-PARAMETRO2-', enable_events=True),
     sg.Checkbox('Data', default=False, key='-PARAMETRO3-', enable_events=True),
     sg.Checkbox('Palavras-chave', default=False, key='-PARAMETRO4-', enable_events=True),
     sg.Checkbox('Título', default=False, key='-PARAMETRO5-', enable_events=True)],
]


    campos = [
        [sg.Checkbox('Resumo', default=True, key='-CAMPO_ABSTRACT-', enable_events=True),
        sg.Checkbox('Autor', default=True, key='-CAMPO_AUTOR-', enable_events=True),
        sg.Checkbox('Data', default=True, key='-CAMPO_DATA-', enable_events=True),
        sg.Checkbox('DOI', default=True, key='-CAMPO_DOI-', enable_events=True),
        sg.Checkbox('Palavra-chave', default=True, key='-CAMPO_KEY-', enable_events=True),
        sg.Checkbox('PDF', default=True, key='-CAMPO_PDF-', enable_events=True),
        sg.Checkbox('Título', default=True, key='-CAMPO_TITULO-', enable_events=True),
        sg.Checkbox('URL', default=True, key='-CAMPO_URL-', enable_events=True)]
    ]

    ordenar = [
        [sg.Radio('Não Ordenar', '-ORDENAR-', key='-NAO_ORDENAR-', enable_events=True),
        sg.Radio('Título (A-Z)', '-ORDENAR-', key='-ORDENAR_TITULO_AZ-', enable_events=True),
        sg.Radio('Título (Z-A)', '-ORDENAR-', key='-ORDENAR_TITULO_ZA-', enable_events=True),
        sg.Radio('Data (mais recente para mais antigo)', '-ORDENAR-', key='-ORDENAR_DATA_RA-', enable_events=True),
        sg.Radio('Data (mais antigo para mais recente)', '-ORDENAR-', key='-ORDENAR_DATA_AR-', enable_events=True)],
    ]


    layout = [
        [sg.Frame('Parametros de Pesquisa', parametros, font=('Helvetica', 13))],
        [sg.Text(" ")],
        [sg.Text('Afiliação:', font=('Helvetica', 15)), sg.Input(size=(85, 10), key='-AFILIACAO-'), sg.Button('Carregar Afiliação')],
        [sg.Button('Eliminar Última Afiliacao'), sg.Button('Eliminar Lista de Afiliações')],
        [sg.Text('Nome do Autor:', font=('Helvetica', 15)), sg.Input(size=(79, 10), key='-AUTORES-'), sg.Button('Carregar Autor')],
        [sg.Button('Eliminar Último Autor'), sg.Button('Eliminar Lista de Autores')],
        [sg.Text('Insira o intervalo de datas:', font=('Helvetica', 15))],
        [sg.Input(key='-DATA1-', size=(10, 1), readonly=True), sg.CalendarButton(button_text='Data de início', target='-DATA1-', format='%Y-%m-%d', key='-CALENDAR1-'),
        sg.Input(key='-DATA2-', size=(10, 1), readonly=True), sg.CalendarButton(button_text='Data de fim', target='-DATA2-', format='%Y-%m-%d', key='-CALENDAR2-')],
        [sg.Text('Palavra-chave:', font=('Helvetica', 15)), sg.Input(key='-KEYWORD-', size=(73, 10)), sg.Button('Carregar Palavra-Chave')],
        [sg.Button('Eliminar Última Palavra-Chave'), sg.Button('Eliminar Lista de Palavras-Chave')],
        [sg.Text('Título', font=('Helvetica', 15)), sg.Input(key='-TITULO-', size=(92, 10)), sg.Button('Carregar Título')],
        [sg.Frame('Ordenar Publicações', ordenar, font=('Helvetica', 13))],
        [sg.Button('PESQUISAR')],
        [sg.Text(" ")],
        [sg.Frame('Campos a listar', campos, font=('Helvetica', 13))],
        [sg.Listbox(values=[], size=(114, 10), key='-LISTA_PUBLICACOES-', horizontal_scroll=True, enable_events=True, select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE)],
        [sg.Button("Remover", key = "-REMOVER-"), sg.Button("Ver Detalhes", key = "-DETALHES-"), sg.Button('GUARDAR'), sg.Button("Sair", key="-SAIR-")]]



    window = sg.Window('Pesquisar Publicações para remover', layout, resizable=True, finalize=True)

    afiliacao = []
    autores = []
    keywords = []
    data_inicio = ''
    data_fim = ''
    publicacoes = []
    titulo = ''
    pub_aux = []

    pesquisar = True
    while pesquisar:
        event, values = window.read()
        if event in [sg.WINDOW_CLOSED, "-SAIR-"]:
            pesquisar = False
            window.close()

        elif event == 'PESQUISAR' and not values['-PARAMETRO1-'] and not values['-PARAMETRO2-'] and not values['-PARAMETRO3-'] and not values['-PARAMETRO4-'] and not values['-PARAMETRO5-']:
            sg.popup(f"Não selecionou nenhum parâmetro para efetuar a pesquisa", title='Aviso')

        elif event == 'PESQUISAR' and not values['-NAO_ORDENAR-'] and not values['-ORDENAR_DATA_RA-'] and not values['-ORDENAR_DATA_AR-'] and not values['-ORDENAR_TITULO_AZ-'] and not values['-ORDENAR_TITULO_ZA-']:
            sg.popup('Por favor, selecione uma opção de ordenação.', title='Aviso')

        elif event == 'Carregar Afiliação':
            afiliacao.append(values['-AFILIACAO-'])
            sg.popup(f"Inseriu {values['-AFILIACAO-']} aos filtros de pesquisa. Já inseriu {len(afiliacao)} afiliações", title='Aviso')
            window['-AFILIACAO-'].update('')
        elif event == 'Eliminar Última Afiliacao':
            afiliacao = afiliacao[:-1]
        elif event == 'Eliminar Lista de Afiliações':
            afiliacao = []

        elif event == 'Carregar Autor':
            autores.append(values['-AUTORES-'])
            sg.popup(f"Inseriu {values['-AUTORES-']} aos filtros de pesquisa. Já inseriu {len(autores)} autores", title='Aviso')
            window['-AUTORES-'].update('')
        elif event == 'Eliminar Último Autor':
            autores = autores[:-1]
        elif event == 'Eliminar Lista de Autores':
            autores = []

        elif event == 'Carregar Palavra-Chave':
            keywords.append(values['-KEYWORD-'])
            sg.popup(f"Inseriu {values['-KEYWORD-']} aos filtros de pesquisa. Já inseriu {len(keywords)} keywords", title='Aviso')
            window['-KEYWORD-'].update('')
        elif event == 'Eliminar Última Palavra-Chave':
            keywords = keywords[:-1]
        elif event == 'Eliminar Lista de Palavras-Chave':
            keywords = []

        elif event == 'GUARDAR' and publicacoes != []:
            nome = sg.popup_get_file("Salvar como Ficheiro JSON", save_as=True, no_window=True, file_types=(('JSON', '*.json'),), title= "Salvar JSON")
            guardar_json(publicacoes, nome)
            sg.popup('O ficheiro foi guardado com sucesso')

        elif event == 'Carregar Título':
            titulo = values['-TITULO-']
            window['-TITULO-'].update('')

        elif event == '-ORDENAR_TITULO_AZ-' and publicacoes != []:
                publicacoes_ordenadas = ordenaTitulo(publicacoes, False)
                titulos_publicacoes = titulos(publicacoes_ordenadas)
                window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
        elif event == '-ORDENAR_TITULO_ZA-' and publicacoes != []:
                publicacoes_ordenadas = ordenaTitulo(publicacoes, True)
                titulos_publicacoes = titulos(publicacoes_ordenadas)
                window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
        elif event == '-ORDENAR_DATA_RA-' and publicacoes != []:
                publicacoes_ordenadas = ordenaData(publicacoes, True)
                titulos_publicacoes = titulos(publicacoes_ordenadas)
                window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
        elif event == '-ORDENAR_DATA_AR-' and publicacoes != []:
                publicacoes_ordenadas = ordenaData(publicacoes, False)
                titulos_publicacoes = titulos(publicacoes_ordenadas)
                window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)


        elif event == 'PESQUISAR':
            cond = True
            parametros_selecionados = True
            info_text = (
        "- Ver Detalhes: Clique neste botão para visualizar todas as informações sobre o artigo selecionado na lista.\n\n"
        "- Remover: Selecione um ou mais artigos na lista e clique neste botão para removê-los permanentemente.\n\n"
        "- Guardar: Clique neste botão para salvar todos os artigos que estão atualmente exibidos na listbox. Isso garantirá que todos os itens visíveis na listbox sejam armazenados.À frente encontra-se uma caixa de texto para nomear o ficheiro."
    )
            sg.popup("Instruções para Gerenciamento de Artigos", info_text)
            if values['-PARAMETRO1-']:   #afiliacao
                if afiliacao != []:
                    afili_publicacoes = consultar_afiliacao(dataset, afiliacao)
                    if afili_publicacoes == []:
                        cond = False
                    else:
                        pub_aux.append(afili_publicacoes)
                else:
                    sg.popup('Por favor, insira uma afiliação.', title='Aviso')
                    cond = False
                    parametros_selecionados = False

            if values['-PARAMETRO2-'] and cond: #autor
                if autores != []:
                    autor_publicacoes = consultar_autores(dataset, autores)
                    if autor_publicacoes == []:
                        cond = False
                    else:
                        pub_aux.append(autor_publicacoes)
                else:
                    sg.popup('Por favor, insira um autor.', title='Aviso')
                    cond = False
                    parametros_selecionados = False

            if values['-PARAMETRO3-'] and cond: #data
                data_inicio = values['-DATA1-']
                data_fim = values['-DATA2-']
                if data_inicio > data_fim:
                    sg.popup('As datas que inseriu não estão válidas', title = 'Erro')
                    cond = False
                    parametros_selecionados = False
                elif data_inicio != '' and data_fim != '':
                    data_publicacoes = consultar_data(dataset, data_inicio, data_fim)
                    if data_publicacoes == []:
                        cond = False
                    else:
                        pub_aux.append(data_publicacoes)
                elif data_inicio == '' and data_fim == '':
                    sg.popup("Não inseriu nenhuma data", title='Aviso')
                    parametros_selecionados = False
                    cond = False
                elif data_fim == '' or data_inicio == '':
                    sg.popup("Não inseriu uma das datas", title='Aviso')
                    parametros_selecionados = False
                    cond = False

            if values['-PARAMETRO4-'] and cond: #palavra-chave
                if keywords != []:
                    keywords_publicacoes = consultar_keywords(dataset, keywords)
                    if keywords_publicacoes == []:
                        cond = False
                    else:
                        pub_aux.append(keywords_publicacoes)
                else:
                    sg.popup('Por favor, insira uma palavra-chave.', title='Aviso')
                    parametros_selecionados = False
                    cond = False

            if values['-PARAMETRO5-'] and cond: #titulo
                if titulo != '':
                    titulo_publicacoes = consultar_titulo(dataset, titulo)
                    if titulo_publicacoes == []:
                        cond = False
                    else:
                        pub_aux.append(titulo_publicacoes)
                else:
                    sg.popup('Por favor, insira um titulo.', title='Aviso')
                    cond = False
                    parametros_selecionados = False

            if cond:
                if len(pub_aux) == 1:
                    publicacoes = pub_aux[0]
                else:
                    publicacoes = comuns(pub_aux)

                if publicacoes != []:
                    if values['-NAO_ORDENAR-']:
                        titulos_publicacoes = titulos(publicacoes)
                        window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
                    else:
                        if values['-ORDENAR_DATA_RA-']:
                            publicacoes_ordenadas = ordenaData(publicacoes, True)
                        elif values['-ORDENAR_DATA_AR-']:
                            publicacoes_ordenadas = ordenaData(publicacoes, False)
                        elif values['-ORDENAR_TITULO_AZ-']:
                            publicacoes_ordenadas = ordenaTitulo(publicacoes, False)
                        elif values['-ORDENAR_TITULO_ZA-']:
                            publicacoes_ordenadas = ordenaTitulo(publicacoes, True)
                        titulos_publicacoes = titulos(publicacoes_ordenadas)
                        window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
                else:
                    cond = False

            if cond == False and parametros_selecionados:
                sg.popup("Não foram encontradas publicações.", title = 'Aviso')
                window['-LISTA_PUBLICACOES-'].update([])
                publicacoes = []


            pub_aux = []


        elif event == '-DETALHES-' and publicacoes != []:
            publicacao_selecionada = values['-LISTA_PUBLICACOES-']
            if not publicacao_selecionada:
                sg.popup("Nenhum artigo selecionado. Por favor, selecione um artigo.", title="Erro")
            if publicacao_selecionada:
                if len(publicacao_selecionada) > 1:
                    sg.popup("Selecione somente um artigo para ver os detalhes.", title="Erro")
                else:
                    publicacao_selecionada = values['-LISTA_PUBLICACOES-'][0]
                    publicacao = encontra_publicacao(publicacoes, publicacao_selecionada)
                    abrir_janela_publicacao(publicacao,values['-CAMPO_ABSTRACT-'], values['-CAMPO_AUTOR-'], values['-CAMPO_DATA-'], values['-CAMPO_DOI-'], values['-CAMPO_PDF-'], values['-CAMPO_URL-'], values['-CAMPO_TITULO-'], values['-CAMPO_KEY-'])


        elif event == '-REMOVER-' and publicacoes != []:
            artigo_selecionado =  values['-LISTA_PUBLICACOES-']
            if artigo_selecionado:
                resposta = sg.popup_yes_no( f"Tem certeza de que deseja remover os seguintes artigos?\n\n- " + "\n\n- ".join(artigo_selecionado), title="Confirmar Remoção")
                if resposta == "Yes":
                    try: 
                        dataset = remover_artigos(dataset, publicacoes, artigo_selecionado)
                        with open(ficheiro, "w", encoding="utf-8") as f:
                            json.dump(dataset, f, ensure_ascii=False, indent=4)

                        continuar = sg.popup_yes_no("Artigos removidos com sucesso, deseja continuar? ", title="Remoção Completa")
                        if continuar == "No":
                            window.close()
                        else:
                            for artigo in artigo_selecionado:
                                artigo = encontra_publicacao(publicacoes,artigo)
                                publicacoes.remove(artigo)
                            titulos_publicacoes = titulos(publicacoes)
                            window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)
                            print(f"Remoção bem-sucedida! -- Nºde publicações removidas: {len(artigo_selecionado)}")

                    except ValueError as e:
                        sg.popup_error(f"Erro ao remover artigos: {e}", title="Erro de Remoção")
                        print("Erro ao remover publicações.")

            else:
                sg.popup_error("Nenhum artigo foi selecionado para remoção.", title="Erro de Remoção")


# ----------- REMOVER ARTIGOS ----------------------------
def remover_artigos(dataset, publicacoes, artigo_selecionado):
    SELECIONADOS = []
    for artigo in artigo_selecionado:
        selecionado = encontra_publicacao(publicacoes, artigo)
        SELECIONADOS.append(selecionado)
    for selecionado in SELECIONADOS:
        dataset.remove(selecionado)
    return dataset

# --------------   IMPORTAR E CARREGAR FICHEIROS ------------------------------------

def importar_ficheiro(dados_existentes,novos_registos):
    if len(novos_registos) == 0:
        sg.popup("Nenhum registo foi encontrado.", title = "Erro")
        return dados_existentes
    elif not isinstance(dados_existentes,list) or not isinstance(novos_registos,list):
        sg.popup("Os ficheiros não possuem a mesma estrutura.", title = "Erro")
        return dados_existentes
    else:
        dados_existentes = dados_existentes + novos_registos
        sg.popup("Os novos registos foram adicionados com sucesso.", title = "Sucesso")
        return dados_existentes


def carregar_arquivo_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, encoding='utf-8') as f:
            ata_médica = json.load(f)
            print("O seu arquivo foi carregado com sucesso.")
            return ata_médica
    except FileNotFoundError:
        print("Erro: O seu arquivo não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro: O seu arquivo não está em um formato JSON válido.")
        return None

def carregar_arquivo_json2(caminho_arquivo):
    try:
        with open(caminho_arquivo, encoding='utf-8') as f:
            dataset = json.load(f)
            return dataset
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

# ------------------------------------------------ ANÁLISE ---------------------------------------------------------


# ------------- interfase analisar -----------------

def interface_analise(dataset):
    ordenar = [
    sg.Radio('Alfabético (A-Z)', '-ORDENAR-', key = '-ORDENAR_TITULO_AZ-', enable_events = True),
    sg.Radio('Alfabético (Z-A)', '-ORDENAR-', key = '-ORDENAR_TITULO_ZA-', enable_events = True),
    sg.Radio('Frequência(mais para menos frequente)', '-ORDENAR-', key='-ORD_FREQ_MAIS_MENOS-', enable_events = True),
    sg.Radio('Frequência(menos para mais frequente)', '-ORDENAR-', key='-ORD_FREQ_MENOS_MAIS-', enable_events = True)
    ]

    campos= [
        [sg.Checkbox('Resumo', default=True, key='-CAMPO_ABSTRACT-', enable_events=True), sg.Checkbox('Autor', default=True, key='-CAMPO_AUTOR-', enable_events=True),
        sg.Checkbox('Data', default=True, key='-CAMPO_DATA-', enable_events=True), sg.Checkbox('DOI', default=True, key='-CAMPO_DOI-', enable_events=True),
        sg.Checkbox('Palavra-chave', default=True, key='-CAMPO_KEY-', enable_events=True),
        sg.Checkbox('PDF', default=True, key='-CAMPO_PDF-', enable_events=True), sg.Checkbox('Título', default=True, key='-CAMPO_TITULO-', enable_events=True),
        sg.Checkbox('URL', default=True, key='-CAMPO_URL-', enable_events=True)]

    ]

    layout = [
    [sg.Text('Análise de ', font=('helsetica', 15)), sg.Combo([ 'Autores','Palavras-Chave'], key='-OPCOES-', default_value='Selecione', readonly=True)],
    [sg.Frame('Ordenar', [[*ordenar]], font = ('Helvetica', 13))],
    [sg.Button('LISTAR')],
    [sg.Listbox(values=[], size=(110, 10), key='-LISTA-', horizontal_scroll=True, enable_events=True)],
    [sg.Frame('Campos a listar', campos, font = ('Helvetica', 13))],
    [sg.Text('Lista de Publicações', font=('Helvetica', 15))],
    [sg.Listbox(values=[], size=(110, 10), key='-LISTA_PUBLICACOES-', horizontal_scroll=True, enable_events=True)],
    [sg.Button('GUARDAR')],
    [sg.Button("Sair",key = "-SAIR-")]
]

    window = sg.Window('Análise', layout)


    resultado_pesquisa = {}
    resultado_nome = []
    resultado_ordenado = []
    publicacoes = []

    stop = True
    while stop:
        event, values = window.read()
        if event in [sg.WINDOW_CLOSED, "-SAIR-"]:
            stop = False

        elif event == 'LISTAR' and not values['-ORDENAR_TITULO_AZ-'] and not values['-ORDENAR_TITULO_ZA-'] and not values['-ORD_FREQ_MAIS_MENOS-'] and not values['-ORD_FREQ_MENOS_MAIS-']:
            sg.popup('Selecione um parâmetro de ordenação', title='Aviso')

        elif values['-OPCOES-'] == 'Autores' and event == 'LISTAR':
            resultado_pesquisa = contar_autores(dataset)
            if resultado_pesquisa != {}:
                if values['-ORDENAR_TITULO_AZ-']:
                    resultado_ordenado = ordena_alfabetico(resultado_pesquisa, False)
                elif values['-ORDENAR_TITULO_ZA-']:
                    resultado_ordenado = ordena_alfabetico(resultado_pesquisa, True)
                elif values['-ORD_FREQ_MAIS_MENOS-']:
                    resultado_ordenado = ordena_frequencia(resultado_pesquisa, True)
                elif values['-ORD_FREQ_MENOS_MAIS-']:
                    resultado_ordenado = ordena_frequencia(resultado_pesquisa, False)

                window['-LISTA-'].update(resultado_ordenado)


        elif values['-OPCOES-'] == 'Palavras-Chave' and event == 'LISTAR':
            resultado_pesquisa = contar_keywords(dataset)
            if resultado_pesquisa != {}:
                if values['-ORDENAR_TITULO_AZ-']:
                    resultado_ordenado = ordena_alfabetico(resultado_pesquisa, False)
                elif values['-ORDENAR_TITULO_ZA-']:
                    resultado_ordenado = ordena_alfabetico(resultado_pesquisa, True)
                elif values['-ORD_FREQ_MAIS_MENOS-']:
                    resultado_ordenado = ordena_frequencia(resultado_pesquisa, True)
                elif values['-ORD_FREQ_MENOS_MAIS-']:
                    resultado_ordenado = ordena_frequencia(resultado_pesquisa, False)

                window['-LISTA-'].update(resultado_ordenado)


        elif event == '-LISTA-' and resultado_pesquisa:
            resultado_selecionado = values['-LISTA-'][0]
            publicacoes = resultado_pesquisa[resultado_selecionado]
            window['-LISTA_PUBLICACOES-'].update(titulos(publicacoes))


        elif event == '-LISTA_PUBLICACOES-' and publicacoes != []:
            publicacao_selecionada =  values['-LISTA_PUBLICACOES-'][0]
            publicacao = encontra_publicacao(publicacoes, publicacao_selecionada)
            abrir_janela_publicacao(publicacao,values['-CAMPO_ABSTRACT-'], values['-CAMPO_AUTOR-'], values['-CAMPO_DATA-'], values['-CAMPO_DOI-'], values['-CAMPO_PDF-'], values['-CAMPO_URL-'], values['-CAMPO_TITULO-'], values['-CAMPO_KEY-'])

        elif event == 'GUARDAR' and publicacoes != []:
            nome = sg.popup_get_file("Salvar como Ficheiro JSON", save_as=True, no_window=True, file_types=(('JSON', '*.json'),), title= "Salvar JSON")
            guardar_json(publicacoes, nome)
            sg.popup('O ficheiro foi guardado com sucesso')
    

    window.close()

# ------------- funções --------------------

def contar_autores(data):
    res = {}
    for pub in data:
        for autor in pub['authors']:
            if autor['name'] not in res:
                res[autor['name']] = [pub]
            else:
                res[autor['name']].append(pub)
    return res

def contar_keywords(data):
    res = {}
    for pub in data:
        if pub.get('keywords') is not None:
            for keyword in pub['keywords'].split(', '):
                if keyword not in res:
                    res[keyword] = [pub]
                else:
                    res[keyword].append(pub)
    return res

def ordena_alfabetico(dicionario, inverso):
    ordenado = sorted(dicionario, reverse=inverso)
    return ordenado

def ordena_frequencia(dicionario, inverso):
    ordenado = sorted(dicionario.items(), key=lambda x: len(x[1]), reverse = inverso)
    res = []
    for autor in ordenado:
        res.append(autor[0])
    return res


# ------------------------------------------------ GUARDAR ---------------------------------------------------------


# ---------- guardar em texto ----------------


def ficheiro_texto(dataset,nome):
    ficheiro = open(nome, "w", encoding="utf-8")
    for artigo in dataset:

        if "title" in artigo:
            title = artigo["title"]
        else:
            title = "Não disponível"

        if "abstract" in artigo:
            abstract = artigo['abstract']
            introducao = metodos = resultados = conclusao = "Não disponível"
            partes = abstract.split("Métodos:")
            if len(partes) > 0:
                introducao = partes[0].strip()
                resumo = ""
                texto_intro = ""
                i = 0
                espaço_encontrado = False
                while i < len(introducao) and not espaço_encontrado:
                    if introducao[i]== " ":
                        resumo = introducao[:i]
                        texto_intro = introducao[i+1:]
                        espaço_encontrado = True
                    i = i + 1
                if not espaço_encontrado:
                    resumo = introducao
                    texto_intro =""


            if len(partes) > 1:
                partes_metodo = partes[1].split("Resultados:")
                if len(partes_metodo) > 0:
                    metodos = partes_metodo[0].strip()

                    if len(partes_metodo) > 1:
                        partes_resultado = partes_metodo[1].split("Conclusão:")
                        if len(partes_resultado) > 0:
                            resultados = partes_resultado[0].strip()

                            if len(partes_resultado) > 1:
                                conclusao = partes_resultado[1].strip()

        if "publish_date" in artigo:
            publish_data = artigo["publish_date"]
        else:
            publish_data = "Não disponível"

        if "doi" in artigo:
            doi = artigo["doi"]
        else:
            doi = "Não disponível"

        if "pdf" in artigo:
            pdf = artigo["pdf"]
        else:
            pdf = "Não disponível"

        if "url" in artigo:
            url = artigo["url"]
        else:
            url = "Não disponível"

        if "keywords" in artigo:
            palavras_chave = artigo["keywords"]
        else:
            palavras_chave = "Não disponível"

        ficheiro.write(f"Título: {title}\n\n")
        ficheiro.write("Autores:\n")
        autores = artigo.get("authors", [])
        if autores:
            for autor in autores:
                nome_autor = autor.get("name", "Não disponível")
                afiliação = autor.get("affiliation", "Não disponível")
                orcid = autor.get("orcid","Não disponível")
                ficheiro.write(f"  Autor: {nome_autor} | Afiliação: {afiliação}| Orcid: {orcid}\n")
        else:
            ficheiro.write("Autores não disponíveis\n")

        ficheiro.write(f"\nData de publicação: {publish_data}\n\n")
        ficheiro.write(f"Resumo:\n")
        ficheiro.write(f"{resumo}\n")
        ficheiro.write(f"{texto_intro}\n")
        ficheiro.write(f"Métodos: {metodos}\n")
        ficheiro.write(f"Resultados: {resultados}\n")
        ficheiro.write(f"Conclusão: {conclusao}\n\n")
        ficheiro.write(f"Palavras-chave: {palavras_chave}\n\n")
        ficheiro.write(f"DOI: {doi}\n\n")
        ficheiro.write(f"PDF: {pdf}\n\n")
        ficheiro.write(f"URL: {url}\n\n")
        ficheiro.write("____________________________________________________\n\n")

    ficheiro.close()
    print(f"O seu arquivo de texto {nome} foi gerado com sucesso.")




# ------------------------------------------- LISTAR -----------------------------------------------

def interface_listar(dataset):
    campos = [
    sg.Checkbox('Resumo', default=True, key='-CAMPO_ABSTRACT-', enable_events=True), sg.Checkbox('Autor', default=True, key='-CAMPO_AUTOR-', enable_events=True),
    sg.Checkbox('Data', default=True, key='-CAMPO_DATA-', enable_events=True), sg.Checkbox('DOI', default=True, key='-CAMPO_DOI-', enable_events=True),
    sg.Checkbox('Palavra-chave', default=True, key='-CAMPO_KEY-', enable_events=True),
    sg.Checkbox('PDF', default=True, key='-CAMPO_PDF-', enable_events=True), sg.Checkbox('Título', default=True, key='-CAMPO_TITULO-', enable_events=True),
    sg.Checkbox('URL', default=True, key='-CAMPO_URL-', enable_events=True)
]

    ordenar = [
    sg.Radio('Título (A-Z)', '-ORDENAR-', key='-ORDENAR_TITULO_AZ-', enable_events=True),
    sg.Radio('Título (Z-A)', '-ORDENAR-', key='-ORDENAR_TITULO_ZA-', enable_events=True),
    sg.Radio('Data (mais recente para mais antigo)', '-ORDENAR-', key='-ORDENAR_DATA_RA-', enable_events=True),
    sg.Radio('Data (mais antigo para mais recente)', '-ORDENAR-', key='-ORDENAR_DATA_AR-', enable_events=True)
]

    layout = [
        [sg.Frame('Ordenar', [[*ordenar]], font=('Helvetica', 13))],
        [sg.Frame('Campos a listar', [[*campos]], font=('Helvetica', 13))],
        [sg.Button('LISTAR')],
        [sg.Listbox(values=[], size=(99, 30), key='-LISTA_PUBLICACOES-', horizontal_scroll=True, enable_events=True)],
        [sg.Button("Sair", key="-SAIR-")]]

    window = sg.Window('Listar', layout)

    publicacoes = []

    stop = True
    while stop:
        event, values = window.read()
        if event in [sg.WINDOW_CLOSED, "-SAIR-"]:
            stop = False

        elif event == 'LISTAR' and not values['-ORDENAR_DATA_RA-'] and not values['-ORDENAR_DATA_AR-'] and not values['-ORDENAR_TITULO_AZ-'] and not values['-ORDENAR_TITULO_ZA-']:
            sg.popup('Por favor, selecione uma opção de ordenação.', title='Aviso')

        elif event == 'LISTAR':
            publicacoes = dataset
            if publicacoes != []:
                if values['-ORDENAR_DATA_RA-']:
                    publicacoes_ordenadas = ordenaData(publicacoes, True)
                elif values['-ORDENAR_DATA_AR-']:
                    publicacoes_ordenadas = ordenaData(publicacoes, False)
                elif values['-ORDENAR_TITULO_AZ-']:
                    publicacoes_ordenadas = ordenaTitulo(publicacoes, False)
                elif values['-ORDENAR_TITULO_ZA-']:
                    publicacoes_ordenadas = ordenaTitulo(publicacoes, True)
                titulos_publicacoes = titulos(publicacoes_ordenadas)
                window['-LISTA_PUBLICACOES-'].update(titulos_publicacoes)


        elif event == '-LISTA_PUBLICACOES-' and publicacoes != []:
            publicacao_selecionada =  values['-LISTA_PUBLICACOES-'][0]
            publicacao = encontra_publicacao(publicacoes, publicacao_selecionada)
            abrir_janela_publicacao(publicacao,values['-CAMPO_ABSTRACT-'], values['-CAMPO_AUTOR-'], values['-CAMPO_DATA-'], values['-CAMPO_DOI-'], values['-CAMPO_PDF-'], values['-CAMPO_URL-'], values['-CAMPO_TITULO-'], values['-CAMPO_KEY-'])


    window.close()

