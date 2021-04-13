# Andrew Hein
# Advanced Programming - Week 10
# 2021/3/29
# hollywood_star.py

import tkinter as tk
import math


def createStar(radius, posX, posY, rotationOffset):
    points = []
    baseRotation = 180 + rotationOffset
    for cycle in range(1, 6):
        x = radius * \
            math.cos(math.radians(baseRotation + cycle*72)) + posX
        y = radius * \
            math.sin(math.radians(baseRotation + cycle*72)) + posY
        points.append([x, y])

    polygon = [points[0][0], points[0][1], points[3][0], points[3][1], points[1]
               [0], points[1][1], points[4][0], points[4][1], points[2][0], points[2][1]]

    return polygon


# window
window = tk.Tk()
window.geometry("600x600")

# canvas
canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()

offset = 300

canvas.create_polygon(createStar(200, offset, offset, 18), fill='gold')
canvas.create_text(offset, offset, text="Andrew",
                   fill='black', font='times 15')

# begin
window.mainloop()
