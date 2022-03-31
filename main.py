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

# from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
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
    f_contacts_list.append(row)

for row1 in f_contacts_list:
    for row2 in f_contacts_list:
        if row1[0] == row2[0] and row1[1] == row2[1]:
            if row1 != row2:
                d = 0
                result = []
                for d in range(len(row1)):
                    if row1[d] == '':
                        result.append(row2[d])
                    else:
                        result.append(row1[d])
                f_contacts_list.remove(row2)
                f_contacts_list.append(result)
                f_contacts_list.remove(row1)
                break

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(f_contacts_list)
