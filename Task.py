# Class to represent a task in our simulation

# Contains variables like:

#taskID = Used to identify the task in the simulation.
#item taskDescription = Used to describe the task and its requirements.
#item taskQuality = Used to assign a arbitrary scaler value the is used to define the quality/priority of a task. For the purposes of this experiment, the value can range between 1 to 10 with a task of 10 holding the highest priority.
# taskRelativeQuality = Used to calculate the quality of the task relative to all the tasks quality. This value makes it easier to relate the priority of the tasks and calculate the final utility value.
#item taskLocation = Used to store the 3D coordinates of the task in the simulation environment.
#item taskType = Used to define the nature of the task, i.e ground firefighting, aerial rescue etc. This property of the task is useful in determining which robot can be allocated to it based on it capabilities.
# taskAllocated = Used to check if the task is allocated to the robots.
#item timeAdded = Used to store the time when this task first appeared in the task queue.
# robotAllocated = Used to store which robot is allocated to this task.
# #\item timeAllocated = Used to store the time when this task was allocated.
#\item timeCompleted = Used to tore the time when this task was completed. As the focus for this experiment is on allocation, this value does not test the robots ability to complete the task but is instead used to keep track of the task completion and remove it from the queue hence it is a arbitrary value. It is calculated by multiplying the tasks scalar quality to the tasks initial distance from the robot assigned. 
#\item isReallocated = Used to check if the task was reallocated.
#\item timeReallocated = Used to store the time when this task was reallocated.To avoid the problem of looping re-allocations, the experiment design at this stage only allows the task to be reallocated once.

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
