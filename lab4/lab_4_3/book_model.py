import pandas as pd


def get_publisher(conn):
    return pd.read_sql(
        """
        SELECT publisher.*, count(book_id)
        FROM publisher
            join book b on publisher.publisher_id = b.publisher_id
        GROUP BY b.publisher_id
        ORDER BY publisher_name
            """,
        conn)


def get_author(conn):
    return pd.read_sql("""
        SELECT a.*, count(book_id)
        FROM book_author
            join author a on book_author.author_id = a.author_id
        GROUP BY author_name
        ORDER BY author_name;
            """, conn)


def get_genre(conn):
    return pd.read_sql(
        """
        SELECT genre.*, count(book_id)
        FROM genre
            join book b on genre.genre_id = b.genre_id
        GROUP BY b.genre_id
        ORDER BY genre_name;
        """, conn)


def card(conn, publishers, genres, authors):
    if len(publishers) == 1:
        publishers = f'({publishers[0]})'
    elif len(genres) == 1:
        genres = f'({genres[0]})'
    elif len(authors) == 1:
        authors = f'({authors[0]})'
    return pd.read_sql(f'''
        SELECT
            title AS 'Название',
            group_concat(DISTINCT author_name) AS 'Авторы',
            genre_name AS 'Жанр',
            publisher_name AS 'Издательство',
            year_publication AS 'Год_издания',
            available_numbers AS 'Количество'
        FROM book
        JOIN genre USING(genre_id)
        JOIN publisher USING(publisher_id)
        JOIN book_author USING(book_id)
        JOIN author USING(author_id)
        GROUP BY book_id
        HAVING (genre_id IN {genres} OR {not genres})
            AND (publisher_id IN {publishers} OR {not publishers})
            AND (author_id IN {authors} OR {not authors})
        ORDER BY
            title,
            available_numbers DESC,
            genre_name,
            year_publication DESC 
    ''', conn)
