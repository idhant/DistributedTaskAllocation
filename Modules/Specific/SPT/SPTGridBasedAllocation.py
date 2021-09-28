from Modules.Base.GridBasedAllocation import GridBasedAllocation

class SPTGridBasedAllocation(GridBasedAllocation):
    '''Child Class which represents the grid based allocation process specifically for the DBA algorithm'''

    # Main function which the scout robot runs 
    def grid_based_allocation(self, task_list, robot_list, verbose = False):
        
        if(verbose):
            print("") 
            print("*****")
            print("Grid Based Allocation Process")
            print("*****")
            print("")

        if self.check_task_queue(task_list) :

            if (verbose):
                print("Task list is not empty, checking tasks.")

            run = 0
            #while(check_allocation_status(task_list) == False & run < len(task_list) - 1):
            while(run < len(task_list) - 1 ):    
                # Check the first task first, which was found by the scout robot first 
                # first added into the queue -> first sent to the robots 
                for task in task_list :
                    
                    # if task isn`t allocated
                    if (task.taskAllocated == False):

                        zone = task.get_zone()

                        if (verbose):
                            print("")
                            print("-----")
                            print("Checking task: " + str(task.get_task_id()))
                            print("Task zone:  " + str(zone))
                            print("-----")
                            print("")
                            print("Checking for robots in this zone.")
                            print("")

                        # Send this task to all the robots in this zone
                        for robot in robot_list :
                            if robot.get_zone() == zone and task.taskAllocated == False :
                                if (verbose):
                                    print("Robot " + str(robot.get_robot_id()) + " is in Zone: " + str(zone))
                                
                                robot.SPT(task)
                                
                        
                        # Both task and service allocated, do nothing
                        if task.taskAllocated == True :
                            if task.taskService is None or task.taskService.taskAllocated == True :
                                if (verbose):
                                    print("Task: " + str(task.get_task_id()) + " is assigned to Robot: " + str(task.robotAllocated.get_robot_id()))
                                    print("Service of Task: " + str(task.get_task_id()) + " is assigned to Robot: " + str(task.taskService.robotAllocated().get_robot_id()))
                            
                        # Task wasn`t allocated
                        elif task.taskAllocated == False :
                            if (verbose):
                                print("")
                                print("Could not find any robots in the same zone to the task")
                                print("Checking other robots in other zones")

                            robot_zone_list = self.get_robot_zones(robot_list)
                            
                            i = 0
                            for robot_zone in robot_zone_list :
                                if robot_zone != zone :
                                    task_assigned = robot_list[i].SPT(task)
                                    if task_assigned == True :
                                        break
                                i += 1

                run += 1


        else :
            if (verbose):
                print("*****")
                print("Task list is empty, Exiting Application.")
                print("*****")
