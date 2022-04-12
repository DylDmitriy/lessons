num = int(input("введите число:"))
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

if num == 1:
    print("Hi, I am Emma")
else:
    print("Call me Liam")

