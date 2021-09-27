import math
import time
from Modules.Base.Task import Task

class SPTTask(Task):
    '''Child class to represent the task in a SPT Environment.'''

    def __init__(self, taskID, taskQuality, taskLocation, taskType, taskService):
        self.taskID = taskID
        self.taskQuality = taskQuality
        self.taskLocation = taskLocation
        self.taskType = taskType
        self.taskService = taskService
        
        current_time = time.perf_counter()
        self.timeAdded = current_time

        self.robotAllocated = -1
        self.taskAllocated = False
        self.timeAllocated = 0

        self.timesReallocated = 0
        self.timeDeallocated = 0

    def service_required(self):
        if(self.taskService is not None):
            return True
        else:
            return False
