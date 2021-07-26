from Robot import Robot
from Task import Task
from Coordinate import Coordinate
import math
import random

robot_list = []
task_list = []

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
        robot_list.append(Robot(SET_ONE_ID[0], TYPE_AERIAL, BASE_COORDINATES, TASK_LIST_AERIAL))
        robot_list.append(Robot(SET_ONE_ID[1], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_ONE_ID[2], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_ONE_ID[3], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_ONE_ID[4], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
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

    if(set == 2):
        robot_list.append(Robot(SET_TWO_ID[0], TYPE_AERIAL, BASE_COORDINATES, TASK_LIST_AERIAL))
        robot_list.append(Robot(SET_TWO_ID[1], TYPE_AERIAL, BASE_COORDINATES, TASK_LIST_AERIAL))
        robot_list.append(Robot(SET_TWO_ID[2], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_TWO_ID[3], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_TWO_ID[4], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_TWO_ID[5], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_TWO_ID[6], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_TWO_ID[7], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_TWO_ID[8], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_TWO_ID[9], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
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
        
    if(set == 3):
        robot_list.append(Robot(SET_THREE_ID[0], TYPE_AERIAL, BASE_COORDINATES, TASK_LIST_AERIAL))
        robot_list.append(Robot(SET_THREE_ID[1], TYPE_AERIAL, BASE_COORDINATES, TASK_LIST_AERIAL))
        robot_list.append(Robot(SET_THREE_ID[2], TYPE_AERIAL, BASE_COORDINATES, TASK_LIST_AERIAL))
        robot_list.append(Robot(SET_THREE_ID[3], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_THREE_ID[4], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_THREE_ID[5], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_THREE_ID[6], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_THREE_ID[7], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_THREE_ID[8], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_THREE_ID[9], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_THREE_ID[10], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_THREE_ID[11], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_THREE_ID[12], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_THREE_ID[13], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
        robot_list.append(Robot(SET_THREE_ID[14], TYPE_GROUND, BASE_COORDINATES, TASK_LIST_GROUND))
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
        robot_list.append(Robot(SET_ONE_ID[0], TYPE_AERIAL, random_coordinates, TASK_LIST_AERIAL))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_ONE_ID[1], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_ONE_ID[2], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_ONE_ID[3], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_ONE_ID[4], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
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

    if(set == 5):
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_TWO_ID[0], TYPE_AERIAL, random_coordinates, TASK_LIST_AERIAL))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_TWO_ID[1], TYPE_AERIAL, random_coordinates, TASK_LIST_AERIAL))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_TWO_ID[2], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_TWO_ID[3], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_TWO_ID[4], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_TWO_ID[5], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_TWO_ID[6], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_TWO_ID[7], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_TWO_ID[8], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_TWO_ID[9], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
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

    if(set == 6):
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[0], TYPE_AERIAL, random_coordinates, TASK_LIST_AERIAL))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[1], TYPE_AERIAL, random_coordinates, TASK_LIST_AERIAL))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[2], TYPE_AERIAL, random_coordinates, TASK_LIST_AERIAL))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[3], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[4], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[5], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[6], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[7], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[8], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[9], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[10], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[11], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[12], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[13], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
        random_coordinates = Coordinate(200 * random.random(), 200 * random.random(), 200 * random.random())
        robot_list.append(Robot(SET_THREE_ID[14], TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
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

# function to calculate the distances of all the robots to all the tasks
def calculate_distance(robot_coordinates, task_coordinates):
    x_axis_distance = robot_coordinates.get_x_coordinate() - task_coordinates.get_x_coordinate()
    x_axis_distance = pow(x_axis_distance, 2)
    y_axis_distance = robot_coordinates.get_y_coordinate() - task_coordinates.get_y_coordinate()
    y_axis_distance = pow(y_axis_distance, 2)
    z_axis_distance = robot_coordinates.get_z_coordinate() - task_coordinates.get_z_coordinate()
    z_axis_distance = pow(z_axis_distance, 2)
    distance = math.sqrt(x_axis_distance + y_axis_distance + z_axis_distance)
    return distance

# function to calculate the visibility of all the robots to all the tasks 
def calculate_visibility(distance):
    visibility = 1/distance
    return visibility

# function to check the capability of the robots and find the visibility sets
def check_capability_and_calculate_visibility():
    task_robot_visibility_set = [[]]

    print("*****")
    print("Checking capability and calculating visibility sets")
    print("*****")
    print("")

    # Calculating capability, distance sets, visibility sets
    for task in task_list:
        task_type = task.get_task_type()
        print("*****")
        print("Task-" + str(task.get_task_id()) + " type is: " + task_type)
        print("*****")
        print("")
        robot_distance_from_task = []
        robot_visibility_from_task = []

        robot_capable = False # enforce false value for correct checking of capability
        #check to see if the tasks in the queue can be accomplished by the current robots available 
        for robot in robot_list:
            capable_task_list = robot.get_is_capable()
            print("-----")
            print("Robot-" + str(robot.get_robot_id()) + " is capable of tasks: ")

            for capable_task in capable_task_list:
                print(capable_task)
                if(capable_task == task_type):
                    robot_capable = True
                    
            # calculate the distances of all the robots to the tasks in the task queue
            if(robot_capable == True):
                print("Robot is Capable of doing this task.")
                distance = calculate_distance(robot.get_robot_location(), task.get_task_location())
                print("Distance of Robot-" + str(robot.get_robot_id()) + " to the task-" + str(task.get_task_id()) + " is " + str(distance))
                robot_distance_from_task.append(distance)
                visibility = calculate_visibility(distance)
                print("Visibility of Robot-" + str(robot.get_robot_id()) + " to the task-" + str(task.get_task_id()) + " is " + str(visibility))
                robot_visibility_from_task.append(visibility)
                robot_capable = False # reset the bool for the loop
            
            # Robot not capable, invalid distances and visibility
            else:
                print("Robot is not capable of doing this task")
                distance = -1
                visibility = -1
                robot_distance_from_task.append(distance)
                robot_visibility_from_task.append(visibility)
            print("-----")
            print("")


        # Adding sets of robot visibility for this task to the main 2d array
        task_robot_visibility_set.append([robot_visibility_from_task])

    print("")
    print("*****")
    print("Visibility sets calculated")
    print("*****")
    print("")

    return task_robot_visibility_set

# function to calculate the relative quality of the tasks 
def calculate_relative_quality():
    quality_list = []
    total_quality = 0

    # Get all qualities and add them in the list 
    for task in task_list:
        quality = task.get_task_quality()
        quality_list.append(quality)
    
    # Calculate total quality
    for quality in quality_list:
        total_quality = quality + total_quality
    
    # Calculate relative quality
    for task in task_list:
        quality = task.get_task_quality()
        relative_quality = quality/total_quality
        task.set_task_relative_quality(relative_quality)

# function to print the relative quality of all the tasks 
def print_relative_quality(task_list):
    print("*****")
    for task in task_list:
        print("Task-" +str(task.get_task_id()) + " Relative Quality is: " + str(task.get_task_relative_quality()))
    print("*****")
    print("")

# function to calculate the utility values from the visibility sets and the quality of the tasks 
def calculate_utility(task_robot_visibility_set):
    print("*****")
    print("Calculating utility")
    print("*****")
    print("")
    task_robot_utility_set = [[]]

    task_index = 0
    for visibility_set in task_robot_visibility_set:
        #print(visibility_set)
        print("*****")

        for visibility in visibility_set:
            print("Calculating utility set for Task-" + str(task_list[task_index].get_task_id()))
            #print(visibility)
            task_utility_set = []
            robot_index = 0
            print("")
            for visible in visibility:
                if(visible != -1):
                    print("Robot-" + str(robot_list[robot_index].get_robot_id()) + " has as visibility value with this task")
                    relative_quality = float(task_list[task_index].get_task_relative_quality())
                    utility = visible * relative_quality 
                    print("Utility of Task-" + str(task_list[task_index].get_task_id()) + " to the Robot-" + str(robot_list[robot_index].get_robot_id()) + " is = " + str(utility))
                    task_utility_set.append(utility)
                    print("")
                else:
                    utility = -1
                    task_utility_set.append(utility)
                robot_index = robot_index + 1
            task_index = task_index + 1
            
            task_robot_utility_set.append([task_utility_set])
        print("*****")
        print("")

    return task_robot_utility_set

# function to calculate the utility probability sets
def calculate_utility_probabilities(task_robot_utility_set):
    print("")
    print("*****")
    print("Calculating utility probabilities")
    print("*****")
    print("")
    utility_probabilities = []
    task_index = 0
    for task_robot_utility in task_robot_utility_set:
        print("*****")
        #print(task_robot_utility)
        for utility_set in task_robot_utility:
            print("Calculating utility probabilities for Task-" + str(task_list[task_index].get_task_id()))
            #print(utility_set)
            robot_index = 0
            utility_sum = 0
            task_assignment_probabilities = []
            #print(task_assignment_probabilities)
            
            for utility in utility_set:
                if(utility != -1):
                    utility_sum += utility
                #print(utility)
            #print(utility_sum)

            for utility in utility_set:
                if(utility != -1):
                    assignment_probability = utility/utility_sum
                    
                    #enforce final assignment
                    task_assignment_probabilities.append(assignment_probability)

                else:
                    assignment_probability = -1
                    task_assignment_probabilities.append(assignment_probability)
                robot_index += 1

            #print(task_assignment_probabilities)
            utility_probabilities.append(task_assignment_probabilities)
            #print(utility_probabilities)
            task_index = task_index + 1

    return utility_probabilities

# function to print hte utility probability sets
def print_utility_probabilities(utility_probabilities):
    print("")
    print("*****")
    print("Utility Probabilities are:")
    print("*****")
    print("")
    task_index = 0
    for utility_probability in utility_probabilities:
        print("*****")
        #print(utility_probability)
        robot_index = 0
        print("Probability of Task-" + str(task_list[task_index].get_task_id()) + " being assigned to the robots are")
        for probability in utility_probability:
            #print(probability)
            print("Robot-" + str(robot_list[robot_index].get_robot_id()) + " = " + str(probability))
            robot_index += 1
        task_index += 1

# function to decide allocations based on the utility probability sets
def assign_allocations(utility_probabilities):
    print("")
    print("*****")
    print("Allocations decided are:")
    print("*****")
    print("")
    task_index = 0
    for utility_probability in utility_probabilities:
        print("*****")
        print("Assignment probabilities for task-" + str(task_list[task_index].get_task_id()) + " are: " + str(utility_probability))
        robot_index = 0

        highest_probability = -1
        assigned_robot_index = -1

        for probability in utility_probability:
            #print(probability)
            if(probability > highest_probability):
                # if the robot is not busy 
                if(robot_list[robot_index].get_robot_status() == False):
                    highest_probability = probability
                    assigned_robot_index = robot_index
            robot_index += 1
        
        if(task_list[task_index].taskAllocated  & robot_list[assigned_robot_index].isBusy == False):
            # Allocating the task to this robot and changing its  status to true
            task_list[task_index].allocate_task(robot_list[assigned_robot_index].get_robot_id())
            robot_list[assigned_robot_index].assign_task(task_list[task_index].get_task_id())

            print("Task-" + str(task_list[task_index].get_task_id()) + " is assigned to robot-" + str(task_list[task_index].get_robot_allocated()) + " with a probability of " + str(highest_probability))
        print("*****")
        print("")
        task_index += 1

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
    for task in task_list:
        print("Time taken to allocate task-" + str(task.get_task_id())  + " was " + str(round(task.get_time_taken_to_allocate(), 2)) + " seconds")
        total_time += task.get_time_taken_to_allocate()
    
    print("")
    print("Total time taken to allocate all the tasks was " + str(round(total_time, 2)) + " seconds")
    print("")

def main():
    
    # create robot sets
    create_robots(1)
    # create task sets
    create_tasks(1)
    
    # Calculate visibility sets
    task_robot_visibility_set = check_capability_and_calculate_visibility()

    # Calculate relative quality
    calculate_relative_quality()

    # print relative quality
    print_relative_quality(task_list)

    # Calculate utilities
    task_robot_utility_set = calculate_utility(task_robot_visibility_set)

    #Calculate utility probabilities
    utility_probabilities = calculate_utility_probabilities(task_robot_utility_set)

    # print the utility probability sets
    print_utility_probabilities(utility_probabilities)

    # decide allocations and print them
    assign_allocations(utility_probabilities)

    # print the local and global time taken to allocate tasks
    print_time_taken_to_allocate()

if __name__ == '__main__':
    main()
