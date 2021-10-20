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
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'App')))
from App import Functions

class VelocidadGUI(Toplevel):
    def __init__(self, parent, name, controllerName, codo):
        super().__init__(parent)
        self.width = 1366
        self.height = 768
        self.name = name
        self.controllerName = controllerName
        self.codo = codo
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
        self.__valueBoxXi.set(0)
        self.__valueBoxXf.set(0)
        self.__valueBoxYi.set(0)
        self.__valueBoxYf.set(0)
        self.__valueBoxZi.set(0)
        self.__valueBoxZf.set(0)
        self.__valueBoxV.set(0)
        self.__valueBoxN.set(0)
        self.__valueBoxXff.set(0)
        self.__valueBoxYff.set(0)
        self.__valueBoxZff.set(0)
        self.n = 0
        self.pep = 0
        self.xi = 0
        self.xf = 0
        self.yi = 0
        self.yf = 0
        self.zi = 0
        self.zf = 0
        self.a1 = 0
        self.a2 = 0
        self.theta1 = 0
        self.theta2 = 0
        self.d3 = 0
        self.__diferentialColor = '#23395B'
        self.__plotsColor = 'white'
        self.__frameDiferentialKinematics = None
        self.__frameset()
        

    def __frameset(self):
        self.geometry('1366x768')
        self.title('Cinematica Diferencial')
        self.resizable(width=False, height=False)
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
        boxColor = '#CBF7ED'
        fontSize =("Arial", 25)
        dataFrame = Frame(self.__frameDiferentialKinematics, bg = frameColor)
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

        labelN = Label(dataFrame, text="tf", bg = frameColor, fg=foregroundLetter, font = fontSize)
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
        self.tomarDatos()
        if (self.name == 'Antropomorfico'):
            lista_q1,lista_q2,lista_q3 = Funciones.cinematicaDiferencial(self.n,self.pep,self.xi,self.yi,self.zi,self.xf,self.yf,self.zf, self.codo)
            q1 = np.array(lista_q1)
            q2 = np.array(lista_q2)
            q3 = np.array(lista_q3)

            #The figure that will contain the plot
            fig = Figure(figsize =(10,10),dpi=100)
            #Plot
            plot1 = fig.add_subplot(131)
            plot1.plot(np.arange(self.n), q1, 'bo', np.arange(self.n), q1, 'k')
            plot1.set_xlabel('n')
            plot1.set_ylabel('θ1')

            plot2 = fig.add_subplot(132)
            plot2.plot(np.arange(self.n), q2, 'bo', np.arange(self.n), q2, 'k')
            plot2.set_xlabel('n')
            plot2.set_ylabel('θ2')

            plot3 = fig.add_subplot(133)
            plot3.plot(np.arange(self.n), q3, 'bo', np.arange(self.n), q3, 'k')
            plot3.set_xlabel('n')
            plot3.set_ylabel('θ3')

            canvas = FigureCanvasTkAgg(fig,master = self.__framePlots)
            canvas.draw()
            canvas.get_tk_widget().pack(expand=True)
            
            xPos, yPos, zPos = np.zeros((1,self.n)), np.zeros((1,self.n)), np.zeros((1,self.n))

            for i in range(self.n):
                # theta, alpha, ai, dis
                a1Matrix = Functions.matrixT(np.radians(q1[i]), -1.5708, 0, 0.1555)
                a2Matrix = Functions.matrixT(np.radians(q2[i]), 0, 0.13617, 0)
                a3Matrix = Functions.matrixT(np.radians(q3[i]), 0, 0.35149, 0)
                tMatrix = Functions.totalMatrix(a1Matrix, a2Matrix, a3Matrix)
                xPos[0,i], yPos[0,i], zPos[0,i] = tMatrix[0,3], tMatrix[1,3], tMatrix[2,3]

            #The figure that will contain the plot
            fig2 = Figure(figsize =(10,10),dpi=100)
            #Plot
            plot3DPlot = fig2.add_subplot(111, projection = '3d')
            zline = zPos[0,:]
            xline = xPos[0,:]
            yline = yPos[0,:]
            plot3DPlot.plot3D(xline, yline, zline, 'gray')
            plot3DPlot.set_xlabel('px')
            plot3DPlot.set_ylabel('py')
            plot3DPlot.set_zlabel('pz')

            canvas3D = FigureCanvasTkAgg(fig2,master = self.__frame3DPlot)
            canvas3D.draw()
            canvas3D.get_tk_widget().pack(expand=True)

        else:            
            q = Funciones.SCARAVel(self.a1, self.a2, self.n, self.pep, self.xi, self.xf, self.yi, self.yf, self.zi, self.zf, self.codo)
            print("Un comentario")
            print(q[0:1,self.n-1],q[1:2,self.n-1],q[2:,self.n-1])
            print("Un comentario matriz")
            print(q)
            #The figure that will contain the plot
            fig = Figure(figsize =(10,10),dpi=100)
            #Plot
            plot1 = fig.add_subplot(131)
            plot1.plot(np.arange(self.n), q[0:1,:].T, 'bo', np.arange(self.n), q[0:1,:].T, 'k')
            plot1.set_xlabel('n')
            plot1.set_ylabel('θ1')

            plot2 = fig.add_subplot(132)
            plot2.plot(np.arange(self.n), q[1:2,:].T, 'bo', np.arange(self.n), q[1:2,:].T, 'k')
            plot2.set_xlabel('n')
            plot2.set_ylabel('θ2')

            plot3 = fig.add_subplot(133)
            plot3.plot(np.arange(self.n), q[2:,:].T, 'bo', np.arange(self.n), q[2:,:].T, 'k')
            plot3.set_xlabel('n')
            plot3.set_ylabel('d3')

            canvas = FigureCanvasTkAgg(fig,master = self.__framePlots)
            canvas.draw()
            canvas.get_tk_widget().pack(expand=True)

            xPos, yPos, zPos = np.zeros((1,self.n)), np.zeros((1,self.n)), np.zeros((1,self.n))
            
            #Calcular cinematica directa
            for i in range(self.n):
                # theta, alpha, ai, di
                a1Matrix = Functions.matrixT(q[0,i], 0, 0.1475, 0.3185)
                a2Matrix = Functions.matrixT(q[1,i], 3.14159, 0.195, 0)
                a3Matrix = Functions.matrixT(1.5708, 0, 0, q[2,i]/1000)
                tMatrix = Functions.totalMatrix(a1Matrix, a2Matrix, a3Matrix)
                xPos[0,i], yPos[0,i], zPos[0,i] = tMatrix[0,3], tMatrix[1,3], tMatrix[2,3]
            

            #The figure that will contain the plot
            fig2 = Figure(figsize =(10,10),dpi=100)
            #Plot
            plot3DPlot = fig2.add_subplot(111, projection = '3d')
            zline = zPos[0,:]
            xline = xPos[0,:]
            yline = yPos[0,:]
            plot3DPlot.plot3D(xline, yline, zline, 'gray')
            plot3DPlot.set_xlabel('px')
            plot3DPlot.set_ylabel('py')
            plot3DPlot.set_zlabel('pz')

            canvas3D = FigureCanvasTkAgg(fig2,master = self.__frame3DPlot)
            canvas3D.draw()
            canvas3D.get_tk_widget().pack(expand=True)

        self.__valueBoxXff.set(xPos[0,self.n-1])
        self.__valueBoxYff.set(yPos[0,self.n-1])
        self.__valueBoxZff.set(zPos[0,self.n-1])
        self.__realFrame()
    
    def tomarDatos(self):
        with open('..\{fname}\mydata.json'.format(fname=self.controllerName)) as json_file:
                data = json.load(json_file)
        self.a1 = data['values']['a1']
        self.a2 = data['values']['a2']
        self.n = int(self.__valueBoxN.get())
        self.pep = float(self.__valueBoxV.get())
        self.xi = float(self.__valueBoxXi.get())
        self.xf = float(self.__valueBoxXf.get())
        self.yi = float(self.__valueBoxYi.get())
        self.yf = float(self.__valueBoxYf.get())
        self.zi = float(self.__valueBoxZi.get())
        self.zf = float(self.__valueBoxZf.get())
