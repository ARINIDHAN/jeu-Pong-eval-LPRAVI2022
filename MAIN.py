#CREATION 18/01/2022
#PAR DURAISAMY LP RAVI2
import pygame
from ball import Ball
from tkinter import *
import time

def main():
    tk = Tk()
    tk.title("JeuPong2022")
    tk.resizable(0, 0)
    canvas = Canvas(tk, bg="red", width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()
    ball1 = Ball(canvas, 'white')
    while 1:
        tk.update()
        ball1.draw()
        time.sleep(0.05)
main()
