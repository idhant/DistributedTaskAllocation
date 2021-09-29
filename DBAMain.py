# This Code file represents the scout robot basically.
# The main function being run here is distributed_bees_algorithm, which tries to 
# emulate how a real scout robot would act when it has tasks in the queue  
# The grid based allocation process is simulated by this function

#Modules and Classes
from Modules.Specific.DBA.DBAGridBasedAllocation import DBAGridBasedAllocation
from Modules.Specific.DBA.DBARobot import DBARobot
from Modules.Base.Task import Task
from Modules.Specific.DBA.DBACreate import DBACreate
from Modules.Base.Print import Print
from Modules.Base.Coordinate import Coordinate

import math
import random
import sys

# Global Vars to keep track of the robots and tasks
TASK_LIST = []
ROBOT_LIST = []

# MAIN STARTPOINT

def main():

    # LOGGING RELATE GLOBAL VARS START

    # vars to control file name, location and details
    ALGORITHM = "DBA"
    EXPERIMENT = "2"
    CASE = "1"
    SET = "5"
    RUN = "10"

    # vars to control robot creation
    NUMBER_OF_ROBOTS = 200
    GROUND_ROBOTS = 0
    AERIAL_ROBOTS = 0

    # vars to control task creation
    NUMBER_OF_TASKS = 200
    GROUND_RESCUE = 0
    GROUND_FIREFIGHT = 0
    AERIAL_RESCUE = 0
    AERIAL_FIREFIGHT = 0

    # LOGGING RELATE GLOBAL VARS END

    # STARTING THE LOG FILE
    sys.stdout = open(f"Test/{ALGORITHM}/Experiment-{EXPERIMENT}/Case-{CASE}/Set-{SET}/Run-{RUN}.txt", "w")

    print(f"This file is for {ALGORITHM}/Experiment-{EXPERIMENT}/Case-{CASE}/Set-{SET}/Run-{RUN}")

    print(f"Experiment-{EXPERIMENT}: Scalability Testing")
    print(f"Case-{CASE}:  ")
    print(f"Set-{SET}: Number of agents and tasks equal to {NUMBER_OF_ROBOTS}.")
    print(f"Run-{RUN}.")

    # CREATING TASKS AND ROBOTS IN THE SYSTEM
    createVar = DBACreate()

    # Simulate the creation of robots in the system 
    #createVar.create_robot_sets(ROBOT_LIST, NUMBER_OF_ROBOTS, GROUND_ROBOTS, AERIAL_ROBOTS)
    createVar.create_random_robot_sets(ROBOT_LIST, NUMBER_OF_ROBOTS, True, True)

    # Introduce tasks in the system
    #createVar.create_task_sets(TASK_LIST, NUMBER_OF_TASKS, GROUND_RESCUE , GROUND_FIREFIGHT, AERIAL_RESCUE, AERIAL_FIREFIGHT)
    createVar.create_random_task_sets(TASK_LIST, NUMBER_OF_TASKS, True, True)

    # SCOUT ROBOT MAIN FUNCTION
    # Call the grid based allocation function
    gridVar = DBAGridBasedAllocation()

    gridVar.grid_based_allocation(TASK_LIST, ROBOT_LIST)
    
    # PRINTING INFO INTO THE LOG FILES
    printVar = Print()
    printVar.print_task_allocations(TASK_LIST)
    printVar.print_time_taken_to_allocate(TASK_LIST)
    printVar.print_robot_details(ROBOT_LIST)
    printVar.print_task_details(TASK_LIST)

    # CLOSING THE LOG FILE
    sys.stdout.close()

if __name__ == '__main__':
    main()
