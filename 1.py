#"{Мкс: 0.2 дист= 5 лог = пзг физ =з преп = хв ен = 4f}"



def Input_String():
    InitString = "{Мкс: 0.2 лог = пзг дист= 5 физ =з преп = хв } ен = 4f}"
    InitString = InitString.lower()
    begin_of_Init= search("{",InitString, 0)
    end_of_Init= search("}",InitString, 0)
    if InitString[end_of_Init-1]== " " and InitString[end_of_Init-2]== " ":
        print("Не используйте более двух пробелов подряд.")
        Input_String()
    if (begin_of_Init is None or end_of_Init is None):
        print ("Нет меток начала и конца описания объекта")
        Input_String()
    
    ObjType = InitString [search("{",InitString, 0)+1: search (":",InitString, 0)]   # Маркер типа объекта
    if ObjType.replace(" ","") == "":
        print("Не введён тип объекта")
        Input_String()
    coord_begin=search (":",InitString, 0)
    coord_end= search(".",InitString,coord_begin+2)
    Num_of_Kompl = InitString[coord_begin+1:coord_end]
    coord_begin = search(" ",InitString,coord_end+2)
    Num_of_Obj = InitString[coord_end+1:coord_begin]

    if Num_of_Kompl.replace(" ","") == "" or Num_of_Obj.replace(" ","") == "":
        print("Ошибка ввода, возможно Вы не ввели номер объекта/комплекта или используете лишние пробелы.")
        Input_String()
    try:
        Num_of_Kompl = int(Num_of_Kompl)                       # Номер комплекта компонента
        Num_of_Obj = int(Num_of_Obj.replace("}",""))                           # номер объекта
    except:
        print("Ошибка ввода (Это не число)")
        Input_String()

    if (not coord_begin or coord_begin+1 >= end_of_Init): pass
    else:
        coord_end = search("=",InitString,coord_begin+1)
        State1 = InitString[coord_begin+1:coord_end].strip()
        coord_begin = search(" ",InitString,coord_end+2)
        Value1 = InitString[coord_end+1:coord_begin].strip()
        if Value1=="": 
            print("Ошибка ввода, возможно вы не ввели параметр \"{0}\" или используете лишние пробелы.".format(State1))
            Input_String()
        Value1=identify(State1,Value1)
    
    if (not coord_begin or coord_begin+1 >= end_of_Init): pass
    else:
        coord_end = search("=",InitString,coord_begin+1)
        State2 = InitString[coord_begin+1:coord_end].strip()
        coord_begin = search(" ",InitString,coord_end+2)
        Value2 = InitString[coord_end+1:coord_begin].strip()
        if Value2=="": 
            print("Ошибка ввода, возможно вы не ввели параметр \"{0}\" или используете лишние пробелы.".format(State2))
            Input_String()
        if (not State2 == State1):
            Value2=identify(State2,Value2)
        else:
            print ("Параметр {0} уже был использован.".format(State2))
            Input_String()

    if (not coord_begin or coord_begin+1 >= end_of_Init): pass
    else:
        coord_end = search("=",InitString,coord_begin+1)
        State3 = InitString[coord_begin+1:coord_end].strip()
        coord_begin = search(" ",InitString,coord_end+2)
        Value3 = InitString[coord_end+1:coord_begin].strip()
        if Value3=="": 
            print("Ошибка ввода, возможно вы не ввели параметр \"{0}\" или используете лишние пробелы.".format(State3))
            Input_String()
        if (not State3 == State1 or not State3 == State2):
            Value3=identify(State3,Value3)
        else:
            print ("Параметр {0} уже был использован.".format(State3))
            Input_String()


    if (not coord_begin or coord_begin+1 >= end_of_Init): pass
    else:
        coord_end = search("=",InitString,coord_begin+1)
        State4 = InitString[coord_begin+1:coord_end].strip()
        coord_begin = search(" ",InitString,coord_end+2)
        Value4 = InitString[coord_end+1:coord_begin].strip()
        if Value4=="": 
            print("Ошибка ввода, возможно вы не ввели параметр \"{0}\" или используете лишние пробелы.".format(State4))
        if (not State4 == State1 or not State4 == State2 or not State4 == State3):
            Value4=identify(State4,Value4)
        else:
            print ("Параметр {0} уже был использован.".format(State4))
            Input_String()


    if (not coord_begin or coord_begin+1 >= end_of_Init): pass
    else:
        coord_end = search("=",InitString,coord_begin+1)
        State5 = InitString[coord_begin+1:coord_end].strip()
        coord_begin = search(" ",InitString,coord_end+2)
        Value5 = InitString[coord_end+1:coord_begin].strip()
        if Value5=="": 
            print("Ошибка ввода, возможно вы не ввели параметр \"{0}\" или используете лишние пробелы.".format(State5))
        if (not State5 == State1 or not State5 == State2 or not State5 == State3 or not State5 == State4):
            Value5=identify(State5,Value5)
        else:
            print ("Параметр {0} уже был использован.".format(State5))
            Input_String()
    print("")


def search(simv,String,i):
    
    for i in range(i,len(String)):
        if String[i] == simv:
            return i
    return None    

def identify(State,Value):
    Value = Value.replace("}","")
        

    match State:
        case "дист":
            try:
                Value=int(Value)
                if 0 <= Value <= 31: return Value
                else: 
                    print("Недопустимый параметр для: \"{0}\" ".format(State))
                    Input_String()
            except:
                print("Параметр \"дист\" должен быть числом")
                Input_String()
        case "лог":
            match Value:
                case "с"|"св"|"своб":
                    return "свободна"
                case "ложз":
                    return "ложно занятая"
                case "логз":
                    return "логически занятая"
                case "пз":
                    return "правильно занятая"
                case "пзг":
                    return "правильно занятая головой"
                case _:
                    print ("Недопустимый параметр для: \"{0}\" ".format(State))
                    Input_String()
        case "физ": 
            match Value:
                case "с"|"св"|"своб":
                    return "свободна"
                case "з":
                    return "занятая"
                case _:
                    print ("Недопустимый параметр для: \"{0}\" ".format(State))
                    Input_String()
        case "преп": 
            match Value:
                case "х"|"хв"|"хвост":
                    return "хвост"
                case "к"|"кр"|"красный":
                    return "красный светофор"
                case "с"|"стр"|"стрелка":
                    return "стрелка"
                case _:
                    print ("Недопустимый параметр для: \"{0}\" ".format(State))
                    Input_String()
        case "ен": 
            try:
                Value = bytes.fromhex(Value)
                return Value
            except: 
                print("Параметр должен быть в HEX")
                Input_String()
        case _:
            print("Недопустимый параметр для: \"{0}\" ".format(State))
            Input_String()
             

# print("{0}{1}".format(len(InitString), InitString))
Input_String()



          
#         sost1 = InitString[coord_end+1:coord_begin]
#     #else Возврат к вводу 
print("")