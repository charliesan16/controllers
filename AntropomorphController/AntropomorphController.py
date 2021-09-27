"""AntropomorphController controller."""
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'App')))
#sys.path.append('Users\lfpin\Downloads\Lab1\Lab1\my_project\controllers\App')
from App import App
import json
from controller import Robot

#from controller import Robot

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

# get the time step of the current world.
#timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)


# Main loop:
# - perform simulation steps until Webots is stopping the controller
#while robot.step(timestep) != -1: 
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    #pass

# Enter here exit cleanup code.

window.mainloop()




