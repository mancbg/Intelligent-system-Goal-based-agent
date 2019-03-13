__author__ = 'MBG'

"""
CSCI-630 Project 1
Author: Manasi Bharat Gund

This program prints the maze and the path in it with turtle

"""
import turtle
import math

# global constants for window dimensions

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1200


def init():
    """
    :pre: pos (0,0) , heading(east), down
    :post: pos (-300,0), heading(east), down
    :return: None
    """
    turtle.tracer(0, 0);
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_HEIGHT / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.up()
    turtle.setx(-300)


def draw_maze(solution):
    """
    Draws the maze
    :pre: pos (0,0) , heading(east), down
    :post: depends on the maze size
    :return: None
    """
    init()
    draw_squares(solution)


def draw_squares(maze):
    side = 500 / len(maze)
    for row in maze:
        for item in row:
            draw_square(item, side)
        turtle.up()
        turtle.right(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.backward(len(row) * side)
    turtle.left(90)
    turtle.forward(len(maze) * side)
    turtle.mainloop()


def draw_square(item, side):
    turtle.down()
    if item == "1":
        turtle.fillcolor("black")
    elif item == "X":
        turtle.fillcolor("blue")
    else:
        turtle.fillcolor("white")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()
    turtle.forward(side)
