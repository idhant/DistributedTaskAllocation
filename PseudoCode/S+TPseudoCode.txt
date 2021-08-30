def SPT(task):

    bids = []

    capability = checkCapability(task)

    if capability is True:
        busyStatus = checkStatus()

        if busyStatus is False:
            distance = calculateDistance(task)
            quality = task.getQuality()
            utility = quality - distance 
            
            if task.requireService() is True:
                bids.append(utility)

                # function which sends the task to other robots
                # to find robot which can complete the service first
                broadcastTasktoOtherRobots(getCurrentRobot, task)

            else:
                assignTask(task)
                return True

        else:
            current_task_quality = getTaskAssigned().getQuality()
            new_task_quality = task.getQuality()

            if (new_task_quality - current_task_quality > differential_factor):
                distance = calculateDistance(task)
                quality = task.getQuality()
                utility = quality - distance 

                if task.requireService() is True:
                    bids.append(utility)
                    
                    # function which sends the task to other robots
                    # to find robot which can complete the service first
                    broadcastTasktoOtherRobots(getCurrentRobot, task)

                else:
                    assignTask(task)
                    return True

            else:
                return False      

    else:
        return False       