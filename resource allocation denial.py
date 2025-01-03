from colorama import Fore

# Input the number of processes and resources
processes = int(input(Fore.MAGENTA + "number of processes : "))
resources = int(input("number of resources : "))

# Input the total maximum resources available in the system
max_resources = [int(i) for i in input("maximum resources : ").split()]

# Input the resources currently allocated to each process
print(Fore.CYAN + "\n---- allocated resources for each process ----")
currently_allocated = [[int(i) for i in input(Fore.LIGHTMAGENTA_EX + f"process {j + 1} : ").split()] for j in range(processes)]

# Input the maximum resource demand for each process
print(Fore.CYAN + "\n---- maximum resources for each process ----")
Max = [[int(i) for i in input(Fore.LIGHTMAGENTA_EX + f"process {j + 1} : ").split()] for j in range(processes)]

# Calculate the total allocated resources
allocation = [0] * resources
for i in range(processes):
    for j in range(resources):
        allocation[j] += currently_allocated[i][j]
print(Fore.YELLOW + f"\ntotal allocated resources : {allocation}")

# Calculate the available resources
Available = [max_resources[i] - allocation[i] for i in range(resources)]
print(f"total available resources : {Available}\n")

# Calculate the "Need" matrix
NEED = [[Max[i][j] - currently_allocated[i][j] for j in range(resources)] for i in range(processes)]
print(Fore.CYAN + "\n---- NEED matrix ----")
for i in range(processes):
    print(f"process {i + 1} : {NEED[i]}")

# Check system safety using the Banker's Algorithm
running = [True] * processes
count = processes
while count != 0:
    safe = False
    for i in range(processes):
        if running[i]:
            executing = True
            for j in range(resources):
                if NEED[i][j] > Available[j]:  # If needs exceed available resources
                    executing = False
                    break
            if executing:
                print(Fore.CYAN + f"\nprocess {i + 1} is executing")
                running[i] = False
                count -= 1
                safe = True
                for j in range(resources):
                    Available[j] += currently_allocated[i][j]  # Release resources after execution
                break
    if not safe:
        print(Fore.RED + "\nthe processes are in an unsafe state.")
        break

print(Fore.GREEN + f"the process is in a safe state.\navailable resources : {Available}")