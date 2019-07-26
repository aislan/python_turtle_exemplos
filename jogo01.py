#exemplo de jogo
from turtle import *

#carregando a tela principal
Screen()
bgcolor('lightgreen')

#criando o jogador
jogador = Turtle()
jogador.color('blue')
jogador.shape('triangle')
jogador.penup()

#velocidade
velocidade = 1

#principal
while True:
    jogador.forward(velocidade)

done()