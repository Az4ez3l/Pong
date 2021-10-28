import turtle


class Paddle:
	def __init__(self, pos):
		self.pos = pos
		self.score = 0
		
		# create paddle
		self.paddle = turtle.Turtle() # create turtle object
		self.paddle.speed(0) # set animation speed to maximum speed
		self.paddle.shape("square") # set object shape
		self.paddle.shapesize(stretch_wid=5, stretch_len=1)
		self.paddle.color("white") # set object color
		self.paddle.penup() # doesn't draw line, when object starts moving
		self.paddle.goto(self.pos,0) # start drawing at coordinates given (x,y)


	def getYCor(self):
		return self.paddle.ycor()

	def increaseScore(self):
		self.score += 1


	def paddleUp(self):
		y = self.paddle.ycor() # returns y cord of object
		if not (y > 230):
			y += 20
			self.paddle.sety(y) # sets object to y position


	def paddleDown(self):
		y = self.paddle.ycor()
		if not (y < -230):
			y -= 20
			self.paddle.sety(y)	