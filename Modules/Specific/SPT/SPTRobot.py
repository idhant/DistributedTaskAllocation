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

    def assign_service(self,service):
        self.serviceAssigned = service
        self.isBusy = True

    def get_assigned_service(self):
        return self.serviceAssigned

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

                # if the task doesn`t require any services, proceed as normal
                if task.service_required() is False:
                    if(verbose):
                        print("Task does not require any services.")
                    
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

                # if the task requires services
                elif task.service_required() is True:
                    if(verbose):
                        print("Task requires completion of a service before it can be assigned to this robot.")

                    service = task.taskService

                    # if this robot can perform this service on its own, complete the service first
                    if self.calculate_capability(service) is True:
                        
                        # calculate values and assign the robot this service
                        serviceDistance = self.calculate_distance(service)
                        serviceVisibility = self.calculate_visibility(serviceDistance)
                        serviceQuality = service.get_task_quality()
                        
                        # Value recorded to compare optimization results
                        serviceUtility = round(serviceQuality * serviceVisibility, 2)

                        if (verbose):
                            print("Distance of the service from the robot is " + str(distance))
                            print("Utility value of service assignment is " + str(utility))

                        # assign service task to robot and robot to service task
                        self.assign_service(service)
                        service.allocate_task(self, serviceUtility)

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

                    if self.calculate_capability(service) is False:
                        return False

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