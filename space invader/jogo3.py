from turtle import *

#configurando a tela
tela = Screen()
tela.bgcolor("black")
tela.title("Space Invaders")

#delimitando as bordas
borda = Turtle()
borda.speed(0)
borda.color("white")
borda.penup()
borda.goto(-300,-300)
borda.pendown()
borda.pensize(3)
for i in range(4):
    borda.fd(600)
    borda.left(90)
borda.hideturtle()

#jogador
jogador = Turtle()
jogador.color("blue")
jogador.shape("triangle")
jogador.penup()
jogador.speed(0)
jogador.goto(0,-250)
jogador.setheading(90)

#velocidade do jogador
velocidade_jogador = 15

#funções
def vai_para_esquerda():
    x = jogador.xcor()
    x -= velocidade_jogador
    if x < - 280:
        x = -280
    jogador.setx(x)

def vai_para_direita():
    x = jogador.xcor()
    x += velocidade_jogador
    if x > 280:
        x = 280
    jogador.setx(x)

#comandos do jogador
listen()
onkey(vai_para_esquerda,"Left")
onkey(vai_para_direita,"Right")


done()
