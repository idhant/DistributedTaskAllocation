# Distributed Version of the Bees Algorithm. 
# Two options to make it this algorithm distributed

# Either have a temporal agent which acts as a temporary centralised allocationer 
# or have all the agents run the algorithm separately.


# NOTE: OPTION-1 Fully decentralized

# To make the algorithm fully decentralized, there will be no communication between the agents,
# The downsides of this are:
# - The robot only knows the distance between itself and the task, so a distance matrix can not be formed which is used to calculate utility probability
# - The relative quality of the task is not known, so absolute quality will be used to determine the utility
# - The allocations can not be optimized properly according to the strengths of the robots

# The algorithm will work as follows:
# - The tasks will spawn randomly in the zones and they will appear in the task queue of the robots. 

# - Instead of the task being visible to all the robots in all the zones, initially it will be visible in the zone its in. 
# - If there are robots in this zone, they will see the task. Else if there are no robots in this zone, the task will appear in other 
# - zones iteratively 

# - The robots in this zone will see a new task appear in the queue and will calculate the following
#   - The robot checks from its capability_list whether the task type is capable to be performed by it.
#   - If it is capable -> Then the robot will calculate the distance of the between the task and robot
# - The robot can then decide to allocate the task to itself.

# - NOTE: This approach considers that all the robots are doing these calculations for the task. 
# - So the current factors for deciding to allocate can lead to un-optimized allocations. 


#Modules and Classes

from Robot import Robot
from Task import Task
from Coordinate import Coordinate
import math
import random


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


def main():
    
    # Creation of the robot

    # Loop function which checks for tasks in the zone_queue

        # if tasks in the queue
        # check capability

        # if task capable
        # check distance

        # if robot not busy 
        # assign the task to itself

        # if robot busy
        # check if the task quality is atleast 9,10 and the current assigned task is less than 8 quality 



if __name__ == '__main__':
    main()
