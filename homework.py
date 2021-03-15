import datetime as dt
DATE_FORMAT = '%d.%m.%Y'


class Record:
    def __init__(self, amount, comment, date=None):
        if date is None:
            date = dt.date.today().strftime(DATE_FORMAT)
        self.date = (dt.datetime.strptime(date, DATE_FORMAT)).date()
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
        today_stats = 0
        today_stats = sum(i.amount for i in self.records
                          if i.date == current_date)
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        current_date = dt.date.today()
        time_delta = dt.timedelta(days=6)
        week_ago = current_date - time_delta
        for i in self.records:
            if week_ago <= i.date <= current_date:
                week_stats += i.amount
        return week_stats

    def day_bal(self):
        return self.limit - self.get_today_stats()


class CashCalculator(Calculator):
    USD_RATE = 73.33
    EURO_RATE = 87.91
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        currency_rate = {'usd': (self.USD_RATE, 'USD'),
                         'eur': (self.EURO_RATE, 'Euro'),
                         'rub': (self.RUB_RATE, 'руб')}
        cash_val = currency_rate.get(currency)
        cash_final = round(self.day_bal() / cash_val[0], 2)
        abs_final = abs(cash_final)
        if cash_final > 0:
            return f'На сегодня осталось {cash_final} {cash_val[1]}'
        elif cash_final == 0:
            return 'Денег нет, держись'
        return f'Денег нет, держись: твой долг - {abs_final} {cash_val[1]}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.day_bal() > 0:
            return 'Сегодня можно съесть что-нибудь ещё, ' \
                f'но с общей калорийностью не более {self.day_bal()} кКал'
        return 'Хватит есть!'
