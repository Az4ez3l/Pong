import os
import turtle

import pen
import ball
import paddle # imports player class


# window setup
wn = turtle.Screen() # create window
wn.title("Pong by SM") # window title
wn.bgcolor("black") # changes background color
wn.setup(width=800, height=600) # set window size
wn.tracer(0) # prevents screen from updating, increase game speed


# paddles
paddleA = paddle.Paddle(-350)
paddleB = paddle.Paddle(350)


# ball
ball = ball.Ball()


# pen
pen = pen.Pen()
pen.scoreBoard(paddleA, paddleB)


# keyboard binding
wn.listen() # tells window to listen for keyboard input
wn.onkeypress(paddleA.paddleUp, 'w') # bind a key to a function
wn.onkeypress(paddleA.paddleDown, 's')
wn.onkeypress(paddleB.paddleUp, "Up") # up arrow bind
wn.onkeypress(paddleB.paddleDown, "Down") # down arrow bind
wn.onkeypress(turtle.bye, 'q') # bind quit game to 'q'


# main game loop
while True:
	wn.update() # update screen whenever loop runs

	ball.moveBall()
	ball.checkBorder(paddleA, paddleB, pen)

	# paddle and ball colisions
	ball.checkCollision(paddleA, paddleB)
