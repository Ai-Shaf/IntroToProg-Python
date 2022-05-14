# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# AShafique,05.13.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

# Read/load data from file
try:     # if file exists
    objToDo = open(objFile, "r")
    for row in objToDo:
        task, priority = row.split(",")
        dicRow = {"Task": task, "Priority": priority.strip()}
        lstTable.append(dicRow)
    objToDo.close()
except:       # if file does not exist
    print("File not found. You can create a new file when you save.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here - Show current Data
        print("Task" + "  |  " + "Priority")
        for row in lstTable:
            print(row["Task"].title() + "|" + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here - Add New Item
        strTask = input("Enter Task to be Added: ")
        strPriority = input("Enter Priority Number of Added Task: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Your item was added to the list.")
        print("Task" + "  |  " + "Priority")
        for row in lstTable:
            print(row["Task"].title() + "|" + row["Priority"])
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here - Remove an Existing Item
        strRemove = input("Which task do you want to remove? ")
        strRemove = strRemove.strip()
        intAbsent = 1               # intializing variable to capture if strRemove is not present 0/1
        for row in lstTable:
            if row["Task"].lower() == strRemove.lower():
                intAbsent= intAbsent*0
                lstTable.remove(row)
                print(strRemove.title() + " was removed. Updated list below.")
            else:
                absent =intAbsent*1
        if intAbsent == 1:
            print("Task not found. See below for updated list of tasks.")
        # Show updated list or remind user of existing items
        print("Task" + "  |  " + "Priority")
        for row in lstTable:
            print(row["Task"].title() + "|" + row["Priority"])

        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here - Save tasks to ToDoList
        objToDo = open(objFile, "w")
        for row in lstTable:
            objToDo.write(row["Task"] + ',' + row["Priority"] + '\n')
        objToDo.close()
        print("Tasks Saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here --Exit Program
        print("You are exiting the program.")
        break  # and Exit the program
    # Catch for errors in strChoice input
    else:
        print("Input not recognized. Please choose numbers 1, 2, 3, 4, or 5.")

