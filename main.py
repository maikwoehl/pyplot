#!/usr/bin/python3

import tkinter as tk
import plotter

# TODO:
# - steps
# -- calculate amount
# -- generate positive and negative list

def main():
    root = tk.Tk()
    root.title("Canvas")
    
    canvas = tk.Canvas(root,width=500,height=500)
    canvas.pack()
    
    exitBtn = tk.Button(root,text="Exit",command=exit)
    exitBtn.pack()
    
    #makeGrid(canvas, 500,500)
    #makeCross(canvas, 100,150)
    
    plot = plotter.Plotter(canvas,500,500)
    plot.makeCross(100,150)
    
    root.mainloop()
    
main()
