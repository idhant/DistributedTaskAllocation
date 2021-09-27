from Modules.Base.Create import Create
from Modules.Specific.SPT.SPTRobot import SPTRobot
from Modules.Specific.SPT.SPTTask import SPTTask
from Modules.Base.Task import Task
from Modules.Base.Coordinate import Coordinate
import random

class SPTCreate(Create):
    '''Child class to create SPT specific robots.'''

    # Function to create SPT suitable robots
    def create_robot_sets(self, robot_list, number_of_robots, ground_robots, aerial_robots, verbose = False):
        
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

            robot_id = 0

            for robot in range(ground_robots):
                random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
                robot_list.append(SPTRobot(robot_id, TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
                robot_id += 1

            for robot in range(aerial_robots):
                random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
                robot_list.append(SPTRobot(robot_id, TYPE_AERIAL, random_coordinates, TASK_LIST_AERIAL))
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
    
    # Function to create randomized SPT suitable robots
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

        robot_id = 0

        for robot in range(ground_robots):
            random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
            robot_list.append(SPTRobot(robot_id, TYPE_GROUND, random_coordinates, TASK_LIST_GROUND))
            robot_id += 1

        for robot in range(aerial_robots):
            random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
            robot_list.append(SPTRobot(robot_id, TYPE_AERIAL, random_coordinates, TASK_LIST_AERIAL))
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

    # Function to create SPT suitable tasks
    def create_task_sets(self, task_list, number_of_tasks, ground_rescue, ground_firefight, aerial_rescue, aerial_firefight, number_of_services, ground_services, aerial_services, verbose = False):

        if(number_of_tasks == ground_rescue + ground_firefight + aerial_rescue + aerial_firefight):
            if(number_of_services == ground_services + aerial_services ):
                
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

                task_id = 0
                service_id = 0

                services_created = 0
                ground_services_created = 0
                aerial_services_created = 0

                for task in range(ground_rescue):
                    random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
                    zone = random_coordinates.get_zone()
                    new_quality = self.zone_quality_assigner(zone, QUALITY_GROUND_RESCUE)

                    service = None
                    if(number_of_services > services_created):
                        if(ground_services > ground_services_created):
                            service = self.create_random_service(service_id, random_coordinates, "ground")
                            services_created += 1
                            ground_services_created += 1
                            service_id += 1
                        else:
                            service = self.create_random_service(service_id, random_coordinates, "aerial")
                            services_created += 1
                            aerial_services_created += 1
                            service_id += 1
                        
                        task_list.append(SPTTask(task_id, new_quality, random_coordinates, TASK_GROUND_RESCUE, service))
                        task_id += 1

                    else:
                        task_list.append(SPTTask(task_id, new_quality, random_coordinates, TASK_GROUND_RESCUE, service))
                        task_id += 1

                for task in range(ground_firefight):
                    random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
                    zone = random_coordinates.get_zone()
                    new_quality = self.zone_quality_assigner(zone, QUALITY_GROUND_FIREFIGHT)

                    service = None
                    if(number_of_services > services_created):
                        if(ground_services > ground_services_created):
                            service = self.create_random_service(service_id, random_coordinates, "ground")
                            services_created += 1
                            ground_services_created += 1
                            service_id += 1
                        else:
                            service = self.create_random_service(service_id, random_coordinates, "aerial")
                            services_created += 1
                            aerial_services_created += 1
                            service_id += 1
                        
                        task_list.append(SPTTask(task_id, new_quality, random_coordinates, TASK_GROUND_FIREFIGHT, service))
                        task_id += 1

                    else:
                        task_list.append(SPTTask(task_id, new_quality, random_coordinates, TASK_GROUND_FIREFIGHT, service))
                        task_id += 1

                for task in range(aerial_rescue):
                    random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
                    zone = random_coordinates.get_zone()
                    new_quality = self.zone_quality_assigner(zone, QUALITY_AERIAL_RESCUE)

                    service = None
                    if(number_of_services > services_created):
                        if(ground_services > ground_services_created):
                            service = self.create_random_service(service_id, random_coordinates, "ground")
                            services_created += 1
                            ground_services_created += 1
                            service_id += 1
                        else:
                            service = self.create_random_service(service_id, random_coordinates, "aerial")
                            services_created += 1
                            aerial_services_created += 1
                            service_id += 1
                        
                        task_list.append(SPTTask(task_id, new_quality, random_coordinates, TASK_AERIAL_RESCUE, service))
                        task_id += 1

                    else:
                        task_list.append(SPTTask(task_id, new_quality, random_coordinates, TASK_AERIAL_RESCUE, service))
                        task_id += 1

                for task in range(aerial_firefight):
                    random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
                    zone = random_coordinates.get_zone()
                    new_quality = self.zone_quality_assigner(zone, QUALITY_AERIAL_FIREFIGHT)

                    service = None
                    if(number_of_services > services_created):
                        if(ground_services > ground_services_created):
                            service = self.create_random_service(service_id, random_coordinates, "ground")
                            services_created += 1
                            ground_services_created += 1
                            service_id += 1
                        else:
                            service = self.create_random_service(service_id, random_coordinates, "aerial")
                            services_created += 1
                            aerial_services_created += 1
                            service_id += 1
                        
                        task_list.append(SPTTask(task_id, new_quality, random_coordinates, TASK_AERIAL_FIREFIGHT, service))
                        task_id += 1

                    else:
                        task_list.append(SPTTask(task_id, new_quality, random_coordinates, TASK_AERIAL_FIREFIGHT, service))
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
                print("Number of Services do not add up, please verify.")

        else:
            print("Number of tasks do not add up, please verify.")

    # Function to create randomized SPT suitable tasks
    def create_random_task_sets(self, task_list, number_of_tasks, ground_types, aerial_types, number_of_services, ground_service_types, aerial_service_types, verbose = False):

        if(ground_service_types == True and aerial_service_types == True):
            ground_services = random.randint(0, number_of_services)
            aerial_services = number_of_services - ground_services
        
        if(ground_service_types == True and aerial_service_types == False):
            ground_services = number_of_services
            aerial_services = 0

        if(ground_service_types == False and aerial_service_types == True):
            ground_services = 0
            aerial_services = number_of_services

        if (ground_types == True and aerial_types == True):
            ground_tasks = random.randint(0, number_of_tasks)
            aerial_tasks = number_of_tasks - ground_tasks

            ground_rescue = random.randint(0, ground_tasks)
            ground_firefight = ground_tasks - ground_rescue

            aerial_rescue = random.randint(0, aerial_tasks)
            aerial_firefight = aerial_tasks - aerial_rescue

            self.create_task_sets(task_list, number_of_tasks, ground_rescue, ground_firefight, aerial_rescue, aerial_firefight, number_of_services, ground_services, aerial_services, verbose)
            return

        if (ground_types == True and aerial_types == False):
            ground_tasks = number_of_tasks

            ground_rescue = random.randint(0, ground_tasks)
            ground_firefight = ground_tasks - ground_rescue

            aerial_rescue = 0
            aerial_firefight = 0

            self.create_task_sets(task_list, number_of_tasks, ground_rescue, ground_firefight, aerial_rescue, aerial_firefight, number_of_services, ground_services, aerial_services, verbose)
            return

        if ground_types == False and aerial_types == True:
            aerial_tasks = number_of_tasks
            aerial_rescue = random.randint(0, aerial_tasks)
            aerial_firefight = aerial_tasks - aerial_rescue
            ground_rescue = 0
            ground_firefight = 0

            self.create_task_sets(task_list, number_of_tasks, ground_rescue, ground_firefight, aerial_rescue, aerial_firefight, number_of_services, ground_services, aerial_services, verbose)
            return

        else:
            print("No condition matched.")
            return

    # Function to calculate adjusted quality value based on the zone multiplier
    def zone_quality_assigner(self, zone, base_quality):
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

    # Function which generates a service task
    def create_random_service(self, service_id, service_coordinates, service_type):
        
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
        
        #random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
        zone = service_coordinates.get_zone()
        
        randvalue = random.random() * 100

        if(service_type == "ground"):

            if (randvalue >= 0 and randvalue < 50):
                new_quality = self.zone_quality_assigner(zone, QUALITY_GROUND_RESCUE)
                return Task(service_id, new_quality, service_coordinates, TASK_GROUND_RESCUE)
                
            elif (randvalue >= 50 and randvalue <= 100): 
                new_quality = self.zone_quality_assigner(zone, QUALITY_GROUND_FIREFIGHT)
                return Task(service_id, new_quality, service_coordinates, TASK_GROUND_FIREFIGHT)

        elif(service_type == "aerial"):

            if (randvalue >= 0 and randvalue < 50): 
                new_quality = self.zone_quality_assigner(zone, QUALITY_AERIAL_RESCUE)
                return Task(service_id, new_quality, service_coordinates, TASK_AERIAL_RESCUE)

            elif (randvalue >= 50 and randvalue <= 100):
                new_quality = self.zone_quality_assigner(zone, QUALITY_AERIAL_FIREFIGHT)
                return Task(service_id, new_quality, service_coordinates, TASK_AERIAL_FIREFIGHT)