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

#inimigos
inimigo = Turtle()
inimigo.color("red")
inimigo.shape("circle")
inimigo.penup()
inimigo.speed(0)
inimigo.goto(-200,250)

#tiro
tiro = Turtle()
tiro.color("yellow")
tiro.shape("triangle")
tiro.penup()
tiro.speed(0)
tiro.setheading(90)
tiro.shapesize(0.5,0.5)
tiro.hideturtle()

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
        estado_do_tiro = "fogo"
        print(estado_do_tiro)
        #movimentando o tiro
        x = jogador.xcor()
        y = jogador.ycor() + 10
        tiro.goto(x,y)
        tiro.showturtle()

#comandos do jogador
listen()
onkey(vai_para_esquerda,"Left")
onkey(vai_para_direita,"Right")
onkey(dispara_tiro,"space")

#principal 
while True:

    #movendo o inimigo
    x = inimigo.xcor()
    x += velocidade_inimigo
    inimigo.setx(x)

    #limitando os movimentos do inimigo 
    if inimigo.xcor() > 280:
        y = inimigo.ycor()
        y -= 40
        velocidade_inimigo *= -1
        inimigo.sety(y)
    
    if inimigo.xcor() < -280:
        y = inimigo.ycor()
        y -= 40
        velocidade_inimigo *= -1
        inimigo.sety(y)
    
    #disparo
    if estado_do_tiro == "fogo":
        y = tiro.ycor()
        y += velocidade_do_tiro
        tiro.sety(y)

    #verifica se o disparo atingiu o topo
    if tiro.ycor() > 275:
        estado_do_tiro = "pronto"
        tiro.hideturtle()
        print('topo ' + estado_do_tiro)

done()
