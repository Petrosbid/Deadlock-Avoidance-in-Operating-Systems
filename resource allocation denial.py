from colorama import Fore

# دریافت اطلاعات
processes = int(input(Fore.MAGENTA + "number of processes : "))
resources = int(input("number of resources : "))
max_resources = [int(i) for i in input("maximum resources : ").split()]

print(Fore.CYAN + "\n---- allocated resources for each process ----")
currently_allocated = [[int(i) for i in input(Fore.LIGHTMAGENTA_EX + f"process {j + 1} : ").split()] for j in range(processes)]

print(Fore.CYAN +"\n---- maximum resources for each process ----")
Max = [[int(i) for i in input(Fore.LIGHTMAGENTA_EX + f"process {j + 1} : ").split()] for j in range(processes)]

# محاسبه منابع تخصیص داده شده
allocation = [0] * resources
for i in range(processes):
    for j in range(resources):
        allocation[j] += currently_allocated[i][j]
print(Fore.YELLOW+ f"\ntotal allocated resources : {allocation}")

# محاسبه منابع موجود
Available = [max_resources[i] - allocation[i] for i in range(resources)]
print(f"total available resources : {Available}\n")

# محاسبه ماتریس نیاز
NEED = [[Max[i][j] - currently_allocated[i][j] for j in range(resources)] for i in range(processes)]
print(Fore.CYAN + "\n---- NEED matrix ----")
for i in range(processes):
    print(f"process {i + 1} : {NEED[i]}")

# بررسی ایمنی سیستم
running = [True] * processes
count = processes
while count != 0:
    safe = False
    for i in range(processes):
        if running[i]:
            executing = True
            for j in range(resources):
                if NEED[i][j] > Available[j]:
                    executing = False
                    break
            if executing:
                print(Fore.CYAN + f"\nprocess {i + 1} is executing")
                running[i] = False
                count -= 1
                safe = True
                for j in range(resources):
                    Available[j] += currently_allocated[i][j]
                break
    if not safe:
        print(Fore.RED + "\nthe processes are in an unsafe state.")
        break

    print(Fore.GREEN + f"the process is in a safe state.\navailable resources : {Available}")
