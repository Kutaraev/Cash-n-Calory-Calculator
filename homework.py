import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        current_date = ((dt.datetime.now()).date())
        today_stats = 0
        for i in self.records:
            if i.date == current_date:
                today_stats += i.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        current_date = ((dt.datetime.now()).date())
        time_delta = dt.timedelta(days=7)
        for i in self.records:
            if (current_date - time_delta) <= i.date <= current_date:
                week_stats += i.amount
        return week_stats


class CashCalculator(Calculator):
    USD_RATE = 73.33
    EURO_RATE = 87.91

    def get_today_cash_remained(self, currency):
        cash_balance = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_final = round(cash_balance / self.USD_RATE, 2)
            if cash_final > 0:
                return f'На сегодня осталось {cash_final} USD'
            elif cash_final == 0:
                return 'Денег нет, держись'
            else:
                return f'Денег нет, держись: твой долг - {abs(cash_final)} USD'

        elif currency == 'eur':
            cash_final = \
                round(cash_balance / self.EURO_RATE, 2)
            if cash_final > 0:
                return f'На сегодня осталось {cash_final} Euro'
            elif cash_final == 0:
                return 'Денег нет, держись'
            else:
                return \
                    f'Денег нет, держись: твой долг - {abs(cash_final)} Euro'

        elif currency == 'rub':
            cash_final = (self.limit - self.get_today_stats())
            if cash_final > 0:
                return f'На сегодня осталось {cash_final} руб'
            elif cash_final == 0:
                return 'Денег нет, держись'
            else:
                return f'Денег нет, держись: твой долг - {abs(cash_final)} руб'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        delta_calories = self.limit - self.get_today_stats()
        if delta_calories > 0:
            return 'Сегодня можно съесть что-нибудь ещё, ' \
                f'но с общей калорийностью не более {delta_calories} кКал'

        else:
            return 'Хватит есть!'


class Record:
    def __init__(self, amount, comment,
                 date=((dt.datetime.now()).date()).strftime('%d.%m.%Y')):
        self.amount = amount
        self.comment = comment
        self.date = (dt.datetime.strptime(date, '%d.%m.%Y')).date()
