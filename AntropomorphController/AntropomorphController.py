"""AntropomorphController controller."""
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'App')))
from App import App
import json
from controller import Robot
import threading

from controller import Robot

# create the Robot instance.
robot = Robot()
timestep = 64

motorAntropo1 = robot.getDevice("BaseAntrop")
motorScara2 = robot.getDevice("artic1Antropo")
motorScara3 = robot.getDevice("artic2Antropo")

#Features JSON
with open('..\App\Features.json') as json_file:
    data = json.load(json_file)

window = App(data['Antropomorfico'][0])


def runMethod():
    while robot.step(timestep) != -1:
       pass
        
hilo_main = threading.Thread(target=runMethod, daemon=True)
hilo_main.start()


window.mainloop()




