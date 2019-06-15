# Create function for adding new spy and to show default spy and use age validation

all_spy_details = [{'name': 'James', 'age': 29, 'experience': '3 years', 'ratings': 3}]


def show_default_spy():
    print(all_spy_details[0])


def add_new_spy():
    while True:
        details = {}
        while True:
            name = input("Enter name: ")
            if name.isalpha() is False:
                print("Name should be a string")
                continue
            else:
                if len(name) >= 3:
                    details['name'] = name
                    break
                else:
                    print("Name of your spy should be minimum 3 characters long")
                    print("Please enter the spy name again.")
                    continue
        while True:
            age = input("Enter age of your spy: ")
            if age.isdigit() is False:
                print("Age should be a number not a alphanumeric string: ")
                continue
            else:
                if int(age) >= 20:
                    details['age'] = int(age)
                    break
                else:
                    print("Age should be greater than 20 years.")
                    print("Please enter the spy age again.")
                    continue
        while True:
            experience = input("Enter the spy experience: ")
            if experience.isdigit() is False:
                print("Experience should be in digits: ")
                continue
            else:
                experience = str(experience) + " years"
                details['experience'] = experience
                break

        while True:
            spy_ratings = int(input("Enter the spy ratings: "))
            if spy_ratings >=1 and spy_ratings <= 5:
                details['ratings'] = spy_ratings
                all_spy_details.append(details)
                break
            else:
                print("Rating must be in the range of 1 to 5")
                continue


        confirmation = input('Want to add more spies [y/n]?: ')
        confirmation = confirmation.lower()

        if confirmation == 'y':
            continue
        elif confirmation == 'n':
            break
        else:
            print("Please choose between 'y' and 'n'")
            break


def show_all_spies():
    for i in all_spy_details:
        print(i)


def choice():
    print("Enter the following keys to execute their corresponding functions")
    print(" 1: show_default_spy()\n 2: show_all_spies()\n 3: add_new_spy() ")
    while True:

        value = int(input("Enter the function number : "))
        if value == 1:
            show_default_spy()
        elif value == 2:
            show_all_spies()
        elif value == 3:
            add_new_spy()
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


