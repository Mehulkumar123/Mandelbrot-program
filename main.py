import tkinter as tk

xmin, xmax, ymin, ymax = -2, 1, -1, 1
max_iter = 100

width, height = 640, 480
xscale = (xmax - xmin) / width
yscale = (ymax - ymin) / height

zoom_factor = 0.5

root = tk.Tk()
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

def draw():
    canvas.delete("all")
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

def zoom_in(event):
    global xmin, xmax, ymin, ymax, xscale, yscale
    x = event.x
    y = event.y
    xc = xmin + x * xscale
    yc = ymin + y * yscale
    xscale *= zoom_factor
    yscale *= zoom_factor
    xmin = xc - (xscale * width / 2)
    xmax = xc + (xscale * width / 2)
    ymin = yc - (yscale * height / 2)
    ymax = yc + (yscale * height / 2)
    draw()

def zoom_out(event):
    global xmin, xmax, ymin, ymax, xscale, yscale
    x = event.x
    y = event.y
    xc = xmin + x * xscale
    yc = ymin + y * yscale
    xscale /= zoom_factor
    yscale /= zoom_factor
    xmin = xc - (xscale * width / 2)
    xmax = xc + (xscale * width / 2)
    ymin = yc - (yscale * height / 2)
    ymax = yc + (yscale * height / 2)
    draw()

def update_max_iter(value):
    global max_iter
    max_iter = int(value)
    draw()

canvas.bind("<Button-1>", zoom_in)
canvas.bind("<Button-3>", zoom_out)
max_iter_slider = tk.Scale(root, from_=50, to=500, orient="horizontal", label="Max iterations", command=update_max_iter)
max_iter_slider.pack()

draw()

root.mainloop()
