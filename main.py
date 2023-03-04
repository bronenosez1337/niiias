import class1
InitString = class1.Train()
InitString2 = class1.Train()
while True:
    if InitString.Input_String(input("Введите строку инициализации:\n")) != False:
        break

InitString.object_print()
print(InitString.__dict__)
print(InitString2.__dict__)
#"{Мкс: 0.2 дист= 5 лог = пзг физ =з преп = хв ен = 4f}"
