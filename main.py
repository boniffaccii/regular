"""Ваша задача: починить адресную книгу, используя регулярные выражения.
Структура данных будет всегда:
lastname,firstname,surname,organization,position,phone,email
Предполагается, что телефон и e-mail у человека может быть только один.
Необходимо:

поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
привести все телефоны в формат +7(999)999-99-99.
Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
объединить все дублирующиеся записи о человеке в одну."""

from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
f_contacts_list = []
great_cl = []
for row in contacts_list:
    if row[0] == 'lastname':
        pass
    elif row[2] == '':
        a = row[0] + ' ' + row[1] + ' ' + row[2]
        split1 = re.split(r'\s', a)
        io = list(split1)
        for i in range(3):
            row[i] = io[i]

    pattern = r'(8|\+7)?\s*\(*(495)\)*-*\s*(\d\d\d)-*(\d\d)-*(\d\d)\s*\(*(доб)*\.*\s*(\d+)*\)*'
    if re.findall(r'доб', row[5]):
        phone = re.sub(pattern, r'+7(\2)\3-\4-\5 доб.\7', row[5])
        row[5] = phone
    else:
        phone = re.sub(pattern, r'+7(\2)\3-\4-\5', row[5])
        row[5] = phone

    print(row)
    f_contacts_list.append(row)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(f_contacts_list)
