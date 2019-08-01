from turtle import *
from math import *
from random import *
import os

#configurando a tela
tela = Screen()
tela.bgcolor("black")
tela.title("Space Invaders")
tela.bgpic("background.gif")

#registrando shape
register_shape("invader.gif")
register_shape("player.gif")

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
jogador.shape("player.gif")
jogador.penup()
jogador.speed(0)
jogador.goto(0,-250)
jogador.setheading(90)

#escolha o número de inimigos
numero_de_inimigos = 5
#criando uma lista vazia de inimigos
inimigos = []

#adicionando os inimigoa para a lista
for i in range(numero_de_inimigos):
    inimigos.append(Turtle())    

for inimigo in inimigos:
    #inimigos
    inimigo.color("red")
    inimigo.shape("invader.gif")
    inimigo.penup()
    inimigo.speed(0)
    x = randint(-200,200)
    y = randint(150,200)
    inimigo.goto(x,y)

#tiro
tiro = Turtle()
tiro.color("yellow")
tiro.shape("triangle")
tiro.penup()
tiro.speed(0)
tiro.setheading(90)
tiro.shapesize(0.5,0.5)
tiro.hideturtle()

#valor do placar
score = 0

#placar
placar = Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.goto(-290,270)
texto_do_placar = "Score: {}".format(score)
placar.write(texto_do_placar,align="left",font=("Arial",14))
placar.hideturtle()

#velocidade do jogador
velocidade_jogador = 15

#velocidade do inimígo 
velocidade_inimigo = 2

#velocidade do tiro
velocidade_do_tiro = 20

#estado do tiro
#pronto | fogo
estado_do_tiro = "pronto"


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

def dispara_tiro():
    #declarar a variável estado_do_tiro como global
    global estado_do_tiro
    if estado_do_tiro == "pronto":
        os.system("play laser.wav&")
        estado_do_tiro = "fogo"
        #movimentando o tiro
        x = jogador.xcor()
        y = jogador.ycor() + 10
        tiro.goto(x,y)
        tiro.showturtle()

def bateu(objeto1, objeto2):
    distancia = sqrt(pow(objeto1.xcor()-objeto2.xcor(),2)+pow(objeto1.ycor()-objeto2.ycor(),2))
    if distancia < 20:
        return True
    else:
        return False

#comandos do jogador
listen()
onkey(vai_para_esquerda,"Left")
onkey(vai_para_direita,"Right")
onkey(dispara_tiro,"space")

#principal 
while True:
    for inimigo in inimigos:
            
        #movendo o inimigo
        x = inimigo.xcor()
        x += velocidade_inimigo
        inimigo.setx(x)

        #limitando os movimentos do inimigo 
        if inimigo.xcor() > 280:
            #movendo todos os inimigos pra baixo
            for i in inimigos:
                y = i.ycor()
                y -= 40
                i.sety(y)
            velocidade_inimigo *= -1
        
        if inimigo.xcor() < -280:
            #movendo todos os inimigos pra baixo
            for i in inimigos:
                y = i.ycor()
                y -= 40
                i.sety(y)
            velocidade_inimigo *= -1

        #verifica se o disparo atingiu o inimigo
        if bateu(tiro,inimigo):
            os.system("play explosion.wav&")
            #reseta o tiro
            tiro.hideturtle()
            estado_do_tiro = "pronto"
            tiro.goto(0,-400)
            #reseta o inimigo
            x = randint(-200,200)
            y = randint(150,200)
            inimigo.goto(x,y)
            #atualizando o placar
            score += 10
            texto_do_placar = "Score: {}".format(score)
            placar.clear()
            placar.write(texto_do_placar,align="left",font=("Arial",14))
                
        #verifica se o inimigo atingiu o jogador
        if bateu(jogador,inimigo):
            jogador.hideturtle()
            inimigo.hideturtle()
            print("Perdeu!")


    #disparo
    if estado_do_tiro == "fogo":
        y = tiro.ycor()
        y += velocidade_do_tiro
        tiro.sety(y)

    #verifica se o disparo atingiu o topo
    if tiro.ycor() > 275:
        estado_do_tiro = "pronto"
        tiro.hideturtle()
    

done()
