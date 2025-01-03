from colorama import Fore

# Input the number of processes and resources
processes = int(input(Fore.MAGENTA + "number of processes : "))
resources = int(input("number of resources : "))

# Input the total maximum resources available in the system
max_resources = [int(i) for i in input("maximum resources : ").split()]

# Input the maximum resource demand for each existing process
print(Fore.CYAN + "\n---- maximum resources for each process ----")
Max = [[int(i) for i in input(Fore.LIGHTMAGENTA_EX + f"process {j + 1} : ").split()] for j in range(processes)]

# Input the maximum resource demand for the new process
new_processes = list(map(int, input(Fore.MAGENTA + "\nmaximum resources for new process : ").split()))

# Calculate the total allocated resources
column_sums = [0] * resources
for row in Max:
    for j in range(resources):
        column_sums[j] += row[j]

# Calculate the available resources
Available = [max_resources[i] - column_sums[i] for i in range(resources)]
print(f"total available resources : {Available}\n")

# Check if the new process can safely enter the system
safe = True
for i in range(len(Available)):
    if Available[i] < new_processes[i]:  # If available resources are less than required
        safe = False
        break
if safe:
    print(Fore.GREEN + "Process can enter!")
else:
    print(Fore.RED + "Process can't enter!")