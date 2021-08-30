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
        
        self.timeAdded = current_time
        self.robotAllocated = -1
        self.taskAllocated = False
        self.timeAllocated = 0

        self.timesReallocated = 0
        self.timeDeallocated = 0

    def allocate_task(self,robot):
        self.robotAllocated = robot
        self.taskAllocated = True
        current_time = time.time()
        #now = datetime.now()
        #current_time = now.strftime("%H:%M:%S")
        self.timeAllocated = current_time

    def deallocate_task(self):
        self.robotAllocated = -1
        self.taskAllocated = False
        current_time = time.time()
        self.timeDeallocated = current_time
        self.timesReallocated += 1 
        self.timeAllocated = 0

    def get_zone(self):
        return self.taskLocation.get_zone()

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

    def get_robot_id(self):
        if self.robotAllocated != -1 :
            return self.robotAllocated.get_robot_id()
        else :
            return -1

    def get_time_added(self):
        return self.timeAdded

    def get_time_taken_to_allocate(self):
        if self.timeAllocated != 0 :
            return (self.timeAllocated - self.timeAdded )
        else:
            return 0

    def get_time_wasted_on_dealloaction(self):
        if self.timeDeallocated != 0 :
            return round((self.timeDeallocated - self.timeAdded ), 2)
        else:
            return 0

    def set_task_relative_quality(self, relative_quality):
        self.taskRelativeQuality = relative_quality

    def get_task_relative_quality(self):
        return self.taskRelativeQuality

    def set_task_status(self, status):
        self.taskAllocated = status

    def set_robot_allocated(self, allocated):
        self.robotAllocated = allocated
    
    pass
