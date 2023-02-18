__author__ = "Jay Browning"

# this program will allow a user to login with user/pass, then add a user, add a task, and view personal or all tasks
# additionally, a user can mark a task as complete, change the due date, or assign to a different user
# reports and statistics regarding the number of tasks tracked and their completion can also be generated and displayed

# =====importing libraries===========
from datetime import datetime
from pathlib import Path

print('welcome to task manager.')


# define functions
def reg_user(new_user):
    # check new username isn't already taken, prompting for password if username is available
    while True:
        with open('./user.txt', 'r') as f:
            for line in f:
                if new_user in line:
                    print('username already exists')
                    new_user = input('please enter a new username:\n'
                                     '>>> ')
                    continue
        new_pass = input('please enter a new password:\n'
                         '>>> ')
        new_pass2 = input('please re-enter password:\n'
                          '>>> ')
        # check passwords match, writing to file if True
        if new_pass == new_pass2:
            with open('./user.txt', 'a') as f:
                f.write(new_user + ', ' + new_pass + '\n')
                print(f'user \'{new_user}\' added successfully.\n')
                break
        # go back to prompt for password if passwords don't match
        else:
            print('passwords do not match')
            continue


def add_task():
    while True:
        # request input from user
        username = input('please enter the username the for which the task is to be assigned:\n'
                         '>>> ')
        title = input('please input the title of the task:\n'
                      '>>> ')
        desc = input('please enter a description of the task:\n'
                     '>>> ')
        due_date = input('please enter a due-date (dd mmm yyyy)\n'
                         '>>> ')
        # fetch today's date
        today = datetime.today()
        # write new task information to tasks file, assigning a value of 'no' to 'completed' slot
        with open('./tasks.txt', 'a') as f:
            f.write(f'\n{username}, {title}, {desc}, {today.strftime("%d %b %Y")}, {due_date}, No')
            break


def view_all():
    while True:
        # define empty list to store each line of task data
        task = []
        # open tasks file and read each line, splitting into individual categories,
        # then assigning each piece of data to individual variables for use in console output
        with open('./tasks.txt', 'r') as f:
            for line in f:
                task = line.strip('\n').split(', ')
                assignee = task[0]
                title = task[1]
                desc = task[2]
                assigned = task[3]
                due = task[4]
                complete = task[5]
                # format data read from task file to a readable output
                print(f'_____________________________________________________________________________________\n\n'
                      f'Task:\t\t\t\t{title}\n'
                      f'Assigned to:\t\t{assignee}\n'
                      f'Date Assigned:\t\t{assigned}\n'
                      f'Due date:\t\t\t{due}\n'
                      f'Task completed?\t\t{complete}\n'
                      f'Task description:\n'
                      f'\t{desc}')
            break
    print(f'_____________________________________________________________________________________\n')


def view_mine():
    while True:
        # define counter, empty dictionary, and inport tasks from tasks.txt
        task_no = 0
        user_tasks = {}
        all_tasks = import_tasks()
        # iterate through tasks checking to see where logged in user is the assignee, and add to counter if true
        # then update dictionary with counter value as key to sub-dictionary of task data
        for x in all_tasks:
            if all_tasks[x]['assignee'] == u_name:
                task_no += 1
                user_tasks.update({
                    task_no: {
                        'assignee': all_tasks[x]['assignee'],
                        'title': all_tasks[x]['title'],
                        'desc': all_tasks[x]['desc'],
                        'assigned': all_tasks[x]['assigned'],
                        'due': all_tasks[x]['due'],
                        'complete': all_tasks[x]['complete'],
                        'task ID': all_tasks[x]['task ID'],
                    }})

        # reset task counter to 0 for next section
        task_no = 0
        # iterate through list of user's tasks, assigning task number to each and printing data
        for task in user_tasks:
            task_no += 1
            print(
                f'_____________________________________________________________________________________\n\n'
                f'Task Number:\t\t {task_no}\n'
                f'Task:\t\t\t\t{user_tasks[task]["title"]}\n'
                f'Assigned to:\t\t {user_tasks[task]["assignee"]}\n'
                f'Date assigned:\t\t{user_tasks[task]["assigned"]}\n'
                f'Due date:\t\t\t{user_tasks[task]["due"]}\n'
                f'Task completed?\t\t{user_tasks[task]["complete"]}\n'
                f'Task description:\n'
                f'\t{user_tasks[task]["desc"]}')
            continue
        print(f'_____________________________________________________________________________________\n')

        # request input from user, check to see if task is already completed
        select_task = int(input('please select task number to edit or enter \'-1\' for main menu: '))
        if select_task == -1:
            break

        elif user_tasks[select_task]['complete'] == ' Yes':
            print('task already completed')
            input("Press Enter to continue...")
            continue

        # request input from user, then reassign dictionary entries based on user input
        else:
            edit_mode = input('would you like to reassign task to different user, '
                              'change due date, or mark as complete?: enter \'r\' to reassign, \'d\' to change due date'
                              ' or \'c\' to mark as complete: ')

            if edit_mode.lower() == 'r':
                new_assignee = input('please enter name of user to which task is to be reassigned: ')
                user_tasks[select_task]['assignee'] = new_assignee
                print(f'task assigned to {new_assignee}.')
                all_tasks[user_tasks[select_task]['task ID']] = user_tasks[select_task]
                output_tasks(all_tasks)
                input("Press Enter to continue...")

            elif edit_mode.lower() == 'd':
                new_date = input('please enter new due-date (dd mmm yyyy): ')
                user_tasks[select_task]['due'] = ' ' + new_date
                print(f'due-date changed to {new_date}. ')
                all_tasks[user_tasks[select_task]['task ID']] = user_tasks[select_task]
                output_tasks(all_tasks)
                input("Press Enter to continue...")

            if edit_mode.lower() == 'c':
                user_tasks[select_task]['complete'] = ' Yes'
                print(f'task number {select_task} marked as completed')
                all_tasks[user_tasks[select_task]['task ID']] = user_tasks[select_task]
                output_tasks(all_tasks)
                input("Press Enter to continue...")
        continue


