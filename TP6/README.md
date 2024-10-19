# Relatório TP6
## Data: 2024-10-19
## Autor: Joana Maria Fernandes Campos
## Número de estudante: a107229
## Curso: Engenharia Biomédica
## Ano letivo: 2024/2025

## Resumo
Aplicação para gestão de alunos:
Considere que o modelo do aluno e da turma têm a seguinte estrutura:
aluno = (nome, id, [notaTPC, notaProj, notaTeste])`
turma = [aluno]`
* Cria uma aplicação que coloca no monitor o seguinte menu de operações:
    - 1: Criar uma turma;
    - 2: Inserir um aluno na turma;
    - 3: Listar a turma;
    - 4: Consultar um aluno por id;
    - 8: Guardar a turma em ficheiro;
    - 9: Carregar uma turma dum ficheiro;
    - 0: Sair da aplicação
* No fim de executar a operação selecionada, a aplicação deverá colocar novamente o menu e pedir ao utilizador a opção para continuar;
* Utiliza a tua aplicação para criar uma turma com 5 alunos.

Iniciei o trabalho com a criação das funções num ficheiro ipynb para depois passar para ficheiro py, ficheiro concebido para o terminal. Numa face incial achei o TP6 confusa, mais nas duas primeiras funções, onde deveria criar uma lista vazia, onde seriam anexadas outras listas, com nomes, ids, notas que deveriam estar no interior de um tuplo, ou seja tinhamos muitas coisas a ter em conta, muitas das funções que já tinhamos feito identicas em aula TP, o que me facilitou a relizar algumas funções.

Optei por fazer uma função de cada vez, foi mais fácil quer para organizar os comandos de cada uma delas, quer para as testar e ir aprefeiçoando até ficarem funcionais, não considero esta a parte mais trabalhosa mas sim o pensamento por detrás deste programa, como referi anteriormente, temos uma lista dentro de uma lista e dentro dessa primeira lista um tuplo, o que pode se tornar confuso, no entanto depois de passar o pensamento para o papel foi mais facil perceber quer a posição das coisas, quer a lógica que deveria ser usada, acho importante destacar que nas últimas aulas houve um aumento alucinante na fasquia, inicialmente trabalhavamos só com prints etc, agora encontramo-nos a trabalhar com coisas bem mais complexas, não é necessariamente algo mau.

Organizar os comandos foi a parte mais simples, era relativamente parecido ao TP5, até usei a mesma formulação na definição do menu, optei por ir buscar lá algumas inspirações.

## Considerações finais
Concluindo, achei o trabalho bastante enriquecedor, o pensamento por detrás era um pouco mais complicado que os anteriores, contudo achei mais simples que o TP5, não só por já saber trabalhar melhor com listas como também pela maneira como o TP foi colocado, achei a forma bem mais clara que a anterior.
Para mim facilitou-me pensar com uma folha, onde podia anotar as diferentes listas a ter em consideração, a evolução do trabalho, apesar de termos alguns comandos relativamente novos, que não conheciamos anteriormente, não me obrigou a uma pesquisa porque já tinhamos falado sobre todos eles.