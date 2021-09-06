import math
from Modules.Base.Robot import Robot

class SPTRobot(Robot):
    '''Child class to represent the robot in a SPT Environment.'''

    def __init__(self, robotID, robotType, robotLocation, isCapable):
        self.robotID = robotID
        self.robotType = robotType
        self.robotLocation = robotLocation
        self.isCapable = isCapable
        
        self.taskAssigned = -1
        self.isBusy = False

        self.serviceAssigned = -1

    def assign_task(self,task):
        self.taskAssigned = task
        self.isBusy = True


    def assign_service(self,service):
        self.serviceAssigned = service
        self.isBusy = True

    # SPT algorithm
    def SPT(self, task, verbose=False):
        if (verbose):
            print("")
            print("-----")
            print("Checking Robot: " + str(self.get_robot_id()) + " Capability.")

        # if robot is capable
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

                # if the task doesnt require any services, proceed as normal
                if task.service_required() is False:
                    if(verbose):
                        print("Task doesnt require any services.")
                    
                    # calculate values and assign the robot this task
                    distance = self.calculate_distance(task)
                    visibility = self.calculate_visibility(distance)
                    quality = task.get_task_quality()
                    
                    # Value recorded to compare optimization results
                    utility = round(quality * visibility, 2)

                    if (verbose):
                        print("Distance of task from the robot is " + str(distance))
                        print("Utility value of task assignment is " + str(utility))

                    # assign task to robot and robot to task
                    self.assign_task(task)
                    task.allocate_task(self)

                    if (verbose):
                        print("Robot: " + str(self.get_robot_id()) + " allocated task: " + str(task.get_task_id()) + " to itself.")
                        print("-----")
                        print("")

                    # store utility value 
                    self.set_assigned_task_utility(utility)

                # if the task requires services
                if task.service_required() is True:
                    if(verbose):
                        print("Task requires completion of a service before it can be assigned to this robot.")

                    service = task.taskService

                    # if this robot can perform this service on its own, complete the service first
                    if self.calculate_capability(service):
                        
                        # calculate values and assign the robot this service
                        distance = self.calculate_distance(service)
                        visibility = self.calculate_visibility(distance)
                        quality = service.get_task_quality()
                        
                        # Value recorded to compare optimization results
                        utility = round(quality * visibility, 2)

                        if (verbose):
                            print("Distance of the service from the robot is " + str(distance))
                            print("Utility value of service assignment is " + str(utility))

                        # assign task to robot and robot to task
                        self.assign_service(service)
                        service.allocate_task(self)

                        if (verbose):
                            print("Robot: " + str(self.get_robot_id()) + " allocated task: " + str(task.get_task_id()) + " to itself.")
                            print("-----")
                            print("")

                        # store utility value 
                        #self.set_assigned_task_utility(utility)

            # if robot is busy, check if reallocation can be done
            # NO REALLOCATION
        
        # Not capable of doing the task, simply return False
        else:
            if (verbose):
                print("Robot is not capable of performing task.")
                print("-----")
                print("")
            return False   
    
    pass