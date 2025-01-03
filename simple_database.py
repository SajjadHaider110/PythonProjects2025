import time

names = []
addresses = []
jobs = []

def welcome_messages():
    print("Enter details into the databases")
    enter_name()

def enter_name():
    entry1 = input("Enter name: ")
    names.append(entry1)
    enter_address()

def enter_address():
    entry2= input("Enter Address: ")
    addresses.append(entry2)
    enter_job()

def enter_job():
    entry3 = input("Enter Job: ")
    jobs.append(entry3)
    showdatabase()

def showdatabase():
    print("searching wait...")
    time.sleep(2)
    print(names)
    print(addresses)
    print(jobs)
    clear_data_base()

def clear_data_base():
    print("Delete details?")
    answer = input("Yes or NO")
    if answer.lower() in ("yes","y"):
        names.clear()
        addresses.clear()
        jobs.clear()
        print("Deleted ",names,addresses,jobs)
    else:
        print("You chose not to delete your info")
        quit()
welcome_messages()

