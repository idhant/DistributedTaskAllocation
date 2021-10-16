# DistributedTaskAllocation

This is the archive repository for the Honor units SIT723/724.

## Centralised Bees Algorithm

The codefiles for sprint-1 which only includes the basic framework and the code for the centralised bees algorithm are placed in the folder "Sprint-1 files ".

The file that will be executed is "CBA.py", the rest of the files are support classes.

It can be executed by running the command `python CBA.py`.

To run the code similar to the test conditions, set modifiers can be changed to handle how many tasks and robots there should be in the system. These creation modifiers are changed in the main function of the CBA.py file, specifically lines 765 and 767. 

### Modifying sets for robots

- To have 5 robots in the system which start with base coordinates we use `create_robots(1)`.
- To have 10 robots in the system which start with base coordinates we use `create_robots(2)`.
- To have 15 robots in the system which start with base coordinates we use `create_robots(3)`.
- To have 5 robots in the system which start with random coordinates we use `create_robots(4)`.
- To have 5 robots in the system which start with random coordinates we use `create_robots(5)`.
- To have 5 robots in the system which start with random coordinates we use `create_robots(6)`.

### Modifying sets for tasks

- To have 5 tasks in the system which start with sample static coordinates we use `create_tasks(1)`.
- To have 10 tasks in the system which start with sample static coordinates we use `create_tasks(2)`.
- To have 15 tasks in the system which start with sample static coordinates we use `create_tasks(3)`.
- To have 5 tasks in the system which start with random  coordinates we use `create_tasks(4)`.
- To have 5 tasks in the system which start with random  coordinates we use `create_tasks(5)`.
- To have 5 tasks in the system which start with random  coordinates we use `create_tasks(6)`.


## Decentralized Bees Algorithm 

The main file for the DBA is the `DBAMain.py` file. It uses basic and specific module classes from the Modules folder.

To run the DBA with different parameters, creation variables can be modified in lines 29 to 45. 

`

    # vars to control file name, location and details
    ALGORITHM = "DBA"
    EXPERIMENT = "2"
    CASE = "1"
    SET = "5"
    RUN = "10"

    # vars to control robot creation
    NUMBER_OF_ROBOTS = 200
    GROUND_ROBOTS = 0
    AERIAL_ROBOTS = 0

    # vars to control task creation
    NUMBER_OF_TASKS = 200
    GROUND_RESCUE = 0
    GROUND_FIREFIGHT = 0
    AERIAL_RESCUE = 0
    AERIAL_FIREFIGHT = 0

`

We can also specify whether we want pre-defined sets of tasks and robots with random coordinates or random sets of tasks and robots with random coordinates.

`

    # Simulate the creation of robots in the system 
    #createVar.create_robot_sets(ROBOT_LIST, NUMBER_OF_ROBOTS, GROUND_ROBOTS, AERIAL_ROBOTS)
    createVar.create_random_robot_sets(ROBOT_LIST, NUMBER_OF_ROBOTS, True, True)

    # Introduce tasks in the system
    #createVar.create_task_sets(TASK_LIST, NUMBER_OF_TASKS, GROUND_RESCUE , GROUND_FIREFIGHT, AERIAL_RESCUE, AERIAL_FIREFIGHT)
    createVar.create_random_task_sets(TASK_LIST, NUMBER_OF_TASKS, True, True)

`

After modification of these parameters,  It can be executed by running the command `python DBAMain.py`. Its important to note that if the creation variables for the output.txt files are changed, some of the files in the test folder can be overwritten. These files are used to create the graphs in the research paper and thesis.

### Modules used

In the Modules/Base sub folder we have the basic classes that are used by the framework. Some Classes from the Modules/Specific/DBA are also used by the `DBAMain.py` file.

- Coordinate Class: This class deals with the coordinates and zones of the tasks/robots in the system. 

- DBARobot Class: Specific class titled `DBARobot.py` is used by the `DBAMain.py` file to handled robots in the system. This is the class where the code for individual robot DB Algorithm is present.

- Task Class: Base class titled `Task.py` handles the task in the system.

- DBACreate Class: Specific class titled `DBACreate.py` handles the creation of both the tasks and robots in the system.

- DBAGridBasedAllocation Class: Specific class titled `DBAGridBasedAllocation.py` handles the grid-based allocation process for this algorithm.

- Print Class: This base class is used to print out the experiment results for sets of robots and tasks defined.

## S+T Algorithm

The main file for the S+T is the `SPTMain.py` file. It uses basic and specific module classes from the Modules folder.

To run the SPT with different parameters, creation variables can be modified in lines 23 to 44. 

`

    # vars to control file name, location and details
    ALGORITHM = "SPT"
    EXPERIMENT = "1"
    CASE = "1"
    SET = "1"
    RUN = "2"

    # vars to control robot creation
    NUMBER_OF_ROBOTS = 2
    GROUND_ROBOTS = 0
    AERIAL_ROBOTS = 0

    # vars to control task creation
    NUMBER_OF_TASKS = 2
    GROUND_RESCUE = 0
    GROUND_FIREFIGHT = 0
    AERIAL_RESCUE = 0
    AERIAL_FIREFIGHT = 0
    
    NUMBER_OF_SERVICES = 1
    GROUND_SERVICES = 0
    AERIAL_SERVICES = 0

`

We can also specify whether we want pre-defined sets of tasks and robots with random coordinates or random sets of tasks and robots with random coordinates.

`

    # Simulate the creation of robots in the system 
    #createVar.create_robot_sets(ROBOT_LIST, NUMBER_OF_ROBOTS, GROUND_ROBOTS, AERIAL_ROBOTS)
    createVar.create_random_robot_sets(ROBOT_LIST, NUMBER_OF_ROBOTS, True, True)

    # Introduce tasks in the system
    #createVar.create_task_sets(TASK_LIST, NUMBER_OF_TASKS, GROUND_RESCUE , GROUND_FIREFIGHT, AERIAL_RESCUE, AERIAL_FIREFIGHT, NUMBER_OF_SERVICES, GROUND_SERVICES, AERIAL_SERVICES)
    createVar.create_random_task_sets(TASK_LIST, NUMBER_OF_TASKS, True, True, NUMBER_OF_SERVICES, True, True)


`

After modification of these parameters,  It can be executed by running the command `python SPTMain.py`. Its important to note that if the creation variables for the output.txt files are changed, some of the files in the test folder can be overwritten. These files are used to create the graphs in the research paper and thesis.

### Modules used

In the Modules/Base sub folder we have the basic classes that are used by the framework. Some Classes from the Modules/Specific/DBA are also used by the `SPTMain.py` file.

- Coordinate Class: This class deals with the coordinates and zones of the tasks/robots in the system. 

- SPTRobot Class: Specific class titled `SPTRobot.py` is used by the `SPTMain.py` file to handled robots in the system. This is the class where the code for individual robot SPT Algorithm is present.

- SPTTask Class: Specific class titled `SPTTask.py` handles the task in the system.

- SPTCreate Class: Specific class titled `SPTCreate.py` handles the creation of both the tasks and robots in the system.

- SPTGridBasedAllocation Class: Specific class titled `SPTGridBasedAllocation.py` handles the grid-based allocation process for this algorithm.

- SPTPrint Class: This Specific class is used to print out the experiment results for sets of robots and tasks defined.