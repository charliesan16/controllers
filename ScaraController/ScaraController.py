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

with open('..\App\Features.json') as json_file:
    data = json.load(json_file)

window2 = App(data['SCARA'][0])

def runMethod2():
    while robot.step(timestep) != -1:
       pass
        
hilo_main2 = threading.Thread(target=runMethod2, daemon=True)
hilo_main2.start()

# Enter here exit cleanup code.
window2.mainloop()