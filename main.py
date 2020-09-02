def getdate():
    """gives present time with date"""
    import datetime
    return datetime.datetime.now()


f = open("users.txt")
user_names = f.readlines()
f.close()


def new(new_user):
    """Create a new file for new user (either for food or exe) for which purpose the user came in program."""
    age_user = input("What is your age?\n>>")
    weight = input("What is your weight?\n>>")
    f = open(f"{new_user}{purpose}.txt", "w")
    f.write(f"Name : {new_user}\nAge: {age_user}\nWeight : {weight}\nTime of registration: {getdate()}\n\n\n")
    if new_user not in str(user_names):
        f1 = open("users.txt","a")
        f1.write(f"{new_user}\n")
        print("New user created.")
        f.close()
        f1.close()
        exit()
    else:
        print("client file created.")
        exit()

# def cont():
#     cont = input("Do you want to continue?(y for yes)\n>>").lower()
#     if cont == "y":
#         continue
#     else:
#         break


def in_food(user_name):
    """input the food details of the existing user. if the existing user has never inputed
    any details then creates a new file for that user otherwise update the old one"""
    global details
    try:
        #open(f"{user_name}{purpose}.txt")
        details = input("Write the name and amount of food.\n>>").title()
        f = open(f"{user_name}{purpose}.txt", "a")
        f.write(f"Food : {details} at {getdate()}\n")
        f.close()
        print("Food details added 😀")
    except FileNotFoundError:
        print("No old records detected. want to create a new profile?('y' for yes)\n>>")
        com = input("")
        if com == "y":
            new(name)
        else:
            exit()



def get_food(user_name):
    """Get food details of the user"""
    try:
        f = open(f"{user_name}{purpose}.txt", "r")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("No data stored to us. Please store some data first! 🤍\n")
        com = input(" want to create a new profile?('y' for yes)\n>>")
        if com == "y":
            new(name)
        else:
            exit()


def in_exe(user_name):
    """input the exercise details of the existing user. if the existing user has never inputed
        any details then creates a new file for that user otherwise update the old one"""
    global details
    try:
        open(f"{user_name}{purpose}.txt")
        details = input("Write the name of exercise performed.\n>>").title()
        #f = open(f"{user_name}{purpose}.txt", "a")
        f.write(f"Exercise : {details} at {getdate()}\n")
        f.close()
        print("Exercise details added. 😀\n")
    except FileNotFoundError:
        print("No old records detected. want to create a new profile?('y' for yes)\n>>")
        com = input("")
        if com == "y":
            new(name)
        else:
            exit()

def get_exe(user_name):
    """Get the execise detail of exising user"""
    try:
        f = open(f"{user_name}Exe.txt", "r")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("No data stored to us. Please store some data first! 🤍\n")
        com = input("want to create a new profile?('y' for yes)\n>>")
        if com == "y":
            new(name)
        else:
            exit()


while True:
    print('''
    Welcome to Ranjan's health tracking program.
    Here you can track your food ingested and 
    exercise performed with accurate time.
    Type "input" for updating your data.
    type "output" for getting your data.
    ''')
    msg = input("What you want to do ?\n>>").lower()
    while True:
        if msg == "input":
            print("Type your first name")
            name = input(">> ").title()
            purpose = input("Type 'food' for adding food details and 'exe' for adding exercise details\n>>").title()
            if (f"{name}") in str(user_names):
                if purpose == "Food":
                    in_food(name)
                    break
                elif purpose == "Exe":
                    in_exe(name)
                    break
                else:
                    print("No such command exist!!\n")
                    break

            else:
                print("no data inputed! New user ditected\n")
                want = input("Want to input data for a new client?(y for yes)\n>>").lower()
                if want == "y":
                    new(name)
                    exit()
                    # purpose = input("Do you want to add new food details or exe details?(type 'food' or 'exe')\n>>").title()
                    # if purpose == "Food":
                    #     in_food(name)
                    #     break
                    # elif purpose == "Exe":
                    #     in_exe(name)
                    #     break
                    # else:
                    #     print("No uch command exist!!")
                    #     break
                else:
                    break
        elif msg == "output":
            print("Type your first name")
            name = input(">> ").title()
            purpose = input("Type 'food' for getting food details and 'exe' for getting exercise details\n>>").title()
            if (f"{name}") in str(user_names):
                if purpose == "Food":
                    get_food(name)
                    break
                elif purpose == "Exe":
                    get_exe(name)
                    break
                else:
                    print("No such command exist!!\n")
                    break
            else:
                print("no data inputed! New user ditected\n")
                want = input("Want to input data for a new client?(y for yes)\n>>").lower()
                if want == "y":
                    new(name)
                    purpose = input("Do you want to add new food details or exe details?(type 'food' or 'exe')\n>>").title()
                    if purpose == "Food":
                        in_food(name)
                        break
                    elif purpose == "Exe":
                        in_exe(name)
                        break
                    else:
                        print("No such command exist!!\n")
                        break

        else:
            print("command do not exist\n")
            break
    cont = input("Do you want to continue?(y for yes)\n>>").lower()
    if cont == "y":
        continue
    else:
        break
