# This will allow you to get todays date.
import datetime
from datetime import date
from dateutil import parser

# Open the files to be used in read and write.
user_file = open('user.txt', 'r+')
tasks_file = open('tasks.txt', 'r+')

# Extract username and password information from user.txt and
# store it in a dictionary.

user_details = {}

for user_contents in user_file:
        # This will remove all the white spaces '\n' from user contents
        user_contents = user_contents.strip().split(", ")
        user_details[user_contents[0]] = user_contents[1]

# =======================================================================
# CHECK USERNAME AND PASSWORD
entered_username = ""
entered_password = ""
flag = False

# Check whether the entered information matches any username and
# password pair in the created dictionary.
# Please note that all information requested from the user is converted to
# lower case letters for more user friendliness.

while flag == False:
    entered_username = input("Please enter your username: ").lower()
    entered_password = input("Please enter your password: ")
    
    if entered_username in user_details.keys():
        if entered_password == user_details[entered_username]:
            flag = True
            break
        else:
            print("The username is correct but the password is incorrect")
            flag = False
    elif entered_username not in user_details.keys():
        if entered_password in user_details.values():
            print("The username is incorrect but the password is correct")
            flag = False
        else:
            print("The username and password are incorrect.")
            flag = False
        
# =======================================================================
# DEFINE FUNCTIONS TO BE USED

# View and edit my tasks
def view_mine():
        new_file_contents = ''
        count_lines = 0
        a = []
        with open("tasks.txt", "r") as file:
            # Count how many lines the file has
            for j in file:
                if j != "\n":
                    count_lines += 1
        task_list = []
        with open("tasks.txt", "r") as file:
            # Loop through the whole file checking for the username (first name in each line)
            while count_lines > 0:
                task_counter = 0
                for i in file:
                    task_counter += 1
                    count_lines -= 1
                    a = i.split(", ")[0]
                    if a == entered_username:
                        task_list = i.split(", ")
                        print("\nTask number", task_counter)
                        print("\nAssigned:", task_list[0])
                        print("Task:", task_list[1])
                        print("Description:", task_list[2])
                        print("Due date:", task_list[3])
                        print("Date assigned:", task_list[4])
                        print("Completed:", task_list[5] + "\n")

        # Edit task or go back to main menu
        print("Enter the number for the task you would like to edit, or -1 for the main menu")
        edit_task = int(input("Enter number: "))
        #print("Are you editing the task or its completion status?")
        #edit_what = input("Enter 'task' or 'status': ")

        
        if edit_task == -1:
            if entered_username == 'admin':
                admin_menu()
            else:
                none_admin_menu()

        else:
            print("Are you editing the task or marking it as complete?")
            action = input("Enter 'edit' or 'mark': ")
            if action == 'edit':
                    print("Edit task", edit_task)
                    print("Are you editing the username or the due date?")
                    which_part = input("Enter 'username' or 'date': ")
                    with open('tasks.txt', 'r+') as file:
                        counter = 0
                        new_file_contents = ''
                        if which_part == 'username':
                            for line in file:
                                counter += 1
                                if counter == edit_task and line.split(", ")[0] == entered_username and line.split(", ")[5].strip("\n") == 'No':
                                    # Replace the first occurance of the username
                                    new_username = input("Enter the new username: ")
                                    new_line = line.replace(entered_username, new_username, 1)
                                    new_file_contents += new_line
                                    print("Task", counter, "has been assigned to", new_username)

                                elif counter == edit_task and line.split(", ")[0] == entered_username and line.split(", ")[5].strip("\n") == 'Yes':
                                    print("The task has been completed. It cannot be edited")
                                    new_file_contents += line

                                elif counter == edit_task and line.split(", ")[0] != entered_username:
                                    print("This is not your task, you cannot edit it")
                                    new_file_contents += line

                                else:
                                    new_file_contents += line
                                    
                            # Clear the file and then write the new information with the changed username
                            file.seek(0)
                            file.truncate()
                            file.write(new_file_contents)


                        elif which_part == 'date':
                            for line in file:
                                counter += 1
                                if counter == edit_task and line.split(", ")[0] == entered_username and line.split(", ")[5].strip("\n") == 'No':
                                    ### The following line doesn't change element [0] of the list to the new username
                                    print("Enter date in the format 'dd Mon yyyy'")
                                    new_date = input("Enter the new due date: ")
                                    new_line = line.replace(line.split(", ")[3], new_date, 1)
                                    new_file_contents += new_line
                                    print("The due date for task", counter, "has been updated")

                                elif counter == edit_task and line.split(", ")[0] == entered_username and line.split(", ")[5].strip("\n") == 'Yes':
                                    print("The task has been completed. It cannot be edited")
                                    new_file_contents += line

                                elif counter == edit_task and line.split(", ")[0] != entered_username:
                                    print("This is not your task, you cannot edit it")
                                    new_file_contents += line

                                else:
                                    new_file_contents += line
                                    
                            # Clear the file and then write the new information with the changed username
                            file.seek(0)
                            file.truncate()
                            file.write(new_file_contents)

        
            elif action == 'mark':
                with open('tasks.txt', 'r+') as file:
                    counter = 0
                    for line in file:
                        counter += 1
                        if counter == edit_task and line.split(", ")[0] == entered_username and line.split(", ")[5].strip("\n") == 'No':
                            # Replace the 'No' with 'Yes'
                            new_line = line.replace(line.split(", ")[5], "Yes")
                            new_file_contents += new_line
                            print("Task", counter, "marked as completed")
                            
                        elif counter == edit_task and line.split(", ")[0] == entered_username and line.split(", ")[5].strip("\n") == 'Yes':
                            print("The task has been completed. It cannot be edited")
                            new_file_contents += line
                            
                        elif counter == edit_task and line.split(", ")[0] != entered_username:
                           print("This is not your task, you cannot edit it")
                           new_file_contents += line
                           
                        else:
                           new_file_contents += line
                           
                    # Clear the file and then write the new information with the changed username
                    file.seek(0)
                    file.truncate()
                    file.write(new_file_contents)
            else:
                print("Incorrect input")
                

