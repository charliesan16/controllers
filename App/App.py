from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image

class App(Tk):
    def __init__(self, features):
        Tk.__init__(self)
        self.width = int(features['width'])
        self.height = int(features['height'])
        self.dimension = features['width']+"x"+features['height']
        self.path = features['imagePath']
        self._img = None
        self.name = features['robotName']
        self.firstSlider = 0
        self.secondSlider = 0
        self.thirdSlider = 0 
        self.Px = 0
        self.Py = 0
        self.Pz = 0
        self._art1Name = features['tituloArticulacion1']
        self._art2Name = features['tituloArticulacion2']
        self._art3Name = features['tituloArticulacion3']
        self.__frameset()
        

    def __frameset(self):
        self.geometry(self.dimension)
        self.title(self.name)
        #self.resizable(width=False, height=False)
        self.__matrixFrame()
        self.__robotFrame()
        self.__valuesFrame()

    def __matrixFrame(self):
        baseText =  "Matriz de transformación "

        frameColor = '#14213D'
        fontColor = 'white'
        frameMatrix = Frame(self, bg = frameColor)
        frameMatrix.place(x=0,rely=0.5,width=self.width, height=self.height/2)

        #Matriz Articulación 1
        labelMatriz1 = Label(frameMatrix, text=baseText + self._art1Name, bg= frameColor, fg=fontColor)
        ############################################################################
        labelsMatrix1_00 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_01 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_02 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_03 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_10 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_11 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_12 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_13 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_20 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_21 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_22 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_23 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_31 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_32 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_33 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix1_34 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        ############################################################################
        
        #Matriz Articulación 2
        labelMatriz2 = Label(frameMatrix, text=baseText + self._art2Name, bg= frameColor, fg=fontColor)
        ############################################################################
        labelsMatrix2_00 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_01 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_02 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_03 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_10 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_11 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_12 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_13 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_20 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_21 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_22 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_23 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_31 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_32 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_33 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix2_34 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        ############################################################################

        #Matriz Articulación 3
        labelMatriz3 = Label(frameMatrix, text=baseText + self._art3Name, bg= frameColor, fg=fontColor)
        ############################################################################
        labelsMatrix3_00 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_01 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_02 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_03 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_10 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_11 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_12 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_13 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_20 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_21 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_22 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_23 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_31 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_32 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_33 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix3_34 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        ############################################################################

        #Matriz Transformación Total
        labelMatriz4 = Label(frameMatrix, text=baseText + "Total", bg= frameColor, fg=fontColor)
        ############################################################################
        labelsMatrix4_00 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_01 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_02 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_03 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_10 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_11 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_12 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_13 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_20 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_21 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_22 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_23 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_31 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_32 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_33 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
        labelsMatrix4_34 = Label(frameMatrix, text='0', bg= frameColor, fg=fontColor)
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
        labelsMatrix1_31.grid(row=4,column=1)
        labelsMatrix1_32.grid(row=4,column=2)
        labelsMatrix1_33.grid(row=4,column=3)
        labelsMatrix1_34.grid(row=4,column=4)
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
        labelsMatrix2_31.grid(row=4,column=7)
        labelsMatrix2_32.grid(row=4,column=8)
        labelsMatrix2_33.grid(row=4,column=9)
        labelsMatrix2_34.grid(row=4,column=10)
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
        labelsMatrix3_31.grid(row=4,column=13)
        labelsMatrix3_32.grid(row=4,column=14)
        labelsMatrix3_33.grid(row=4,column=15)
        labelsMatrix3_34.grid(row=4,column=16)
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
        labelsMatrix4_31.grid(row=4,column=19)
        labelsMatrix4_32.grid(row=4,column=20)
        labelsMatrix4_33.grid(row=4,column=21)
        labelsMatrix4_34.grid(row=4,column=22)

        #Pesos Grilla
        for i in range(24):
            frameMatrix.columnconfigure(i, weight=1)
        
        for i in range(1,5):
            frameMatrix.rowconfigure(i, weight=1)

    def __robotFrame(self):
        frameColor = '#000000'
        paddingImg = 10
        #Frame
        frameRobot = Frame(self, bg = frameColor)
        frameRobot.place(x=0,y=0,width=self.width*0.3, height=self.height/2)
        #Imagen
        reSize = (int(self.width*0.3)-2*paddingImg,int(self.height/2)-2*paddingImg)
        self._img = ImageTk.PhotoImage(Image.open(self.path).resize(reSize,Image.ANTIALIAS))
        Label(frameRobot, image = self._img, bg=frameColor).grid(row=0,column=0, padx= paddingImg, pady= paddingImg)

    def __valuesFrame(self):
        frameColor = '#FCA311'

        #Frame Padre
        frameValues = Frame(self, bg = frameColor)
        ratioAspectX = 0.7
        frameWidth = self.width*ratioAspectX
        frameHeight = self.height/2
        frameValues.place(relx=1-ratioAspectX,y=0,width=frameWidth, height=frameHeight)
        #Frame de Sliders
        frameSliders = Frame(frameValues, bg = frameColor)
        frameSliders.place(x=0, y=0,  width=frameWidth/2, height=frameHeight)
        #Frame Inversa
        frameInverse= Frame(frameValues, bg = 'green')
        frameInverse.place(relx=0.5, y=0,  width=frameWidth/2, height=frameHeight)

        #Style tkk Sliders
        ttk.Style().configure("TScale", background=frameColor)

        #Primer Slider
        labelSlider1 = Label(frameSliders, text=self._art1Name, bg = frameColor)
        self.firstSlider = ttk.Scale(frameSliders, from_=0, to=200, orient=HORIZONTAL, style="TScale")
        
        labelValue1 = Label(frameSliders, text="Valor Actual", bg = frameColor)
        valueBox1 = Entry(frameSliders, width = 20, bg = '#CE2321')
        buttonValue1 = Button(frameSliders, text='Posicionar') 

        #Segundo Slider
        labelSlider2 = Label(frameSliders, text=self._art2Name, bg = frameColor)
        self.secondSlider = ttk.Scale(frameSliders, from_=0, to=200, orient=HORIZONTAL)

        labelValue2 = Label(frameSliders, text="Valor Actual", bg = frameColor)
        valueBox2 = Entry(frameSliders, width = 20, bg = '#CE2321')
        buttonValue2 = Button(frameSliders, text='Posicionar') 

        #Tercer Slider
        labelSlider3 = Label(frameSliders, text=self._art3Name, bg = frameColor)
        self.thirdSlider = ttk.Scale(frameSliders, from_=0, to=200, orient=HORIZONTAL)
        
        labelValue3 = Label(frameSliders, text="Valor Actual", bg = frameColor)
        valueBox3 = Entry(frameSliders, width = 20, bg = '#CE2321')
        buttonValue3 = Button(frameSliders, text='Posicionar') 
        
        #Configurar Grilla Sliders
        labelSlider1.grid(row = 0, column= 0, columnspan=3, sticky="ew")
        self.firstSlider.grid(row=1,column=0, columnspan=3, sticky="ew")
        labelValue1.grid(row=2,column=0)
        valueBox1.grid(row=2,column=1)
        buttonValue1.grid(row=2,column=2)

        labelSlider2.grid(row = 3, column= 0, columnspan=3, sticky="ew")
        self.secondSlider.grid(row=4,column=0, columnspan=3, sticky="ew")
        labelValue2.grid(row=5,column=0)
        valueBox2.grid(row=5,column=1)
        buttonValue2.grid(row=5,column=2)

        labelSlider3.grid(row = 6, column= 0, columnspan=3, sticky="ew")
        self.thirdSlider.grid(row=7,column=0, columnspan=3, sticky="ew")
        labelValue3.grid(row=8,column=0)
        valueBox3.grid(row=8,column=1)
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
        labelPx = Label(frameInverse, text="Px", bg = frameColor)
        self.Px = Entry(frameInverse, width = 20, bg = '#CE2321')
        labelPy = Label(frameInverse, text="Py", bg = frameColor)
        self.Py = Entry(frameInverse, width = 20, bg = '#CE2321')
        labelPz = Label(frameInverse, text="Pz", bg = frameColor)
        self.Pz = Entry(frameInverse, width = 20, bg = '#CE2321')
        #Boton Inversa
        buttonInverse = Button(frameInverse, text='Calcular') 
        
        #Configurar Grilla Puntos
        labelPx.grid(row=0,column=0, sticky="nsew")
        labelPy.grid(row=1,column=0, sticky="nsew")
        labelPz.grid(row=2,column=0, sticky="nsew")
        self.Px.grid(row=0,column=1)
        self.Py.grid(row=1,column=1)
        self.Pz.grid(row=2,column=1)
        buttonInverse.grid(row=0,column=2, rowspan=3, sticky="nsew")
        frameInverse.columnconfigure(0, weight=1)
        frameInverse.columnconfigure(1, weight=1)
        frameInverse.columnconfigure(2, weight=1)