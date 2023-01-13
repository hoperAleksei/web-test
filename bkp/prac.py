import sqlite3
import pprint

if __name__ == '__main__':
    con = sqlite3.connect("../lab4/lab_4_1/library.sqlite")

    f_damp = open('library.db', 'r', encoding='utf-8-sig')
    damp = f_damp.read()
    f_damp.close()
    con.executescript(damp)
    con.commit()

    cursor = con.cursor()

    cursor.execute("""SELECT book_id, genre_id
FROM book AS BO
WHERE (SELECT COUNT(1) FROM book_reader WHERE BO.book_id = book_reader.book_id) >= (SELECT max(l)
                                                                                    FROM (SELECT (SELECT COUNT(1)
                                                                                                  FROM book_reader AS BB
                                                                                                  WHERE BB.book_id = b.book_id) AS l
                                                                                          FROM book AS b WHERE bo.genre_id = B.genre_id));""")
    print(cursor.fetchall())

    con.close()
