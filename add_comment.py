import sqlite3 as sql
from aifc import Error
from instagrapi import Client

'''
Добавление записей в таблицы comment_info и commentators
'''


def create_connection(db_file):
    conn = None
    try:
        conn = sql.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_comment_info(conn, account):
    query = ''' INSERT INTO comment_info(comment_id, post_id, commentator_id, comment, created_at)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(query, account)
    conn.commit()
    return cur.lastrowid


def create_commentators(conn, account):
    query = ''' INSERT INTO commentators(commentator_id, post_id, username)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(query, account)
    conn.commit()
    return cur.lastrowid


def main():
    database = "instagram_instagram.db"
    conn = create_connection(database)

    cl = Client()
    cl.login('vikamir15', 'vika_mir_15')
    commentators = []
    h = 1
    for i in cl.user_following(cl.user_id):
        for j in cl.user_medias(i):
            for com in cl.media_comments(j.id):
                general = (h, str(com.pk), int(com.user.pk), com.text, com.created_at_utc)
                create_comment_info(conn, general)
                if int(com.user.pk) not in commentators:
                    comm = (int(com.user.pk), str(j.id), com.user.username)
                    create_commentators(conn, comm)
                    commentators.append(int(com.user.pk))


if __name__ == '__main__':
    main()
