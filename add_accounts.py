import sqlite3 as sql
from aifc import Error
from instagrapi import Client

'''
Добавление записей в таблицу accounts
'''

def create_connection(db_file):
    conn = None
    try:
        conn = sql.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_accounts(conn, account):
    query = ''' INSERT INTO accounts(user_id,username,full_name, media_count, follower_count, following_count)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(query, account)
    conn.commit()
    return cur.lastrowid


def add_pic_accounts(photo, conn):
    query = '''update accounts set profile_photo = ? where user_id = 29776346449'''
    cur = conn.cursor()
    with open(photo, mode='rb') as f:
        binary = sql.Binary(f.read())
        cur.execute(query, (binary,))
        conn.commit()

def main():
    database = "instagram_instagram.db"

    conn = create_connection(database)
    cl = Client()
    cl.login('vikamir15', 'vika_mir_15')
    with conn:
        for i in cl.user_following(cl.user_id):
            account = (int(cl.user_info(i).pk), cl.user_info(i).username, cl.user_info(i).full_name,
                       cl.user_info(i).media_count, cl.user_info(i).follower_count,
                       cl.user_info(i).following_count)
            create_accounts(conn, account)

if __name__ == '__main__':
    main()