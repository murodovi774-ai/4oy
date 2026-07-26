class MyDate:
    MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", 
              "Iyul", "Avgust", "Sentyabr", "Oktabr", "Noyabr", "Dekabr"]
    DAY_IN_MONTHS = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  
    def __init__(self, day, month, year):
        if self.isValidDate(day,month,year):
            self.__day=day
            self.__month=month
            self.__year=year
        else:
            raise ValueError("Noto'g'ri sana kiritildi!")    

    def isLeapYear(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def isValidDate(self, day, month, year): 
        if 1<=year<=9999:
            if 1<=month<=12:
                days=self.DAY_IN_MONTHS[month]
                if month==2 and self.isLeapYear(year):
                    days+=1
                if 1<=day<=days:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
                    

    def setDate(self, day, month, year):
        if self.isValidDate(day,month,year):
            self.__day=day
            self.__month=month
            self.__year=year
        else:
            raise ValueError("Noto'g'ri sana kiritildi!") 
        
    def nextDay(self):
        days=self.DAY_IN_MONTHS[self.__month]
        if self.__day < days:
            self.__day += 1
        else:
            self.__day = 1

            if self.__month < 12:
               self.__month += 1
            else:
               self.__month = 1
               self.__year += 1
    def previousDay(self):
        if self.__day>1:
            self.__day-=1
        else:
            if self.__month==1:
                self.__year-=1
                self.__month=12
            else:
                self.__month-=1
            days=self.DAY_IN_MONTHS[self.__month]
            if self.__month ==2 and self.isLeapYear(self.__year):
                days+=1
            self.__day=days            
                    
    def nextMonth(self):
        if self.__month < 12:
            self.__month += 1
        else:
            self.__month = 1
            self.__year += 1

        days = self.DAY_IN_MONTHS[self.__month]

        if self.__month == 2 and self.isLeapYear(self.__year):
            days += 1

        if self.__day > days:
            self.__day = days
    def previousMonth(self):
        if self.__month > 1:
            self.__month -= 1
        else:
            self.__month = 12
            self.__year -= 1

        days = self.DAY_IN_MONTHS[self.__month]

        if self.__month == 2 and self.isLeapYear(self.__year):
            days += 1

        if self.__day > days:
            self.__day = days
    
    def nextYear(self):
        self.__year += 1
        if self.__month == 2 and self.__day == 29:
            if not self.isLeapYear(self.__year):
               self.__day = 28
        

    def previousYear(self):
        self.__year-=1
        if self.__month == 2 and self.__day == 29:
           if not self.isLeapYear(self.__year):
              self.__day = 28

    def __str__(self):
        return f"{self.__day}-{self.MONTHS[self.__month-1]} {self.__year} yil"
    
sana = MyDate(1, 1, 2023)
sana.previousDay()
print(sana)