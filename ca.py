import tkinter as tk

root = tk.Tk()
root.title("Canvas Animation")

canvas = tk.Canvas(
    root,
    width=600,
    height=350,
    bg="white"
)

canvas.pack()

ball = canvas.create_oval(
    20, 120, 70, 170,
    fill="orange",
    outline=""
)

dx = 5

def animate():
    global dx

    x1, y1, x2, y2 = canvas.coords(ball)

    if x2 >= 600:
        dx = -5

    elif x1 <=0:
        dx = 5

    canvas.move(ball, dx, 0)

    root.after(20, animate)

animate()
root.mainloop()