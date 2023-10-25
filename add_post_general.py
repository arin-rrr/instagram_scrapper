import sqlite3 as sql
from aifc import Error
from instagrapi import Client

'''
Добавление записей в таблицы posts_general и description_post
'''

media_type = {1: 'Photo', 2: ['Video', 'IDTV', 'Reel'], 8: 'Album'}


def create_connection(db_file):
    conn = None
    try:
        conn = sql.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_posts_general(conn, account):
    query = ''' INSERT INTO posts_general(user_id, post_id, taken_at, media_type)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(query, account)
    conn.commit()
    return cur.lastrowid


def create_posts_description(conn, account):
    query = ''' INSERT INTO posts_general(post_id, comment_count, like_count, caption)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(query, account)
    conn.commit()
    return cur.lastrowid


def main():
    database = "instagram_instagram.db"
    conn = create_connection(database)

    cl = Client()
    cl.login('vikamir15', 'vika_mir_15')
    with conn:
        for i in cl.user_following(cl.user_id):
            for j in cl.user_medias(i):
                if j.media_type == 1 or j.media_type == 8:
                    general = (int(cl.user_info(i).pk), str(j.id), j.taken_at.date(), media_type[j.media_type])
                    create_posts_general(conn, general)

                    description = (str(j.id), j.comment_count, j.like_count, j.caption_text)
                    create_posts_description(conn, description)
                else:
                    if j.product_type == 'feed':
                        general = (int(cl.user_info(i).pk), str(j.id), j.taken_at.date(), media_type[j.media_type][0])
                        create_posts_general(conn, general)

                        description = (str(j.id), j.comment_count, j.like_count, j.caption_text)
                        create_posts_description(conn, description)
                    elif j.product_type == 'igtv':
                        general = (int(cl.user_info(i).pk), str(j.id), j.taken_at.date(), media_type[j.media_type][1])
                        create_posts_general(conn, general)

                        description = (str(j.id), j.comment_count, j.like_count, j.caption_text)
                        create_posts_description(conn, description)
                    else:
                        general = (int(cl.user_info(i).pk), str(j.id), j.taken_at.date(), media_type[j.media_type][2])
                        create_posts_general(conn, general)

                        description = (str(j.id), j.comment_count, j.like_count, j.caption_text)
                        create_posts_description(conn, description)

if __name__ == '__main__':
    main()