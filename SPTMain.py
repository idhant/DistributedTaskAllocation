# This Code file represents the scout robot partially.

#Modules and Classes
from Modules.Specific.SPT.SPTRobot import SPTRobot
from Modules.Specific.SPT.SPTTask import SPTTask
from Modules.Specific.SPT.SPTCreate import SPTCreate
from Modules.Specific.SPT.SPTPrint import SPTPrint
from Modules.Base.Coordinate import Coordinate

import math
import random
import sys

task_list = []
robot_list = []

# HELPER Functions

# Function to check if the task queue is empty or not 
def check_task_queue(tasks):
    if len(tasks) > 0 :
        return True
    else:
        return False

# Function to return a list with the respective robot zones as the elements
def get_robot_zones():
    robot_zone_list = []

    for robot in robot_list :
        zone = robot.get_zone()
        robot_zone_list.append(zone)

    return robot_zone_list

# Main function

def grid_based_allocation(verbose=False):

    if(verbose):
        print("") 
        print("*****")
        print("SPlusT Algorithm")
        print("*****")
        print("")

    # if task list is not empty
    if check_task_queue(task_list) :

        if (verbose):
            print("Task list is not empty, checking tasks.")

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

                # Send this task to all the robots in this zone and keep track of the bids in case of services
                for robot in robot_list :
                    if robot.get_zone() == zone and task.taskAllocated == False :
                        if (verbose):
                            print("Robot " + str(robot.get_robot_id()) + " is in Zone: " + str(zone))
                        
                        task_assigned = robot.SPT(task)
                        
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
                            task_assigned = robot_list[i].SPT(task)
                            if task_assigned == True :
                                break
                        i += 1

    else :
        if (verbose):
            print("*****")
            print("Task list is empty, Exiting Application.")
            print("*****")


def main():

    # LOGGING RELATE GLOBAL VARS START

    # vars to control file name, location and details
    ALGORITHM = "SPT"
    EXPERIMENT = "1"
    CASE = "1"
    SET = "1"
    RUN = "1"

    # vars to control robot creation
    NUMBER_OF_ROBOTS = 5
    GROUND_ROBOTS = 5
    AERIAL_ROBOTS = 0

    # vars to control task creation
    NUMBER_OF_TASKS = 5
    GROUND_RESCUE = 5
    GROUND_FIREFIGHT = 0
    AERIAL_RESCUE = 0
    AERIAL_FIREFIGHT = 0
    
    NUMBER_OF_SERVICES = 1
    GROUND_SERVICES = 1
    AERIAL_SERVICES = 0

    # LOGGING RELATE GLOBAL VARS END

    # STARTING THE LOG FILE
    sys.stdout = open(f"Test/{ALGORITHM}/Experiment-{EXPERIMENT}/Case-{CASE}/Set-{SET}/Run-{RUN}.txt", "w")

    print(f"This file is for {ALGORITHM}/Experiment-{EXPERIMENT}/Case-{CASE}/Set-{SET}/Run-{RUN}")

    print(f"Experiment-{EXPERIMENT}: incrementally increasing the number of robots and tasks in the system.")
    print(f"Case-{CASE}: the type of tasks and robots are also limited to one category such as ground based. ")
    print(f"Set-{SET}: Number of agents and tasks equal to {NUMBER_OF_ROBOTS}.")
    print(f"Run-{RUN}.")

    # CREATING TASKS AND ROBOTS IN THE SYSTEM
    createVar = SPTCreate()

    # Simulate the creation of robots in the system 
    createVar.create_robot_sets(robot_list, NUMBER_OF_ROBOTS, GROUND_ROBOTS, AERIAL_ROBOTS)
    #create_random_robot_sets(NUMBER_OF_ROBOTS)

    # Introduce tasks in the system
    #createVar.create_task_sets(task_list, NUMBER_OF_TASKS, GROUND_RESCUE , GROUND_FIREFIGHT, AERIAL_RESCUE, AERIAL_FIREFIGHT, NUMBER_OF_SERVICES, GROUND_SERVICES, AERIAL_SERVICES)
    createVar.create_random_task_sets(task_list, NUMBER_OF_TASKS, True, False, NUMBER_OF_SERVICES, True, False)

    # SCOUT ROBOT MAIN FUNCTION
    # Call the grid based allocation function
    grid_based_allocation()
    
    # PRINTING INFO INTO THE LOG FILES
    printVar = SPTPrint()
    printVar.print_task_allocations(task_list)
    printVar.print_time_taken_to_allocate(task_list)
    printVar.print_robot_details(robot_list)
    printVar.print_task_details(task_list)

    # CLOSING THE LOG FILE
    sys.stdout.close()

if __name__ == '__main__':
    main()