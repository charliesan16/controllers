from tkinter import *
import tkinter.ttk as ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure
import FuncionesTrayectoria
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'App')))
from App import Functions




class TrayectoriaGUI(Toplevel):
    def __init__(self, parent, name, controllerName, codo, l1, l2, l3):
        super().__init__(parent)
        self.width = 1366
        self.height = 768
        self.name = name
        self.controllerName = controllerName
        self.codo = codo
        self.__l1 = l1
        self.__l2 = l2
        self.__l3 = l3
        self.my_var = IntVar() 
        self.__flag = "arriba"
        self.__frameColor = '#23395B'
        self.__valueBoxXi = DoubleVar(0)
        self.__valueBoxXf = DoubleVar(0)
        self.__valueBoxYi = DoubleVar(0)
        self.__valueBoxYf = DoubleVar(0)
        self.__valueBoxZi = DoubleVar(0)
        self.__valueBoxZf = DoubleVar(0)
        self.__valueBoxTf = DoubleVar(0)
        self.__valueBoxXi.set(0)
        self.__valueBoxXf.set(0)
        self.__valueBoxYi.set(0)
        self.__valueBoxYf.set(0)
        self.__valueBoxZi.set(0)
        self.__valueBoxZf.set(0)
        self.__valueBoxTf.set(0)
        self.__valueBoxA1 = DoubleVar(0)
        self.__valueBoxA2 = DoubleVar(0)
        self.__valueBoxA3 = DoubleVar(0)
        self.__valueBoxV1 = DoubleVar(0)
        self.__valueBoxV2 = DoubleVar(0)
        self.__valueBoxV3 = DoubleVar(0)
        self.__valueBoxA1.set(0)
        self.__valueBoxA2.set(0)
        self.__valueBoxA3.set(0)
        self.__valueBoxV1.set(0)
        self.__valueBoxV2.set(0)
        self.__valueBoxV3.set(0)
        self.rbPolinomial = None
        self.rbTrapezoidalA = None
        self.rbTrapezoidalV = None
        self.A1 = None
        self.A2 = None
        self.A3 = None
        self.V1 = None
        self.V2 = None
        self.V3 = None
        self.changeFlag = True
        self.theta1i, self.theta2i, self.theta3i, self.d3i = None, None, None, None
        self.theta1f, self.theta2f, self.theta3f, self.d3f = None, None, None, None
        self.n = 1000
        self.dt = None
        self.q1, self.q1p, self.q1pp = None, None, None
        self.q2, self.q2p, self.q2pp = None, None, None
        self.q3, self.q3p, self.q3pp = None, None, None
        self.q1t1, self.q1pt1, self.q1ppt1 = None, None, None
        self.q2t1, self.q2pt1, self.q2ppt1 = None, None, None
        self.q3t1, self.q3pt1, self.q3ppt1 = None, None, None
        self.q1t2, self.q1pt2, self.q1ppt2 = None, None, None
        self.q2t2, self.q2pt2, self.q2ppt2 = None, None, None
        self.q3t2, self.q3pt2, self.q3ppt2 = None, None, None
        self.__frameset()

    def __frameset(self):
        self.geometry('{0}x{1}'.format(self.width, self.height))
        self.title('Planeación de Trayectoria')
        #self.resizable(width=False, height=False)
        self.__leftFrame()
        self.__rightFrame()
        self.__menu()

    def __menu(self):
        newMenu = Menu(self)
        self.config(menu=newMenu)
        menuCascada2 = Menu(newMenu, tearoff="off")
        newMenu.add_cascade(label="Codo", menu=menuCascada2)
        menuCascada2.add_command(label="Codo Arriba", command= self.elbowUp)
        menuCascada2.add_command(label="Codo Abajo", command= self.elbowDown)

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
        #topFrameLeftDown = Frame(topFrame, bg = frameColor, borderwidth=5, relief=SUNKEN)
        #topFrameLeftDown.place(x=0,rely=0.4, width= self.width*0.3*0.3, height=self.height*0.3*0.6)
        topFrameBoxes = Frame(topFrame, bg=frameColor)
        topFrameBoxes.place(relx=0.3,y=0, width= self.width*0.3*0.7, height=self.height*0.3)
        topFrameRightUp = Frame(topFrameBoxes, bg = frameColor, borderwidth=5, relief=SUNKEN)
        topFrameRightUp.place(x=0,y=0, width= self.width*0.3*0.7, height=self.height*0.3*0.75)
        topFrameRightDown = Frame(topFrameBoxes, bg = frameColor, borderwidth=5, relief=SUNKEN)
        topFrameRightDown.place(x=0,rely=0.75, width= self.width*0.3*0.7, height=self.height*0.3*0.25)

        #Orientación
        ttk.Style().configure('Wild.TRadiobutton', background = frameColor, foreground=foregroundLetter)
        #rbCodoArriba = ttk.Radiobutton(topFrameLeftTop, text='Codo Arriba', variable=self.my_var, value=5, style = 'Wild.TRadiobutton')
        #rbCodoAbajo = ttk.Radiobutton(topFrameLeftTop, text='Codo Abajo', variable=self.my_var, value=10, style = 'Wild.TRadiobutton')

        #rbCodoArriba.grid(row=0, column=0, sticky="we")
        #rbCodoAbajo.grid(row=1, column=0, sticky="we")
        #Perfil
        
        self.rbPolinomial = ttk.Radiobutton(topFrameLeft, text='Polinomial', variable=self.my_var, value=1, style = 'Wild.TRadiobutton', command=self.ShowChoice)
        self.rbTrapezoidalA = ttk.Radiobutton(topFrameLeft, text='Trapezoidal A', variable=self.my_var, value=2, style = 'Wild.TRadiobutton', command=self.ShowChoice)
        self.rbTrapezoidalV = ttk.Radiobutton(topFrameLeft, text='Trapezoidal V', variable=self.my_var, value=3, style = 'Wild.TRadiobutton', command=self.ShowChoice)

        self.rbPolinomial.invoke()

        self.rbPolinomial.grid(row=0, column=0, sticky="we")
        self.rbTrapezoidalA.grid(row=1, column=0, sticky="we")
        self.rbTrapezoidalV.grid(row=2, column=0, sticky="we")

        #for i in range(2):
        #    topFrameLeftTop.rowconfigure(i, weight=1)
        #for i in range(1):
        #    topFrameLeftTop.columnconfigure(i, weight=1)

        for i in range(3):
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
        Tf = Entry(topFrameRightDown, textvariable=self.__valueBoxTf, bg = boxColor)

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
        self.A1 = Entry(middleFrameUp, textvariable=self.__valueBoxA1, bg = boxColor, state='disable')

        labelA2 = Label(middleFrameUp, text="A2", bg = frameColor, fg=foregroundLetter, font = fontSize)
        self.A2 = Entry(middleFrameUp, textvariable=self.__valueBoxA2, bg = boxColor, state='disable')

        labelA3 = Label(middleFrameUp, text="A3", bg = frameColor, fg=foregroundLetter, font = fontSize)
        self.A3 = Entry(middleFrameUp, textvariable=self.__valueBoxA3, bg = boxColor, state='disable')

        labelV1 = Label(middleFrameUp, text="V1", bg = frameColor, fg=foregroundLetter, font = fontSize)
        self.V1 = Entry(middleFrameUp, textvariable=self.__valueBoxV1, bg = boxColor, state='disable')

        labelV2 = Label(middleFrameUp, text="V2", bg = frameColor, fg=foregroundLetter, font = fontSize)
        self.V2 = Entry(middleFrameUp, textvariable=self.__valueBoxV2, bg = boxColor, state='disable')

        labelV3 = Label(middleFrameUp, text="V3", bg = frameColor, fg=foregroundLetter, font = fontSize)
        self.V3 = Entry(middleFrameUp, textvariable=self.__valueBoxV3, bg = boxColor, state='disable')

        #Grilla
        labelA1.grid(row=0, column=2)
        labelA2.grid(row=0, column=4)
        labelA3.grid(row=0, column=6)
        labelV1.grid(row=2, column=2)
        labelV2.grid(row=2, column=4)
        labelV3.grid(row=2, column=6)

        self.A1.grid(row=1, column=2)
        self.A2.grid(row=1, column=4)
        self.A3.grid(row=1, column=6)
        self.V1.grid(row=3, column=2)
        self.V2.grid(row=3, column=4)
        self.V3.grid(row=3, column=6)

        #Botones
        buttonCalculate = Button(middleFrameDown, text='Calcular', bg='#8EA8C3', fg = "black", command= self.buttonCalcular) 
        buttonClear = Button(middleFrameDown, text='Clear', bg='#8EA8C3', fg = "black", command= self.buttonClear) 

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

        self.framePlotUp = Frame(framePlots, bg = 'white', borderwidth=5, relief=SUNKEN)
        self.framePlotUp.place(x=0,y=0, width = self.width*0.7, height = self.height*0.33)

        self.framePlotMiddle = Frame(framePlots, bg = 'white', borderwidth=5, relief=SUNKEN)
        self.framePlotMiddle.place(x=0,rely=(1/3), width = self.width*0.7, height = self.height*0.33)

        self.framePlotDown = Frame(framePlots, bg = 'white', borderwidth=5, relief=SUNKEN)
        self.framePlotDown.place(x=0,rely=(2/3), width = self.width*0.7, height = self.height*0.33)

    def buttonCalcular(self):
        dt = self.__valueBoxTf.get()/self.n
        if self.name == "Antropomorfico":
            if self.my_var.get() == 1:
                self.q1, self.q1p, self.q1pp = FuncionesTrayectoria.treyectoriaCuadratAntro(self.theta1i, self.theta1f, self.__valueBoxTf.get(), dt)
                self.q2, self.q2p, self.q2pp = FuncionesTrayectoria.treyectoriaCuadratAntro(self.theta2i, self.theta2f, self.__valueBoxTf.get(), dt)
                self.q3, self.q3p, self.q3pp = FuncionesTrayectoria.treyectoriaCuadratAntro(self.theta3i, self.theta3f, self.__valueBoxTf.get(), dt)
                self.graficar(self.q1, self.q1p, self.q1pp, self.q2, self.q2p, self.q2pp, self.q3, self.q3p, self.q3pp)
            elif self.my_var.get() == 2:
                self.q1t2, self.q1pt2, self.q1ppt2 = FuncionesTrayectoria.trapes2Antropo(self.__valueBoxA1.get(), self.theta1i, self.theta1f, self.__valueBoxTf.get(), dt)
                self.q2t2, self.q2pt2, self.q2ppt2 = FuncionesTrayectoria.trapes2Antropo(self.__valueBoxA2.get(), self.theta2i, self.theta2f, self.__valueBoxTf.get(), dt)
                self.q3t2, self.q3pt2, self.q3ppt2 = FuncionesTrayectoria.trapes2Antropo(self.__valueBoxA3.get(), self.theta3i, self.theta3f, self.__valueBoxTf.get(), dt)
                self.graficar(self.q1t2, self.q1pt2, self.q1ppt2, self.q2t2, self.q2pt2, self.q2ppt2, self.q3t2, self.q3pt2, self.q3ppt2)
            elif self.my_var.get() == 3:
                self.q1t1, self.q1pt1, self.q1ppt1 = FuncionesTrayectoria.trapes1Antropo(self.__valueBoxV1.get(), self.theta1i, self.theta1f, self.__valueBoxTf.get(), dt)
                self.q2t1, self.q2pt1, self.q2ppt1 = FuncionesTrayectoria.trapes1Antropo(self.__valueBoxV2.get(), self.theta2i, self.theta2f, self.__valueBoxTf.get(), dt)
                self.q3t1, self.q3pt1, self.q3ppt1 = FuncionesTrayectoria.trapes1Antropo(self.__valueBoxV3.get(), self.theta3i, self.theta3f, self.__valueBoxTf.get(), dt)
                self.graficar(self.q1t1, self.q1pt1, self.q1ppt1, self.q2t1, self.q2pt1, self.q2ppt1, self.q3t1, self.q3pt1, self.q3ppt1)
            else:
                pass
        else:
            if self.my_var.get() == 1:
                self.q1, self.q1p, self.q1pp = FuncionesTrayectoria.treyectoriaCuadratSCARA(self.theta1i, self.theta1f, self.__valueBoxTf.get(), dt)
                self.q2, self.q2p, self.q2pp = FuncionesTrayectoria.treyectoriaCuadratSCARA(self.theta2i, self.theta2f, self.__valueBoxTf.get(), dt)
                self.q3, self.q3p, self.q3pp = FuncionesTrayectoria.treyectoriaCuadratSCARA(self.d3i/100, self.d3f/100, self.__valueBoxTf.get(), dt)
                self.graficar(self.q1, self.q1p, self.q1pp, self.q2, self.q2p, self.q2pp, self.q3, self.q3p, self.q3pp)
            elif self.my_var.get() == 2:
                self.q1t2, self.q1pt2, self.q1ppt2 = FuncionesTrayectoria.trapes2SCARA(self.__valueBoxA1.get(), self.theta1i, self.theta1f, self.__valueBoxTf.get(), dt)
                self.q2t2, self.q2pt2, self.q2ppt2 = FuncionesTrayectoria.trapes2SCARA(self.__valueBoxA2.get(), self.theta2i, self.theta2f, self.__valueBoxTf.get(), dt)
                self.q3t2, self.q3pt2, self.q3ppt2 = FuncionesTrayectoria.trapes2SCARA(self.__valueBoxA3.get(), self.d3i/100, self.d3f/100, self.__valueBoxTf.get(), dt)
                print(self.q1t2, self.q1pt2, self.q1ppt2, self.q2t2, self.q2pt2, self.q2ppt2, self.q3t2, self.q3pt2, self.q3ppt2)
                self.graficar(self.q1t2, self.q1pt2, self.q1ppt2, self.q2t2, self.q2pt2, self.q2ppt2, self.q3t2, self.q3pt2, self.q3ppt2)
            elif self.my_var.get() == 3:
                self.q1t1, self.q1pt1, self.q1ppt1 = FuncionesTrayectoria.trapes1SCARA(self.__valueBoxV1.get(), self.theta1i, self.theta1f, self.__valueBoxTf.get(), dt)
                self.q2t1, self.q2pt1, self.q2ppt1 = FuncionesTrayectoria.trapes1SCARA(self.__valueBoxV2.get(), self.theta2i, self.theta2f, self.__valueBoxTf.get(), dt)
                self.q3t1, self.q3pt1, self.q3ppt1 = FuncionesTrayectoria.trapes1SCARA(self.__valueBoxV3.get(), self.d3i/100, self.d3f/100, self.__valueBoxTf.get(), dt)
                self.graficar(self.q1t1, self.q1pt1, self.q1ppt1, self.q2t1, self.q2pt1, self.q2ppt1, self.q3t1, self.q3pt1, self.q3ppt1)
                pass

        

    def buttonClear(self):
        pass

    def elbowUp(self):
        self.__flag = "arriba"
        self.calcular()
        

    def elbowDown(self):
        self.__flag = "abajo"
        self.calcular()

    def calcular(self):
        if self.name == "Antropomorfico":
            self.theta1i, self.theta2i, self.theta3i = self.inverse(self.__valueBoxXi.get(), self.__valueBoxYi.get(), self.__valueBoxZi.get())
            self.theta1f, self.theta2f, self.theta3f = self.inverse(self.__valueBoxXf.get(), self.__valueBoxYf.get(), self.__valueBoxZf.get())
        else:
            self.theta1i, self.theta2i, self.d3i = self.inverse(self.__valueBoxXi.get(), self.__valueBoxYi.get(), self.__valueBoxZi.get())
            self.theta1f, self.theta2f, self.d3f = self.inverse(self.__valueBoxXf.get(), self.__valueBoxYf.get(), self.__valueBoxZf.get())

    def inverse(self, x, y, z):
        P = np.array([x, y, z]).astype(float)
        L = [self.__l1, self.__l2, self.__l3]
        if self.__flag == "arriba":
            value1, _, value2, _, value3, _ = Functions.inverseKinematics(self.name, P, L)
        else:
            _, value1, _, value2, _, value3 = Functions.inverseKinematics(self.name, P, L)
        return value1, value2, value3
    
    def ShowChoice(self):
        if self.my_var.get() == 1 and self.changeFlag == False:
            self.A1.configure(state='disable')
            self.A2.configure(state='disable')
            self.A3.configure(state='disable')
            self.V1.configure(state='disable')
            self.V2.configure(state='disable')
            self.V3.configure(state='disable')
        elif self.my_var.get() == 2:
            self.A1.configure(state='normal')
            self.A2.configure(state='normal')
            self.A3.configure(state='normal')
            self.V1.configure(state='disable')
            self.V2.configure(state='disable')
            self.V3.configure(state='disable')
            self.changeFlag = False
        elif self.my_var.get() == 3:
            print(self.my_var.get())
            self.A1.configure(state='disable')
            self.A2.configure(state='disable')
            self.A3.configure(state='disable')
            self.V1.configure(state='normal')
            self.V2.configure(state='normal')
            self.V3.configure(state='normal')
            self.changeFlag = False
        else:
            pass
    
    def graficar(self, y1a1, y1a2, y1a3, y2a1, y2a2, y2a3, y3a1, y3a2, y3a3):
        #The figure that will contain the plot
        fig = Figure(figsize =(10,10),dpi=100)
        fig2 = Figure(figsize =(10,10),dpi=100)
        fig3 = Figure(figsize =(10,10),dpi=100)

        xlin = np.linspace(0, self.__valueBoxTf.get(), self.n)

        plot1 = fig.add_subplot(111)
        plot1.plot(xlin, y1a1, 'bo', xlin, y1a2, 'bo', xlin, y1a3, 'bo')
        plot1.set_xlabel('x')
        plot1.set_ylabel('y')

        plot2 = fig2.add_subplot(111)
        plot2.plot(xlin, y2a1, 'bo', xlin, y2a2, 'bo', xlin, y2a3, 'bo')
        plot2.set_xlabel('x')
        plot2.set_ylabel('y')

        plot3 = fig3.add_subplot(111)
        plot3.plot(xlin, y3a1, 'bo', xlin, y3a2, 'bo', xlin, y3a3, 'bo')
        plot3.set_xlabel('x')
        plot3.set_ylabel('y')

        canvas = FigureCanvasTkAgg(fig,master = self.framePlotUp)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True)

        canvas2 = FigureCanvasTkAgg(fig2,master = self.framePlotMiddle)
        canvas2.draw()
        canvas2.get_tk_widget().pack(expand=True)

        canvas3 = FigureCanvasTkAgg(fig3,master = self.framePlotDown)
        canvas3.draw()
        canvas3.get_tk_widget().pack(expand=True)