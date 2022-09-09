from pprint import pprint
from data import pattern, substitution
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

new_contacts_list = []
for contact_list in contacts_list:
    b = []
    new_contacts_list.append(b)

    if len(contact_list) > 7:
        del contact_list[-1]

    for contact in contact_list:
        b.append(re.sub(pattern, substitution, contact))

for i in range(len(new_contacts_list)):
    j = (" ".join(contacts_list[i]).split())
    new_contacts_list[i][0] = j[0]
    new_contacts_list[i][1] = j[1]
    new_contacts_list[i][2] = j[2]

count = 1
for contact in new_contacts_list:
    for contact_ in new_contacts_list[count:]:
        if contact[0] == contact_[0] and contact[1] == contact_[1]:
            if contact[2] == '':
                contact[2] = contact_[2]
            if contact[3] == '':
                contact[3] = contact_[2]
            if contact[4] == '':
                contact[4] = contact_[4]
            if contact[5] == '':
                contact[5] = contact_[5]
            if contact[6] == '':
                contact[6] = contact_[6]
            new_contacts_list.remove(contact_)
    count += 1


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_contacts_list)
