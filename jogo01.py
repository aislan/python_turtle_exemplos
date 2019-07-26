#exemplo de jogo
from turtle import *
from math import *
from random import *
import os

#carregando a tela principal
Screen()
bgcolor("black")
bgpic("fundo.png")
tracer(3)

#desenhando os limites/bordas do jogo
arena = Turtle()
arena.color("white")
arena.penup()
arena.setposition(-300,-300)
arena.pendown()
arena.pensize(3)
for lado in range(4):
    arena.fd(600)
    arena.left(90)
arena.hideturtle()

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

def bateu(objeto1, objeto2):
    distancia = sqrt(pow(objeto1.xcor()-objeto2.xcor(),2)+pow(objeto1.ycor()-objeto2.ycor(),2))
    if distancia < 20:
        return True
    else:
        return False


#comandos do jogo
listen()
onkey(vira_a_esquerda,"Left")
onkey(vira_a_direita,"Right")
onkey(aumenta_velocidade,"Up")

#criando pilulas
max_pilulas = 6
pilulas = []

#pilulas de energia 
for i in range(max_pilulas):
    pilulas.append(Turtle())
    pilulas[i].color("red")
    pilulas[i].shape("circle")
    pilulas[i].penup()
    pilulas[i].speed(0)
    pilulas[i].setposition(randint(-300,300),randint(-300,300))


#principal
while True:
    jogador.forward(velocidade)

    #verificação de limite/borda jogador
    if jogador.xcor() > 300 or jogador.xcor() < -300:
        jogador.right(100)
        os.system("bateu.mp3&")
    if jogador.ycor() > 300 or jogador.ycor() < -300:
        jogador.right(100)
        os.system("bateu.mp3&")

    #movendo as píluas
    for i in range(max_pilulas):
        pilulas[i].fd(3)

        #verificação de limite/borda pilula
        if pilulas[i].xcor() > 290 or pilulas[i].xcor() < -290:
            pilulas[i].right(100)
            os.system("bateu.mp3&")
        
        if pilulas[i].ycor() > 290 or pilulas[i].ycor() < -290:
            pilulas[i].right(100)
            os.system("bateu.mp3&")

         #verificar colisão
        if bateu(jogador,pilulas[i]):
            pilulas[i].setposition(randint(-300,300),randint(-300,300))
            pilulas[i].right(randint(0,360))

done()