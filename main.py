from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


def today_date():
    date = datetime.now()
    print(date.date())


if __name__ == '__main__':
    today_date()
    calculate_salary()
    get_employees()
