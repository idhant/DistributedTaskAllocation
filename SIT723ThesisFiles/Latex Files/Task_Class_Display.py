from datetime import datetime
import time

class Task:
    '''Base class to represent the task object type in the experiment.'''
    
    def __init__(self, taskID, taskQuality, taskLocation, taskType):
        self.taskID = taskID
        self.taskQuality = taskQuality
        self.taskLocation = taskLocation
        self.taskType = taskType
        
        current_time = time.time()
        #now = datetime.now()
        #current_time = now
        #current_time = now.strftime("%H:%M:%S")
        self.timeAdded = current_time
        self.robotAllocated = 0
        self.taskAllocated = False

    def allocate_task(self,robotID):
        self.robotAllocated = robotID
        self.taskAllocated = True
        current_time = time.time()
        #now = datetime.now()
        #current_time = now.strftime("%H:%M:%S")
        self.timeAllocated = current_time

    def get_task_id(self):
        return self.taskID

    def get_task_quality(self):
        return self.taskQuality

    def get_task_type(self):
        return self.taskType

    def get_task_location(self):
        return self.taskLocation

    def get_task_quality(self):
        return self.taskQuality

    def get_robot_allocated(self):
        return self.robotAllocated

    def get_time_added(self):
        return self.timeAdded

    def get_time_taken_to_allocate(self):
        return (self.timeAllocated - self.timeAdded )

    def set_task_relative_quality(self, relative_quality):
        self.taskRelativeQuality = relative_quality

    def get_task_relative_quality(self):
        return self.taskRelativeQuality

    def set_task_status(self, status):
        self.taskAllocated = status

    def set_robot_allocated(self, allocated):
        self.robotAllocated = allocated
    
    pass
