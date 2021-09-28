import math
from Modules.Base.Robot import Robot

class DBARobot(Robot):
    '''Child class to represent the robot in a DBA Environment.'''

    # DBA algorithm for each robot
    def DBA(self, task, verbose=False):
        if (verbose):
            print("")
            print("-----")
            print("Checking Robot: " + str(self.get_robot_id()) + " Capability.")
        
        # Check Robot capability
        if self.calculate_capability(task) :
            if (verbose):
                print("Robot capable to perform this task")
                # check busy status
                print("Checking Robot Status")

            # Check Robot Status
            busyStatus = self.get_robot_status()

            # if robot is not busy
            if busyStatus is False:
                if (verbose):
                    print("Robot is Free")

                # calculate values and assign the robot this task
                distance = self.calculate_distance(task)
                visibility = self.calculate_visibility(distance)
                quality = task.get_task_quality()
                
                # Value recorded to compare optimization results
                utility = round(quality * visibility, 2)

                if (verbose):
                    print("Distance of task from the robot is " + str(distance))
                    print("Utility value of task assignment is " + str(utility))

                # assign task to robot and robot to task and store the utility value 
                self.assign_task(task)
                task.allocate_task(self, utility)

                if (verbose):
                    print("Robot: " + str(self.get_robot_id()) + " allocated task: " + str(task.get_task_id()) + " to itself.")
                    print("-----")
                    print("")

                return True

            # if robot is busy, check if reallocation can be done 
            else:
                if (verbose):
                    print("Robot is Not Free")

                # compare the quality values of the tasks
                current_task = self.get_assigned_task()
                current_task_quality = current_task.get_task_quality()
                new_task_quality = task.get_task_quality()

                # quality factor is a threshold value which decides if one task can 
                # supercede the other task
                differential_factor = 2
                
                if (new_task_quality - current_task_quality > differential_factor):

                    # Unassign previous task 
                    current_task.deallocate_task()

                    # calculate values and assign new task to the the robot
                    distance = self.calculate_distance(task)
                    visibility = self.calculate_visibility(distance)
                    quality = task.get_task_quality()
                    
                    # Value recorded to compare optimization results
                    utility = round(quality * visibility, 2)

                    if (verbose):
                        print("Distance of task from the robot is " + str(distance))
                        print("Utility value of task assignment is " + str(utility))

                    # assign task to robot and robot to task and store the utility value 
                    self.assign_task(task)
                    task.allocate_task(self, utility)

                    if (verbose):
                        print("Robot: " + str(self.get_robot_id()) + " allocated task: " + str(task.get_task_id()) + " to itself.")
                        print("-----")
                        print("")

                    return True

                else:
                    if (verbose):
                        print("The New task could not supercede the old task.")
                        print("-----")
                        print("")
                    return False      

        # Not capable of doing the task, simply return False
        else:
            if (verbose):
                print("Robot is not capable of performing task.")
                print("-----")
                print("")
            return False   

    pass