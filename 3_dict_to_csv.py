import csv
"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('my_csv_file.csv', 'w', encoding='utf-8', newline='') as file:
        columns = ['name', 'age', 'job']
        data = [
            {'name': 'Гендальф', 'age': '2500', 'job': 'Порамситель проблем'},
            {'name': 'Сарумян', 'age': '2500', 'job': 'Просто запустался' },
            {'name': 'Келебримбор', 'age': '1500', 'job': 'Скромный кузнец'},
            {'name': 'Талион', 'age': '28', 'job': 'тачка Келебримбора'}
        ]
        w = csv.DictWriter(file, fieldnames=columns, delimiter=';')
        w.writeheader()
        w.writerows(data)


if __name__ == "__main__":
    main()
