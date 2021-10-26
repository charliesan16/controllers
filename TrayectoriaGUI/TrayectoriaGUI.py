from tkinter import *
import tkinter.ttk as ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'App')))
from App import Functions


class TrayectoriaGUI(Toplevel):
    def __init__(self, parent, name, controllerName, codo):
        super().__init__(parent)
        self.width = 1366
        self.height = 768
        self.name = name
        self.controllerName = controllerName
        self.codo = codo
        self.my_var = 0
        self.__frameColor = '#23395B'
        self.__valueBoxXi = StringVar(0)
        self.__valueBoxXf = StringVar(0)
        self.__valueBoxYi = StringVar(0)
        self.__valueBoxYf = StringVar(0)
        self.__valueBoxZi = StringVar(0)
        self.__valueBoxZf = StringVar(0)
        self.__valueBoxN = StringVar(0)
        self.__valueBoxXi.set(0)
        self.__valueBoxXf.set(0)
        self.__valueBoxYi.set(0)
        self.__valueBoxYf.set(0)
        self.__valueBoxZi.set(0)
        self.__valueBoxZf.set(0)
        self.__valueBoxN.set(0)
        self.__valueBoxA1 = StringVar(0)
        self.__valueBoxA2 = StringVar(0)
        self.__valueBoxA3 = StringVar(0)
        self.__valueBoxV1 = StringVar(0)
        self.__valueBoxV2 = StringVar(0)
        self.__valueBoxV3 = StringVar(0)
        self.__valueBoxA1.set(0)
        self.__valueBoxA2.set(0)
        self.__valueBoxA3.set(0)
        self.__valueBoxV1.set(0)
        self.__valueBoxV2.set(0)
        self.__valueBoxV3.set(0)
        self.__frameset()

    def __frameset(self):
        self.geometry('{0}x{1}'.format(self.width, self.height))
        self.title('Planeación de Trayectoria')
        #self.resizable(width=False, height=False)
        self.__leftFrame()
        self.__rightFrame()

    def __leftFrame(self):
        self.__lefFrameParent = Frame(self, bg=self.__frameColor)
        self.__lefFrameParent.place(x=0,y=0, width = self.width*0.3, height = self.height)
        self.__topFrame()
        self.__middleFrame()
        self.__bottomFrame()

    def __topFrame(self):
        frameColor = '#23395B'
        foregroundLetter = 'white'
        boxColor = '#5C7AEA'
        fontSize =("Arial", 15)
        topFrame = Frame(self.__lefFrameParent, bg = frameColor)
        topFrame.place(x=0,y=0, width= self.width*0.3, height=self.height*0.3)

        topFrameLeft = Frame(topFrame, bg = frameColor, borderwidth=5, relief=SUNKEN)
        topFrameLeft.place(x=0,y=0, width= self.width*0.3*0.3, height=self.height*0.3)
        topFrameBoxes = Frame(topFrame, bg=frameColor)
        topFrameBoxes.place(relx=0.3,y=0, width= self.width*0.3*0.7, height=self.height*0.3)
        topFrameRightUp = Frame(topFrameBoxes, bg = frameColor, borderwidth=5, relief=SUNKEN)
        topFrameRightUp.place(x=0,y=0, width= self.width*0.3*0.7, height=self.height*0.3*0.75)
        topFrameRightDown = Frame(topFrameBoxes, bg = frameColor, borderwidth=5, relief=SUNKEN)
        topFrameRightDown.place(x=0,rely=0.75, width= self.width*0.3*0.7, height=self.height*0.3*0.25)

        #Orientación
        ttk.Style().configure('Wild.TRadiobutton', background = frameColor, foreground=foregroundLetter)
        rbCodoArriba = ttk.Radiobutton(topFrameLeft, text='Codo Arriba', variable=self.my_var, value=5, style = 'Wild.TRadiobutton')
        rbCodoAbajo = ttk.Radiobutton(topFrameLeft, text='Codo Abajo', variable=self.my_var, value=10, style = 'Wild.TRadiobutton')

        rbCodoArriba.grid(row=0, column=0, sticky="we")
        rbCodoAbajo.grid(row=1, column=0, sticky="we")
        #Perfil
        rbPolinomial = ttk.Radiobutton(topFrameLeft, text='Polinomial', variable=self.my_var, value=15, style = 'Wild.TRadiobutton')
        rbTrapezoidalA = ttk.Radiobutton(topFrameLeft, text='Trapezoidal A', variable=self.my_var, value=20, style = 'Wild.TRadiobutton')
        rbTrapezoidalV = ttk.Radiobutton(topFrameLeft, text='Trapezoidal V', variable=self.my_var, value=25, style = 'Wild.TRadiobutton')

        rbPolinomial.grid(row=2, column=0, sticky="we")
        rbTrapezoidalA.grid(row=3, column=0, sticky="we")
        rbTrapezoidalV.grid(row=4, column=0, sticky="we")

        for i in range(5):
            topFrameLeft.rowconfigure(i, weight=1)
        for i in range(1):
            topFrameLeft.columnconfigure(i, weight=1)

        #Datos de entrada
        labelXi = Label(topFrameRightUp, text="xi", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Xi = Entry(topFrameRightUp, textvariable=self.__valueBoxXi, bg = boxColor)

        labelXf = Label(topFrameRightUp, text="xf", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Xf = Entry(topFrameRightUp, textvariable=self.__valueBoxXf, bg = boxColor)

        labelYi = Label(topFrameRightUp, text="yi", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Yi = Entry(topFrameRightUp, textvariable=self.__valueBoxYi, bg = boxColor)

        labelYf = Label(topFrameRightUp, text="yf", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Yf = Entry(topFrameRightUp, textvariable=self.__valueBoxYf, bg = boxColor)

        labelZi = Label(topFrameRightUp, text="zi", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Zi = Entry(topFrameRightUp, textvariable=self.__valueBoxZi, bg = boxColor)

        labelZf = Label(topFrameRightUp, text="zf", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Zf = Entry(topFrameRightUp, textvariable=self.__valueBoxZf, bg = boxColor)

        labelTf = Label(topFrameRightDown, text="tf", bg = frameColor, fg=foregroundLetter, font = fontSize)
        Tf = Entry(topFrameRightDown, textvariable=self.__valueBoxN, bg = boxColor)

        #Grilla
        labelXi.grid(row=0, column=1)
        labelXf.grid(row=0, column=3)
        labelYi.grid(row=1, column=1)
        labelYf.grid(row=1, column=3)
        labelZi.grid(row=2, column=1)
        labelZf.grid(row=2, column=3)
        Xi.grid(row=0, column=2)
        Xf.grid(row=0, column=4)
        Yi.grid(row=1, column=2)
        Yf.grid(row=1, column=4)
        Zi.grid(row=2, column=2)
        Zf.grid(row=2, column=4)

        labelTf.grid(row=0, column=0)
        Tf.grid(row=0, column=1)

        for i in range(3):
            topFrameRightUp.rowconfigure(i, weight=1)
        for i in range(1,5):
            topFrameRightUp.columnconfigure(i, weight=1)

        for i in range(1):
            topFrameRightDown.rowconfigure(i, weight=1)
        for i in range(2):
            topFrameRightDown.columnconfigure(i, weight=1)

    def __middleFrame(self):
        frameColor = '#23395B'
        foregroundLetter = 'white'
        boxColor = '#5C7AEA'
        fontSize =("Arial", 15)
        middleFrame = Frame(self.__lefFrameParent, bg = frameColor)
        middleFrame.place(x=0,rely=0.3, width= self.width*0.3, height=self.height*0.3)
        middleFrameUp = Frame(middleFrame, bg = frameColor)
        middleFrameUp.place(x=0,y=0, width= self.width*0.3, height=self.height*0.3*0.8)
        middleFrameDown = Frame(middleFrame, bg = frameColor)
        middleFrameDown.place(x=0,rely=0.8, width= self.width*0.3, height=self.height*0.3*0.2)
        #Datos de entrada
        labelA1 = Label(middleFrameUp, text="A1", bg = frameColor, fg=foregroundLetter, font = fontSize)
        A1 = Entry(middleFrameUp, textvariable=self.__valueBoxA1, bg = boxColor)

        labelA2 = Label(middleFrameUp, text="A2", bg = frameColor, fg=foregroundLetter, font = fontSize)
        A2 = Entry(middleFrameUp, textvariable=self.__valueBoxA2, bg = boxColor)

        labelA3 = Label(middleFrameUp, text="A3", bg = frameColor, fg=foregroundLetter, font = fontSize)
        A3 = Entry(middleFrameUp, textvariable=self.__valueBoxA3, bg = boxColor)

        labelV1 = Label(middleFrameUp, text="V1", bg = frameColor, fg=foregroundLetter, font = fontSize)
        V1 = Entry(middleFrameUp, textvariable=self.__valueBoxV1, bg = boxColor)

        labelV2 = Label(middleFrameUp, text="V2", bg = frameColor, fg=foregroundLetter, font = fontSize)
        V2 = Entry(middleFrameUp, textvariable=self.__valueBoxV2, bg = boxColor)

        labelV3 = Label(middleFrameUp, text="V3", bg = frameColor, fg=foregroundLetter, font = fontSize)
        V3 = Entry(middleFrameUp, textvariable=self.__valueBoxV3, bg = boxColor)

        #Grilla
        labelA1.grid(row=0, column=2)
        labelA2.grid(row=0, column=4)
        labelA3.grid(row=0, column=6)
        labelV1.grid(row=2, column=2)
        labelV2.grid(row=2, column=4)
        labelV3.grid(row=2, column=6)

        A1.grid(row=1, column=2)
        A2.grid(row=1, column=4)
        A3.grid(row=1, column=6)
        V1.grid(row=3, column=2)
        V2.grid(row=3, column=4)
        V3.grid(row=3, column=6)

        #Botones
        buttonCalculate = Button(middleFrameDown, text='Calcular', bg='#8EA8C3', fg = "black", command= self.buttonCalcular) 
        buttonClear = Button(middleFrameDown, text='Clear', bg='#8EA8C3', fg = "black", command= self.buttonCalcular) 

        buttonCalculate.grid(row=1,column=0, sticky="nsew")
        buttonClear.grid(row=1,column=1, sticky="nsew")

        for i in range(4):
            middleFrameUp.rowconfigure(i, weight=1)
        for i in range(1,8):
            middleFrameUp.columnconfigure(i, weight=1)

        middleFrameDown.rowconfigure(1, weight=1)
        for i in range(2):
            middleFrameDown.columnconfigure(i, weight=1)

    def __bottomFrame(self):
        bottomFrame = Frame(self.__lefFrameParent, bg = 'white', borderwidth=5, relief=SUNKEN)
        bottomFrame.place(x=0,rely=0.6, width= self.width*0.3, height=self.height*0.4)
        #The figure that will contain the plot
        fig2 = Figure(figsize =(10,10),dpi=100)
        #Plot
        plot3DPlot = fig2.add_subplot(111, projection = '3d')
        zline = np.arange(100)
        xline = np.arange(100)
        yline = np.arange(100)
        plot3DPlot.plot3D(xline, yline, zline, 'gray')
        plot3DPlot.set_xlabel('x')
        plot3DPlot.set_ylabel('y')
        plot3DPlot.set_zlabel('z')

        canvas3D = FigureCanvasTkAgg(fig2,master = bottomFrame)
        canvas3D.draw()
        canvas3D.get_tk_widget().pack(expand=True)


    def __rightFrame(self):
        framePlots = Frame(self, bg = 'white')
        framePlots.place(relx=0.3,y=0, width = self.width*0.7, height = self.height)

        framePlotUp = Frame(framePlots, bg = 'white', borderwidth=5, relief=SUNKEN)
        framePlotUp.place(x=0,y=0, width = self.width*0.7, height = self.height*0.33)

        framePlotMiddle = Frame(framePlots, bg = 'white', borderwidth=5, relief=SUNKEN)
        framePlotMiddle.place(x=0,rely=(1/3), width = self.width*0.7, height = self.height*0.33)

        framePlotDown = Frame(framePlots, bg = 'white', borderwidth=5, relief=SUNKEN)
        framePlotDown.place(x=0,rely=(2/3), width = self.width*0.7, height = self.height*0.33)

        #The figure that will contain the plot
        fig = Figure(figsize =(10,10),dpi=100)
        fig2 = Figure(figsize =(10,10),dpi=100)
        fig3 = Figure(figsize =(10,10),dpi=100)
        plot1 = fig.add_subplot(111)
        plot1.plot(np.arange(10), np.arange(10), 'bo')
        plot1.set_xlabel('x')
        plot1.set_ylabel('y')

        plot2 = fig2.add_subplot(111)
        plot2.plot(np.arange(10), np.arange(10), 'bo')
        plot2.set_xlabel('x')
        plot2.set_ylabel('y')

        plot3 = fig3.add_subplot(111)
        plot3.plot(np.arange(10), np.arange(10), 'bo')
        plot3.set_xlabel('x')
        plot3.set_ylabel('y')

        canvas = FigureCanvasTkAgg(fig,master = framePlotUp)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True)

        canvas2 = FigureCanvasTkAgg(fig2,master = framePlotMiddle)
        canvas2.draw()
        canvas2.get_tk_widget().pack(expand=True)

        canvas3 = FigureCanvasTkAgg(fig3,master = framePlotDown)
        canvas3.draw()
        canvas3.get_tk_widget().pack(expand=True)

    def buttonCalcular(self):
        pass