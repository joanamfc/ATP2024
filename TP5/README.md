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


Iniciei o trabalho com a criação das funções, inicialmente fiquei com dúvidas se o exercício seria para realizar em ficheiro ipynb ou py,como realizamos um parecido em aula recorrento a um ficheiro ipynb, optei por fazer o mesmo no TP, no ínicio fiquei um bocadinho confusa com este trabalho, apesar de já termos feito em aula TP, mas assim que identifiquei algumas salas tornou-se mais simples, porque passaram a haver dados em que trabalhar, consegui perceber como devia fazer cada função de modo a que o programa funcionasse.

Optei por fazer uma função de cada vez, foi mais fácil quer para organizar os comandos de cada uma delas, quer para as testar e ir aprefeiçoando até ficarem funcionais, não considero esta a parte mais trabalhosa mas sim o pensamento por detrás deste programa, acho importante destacar que haviam vários parâmetros a ter em conta, nomeadamente a formulação a usar em determinados casos, formulação essa que nos foi imposta, nomeadamente na função disponivel, inicialmente tinha criado uma função  que funcionava mas não incluia o False e o True, deixei essa função como alternativa à que criei com os parâmetros pedidos.

Organizar os comandos foi a parte mais simples, era relativamente parecido ao TP4, por isso optei por ir buscar lá algumas inspirações, apenas trocando as funções em causa e acrescentando partes que achei relevantes.


## Considerações finais
Concluindo, o pensamento por detrás do trabalho era um pouco mais complicado que os anteriores, também pelo facto de nos anteriores não usarmos listas, mas depois de pensar com determinadas salas, tornou-se mais simples, novamente foi muito parecido com o que fizemos na sala de aula e mesmo nos guiões práticos, não utilizei nada de novo, conhecia todos os comandos, achei menos trabalhoso que o TP anterior, mas com um pensamento mais complexo, este TP também possuí muitos comandos a serem testados, alguns promenores solicitados pelos docentes que temos de colocar.
