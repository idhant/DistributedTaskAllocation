# This Code file represents the scout robot partially.

#Modules and Classes
from Modules.Specific.SPT.SPTGridBasedAllocation import SPTGridBasedAllocation
from Modules.Specific.SPT.SPTRobot import SPTRobot
from Modules.Specific.SPT.SPTTask import SPTTask
from Modules.Specific.SPT.SPTCreate import SPTCreate
from Modules.Specific.SPT.SPTPrint import SPTPrint
from Modules.Base.Coordinate import Coordinate

import math
import random
import sys

# Global Vars to keep track of the robots and tasks
TASK_LIST = []
ROBOT_LIST = []

def main():

    # LOGGING RELATE GLOBAL VARS START

    # vars to control file name, location and details
    ALGORITHM = "SPT"
    EXPERIMENT = "1"
    CASE = "1"
    SET = "1"
    RUN = "1"

    # vars to control robot creation
    NUMBER_OF_ROBOTS = 2
    GROUND_ROBOTS = 1
    AERIAL_ROBOTS = 1

    # vars to control task creation
    NUMBER_OF_TASKS = 2
    GROUND_RESCUE = 1
    GROUND_FIREFIGHT = 0
    AERIAL_RESCUE = 1
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
    createVar.create_robot_sets(ROBOT_LIST, NUMBER_OF_ROBOTS, GROUND_ROBOTS, AERIAL_ROBOTS)
    #createVar.create_random_robot_sets(ROBOT_LIST, NUMBER_OF_ROBOTS)

    # Introduce tasks in the system
    createVar.create_task_sets(TASK_LIST, NUMBER_OF_TASKS, GROUND_RESCUE , GROUND_FIREFIGHT, AERIAL_RESCUE, AERIAL_FIREFIGHT, NUMBER_OF_SERVICES, GROUND_SERVICES, AERIAL_SERVICES)
    #createVar.create_random_task_sets(TASK_LIST, NUMBER_OF_TASKS, True, False, NUMBER_OF_SERVICES, True, False)

    # SCOUT ROBOT MAIN FUNCTION
    # Call the grid based allocation function
    gridVar = SPTGridBasedAllocation()

    gridVar.grid_based_allocation(TASK_LIST, ROBOT_LIST)
    
    # PRINTING INFO INTO THE LOG FILES
    printVar = SPTPrint()
    printVar.print_task_allocations(TASK_LIST)
    printVar.print_time_taken_to_allocate(TASK_LIST)
    printVar.print_robot_details(ROBOT_LIST)
    printVar.print_task_details(TASK_LIST)

    # CLOSING THE LOG FILE
    sys.stdout.close()

if __name__ == '__main__':
    main()