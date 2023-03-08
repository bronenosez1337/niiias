import class1
import copy
Object1 = class1.Train()
Object2 = class1.Train()

def new_object(InitString):
    while True:
        if InitString.Input_String(input("Введите строку инициализации:\n")) != False:
            break
def print_help():
    print("Доступные команды:\nhelp -- вывод этого текста \nnew -- создание нового объекта класса \ncopy -- создание копии объекта")
    print("compare -- сравнение заданных объектов \nexit -- завершение программы")

while True:
    Command=input("Введите команду\n")
    match Command:
        case "help":
            print_help()
        case "new":
            new_object(Object1)
        case "copy":
            deepcopy_of_object = copy.deepcopy(Object1)
        case "compare":
            pass
        case "print":
            pass
        case "exit":
            break
        case _:
            print_help()



Object1.object_print()
deepcopy_of_object.object_print()
print(deepcopy_of_object.__dict__)
print(Object1.__dict__)
print(Object2.__dict__)
#"{Мкс: 0.2 дист= 5 лог = пзг физ =з преп = хв ен = 4f}"
