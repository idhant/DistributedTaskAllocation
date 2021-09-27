# This Code file represents the scout robot partially.

#Modules and Classes
from Modules.Specific.DBARobot import DBARobot
from Modules.Base.Task import Task
from Modules.Base.Coordinate import Coordinate
from Modules.Base.Print import Print
from Modules.Specific.DBACreate import DBACreate

import math
import random
import sys

# Global Vars to keep track of the agents and tasks
task_list = []
robot_list = []

# Functions 

# HELPER FUNCTIONS 

# Function to check if the task queue is empty or not 
def check_task_queue(tasks):
    if len(tasks) > 0 :
        return True
    else:
        return False

# Function to check if all tasks are allocated
def check_allocation_status(tasks):
    for task in tasks:
        if task.taskAllocated == False:
            return False
    return True

# Function to return a list with the respective robot zones as the elements
def get_robot_zones():
    robot_zone_list = []

    for robot in robot_list :
        zone = robot.get_zone()
        robot_zone_list.append(zone)

    return robot_zone_list

def randomize_robot_types(number_of_robots, ground_robots, aerial_robots):
    ground_robots = random.randint(0, number_of_robots)
    aerial_robots = number_of_robots - ground_robots


# MAIN FUNCTION

# Main function which the scout robot runs 
def distributed_bees_algorithm(verbose = False):
    
    if(verbose):
        print("") 
        print("*****")
        print("DistributedBeesAlgorithm")
        print("*****")
        print("")

    if check_task_queue(task_list) :

        if (verbose):
            print("Task list is not empty, checking tasks.")

        run = 0
        #while(check_allocation_status(task_list) == False & run < len(task_list) - 1):
        while(run < len(task_list) - 1 ):    
            # Check the first task first, which was found by the scout robot first 
            # first added into the queue -> first sent to the robots 
            for task in task_list :
                
                # if task isn`t allocated
                if (task.taskAllocated == False):

                    zone = task.get_zone()

                    if (verbose):
                        print("")
                        print("-----")
                        print("Checking task: " + str(task.get_task_id()))
                        print("Task zone:  " + str(zone))
                        print("-----")
                        print("")
                        print("Checking for robots in this zone.")
                        print("")

                    # Send this task to all the robots in this zone
                    for robot in robot_list :
                        if robot.get_zone() == zone and task.taskAllocated == False :
                            if (verbose):
                                print("Robot " + str(robot.get_robot_id()) + " is in Zone: " + str(zone))
                            task_assigned = robot.DBA(task)
                            
                    if task.taskAllocated == True :
                        if (verbose):
                            print("Task: " + str(task.get_task_id()) + " is assigned to Robot: " + str(robot.get_robot_id()))
                    
                    elif task.taskAllocated == False :
                        if (verbose):
                            print("")
                            print("Could not find any robots in the same zone to the task")
                            print("Checking other robots in other zones")

                        robot_zone_list = get_robot_zones()
                        
                        i = 0
                        for robot_zone in robot_zone_list :
                            if robot_zone != zone :
                                task_assigned = robot_list[i].DBA(task)
                                if task_assigned == True :
                                    break
                            i += 1

            run += 1


    else :
        if (verbose):
            print("*****")
            print("Task list is empty, Exiting Application.")
            print("*****")


# STARTPOINT

def main():

    # vars to control file name, location and details
    ALGORITHM = "DBA"
    EXPERIMENT = "1"
    CASE = "1"
    SET = "1"
    RUN = "1"

    # vars to control robot creation
    NUMBER_OF_ROBOTS = 10
    GROUND_ROBOTS = 10
    AERIAL_ROBOTS = 0

    # vars to control task creation
    NUMBER_OF_TASKS = 10
    GROUND_RESCUE = 10
    GROUND_FIREFIGHT = 0
    AERIAL_RESCUE = 0
    AERIAL_FIREFIGHT = 0

    sys.stdout = open(f"Test/{ALGORITHM}/Experiment-{EXPERIMENT}/Case-{CASE}/Set-{SET}/Run-{RUN}.txt", "w")

    print(f"This file is for {ALGORITHM}/Experiment-{EXPERIMENT}/Case-{CASE}/Set-{SET}/Run-{RUN}")

    print(f"Experiment-{EXPERIMENT}: incrementally increasing the number of robots and tasks in the system.")
    print(f"Case-{CASE}: the type of tasks and robots are also limited to one category such as ground based. ")
    print(f"Set-{SET}: Number of agents and tasks equal to {NUMBER_OF_ROBOTS}.")
    print(f"Run-{RUN}.")

    createVar = DBACreate()

    # Simulate the creation of robots in the system 
    createVar.create_robot_sets(robot_list, NUMBER_OF_ROBOTS, GROUND_ROBOTS, AERIAL_ROBOTS)
    #create_random_robot_sets(NUMBER_OF_ROBOTS)

    # Introduce tasks in the system
    #createVar.create_task_sets(task_list, NUMBER_OF_TASKS, GROUND_RESCUE , GROUND_FIREFIGHT, AERIAL_RESCUE, AERIAL_FIREFIGHT)
    createVar.create_random_task_sets(task_list, NUMBER_OF_TASKS, True, False)

    #distributed_bees_algorithm()
    distributed_bees_algorithm()
    
    printVar = Print()
    printVar.print_task_allocations(task_list)
    printVar.print_time_taken_to_allocate(task_list)
    printVar.print_robot_details(robot_list)
    printVar.print_task_details(task_list)

    sys.stdout.close()

if __name__ == '__main__':
    main()

# NOT USED
def get_robot_distances_from_task(task):
    robot_task_distances = []
    for robot in robot_list :
        distance = robot.calculate_distance(task)
        robot_task_distances.append(distance)
    return robot_task_distances

# Function to return a  task with the highest priority
def get_highest_priority_task():

    highest_quality = task_list[0].get_task_quality()
    highest_priority = 0

    for task in task_list:
        new_quality = task.get_task_quality()
        if (new_quality > highest_quality):
            highest_quality = new_quality
            highest_priority = task.get_task_id()

    return task_list[highest_priority]
