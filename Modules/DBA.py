#Modules and Classes

from Robot import Robot
from Task import Task
from Coordinate import Coordinate
import math

# function to check if the robot is capable to do this task 
def calculate_capability(capability_list, task):
    for capable_task in capability_list:
        if(capable_task == task.get_task_type()):
            return True

# function to calculate the 3D distance of the robot to the task
def calculate_distance(robot_coordinates, task_coordinates):
    x_axis_distance = robot_coordinates.get_x_coordinate() - task_coordinates.get_x_coordinate()
    x_axis_distance = pow(x_axis_distance, 2)
    y_axis_distance = robot_coordinates.get_y_coordinate() - task_coordinates.get_y_coordinate()
    y_axis_distance = pow(y_axis_distance, 2)
    z_axis_distance = robot_coordinates.get_z_coordinate() - task_coordinates.get_z_coordinate()
    z_axis_distance = pow(z_axis_distance, 2)
    distance = math.sqrt(x_axis_distance + y_axis_distance + z_axis_distance)
    return distance

# function to calculate the visibility of the robot to the task
def calculate_visibility(distance):
    visibility = 1/distance
    return visibility