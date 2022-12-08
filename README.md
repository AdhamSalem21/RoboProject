# RoboProject Documentation
Contributors: Adham Saad, Youssef El Shershaby, Mohamed Gadallah
## Introduction
The aim of this project is to provide autonomous navigation for a robot to reach it's target, while avoiding obstacle and the walls of the map. The python version used was python 3.6

## Libraries Imported
- roboticstoolbox
- matplotlib.pyplot
- matplotlib.image
- math
- numpy


## User Inputs
- Coordinates of the robot.
- Coordinates of the target.
- Number of obstacles.
- Decision to show distance and angle to target

## Output
The terminal output that the user views, asks for the user to input the vehicle intial position, the target coordinates, the number of obstacles desired and whether he would like to view the sensor readings(distance and angle from the vehicle to each obstacle) or not.
![Terminal output](Terminaloutput.png)

The output after the user inputs shows the robot icon at the coordinates chosen.
![Initial position](Start.png)

The end result is as expected where the robot icon reaches the target while avoiding all obstacles.
![End result](End.png)

## Methodology
The movement code is desired to satisfy two main task:
### Movement to target
To achieve this we make use of the atan2 function from the math library named goal_heading in our code, which helps with calculating the angle of target from the robot. To reach the target we umake use of goal heading by moving the robot using veh.step which is a function in the robotics toolbox which needs two arguments the speed and an angle. The angle in the step is uses the goal_heading which makes the robot move towards the target with a steady speed and with an angle that ensures it reaching the target. Once it reaches the target, the robot stops. 
### Avoid obstacles

![Navigation code](Body code.png)

## Improvements
Our code runs perfectly and the algorithm to avoid the obstacle and reach the target works smoothly. However, we could not execute the algorithem to make the robot avoid the walls of the maze correctly. We had two approaches in mind, One is to make a list of the walls coordinates and make the robot avoid those coordinates but we got an error stating that the list is too ambigous. The second approach was to create rectangular blocks that cover the walls of the maze but we could not comprehend how to make a comparison between the vehicle coordinates and the coordinates of said blocks.

![Rectangular blocks Algorithm](Rectangles.png)

## Contribution towards the code
Unfortunately we all had a problem with commiting the changes in the code from ubuntu. Therefore, we uploaded our file after it was finished on github.

We created a list of contributions as we have been told by Doctor Khaled Geneidy.

- Mohammed Adel: worked on initialising the vehicle icon, the target icon, user inputs and the sesnor reading algorithm.
- Adham Saad: Worked on reaching the target algorithm and avoiding obstacles.
- Yousef Mamdouh: Worked on reaching the target algorithm and avoiding obstacles.



