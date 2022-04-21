from tkinter import *
from tkinter import ttk
from tkinter import font
from ttkbootstrap import Style
import numpy as np
from matplotlib import pyplot as plt 


style = Style('superhero')
window = style.master
window.title("graphs")
window.geometry("700x700")

def mainWindow():
    titleLabel = ttk.Label(window, text="Trendová spojnica maker", font="Helvetica 18 bold")
    titleLabel.config(anchor=CENTER)
    titleLabel.pack(pady=20)
    xaxisLabel = ttk.Label(window, text="Osa X: ", font="Helvetica 12 bold").pack(pady=5)
    xaxisEntry = ttk.Entry(window, width=90)
    xaxisEntry.pack()
    yaxisLabel = ttk.Label(window, text="Osa Y: ", font="Helvetica 12 bold").pack(pady=5)
    yaxisEntry = ttk.Entry(window, width=90)
    yaxisEntry.pack()
    polynomeLabel = ttk.Label(window, text="Stupeň polynómu: ", font="Helvetica 12 bold").pack(pady=5)
    polynomeEntry = ttk.Entry(window, width=90)
    polynomeEntry.pack()


    def plotGraph():
        xaxis = xaxisEntry.get()
        yaxis = yaxisEntry.get()
        x = []
        y = []
        x = xaxis.split(", ")
        for i in range(len(x)):
            x[i] = int(x[i])
            i += 1    
        y = yaxis.split(", ")
        for i in range(len(y)): 
            y[i] = int(y[i])
            i += 1

        plt.plot(x, y, color ='r',  marker = 'x', linestyle = 'none', label = 'Legend')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Polynomicka funkcia')

        zadanie = polynomeEntry.get()
        z = np.polyfit(x, y, int(zadanie))
        p = np.poly1d(z)
        plt.plot(x,p(x),"b:")
        print(z)

        zLabel = ttk.Label(window, text=z, font="Helvetica 12 bold").pack(pady=5)

        plt.legend()
        plt.grid()
        plt.show()

    plotButton = ttk.Button(window, text="Plot", command=plotGraph, style="danger.TButton").pack(pady=20)

mainWindow()
window.mainloop() 