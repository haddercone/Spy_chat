import os
import re
''' the code snippet given below is to check whether the file names and spy ids already exist or not '''
ids = []
files = []
for j in os.listdir('.'):
    if '.txt' in j:
        f = open(j, 'rt')
        j = j.replace('.txt', '')
        files.append(j)
        f = f.readline().replace('SPY ID : ', '')
        f = f.replace('\n', '')
        ids.append(f)
# print(ids)
# print(files)
all_spy_details = {1234: {'name': 'Mr. James', 'age': 29, 'experience': "3 years. You're improving."}}


# method to  show default spy
def show_default_spy():
    print("\t"*10, all_spy_details[1234])


# method to add new spy
def add_new_spy():
    while True:
        details = {}
        while True:
            salutation = input("Enter Salutation: ")
            salutation = salutation.capitalize()
            if salutation == 'Mr' or salutation == 'Mrs' or salutation == 'Ms':
                name = input("Enter name: ")
                name = name.capitalize()
                if name.isalpha() is False:
                    print("Name should be a string")
                    continue
                else:
                    if len(name) >= 3:
                        details['name'] = salutation + ". " + name
                        break
                    else:
                        print("Name of your spy should be minimum 3 characters long")
                        print("Please enter the spy name again.")
                        continue
            else:
                print("Salutation should start from Mr., Mrs., Ms.")
                continue

        while True:
            age = input("Enter age of your spy: ")
            if age.isdigit() is False:
                print("Age should be a number not a string: ")
                continue
            else:
                if 20 <= int(age) <= 60:
                    details['age'] = int(age)
                    break
                else:
                    print("Age should be greater than 20 years and less than 60 years.")
                    print("Please enter the spy age again.")
                    continue
        while True:
            try:
                experience = input("Enter the spy experience: ")
                # regular expression used for taking the float values with validations.
                if re.search(r'[0-9].*[0-9]*', experience):
                    if 1 <= float(experience) < 2:
                        experience = str(experience) + " years. "
                        appreciation_message = "You are a beginner. Don't lose hope"
                        details['experience'] = str(experience) + appreciation_message
                        break
                    elif 2 <= float(experience) < 3:
                        experience = str(experience) + " years. "
                        appreciation_message = "You can do better. Keep it up"
                        details['experience'] = str(experience) + appreciation_message
                        break
                    elif 3 <= float(experience) < 4:
                        experience = str(experience) + " years. "
                        appreciation_message = "You're improving."
                        details['experience'] = str(experience) + appreciation_message
                        break
                    if 4 <= float(experience) <= 5:
                        experience = str(experience) + " years. "
                        appreciation_message = "You're doing a great job!"
                        details['experience'] = str(experience) + appreciation_message
                        break
                    else:
                        print("Experience should be in the range of 1 to 5")
                        continue
            except ValueError:
                print("Please enter floats and integers only.")
                continue

        while True:
            spy_id = input("Enter spy id: ")
            if spy_id not in ids:
                if len(spy_id) == 4 and spy_id.isdigit():
                    if int(spy_id) in all_spy_details.keys():
                        print("This spy id already exist choose another id.")
                        continue
                    else:
                        all_spy_details[int(spy_id)] = details
                        print("\nWelcome on board ", details['name'])
                        break
                else:
                    print("Spy id should be of four digits.")
                    continue
            else:
                print("This id already exist please choose another id: ")
                continue

        confirmation = input('Want to add more spies [y/n]?: ')
        confirmation = confirmation.lower()

        if confirmation == 'y':
            p = input("\nPlease enter the password again to continue: ")
            f1 = open('../password.txt', 'rt')
            password = f1.read()
            if password == p:
                print("Access granted!. You are allowed to add spies.")
                continue
            else:
                print("\nYou are not authorised to add spies.\nPlease enter the correct password to continue.")
                break
        elif confirmation == 'n':
            break
        else:
            print("Please choose between 'y' and 'n'")
            break
    return all_spy_details


