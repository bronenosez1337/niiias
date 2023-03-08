import class1
# import copy
Objects = []
i=0
def comparefunc():
    objnum1 = input("Первый объект сравнения? Введите порядковый номер:\n")
    objnum2 = input("Второй объект сравнения? Введите порядковый номер:\n")
    try:
        objnum1 = int(objnum1)
        objnum2 = int(objnum2)
    except:
        print("Вы ввели не число")
        comparefunc()
    
    print ("\tТип объекта:\t\t{0}\t\t{1}".format(getattr(Objects[objnum1],"Тип объекта"),getattr(Objects[objnum2],"Тип объекта")))
    print ("\tНомер комплекта:\t{0}\t\t{1}".format(getattr(Objects[objnum1],"Номер комплекта объекта"),getattr(Objects[objnum2],"Номер комплекта объекта"))) 
    print ("\tНомер объекта:\t\t{0}\t\t{1}".format(getattr(Objects[objnum1],"Номер объекта"),getattr(Objects[objnum2],"Номер объекта")))
    print ("\tНомер объекта:\t\t{0}\t\t{1}".format(getattr(Objects[objnum1],"Номер объекта"),))
    print ("{0}")
def printfunc():
    objnum = input("Какой объект вывести? Введите порядковый номер:\n")
    
    try:
        objnum = int(objnum)
    except:
        print("Вы ввели не число")
        printfunc()
    try:
        Objects[objnum].object_print()
    except:
        print("Такого объекта не существует")
        printfunc()

def copyfunc(i):
    objnum = input("Копию какого объекта сделать? Введите порядковый номер или \"cancel\" для отмены копирования:\n")
    if objnum =="cancel":
        return
    try:
        objnum = int(objnum)
    except:
        print("Вы ввели не число")
        copyfunc()
    try:
        Objects.append(class1.Train())
        Objects[i] = Objects[objnum]
        i+=1
        return i
    except:
        print("Такого объекта не существует")
        copyfunc(i)

def new_object():
    Objects.append(class1.Train())
    while True:
        if Objects[i].Input_String(input("Введите строку инициализации:\n")) != False:
            break
        # if Objects[i].Input_String(input("Введите строку инициализации:\n")) != False:
        #     break

def print_help():
    print("╔═══════════════════════════════════════════════════════════════════════════════╗")
    print("║Доступные команды:\t\t\t\t\t\t\t\t║\n║help -- вывод этого текста \t\t\t\t\t\t\t║\n║new -- создание нового объекта класса \t\t\t\t\t\t║\n║copy -- создание копии объекта\t\t\t\t\t\t\t║ ")
    print("║compare -- сравнение заданных объектов \t\t\t\t\t║\n║exit -- завершение программы\t\t\t\t\t\t\t║")
    print("╠═══════════════════════════════════════════════════════════════════════════════╣")
    print("║Строка инициализации должна иметь вид:\t\t\t\t\t\t║\n║\t{Мкс: 0.2 дист= 5 лог = пзг физ =з преп = хв ен = 4f}\t\t\t║\n║где:\t\t\t\t\t\t\t\t\t\t║")
    print("║\t{ и } метки начала и конца описания объекта\t\t\t\t║")
    print("║\tМКС - обязательный маркер типа объекта\t\t\t\t\t║")
    print("║\t: метка конца описания типа объекта\t\t\t\t\t║")
    print("║\t0 номер комплекта объекта\t\t\t\t\t\t║")
    print("║\t2 номер объекта\t\t\t\t\t\t\t\t║")
    print("║\tдист= 5 задаваемая дистанция на объекте [0..31]\t\t\t\t║")
    print("║\tлог = пзг логическое состояние РЦ. Возможные состояния:\t\t\t║\n║\t\t“с”, “св”, “своб” - свободна\t\t\t\t\t║\n║\t\t“ложз” - ложно занятая\t\t\t\t\t\t║\n║\t\t“логз” - логически занятия\t\t\t\t\t║\n║\t\t“пз” - правильно занятая\t\t\t\t\t║\n║\t\t“пзг” - правильно занятая головой\t\t\t\t║")
    print("║\tфиз =з физическое состояние РЦ. Возможные состояния:\t\t\t║\n║\t\t“с”, “св”, “своб” - свободна\t\t\t\t\t║\n║\t\t“з” - занятая\t\t\t\t\t\t\t║")
    print("║\tпреп = хв препятствие на объекте. Возможные состояния:\t\t\t║\n║\t\t“х”, “хв”, “хвост” - хвост\t\t\t\t\t║\n║\t\t“к”, “кр”, “красный” - красный светофор\t\t\t\t║\n║\t\t“с”, “стр”, “стрелка” - стрелка\t\t\t\t\t║")
    print("║\tен = 4f Значение сигнала АЛС-ЕН типа байт в шестнадцатеричной форме\t║")
    print("╚═══════════════════════════════════════════════════════════════════════════════╝")
while True:
    Command=input("Введите команду\n")
    match Command:
        case "help":
            print_help()
        case "new":
            new_object()
            i+=1
        case "copy":
            i= copyfunc(i)
        case "compare":
            comparefunc()
        case "print":
            printfunc()
        case "exit":
            break
        case _:
            print_help()



# print(deepcopy_of_object.__dict__)
# print(Object1.__dict__)
# print(Object2.__dict__)
#"{Мкс: 0.2 дист= 5 лог = пзг физ =з преп = хв ен = 4f}"
