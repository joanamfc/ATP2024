# Relatório TP3
## Data: 2024-09-28
## Autor: Joana Maria Fernandes Campos
## Número de estudante: a107229
## Curso: Engenharia Biomédica
## Ano letivo: 2024/2025

## Resumo
O TP3 consistiu na realizacão de um jogo, o "Jogo dos 21 fósforos", que consiste em:
* No início do jogo, há 21 fósforos;
* Cada jogador (computador ou utilizador), pode tirar 1, 2, 3 ou 4 fósforos quando for a sua vez de jogar;
* Os jogadores jogam alternadamente;
* Quem tirar o último fósforo perde!
### O programa 
* O jogo deverá ter dois modos: o jogador joga em primeiro lugar e o computador começa a jogar em segundo lugar e, no segundo modo, o computador começa em primeiro; 
* Quando o computador começa a jogar em segundo lugar, deve ganhar sempre o jogo;
* Quando o computador começa a jogar em primeiro lugar, se o utilizador cometer um erro de cálculo, o computador deverá passar para a posição de vencedor e ganhar o jogo.

Iniciei o trabalho pela realização das duas modalidades, uma de cada vez, para ser mais fácil quer organizar os comandos de cada uma delas, quer para as testar e ir aprefeiçoando até ficarem funcionais, foi a parte mais trabalhosa, em que é preciso ter vários parâmetros em conta, nomeadamente as fórmulas a usar em determinados casos, quer seja o usuário a ganhar ou o computador.

Em seguida, dediquei-me ao "menu principal", onde são dadas as boas-vindas ao usuário e o utilizador escolhe a modalidade desejada, no fundo é onde se encaixam as duas modalidades, optei por criar uma experiência extra, podendo ser vista quando o programa pergunta o nome de usuário e dá as boas vindas ao jogador tratanto-o pelo nome escolhido, deixando ao seu critério, perante respetiva seleção, jogar a modalidade 1, onde o computador joga em segundo lugar, sendo o primeiro ocupado pelo usário, neste caso o computador deve sempre ganhar o jogo, como segunda modalidade o computador joga em primeiro lugar e o usuário joga em segundo, se o o usário cometer um erro quem vence é o computador, ou seja esta última podia acabar com dois diferentes vencedores e foi esta parte que me deu mais trabalho, porque em muitas das tentativas o programa não encerrava como devia, para não utilizar o break, que nos foi proibido, obtei por tentar outra abordagem.

Para mim a parte mais difícil foi mesmo o pensamento por detrás deste jogo, a primeira modalidade ainda é simples, se pensarmos jogada a jogada, se fizermos alguns testes com números chegamos a esse pensamento, achei a segunda mais complicada de formular que a primeira, no ínicio fiquei perdida relativamente a qual deveria ser a minha abordagem, porque afinal são muitos fósforos e só podemos retirar de 1 a 4 por vez, não podendo retirar nem mais nem menos, logo temos de criar uma sequência que proiba o utilizador de retirar alguns números de fósforos e além disso nasce uma nova possibilidade comparada com a primeira modalidade que é o facto do usuário poder vencer, assim obtei por fazer, as abordagens juntas numa primeira face, copiava e colava noutra folha e testava para ver se não tinham erros e se estavam completamente funcionais então voltava a colar no local onde apresento o TPC, isto ajudou-me a organizar as minhas ideias e a testar alguns comandos que não tinha a certeza se resultariam, sei que a realizar o jogo poderia ter dado uso a funções mas quis trablhar mais algum tempo com as estruturas cíclicas e o condicional.

## Considerações finais
Concluindo, achei o trabalho interessante, no entanto levemente mais complicado que o que temos feito na sala de aula e mesmo nos guiões práticos, não utilizei nada de novo, conhecia todos os comandos, este jogo acaba por ter um pensamento bastante elaborado por trás, não que seja complicado, mas possuí várias vententes o que acabou por me confundir um bocadinho, existem várias formas de resolução, esta que apresento é a segunda forma que testei, a primeira ficou menos detalhada que esta, mas serviu para eu organizar as minhas ideias, para saber os passos a seguir e conseguir fazer uma abordagem mais completa, que é a que apresento.