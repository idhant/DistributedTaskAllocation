# This Code file represents the scout robot partially.

#Modules and Classes
from Modules.Specific.DBARobot import DBARobot
from Modules.Base.Task import Task
from Modules.Base.Coordinate import Coordinate

import math
import random
import sys

# Global Vars to keep track of the agents and tasks
task_list = []
robot_list = []

# Functions 

# CREATION FUNCTIONS 

# Modified function to create robots
def create_robot_sets(number_of_robots, ground_robots, aerial_robots, verbose = False):
    
    if(number_of_robots == ground_robots + aerial_robots):

        if(verbose):
            print("")
            print("*****")
            print("Starting create_robots function")
            print("*****")
            print("")

            print("*****")
            print("Number of Robots to Create: " + str(number_of_robots))
            print("Number of Ground Robots to Create:" + str(ground_robots))
            print("Number of Aerial Robots to Create:" + str(aerial_robots))
            print("*****")

        TYPE_GROUND = "ground_robot"
        TYPE_AERIAL = "aerial_robot"

        TASK_LIST_GROUND = ["ground_fire_extinguish", "ground_rescue"]
        TASK_LIST_AERIAL = ["aerial_fire_extinguish", "aerial_rescue"] 

        global robot_list

        robot_id = 0

        for robot in range(ground_robots):
            random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
            robot_list.append(DBARobot(robot_id, TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
            robot_id += 1

        for robot in range(aerial_robots):
            random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
            robot_list.append(DBARobot(robot_id, TYPE_AERIAL, random_coordinates, TASK_LIST_AERIAL))
            robot_id += 1

        if(verbose):
            print("Created " + str(number_of_robots) + " robots.")
            print("")
            for robot in robot_list:
                print("*****")
                print("Robot ID: " + str(robot.get_robot_id())) 
                print("Robot Type: " + robot.get_robot_type()) 
                print("Robot Location: ")
                print("X: " + str(robot.get_robot_location().get_x_coordinate()))
                print("Y: " + str(robot.get_robot_location().get_y_coordinate()))
                print("Z: " + str(robot.get_robot_location().get_z_coordinate()))
                print("Robot Task Capabilities: ")
                for capability in robot.get_is_capable():
                    print(capability)
                print("*****")
                print("")
            print("*****")
            print("Ending create_robots function")
            print("*****")
            print("")

    else:
        print("Number of robots do not add up, please verify.")

def create_random_robot_sets(number_of_robots, verbose = False):
    ground_robots = random.randint(0, number_of_robots)
    aerial_robots = number_of_robots - ground_robots

    if(verbose):
        print("")
        print("*****")
        print("Starting create_robots function")
        print("*****")
        print("")

        print("*****")
        print("Number of Robots to Create: " + str(number_of_robots))
        print("Number of Ground Robots to Create:" + str(ground_robots))
        print("Number of Aerial Robots to Create:" + str(aerial_robots))
        print("*****")

    TYPE_GROUND = "ground_robot"
    TYPE_AERIAL = "aerial_robot"

    TASK_LIST_GROUND = ["ground_fire_extinguish", "ground_rescue"]
    TASK_LIST_AERIAL = ["aerial_fire_extinguish", "aerial_rescue"] 

    global robot_list

    robot_id = 0

    for robot in range(ground_robots):
        random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
        robot_list.append(DBARobot(robot_id, TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        robot_id += 1

    for robot in range(aerial_robots):
        random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
        robot_list.append(DBARobot(robot_id, TYPE_AERIAL, random_coordinates, TASK_LIST_AERIAL))
        robot_id += 1

    if(verbose):
        print("Created " + str(number_of_robots) + " robots.")
        print("")
        for robot in robot_list:
            print("*****")
            print("Robot ID: " + str(robot.get_robot_id())) 
            print("Robot Type: " + robot.get_robot_type()) 
            print("Robot Location: ")
            print("X: " + str(robot.get_robot_location().get_x_coordinate()))
            print("Y: " + str(robot.get_robot_location().get_y_coordinate()))
            print("Z: " + str(robot.get_robot_location().get_z_coordinate()))
            print("Robot Task Capabilities: ")
            for capability in robot.get_is_capable():
                print(capability)
            print("*****")
            print("")
        print("*****")
        print("Ending create_robots function")
        print("*****")
        print("")

# Modified function to create tasks for
def create_task_sets(number_of_tasks, ground_rescue, ground_firefight, aerial_rescue, aerial_firefight, verbose = False):

    if(number_of_tasks == ground_rescue + ground_firefight + aerial_rescue + aerial_firefight):
        if(verbose):
            print("")
            print("*****")
            print("Starting create_tasks function")
            print("*****")
            print("")

            print("*****")
            print("Number of Tasks to Create: " + str(number_of_tasks))
            print("Number of Ground Rescue Tasks to Create:" + str(ground_rescue))
            print("Number of Ground Firefight Tasks to Create:" + str(ground_firefight))
            print("Number of Aerial Rescue Tasks to Create:" + str(aerial_rescue))
            print("Number of Aerial Firefight Tasks to Create:" + str(aerial_firefight))
            print("*****")

        # Task names
        TASK_AERIAL_FIREFIGHT = "aerial_fire_extinguish"
        TASK_GROUND_FIREFIGHT = "ground_fire_extinguish"
        TASK_AERIAL_RESCUE = "aerial_rescue"
        TASK_GROUND_RESCUE = "ground_rescue"

        # Base qualities
        QUALITY_AERIAL_FIREFIGHT = 6
        QUALITY_GROUND_FIREFIGHT = 4
        QUALITY_AERIAL_RESCUE = 10
        QUALITY_GROUND_RESCUE = 8

        global task_list

        task_id = 0

        for task in range(ground_rescue):
            random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
            zone = random_coordinates.get_zone()
            new_quality = zone_quality_assigner(zone, QUALITY_GROUND_RESCUE)
            task_list.append(Task(task_id, new_quality, random_coordinates, TASK_GROUND_RESCUE))
            task_id += 1

        for task in range(ground_firefight):
            random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
            zone = random_coordinates.get_zone()
            new_quality = zone_quality_assigner(zone, QUALITY_GROUND_FIREFIGHT)
            task_list.append(Task(task_id, new_quality, random_coordinates, TASK_GROUND_FIREFIGHT))
            task_id += 1

        for task in range(aerial_rescue):
            random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
            zone = random_coordinates.get_zone()
            new_quality = zone_quality_assigner(zone, QUALITY_AERIAL_RESCUE)
            task_list.append(Task(task_id, new_quality, random_coordinates, TASK_AERIAL_RESCUE))
            task_id += 1

        for task in range(aerial_firefight):
            random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
            zone = random_coordinates.get_zone()
            new_quality = zone_quality_assigner(zone, QUALITY_AERIAL_FIREFIGHT)
            task_list.append(Task(task_id, new_quality, random_coordinates, TASK_AERIAL_FIREFIGHT))
            task_id += 1


        if(verbose):
            print("Created " + str(number_of_tasks) + " tasks.")
            print("")
            for task in task_list:
                print("*****")
                print("Task ID: " + str(task.get_task_id()))
                print("Task Type: " + task.get_task_type())
                print("Task Quality: "+ str(task.get_task_quality()))
                print("Task Location: ")
                print("X: " + str(task.get_task_location().get_x_coordinate()))
                print("Y: " + str(task.get_task_location().get_y_coordinate()))
                print("z: " + str(task.get_task_location().get_z_coordinate()))
                print("Task Zone: " + str(task.get_zone()))
                #print(task.get_time_added())
                print("*****")
                print("")
            print("*****")
            print("Ending create_tasks function")
            print("*****")
            print("")

    else:
        print("Number of tasks do not add up, please verify.")

def create_random_task_sets(number_of_tasks, ground_types, aerial_types, verbose = False):

    if (ground_types == True and aerial_types == True):
        ground_tasks = random.randint(0, number_of_tasks)
        aerial_tasks = number_of_tasks - ground_tasks

        ground_rescue = random.randint(0, ground_tasks)
        ground_firefight = ground_tasks - ground_rescue

        aerial_rescue = random.randint(0, aerial_tasks)
        aerial_firefight = aerial_tasks - aerial_rescue

        create_task_sets(number_of_tasks, ground_rescue, ground_firefight, aerial_rescue, aerial_firefight, verbose)
        return

    if (ground_types == True and aerial_types == False):
        ground_tasks = number_of_tasks

        ground_rescue = random.randint(0, ground_tasks)
        ground_firefight = ground_tasks - ground_rescue

        aerial_rescue = 0
        aerial_firefight = 0

        create_task_sets(number_of_tasks, ground_rescue, ground_firefight, aerial_rescue, aerial_firefight, verbose)
        return

    if ground_types == False and aerial_types == True:
        aerial_tasks = number_of_tasks
        aerial_rescue = random.randint(0, aerial_tasks)
        aerial_firefight = aerial_tasks - aerial_rescue
        ground_rescue = 0
        ground_firefight = 0

        create_task_sets(number_of_tasks, ground_rescue, ground_firefight, aerial_rescue, aerial_firefight, verbose)
        return

    else:
        print("No condition matched.")
        return

# Function to calculate adjusted quality value based on the zone multiplier
def zone_quality_assigner(zone, base_quality):
    # Zone multipliers
    ZONE_ONE_X = 3
    ZONE_TWO_X = 1.5
    ZONE_THREE_X = 1
    ZONE_FOUR_X = 0.75

    if(zone == 1):
        new_quality = base_quality * ZONE_ONE_X
        return new_quality
    
    if(zone == 2):
        new_quality = base_quality * ZONE_TWO_X
        return new_quality

    if(zone == 3):
        new_quality = base_quality * ZONE_THREE_X
        return new_quality

    if(zone == 4):
        new_quality = base_quality * ZONE_FOUR_X
        return new_quality

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

# MAin function which the scout robot runs 
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

# PRINTING FUNCTIONS

# Function to print all the robot details in the system
def print_robot_details():
    print("")
    print("*****")
    print("Robot Details in the system:")
    print("*****")
    print("")
    for robot in robot_list:
        print("*****")
        print("Robot ID: " + str(robot.get_robot_id())) 
        print("Robot Type: " + robot.get_robot_type()) 
        print("Robot Location: ")
        print("X: " + str(robot.get_robot_location().get_x_coordinate()))
        print("Y: " + str(robot.get_robot_location().get_y_coordinate()))
        print("Z: " + str(robot.get_robot_location().get_z_coordinate()))
        print("Robot Zone: " + str(robot.get_zone()))
        print("Robot Task Capabilities: ")
        for capability in robot.get_is_capable():
            print(capability)
        print("Robot Status: " + str(robot.get_robot_status()))
        if(robot.get_assigned_task() != -1):
            print("Robot allocated task: " + str(robot.get_assigned_task().get_task_id()))
        if(robot.get_assigned_task() == -1):
            print("Robot is not allocated any task.")
        print("*****")
        print("")

# Function to print all the task details in the system
def print_task_details():
    print("")
    print("*****")
    print("Task Details in the system:")
    print("*****")
    print("")
    for task in task_list:
        print("*****")
        print("Task ID: " + str(task.get_task_id()))
        print("Task Type: " + task.get_task_type())
        print("Task Quality: "+ str(task.get_task_quality()))
        print("Task Location: ")
        print("X: " + str(task.get_task_location().get_x_coordinate()))
        print("Y: " + str(task.get_task_location().get_y_coordinate()))
        print("z: " + str(task.get_task_location().get_z_coordinate()))
        print("Task Zone: " + str(task.get_zone()))
        print("Task Time Added: " + str(round(task.get_time_added(), 4)) )
        print("Task Allocated: " + str(task.taskAllocated))
        if(task.taskAllocated):
            print("Robot Allocated to this task: " + str(task.robotAllocated.get_robot_id()))
            print("Time Allocated: " + str(round(task.timeAllocated, 4)) )
            print('Time Taken to allocate: ' + str(round(task.get_time_taken_to_allocate(), 4)) )
            print("Times Reallocated: " + str(task.timesReallocated))
            print("Time Consumed in reallocations: " + str(round(task.timeDeallocated, 4)) )
        print()
        print("*****")
        print("")

# Function to print allocations
def print_task_allocations():
    print("")
    print("*****")
    print("Task Allocations")
    print("*****")
    print("")
    for task in task_list:
        if(task.get_robot_id() != -1):
            print("Task: " + str(task.get_task_id()) + " is assigned to robot " + str(task.get_robot_id()))
        else:
            print("Task: " + str(task.get_task_id()) + " could not be assigned to any robot in the first run.")

# function to print the global and local runtime of the algorithm
def print_time_taken_to_allocate():
    print("")
    print("*****")
    print("Time taken to allocate tasks:")
    print("*****")
    print("")

    print("Time taken to allocate for particular tasks:")
    print("")
    total_time = 0
    time_wasted = 0
    reallocations_performed = 0
    for task in task_list:
        
        # Task Allocated
        if task.taskAllocated :

            if task.timesReallocated > 0 :
                reallocations_performed += 1
                print("Task " + str(task.get_task_id()) + " was deallocated " + str(task.timesReallocated) + " times")
                print("Time wasted on deallocation " + str(round(task.get_time_wasted_on_dealloaction(), 4)) + " seconds")
                print("Time taken to allocate task-" + str(task.get_task_id())  + " was " + str(round(task.get_time_taken_to_allocate(), 4)) + " seconds")
                total_time += task.get_time_taken_to_allocate()
                time_wasted += task.get_time_wasted_on_dealloaction()

            else:
                print("Time taken to allocate task-" + str(task.get_task_id())  + " was " + str(round(task.get_time_taken_to_allocate(), 4)) + " seconds")
                total_time += task.get_time_taken_to_allocate()

        # Task not allocated
        else:
            if task.timesReallocated > 0 :
                reallocations_performed += 1
                print("Task was allocated but deallocated later")
                print("Task " + str(task.get_task_id()) + " was deallocated " + str(task.timesReallocated) + " times")
                print("Time wasted on deallocation " + str(task.get_time_wasted_on_dealloaction()))
                total_time += task.get_time_wasted_on_dealloaction()
                time_wasted += task.get_time_wasted_on_dealloaction()
            else:
                print("Task was never allocated")

    
    print("")
    print("Total time taken to allocate all the tasks was " + str(round(total_time, 4)) + " seconds.")
    print("")
    print("Reallocations were performed " + str(reallocations_performed) + " times in total.")
    print("")
    print("Time consumed in reallocation of the the tasks was " + str(round(time_wasted, 4)) + " seconds.")
    print("")

# STARTPOINT

def main():

    # vars to control file name, location and details
    ALGORITHM = "DBA"
    EXPERIMENT = "1"
    CASE = "1"
    SET = "6"
    RUN = "10"

    # vars to control robot creation
    NUMBER_OF_ROBOTS = 1000
    GROUND_ROBOTS = 1000
    AERIAL_ROBOTS = 0

    # vars to control task creation
    NUMBER_OF_TASKS = 1000
    GROUND_RESCUE = 0
    GROUND_FIREFIGHT = 0
    AERIAL_RESCUE = 0
    AERIAL_FIREFIGHT = 0

    sys.stdout = open(f"Test/{ALGORITHM}/Experiment-{EXPERIMENT}/Case-{CASE}/Set-{SET}/Run-{RUN}.txt", "w")

    print(f"This file is for {ALGORITHM}/Experiment-{EXPERIMENT}/Case-{CASE}/Set-{SET}/Run-{RUN}")

    print(f"Experiment-{EXPERIMENT}: incrementally increasing the number of robots and tasks in the system.")
    print(f"Case-{CASE}: the type of tasks and robots are also limited to one category such as ground based. ")
    print(f"Set-{SET}: Number of agents and tasks equal to {NUMBER_OF_ROBOTS}.")
    print(f"Run-{RUN}.")


    # Simulate the creation of robots in the system 
    create_robot_sets(NUMBER_OF_ROBOTS, GROUND_ROBOTS, AERIAL_ROBOTS)
    #create_random_robot_sets(NUMBER_OF_ROBOTS)

    # Introduce tasks in the system
    #create_task_sets(NUMBER_OF_TASKS, GROUND_RESCUE , GROUND_FIREFIGHT, AERIAL_RESCUE, AERIAL_FIREFIGHT)
    create_random_task_sets(NUMBER_OF_TASKS, True, False)

    #distributed_bees_algorithm()
    distributed_bees_algorithm()
    
    print_task_allocations()

    print_time_taken_to_allocate()

    print_robot_details()

    print_task_details()

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
