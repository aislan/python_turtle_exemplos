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
jogador.speed(0)

#velocidade
velocidade = 1

#ações dos comandos
def vira_a_esquerda():
    jogador.left(30)

def vira_a_direita():
    jogador.right(30)

def aumenta_velocidade():
    global velocidade
    velocidade += 1

#comandos do jogo
listen()
onkey(vira_a_esquerda,"Left")
onkey(vira_a_direita,"Right")
onkey(aumenta_velocidade,"Up")

#principal
while True:
    jogador.forward(velocidade)

done()