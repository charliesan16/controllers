from tkinter import *
import tkinter.ttk as ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure
import Funciones
import json

class VelocidadGUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.width = 1366
        self.height = 768
        self.__framePlots = None
        self.__frame3DPlot = None
        self.__valueBoxXi = StringVar(0)
        self.__valueBoxXf = StringVar(0)
        self.__valueBoxYi = StringVar(0)
        self.__valueBoxYf = StringVar(0)
        self.__valueBoxZi = StringVar(0)
        self.__valueBoxZf = StringVar(0)
        self.__valueBoxV = StringVar(0)
        self.__valueBoxN = StringVar(0)
        self.__valueBoxXff = StringVar(0)
        self.__valueBoxYff = StringVar(0)
        self.__valueBoxZff = StringVar(0)
        self.__diferentialColor = '#23395B'
        self.__plotsColor = 'white'
        self.__frameDiferentialKinematics = None
        self.__frameset()

    def __frameset(self):
        self.geometry('1366x768')
        self.title('Cinematica Diferencial')
        self.__diferentialKinematicsFrame()
        self.__plotsFrame()

    def __diferentialKinematicsFrame(self):
        frameColor = self.__diferentialColor
        self.__frameDiferentialKinematics = Frame(self, bg = frameColor)
        self.__frameDiferentialKinematics.place(x=0,y=0, width = self.width*0.3, height = self.height)
        self.__dataFrame()
        self.__realFrame()
        self.__buttonsFrame()

    def __dataFrame(self):
        frameColor = '#23395B'
        foregroundLetter = 'white'
        boxColor = '#5C7AEA'
        fontSize =("Arial", 25)
        dataFrame = Frame(self.__frameDiferentialKinematics, bg = frameColor, highlightbackground="black")
        dataFrame.place(x=0,y=0, width = self.width*0.3*0.5, height = self.height*0.7)
        
        #Entradas
        labelXi = Label(dataFrame, text="xi", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Xi = Entry(dataFrame, textvariable=self.__valueBoxXi, width = 20, bg = boxColor)

        labelXf = Label(dataFrame, text="xf", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Xf = Entry(dataFrame, textvariable=self.__valueBoxXf, width = 20, bg = boxColor)

        labelYi = Label(dataFrame, text="yi", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Yi = Entry(dataFrame, textvariable=self.__valueBoxYi, width = 20, bg = boxColor)

        labelYf = Label(dataFrame, text="yf", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Yf = Entry(dataFrame, textvariable=self.__valueBoxYf, width = 20, bg = boxColor)

        labelZi = Label(dataFrame, text="zi", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Zi = Entry(dataFrame, textvariable=self.__valueBoxZi, width = 20, bg = boxColor)

        labelZf = Label(dataFrame, text="zf", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Zf = Entry(dataFrame, textvariable=self.__valueBoxZf, width = 20, bg = boxColor)

        labelV = Label(dataFrame, text="V", bg = frameColor, fg=foregroundLetter, font = fontSize)
        V = Entry(dataFrame, textvariable=self.__valueBoxV, width = 20, bg = boxColor)

        labelN = Label(dataFrame, text="n", bg = frameColor, fg=foregroundLetter, font = fontSize)
        N = Entry(dataFrame, textvariable=self.__valueBoxN, width = 20, bg = boxColor)

        #Grilla
        labelXi.grid(row=0, column=0)
        labelXf.grid(row=0, column=1)
        Xi.grid(row=1, column=0)
        Xf.grid(row=1, column=1)
        labelYi.grid(row=2, column=0)
        labelYf.grid(row=2, column=1)
        Yi.grid(row=3, column=0)
        Yf.grid(row=3, column=1)
        labelZi.grid(row=4, column=0)
        labelZf.grid(row=4, column=1)
        Zi.grid(row=5, column=0)
        Zf.grid(row=5, column=1)
        labelV.grid(row=6, column=0)
        labelN.grid(row=6, column=1)
        V.grid(row=7, column=0)
        N.grid(row=7, column=1)

        for i in range(2):
            dataFrame.columnconfigure(i, weight=1)

        for i in range(8):
            dataFrame.rowconfigure(i, weight=1)
   

    def __realFrame(self):
        frameColor = '#23395B'
        foregroundLetter = 'white'
        boxColor = '#5C7AEA'
        fontSize =("Arial", 25)
        realFrame = Frame(self.__frameDiferentialKinematics, bg = frameColor, highlightbackground="black")
        realFrame.place(relx=0.5, y=0, width = self.width*0.3*0.5, height = self.height*0.7)

        #Entradas
        labelXf = Label(realFrame, text="xf", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Xf = Entry(realFrame, textvariable=self.__valueBoxXff, width = 20, bg = boxColor)

        labelYf = Label(realFrame, text="yf", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Yf = Entry(realFrame, textvariable=self.__valueBoxYff, width = 20, bg = boxColor)

        labelZf = Label(realFrame, text="zf", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Zf = Entry(realFrame, textvariable=self.__valueBoxZff, width = 20, bg = boxColor)

        #Grilla
        labelXf.grid(row=0, column=0)
        Xf.grid(row=1, column=0)
        labelYf.grid(row=2, column=0)
        Yf.grid(row=3, column=0)
        labelZf.grid(row=4, column=0)
        Zf.grid(row=5, column=0)

        realFrame.columnconfigure(0, weight=1)

        for i in range(6):
            realFrame.rowconfigure(i, weight=1)

    def __buttonsFrame(self):
        frameColor = '#161925'
        buttonsFrame = Frame(self.__frameDiferentialKinematics, bg = frameColor)
        buttonsFrame.place(x=0,rely=0.7, width = self.width*0.3, height = self.height*0.3)
        buttonCalculate = Button(buttonsFrame, text='Cinematica Diferencial', bg='#8EA8C3', fg = "black", font=("Arial", 25), command= self.buttonCalcular) 
        buttonCalculate.grid(row=1,column=1, sticky="nsew")
        for i in range(3):
            buttonsFrame.rowconfigure(i, weight=1)
        for i in range(3):
            buttonsFrame.columnconfigure(i, weight=1)

    def __plotsFrame(self):
        frameColor = self.__plotsColor
        self.__framePlots = Frame(self, bg = frameColor)
        self.__framePlots.place(relx=0.3,y=0, width = self.width*0.7, height = self.height*0.5)
        self.__frame3DPlot = Frame(self, bg = 'white')
        self.__frame3DPlot.place(relx=0.3, rely=0.5, width = self.width*0.7, height = self.height*0.5)


    def buttonCalcular(self):
        with open('..\AntropomorphController\mydata.json') as json_file:
            data = json.load(json_file)
        a1 = data['values']['a1']
        a2 = data['values']['a2']
        theta1 = data['values']['theta1']
        theta2 = data['values']['theta2']
        #n = float(self.__valueBoxN.get())
        n = 30
        pep = data['values']['pep']
        #xi = float(self.__valueBoxXi.get())
        #xf = float(self.__valueBoxXf.get())
        #yi = float(self.__valueBoxYi.get())
        #yf = float(self.__valueBoxYf.get())
        #zi = float(self.__valueBoxZf.get())
        #zf = float(self.__valueBoxZf.get())
        d3 = data['values']['d3']
        #2, 0.278051, 0.31, 0.046298, 0.1, 0.2185, 0.3, 0.1
        q = Funciones.SCARAVel(a1, a2, theta1, theta2,
         n, pep, 0.278051, 0.31, 0.046298, 0.1, 0.2185, 0.3, d3)
        #The figure that will contain the plot
        fig = Figure(figsize =(10,10),dpi=100)
        #Plot
        plot1 = fig.add_subplot(131)
        plot1.plot(np.arange(n), q[0:1,:].T, 'bo', np.arange(n), q[0:1,:].T, 'k') 

        plot2 = fig.add_subplot(132)
        plot2.plot(np.arange(n), q[1:2,:].T, 'bo', np.arange(n), q[1:2,:].T, 'k')

        plot3 = fig.add_subplot(133)
        plot3.plot(np.arange(n), q[2:,:].T, 'bo', np.arange(n), q[2:,:].T, 'k')

        canvas = FigureCanvasTkAgg(fig,master = self.__framePlots)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True)

        #The figure that will contain the plot
        fig2 = Figure(figsize =(10,10),dpi=100)
        #Plot
        plot3DPlot = fig2.add_subplot(111, projection = '3d')
        zline = np.linspace(0, 15, 1000)
        xline = np.sin(zline)
        yline = np.cos(zline)
        plot3DPlot.plot3D(xline, yline, zline, 'gray')

        canvas3D = FigureCanvasTkAgg(fig2,master = self.__frame3DPlot)
        canvas3D.draw()
        canvas3D.get_tk_widget().pack(expand=True)
