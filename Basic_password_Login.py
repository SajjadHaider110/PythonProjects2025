user = "sajjad"
password = "haider110"

def login():
    print("Enter User and Password")
    entry1 = input("User: ")
    entry2 = input("Password: ")
    if entry1 == user and entry2 == password:
        print("Access Granted")
        logged_in()
    else:
        print("Access Denied!")

def logged_in():
    print("Logged in")
    quit()

login()