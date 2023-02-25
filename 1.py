#"{Мкс: 0.2 дист= 5 лог = пзг физ =з преп = хв ен = 4f}"

InitString = "{Мкс: 0.2 дист= о5 лог = пзг физ =з ен = 4f}"
InitString.lower()
def search(simv,simv2,i):
    
    for i in range(i,len(InitString)):
        if InitString[i] == simv or InitString[i] == simv2:
            return i
        # if InitString[i] == None: return 
        #else Возврат в функцию ввода

def identify(State,Value):
    Value = Value.replace("}","")
        

    match State:
        case "дист":
            try:
                Value=int(Value)
                if(Value >=0 and Value<=31): return Value
                else: print("Ошибка ввода параметра", bState)
            except:
                print("Параметр \"дист\" должен быть числом")
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
                    print ("Input error")
        case "физ": 
            match Value:
                case "с"|"св"|"своб":
                    return "свободна"
                case "з":
                    return "занятая"
                case _:
                    print ("Input error")
        case "преп": 
            match Value:
                case "х"|"хв"|"хвост":
                    return "хвост"
                case "к"|"кр"|"красный":
                    return "красный светофор"
                case "с"|"стр"|"стрелка":
                    return "стрелка"
                case _:
                    print ("Input error")
        case "ен": 
            try:
                Value = bytes.fromhex(Value)
                return Value
            except: 
                print("Параметр должен быть в HEX")
             
            
            



# print("{0}{1}".format(len(InitString), InitString))
begin_of_Init= search("{",None, 0)
end_of_Init= search("}",None, 0)
endtypemark= search (":",None, 0)
coord_begin= search(" ",None, 0)
coord_end= search(" ",None,coord_begin+1)
# if(end!=None and beg!= None):           
#     print ("yes")
# else:
#     print ('no')
ObjType = InitString [begin_of_Init+1:endtypemark]   # Маркер типа объекта

Numbers = InitString [coord_begin+1:coord_end].split(sep='.',maxsplit=2)  
if (Numbers[0].isdigit()):
    Num_of_Kompl = int(Numbers[0])                       # Номер комплекта компонента
if (Numbers[1].isdigit()):
    Num_of_Obj = int(Numbers[1])                         # номер объекта

if (not coord_end): pass
elif(not coord_end+1 == end_of_Init):
    coord_begin = search(None,"=",coord_end+1)
    State1 = InitString[coord_end+1:coord_begin].strip()
    coord_end = search(" ",None ,coord_begin+2)
    Value1 = InitString[coord_begin+1:coord_end].strip()
    if Value1=="": 
        print("exit")
    Value1=identify(State1,Value1)

if (not coord_end): pass
elif(not coord_end+1 == end_of_Init):
    coord_begin = search(None,"=",coord_end+1)
    if (not coord_begin): pass
    elif(not coord_begin+1 == end_of_Init):
        State2 = InitString[coord_end+1:coord_begin].strip()
        coord_end = search(" ",None ,coord_begin+2)
        Value2 = InitString[coord_begin+1:coord_end].strip()
        if Value2=="": print("exit")
        Value2=identify(State2,Value2)

if (not coord_end): pass 
elif(not coord_end+1 == end_of_Init):
    coord_begin = search(None,"=",coord_end+1)
    if (not coord_begin): pass
    elif(not coord_begin+1 == end_of_Init):
        State3 = InitString[coord_end+1:coord_begin].strip()
        coord_end = search(" ",None ,coord_begin+2)
        Value3 = InitString[coord_begin+1:coord_end].strip()
        if Value3=="": print("exit")
        Value3 = identify(State3,Value3)

if (not coord_end): pass
elif(not coord_end+1 == end_of_Init):
    coord_begin = search(None,"=",coord_end+1)
    if (not coord_begin): pass
    elif(not coord_begin+1 == end_of_Init):
        State4 = InitString[coord_end+1:coord_begin].strip()
        coord_end = search(" ",None ,coord_begin+2)
        Value4 = InitString[coord_begin+1:coord_end].strip()
        if Value4=="": print("exit")
        Value4 = identify(State4,Value4)

if (not coord_end): pass
elif(not coord_end+1 == end_of_Init):
    coord_begin = search(None,"=",coord_end+1)
    if (not coord_begin): pass
    elif(not coord_begin+1 == end_of_Init):
        State5 = InitString[coord_end+1:coord_begin].strip()
        coord_end = search(" ",None ,coord_begin+2)
        Value5 = InitString[coord_begin+1:coord_end].strip()
        if Value5=="": print("exit")
        Value5 = identify(State5,Value5)

          
#         sost1 = InitString[coord_end+1:coord_begin]
#     #else Возврат к вводу 
print("")