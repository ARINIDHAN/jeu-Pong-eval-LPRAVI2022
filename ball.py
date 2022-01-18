#CREATION 18/01/2022
#PAR DURAISAMY LP RAVI2
import random
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(30, 30, 50, 50, fill=color)
        self.canvas.move(self.id, 100, 200)

        position_depart = [-4,-3, -2, -1, 1, 2, 3,4]
        random.shuffle(position_depart)
        self.x = position_depart[0]
        self.y = -4
        self.canvas_height = self.canvas.winfo_height()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1
