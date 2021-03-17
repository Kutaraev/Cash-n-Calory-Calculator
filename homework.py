import datetime as dt

DATE_FORMAT = '%d.%m.%Y'


class Record:
    def __init__(self, amount, comment, date=None):
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()
        self.amount = amount
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        current_date = dt.date.today()
        today_stats = sum(i.amount for i in self.records
                          if i.date == current_date)
        return today_stats

    def get_week_stats(self):
        current_date = dt.date.today()
        week_ago = current_date - dt.timedelta(days=6)
        week_stats = sum(i.amount for i in self.records
                         if week_ago <= i.date <= current_date)
        return week_stats

    def get_balance(self):
        return self.limit - self.get_today_stats()


class CashCalculator(Calculator):
    USD_RATE = 73.33
    EURO_RATE = 87.91
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        currency_rate = {'usd': (self.USD_RATE, 'USD'),
                         'eur': (self.EURO_RATE, 'Euro'),
                         'rub': (self.RUB_RATE, 'руб')}
        today_balance = self.get_balance()
        if currency not in currency_rate:
            raise ValueError('Введено неверное обозначение валюты.')
        (currency_val, currency_name) = currency_rate.get(currency)
        if today_balance == 0:
            return 'Денег нет, держись'
        cash_final = round(today_balance / currency_val, 2)
        if cash_final > 0:
            return f'На сегодня осталось {cash_final} {currency_name}'
        abs_final = abs(cash_final)
        return f'Денег нет, держись: твой долг - {abs_final} {currency_name}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calory_balance = self.get_balance()
        if calory_balance > 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {calory_balance} кКал')
        return 'Хватит есть!'
