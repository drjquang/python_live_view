# Date: Thu, 11-Jan-2024
# Desc: Draw roulette slot, inside has number
# Info: canvas 600x600, font size 16

import tkinter as tk
from math import radians, sin, cos

guide_line_axis = 90
FULL_CIRCLE = 360
NUM_OF_SLOT = 37
FULL_WIDTH = 360 / 37  # Slot width in full
HALF_WIDTH = FULL_WIDTH / 2
canvas_background = 'skyblue'
canvas_height = 600
canvas_width = canvas_height
outer_circle = (canvas_height / 2) * 0.8
inner_circle = (canvas_height / 2) * 0.68
count_circle = (canvas_height / 2) * 0.3
x = canvas_width/2
y = (canvas_height/2)*0.26

roulette_number = ['0',
                   '32', '15', '19', '4', '21', '2', '25', '17', '34', '6', '27', '13', '36', '11', '30', '8',
                   '23', '10', '5', '24', '16', '33', '1', '20', '14', '31', '9', '22', '18', '29', '7', '28',
                   '12', '35', '3', '26']


# Function to draw inclined text
def draw_inclined_text(x_val, y_val, text, angle_degrees):
    angle_radians = radians(angle_degrees)
    canvas.create_text(x_val, y_val, text=text, angle=angle_degrees, anchor="center", font=("Purisa", 16), fill="#DDD")


# Function to set slot color
def set_slot_color(order_number):
    if order_number == 0:
        return 'green'
    elif order_number % 2 == 0:
        return 'black'
    else:
        return 'red'


# Function to draw one slot, including the slot and the text
def draw_one_slot(canvas, center_x, center_y, radius, guide_line, color, text, order_number):
    canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                      start=guide_line - HALF_WIDTH, extent=FULL_WIDTH, fill=color, outline="#DDD", width=2)
    delta_x = (canvas_height / 2) * 0.74 * sin(radians(FULL_WIDTH * order_number))
    delta_y = (canvas_height / 2) * 0.74 * (1 - cos(radians(FULL_WIDTH * order_number)))
    draw_inclined_text(x + delta_x, y + delta_y, text, 360-order_number*FULL_WIDTH)


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


tk.Canvas.create_circle = _create_circle
# ----------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.title("Roulette countdown")
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg=canvas_background)
canvas.pack()

for i in range(len(roulette_number)):
    draw_one_slot(canvas, canvas_width / 2, canvas_height/2, outer_circle,
                  guide_line_axis - i*FULL_WIDTH,
                  set_slot_color(i),
                  roulette_number[i],
                  i)
# make a circle with the same background color to hide the remaining
canvas.create_circle(canvas_width / 2, canvas_height / 2, inner_circle, fill=canvas_background, outline="#DDD", width=2)

# draw the count down number
countdown_value = tk.StringVar(root, '60')
canvas.create_circle(canvas_width / 2, canvas_height / 2, count_circle, fill='black', outline="#DDD", width=2)
countdown_display = canvas.create_text(canvas_width / 2, canvas_height/2,
                   text=countdown_value.get(), angle=0, anchor="center", font=("Purisa", 64), fill="#DDD")


def on_change(varname, index, mode):
    canvas.itemconfigure(countdown_display, text=root.getvar(varname))


countdown_value.trace_variable('w', on_change)


def trigger_change():
    temp_value = int(countdown_value.get())
    temp_value = temp_value - 1
    countdown_value.set(str(temp_value))
    root.after(1000, trigger_change)


trigger_change()

root.mainloop()
