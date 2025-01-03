# Deadlock Avoidance in Operating Systems

## Introduction
Deadlock avoidance is a crucial aspect of operating system design, ensuring that processes can access shared resources without entering a state where no progress is possible. Two common strategies for avoiding deadlocks are:

1. **Process Initiation Denial**: A process is only allowed to start if the system can guarantee that it won't lead to an unsafe state.
2. **Resource Allocation Denial (Banker's Algorithm)**: Resources are allocated dynamically in such a way that the system remains in a safe state.

This repository contains Python implementations for both strategies, using interactive input and color-coded outputs for a better user experience.

---

## Files in This Repository

1. **`process_initiation_denial.py`**: Implements the Process Initiation Denial method.
2. **`bankers_algorithm.py`**: Implements the Resource Allocation Denial (Banker's Algorithm).

---

## How It Works

### 1. Process Initiation Denial
This script ensures that a new process can only begin if it does not lead the system into an unsafe state. The algorithm checks if the available resources are sufficient for the new process's maximum requirements.

#### Input
- Number of processes
- Number of resource types
- Total maximum resources available in the system
- Maximum resource demand for each existing process
- Maximum resource demand for the new process

#### Output
- Total available resources
- Whether the new process can safely enter the system

#### Example Screenshot
![IMG_20241206_211707_774](https://github.com/user-attachments/assets/77d30986-c3eb-4626-ac9a-ee6403583877)
![IMG_20241206_211707_522](https://github.com/user-attachments/assets/b45562ca-76df-4d83-b72c-93b1bd7729b5)

---

### 2. Resource Allocation Denial (Banker's Algorithm)
This script allocates resources to processes in a way that guarantees the system remains in a safe state. It uses the Banker's Algorithm to calculate the need matrix and determines the safety of the system.

#### Input
- Number of processes
- Number of resource types
- Total maximum resources available in the system
- Resources currently allocated to each process
- Maximum resource demand for each process

#### Output
- Total allocated resources
- Total available resources
- The "Need" matrix
- Execution order of processes, if safe
- Whether the system is in a safe or unsafe state

#### Example Screenshot
![Screenshot 2024-12-06 193710](https://github.com/user-attachments/assets/b6d94d9c-80fd-4dcf-90f6-c19a7a8db809)
![Screenshot 2024-12-06 193535](https://github.com/user-attachments/assets/ccc3ef84-a0bb-4fce-82fa-4184286ed0be)


---

## Key Features
- Interactive input prompts with color-coded guidance using the `colorama` library.
- Real-time calculations of available resources and safety state.
- Modular and readable Python code for educational purposes.

---

## Requirements
- Python 3.6+
- `colorama` library (Install using `pip install colorama`)

---

## Running the Scripts

### Process Initiation Denial
```
python process_initiation_denial.py
```

### Banker's Algorithm
```
python bankers_algorithm.py
```

---

## Understanding Deadlock Avoidance
Deadlock occurs when processes in a system are unable to proceed because each is waiting for resources held by others. Avoiding deadlock is essential for maintaining system stability and efficiency.

- **Safe State**: A state where the system can allocate resources to each process in some order and still avoid deadlock.
- **Unsafe State**: A state where there is a potential for deadlock.

Both strategies implemented here ensure that the system operates in a safe state.

---

## Contributions
Contributions to improve the scripts or extend their functionality are welcome. Please open an issue or submit a pull request.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Keywords
`Deadlock Avoidance`, `Banker's Algorithm`, `Process Initiation Denial`, `Operating Systems`, `Python`, `Resource Management`

