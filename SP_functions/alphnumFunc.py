# Write Python Program To Get A Username From The User That Should Have Alphanumeric Characters, Then Pass That Username To Function As Parameter, To Display That Username

def check_pass(username):
    alpha=False
    num=False
    for ch in username:
        if ch.isalpha():
            alpha=True
        if ch.isdigit():
            num=True
    if len(username)<8:
        print('lenght is too short')

    if not alpha or not num:
        print("not a alphanum password ")


username=input("Enter username :")
check_pass(username)