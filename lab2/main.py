import sqlite3

if __name__ == '__main__':

    con = sqlite3.connect("sqlite/travel_agency.sqlite")

    cur = con.cursor()

    with open('sqlite/init.sql', 'r', encoding='utf-8-sig') as f:
        cur.executescript(f.read())

    with open('sqlite/fixtures.sql', 'r', encoding='utf-8-sig') as f:
        cur.executescript(f.read())

    con.commit()

    with open('sqlite/queries.sql', 'r', encoding='utf-8-sig') as f:
        queries = f.read().split(';')
        for q in queries:
            cur.execute(q)
            print(q)
            print(cur.fetchall())

    con.close()
