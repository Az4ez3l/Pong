import os
from util import playSound
import turtle


class Ball:
	def __init__(self):
		self.ball = turtle.Turtle()
		self.ball.speed(0)
		self.ball.shape("circle")
		self.ball.color("white")
		self.ball.penup()
		self.ball.goto(0,0)
		self.ball.dx = 0.5 # tells how much pixel to move object by on x axis
		self.ball.dy = 0.5 # tells how much pixel to move object by on y axis

	def moveBall(self):
		self.ball.setx(self.ball.xcor() + self.ball.dx)
		self.ball.sety(self.ball.ycor() + self.ball.dy)


	def checkBorder(self, paddleA, paddleB, pen):
		if self.ball.ycor() > 290:
			self.ball.sety(290)
			self.ball.dy *= -1 # reverse ball direction

		
		if self.ball.ycor() < -290:
			self.ball.sety(-290)
			self.ball.dy *= -1
		
		if self.ball.xcor() > 390:
			self.ball.goto(0,0)
			self.ball.dx *= -1
			paddleA.increaseScore()
			playSound("assets/lose_point.wav")
		
		if self.ball.xcor() < -390:
			self.ball.goto(0,0)
			self.ball.dx *= -1
			paddleB.increaseScore()
			playSound("assets/lose_point.wav")

		pen.scoreBoard(paddleA, paddleB)


	def checkCollision(self, paddleA, paddleB):
		if self.ball.xcor() > 340 and self.ball.xcor() < 350 and (self.ball.ycor() < paddleB.getYCor() + 40 and self.ball.ycor() > paddleB.getYCor() - 40):
			self.ball.setx(340)
			self.ball.dx *= -1

		if self.ball.xcor() < -340 and self.ball.xcor() > -350 and (self.ball.ycor() < paddleA.getYCor() + 40 and self.ball.ycor() > paddleA.getYCor() - 40):
			self.ball.setx(-340)
			self.ball.dx *= -1