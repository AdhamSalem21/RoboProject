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


## Improvements
Our code runs perfectly and the algorithm to avoid the obstacle and reach the target works smoothly. However, we could not execute the algorithem to make the robot avoid the walls of the maze correctly. We had two approaches in mind, One is to make a list of the walls coordinates and make the robot avoid those coordinates but we got an error stating that the list is too ambigous. The second approach was to create rectangular blocks that cover the walls of the maze but we could not comprehend how to make a comparison between the vehicle coordinates and the coordinates of said blocks.

![Rectangular blocks Algorithm](Rectangles.png)



