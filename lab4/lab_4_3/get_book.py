if __name__ == '__main__':

    from jinja2 import Template
    import sqlite3
    from book_model import get_publisher, get_author, get_genre, card

    genres = tuple()
    authors = tuple()
    publishers = tuple()
    conn = sqlite3.connect("library.sqlite")

    with open("library.db", "r", encoding="utf-8-sig") as f:
        damp = f.read()
        conn.executescript(damp)
        conn.commit()

    df_author = get_author(conn)
    df_publisher = get_publisher(conn)
    df_genre = get_genre(conn)
    df_card = card(conn, publishers, genres, authors)
    conn.close()

    # f_template = open('template.html')
    file = open('book_templ.html', 'r', encoding='utf-8')
    # f_template.close()
    html = file.read()
    file.close()

    template = Template(html)
    result_html = template.render(
        authors=df_author,
        publishers=df_publisher,
        genres=df_genre,
        card=df_card,
        sel_authors=authors,
        sel_publishers=publishers,
        sel_genres=genres,
        len=len
    )

    f = open('book.html', 'w', encoding='utf-8-sig')
    f.write(result_html)
    f.close()
