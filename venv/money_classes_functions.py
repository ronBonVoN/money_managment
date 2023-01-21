from datetime import date
from datetime import datetime
from datetime import timedelta

date_format = '%m.%d.%y' #all dates need to be written in the same way

class Transaction():
    def __init__(self, amt, type, date, reason): #type = withdraw or deposite, reason will be user imput
        super().__init__()
        self.date = datetime.strptime(date, date_format)
        self.amt = amt
        self.type = type
        self.reason = reason

    def view(self):
        return f'{self.date}: ${self.amt} {self.type}, reason: {self.reason}'

class Log:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.txt = self.create_txt() #create text file
        self.dict = self.build_dict() #dictionary to record all transactions

    def create_txt(self):
        self.txt = open(f'money log: {self.start}-{self.end}.txt', 'a')
        self.txt.close()

    def build_dict(self):
        self.dict = {}
        date = datetime.strptime(self.start, '%m.%d.%y')
        while date != datetime.strptime(self.end, '%m.%d.%y'):
            self.dict[date.strftime('%m.%d.%y')]  = []
            date += timedelta(days=1)

    def add(self, date, transaction):
        self.dict[date] = self.dict[date].append(transaction)

    def write(self, str):
        file = open(self.pathname, 'w')
        file.write(str)
        file.close()

def withdraw(log, amt, date, reason):
    withdraw = Transaction(amt, 'withdraw', date, reason)
    log.add(date, withdraw)
    log.write(withdraw.view())

def deposite(log, amt, date, reason):
    deposite = Transaction(amt, 'deposite', date, reason)
    log.add(date, withdraw)
    log.write(deposite.view())





































