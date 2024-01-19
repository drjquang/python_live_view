import tkinter as tk
from math import radians, sin, cos

guide_line_axis = 90
FULL_CIRCLE = 360
NUM_OF_SLOT = 37
FULL_WIDTH = 360 / 37  # Slot width in full
HALF_WIDTH = FULL_WIDTH / 2


# Function to draw inclined text
def draw_inclined_text(x, y, text, angle_degrees):
    angle_radians = radians(angle_degrees)
    canvas.create_text(x, y, text=text, angle=angle_degrees, anchor="center", font=("Purisa", 16), fill="#DDD")


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


tk.Canvas.create_circle = _create_circle


def draw_a_slot(canvas, center_x, center_y, radius, guide_line, color):
    canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                      start=guide_line - HALF_WIDTH, extent=FULL_WIDTH, fill=color, outline="#DDD", width=2)


def red_or_black(order_number):
    if order_number % 2 == 0:
        return 'black'
    else:
        return 'red'


root = tk.Tk()
canvas_background = 'skyblue'
canvas_height = 600
canvas_width = canvas_height
outer_circle = (canvas_height / 2) * 0.8
inner_circle = (canvas_height / 2) * 0.68
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg=canvas_background)
canvas.pack()

draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis, 'green')
x = canvas_width/2
y = (canvas_height/2)*0.26
draw_inclined_text(x, y, '0', 90-guide_line_axis)

draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - FULL_WIDTH, 'red')
delta_x = (canvas_height/2)*0.74*sin(radians(FULL_WIDTH))
delta_y = (canvas_height/2)*0.74 - (canvas_height/2)*0.74*cos(radians(FULL_WIDTH))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   '32',
                   360-FULL_WIDTH)

draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - 2*FULL_WIDTH, 'black')
delta_x_2 = (canvas_height/2)*0.74*sin(radians(FULL_WIDTH*2))
delta_y_2 = (canvas_height/2)*0.74 - (canvas_height/2)*0.74*cos(radians(FULL_WIDTH*2))
draw_inclined_text(x + delta_x_2,
                   y + delta_y_2,
                   '15',
                   360-2*FULL_WIDTH)

# ----------------------------------------------------------------------------------------------------------------
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - 3*FULL_WIDTH, 'red')
delta_x_3 = (canvas_height/2)*0.74*sin(radians(FULL_WIDTH*3))
delta_y_3 = (canvas_height/2)*0.74 - (canvas_height/2)*0.74*cos(radians(FULL_WIDTH*3))
draw_inclined_text(x + delta_x_3,
                   y + delta_y_3,
                   '19',
                   360-3*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 4
slot_number = '4'
slot_color = 'black'
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74*sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 - (canvas_height/2)*0.74*cos(radians(FULL_WIDTH*slot_info[0]))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 5
slot_number = '21'
slot_color = 'red'
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 6
slot_number = '2'
slot_color = 'black'
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 7
slot_number = '25'
slot_color = 'red'
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 8
slot_number = '17'
if (slot_order % 2) == 0:
    slot_color = 'black'
else:
    slot_color = 'red'
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 9
slot_number = '34'
if (slot_order % 2) == 0:
    slot_color = 'black'
else:
    slot_color = 'red'
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 10
slot_number = '6'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 11
slot_number = '27'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 12
slot_number = '13'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 13
slot_number = '36'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 14
slot_number = '11'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 15
slot_number = '30'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 16
slot_number = '8'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 17
slot_number = '23'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 18
slot_number = '10'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 19
slot_number = '5'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 20
slot_number = '24'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 21
slot_number = '16'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
slot_order = 22
slot_number = '33'
slot_color = red_or_black(slot_order)
slot_info = [slot_order, slot_number, slot_color]
draw_a_slot(canvas, canvas_width / 2, canvas_height / 2, outer_circle, guide_line_axis - slot_info[0]*FULL_WIDTH, slot_info[2])
delta_x = (canvas_height/2)*0.74 * sin(radians(FULL_WIDTH*slot_info[0]))
delta_y = (canvas_height/2)*0.74 * (1 - cos(radians(FULL_WIDTH*slot_info[0])))
draw_inclined_text(x + delta_x,
                   y + delta_y,
                   slot_info[1],
                   360-slot_info[0]*FULL_WIDTH)
# ----------------------------------------------------------------------------------------------------------------
# make a circle with the same background color to hide the remaining
canvas.create_circle(canvas_width / 2, canvas_height / 2, inner_circle, fill=canvas_background, outline="#DDD", width=2)


root.mainloop()
