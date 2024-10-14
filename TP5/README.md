# Relatório TP5
## Data: 2024-10-12
## Autor: Joana Maria Fernandes Campos
## Número de estudante: a107229
## Curso: Engenharia Biomédica
## Ano letivo: 2024/2025

## Resumo

Suponha que está a desenvolver uma aplicacão para gestão de um conjunto de salas de cinema de um centro comercial. 
Nesse centro comercial existem algumas salas de cinema (que poderão estar a exibir filmes ou não), cada sala tem uma determinada 
lotação, uma lista com a referência dos bilhetes vendidos (lugares ocupados; cada lugar é identificado por um número inteiro), e cada sala tem um filme associado.
Especifique as funções utilizadas no exemplo:
1. listar( cinema ) - que lista no monitor todos os filmes que estão em exibição nas salas do cinema passado como argumento;
2. disponivel( cinema, filme, lugar ) - que dá como resultado **False** se o lugar lugar já estiver ocupado na sala onde o filme está a ser exibido e dará como resultado **True** se o inverso acontecer;
3. vendebilhete( cinema, filme, lugar ) - que dá como resultado um novo cinema resultante de acrescentar o lugar à lista dos lugares ocupados, na sala onde está a ser exibido o filme;
4. listardisponibilidades( cinema ) - que, para um dado cinema, lista no monitor para cada sala, o filme que está a ser exibido e o total de lugares disponíveis nessa sala (número de lugares na sala menos o número de lugares ocupados);
5. inserirSala( cinema, sala ) - que acrescenta uma sala nova a um cinema (devendo verificar se a sala já existe);
6. Acrescente todas as outras funcionalidades que achar necessárias;
7. À semelhança do exercício 3, construa uma aplicação com um menu de interface para as operações.


Iniciei o trabalho com a criação das funções, inicialmente fiquei com dúvidas se o exercício seria para realizar em ficheiro ipynb ou py, como realizamos um parecido em aula recorrendo a um ficheiro ipynb, optei por fazer das duas formas, pois pela leitura do enunciado já me deu a entender que seria em ficheiro py.
Comecei no ficheiro ipynb, depois de ter os comandos feitos, passei para o ficheiro concebido para o terminal e mudei algumas coisas que deixariam o programa esteticamente mais bonito, no ínicio fiquei um bocadinho confusa com este trabalho, apesar de já termos feito parecido em aula TP, no entanto assim que identifiquei algumas salas tornou-se mais simples, porque passaram a haver dados em que trabalhar, consegui perceber como devia fazer cada função de modo a que o programa funcionasse.

Optei por fazer uma função de cada vez, foi mais fácil quer para organizar os comandos de cada uma delas, quer para as testar e ir aprefeiçoando até ficarem funcionais, não considero esta a parte mais trabalhosa mas sim o pensamento por detrás deste programa, acho importante destacar que haviam vários parâmetros a ter em conta, nomeadamente a formulação a usar em determinados casos, formulação essa que nos foi imposta, nomeadamente na função disponivel, inicialmente tinha criado uma função que não incluia o False e o True, tive de alterar uns pontos para conseguir colocar da forma pedida, mas consegui chegar lá e não teve influência no TP.

Organizar os comandos foi a parte mais simples, era relativamente parecido ao TP4, por isso optei por ir buscar lá algumas inspirações, apenas trocando as funções em causa e acrescentando partes que achei relevantes.


## Considerações finais
Concluindo, achei o trabalho bastante enriquecedor, o pensamento por detrás era um pouco mais complicado que os anteriores, também pelo facto de nos anteriores não usarmos listas.
Para mim facilitou-me pensar com determinadas salas, ou seja com casos concreto, novamente este TP foi muito parecido com o que fizemos na sala de aula e mesmo nos guiões práticos, embora achasse mais complicado que o da TP, talvez pelo facto de aqui termos a necessidade de começar as funções pelo zero, ir testando muitas vezes, em algumas dessas vezes percebemos que apenas nos esquecemos de um vírgula ou e de um dois pontos e a função já fica incorreta, no entanto não utilizei nada de novo, conhecia todos os comandos, é óbvio que este TP exigiu trabalho autónomo no entanto não na parte de ir à descoberta de comAndos não conhecidos.
