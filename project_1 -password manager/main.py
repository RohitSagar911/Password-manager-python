from cryptography.fernet import Fernet

"""def write_key():
    key = Fernet.generate_key() #generating key
    with open("key.key", "wb") as file:
        file.write(key) #saving key in file"""


def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

mast_Pass = input("enter the master password: ")

key = load_key() + mast_Pass.encode()
fer = Fernet(key) #initializing the key...


def add():
    acc_name = input("Enter account name: ")
    password = input("Enter password: ")

    with open("password.txt", "a") as f:
        f.write(
            acc_name + "|" + str(fer.encrypt(password.encode()).decode()) + "\n"
        )  # separating username and password
        print("Password added successfully!")


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print(
                f"\naccount name:{user}\nPassword:{fer.decrypt(password.encode()).decode()}\n"
            )


while True:
    modes = input(
        'chose the the mode to:\n"view" to view passwords.\n"add" to add passwords.\n"quit" to quit.'
    ).lower()
    if modes == "quit":
        break

    if modes == "view":
        view()

    elif modes == "add":
        add()
    else:
        print("invalid entry try again!")
        continue
