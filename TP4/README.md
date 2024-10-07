# Relatório TP4
## Data: 2024-10-06
## Autor: Joana Maria Fernandes Campos
## Número de estudante: a107229
## Curso: Engenharia Biomédica
## Ano letivo: 2024/2025

## Resumo
- Crie uma aplicação em Python que coloca no monitor o seguinte menu:
    * (1) Criar Lista 
    * (2) Ler Lista
    * (3) Soma
    * (4) Média
    * (5) Maior
    * (6) Menor
    * (7) estaOrdenada por ordem crescente
    * (8) estaOrdenada por ordem decrescente
    * (9) Procura um elemento
    * (0) Sair
- O utilizador irá escolher uma das opções introduzindo o número correspondente;
- Se a opção não for sair, a aplicação executa a operação pretendida, apresenta o resultado e a seguir apresenta de novo o menu;
- Se a opção for sair, a aplicação termina colocando uma mensagem no monitor.

* No desenvolvimento da aplicação deverá ter em atenção o seguinte:
    - A aplicação terá uma variável interna para guardar uma lista de números;
    - Na opção 1, deverá ser criada uma lista de números aleatórios entre 1 e 100 que será guardada na variável interna;
    - Na opção 2, deverá ser criada uma lista com números introduzidos pelo utilizador, que será guardada na variável interna;
    - Nestas primeiras opções, se a variável interna já tiver uma lista, esta será sobreposta/apagada pela nova lista;
    - Na opção 3, será calculada a soma dos elementos na lista no momento;
    - Na opção 4, será calculada a média dos elementos na lista no momento;
    - Na opção 5, será calculado o maior elemento da lista no momento;
    - Na opção 6, será calculado o menor elemento da lista no momento;
    - Na opção 7, a aplicação deverá indicar (Sim/Não) se a lista está ordenada por ordem crescente;
    - Na opção 8, a aplicação deverá indicar (Sim/Não) se a lista está ordenada por ordem decrescente;
    - Na opção 9, a aplicação irá procurar um elemento na lista, se o encontrar deverá devolver a sua posição, devolverá -1 se o elemento não estiver na lista;
    - Se o utilizador selecionar a opção 0, a aplicação deverá terminar mostrando a lista que está nesse momento guardada.

Iniciei o trabalho pela criação de um ficheiro em ipynb, por estar mais habituada, serviu para apresentar o exercício de uma maneira alternativa, depois de ter todos os comando funcionais parti para o ficheiro py, concebido para ser realizado no Terminal, como já tinha os comandos feitos na primeira versão, alterei alguns promenores e ficou com queria, desta forma consegui pensar melhor nas modalidades como um todo, no entanto fazendo uma de cada vez para ser mais fácil quer organizar os comandos de cada uma delas, quer para as testar e ir aprefeiçoando até ficarem funcionais, foi a parte mais trabalhosa, em que é preciso ter vários parâmetros em conta, nomeadamente as fórmulas a usar em determinados casos, porque a lista criada, ou mandada criar deve servir como base para o funcionamento das outras funcionalidades.

Para mim a parte mais difícil foi mesmo organizar tudo, são muitas funcionalidades, a lista deve ser armazenada e depois temos alguns promenores que nos foram pedidos para implementar, logo devemos ter atenção ao cumprimento dos mesmos, já tinhamos trabalhado com a maior parte das funções em aula, então não achei muito complicado, no fundo o pedido neste TP4 era para juntarmos o que temos apreendido e descobrirmos, acredito eu, formas mais rápidas de o fazer. 

Numa das versões optei por utilizar mais as estruturas cícilas ( if, elif, else ) não esquecendo o While, na outra optei pela criação de funções para cada opção, fazendo uso também das estruturas referidas em cima, sei que o facto de criar duas versões me deu muito mais trabalho, mas quando li as indicações pela primeira vez pensei que o TP4 era concebido para fazer em ficheiro ipynb, no entanto quando fui ler pela segunda vez já notei que tinha de ser criado num ficheiro py, por isso opto por trazer as duas versões.

## Considerações finais
Concluindo, achei o trabalho interessante, muito parecido com o que temos feito na sala de aula e mesmo nos guiões práticos, não utilizei nada de novo, conhecia todos os comandos, no ínicio, sem testar, achei desafiante o facto da lista ter de ser guardada, mas depois percebi que não era nada de muito díficil, este programa possuí muitas vententes, tem muitos comandos a serem testados, mas serviu como uma introdução para percebemos que vamos ter de trabalhar com muitos dados e muitas escolhas para o utilizador, de modo a tornar a sua experiência em algo cada vez melhor.
