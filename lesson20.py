if __name__== "__main__":
        login = ("user")
        try:
            i = str(input("Логин:"))
            if i == login:
                print("Вы в системе")
        except Exception:
            print("Ошибка")



