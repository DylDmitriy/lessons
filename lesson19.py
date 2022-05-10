import argparse
import sys

global_dict = {"user": "1235", "qwerty": "pass", "aBcD": "qwerty123" }
just_x = 0

def login(func):
    def wrapper(account_login, account_password):
        if check_password(account_login, account_password):
            return func()
        return False
    return wrapper
@login
def authenticate(account_login, account_password) -> bool:
    return True
def check_password(account_login: str, account_password: str) -> bool:
    return global_dict.get(account_login) == account_password
def one_more_time():
    for i in range(4):
        global just_x
        just_x = i
        from_terminal(account_login, account_password)
        if check_password(account_login, account_password) is True:
            print("Вы в системе!")
        elif i < 3:
            print("Не правильное Имя или Пароль"
                  "\n" f"У Вас осталось {3 - i} попыток")
        elif i == 3:
            print("Вы не прошли")
def from_terminal(account_login, account_password):
    if just_x == 0:
        if account_login == 0:
            account_login = input("Login:")
            return check_password(account_login, account_password)
        elif account_password == 1:
            account_password = input("Password:")
            return check_password(account_login, account_password)
    if just_x > 0:
        account_login = input("Login:")
        account_password = input("Password:")
        return check_password(account_login, account_password)
if __name__== "__main__":
    parser = argparse.ArgumentParser(description="Enter to the sys with"
                                                 "Login and password")
    parser.add_argument("-l", dest="username")
    parser.add_argument("-p", dest="password")
    account_login = parser.parse_args().username or input("username")
    account_password = parser.parse_args().password or input("password")
    one_more_time()




