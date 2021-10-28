import turtle

class Pen:
	def __init__(self):
		self.pen = turtle.Turtle();
		self.pen.speed(0)
		self.pen.color("white")
		self.pen.penup()
		self.pen.hideturtle() # hides object on screen
		self.pen.goto(0,260)
		

	def scoreBoard(self, paddleA, paddleB):
		self.pen.clear()
		self.pen.write(f"Player A: {paddleA.score} | Player B: {paddleB.score}", align="center", font=("Courier", 24, "normal"))
			