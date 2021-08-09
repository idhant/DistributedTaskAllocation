def DBA(task):

    if task is not None:
        capability = checkCapability(task)

        if capability is True:
            busyStatus = checkStatus()

            if busyStatus is False:
                distance = calculateDistance(task)
                quality = task.getQuality()
                # Value recorded to compare optimization results
                utility = quality - distance 
                return True

            else:
                current_task_quality = getTaskAssigned().getQuality()
                new_task_quality = task.getQuality()

                # quality factor is a threshold value which decides if one task can 
                # supercede the other task
                if (new_task_quality - current_task_quality > differential_factor):
                    distance = calculateDistance(task)
                    quality = task.getQuality()
                    utility = quality - distance 
                    return True

                else:
                    return False      

        else:
            return False       