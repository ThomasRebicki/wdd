# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from random import seed
from random import randrange
from timeit import repeat
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    for i in range(0,4):
        sheesh = randrange(800)
        sheeesh = 20 + randrange(80)
        heesh = sheeesh + 100 + (20 + randrange(80))
        draw_pine_tree(canvas,sheesh,sheeesh,heesh)

    for i in range(0,5):
        sheesh = randrange(800)
        popo = 300 + randrange(200)
        draw_cloud(canvas, sheesh, popo)

    for i in range(0,25):
        sheesh = randrange(800)
        popo = randrange(500)
        draw_oval(canvas, sheesh, popo , sheesh + 5, popo+5,fill = "white")

    for i in range(0,5):
     draw_snow_bro(canvas,randrange(800),20 + randrange(80))
 


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="white")


def draw_cloud(canva,xx,yy):
    for i in range(0,15):
        sheesh = 30 - randrange(60)
        jsios =  30 - randrange(60)
        draw_oval(canva, xx+ sheesh, yy + jsios , xx + sheesh + 40, yy + jsios + 40 ,fill = "white",outline = "white")



def draw_snow_bro(canva,xx,yy):

        draw_oval(canva, xx, yy , xx + 60, yy +60 ,fill = "white")
        draw_oval(canva, xx + 5, yy+30 , xx + 55, yy+30 +50 ,fill = "white")
        draw_oval(canva, xx + 10, yy+60 , xx + 50, yy+60+ 40 ,fill = "white")

        draw_oval(canva, xx+30, yy+80 , xx +25, yy +85 ,fill = "black")
        draw_oval(canva, xx+40, yy+80 , xx +35, yy +85 ,fill = "black")
        draw_polygon(canva, xx+35, yy + 75, xx + 20, yy + 70,xx+35,yy+70, fill = "orange")


def draw_pine_tree(canvas, center_x, bottom, height):
   
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height


    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")














main()