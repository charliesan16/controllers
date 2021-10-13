from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import numpy as np
import Functions 
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'VelocidadGUI')))
from VelocidadGUI import VelocidadGUI
import json

class App(Tk):
    def __init__(self, features):
        Tk.__init__(self)
        #Constructor Valores Vista
        self.width = int(features['width'])
        self.height = int(features['height'])
        self.dimension = features['width']+"x"+features['height']
        self.name = features['robotName']
        self.controllerName = features['controllerName']
            #Imagen
        self.path = features['imagePath']
        self._img = None
            #Sliders
        self.firstSlider = None
        self.__minFS = features['sliderValues'][0]['min1']
        self.__maxFS = features['sliderValues'][0]['max1']
        self.secondSlider = None
        self.__minSS = features['sliderValues'][0]['min2']
        self.__maxSS = features['sliderValues'][0]['max2']
        self.thirdSlider = None
        self.__minTS = features['sliderValues'][0]['min3']
        self.__maxTS = features['sliderValues'][0]['max3']
            #Set points de boxes
        self.__valueBox1Variable = StringVar(0)
        self.__valueBox2Variable = StringVar(0)
        self.__valueBox3Variable = StringVar(0)
            #Set points valores DH
        self.theta1 = features['dHValues'][0]['theta1']
        self.theta2 = features['dHValues'][0]['theta2']
        self.theta3 = features['dHValues'][0]['theta3']
        self.a1 = features['dHValues'][0]['a1']
        self.a2 = features['dHValues'][0]['a2']
        self.a3 = features['dHValues'][0]['a3']
        self.d1 = features['dHValues'][0]['d1']
        self.d2 = features['dHValues'][0]['d2']
        self.d3 = features['dHValues'][0]['d3']
        self.alpha1 = features['dHValues'][0]['alpha1']
        self.alpha2 = features['dHValues'][0]['alpha2']
        self.alpha3 = features['dHValues'][0]['alpha3']
            #Set points inversa
        self.__l1 = features['inverseValues'][0]['l1']
        self.__l2 = features['inverseValues'][0]['l2']
        self.__l3 = features['inverseValues'][0]['l3']
            #Matrices
        self.a1Matrix = np.zeros([4,4])
        self.a2Matrix = np.zeros([4,4])
        self.a3Matrix = np.zeros([4,4])
        self.tMatrix = np.zeros([4,4])
            #Puntos
        self.__valuePx = StringVar(0)
        self.__valuePy = StringVar(0)
        self.__valuePz = StringVar(0)
        self.__valuePx.set(0)
        self.__valuePy.set(0)
        self.__valuePz.set(0)
            #Thetas cinematica inversa
        self.__theta1Inv = 0
        self.__theta2Inv = 0
        self.__theta3Inv = 0
        self._theta1InvDown = 0
        self.__theta2InvDown = 0
        self.__theta3InvDown = 0
        self.__flag = "arriba"
            #Nombres Articulaciones
        self._art1Name = features['tituloArticulacion1']
        self._art2Name = features['tituloArticulacion2']
        self._art3Name = features['tituloArticulacion3']
            #Colores
        self.__titleColor = features['titleColor']
        self.__frameColor = features['frameColor']
        self.__frameInverserColor = features['frameInverserColor']
        self.__boxColor = features['boxColor']
        self.__buttonColor = features['buttonColor']
        self.__fontColor = features['fontColor']
        self.__fontColorInverse = features['fontColorInverse']
        self.__fontColorButton = features['fontColorButton']
        self.__bottomFrameColor = features['bottomFrameColor']
        self.__bottomFontColor = features['bottomFontColor']
        self.__imageFrameColor = features['imageFrameColor']
        self.__elbowUpColor = '#23395B'
        self.__elbowDownColor = '#23395B'
        #Creación Vista
        self.__frameset()
            #Set points de sliders
        self.firstSlider.set(0)
        self.secondSlider.set(0)
        self.thirdSlider.set(0)
        

    def __frameset(self):
        self.geometry(self.dimension)
        self.title(self.name)
        self.resizable(width=False, height=False)
        self.__matrixFrame()
        self.__robotFrame()
        self.__valuesFrame()
        self.__menu()

    def __matrixFrame(self):
        baseText =  "Matriz de transformación "

        frameColor = self.__bottomFrameColor
        fontColor = self.__bottomFontColor
        frameMatrix = Frame(self, bg = frameColor)
        frameMatrix.place(x=0,rely=0.5,width=self.width, height=self.height/2)

        #Matriz Articulación 1
        labelMatriz1 = Label(frameMatrix, text=baseText + self._art1Name, bg= frameColor, fg=fontColor)
        ############################################################################
        labelsMatrix1_00 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[0,0]), bg= frameColor, fg=fontColor)
        labelsMatrix1_01 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[0,1]), bg= frameColor, fg=fontColor)
        labelsMatrix1_02 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[0,2]), bg= frameColor, fg=fontColor)
        labelsMatrix1_03 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[0,3]), bg= frameColor, fg=fontColor)
        labelsMatrix1_10 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[1,0]), bg= frameColor, fg=fontColor)
        labelsMatrix1_11 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[1,1]), bg= frameColor, fg=fontColor)
        labelsMatrix1_12 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[1,2]), bg= frameColor, fg=fontColor)
        labelsMatrix1_13 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[1,3]), bg= frameColor, fg=fontColor)
        labelsMatrix1_20 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[2,0]), bg= frameColor, fg=fontColor)
        labelsMatrix1_21 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[2,1]), bg= frameColor, fg=fontColor)
        labelsMatrix1_22 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[2,2]), bg= frameColor, fg=fontColor)
        labelsMatrix1_23 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[2,3]), bg= frameColor, fg=fontColor)
        labelsMatrix1_30 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[3,0]), bg= frameColor, fg=fontColor)
        labelsMatrix1_31 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[3,1]), bg= frameColor, fg=fontColor)
        labelsMatrix1_32 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[3,2]), bg= frameColor, fg=fontColor)
        labelsMatrix1_33 = Label(frameMatrix, text='{:.3f}'.format(self.a1Matrix[3,3]), bg= frameColor, fg=fontColor)
        ############################################################################
        
        #Matriz Articulación 2
        labelMatriz2 = Label(frameMatrix, text=baseText + self._art2Name, bg= frameColor, fg=fontColor)
        ############################################################################
        labelsMatrix2_00 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[0,0]), bg= frameColor, fg=fontColor)
        labelsMatrix2_01 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[0,1]), bg= frameColor, fg=fontColor)
        labelsMatrix2_02 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[0,2]), bg= frameColor, fg=fontColor)
        labelsMatrix2_03 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[0,3]), bg= frameColor, fg=fontColor)
        labelsMatrix2_10 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[1,0]), bg= frameColor, fg=fontColor)
        labelsMatrix2_11 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[1,1]), bg= frameColor, fg=fontColor)
        labelsMatrix2_12 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[1,2]), bg= frameColor, fg=fontColor)
        labelsMatrix2_13 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[1,3]), bg= frameColor, fg=fontColor)
        labelsMatrix2_20 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[2,0]), bg= frameColor, fg=fontColor)
        labelsMatrix2_21 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[2,1]), bg= frameColor, fg=fontColor)
        labelsMatrix2_22 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[2,2]), bg= frameColor, fg=fontColor)
        labelsMatrix2_23 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[2,3]), bg= frameColor, fg=fontColor)
        labelsMatrix2_30 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[3,0]), bg= frameColor, fg=fontColor)
        labelsMatrix2_31 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[3,1]), bg= frameColor, fg=fontColor)
        labelsMatrix2_32 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[3,2]), bg= frameColor, fg=fontColor)
        labelsMatrix2_33 = Label(frameMatrix, text='{:.3f}'.format(self.a2Matrix[3,3]), bg= frameColor, fg=fontColor)
        ############################################################################

        #Matriz Articulación 3
        labelMatriz3 = Label(frameMatrix, text=baseText + self._art3Name, bg= frameColor, fg=fontColor)
        ############################################################################
        labelsMatrix3_00 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[0,0]), bg= frameColor, fg=fontColor)
        labelsMatrix3_01 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[0,1]), bg= frameColor, fg=fontColor)
        labelsMatrix3_02 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[0,2]), bg= frameColor, fg=fontColor)
        labelsMatrix3_03 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[0,3]), bg= frameColor, fg=fontColor)
        labelsMatrix3_10 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[1,0]), bg= frameColor, fg=fontColor)
        labelsMatrix3_11 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[1,1]), bg= frameColor, fg=fontColor)
        labelsMatrix3_12 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[1,2]), bg= frameColor, fg=fontColor)
        labelsMatrix3_13 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[1,3]), bg= frameColor, fg=fontColor)
        labelsMatrix3_20 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[2,0]), bg= frameColor, fg=fontColor)
        labelsMatrix3_21 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[2,1]), bg= frameColor, fg=fontColor)
        labelsMatrix3_22 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[2,2]), bg= frameColor, fg=fontColor)
        labelsMatrix3_23 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[2,3]), bg= frameColor, fg=fontColor)
        labelsMatrix3_30 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[3,0]), bg= frameColor, fg=fontColor)
        labelsMatrix3_31 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[3,1]), bg= frameColor, fg=fontColor)
        labelsMatrix3_32 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[3,2]), bg= frameColor, fg=fontColor)
        labelsMatrix3_33 = Label(frameMatrix, text='{:.3f}'.format(self.a3Matrix[3,3]), bg= frameColor, fg=fontColor)
        ############################################################################

        #Matriz Transformación Total
        labelMatriz4 = Label(frameMatrix, text=baseText + "Total", bg= frameColor, fg=fontColor)
        ############################################################################
        labelsMatrix4_00 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[0,0]), bg= frameColor, fg=fontColor)
        labelsMatrix4_01 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[0,1]), bg= frameColor, fg=fontColor)
        labelsMatrix4_02 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[0,2]), bg= frameColor, fg=fontColor)
        labelsMatrix4_03 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[0,3]), bg= frameColor, fg=fontColor)
        labelsMatrix4_10 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[1,0]), bg= frameColor, fg=fontColor)
        labelsMatrix4_11 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[1,1]), bg= frameColor, fg=fontColor)
        labelsMatrix4_12 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[1,2]), bg= frameColor, fg=fontColor)
        labelsMatrix4_13 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[1,3]), bg= frameColor, fg=fontColor)
        labelsMatrix4_20 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[2,0]), bg= frameColor, fg=fontColor)
        labelsMatrix4_21 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[2,1]), bg= frameColor, fg=fontColor)
        labelsMatrix4_22 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[2,2]), bg= frameColor, fg=fontColor)
        labelsMatrix4_23 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[2,3]), bg= frameColor, fg=fontColor)
        labelsMatrix4_30 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[3,0]), bg= frameColor, fg=fontColor)
        labelsMatrix4_31 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[3,1]), bg= frameColor, fg=fontColor)
        labelsMatrix4_32 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[3,2]), bg= frameColor, fg=fontColor)
        labelsMatrix4_33 = Label(frameMatrix, text='{:.3f}'.format(self.tMatrix[3,3]), bg= frameColor, fg=fontColor)
        ############################################################################

        #Grilla Labels
        labelMatriz1.grid(row=0,column=0, columnspan=6, sticky="nsew")
        labelMatriz2.grid(row=0,column=6, columnspan=6, sticky="nsew")
        labelMatriz3.grid(row=0,column=12, columnspan=6, sticky="nsew")
        labelMatriz4.grid(row=0,column=18, columnspan=6, sticky="nsew")
        #Grilla M1
        labelsMatrix1_00.grid(row=1,column=1)
        labelsMatrix1_01.grid(row=1,column=2)
        labelsMatrix1_02.grid(row=1,column=3)
        labelsMatrix1_03.grid(row=1,column=4)
        labelsMatrix1_10.grid(row=2,column=1)
        labelsMatrix1_11.grid(row=2,column=2)
        labelsMatrix1_12.grid(row=2,column=3)
        labelsMatrix1_13.grid(row=2,column=4)
        labelsMatrix1_20.grid(row=3,column=1)
        labelsMatrix1_21.grid(row=3,column=2)
        labelsMatrix1_22.grid(row=3,column=3)
        labelsMatrix1_23.grid(row=3,column=4)
        labelsMatrix1_30.grid(row=4,column=1)
        labelsMatrix1_31.grid(row=4,column=2)
        labelsMatrix1_32.grid(row=4,column=3)
        labelsMatrix1_33.grid(row=4,column=4)
        #Grilla M2
        labelsMatrix2_00.grid(row=1,column=7)
        labelsMatrix2_01.grid(row=1,column=8)
        labelsMatrix2_02.grid(row=1,column=9)
        labelsMatrix2_03.grid(row=1,column=10)
        labelsMatrix2_10.grid(row=2,column=7)
        labelsMatrix2_11.grid(row=2,column=8)
        labelsMatrix2_12.grid(row=2,column=9)
        labelsMatrix2_13.grid(row=2,column=10)
        labelsMatrix2_20.grid(row=3,column=7)
        labelsMatrix2_21.grid(row=3,column=8)
        labelsMatrix2_22.grid(row=3,column=9)
        labelsMatrix2_23.grid(row=3,column=10)
        labelsMatrix2_30.grid(row=4,column=7)
        labelsMatrix2_31.grid(row=4,column=8)
        labelsMatrix2_32.grid(row=4,column=9)
        labelsMatrix2_33.grid(row=4,column=10)
        #Grilla M3
        labelsMatrix3_00.grid(row=1,column=13)
        labelsMatrix3_01.grid(row=1,column=14)
        labelsMatrix3_02.grid(row=1,column=15)
        labelsMatrix3_03.grid(row=1,column=16)
        labelsMatrix3_10.grid(row=2,column=13)
        labelsMatrix3_11.grid(row=2,column=14)
        labelsMatrix3_12.grid(row=2,column=15)
        labelsMatrix3_13.grid(row=2,column=16)
        labelsMatrix3_20.grid(row=3,column=13)
        labelsMatrix3_21.grid(row=3,column=14)
        labelsMatrix3_22.grid(row=3,column=15)
        labelsMatrix3_23.grid(row=3,column=16)
        labelsMatrix3_30.grid(row=4,column=13)
        labelsMatrix3_31.grid(row=4,column=14)
        labelsMatrix3_32.grid(row=4,column=15)
        labelsMatrix3_33.grid(row=4,column=16)
        #Grilla M4
        labelsMatrix4_00.grid(row=1,column=19)
        labelsMatrix4_01.grid(row=1,column=20)
        labelsMatrix4_02.grid(row=1,column=21)
        labelsMatrix4_03.grid(row=1,column=22)
        labelsMatrix4_10.grid(row=2,column=19)
        labelsMatrix4_11.grid(row=2,column=20)
        labelsMatrix4_12.grid(row=2,column=21)
        labelsMatrix4_13.grid(row=2,column=22)
        labelsMatrix4_20.grid(row=3,column=19)
        labelsMatrix4_21.grid(row=3,column=20)
        labelsMatrix4_22.grid(row=3,column=21)
        labelsMatrix4_23.grid(row=3,column=22)
        labelsMatrix4_30.grid(row=4,column=19)
        labelsMatrix4_31.grid(row=4,column=20)
        labelsMatrix4_32.grid(row=4,column=21)
        labelsMatrix4_33.grid(row=4,column=22)

        #Pesos Grilla
        for i in range(24):
            frameMatrix.columnconfigure(i, weight=1)
        
        for i in range(1,5):
            frameMatrix.rowconfigure(i, weight=1)

    def __robotFrame(self):
        frameColor = self.__imageFrameColor
        paddingImg = 10
        #Frame
        frameRobot = Frame(self, bg = frameColor)
        frameRobot.place(x=0,y=0,width=self.width*0.3, height=self.height/2)
        #Imagen
        reSize = (int(self.width*0.3)-2*paddingImg,int(self.height/2)-2*paddingImg)
        self._img = ImageTk.PhotoImage(Image.open(self.path).resize(reSize,Image.ANTIALIAS))
        Label(frameRobot, image = self._img, bg=frameColor).grid(row=0,column=0, padx= paddingImg, pady= paddingImg)

    def __valuesFrame(self):

        #Frame Padre
        frameValues = Frame(self, bg = self.__frameColor)
        ratioAspectX = 0.7
        frameWidth = self.width*ratioAspectX
        frameHeight = self.height/2
        frameValues.place(relx=1-ratioAspectX,y=0,width=frameWidth, height=frameHeight)
        #Frame de Sliders
        frameSliders = Frame(frameValues, bg = self.__frameColor)
        frameSliders.place(x=0, y=0,  width=frameWidth/2, height=frameHeight)
        #Frame Inversa
        frameInverse= Frame(frameValues, bg = self.__frameInverserColor)
        frameInverse.place(relx=0.5, y=0,  width=frameWidth/2, height=frameHeight)

        #Style tkk Sliders
        ttk.Style().configure("TScale", background=self.__frameColor)

        #Primer Slider
        labelSlider1 = Label(frameSliders, text=self._art1Name, bg = self.__titleColor, fg = self.__fontColor)
        self.firstSlider = ttk.Scale(frameSliders, from_=self.__minFS, to=self.__maxFS, orient=HORIZONTAL, command = self.sliderOne)
        
        labelValue1 = Label(frameSliders, text="Valor Actual", bg = self.__frameColor, fg = self.__fontColor)
        self.valueBox1 = Entry(frameSliders, textvariable=self.__valueBox1Variable, width = 20, bg = self.__boxColor)
        buttonValue1 = Button(frameSliders, text='Posicionar', bg=self.__buttonColor, fg = self.__fontColorButton, command= self.buttonCmmd1) 

        #Segundo Slider
        labelSlider2 = Label(frameSliders, text=self._art2Name, bg = self.__titleColor, fg = self.__fontColor)
        self.secondSlider = ttk.Scale(frameSliders, from_=self.__minSS, to=self.__maxSS, orient=HORIZONTAL, command = self.sliderTwo)

        labelValue2 = Label(frameSliders, text="Valor Actual", bg = self.__frameColor, fg = self.__fontColor)
        self.valueBox2 = Entry(frameSliders, textvariable=self.__valueBox2Variable,width = 20, bg = self.__boxColor)
        buttonValue2 = Button(frameSliders, text='Posicionar', bg=self.__buttonColor, fg = self.__fontColorButton, command= self.buttonCmmd2) 

        #Tercer Slider
        labelSlider3 = Label(frameSliders, text=self._art3Name, bg = self.__titleColor, fg = self.__fontColor)
        self.thirdSlider = ttk.Scale(frameSliders, from_=self.__minTS, to=self.__maxTS, orient=HORIZONTAL, command = self.sliderThree)
        
        labelValue3 = Label(frameSliders, text="Valor Actual", bg = self.__frameColor, fg = self.__fontColor)
        self.valueBox3 = Entry(frameSliders, textvariable=self.__valueBox3Variable, width = 20, bg = self.__boxColor)
        buttonValue3 = Button(frameSliders, text='Posicionar', bg=self.__buttonColor, fg = self.__fontColorButton, command= self.buttonCmmd3) 
        
        #Configurar Grilla Sliders
        labelSlider1.grid(row = 0, column= 0, columnspan=3, sticky="ew")
        self.firstSlider.grid(row=1,column=0, columnspan=3, sticky="ew")
        labelValue1.grid(row=2,column=0)
        self.valueBox1.grid(row=2,column=1)
        buttonValue1.grid(row=2,column=2)

        labelSlider2.grid(row = 3, column= 0, columnspan=3, sticky="ew")
        self.secondSlider.grid(row=4,column=0, columnspan=3, sticky="ew")
        labelValue2.grid(row=5,column=0)
        self.valueBox2.grid(row=5,column=1)
        buttonValue2.grid(row=5,column=2)

        labelSlider3.grid(row = 6, column= 0, columnspan=3, sticky="ew")
        self.thirdSlider.grid(row=7,column=0, columnspan=3, sticky="ew")
        labelValue3.grid(row=8,column=0)
        self.valueBox3.grid(row=8,column=1)
        buttonValue3.grid(row=8,column=2)
        #Pesos Grilla Sliders
        sliderWeight = 2
        frameSliders.rowconfigure(1, weight=sliderWeight)
        frameSliders.rowconfigure(4, weight=sliderWeight)
        frameSliders.rowconfigure(7, weight=sliderWeight)
        frameSliders.columnconfigure(0, weight=1)
        frameSliders.columnconfigure(1, weight=1)
        frameSliders.columnconfigure(2, weight=1)

        #Px Py Pz
        labelPx = Label(frameInverse, text="Px", bg = self.__frameInverserColor, fg = self.__fontColorInverse)
        Px = Entry(frameInverse, width = 20, bg = self.__boxColor, textvariable = self.__valuePx)
        labelPy = Label(frameInverse, text="Py", bg = self.__frameInverserColor, fg = self.__fontColorInverse)
        Py = Entry(frameInverse, width = 20, bg = self.__boxColor, textvariable = self.__valuePy)
        labelPz = Label(frameInverse, text="Pz", bg = self.__frameInverserColor, fg = self.__fontColorInverse)
        Pz = Entry(frameInverse, width = 20, bg = self.__boxColor, textvariable = self.__valuePz)
        #Boton Inversa
        buttonInverse = Button(frameInverse, text='Cinematica Diferencial', bg=self.__buttonColor, fg = self.__fontColorButton, command= self.buttonDiferential) 
        
        #Configurar Grilla Puntos
        labelPx.grid(row=0,column=0, sticky="nsew")
        labelPy.grid(row=1,column=0, sticky="nsew")
        labelPz.grid(row=2,column=0, sticky="nsew")
        Px.grid(row=0,column=1)
        Py.grid(row=1,column=1)
        Pz.grid(row=2,column=1)
        buttonInverse.grid(row=0,column=2, rowspan=3, columnspan=2, sticky="nsew")
        for i in range(4):
            frameInverse.columnconfigure(i, weight=1)

        #Codo Arriba
        labelCodoArriba = Label(frameInverse, text="Codo Arriba", bg = self.__elbowUpColor, fg = self.__fontColorInverse)
        theta1CodoArriba = Label(frameInverse, text="theta1", bg = self.__elbowUpColor, fg = self.__fontColorInverse)
        theta2CodoArriba = Label(frameInverse, text="theta2", bg = self.__elbowUpColor, fg = self.__fontColorInverse)
        theta3CodoArriba = Label(frameInverse, text="theta3", bg = self.__elbowUpColor, fg = self.__fontColorInverse)
        theta1CodoArribaResultado = Label(frameInverse, text='{:.3f}'.format(self.__theta1Inv), bg = self.__elbowUpColor, fg = self.__fontColorInverse)
        theta2CodoArribaResultado = Label(frameInverse, text='{:.3f}'.format(self.__theta2Inv), bg = self.__elbowUpColor, fg = self.__fontColorInverse)
        theta3CodoArribaResultado = Label(frameInverse, text='{:.3f}'.format(self.__theta3Inv), bg = self.__elbowUpColor, fg = self.__fontColorInverse)

        #Codo Abajo
        labelCodoAbajo = Label(frameInverse, text="Codo Aabajo", bg = self.__elbowDownColor, fg = self.__fontColorInverse)
        theta1CodoAbajo = Label(frameInverse, text="theta1", bg = self.__elbowDownColor, fg = self.__fontColorInverse)
        theta2CodoAbajo = Label(frameInverse, text="theta2", bg = self.__elbowDownColor, fg = self.__fontColorInverse)
        theta3CodoAbajo = Label(frameInverse, text="theta3", bg = self.__elbowDownColor, fg = self.__fontColorInverse)
        theta1CodoAbajoResultado = Label(frameInverse, text='{:.3f}'.format(self._theta1InvDown), bg = self.__elbowDownColor, fg = self.__fontColorInverse)
        theta2CodoAbajoResultado = Label(frameInverse, text='{:.3f}'.format(self.__theta2InvDown), bg = self.__elbowDownColor, fg = self.__fontColorInverse)
        theta3CodoAbajoResultado = Label(frameInverse, text='{:.3f}'.format(self.__theta3InvDown), bg = self.__elbowDownColor, fg = self.__fontColorInverse)

        #Grilla Resultados Inversa
        labelCodoArriba.grid(row=3, column=0, columnspan=2)
        theta1CodoArriba.grid(row=4, column=0)
        theta2CodoArriba.grid(row=5, column=0)
        theta3CodoArriba.grid(row=6, column=0)
        theta1CodoArribaResultado.grid(row=4, column=1)
        theta2CodoArribaResultado.grid(row=5, column=1)
        theta3CodoArribaResultado.grid(row=6, column=1)
        labelCodoAbajo.grid(row=3, column=2, columnspan=2)
        theta1CodoAbajo.grid(row=4, column=2)
        theta2CodoAbajo.grid(row=5, column=2)
        theta3CodoAbajo.grid(row=6, column=2)
        theta1CodoAbajoResultado.grid(row=4, column=3)
        theta2CodoAbajoResultado.grid(row=5, column=3)
        theta3CodoAbajoResultado.grid(row=6, column=3)

        for i in range(7):
            frameInverse.rowconfigure(i, weight=1)

    def __menu(self):
        newMenu = Menu(self)
        self.config(menu=newMenu)
        menuCascada = Menu(newMenu, tearoff="off")
        newMenu.add_cascade(label="Calculos", menu=menuCascada)
        menuCascada.add_command(label="Directa", command= self.matrixTransformation)
        menuCascada.add_command(label="Inversa", command= self.inverseKinematics)
        menuCascada2 = Menu(newMenu, tearoff="off")
        newMenu.add_cascade(label="Codo", menu=menuCascada2)
        menuCascada2.add_command(label="Codo Arriba", command= self.elbowUp)
        menuCascada2.add_command(label="Codo Abajo", command= self.elbowDown)

    ##############################################################################################
    ##############################################################################################
    #FUNCIONES
    ##############################################################################################
    ##############################################################################################

    def sliderOne(self, value):
        self.__valueBox1Variable.set(value)
    
    def sliderTwo(self, value):
        self.__valueBox2Variable.set(value)

    def sliderThree(self, value):
        self.__valueBox3Variable.set(value)

    def buttonCmmd1(self):
        self.firstSlider.set(float(self.__valueBox1Variable.get()))

    def buttonCmmd2(self):
        self.secondSlider.set(float(self.__valueBox2Variable.get()))
    
    def buttonCmmd3(self):
        self.thirdSlider.set(float(self.__valueBox3Variable.get()))

    def exportSlider1(self, flag):
        if flag==1:
            value = np.radians(float(self.firstSlider.get()))
        elif flag==2:
            value = np.radians(float(self.secondSlider.get()))
        else:
            value = np.radians(float(self.thirdSlider.get()))
        return value



    def matrixTransformation(self):
        self.changeDHValues()
        self.a1Matrix = Functions.matrixT(self.theta1, self.alpha1, self.a1, self.d1)
        self.a2Matrix = Functions.matrixT(self.theta2, self.alpha2, self.a2, self.d2)
        self.a3Matrix = Functions.matrixT(self.theta3, self.alpha3, self.a3, self.d3)
        self.tMatrix = Functions.totalMatrix(self.a1Matrix, self.a2Matrix, self.a3Matrix)
        self.__matrixFrame()

    def changeDHValues(self):
        if (self.name == 'Antropomorfico'):
            self.theta3 = np.radians(float(self.thirdSlider.get()))
        else:
            self.d3 = float(self.thirdSlider.get())/1000
        self.theta1 = np.radians(float(self.firstSlider.get()))
        self.theta2 = np.radians(float(self.secondSlider.get()))

    def inverseKinematics(self):
        P = np.array([self.__valuePx.get(),self.__valuePy.get(),self.__valuePz.get()]).astype(float)
        L = [self.__l1, self.__l2, self.__l3]
        self.__theta1Inv, self._theta1InvDown, self.__theta2Inv, self.__theta2InvDown, self.__theta3Inv, self.__theta3InvDown = Functions.inverseKinematics(self.name, P, L)
        self.__valuesFrame()
        if self.__flag == "arriba":
            self.firstSlider.set(self.__theta1Inv)
            self.secondSlider.set(self.__theta2Inv)
            self.thirdSlider.set(self.__theta3Inv)
        elif self.__flag == "abajo":
            self.firstSlider.set(self._theta1InvDown)
            self.secondSlider.set(self.__theta2InvDown)
            self.thirdSlider.set(self.__theta3InvDown)

    def elbowUp(self):
        self.__elbowDownColor = '#23395B'
        self.__elbowUpColor = 'green'
        self.__flag = "arriba"
        self.__valuesFrame()

    def elbowDown(self):
        self.__elbowUpColor = '#23395B'
        self.__elbowDownColor = 'green'
        self.__flag = "abajo"
        self.__valuesFrame()

    def buttonDiferential(self):
        data = {}
        if (self.name == 'Antropomorfico'):
            data['values'] = {
                'a1': 0.1475,
                'a2': 0.195,
                'theta1': np.radians(50),
                'theta2': np.radians(-70),
                'd3': 0.1  
            }
        else :
            data['values'] = {
                'a1': 0.1475,
                'a2': 0.195,
                'theta1': np.radians(50),
                'theta2': np.radians(-70),
                'd3': 0.1  
            }
        with open('mydata.json', 'w') as output:
            json.dump(data, output)
        window = VelocidadGUI(self, self.name, self.controllerName, self.__flag)
        window.grab_set()