# from cryptography.fernet import Fernet

# '''
# def write_key():
#     key=Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)
# write_key()'''

# def load_key():
#     text=open("key.key","rb")
#     key=text.read()
#     text.close()
#     return key

# master_password=input("What is your password? ")
# key=load_key()+master_password.encode()
# fer=Fernet(key)



# def view():
#     with open("password.txt",'r')as f:
#         for line in f.readlines():
#             data=line.rstrip()
#             user,password=data.split("-")
#             print(f"user={user},password={fer.decrypt(password.encode())}")

# def add():
#     name=input("Enter your name: ")
#     password=input("Enter you password: ")
#     with open("password.txt",'a')as f:
#         f.write(f"{name}-{fer.encrypt(password.encode()).decode()}\n")

# while True:
#     mode=input("Would you like to add a new password or view existing ones(view,add)").lower()
#     if mode=="q":
#         break
#     elif mode=="view":
#         view()
#     elif mode=="add":
#         add()




print("Welcome to password manager")
def view():
    with open("password.txt","r")as f:
        for line in f.readlines():
            line=line.rstrip()
            usr,passs=line.split("-")
            print(f"name={usr},password={passs}")
def add():
    name=input("Enter your uname? ")
    password=input("Enter your password: ")
    with open ("password.txt","a")as f:
        f.write(f"{name}-{password}\n")


while True:
    user=input("Would you like to add a new password or view existing ones(view,add,quite)").lower()
    if user=="quit":
        break
    elif user=="view":
        view()
    elif user=="add":
        add()
    else:
        print("Invalid Input!!")