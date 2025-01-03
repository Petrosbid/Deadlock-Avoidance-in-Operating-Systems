from colorama import Fore

# دریافت اطلاعات
processes = int(input(Fore.MAGENTA + "number of processes : "))
resources = int(input("number of resources : "))
max_resources = [int(i) for i in input("maximum resources : ").split()]

print(Fore.CYAN +"\n---- maximum resources for each process ----")
Max = [[int(i) for i in input(Fore.LIGHTMAGENTA_EX + f"process {j + 1} : ").split()] for j in range(processes)]
new_processes = list(map(int , input(Fore.MAGENTA + "\nmaximum resources for new process : ").split()))

# 
column_sums = [0] * resources
for row in Max:
    for j in range(resources):
        column_sums[j] += row[j]


# محاسبه منابع موجود
Available = [max_resources[i] - column_sums[i] for i in range(resources)]
print(f"total available resources : {Available}\n")

# بررسی ایمنی سیستم
safe = True
for i in range(len(Available)):
    if(Available[i] < new_processes[i]): 
        safe = False
        break
if safe:
    print(Fore.GREEN + "Process can enter!")
else:
    print(Fore.RED + "Process can't enter!")