# After adding the spy details this method asks for the status for each spy that has been added recently'''
def add_status():
    status = ['Underground', 'Abducted', 'Missing']
    add_spy_status = all_spy_details
    add_spy_status.pop(1234)
    print("\nAdd status for your spies: \n1.Add default status \n2.Add your status.\n ")
    for i in add_spy_status:
        print("Add status for " + add_spy_status[i]['name'] + "\n")
        while True:
            status_choice = int(input("Enter 1 for default and 2 for new status : "))
            if status_choice == 1:

                print("Please choose from the following status: ")
                print("1. " + status[0] + "\n" + "2. " + status[1] + "\n" + "3. " + status[2])
                while True:
                    chosen_status = input(
                        "\nEnter the status number to add status for " + add_spy_status[i]['name'] + " : ")
                    if chosen_status == '1':
                        add_spy_status[i]['status'] = status[0]
                        break
                    elif chosen_status == '2':
                        add_spy_status[i]['status'] = status[1]
                        break
                    elif chosen_status == '3':
                        add_spy_status[i]['status'] = status[2]
                        break
                    else:
                        print("Please choose from the given status")
                        continue
                break
            elif status_choice == 2:
                input_status = input("Enter the status: ")
                add_spy_status[i]['status'] = input_status
                break
            else:
                print("Please choose from the above.")
                continue

    return add_spy_status


# The method given below shows the spy details form the database in the system
def fetch_spy_data():
    fetch_data = input("Enter file name to access it's data: ")
    print("")
    try:
        with open(fetch_data + '.txt', 'rt') as af:
            print(af.read())
            af.close()
    except FileNotFoundError:
        print("File by the name '" + fetch_data + "' does not exist")


def show_all_spies():
    count = 1
    for i in os.listdir('.'):
        if '.txt' in i:
            f4 = open(i, 'rt')
            print("\n\nSPY " + str(count) + " DETAILS: \n\n")
            print(f4.read())
            count += 1


# The method given below gives the choices for the user to select the operations
def choice():
    print("Enter the following keys to execute their corresponding functions")
    print(" 1: show_default_spy()\n 2: show_all_spies()\n 3: add_new_spy()\n 4.fetch_spy_data() ")
    while True:

        value = input("\nEnter the function number to execute : ")
        if value == '1':
            show_default_spy()
            print('\n')
        elif value == '2':
            show_all_spies()
            print('\n')
        elif value == '3':
            p = input("Please enter password to add spies.")
            f1 = open('../password.txt', 'rt')
            password = f1.read()
            if password == p:
                print("Access granted!. You're allowed to add spies.\n")
                add_new_spy()
                print('\n')
            else:
                print("You are not authorised to add spies.")
        elif value == '4':
            f2 = open('../password.txt', 'rt')
            p1 = f2.read()
            password1 = input("Please enter the password to access the spy data.")
            if password1 == p1:
                fetch_spy_data()
            else:
                print("You are not authorised to access the spy data.")
        else:
            print("Please choose among the above specified keys")

        choice_value = input("Want to execute any specified function again [y/n]? : ")
        choice_value = choice_value.lower()

        if choice_value == 'y':
            continue
        elif choice_value == 'n':
            break
        else:
            print("Please choose between 'y' and 'n' ")
            break


choice()


# The method given below creates the file for each spy that has been added recently
def save_spy_data():
    get_data = add_status()
    # Get spy data from all spy details and save it as txt file
    for i in get_data:
        while True:
            file_name = input("Enter the file name for " + str(get_data[i]['name'] + ' :'))
            if file_name not in files:
                files.append(file_name)
                with open(file_name + ".txt", 'w') as f3:
                    f3.writelines("SPY ID : " + str(i))
                    f3.writelines("\n\nSPY NAME : " + str(get_data[i]['name']).upper())
                    f3.writelines("\n\nSPY STATUS : " + str(get_data[i]['status']).upper())
                    f3.writelines("\n\nSPY AGE : " + str(get_data[i]['age']).upper())
                    f3.writelines("\n\nSPY EXPERIENCE : " + str(get_data[i]['experience']).upper())
                    f3.close()
                    break
            else:
                print("File already exist by the name of " + file_name + ".txt . Please choose another file name")
                continue


save_spy_data()