def import_tasks():
    while True:
        # define empty dictionary to store tasks read in from tasks.txt, define task counter for dict keys, and
        # temporary list to store data read in from file before being assigned to keys in sub-dictionary
        all_tasks = {}
        task_id = 0
        temp_list = []
        # open file, read lines in as list items, then assign data to sub dictionary using task counter as main key
        with open('./tasks.txt', 'r') as f:
            tasklist = f.readlines()
            for task in tasklist:
                temp_list.append(task.strip('\n').split(','))
                all_tasks.update({
                    task_id + 1: {
                        'assignee': temp_list[task_id][0],
                        'title': temp_list[task_id][1],
                        'desc': temp_list[task_id][2],
                        'assigned': temp_list[task_id][3],
                        'due': temp_list[task_id][4],
                        'complete': temp_list[task_id][5],
                        'task ID': task_id + 1,
                    }})
                task_id += 1

            return all_tasks


def output_tasks(all_tasks):
    # format sub-dictionary data from each key in all_tasks into a single string and write string back to file
    out_string = ''
    for i in all_tasks:
        out_list = list(all_tasks[i].values())
        out_string = out_string + f"{','.join(out_list[0:6])}\n"
    with open('./tasks.txt', 'w') as f:
        f.write(out_string)


def task_counter(task_dict, key, value):
    # pass in dictionary of tasks, a key and a value to check against, and add to counter if true
    comp_tasks = 0
    while True:
        for task in task_dict:
            if task_dict[task][key].lower() == value:
                comp_tasks += 1
        return comp_tasks


def overdue(all_tasks,):
    # pass in dictionary of tasks and check if due date of incomplete tasks has passed, adding to counter if true
    overdue_tasks = 0
    while True:
        for task in all_tasks:
            if datetime.strptime(all_tasks[task]['due'], " %d %b %Y") < datetime.today() \
                    and all_tasks[task]['complete'].lower() == ' no':
                overdue_tasks += 1
        return overdue_tasks


def percentage(divisor, dividend):
    # calculate a percentage
    percent = (dividend / divisor) * 100
    return percent


def task_overview():
    all_tasks = import_tasks()          # call import tasks function to get updated data from tasks.txt
    tot_tasks = len(all_tasks)          # check length of dictionary for total tasks tracked
    complete = task_counter(all_tasks, 'complete', ' yes')      # call task counter checking for completed tasks
    incomplete = task_counter(all_tasks, 'complete', ' no')     # call task counter checking for incomplete tasks
    outstanding = overdue(all_tasks)    # call overdue function, checking for incomplete tasks that are overdue
    percent_incomp = percentage(tot_tasks, incomplete)      # calculate percent passing total tasks and incomplete tasks
    percent_over = percentage(tot_tasks, outstanding)       # calculate percent passing total tasks and outstanding task
    with open('./task_overview.txt', 'w') as overview:      # open task_overview, format and write data to file
        overview.write(
            f'the total amount of tasks being tracked is: {tot_tasks}\n'
            f'the number of completed tasks is: {complete}\n'
            f'the number of incomplete tasks is: {incomplete}\n'
            f'the number of outstanding tasks that are overdue is: {outstanding}\n'
            f'the percentage of incomplete tasks is: {percent_incomp:.2f}%\n'
            f'the percentage of overdue tasks is: {percent_over:.2f}%'
        )


