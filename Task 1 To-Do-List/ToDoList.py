# To Do List in Python using File handling (Binary File)

import pickle

# insert a new task
def insertTask():
    description = input("Enter the description of the task: ")
    file = open("C:/Users/Admin/Downloads/todolist.dat","ab")
    length = findSerialNo()
    record = {"sno":length+1,"description":description,"status":"Not Done"}
    
    pickle.dump(record,file)
    print("The Task has been added")
    file.close()

def findSerialNo():
    file = open("C:/Users/Admin/Downloads/todolist.dat","rb")
    serial = 0
    while True:
        try:
            rec = pickle.load(file)
            serial+=1
        except EOFError:
            break
    file.close()
    return serial

# view to-do list
def displayTasks():
    file = open("C:/Users/Admin/Downloads/todolist.dat","rb")
    print("{:<30}".format("List of Tasks"))
    print("------------------------------------------------------------")
    print("{:<7} {:<30} {:10}".format("S.NO","Task","Status"))
    print("------------------------------------------------------------")
    while True:
        try:
            record = pickle.load(file)
            print("{:<7} {:<30} {:10}".format(record["sno"],record["description"],record["status"]))
        except EOFError:
            break
    file.close()

# update the task
def updateTask(taskNumber):
    file = open("C:/Users/Admin/Downloads/todolist.dat","rb")
    rec = []
    updated = False
    while True:
        try: 
            record = pickle.load(file)
            rec.append(record)
        except EOFError:
            break
    file.close()
    

    for i in range(len(rec)):
        if rec[i]["sno"]==taskNumber:
            newtask = input("Enter the description for the new task: ")
            rec[i]["description"] = newtask
            print("The task has been updated")
            updated = True
    if updated == False:
        print("Invalid task Number!")
    file = open("C:/Users/Admin/Downloads/todolist.dat","wb")
    for x in rec:
        pickle.dump(x,file)
    file.close()

# delete the task
def deleteTask(taskNumber):
    file = open("C:/Users/Admin/Downloads/todolist.dat","rb")
    rec = []
    deleted = False
    while True:
        try:
            record = pickle.load(file)
            rec.append(record)
        except EOFError:
            break
    file.close()
    file = open("C:/Users/Admin/Downloads/todolist.dat","wb")
    sno = 1
    for x in rec:
        if x["sno"]==taskNumber:
            print("The task has been deleted")
            deleted = True
            continue
        x["sno"] = sno
        sno+=1
        pickle.dump(x,file)
    
    if deleted == False:
        print("Invalid Task Number")
    file.close()

# Mark as Completed
def TaskCompleted(taskNumber):
    file = open("C:/Users/Admin/Downloads/todolist.dat","rb")
    rec = []
    completed = False
    while True:
        try:
            record = pickle.load(file)
            rec.append(record)
        except EOFError:
            break
    file.close()
    for x in rec:
        if x["sno"]==taskNumber:
            x["status"]="Done"
            print("The task has been marked done")
            completed = True
    if completed == False:
        print("Invalid task Number!")

    file = open("C:/Users/Admin/Downloads/todolist.dat","wb")
    for x in rec:
        pickle.dump(x,file)
    file.close()

def main():
    while True:
        print("==========================================================================")
        print('Option Available: ')
        print("==========================================================================")
        print("1. Add task ")
        print("2. View To-Do List")
        print("3. Update task ")
        print("4. Delete task")
        print("5. Mark task as Complete ")
        print("6. Exit")
        print("==========================================================================")

        choice = int(input("Enter the choice (1/2/3/4/5/6): "))

        if choice == 1:
            insertTask()

        elif choice == 2:
            displayTasks()

        elif choice == 3:
            displayTasks()
            print("------------------------------------------------------------")
            taskNumber = int(input("Enter the task Number: "))
            updateTask(taskNumber)

        elif choice == 4:
            displayTasks()
            print("------------------------------------------------------------")
            taskNumber = int(input("Enter the task Number to be deleted: "))
            deleteTask(taskNumber)

        elif choice == 5:
            displayTasks()
            print("------------------------------------------------------------")
            taskNumber = int(input("Enter the task number to mark as complete: "))
            TaskCompleted(taskNumber)

        elif choice == 6:
            print("==========================================================================")
            print("You have exited from To-Do List")
            print("Thank you!")
            print("==========================================================================")
            break

main()
         