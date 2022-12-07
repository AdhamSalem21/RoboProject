from roboticstoolbox import Bicycle,RandomPath,VehicleIcon, RangeBearingSensor, LandmarkMap
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import pi,atan2
import numpy as np



intial_position = [float(input('input your vehile x-coordinate:')),float(input('input your vehile y-coordinate:'))] #user input for robot initial coordinates
goal = [float(input('input your goal x-coordinate:')),float(input('input your goal y-coordinate:'))]#user input for target coordinates
obstacles=int(input('enter the number of obstacles wanted:')) #user input for number of obstacles
show_obs_dist=str(input('would you like to see the distance and angle to obstacles? (yes or no):'))
anim = VehicleIcon('tiralrobo',scale=4)

#creating a robot icon on the grid
veh = Bicycle(
animation = anim,
dim = 20, 
control = RandomPath,
x0 = (intial_position[0], intial_position[1],0)
)
#initializing the vehicle plot
veh.init(plot = True)


#creating a target icon
goal_marker_style = {
    'marker' : 'd', 
    'markersize' : 6, 
    'color': 'b' , 
}
#plotting the target icon 
plt.plot(goal[0],goal[1],**goal_marker_style)
plt.plot()


#creating and plotting obstacles with random coordinates
map = LandmarkMap(obstacles,30)
map.plot()
#putting a map as a background
image = mpimg.imread("map.png")
plt.imshow(image, extent = [-30,30,-30,30])

#calculates distance and angle of obstacle from vehicle
sensor=RangeBearingSensor(robot=veh,map=map,animate=True)

#prints the obstacle distance and angle from vehicle based on user input
if(show_obs_dist== 'yes'):
    print('Sensor readings: \n', sensor.h(veh.x))
 
#function to avoid the obstacles
def avoid_obstacles(sensor):
  for i in sensor.h(veh.x):
     if (i[0] < 3):
      if(abs(i[1]) < pi/4):
          return False
  else:
    veh.step(2.5,0)
    veh._animation.update(veh.x)
    plt.pause(0.05)

#loop that moves the vehicle towards the target 
run=True
while(run):
  goal_heading= atan2 (goal[1]-veh.x[1],goal[0]-veh.x[0])
  steer=goal_heading-veh.x[2]
  veh.step(2,steer)
  if((abs(goal[0]-veh.x[0])>0.05) or (abs(goal[1]-veh.x[1])>0.05)):
    if (avoid_obstacles(sensor) is False):
     steer = (veh.x[2]+ pi/4 or veh.x[2]+ pi/4)
     veh.step(2.5,steer)
  else:
    run=False
  veh._animation.update(veh.x)
  plt.pause(0.005)



plt.pause(1000)