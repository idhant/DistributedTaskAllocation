from Modules.Base.Print import Print

class SPTPrint(Print):
    '''Child class to print related functions in SPT algorithm'''

    # Function to print all the robot details in the system
    def print_robot_details(self, robot_list):
        print("")
        print("*****")
        print("Robot Details in the system:")
        print("*****")
        print("")
        for robot in robot_list:
            print("*****")
            print("Robot ID: " + str(robot.get_robot_id())) 
            print("Robot Type: " + robot.get_robot_type()) 
            print("Robot Location: ")
            print("X: " + str(robot.get_robot_location().get_x_coordinate()))
            print("Y: " + str(robot.get_robot_location().get_y_coordinate()))
            print("Z: " + str(robot.get_robot_location().get_z_coordinate()))
            print("Robot Zone: " + str(robot.get_zone()))
            print("Robot Task Capabilities: ")
            for capability in robot.get_is_capable():
                print(capability)
            print("Robot Status: " + str(robot.get_robot_status()))
            if(robot.get_assigned_task() != -1):
                print("Robot is allocated to task: " + str(robot.get_assigned_task().get_task_id()))
            if(robot.get_assigned_task() == -1):
                print("Robot is not allocated any task.")
            if(robot.get_assigned_service() != -1):
                print("Robot is allocated to a service task : " + str(robot.get_assigned_service().get_task_id()))
            if(robot.get_assigned_service() == -1):
                print("Robot is not allocated to any service task.")
            print("*****")
            print("")

    # Function to print all the task details in the system
    def print_task_details(self, task_list):
        print("")
        print("*****")
        print("Task Details in the system:")
        print("*****")
        print("")
        for task in task_list:
            print("*****")
            print("Task ID: " + str(task.get_task_id()))
            print("Task Type: " + task.get_task_type())
            print("Task Quality: "+ str(task.get_task_quality()))
            print("Task Location: ")
            print("X: " + str(task.get_task_location().get_x_coordinate()))
            print("Y: " + str(task.get_task_location().get_y_coordinate()))
            print("z: " + str(task.get_task_location().get_z_coordinate()))
            print("Task Zone: " + str(task.get_zone()))
            print("Task Time Added: " + str(round(task.get_time_added(), 4)) )
            print("Task Allocated: " + str(task.taskAllocated))
            if(task.taskAllocated):
                print("Robot Allocated to this task: " + str(task.robotAllocated.get_robot_id()))
                print("Time Allocated: " + str(round(task.timeAllocated, 4)) )
                print('Time Taken to allocate: ' + str(round(task.get_time_taken_to_allocate(), 4)) )
                print("Times Reallocated: " + str(task.timesReallocated))
                print("Time Consumed in reallocations: " + str(round(task.timeDeallocated, 4)) )
            
            print("")
           
            print("Service Required: " + str(task.service_required()) )
            if(task.service_required()):
                service = task.taskService
                print("Service Task ID: " + str(service.get_task_id()))
                print("Service Task Type: " + service.get_task_type())
                print("Service Task Quality: "+ str(service.get_task_quality()))
                print("Service Task Location: ")
                print("X: " + str(service.get_task_location().get_x_coordinate()))
                print("Y: " + str(service.get_task_location().get_y_coordinate()))
                print("z: " + str(service.get_task_location().get_z_coordinate()))
                print("Service Task Zone: " + str(service.get_zone()))
                print("Service Task Time Added: " + str(round(service.get_time_added(), 4)) )

            print("*****")
            print("")

    # Function to print allocations
    def print_task_allocations(self, task_list):
        print("")
        print("*****")
        print("Task Allocations")
        print("*****")
        print("")
        for task in task_list:
            if(task.get_robot_id() != -1):
                print("Task: " + str(task.get_task_id()) + " is assigned to robot " + str(task.get_robot_id()))
            else:
                print("Task: " + str(task.get_task_id()) + " could not be assigned to any robot in the first run.")

    # function to print the global and local runtime of the algorithm
    def print_time_taken_to_allocate(self, task_list):
        print("")
        print("*****")
        print("Time taken to allocate tasks:")
        print("*****")
        print("")

        print("Time taken to allocate for particular tasks:")
        print("")

        total_time = 0
        time_wasted = 0
        reallocations_performed = 0
        
        for task in task_list:
            
            # Task Allocated
            if task.taskAllocated :

                if task.timesReallocated > 0 :
                    reallocations_performed += 1
                    print("Task " + str(task.get_task_id()) + " was deallocated " + str(task.timesReallocated) + " times")
                    print("Time wasted on deallocation " + str(round(task.get_time_wasted_on_dealloaction(), 4)) + " seconds")
                    print("Time taken to allocate task-" + str(task.get_task_id())  + " was " + str(round(task.get_time_taken_to_allocate(), 4)) + " seconds")
                    total_time += task.get_time_taken_to_allocate()
                    time_wasted += task.get_time_wasted_on_dealloaction()

                else:
                    print("Time taken to allocate task-" + str(task.get_task_id())  + " was " + str(round(task.get_time_taken_to_allocate(), 4)) + " seconds")
                    total_time += task.get_time_taken_to_allocate()

            # Task not allocated
            else:
                if task.timesReallocated > 0 :
                    reallocations_performed += 1
                    print("Task was allocated but deallocated later")
                    print("Task " + str(task.get_task_id()) + " was deallocated " + str(task.timesReallocated) + " times")
                    print("Time wasted on deallocation " + str(task.get_time_wasted_on_dealloaction()))
                    total_time += task.get_time_wasted_on_dealloaction()
                    time_wasted += task.get_time_wasted_on_dealloaction()
                else:
                    print("Task was never allocated")

        
        print("")
        print("Total time taken to allocate all the tasks was " + str(round(total_time, 4)) + " seconds.")
        print("")
        print("Reallocations were performed " + str(reallocations_performed) + " times in total.")
        print("")
        print("Time consumed in reallocation of the the tasks was " + str(round(time_wasted, 4)) + " seconds.")
        print("")

