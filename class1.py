#"{Мкс: 0.2 дист= 5 лог = пзг физ =з преп = хв ен = 4f}"


class Train():

    def Input_String(self,InitString):
        #InitString = "{Мкс: 0.2 лог = пзг дист= 5 физ =з преп  = хв } ен = 4f}"
        
        InitString = InitString.lower()
        begin_of_Init= self.search("{",InitString, 0)
        end_of_Init= self.search("}",InitString, 0)
        if (begin_of_Init is None or end_of_Init is None):
            print ("Нет меток начала и/или конца описания объекта")
            return False
        if InitString[end_of_Init-1]== " " and InitString[end_of_Init-2]== " ":
            print("Не используйте более двух пробелов подряд.")
            return False
        
        
        ObjType = InitString [self.search("{",InitString, 0)+1: self.search (":",InitString, 0)]   # Маркер типа объекта
        if ObjType.replace(" ","") == "":
            print("Не введён тип объекта")
            return False
        
        coord_begin=self.search (":",InitString, 0)
        if coord_begin is None:
            print("Не найден разделитель")
            return False
        coord_end= self.search(".",InitString,coord_begin+2)
        if coord_end is None: 
            print("Не найден разделитель")
            return False
        Num_of_Kompl = InitString[coord_begin+1:coord_end]
        coord_begin = self.search(" ",InitString,coord_end+2)
        Num_of_Obj = InitString[coord_end+1:coord_begin]

        if Num_of_Kompl.replace(" ","") == "" or Num_of_Obj.replace(" ","") == "":
            print("Ошибка ввода, возможно Вы не ввели номер объекта/комплекта или используете лишние пробелы.")
            return False
        try:
            Num_of_Kompl = int(Num_of_Kompl)                       # Номер комплекта компонента
            Num_of_Obj = int(Num_of_Obj.replace("}",""))                           # номер объекта
        except:
            print("Ошибка ввода (Это не число)")
            return False
        
        if (not coord_begin or coord_begin+1 >= end_of_Init): pass
        else:
            coord_end = self.search("=",InitString,coord_begin+1)
            State1 = InitString[coord_begin+1:coord_end].strip()
            coord_begin = self.search(" ",InitString,coord_end+2)
            Value1 = InitString[coord_end+1:coord_begin].strip()
            if Value1=="": 
                print("Ошибка ввода, возможно вы не ввели параметр \"{0}\" или используете лишние пробелы.".format(State1))
                return False
            Value1=self.identify(State1,Value1)
            if Value1 is None: return False
            
        
        if (not coord_begin or coord_begin+1 >= end_of_Init): pass
        else:
            coord_end = self.search("=",InitString,coord_begin+1)
            State2 = InitString[coord_begin+1:coord_end].strip()
            coord_begin = self.search(" ",InitString,coord_end+2)
            Value2 = InitString[coord_end+1:coord_begin].strip()
            if Value2=="": 
                print("Ошибка ввода, возможно вы не ввели параметр \"{0}\" или используете лишние пробелы.".format(State2))
                return False
            if (not State2 == State1):
                Value2=self.identify(State2,Value2)
                if Value2 is None: return False
            else:
                print ("Параметр {0} уже был использован.".format(State2))
                return False

        if (not coord_begin or coord_begin+1 >= end_of_Init): pass
        else:
            coord_end = self.search("=",InitString,coord_begin+1)
            State3 = InitString[coord_begin+1:coord_end].strip()
            coord_begin = self.search(" ",InitString,coord_end+2)
            Value3 = InitString[coord_end+1:coord_begin].strip()
            if Value3=="": 
                print("Ошибка ввода, возможно вы не ввели параметр \"{0}\" или используете лишние пробелы.".format(State3))
                return False
            if (not State3 == State1 or not State3 == State2):
                Value3=self.identify(State3,Value3)
                if Value3 is None: return False
            else:
                print ("Параметр {0} уже был использован.".format(State3))
                return False


        if (not coord_begin or coord_begin+1 >= end_of_Init): pass
        else:
            coord_end = self.search("=",InitString,coord_begin+1)
            State4 = InitString[coord_begin+1:coord_end].strip()
            coord_begin = self.search(" ",InitString,coord_end+2)
            Value4 = InitString[coord_end+1:coord_begin].strip()
            if Value4=="": 
                print("Ошибка ввода, возможно вы не ввели параметр \"{0}\" или используете лишние пробелы.".format(State4))
            if (not State4 == State1 or not State4 == State2 or not State4 == State3):
                Value4=self.identify(State4,Value4)
                if Value4 is None: return False
            else:
                print ("Параметр {0} уже был использован.".format(State4))
                return False


        if (not coord_begin or coord_begin+1 >= end_of_Init): pass
        else:
            coord_end = self.search("=",InitString,coord_begin+1)
            State5 = InitString[coord_begin+1:coord_end].strip()
            coord_begin = self.search(" ",InitString,coord_end+2)
            Value5 = InitString[coord_end+1:coord_begin].strip()
            if Value5=="": 
                print("Ошибка ввода, возможно вы не ввели параметр \"{0}\" или используете лишние пробелы.".format(State5))
            if (not State5 == State1 or not State5 == State2 or not State5 == State3 or not State5 == State4):
                Value5=self.identify(State5,Value5)
                if Value5 is None: return False
            else:
                print ("Параметр {0} уже был использован.".format(State5))
                return False
        print("")
        try:
            self.ObjType = ObjType
        except: pass
        
        try:
            self.Num_of_Kompl=Num_of_Kompl
            self.Num_of_Obj = Num_of_Obj
        except: pass
        
        try:
            self.State1 = State1
            self.Value1 = Value1
        except: pass
        try:
            self.State2 = State2
            self.Value2 = Value2
        except: pass
        try:
            self.State3 = State3
            self.Value3 = Value3
        except: pass
        try:
            self.State4 = State4
            self.Value4 = Value4
        except: pass
        try:
            self.State5 = State5
            self.Value5 = Value5
        except: pass
    # def __setattr__(self, __name: str, __value: Any) -> None:
    #     pass


    def object_print(self):
        try:print("Тип объекта:\t\t{0} ".format(self.ObjType))
        except: pass
        try: print("Номер комплекта объекта:{0}".format(self.Num_of_Kompl))
        except: pass
        try: print("Номер объекта:\t\t{0} ".format(self.Num_of_Obj))
        except: pass
        try: print ("Параметр {0}:\t\t{1}".format(self.State1,self.Value1))
        except: pass
        try: print ("Параметр {0}:\t\t{1}".format(self.State2,self.Value2))
        except: pass
        try: print ("Параметр {0}:\t\t{1}".format(self.State3,self.Value3))
        except: pass
        try: print ("Параметр {0}:\t\t{1}".format(self.State4,self.Value4))
        except: pass
        try: print ("Параметр {0}:\t\t{1}".format(self.State5,self.Value5))
        except: pass
    
    
    def search(self,simv,String,i):
        
        for i in range(i,len(String)):
            if String[i] == simv:
                return i
        return None    

    def identify(self,State,Value):
        Value = Value.replace("}","")
        match State:
            case "дист":
                try:
                    Value=int(Value)
                    if 0 <= Value <= 31: return Value
                    else: 
                        print("Параметр \"{0}\" должен быть от 0 до 31".format(State))
                        return None
                except:
                    print("Атрибут \"{0}\" должен быть числом".format(State))
                    return None
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
                        return None
            case "физ": 
                match Value:
                    case "с"|"св"|"своб":
                        return "свободна"
                    case "з":
                        return "занятая"
                    case _:
                        print ("Недопустимый параметр для: \"{0}\" ".format(State))
                        return None
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
                        return None
            case "ен": 
                try:
                    Value = bytes.fromhex(Value)
                    return Value
                except: 
                    print("Параметр \"{0}\" должен быть в HEX".format(State))
                    return None
            case _:
                print("Неизвестный атрибут \"{0}\" ".format(State))
                return None
             

