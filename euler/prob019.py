

class Day:
    def __init__(self, day: int):
        self.days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        self.day = day #choose starting day 0 = monday, 6 = sunday
    
    def get_current_day(self):
        return self.days[self.day]
    
    def increment_day(self):
        self.day = (self.day + 1) % 7

class Month:
    def __init__(self, day: Day, month: int):
        self.months = ['january','february','march','april','may','june','july','august','september','october','november','december']
        self.month = month
        self.day = day

    def get_current_month(self):
        return self.months[self.month]
    
    def increment_month(self):
        ...
# we are starting on 1 January 1901 which is a Tuesday
class Calendar:
    def __init__(self, day_date: int, month: int, year: int, day_name: int):
        self.day_date = day_date # different depending on the month
        self.month = month # mod 12
        self.year = year    
        self.day_name = day_name # mod 7
        if self.year % 4 == 0:
            self.leap = True
        else:
            self.leap = False

    def get_day_name(self):
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        return days[self.day_name]
    def get_month_name(self):
        months = ['january','february','march','april','may','june','july','august','september','october','november','december']
        return months[self.month]
    

    def add_one_day(self):
        
        #always increment the day
        self.day_name = (self.day_name + 1) % 7

        #check for the end of the month with thirty days
        thirty_months = [8,3,5,10]
        thirty_one_months = [0,2,4,6,7,9,11]
        if self.day_date == 30 and self.month in thirty_months: #that last one is february
            self.day_date = 1
            self.month = (self.month + 1) % 12 # we dont have to worry about the end of the year because december has 31 days
        
        elif self.day_date == 31 and self.month in thirty_one_months:
            self.day_date = 1 # date goes back to one
            if self.month == 11: # add to the year
                self.year += 1
                self.leap = True if self.year % 4 == 0 else False
            self.month = (self.month + 1) % 12 # increment the month

        # february :(
        elif self.day_date == 28 and self.month == 1 and not self.leap: #thats february :/
            self.day_date = 1
            self.month = (self.month + 1) % 12
        elif self.day_date == 29 and self.month == 1 and self.leap:
            self.day_date = 1
            self.month = (self.month + 1) % 12

        # if its not the end of a month just add a day :)
        else:
            self.day_date += 1
        

# d = Day(0)

# for i in range(14):
#     print(d.get_current_day())
#     d.increment_day()

def counting_sundays():
    cal = Calendar(1, 0, 1901, 1)

    cnt = 0
    while cal.year < 2001:
        if cal.day_name == 6 and cal.day_date == 1:
            print(f"{cal.day_date} {cal.get_month_name()} {cal.year} {cal.get_day_name()}")
            cnt += 1
        cal.add_one_day()

    print(cnt)

counting_sundays()