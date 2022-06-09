# projeto-final-joao-gui-ricardo
INTEGRANTES:
João Amaral Ferraz
Ricardo Wurzmann
Guilherme Froes da Fonseca

ESPECIFICAÇÕES:
O jogo "Dinossauro Maluco" têm seu código divido em 7 abas. Ao dar início no jogo, realizando um Run na aba 'main.py' (melhor explicado à frente), o jogo inicia-se na sua tela inicial, onde será necessário apertar tecla de espaço do computador pra começar o jogo. Ao entrar na tela de jogo, o operador se depará com o Dinossauro em um fundo de velho-oeste. O jogo foi insparado no Dinossauro do Google Chrome, aquele jogo que todos nós jogamos quando estamos sem internet... Dessa forma, os objetivos são os mesmos. De forma gradativa, a velocidade do jogo irá aumentando e o objetivo do operador será pular os cactos que vem na direção do seu Dinossauro, apertando e tecla de espaço. Ao colidir com o obstáculo, o jogo está programado para ir para a tela final, o 'game over', dando encerramento a jogo. Assim, o operador tem a opção de sair do jogo ou tentar outra vez, novamente pressioando a barra de espaço para jogar.

1- A primeira aba, 'Assets.py', tem como função criar os assets de cada imagem que é utilizada na montagem do jogo, assim como seus respectivos tamanhos.
2- A segunda aba, 'Config.py' foi utilizada para definir os valores num~ericos de cada ação do jogo. Por exemplo, tamanho do pulo do Dinossauro, a intensidade da gravidade, as dimensões do jogador e também os estados do jogo.
3- A terceira aba, 'gamescreen.py', é onde está propriamente toda a montagem do jogo. Isto é, o looping principal, os modos de como os obstáculos aparecem, o carregamento da imagem de jogo e a definição da colisão com os obstáculos e suas consequências.
4- A quarta aba, 'main.py', é a aba utilizada para rodar o jogo. Junta-se todas as montagens das outras abas. Assim, ao dar Run, o processo do jogo será iniciado. 
5- A quinta aba, 'sprites.py', é utilizada para criar as classes e as sprites que serão utilizadas no jogo. 
6- e 7- Configurações da imagem da tela inicial e da tela final de jogo. Respectivamente com os nomes 'telainicial.py' e 'tela_final.py'


VÍDEO: https://www.youtube.com/watch?v=MiQqmVj4V94