def user_register():        # creates list of users from users.txt
    user_list = []
    temp_list = []
    counter = 0
    with open('./user.txt', 'r') as account_list:
        users_input = account_list.readlines()
        for user in users_input:                            # iterate through users list, adding only username to list
            temp_list.append(user.strip('\n').split(','))   # of users
            user_list.append(temp_list[counter][0])
            counter += 1
    return user_list


def loop_dict(dictionary, key1, key2, assignee, value):     # counts instances of tasks assigned to individual users
    task_count = 0
    for x in dictionary:
        if dictionary[x][key1].lower() == assignee and dictionary[x][key2].lower() == value:
            task_count += 1
    return task_count


def user_overdue(all_tasks, key, value):                    # counts number of overdue tasks for individual users
    user_overdue_tasks = 0
    while True:
        for task in all_tasks:
            if all_tasks[task][key].lower() == value:
                if datetime.strptime(all_tasks[task]['due'], " %d %b %Y") < datetime.today() \
                        and all_tasks[task]['complete'].lower() == ' no':
                    user_overdue_tasks += 1
        return user_overdue_tasks


def user_overview():                                        # reads in all tasks, and generates report of users and
    all_tasks = import_tasks()                              # and their tasks
    tot_tasks = len(all_tasks)
    users = user_register()
    tot_users = len(users)
    u_task_count_dict = {}

    # clear contents of output file if it exists
    with open('./user_overview.txt', 'w', ) as f:           # clear contents of report if already created
        f.write('')
    with open('./user_overview.txt', 'a', ) as f:           # write general data to report
        f.write(f'the total number of users registered is: {tot_users}\n'
                f'the total number of tasks being tracked is: {tot_tasks}\n'
                f'_____________________________________________________________________________________\n')

    for user in users:                                      # iterate through users, to retrieve data to calculate %s
        u_task_count = task_counter(all_tasks, 'assignee', user)
        u_task_count_dict.update({user: u_task_count})
        if u_task_count_dict[user] == 0:
            u_percentage = 0
        elif u_task_count_dict[user] != 0:
            u_percentage = percentage(tot_tasks, u_task_count_dict[user])
            u_comp_percentage = percentage(u_task_count_dict[user],
                                           loop_dict(all_tasks, 'assignee', 'complete', user, ' yes'))
            user_incomp = percentage(u_task_count_dict[user], loop_dict(all_tasks, 'assignee', 'complete', user, ' no'))
            user_outstanding = percentage(u_task_count_dict[user], user_overdue(all_tasks, 'assignee', user))

            with open('./user_overview.txt', 'a', ) as f:   # write user specific data to file
                f.write(f'user: \t\t\t\t\t{user}\n'
                        f'no. tasks assigned: \t\t\t{u_task_count}\n'
                        f'percentage of tasks assigned to user: \t{u_percentage:.2f}%\n'
                        f'percentage of tasks complete: \t\t{u_comp_percentage:.2f}%\n'
                        f'percentage of tasks incomplete: \t{user_incomp:.2f}%\n'
                        f'percentage of tasks overdue: \t\t{user_outstanding:.2f}\n'
                        f'_____________________________________________________________________________________\n')


def print_stats(filepath):                                  # reads reports and displays in console
    with open(filepath, 'r') as f:
        task_display = f.readlines()
        for line in task_display:
            print(line.strip('\n'))


def display_stats(stat_type, filepath):                     # checks to see if report file exists, and either calls the
    path = Path(filepath)                                   # function to generate reports if they don't exist or
    if path.is_file():                                      # the function to display stats in console
        print_stats(filepath)
    else:
        stat_type()
        print_stats(filepath)


# ====Login Section====

while True:
    # request input from user for username and password
    u_name = input('please enter your username:\n'
                   '>>> ')
    u_pass = input('please enter your password:\n'
                   '>>> ')

    # open user/pass file as 'account_list', read each line in, remove comma, and store as 'username' and 'password'
    with open('./user.txt', 'r') as account_list:
        for line in account_list:
            username, password = line.replace(',', '').split()

            # compare user input to values from file, proceeding to menu if successful login,
            if u_name == username and u_pass == password:
                print('\nw00t! access granted.\n')
                break

        # or prompting re-entry of login credentials
        else:
            print('\ninvalid username / password combination.')
            continue
    break

# ====Menu Section====

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.ad
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - Generate reports
ds - Display Statistics
e - Exit

>>> ''').lower()

    if menu == 'r':
        # request new username from user
        new_name = input('please enter a new username:\n'
                         '>>> ')
        reg_user(new_name)

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        task_overview()
        user_overview()
        print('reports generated!')

    elif menu == 'ds':
        display_stats(task_overview, './task_overview.txt')
        display_stats(user_overview, './user_overview.txt')

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print('You have made a wrong choice, please try again\n')
