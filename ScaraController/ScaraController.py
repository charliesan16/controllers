"""ScaraController controller."""
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'App')))
import threading
from App import App
import json

from controller import Robot

# create the Robot instance.

robot = Robot()
timestep = 64

motorScara1 = robot.getDevice("Rot1Scara")
motorScara2 = robot.getDevice("Rot2Scara")
motorScara3 = robot.getDevice("GuideScara")

with open('..\App\Features.json') as json_file:
    data = json.load(json_file)

window2 = App(data['SCARA'][0])

def runMethod2():
    while robot.step(timestep) != -1:
        motorScara1.setPosition(window2.exportSlider1(1))
        motorScara2.setPosition(window2.exportSlider1(2))
        motorScara3.setPosition(-window2.exportSlider1(3))
        
hilo_main2 = threading.Thread(target=runMethod2, daemon=True)
hilo_main2.start()

# Enter here exit cleanup code.
window2.mainloop()
