#!/usr/bin/python3

import tkinter as tk
import plotter

def main():
    root = tk.Tk()
    root.title("Canvas")
    
    canvas = tk.Canvas(root,width=800,height=500)
    canvas.pack()
    
    exitBtn = tk.Button(root,text="Exit",command=exit)
    exitBtn.pack()
    
    plot = plotter.Plotter(canvas,50)
    plot.makeCross(100,150)
    
    root.mainloop()
    
main()
