import random
import math
from collections import namedtuple

# Define the task structure
Task = namedtuple('Task', ['C', 'D', 'T', 'L'])

def generateTaskFromUtilization(UtilizationSet):
    taskList = []
    utilizations = []
    for util in UtilizationSet:
        # Generate period (T), execution time (C), and deadline (D)
        T = random.randint(10, 70)
        C = math.ceil(T * util)  # Execution time is proportional to period and utilization
        D = T  # Deadline equals period for simplicity
        L = []  # Untrusted list is empty for now
        taskList.append(Task(C, D, T, L))
        utilizations.append(util)
    return taskList, utilizations

def uunifast(n, U):
    vectU = []
    sumU = U
    for i in range(1, n):
        nextSumU = sumU * (random.uniform(0, 1)**(1/(n-i)))
        vectU.append(sumU - nextSumU)
        sumU = nextSumU
    vectU.append(sumU)
    AllSum = sum(vectU)

    return AllSum, vectU

def uunifasts(N, n, U):
    taskSets = []
    utilizationsSets = []
    counter = 1
    while counter <= N:
        Sum, Vect = uunifast(n, U)
        # Due to rounding errors, utilization may not be exactly equal to U
        if math.isclose(Sum, U, rel_tol=1e-9):
            # Generate the task set from the utilization vector
            taskSet, utilizations = generateTaskFromUtilization(Vect)
            taskSets.append(taskSet)
            utilizationsSets.append(utilizations)
            counter += 1
    return taskSets, utilizationsSets

def write_tasks_to_file(taskSets, utilizationsSets, filename="task_sets.txt"):
    with open(filename, 'w') as file:
        for i, (taskSet, utilizations) in enumerate(zip(taskSets, utilizationsSets)):
            file.write(f"Task Set {i+1}:\n")
            file.write(f"Utilizations: {utilizations}\n")
            for task in taskSet:
                file.write(f"Period: {task.T}, Execution: {task.C}, Deadline: {task.D}, L: {task.L}\n")
            file.write("\n")

# Run the UUniFast algorithm
#RUN = 3   # Number of times to run the UUniFast algorithm
#JOB_NUMBERS = 3  # Number of tasks in each set
#UTILIZATION = 0.4  # Desired total utilization

# Generate task sets
#taskSets, utilizationsSets = uunifasts(RUN, JOB_NUMBERS, UTILIZATION)

