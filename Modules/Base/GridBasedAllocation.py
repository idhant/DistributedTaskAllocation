class GridBasedAllocation():
    '''Class which represents the grid based allocation process the scout robot follows'''

    # Function to check if the task queue is empty or not 
    def check_task_queue(self, task_list):
        if len(task_list) > 0 :
            return True
        else:
            return False

    # Function to check if all tasks are allocated
    def check_allocation_status(self, task_list):
        for task in task_list:
            if task.taskAllocated == False:
                return False
        return True

    # Function to return a list with the respective robot zones as the elements
    def get_robot_zones(self, robot_list):
        robot_zone_list = []

        for robot in robot_list :
            zone = robot.get_zone()
            robot_zone_list.append(zone)

        return robot_zone_list

