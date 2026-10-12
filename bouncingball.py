
import tkinter as tk

# Create root window
root = tk.Tk()
root.title("Bouncing Ball")
root.geometry("600x400")

# Create canvas
canvas = tk.Canvas(root, width=600, height=400, bg="lightblue")
canvas.pack()

# Draw ground
canvas.create_line(0, 350, 600, 350, width=3)

# Create ball
ball = canvas.create_oval(20, 100, 60, 140,
                         fill="orange", outline="black")

# Variables
velocity_y = 0
velocity_x = 3
gravity = 0.5
bounce = 0.75

# Animation
def move_ball():
    global velocity_y, velocity_x

    # Apply gravity
    velocity_y += gravity

    # Move ball
    canvas.move(ball, velocity_x, velocity_y)

    # Get ball position
    x1, y1, x2, y2 = canvas.coords(ball)

    # Bounce on ground
    if y2 >= 350:
        canvas.move(ball, 0, 350 - y2)

        velocity_y = -velocity_y * bounce

        # Slow down horizontal movement
        velocity_x *= 0.8

        # Stop ball when bounce is very small
        if abs(velocity_y) < 2:
            velocity_y = 0
            velocity_x = 0
            return

    # Bounce off right wall
    if x2 >= 600:
        canvas.move(ball, 600 - x2, 0)
        velocity_x = -abs(velocity_x)

    # Repeat animation
    root.after(20, move_ball)

# Start animation
move_ball()

root.mainloop()
