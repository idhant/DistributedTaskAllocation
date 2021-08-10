# Distributed Version of the Bees Algorithm. 

# NOTE: It is possible to make the algorithms decentralized to a good extent, but still in the code to show the results, visualise 
# there will be a need to store some common parameters, variables. 
# For example, 
# - initial declaration of the robots in the system
# - Implementing loop checking for all the robots to see their respective zone task queue
# - a task queue creater, handler of sorts which will simulate "scout bees" which find these tasks and put them in the queue,
# as how tasks are found is not in the scope of this research, we will chose to ignore that part.


# Two options to make this algorithm distributed are as follows:

# OPTION-1 All the agents in the system run a version of the algorithm independent of other agents. Meaning they all need
# to have some processing power always reserved for task allocation. This also means very minimal communication between agents which 
# can cause unoptimized results. 

# To avoid the scenario of all the robots in the system checking for the new tasks in the queue, i propose a zone/grid based visibility
# approach. In this approach, the task is initially only visible to the robots that are in the same zone/grid. 

# - IF the robots in this zone are capable to do the task, are not busy, not performing a higher quality task then they can decide to
# allocate themselves to this task. (BEST CASE SCENARIO)

# - ELSE, the task then iteratively becomes available in the nearby grids one-by-one until a suitable robot is found. 

# OPTION-2 A temporal agent is present in zones where the number of robots are high. This agent serves as a mini
# version of the centralised algorithm for a small group of robots. A version of the algorithm runs on this agent.

# This approach can reduce the amount of processing power needed to run the algorithm on all the agents 
# but has the downside of communication costs. 


# NOTE: OPTION-1 Fully decentralized

# To make the algorithm fully decentralized, there will be no communication between the agents,

# The keypoints of this are:
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


# NOTE: OPTION-2 Partial decentralized

# In this approach one of the robots in the zones acts as a temporal agent, so some communication is necessary.

# The keypoints of this are:
# - Instead of the tasks being received by all the robots in the zone, they are received by the temporary agent 
# - This temporary agent needs to know some values such as the capabilities, distances, status of the robots in its team. 
# - The allocations can be optimized to an certain extent
# - Any robot is capable of being this temporary agent and the team of robots is dynamic, i.e, if a task is assigned to a robot 
# in the team, it will leave the team and pursue that task

# The algorithm will work similar to the fully decentralized version and the centralized version in a way. It will
# act as a centralized mini version for a small group of robots in the zone. 

# NOTE: This approach is only useful if the number of robots are particularly high in the zone. 


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


def check_task_queue(task_queue):

    # Loop function which checks for tasks in the zone_queue
    while True:
        if (task_queue.length > 0):

            # Check for the highest quality task first
            highest_quality_task = task_queue[0]

            for task in task_queue:
                if (task.get_task_quality() > highest_quality_task.get_task_quality()):
                    highest_quality_task = task


            capable = calculate_capability()

        # if tasks in the queue
        # check capability

        # if task capable
        # check distance

        # if robot not busy 
        # assign the task to itself

        # if robot busy
        # check if the task quality is atleast 9,10 and the current assigned task is less than 8 quality 

