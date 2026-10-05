import tkinter as tk

root = tk.Tk()
root.title("Yues home")
root.geometry("700x600")

canvas = tk.Canvas(root, width=700, height=600, bg="white")
canvas.pack()

# Main house body
canvas.create_rectangle(
    150, 250, 450, 500,
    fill="#F6E3A1",   # butter yellow
    outline="black",
    width=3
)

# Main house roof
canvas.create_polygon(
    100, 250,
    300, 80,
    500, 250,
    fill="red",
    outline="black",
    width=3
)

# Left window
canvas.create_rectangle(
    190, 300, 250, 360,
    fill="lightblue",
    outline="black",
    width=3
)
canvas.create_line(220, 300, 220, 360, width=2)
canvas.create_line(190, 330, 250, 330, width=2)

# Right window
canvas.create_rectangle(
    350, 300, 410, 360,
    fill="lightblue",
    outline="black",
    width=3
)
canvas.create_line(380, 300, 380, 360, width=2)
canvas.create_line(350, 330, 410, 330, width=2)

# Door
canvas.create_rectangle(
    270, 390, 330, 500,
    fill="brown",
    outline="black",
    width=3
)

# Door knob
canvas.create_oval(
    315, 440, 325, 450,
    fill="yellow",
    outline="black"
)

# Sun
canvas.create_oval(
    520, 50, 600, 130,
    fill="yellow",
    outline="orange",
    width=3
)

# Dog house body
canvas.create_rectangle(
    520, 400, 620, 500,
    fill="#D2B48C",
    outline="black",
    width=3
)

# Dog house roof
canvas.create_polygon(
    500, 400,
    570, 340,
    640, 400,
    fill="red",
    outline="black",
    width=3
)

# Dog house entrance
canvas.create_oval(
    550, 440, 590, 500,
    fill="black",
    outline="black"
)

root.mainloop()