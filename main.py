# Задание 1 Вывести количество записей, у которых в поле ```Название``` строка длиннее 30 символов.

import csv
import random

with open('books-en.csv') as fh:
    count = 0
    for Bookname in fh :
        lst= Bookname.split(";") 
        if len(lst[1]) > 30:
            count += 1
print(count)

# ЗАДАНИЕ 2 Реализовать поиск книги по автору, использовать ограничение на выдачу не более 150 рублей

author=input("Type author's name:" )

with open('books-en.csv') as fh:
    for Bookname in fh :
        lst= Bookname.split(";")
        lst_6 = lst[6].replace("\n", "")
        lst_6 = lst_6.replace(",", ".")
        if lst[2] == author and float(lst_6) <=150:
            print(lst[2],lst[1])
        elif lst[2] == author and float(lst_6) > 150:
            print (lst[2],lst[1],'Too expensive! :( ')
            




# Задание 3  Реализовать генератор библиографических ссылок вида ```<автор>. <название> - <год>``` для 20 записей. Записи выбрать произвольно. Список сохраняется как отдельный файл текстового формата с нумерацией строк



with open('books-en.csv', 'r') as file:
    reader = csv.reader(file)
    rows = [row for row in reader]

random_index = random.sample(range(len(rows)), 20)

random_col = [rows[i] for i in random_index]

with open('list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(random_col)