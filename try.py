z = 2


def pr():
    print("Просто вывела после функции):", z)


def calc():
    z = 9
    print("Изменлиа значение в функции:", z)


def pr2():
    print("Просто вывела после функции:", z)


calc()
pr()
pr2()
print("ВНЕ функции: ", z)