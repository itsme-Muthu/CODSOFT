<h2> Task 1: To Do List </h2>

The provided Python program is a command-line based To-Do List application that uses binary file handling with the pickle module to store and manage tasks. Below is a brief description of its functionality:

---

Functions:

<h3> insertTask() </h3>

- Prompts the user to enter a task description.
- Appends the new task to the binary file todolist.dat with a status of "Not Done" and an incremented serial number.

<h3> findSerialNo() </h3>

- Reads the binary file to determine the current highest serial number of the tasks.
- Returns the next serial number to be assigned to a new task.

<h3> displayTasks() </h3>

- Reads and displays all tasks from the binary file in a formatted table.

<h3> updateTask(taskNumber) </h3>

- Prompts the user to enter a new description for a specific task identified by its serial number.
- Updates the task in the binary file if found, otherwise prints an error message.

<h3> deleteTask(taskNumber) </h3>

- Deletes a specific task identified by its serial number from the binary file.
- Reassigns serial numbers to maintain sequence after deletion.
- Prints a confirmation message if the task is deleted, otherwise prints an error message.

<h3>TaskCompleted(taskNumber) </h3>

Marks a specific task identified by its serial number as "Done" in the binary file.
Prints a confirmation message if the task is marked as complete, otherwise prints an error message.

<h3> main() </h3>

Displays a menu of options for the user to interact with the to-do list.
Calls the appropriate function based on the user's choice.
Allows the user to add, view, update, delete tasks, mark tasks as complete, or exit the program.
The program continuously runs in a loop, displaying the menu and performing the corresponding operations until the user chooses to exit.
