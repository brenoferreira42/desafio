# Desafio
O desafio consiste em simular um jogo hipotético muito semelhante ao Banco Imobiliário, no qual quatro jogadores se alternam em rodadas, seguindo uma ordem definida no começo da partida. Cada jogador começa com um saldo de 300, joga um dado de 6 faces e anda pelo tabuleiro; a cada volta percorrida, o jogador ganha 100 de saldo. O tabuleiro é composto por 20 propriedades, cada uma com um custo de venda, um valor de aluguel e um proprietário.

Caso uma propriedade não tenha proprietário, o jogador pode comprá-la; se a propriedade já tiver um proprietário, o jogador deve pagar o aluguel da propriedade ao proprietário. Se um jogador fica com saldo negativo, ele perde o jogo, junto com suas propriedades, e não joga mais.

Caso reste apenas um jogador com saldo positivo, ele ganha a qualquer momento; ou, se a partida demorar muito, o jogo termina na milésima rodada, com a vitória do jogador com maior saldo. O critério de desempate é a ordem dos turnos dos jogadores na partida.

Cada um dos quatro jogadores tem um perfil, sendo eles:
* Jogador Impulsivo - compra qualquer propriedade sobre a qual ele parar.
* Jogador Exigente - compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
* Jogador cauteloso - compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
* Jogador aleatório - compra a propriedade que ele parar em cima com probabilidade de 50%.

# Objetivo
O objetivo deste desafio é rodar 300 simulações (partidas), mostrando no console as seguintes informações no fim:
* Quantas partidas terminam portime out (1000 rodadas);
* Quantos turnos em média demora uma partida;
* Qual a porcentagem de vitórias por comportamento dos jogadores;
* Qual o comportamento que mais vence.


# Abordagem seguida
A classe principal que roda uma simulação `GameSimulation` cria um tabuleiro por partida, tabuleiro este que foi implementado utilizando um buffer circular. O tabuleiro, por sua vez, possui 20 propriedades indexadas para cada posição do tabuleiro, com 4 jogadores dispostos aleatoriamente. Cada jogador tem um tipo diferente de estratégia para jogar, e para isso utilizei o padrão de projeto `Strategy` para cada um dos algoritmos de estratégias do jogador. Ao final, tendo um vencedor no jogo, o relatório do turno é gerado, e ao final das 300 simulações (partidas), o relatório final é gerado, mostrando as informações dos turnos jogados.


# Como rodar a aplicação

* Construa a imagem do Docker:<br>
`docker build -t desafio .`

*  Execute o container:<br>
`sudo docker run -p 8080:8080 desafio`
