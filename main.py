import tkinter as tk

# Define the complex plane and the maximum number of iterations
xmin, xmax, ymin, ymax = -2, 1, -1, 1
max_iter = 100

# Define the size of the canvas and the scale factor
width, height = 640, 480
xscale = (xmax - xmin) / width
yscale = (ymax - ymin) / height

# Create the main window and canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

# Draw the Mandelbrot set
for x in range(width):
    for y in range(height):
        c = complex(xmin + x * xscale, ymin + y * yscale)
        z = complex(0, 0)
        for i in range(max_iter):
            if abs(z) > 2:
                break
            z = z**2 + c
        color = "#%02x%02x%02x" % (i*255//max_iter, i*255//max_iter, i*255//max_iter)
        canvas.create_rectangle(x, y, x+1, y+1, fill=color, outline="")

# Start the main loop
root.mainloop()
