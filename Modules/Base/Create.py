from Modules.Base.Task import Task
from Modules.Base.Coordinate import Coordinate
import random

class Create:
    '''Base class to create tasks and robots of different types and numbers for different algorithms.'''

    # Modified function to create tasks for
    def create_task_sets(self, task_list, number_of_tasks, ground_rescue, ground_firefight, aerial_rescue, aerial_firefight, verbose = False):

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

            #global task_list

            task_id = 0

            for task in range(ground_rescue):
                random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
                zone = random_coordinates.get_zone()
                new_quality = self.zone_quality_assigner(zone, QUALITY_GROUND_RESCUE)
                task_list.append(Task(task_id, new_quality, random_coordinates, TASK_GROUND_RESCUE))
                task_id += 1

            for task in range(ground_firefight):
                random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
                zone = random_coordinates.get_zone()
                new_quality = self.zone_quality_assigner(zone, QUALITY_GROUND_FIREFIGHT)
                task_list.append(Task(task_id, new_quality, random_coordinates, TASK_GROUND_FIREFIGHT))
                task_id += 1

            for task in range(aerial_rescue):
                random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
                zone = random_coordinates.get_zone()
                new_quality = self.zone_quality_assigner(zone, QUALITY_AERIAL_RESCUE)
                task_list.append(Task(task_id, new_quality, random_coordinates, TASK_AERIAL_RESCUE))
                task_id += 1

            for task in range(aerial_firefight):
                random_coordinates = Coordinate(round(200 * random.random(), 2), round(200 * random.random(), 2), round(200 * random.random(), 2))
                zone = random_coordinates.get_zone()
                new_quality = self.zone_quality_assigner(zone, QUALITY_AERIAL_FIREFIGHT)
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

    # Function which creates randomized task sets 
    def create_random_task_sets(self, task_list, number_of_tasks, ground_types, aerial_types, verbose = False):

        if (ground_types == True and aerial_types == True):
            ground_tasks = random.randint(0, number_of_tasks)
            aerial_tasks = number_of_tasks - ground_tasks

            ground_rescue = random.randint(0, ground_tasks)
            ground_firefight = ground_tasks - ground_rescue

            aerial_rescue = random.randint(0, aerial_tasks)
            aerial_firefight = aerial_tasks - aerial_rescue

            self.create_task_sets(task_list, number_of_tasks, ground_rescue, ground_firefight, aerial_rescue, aerial_firefight, verbose)
            return

        if (ground_types == True and aerial_types == False):
            ground_tasks = number_of_tasks

            ground_rescue = random.randint(0, ground_tasks)
            ground_firefight = ground_tasks - ground_rescue

            aerial_rescue = 0
            aerial_firefight = 0

            self.create_task_sets(task_list, number_of_tasks, ground_rescue, ground_firefight, aerial_rescue, aerial_firefight, verbose)
            return

        if ground_types == False and aerial_types == True:
            aerial_tasks = number_of_tasks
            aerial_rescue = random.randint(0, aerial_tasks)
            aerial_firefight = aerial_tasks - aerial_rescue
            ground_rescue = 0
            ground_firefight = 0

            self.create_task_sets(task_list, number_of_tasks, ground_rescue, ground_firefight, aerial_rescue, aerial_firefight, verbose)
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
