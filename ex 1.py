class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                return f'Верная дата'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Сегодня: {Data.extract(self.day_month_year)}'


print(Data.valid(35, 11, 2020))
print(Data.valid(11, 13, 2015))
print(Data.valid(21, 12, 2012))
print(Data.extract('11 - 11 - 2011'))
print(Data.extract('01 - 01 - 2021'))
