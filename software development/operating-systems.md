# Programs, processes, and threads
Programs are made up of processes and threads:
  - A **program** is an executable like chrome.exe
  - A **process** is an executing instance of a program. Double click Google Chrome and you start a process which will run the Google Chrome program.
  - A **thread** is the smallest executable unit of a process. A process can have multiple threads: A single thread is a current tab, and a different thread is another tab.
## Process
A process is a program in execution. Each process is able to run concurrent subtasks called threads.
When loaded into memory it becomes a process, and it can be divided into four sections:
1. Stack
   - Contains temporary data: method/function paramters, return address and local variables
2. Heap
   - Dynamically allocated memory to a process during its run time.
3. Text
   - Program counter.
4. Data
   - Contains global and static variables.
### Process Life Cycle
1. Start
2. Ready
3. Running
4. Waiting
5. Terminated or Exit
### Process Control Block (PCB)
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
## Threads
A thread is a sub-task of processes.
- Multithreading allows for concurrent (simultaenous) execution of two or more parts of a program to maximize utilization of CPU.
- Allows you to write code in one program and listen to music in the other.
### Concurrency
The ability of your program to deal with many things at once, which is achieved through multithreading. 
#### Concurrency vs. Parallelism:
**Concurrency** is dealing with many things at once. **Parallelism** is doing lots of things at once.
- An application can be **concurrent but not parallel** when processes more than one task at same time, but no two tasks execute at the same time.
- An application can be **parallel but not concurrent** when it processes multiple sub-tasks of a task in multi-core CPU at the same time.
- An application can be **neither concurrent nor parallel** when it processes all tasks one at a time (sequentially).
- An application can be **both concurrent and parallel** when it processes multiple tasks concurrently in multi-core CPU at the same time.

**Context switching** is the technique where CPU time is shared accross all running processes and is key for multitasking.
**Thread pools** allow decoupling task submission and execution.
**Locks** are a synchronization technique used to limit access to a resource in an environment where there are many threads of execution. An example of a lock is a **mutex** which is used to guard shared data such as a linked-list, an array, or any simple primitive type. A mutex allows only a single thread to access a resource.
**Thread safety** is a concept that means different threads can access the same resources without exposing erroneous behavior or producing unpredictable results, such as a race condition of deadlock.
- A **deadlock** happens when two or more threads aren't able to many any progress because resource required by first thread is held by the second, and resource required by second is held by first.
    - How to avoid:
        1. Avoid nested locks: Don't give locks to multiple threads.
        2. Avoid unnecessary locks: Reduce the need to lock things.
- A **race condition** is when the threads "race" through the critical section to write or read shared resources and depending on their order in which threads finish the "race" the program output changes, causing the data to be inconsistent.
    - How to avoid: Proper thread synchronization by using techniques such as locks, atomic variables, and message passing.
- **Starvation** is where a thread never gets CPU time or access to shared resources due to other threads hogging resources.
    - How to avoid: Use a **mutex** for granting access to the thread that has been waiting the longest, or **semaphore** for multiple threads.
- A **livelock** happens when two threads keep taking actions in response to the other instead of making progress.
    - Don't block locks: IF a thread can't acquire a lock, it should release previously acquired locks to try again later.
