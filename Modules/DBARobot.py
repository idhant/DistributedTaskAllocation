import math
from Modules.Robot import Robot

class DBARobot(Robot):
    '''Child class to represent the robot in a DBA Environment.'''


    # function to check if the robot is capable to do this task 
    def calculate_capability(self, task):
        for capable_task in self.isCapable:
            if(capable_task == task.get_task_type()):
                return True
        return False

    # function to calculate the 3D distance of the robot to the task
    def calculate_distance(self, task):
        x_axis_distance = self.robotLocation.get_x_coordinate() - task.taskLocation.get_x_coordinate()
        x_axis_distance = pow(x_axis_distance, 2)
        y_axis_distance = self.robotLocation.get_y_coordinate() - task.taskLocation.get_y_coordinate()
        y_axis_distance = pow(y_axis_distance, 2)
        z_axis_distance = self.robotLocation.get_z_coordinate() - task.taskLocation.get_z_coordinate()
        z_axis_distance = pow(z_axis_distance, 2)
        distance = math.sqrt(x_axis_distance + y_axis_distance + z_axis_distance)
        return distance

    # function to calculate the visibility of the robot to the task
    def calculate_visibility(self, distance):
        visibility = 1/distance
        return visibility

    def set_assigned_task_utility(self, utility):
        self.taskUtility = utility

    def get_zone(self):
        return self.robotLocation.get_zone()

    # DBA algorithm for each robot
    def DBA(self, task):
        print("")
        print("-----")
        print("Checking Robot: " + str(self.get_robot_id()) + " Capability.")
        # Check capability
        if self.calculate_capability(task) :
            print("Robot capable to perform this task")
            # check busy status
            print("Checking Robot Status")
            busyStatus = self.get_robot_status()

            if busyStatus is False:
                print("Robot is Free")
                # calculate values and assign the robot this task
                distance = self.calculate_distance(task)
                visibility = self.calculate_visibility(distance)
                quality = task.get_task_quality()
                
                # Value recorded to compare optimization results
                utility = quality * visibility 

                print("Distance of task from the robot is " + str(distance))
                print("Utility value of task assignment is " + str(utility))


                # assign task to robot and robot to task
                self.assign_task(task)
                task.allocate_task(self)

                print("Robot: " + str(self.get_robot_id()) + " allocated task: " + str(task.get_task_id()) + " to itself.")
                print("-----")
                print("")

                # store utility value 
                self.set_assigned_task_utility(utility)

                return True

            else:
                print("Robot is Not Free")
                current_task_quality = self.get_assigned_task().get_task_quality()
                new_task_quality = task.get_task_quality()

                differential_factor = 2
                # quality factor is a threshold value which decides if one task can 
                # supercede the other task
                if (new_task_quality - current_task_quality > differential_factor):
                    # calculate values and assign the robot this task
                    distance = self.calculate_distance(task)
                    visibility = self.calculate_visibility(distance)
                    quality = task.get_task_quality()
                    
                    # Value recorded to compare optimization results
                    utility = quality * visibility 

                    print("Distance of task from the robot is " + str(distance))
                    print("Utility value of task assignment is " + str(utility))

                    # assign task to robot and robot to task
                    self.assign_task(task)
                    task.allocate_task(self)

                    print("Robot: " + str(self.get_robot_id()) + " allocated task: " + str(task.get_task_id()) + " to itself.")
                    print("-----")
                    print("")

                    # store utility value 
                    self.set_assigned_task_utility(utility)

                    return True

                else:
                    print("The New task could not supercede the old task.")
                    print("-----")
                    print("")
                    return False      

        else:
            print("Robot is not capable of performing task.")
            print("-----")
            print("")
            return False   

    pass