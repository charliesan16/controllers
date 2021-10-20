"""AntropomorphController controller."""
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'App')))
from App import App
import json
import threading

from controller import Robot
'''
# create the Robot instance.
robot = Robot()
timestep = 64

base = robot.getDevice("BaseAntrop")
artUno = robot.getDevice("artic1Antropo")
artDos = robot.getDevice("artic2Antropo")

#Features JSON
with open('..\App\Features.json') as json_file:
    data = json.load(json_file)

window = App(data['Antropomorfico'][0])

def runMethod():
    while robot.step(timestep) != -1:
        base.setPosition(window.exportSlider1(1))
        artUno.setPosition(window.exportSlider1(2))
        artDos.setPosition(window.exportSlider1(3))
        
hilo_main = threading.Thread(target=runMethod, daemon=True)
hilo_main.start()


window.mainloop()
'''