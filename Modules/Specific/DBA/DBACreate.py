from Modules.Base.Create import Create
from Modules.Specific.DBA.DBARobot import DBARobot
from Modules.Base.Coordinate import Coordinate
import random

class DBACreate(Create):
    '''Child class to create DBA specific robots.'''

    # Modified function to create robots
    def create_robot_sets(self, robot_list, number_of_robots, ground_robots, aerial_robots, verbose = False ):
        
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

            #global robot_list

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

    # Function which creates randomized robot sets 
    def create_random_robot_sets(self, robot_list, number_of_robots, verbose = False):
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

        #global robot_list

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
