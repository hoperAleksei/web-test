import sqlite3

con = sqlite3.connect("../sqlite/travel_agency.sqlite")
f_damp = open('sqlite/travel_agency.db', 'r', encoding='utf-8-sig')
# читаем данные из файла
damp = f_damp.read()
# закрываем файл с дампом
f_damp.close()
# запускаем запросы
con.executescript(damp)
# сохраняем информацию в базе данных
con.commit()
# # создаем курсор
# cursor = con.cursor()
# # выбираем и выводим записи из таблиц author, reader
# cursor.execute("SELECT * FROM author")
# print(cursor.fetchall())
# cursor.execute("SELECT * FROM reader")
# print(cursor.fetchall())
# # закрываем соединение с базой
# con.close()
# # создаем базу данных и устанавливаем соединение с ней
# con = sqlite3.connect("library.sqlite")
# # создаем курсор
# cursor = con.cursor()
# # выбираем и выводим записи из таблиц author, reader
# cursor.execute('''
#  SELECT
#  title,
#  publisher_name,
#  year_publication
#  FROM book
#  JOIN genre USING (genre_id)
#  JOIN publisher USING (publisher_id)
#  WHERE genre_name = :p_genre AND year_publication > :p_year
# ''',{"p_genre": "Детектив", "p_year": 2016})
# print(cursor.fetchall())
# # закрываем соединение с базой
# con.close()
