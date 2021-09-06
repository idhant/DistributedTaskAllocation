import math

class Robot:
    '''Base class to represent the robot object type in the experiment.'''

    def __init__(self, robotID, robotType, robotLocation, isCapable):
        self.robotID = robotID
        self.robotType = robotType
        self.robotLocation = robotLocation
        self.isCapable = isCapable
        
        self.taskAssigned = -1
        self.isBusy = False
        

    def assign_task(self,task):
        self.taskAssigned = task
        self.isBusy = True
        
    def get_assigned_task(self):
        return self.taskAssigned

    def get_robot_id(self):
        return self.robotID

    def get_robot_type(self):
        return self.robotType

    def get_robot_location(self):
        return self.robotLocation

    def get_is_capable(self):
        return self.isCapable

    def get_robot_location(self):
        return self.robotLocation

    def get_robot_status(self):
        return self.isBusy

    def set_robot_location(self,newLocation):
        self.robotLocation = newLocation

    def set_robot_task(self,newTask):
        self.taskAssigned = newTask

    def set_robot_status(self,newStatus):
        self.isBusy = newStatus

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
        distance = round(math.sqrt(x_axis_distance + y_axis_distance + z_axis_distance), 2)
        return distance

    # function to calculate the visibility of the robot to the task
    def calculate_visibility(self, distance):
        visibility = 1/distance
        return visibility

    def set_assigned_task_utility(self, utility):
        self.taskUtility = utility

    def get_zone(self):
        return self.robotLocation.get_zone()


    pass
