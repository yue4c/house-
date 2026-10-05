import tkinter as tk

root = tk.Tk()
root.title("Cartoon Community")
root.geometry("1000x700")

canvas = tk.Canvas(root, width=1000, height=700, bg="skyblue")
canvas.pack()

# Sky and ground
canvas.create_rectangle(0, 0, 1000, 700, fill="skyblue", outline="skyblue")
canvas.create_rectangle(0, 500, 1000, 620, fill="lightgreen", outline="lightgreen")
canvas.create_rectangle(0, 620, 1000, 700, fill="gray40", outline="gray40")

# Road line
canvas.create_line(0, 660, 1000, 660, fill="white", width=4, dash=(20, 15))

# Clouds
def draw_cloud(x, y):
    canvas.create_oval(x, y, x+50, y+40, fill="white", outline="white")
    canvas.create_oval(x+30, y-20, x+80, y+30, fill="white", outline="white")
    canvas.create_oval(x+60, y, x+110, y+40, fill="white", outline="white")
    canvas.create_oval(x+20, y+10, x+90, y+50, fill="white", outline="white")

draw_cloud(80, 80)
draw_cloud(350, 60)
draw_cloud(700, 90)

# Sun
canvas.create_oval(850, 50, 930, 130, fill="yellow", outline="orange", width=3)

# Function to draw a house
def draw_house(x, y, body_color, roof_color, open_door=False):
    # House body
    canvas.create_rectangle(
        x, y, x+120, y+100,
        fill=body_color, outline="black", width=2
    )

    # Roof
    canvas.create_polygon(
        x-10, y,
        x+60, y-60,
        x+130, y,
        fill=roof_color, outline="black", width=2
    )

    # Left window
    canvas.create_rectangle(
        x+18, y+25, x+48, y+55,
        fill="lightblue", outline="black", width=2
    )
    canvas.create_line(x+33, y+25, x+33, y+55, width=1)
    canvas.create_line(x+18, y+40, x+48, y+40, width=1)

    # Right window
    canvas.create_rectangle(
        x+72, y+25, x+102, y+55,
        fill="lightblue", outline="black", width=2
    )
    canvas.create_line(x+87, y+25, x+87, y+55, width=1)
    canvas.create_line(x+72, y+40, x+102, y+40, width=1)

    # Door
    if open_door:
        # dark inside
        canvas.create_rectangle(
            x+48, y+60, x+72, y+100,
            fill="black", outline="black", width=2
        )
        # open door flap
        canvas.create_polygon(
            x+72, y+60,
            x+95, y+70,
            x+95, y+105,
            x+72, y+100,
            fill="peru", outline="black", width=2
        )
    else:
        canvas.create_rectangle(
            x+48, y+60, x+72, y+100,
            fill="saddlebrown", outline="black", width=2
        )
        canvas.create_oval(
            x+66, y+78, x+70, y+82,
            fill="yellow", outline="black"
        )

# Trees
def draw_tree(x, y):
    canvas.create_rectangle(x+18, y+40, x+32, y+90, fill="sienna4", outline="black")
    canvas.create_oval(x, y, x+50, y+50, fill="green", outline="black")
    canvas.create_oval(x+20, y-20, x+70, y+30, fill="green", outline="black")
    canvas.create_oval(x+35, y, x+85, y+50, fill="green", outline="black")

# Houses placed on ground properly
draw_house(60, 400, "#F6E3A1", "red", open_door=False)
draw_house(220, 400, "#FFD1DC", "orange", open_door=True)
draw_house(380, 400, "#CDE7B0", "purple", open_door=False)
draw_house(560, 400, "#AEC6CF", "red", open_door=True)
draw_house(720, 400, "#FFF2A8", "hotpink", open_door=False)
draw_house(860, 400, "#D8BFD8", "blue", open_door=True)

# Trees on grass
draw_tree(150, 460)
draw_tree(500, 460)
draw_tree(790, 460)

root.mainloop()