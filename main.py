import tkinter as tk

root = tk.Tk()
root.title("House")
root.geometry("600x600")

canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

# 🟨 House body - Butter Yellow
canvas.create_rectangle(
    150, 250, 450, 500,
    fill="#F6E3A1",
    outline="black",
    width=3
)

# 🔺 Roof - Red
canvas.create_polygon(
    100, 250,
    300, 80,
    500, 250,
    fill="red",
    outline="black",
    width=3
)

# 🪟 Left window
canvas.create_rectangle(
    190, 300, 250, 360,
    fill="lightblue",
    outline="black",
    width=3
)

# Left window lines
canvas.create_line(220, 300, 220, 360, width=2)
canvas.create_line(190, 330, 250, 330, width=2)

# 🪟 Right window
canvas.create_rectangle(
    350, 300, 410, 360,
    fill="lightblue",
    outline="black",
    width=3
)

# Right window lines
canvas.create_line(380, 300, 380, 360, width=2)
canvas.create_line(350, 330, 410, 330, width=2)

# 🚪 Door
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

root.mainloop()