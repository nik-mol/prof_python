from datetime import date

from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':

    date_now = date.today().strftime("%d.%m.%Y")
    print(f"Добрый день! Текущая дата: {date_now}")

    calculate_salary()
    get_employees()