# Processes
A process is a program in execution.
When loaded into memory it becomes a process, and it can be divided into four sections:
1. Stack
   - Contains temporary data: method/function paramters, return address and local variables
2. Heap
   - Dynamically allocated memory to a process during its run time.
3. Text
   - Program counter.
4. Data
   - Contains global and static variables.
## Process Life Cycle
1. Start
2. Ready
3. Running
4. Waiting
5. Terminated or Exit
## Process Control Block (PCB)
- C
- Dependent on OS
- Maintained for lifetime of process
- Deleted once process terminates
1. Process State
2. Process privileges
3. Process ID
4. Pointer
5. Program Counter
6. CPU registers
7. CPU scheduling information
8. Memory management information
9. Accounting information
10. IO status information
    

# Threads
- Multithreading allows for concurrent (simultaenous) execution of two or more parts of a program to maximize utilization of CPU.
- Allows you to write code in one program and listen to music in the other.
- Programs are made up of processes and threads:
  - A **program** is an executable like chrome.exe
  - A **process** is an executing instance of a program.
  - A **thread** is the smallest executable unit of a process.

# Concurrency

# Locks

# Mutexes

# Semaphores

# Monitors