# Generate reports
def generate_reports():
        total_tasks = 0
        completed_tasks = 0
        uncompleted_tasks = 0
        tasks_overdue = 0
        with open('task_overview.txt', 'w') as file:
            # Number of tasks
            with open('tasks.txt', 'r') as f:
                for i in f:
                    total_tasks += 1
                file.write("Total number of tasks: " + str(total_tasks))

            # Number of completed tasks
            with open('tasks.txt', 'r') as f:    
                for i in f:
                    if i.split(", ")[5].strip("\n") == "Yes":
                        completed_tasks += 1
                file.write("\nNumber of completed tasks: " + str(completed_tasks))

            # Number of uncompleted tasks
            uncompleted_tasks = total_tasks - completed_tasks
            file.write("\nNumber of uncompleted tasks: " + str(uncompleted_tasks))

            # Number of overdue tasks
            with open('tasks.txt', 'r') as f:
                for i in f:
                    due = i.split(", ")[3]
                    date_due = datetime.datetime.strptime(due, "%d %b %Y")
                    today = date.today().strftime("%d %b %Y")
                    date_today = datetime.datetime.strptime(str(today), "%d %b %Y")
                    if date_today > date_due and i.split(", ")[5].strip("\n") == "No":
                        tasks_overdue += 1
                file.write(f"\nTasks overdue: {tasks_overdue}")

            # Percentage of tasks incomplete
            percentage = round(((uncompleted_tasks/total_tasks) * 100), 2)
            file.write(f"\nPercentage of incomplete tasks: {percentage}%")

            # Percentage of tasks overdue
            percentage = round(((tasks_overdue/total_tasks) * 100), 2)
            file.write(f"\nPercentage of overdue tasks: {percentage}%")


        with open('user_overview.txt', 'w') as file:
            # Total number of users
            count_lines = 0
            with open("user.txt", "r") as f:
                # Count how many lines the file has
                for j in f:
                    if j != "\n":
                        count_lines += 1
            file.write(f"Total number of users: {count_lines}")

            #Total number of tasks
            count_lines = 0
            with open("tasks.txt", "r") as f:
                # Count how many lines the file has
                for j in f:
                    if j != "\n":
                        count_lines += 1
            file.write(f"\nTotal number of tasks: {count_lines}")

            # Check user, and give user specific specs
            users_with_tasks = []
            tasks_per_user = []
            
            
            with open('user.txt', 'r') as user_file:
                # Which user has a task
                for i in user_file:
                    with open('tasks.txt', 'r') as tasks_file:
                        for j in tasks_file:
                            # This will also help avoid duplicates
                            if j.split(", ")[0] == i.split(", ")[0] and j.split(", ")[0] not in users_with_tasks:
                                users_with_tasks.append(j.split(", ")[0])
                # Number of tasks per user and percentages
                for i in users_with_tasks:
                    counter = 0
                    completed = 0
                    overdue = 0
                    file.write(f"\n\nUsername: {i}")
                    with open('tasks.txt', 'r') as tasks_file:
                        for j in tasks_file:
                            if i == j.split(", ")[0]:
                                counter += 1
                            if i == j.split(", ")[0] and j.split(", ")[5].strip("\n") == 'Yes':
                                completed += 1
                            # Check overdue
                            date_due = j.split(", ")[3]
                            parser.parse(date_due)
                            today = date.today()
                            date_today = today.strftime("%d %b %Y")
                            if i == j.split(", ")[0] and j.split(", ")[5].strip("\n") == 'No' and date_today > date_due:
                                overdue += 1
                            
                    file.write(f"\nNumber of tasks: {counter}")
                    file.write("\nPercentage of total tasks: " + str(round(((counter/total_tasks)*100), 2)) + "%")
                    file.write("\nPercentage of completed tasks: " + str(round(((completed/counter)*100), 2)) + "%")
                    file.write("\nPercentage of uncompleted tasks: " + str(round(((100 - (completed/counter)*100)), 2)) + "%")
                    file.write("\nPercentage of tasks overdue: " + str(round(((overdue/counter)*100), 2)) + "%")
                 
        print("\nReport generated")


