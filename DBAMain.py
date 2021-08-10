#Modules and Classes

from Modules.DBARobot import DBARobot
from Modules.Task import Task
from Modules.Coordinate import Coordinate
import math
import random

task_list = []
robot_list = []

# Function to create different sets of robots
def create_robots(set):
    print("")
    print("*****")
    print("Starting create_robots function")
    print("*****")
    print("")

    SET_ONE_ID = [1,2,3,4,5]
    SET_TWO_ID = [1,2,3,4,5,6,7,8,9,10]
    SET_THREE_ID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    TYPE_GROUND = "ground_robot"
    TYPE_AERIAL = "aerial_robot"

    TASK_LIST_GROUND = ["ground_fire_extinguish", "ground_rescue"]
    TASK_LIST_AERIAL = ["aerial_fire_extinguish", "aerial_rescue"] 

    BASE_LOCATION_X = 100
    BASE_LOCATION_Y = 100
    BASE_LOCATION_Z = 0

    BASE_COORDINATES = Coordinate(BASE_LOCATION_X, BASE_LOCATION_Y, BASE_LOCATION_Z)

    global robot_list

    # set-1, 1 aerial robot, 4 ground robots
    if(set == 1):
        robot_list.append(DBARobot(SET_ONE_ID[0], TYPE_AERIAL, BASE_COORDINATES, TASK_LIST_AERIAL))
        robot_list.append(DBARobot(SET_ONE_ID[1], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(DBARobot(SET_ONE_ID[2], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(DBARobot(SET_ONE_ID[3], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(DBARobot(SET_ONE_ID[4], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        print("Created Set-" + str(set) + " of Robot Sets.")
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

    if(set == 4):
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(DBARobot(SET_ONE_ID[0], TYPE_AERIAL, random_coordinates, TASK_LIST_AERIAL))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(DBARobot(SET_ONE_ID[1], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(DBARobot(SET_ONE_ID[2], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(DBARobot(SET_ONE_ID[3], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(DBARobot(SET_ONE_ID[4], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        print("Created Set-" + str(set) + " of Robot Sets.")
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


# Function to create different sets of tasks 
def create_tasks(set):
    print("")
    print("*****")
    print("Starting create_tasks function")
    print("*****")
    print("")

    SET_ONE_ID = [1,2,3,4,5]
    SET_TWO_ID = [1,2,3,4,5,6,7,8,9,10]
    SET_THREE_ID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    TASK_AERIAL_FIREFIGHT = "aerial_fire_extinguish"
    TASK_GROUND_FIREFIGHT = "ground_fire_extinguish"
    TASK_AERIAL_RESCUE = "aerial_rescue"
    TASK_GROUND_RESCUE = "ground_rescue"

    QUALITY_AERIAL_FIREFIGHT = 6
    QUALITY_GROUND_FIREFIGHT = 4
    QUALITY_AERIAL_RESCUE = 10
    QUALITY_GROUND_RESCUE = 8

    SAMPLE_COORDINATE_X = 150
    SAMPLE_COORDINATE_Y = 150
    SAMPLE_COORDINATE_Z = 0
    SAMPLE_COORDINATES = Coordinate(SAMPLE_COORDINATE_X, SAMPLE_COORDINATE_Y, SAMPLE_COORDINATE_Z)

    global task_list

    # set-1, 1 aerial firefight, 3 ground firefight, 1 ground rescue 
    if(set == 1):
        task_list.append(Task(SET_ONE_ID[0], QUALITY_AERIAL_FIREFIGHT, SAMPLE_COORDINATES, TASK_AERIAL_FIREFIGHT))
        task_list.append(Task(SET_ONE_ID[1], QUALITY_GROUND_RESCUE, SAMPLE_COORDINATES, TASK_GROUND_RESCUE))
        task_list.append(Task(SET_ONE_ID[2], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_ONE_ID[3], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_ONE_ID[4], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        
        print("Created Set-" + str(set) + " of Task Sets.")
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
            #print(task.get_time_added())
            print("*****")
            print("")
        print("*****")
        print("Ending create_tasks function")
        print("*****")
        print("")

    if(set == 2):
        task_list.append(Task(SET_TWO_ID[0], QUALITY_AERIAL_RESCUE, SAMPLE_COORDINATES, TASK_AERIAL_RESCUE))
        task_list.append(Task(SET_TWO_ID[1], QUALITY_AERIAL_FIREFIGHT, SAMPLE_COORDINATES, TASK_AERIAL_FIREFIGHT))
        task_list.append(Task(SET_TWO_ID[2], QUALITY_GROUND_RESCUE, SAMPLE_COORDINATES, TASK_GROUND_RESCUE))
        task_list.append(Task(SET_TWO_ID[3], QUALITY_GROUND_RESCUE, SAMPLE_COORDINATES, TASK_GROUND_RESCUE))
        task_list.append(Task(SET_TWO_ID[4], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_TWO_ID[5], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_TWO_ID[6], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_TWO_ID[7], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_TWO_ID[8], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_TWO_ID[9], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        print("Created Set-" + str(set) + " of Task Sets.")
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
            #print(task.get_time_added())
            print("*****")
            print("")
        print("*****")
        print("Ending create_tasks function")
        print("*****")
        print("")

    if(set == 3):
        task_list.append(Task(SET_THREE_ID[0], QUALITY_AERIAL_RESCUE, SAMPLE_COORDINATES, TASK_AERIAL_RESCUE))
        task_list.append(Task(SET_THREE_ID[1], QUALITY_AERIAL_FIREFIGHT, SAMPLE_COORDINATES, TASK_AERIAL_FIREFIGHT))
        task_list.append(Task(SET_THREE_ID[2], QUALITY_AERIAL_FIREFIGHT, SAMPLE_COORDINATES, TASK_AERIAL_FIREFIGHT))
        task_list.append(Task(SET_THREE_ID[3], QUALITY_GROUND_RESCUE, SAMPLE_COORDINATES, TASK_GROUND_RESCUE))
        task_list.append(Task(SET_THREE_ID[4], QUALITY_GROUND_RESCUE, SAMPLE_COORDINATES, TASK_GROUND_RESCUE))
        task_list.append(Task(SET_THREE_ID[5], QUALITY_GROUND_RESCUE, SAMPLE_COORDINATES, TASK_GROUND_RESCUE))
        task_list.append(Task(SET_THREE_ID[6], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_THREE_ID[7], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_THREE_ID[8], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_THREE_ID[9], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_THREE_ID[10], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_THREE_ID[11], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_THREE_ID[12], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_THREE_ID[13], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        task_list.append(Task(SET_THREE_ID[14], QUALITY_GROUND_FIREFIGHT, SAMPLE_COORDINATES, TASK_GROUND_FIREFIGHT))
        print("Created Set-" + str(set) + " of Task Sets.")
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
            #print(task.get_time_added())
            print("*****")
            print("")
        print("*****")
        print("Ending create_tasks function")
        print("*****")
        print("")

    if(set == 4):
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_ONE_ID[0], QUALITY_AERIAL_FIREFIGHT, random_coordinates, TASK_AERIAL_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_ONE_ID[1], QUALITY_GROUND_RESCUE, random_coordinates, TASK_GROUND_RESCUE))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_ONE_ID[2], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_ONE_ID[3], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_ONE_ID[4], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        
        print("Created Set-" + str(set) + " of Task Sets.")
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
            #print(task.get_time_added())
            print("*****")
            print("")
        print("*****")
        print("Ending create_tasks function")
        print("*****")
        print("")

    if(set == 5):
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_TWO_ID[0], QUALITY_AERIAL_RESCUE, random_coordinates, TASK_AERIAL_RESCUE))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_TWO_ID[1], QUALITY_AERIAL_FIREFIGHT, random_coordinates, TASK_AERIAL_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_TWO_ID[2], QUALITY_GROUND_RESCUE, random_coordinates, TASK_GROUND_RESCUE))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_TWO_ID[3], QUALITY_GROUND_RESCUE, random_coordinates, TASK_GROUND_RESCUE))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_TWO_ID[4], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_TWO_ID[5], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_TWO_ID[6], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_TWO_ID[7], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_TWO_ID[8], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_TWO_ID[9], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        print("Created Set-" + str(set) + " of Task Sets.")
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
            #print(task.get_time_added())
            print("*****")
            print("")
        print("*****")
        print("Ending create_tasks function")
        print("*****")
        print("")

    if(set == 6):
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[0], QUALITY_AERIAL_RESCUE, random_coordinates, TASK_AERIAL_RESCUE))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[1], QUALITY_AERIAL_FIREFIGHT, random_coordinates, TASK_AERIAL_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[2], QUALITY_AERIAL_FIREFIGHT, random_coordinates, TASK_AERIAL_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[3], QUALITY_GROUND_RESCUE, random_coordinates, TASK_GROUND_RESCUE))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[4], QUALITY_GROUND_RESCUE, random_coordinates, TASK_GROUND_RESCUE))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[5], QUALITY_GROUND_RESCUE, random_coordinates, TASK_GROUND_RESCUE))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[6], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[7], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[8], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[9], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[10], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[11], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[12], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[13], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        task_list.append(Task(SET_THREE_ID[14], QUALITY_GROUND_FIREFIGHT, random_coordinates, TASK_GROUND_FIREFIGHT))
        print("Created Set-" + str(set) + " of Task Sets.")
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
            #print(task.get_time_added())
            print("*****")
            print("")
        print("*****")
        print("Ending create_tasks function")
        print("*****")
        print("")


def check_task_queue(tasks):
    if len(tasks) > 0 :
        return True
    else:
        return False


def distributed_bees_algorithm():
    print("")
    print("*****")
    print("DistributedBeesAlgorithm")
    print("*****")
    print("")
    if check_task_queue(task_list) :
        print("Task list is not empty, checking tasks.")
        print("")
        # Check the first task first
        for task in task_list :
            task_assigned = False

            print("-----")
            print("Checking task: " + str(task.get_task_id()))
            zone = task.get_zone()
            print("Task zone:  " + str(zone))
            print("")

            print("Checking for robots in this zone")

            # Send this task to all the robots in this zone
            for robot in robot_list :
                if robot.get_zone() == zone :
                    print("Robot " + str(robot.get_robot_id()) + " is in Zone: " + str(zone))
                    task_assigned = robot.DBA(task)
            
            if task_assigned == True :
                print("Task: " + str(task.get_task_id()) + " is assigned to Robot: " + str(robot.get_robot_id()))
            
            elif task_assigned == False :
                print("")
                print("Could not find any robots in the same zone to the task")
                    

    else :
        print("*****")
        print("Task list is empty, Exiting Application.")
        print("*****")

def print_task_allocations():
    print("")
    print("*****")
    print("Task Allocations")
    print("*****")
    print("")
    for task in task_list:
        print("Task: " + str(task.get_task_id()) + " is assigned to robot " + str(task.get_robot_id()))

def main():
    create_tasks(4)
    create_robots(4)
    distributed_bees_algorithm()
    print_task_allocations()

if __name__ == '__main__':
    main()