# Register new user
def reg_user():
    added_user = False
    while added_user == False:            
        entered_username = input("Please enter your new username: ")
        if entered_username not in user_details.keys():
            entered_password = input("Please enter your new password: ")
            confirmation = input("Please confirm the password: ")
            if confirmation == entered_password:
                user_file.writelines("\n" + '%s, %s' %(entered_username, entered_password))
                added_user = True
                break
        else:
            print("The username you have entered already exists, try again\n")
            added_user = False
    print("\nThe user has been registered")

        
# Add new task
def add_task():
        # Get todays date
        # https://www.programiz.com/python-programming/datetime/current-datetime
        today = date.today() 
        date_assigned = today.strftime("%d %b %Y")

        print("\nAdding new task")
        username = input("Please enter username of person to assign task to: ").lower()
        task = input("Please enter title of the task: ")
        description = input("Please enter description of the task: ")
        print("The due date is required in form 'dd Mon yyyy'")
        due_date = input("Please enter the due date: ")
        task_completed = "No"
        with open("tasks.txt", "a") as file:
            # Start on the next line
            file.write("\n")
            file.write(username + ", " + task + ", " + description + ", " + due_date+"\
" + ", " + date_assigned + ", " + task_completed)
            print("\nThe task has been added")


# View all tasks
def view_all():
        task_number = 1
        tasks = ""
        with open("tasks.txt", "r") as file:
            for i in file:
                print("Task", task_number)
                tasks = i + "\n"
                task_number += 1
                print(tasks)
        
# =======================================================================
# ADMIN OPTIONS
def admin_menu():
        # If the password is correct, proceed with the following options:
        print("\nPlease select one of the following options:")
        print("r - register user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("gr - generate reports")
        print("ds - display statistics")
        print("e - exit")

        selection = input("\nPlease enter your selection: ").lower()

        # If selection = register user
        if selection == "r":
            reg_user()


        # If selection = add task
        elif selection == "a":
            add_task()

            
        # If selection = view all tasks
        elif selection == "va":
            view_all()

            
        # If selection = view my tasks
        elif selection == "vm":
            view_mine()


        # If selection = generate reports
        if selection == "gr":
            generate_reports()


        # If selection = display statistics
        elif selection == "ds":
            generate_reports()
            
            with open('user_overview.txt', 'r') as user_overview_file:
                print("\n\nUser Overview\n")
                for i in user_overview_file:
                    print(i)

            with open('task_overview.txt', 'r') as task_overview_file:
                print("\n\nTask Overview\n")
                for j in task_overview_file:
                    print(j)


        # If selection = exit
        elif selection == "e":
             print("Exiting Program\nGoodbye!")

# =======================================================================
# EVERYBODY ELSE OPTIONS
def none_admin_menu():
        # If the password is correct, proceed with the following options:
        print("\nPlease select one of the following options:")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("e - exit")

        selection = input("\nPlease enter your selection: ").lower()

        # If selection = add task
        if selection == "a":
                add_task()

        # If selection = view all tasks
        elif selection == "va":
            view_all()

        # If selection = view my tasks
        elif selection == "vm":
            view_mine()
            
        # If selection = exit
        elif selection == "e":
             print("Exiting Program\nGoodbye!")

        else:
            print("\nIncorrect input")             

# =======================================================================

if entered_username == "admin":
        admin_menu()

else:
        none_admin_menu()

user_file.close()
tasks_file.close()


# REFERENCES
# I learnt about looping through 2 loops at the same time from
# stackoverflow under "how to iterate through two lists in parallel"

# thispointer.com 'How to append text or lines to a file in python' was very helpful in learning about
# appending information to a text file on a new line.

# I learnt about strftime() from geeksforgeeks.org under "Python strftime() function" when I was
# googling how to tell today's date.

# I learnt about the 3rd party library dateutil from stackoverflow.
# It was a response by Simon Willison responding to "Converting string into datetime"
# This library apparently has a function to tell the format of the date

# I learnt about .seek() and .truncate() to clear file from stackoverflow.
# It was a response by Snigdha Batra to 'How to erase the file contents of text file in Python?'
