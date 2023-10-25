import sqlite3 as sql
import tkinter as tk
from tkinter import ttk


def create_connection(db_file):
    conn = None
    conn = sql.connect(db_file)
    return conn


def db_n_comment(digit):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select * from comment_info''')
    evr = cur.fetchall()
    n_comment = {}
    vv = []
    for i in evr:
        if i[2] not in n_comment:
            n_comment[i[2]] = 1
        else:
            n_comment[i[2]] += 1
    for i in n_comment:
        if n_comment[i] >= digit:
            vv.append(i)
    cur.execute('select commentator_id, username from commentators')
    evr1 = cur.fetchall()
    dict1 = {}
    for i in evr1:
        dict1[i[0]] = i[1]
    res = {}
    for i in dict1:
        if i in vv:
            res[i] = dict1[i]
    return res


def n_comment():
    if not work5.get().isalpha():
        root = tk.Tk()
        root.resizable(False, False)
        root.title("Instagram DataBase")

        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)

        text = tk.Text(root, height=10)
        text.grid(row=0, column=0, sticky=tk.EW)

        scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        text['yscrollcommand'] = scrollbar.set
        comm_id = db_n_comment(int(work5.get()))
        if len(comm_id) == 0:
            position = '0.0'
            text.insert(position, 'Нет пользователей, оставивших такое количество комментариев')
        else:
            j = 2
            for i in comm_id:
                position3 = f'{j}.0'
                position4 = f'{j + 1}.0'
                position5 = f'{j + 2}.0'
                text.insert(position3, f'{i}\n')
                text.insert(position4, f'{comm_id[i]}\n')
                text.insert(position5, '\n')
                j += 3
            position1 = '1.0'
            position2 = '2.0'
            text.insert(position1, 'ID пользователя\n')
            text.insert(position2, 'USERNAME пользователя\n')
        root.mainloop()
    else:
        win2 = tk.Tk()
        win2.title('Ошибка')
        win2.geometry('400x100+100+100')
        win2.resizable(False, False)
        tk.Label(win2, text='Ошибка! Введите число', font=('Arial', 20, 'bold'), foreground='black',
                 justify=tk.CENTER).grid(row=0, column=0, stick='wens', padx=10, pady=10)
        win2.mainloop()


def db_comment_user(username):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select commentator_id, username from commentators''')
    evr = cur.fetchall()
    id_user = -1
    for i in evr:
        if i[1] == username:
            id_user = int(i[0])
    if id_user == -1:
        return False
    else:
        res = []
        cur.execute('select commentator_id, comment from comment_info')
        evr1 = cur.fetchall()
        for i in evr1:
            if i[0] == id_user:
                res.append(i[1])
        return res


def comment_user():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Instagram DataBase")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    text = tk.Text(root, height=10)
    text.grid(row=0, column=0, sticky=tk.EW)

    scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    text['yscrollcommand'] = scrollbar.set

    username = work.get()
    a = db_comment_user(username)
    if db_comment_user(username) is False:
        position = '0.0'
        text.insert(position, 'Такого пользователя в базе данных не найдено')
    else:
        j = 1
        for i in a:
            position3 = f'{j}.0'
            text.insert(position3, f'{i}\n')
            j += 2
    root.mainloop()


def db_comment_user_sort(username):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select commentator_id, username from commentators''')
    evr = cur.fetchall()
    id_user = -1
    for i in evr:
        if i[1] == username:
            id_user = int(i[0])
    if id_user == -1:
        return False
    else:
        res = []
        cur.execute('select commentator_id, comment from comment_info')
        evr1 = cur.fetchall()
        for i in evr1:
            if i[0] == id_user:
                res.append(i[1])
        res.sort()
        return res


def comment_user_sort():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Instagram DataBase")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    text = tk.Text(root, height=10)
    text.grid(row=0, column=0, sticky=tk.EW)

    scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    text['yscrollcommand'] = scrollbar.set

    username = work.get()
    a = db_comment_user_sort(username)
    if db_comment_user(username) is False:
        position = '0.0'
        text.insert(position, 'Такого пользователя в базе данных не найдено')
    else:
        j = 1
        for i in a:
            position3 = f'{j}.0'
            text.insert(position3, f'{i}\n')
            j += 2
    root.mainloop()


def db_comment_time(b, e):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select comment, created_at from comment_info''')
    evr = cur.fetchall()
    res = []
    for i in evr:
        if b <= i[1] <= e:
            res.append(i[0])
    return res


def db_comment_time2(b, e):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select comment, created_at from comment_info order by created_at''')
    evr = cur.fetchall()
    res = []
    for i in evr:
        if b <= i[1] <= e:
            res.append(i[0])
    return res


def comment_time():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Instagram DataBase")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    text = tk.Text(root, height=10)
    text.grid(row=0, column=0, sticky=tk.EW)

    scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    text['yscrollcommand'] = scrollbar.set

    if len(work1.get()) == 0 or len(work2.get()) == 0 or len(work1.get().split('.')) != 3 or len(
            work2.get().split('.')) != 3:
        position = '0.0'
        text.insert(position, 'Введите дату в формате dd.mm.yyyy')
    else:
        b = work1.get().split('.')[2] + '-' + work1.get().split('.')[1] + '-' + work1.get().split('.')[0]
        e = work2.get().split('.')[2] + '-' + work2.get().split('.')[1] + '-' + work2.get().split('.')[0]
        res = db_comment_time(b, e)
        if len(res) == 0:
            position = '0.0'
            text.insert(position, 'В эти даты нет комментариев')
        else:
            j = 1
            for i in res:
                position3 = f'{j}.0'
                text.insert(position3, f'{i}\n')
                j += 2
    root.mainloop()


def comment_time_sort():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Instagram DataBase")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    text = tk.Text(root, height=10)
    text.grid(row=0, column=0, sticky=tk.EW)

    scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    text['yscrollcommand'] = scrollbar.set
    if len(work1.get()) == 0 or len(work2.get()) == 0 or len(work1.get().split('.')) != 3 or len(
            work2.get().split('.')) != 3:
        position = '0.0'
        text.insert(position, 'Введите дату в формате dd.mm.yyyy')
    else:
        b = work1.get().split('.')[2] + '-' + work1.get().split('.')[1] + '-' + work1.get().split('.')[0]
        e = work2.get().split('.')[2] + '-' + work2.get().split('.')[1] + '-' + work2.get().split('.')[0]
        res = db_comment_time(b, e)
        if len(res) == 0:
            position = '0.0'
            text.insert(position, 'В эти даты нет комментариев')
        else:
            j = 1
            res.sort()
            for i in res:
                position3 = f'{j}.0'
                text.insert(position3, f'{i}\n')
                j += 2
    root.mainloop()


def comment_time_sort2():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Instagram DataBase")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    text = tk.Text(root, height=10)
    text.grid(row=0, column=0, sticky=tk.EW)

    scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    text['yscrollcommand'] = scrollbar.set
    if len(work1.get()) == 0 or len(work2.get()) == 0 or len(work1.get().split('.')) != 3 or len(
            work2.get().split('.')) != 3:
        position = '0.0'
        text.insert(position, 'Введите дату в формате dd.mm.yyyy')
    else:
        b = work1.get().split('.')[2] + '-' + work1.get().split('.')[1] + '-' + work1.get().split('.')[0]
        e = work2.get().split('.')[2] + '-' + work2.get().split('.')[1] + '-' + work2.get().split('.')[0]
        res = db_comment_time2(b, e)
        if len(res) == 0:
            position = '0.0'
            text.insert(position, 'В эти даты нет комментариев')
        else:
            j = 1
            for i in res:
                position3 = f'{j}.0'
                text.insert(position3, f'{i}\n')
                j += 2
    root.mainloop()


def db_comment_acc(username):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select user_id, username from accounts''')
    evr = cur.fetchall()
    id_account = -1
    for i in evr:
        if i[1] == username:
            id_account = int(i[0])
    if id_account == -1:
        return False
    else:
        posts = []
        cur.execute('select user_id, post_id from posts_general')
        evr1 = cur.fetchall()
        for i in evr1:
            if i[0] == id_account:
                posts.append(i[1])
        res = []
        cur.execute('select post_id, comment from comment_info')
        evr2 = cur.fetchall()
        for i in evr2:
            if i[0] in posts and isinstance(i[1], str):
                res.append(i[1])
        return res


def comment_acc():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Instagram DataBase")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    text = tk.Text(root, height=10)
    text.grid(row=0, column=0, sticky=tk.EW)

    scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    text['yscrollcommand'] = scrollbar.set
    username = work3.get()
    a = db_comment_acc(username)
    if a is False:
        position = '0.0'
        text.insert(position, 'Такого аккаунта не найдено')
    else:
        j = 1
        if len(a) == 0:
            position3 = f'{j}.0'
            text.insert(position3, 'Под постами этого пользователя нет комментариев')
        else:
            for i in a:
                position3 = f'{j}.0'
                text.insert(position3, f'{i}\n')
                j += 2
    root.mainloop()


def comment_acc_sort():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Instagram DataBase")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    text = tk.Text(root, height=10)
    text.grid(row=0, column=0, sticky=tk.EW)

    scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    text['yscrollcommand'] = scrollbar.set
    username = work3.get()
    a = db_comment_acc(username)
    if a is False:
        position = '0.0'
        text.insert(position, 'Такого аккаунта не найдено')
    else:
        j = 1
        a.sort()
        for i in a:
            position3 = f'{j}.0'
            text.insert(position3, f'{i}\n')
            j += 2
    root.mainloop()


def db_comment_word(word):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select comment from comment_info''')
    evr = cur.fetchall()
    comments = []
    for i in evr:
        if isinstance(i[0], str):
            work = i[0].split()
            for j in work:
                if j.lower() == word.lower():
                    comments.append(i[0])
    return comments


def comment_word():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Instagram DataBase")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    text = tk.Text(root, height=10)
    text.grid(row=0, column=0, sticky=tk.EW)

    scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    text['yscrollcommand'] = scrollbar.set
    word = work4.get()
    a = db_comment_word(word)
    if len(a) == 0:
        position = '0.0'
        text.insert(position, 'Такого слова нет ни в одном комментарии')
    else:
        j = 1
        for i in a:
            position3 = f'{j}.0'
            text.insert(position3, f'{i}\n')
            j += 2
    root.mainloop()


def comment_word_sort():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Instagram DataBase")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    text = tk.Text(root, height=10)
    text.grid(row=0, column=0, sticky=tk.EW)

    scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    text['yscrollcommand'] = scrollbar.set
    word = work4.get()
    a = db_comment_word(word)
    if len(a) == 0:
        position = '0.0'
        text.insert(position, 'Такого слова нет ни в одном комментарии')
    else:
        j = 1
        a.sort()
        for i in a:
            position3 = f'{j}.0'
            text.insert(position3, f'{i}\n')
            j += 2
    root.mainloop()


def db_request(r):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    try:
        cur.execute(r)
        evr = cur.fetchall()
        return evr
    except:
        return False


def request():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Instagram DataBase")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    text = tk.Text(root, height=10)
    text.grid(row=0, column=0, sticky=tk.EW)

    scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    text['yscrollcommand'] = scrollbar.set
    request = work6.get()
    a = db_request(request)
    if a is False:
        position = '0.0'
        text.insert(position, 'Неверный запрос')
    else:
        j = 1
        for i in a:
            position3 = f'{j}.0'
            text.insert(position3, f'{i}\n')
            j += 2
    root.mainloop()


win = tk.Tk()
win.title('Instagram DataBase')
win.geometry('1000x500+100+100')
win.resizable(False, False)

photo = tk.PhotoImage(file='instagram_photo.png')
win.iconphoto(False, photo)

# done
l1 = tk.Label(win, text='1. Форма поиска по пользователю (введите username)', font=('Arial', 12, 'bold'),
              foreground='black', justify=tk.LEFT)
l1.grid(row=0, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work = tk.Entry(win, font=('Arial', 16, 'bold'), foreground='grey')
work.grid(row=1, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work.insert(0, 'начните ввод')
b1 = tk.Button(win, text='Поиск', font=('Arial', 10), foreground='black', relief='raised',
               background='white', bd=3, command=lambda: comment_user())
b1.grid(row=1, column=3, stick='wens', padx=5, pady=5)
b3 = tk.Button(win, text='Сортировка по алфавиту (в комментарии)', font=('Arial', 8), foreground='black',
               relief='raised',
               background='white', bd=3, command=lambda: comment_user_sort())
b3.grid(row=1, column=4, stick='wens', padx=5, pady=5)

# done
l2 = tk.Label(win, text='2. Форма поиска по временному промежутку (c 04.01.19 по 19.10.23)', font=('Arial', 12, 'bold'),
              foreground='black', justify=tk.LEFT)
l2.grid(row=2, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work1 = tk.Entry(win, font=('Arial', 16, 'bold'), justify=tk.LEFT, foreground='grey')
work1.grid(row=3, column=0, rowspan=2, stick='wens', padx=5, pady=5)
work1.insert(0, 'начало')
work2 = tk.Entry(win, font=('Arial', 16, 'bold'), justify=tk.LEFT, foreground='grey')
work2.grid(row=3, column=1, rowspan=2, stick='wens', padx=5, pady=5)
work2.insert(0, 'конец')
b2 = tk.Button(win, text='Поиск', font=('Arial', 10), foreground='black', relief='raised',
               background='white', bd=3, command=lambda: comment_time())
b2.grid(row=3, column=3, rowspan=2, stick='wens', padx=5, pady=5)
b4 = tk.Button(win, text='Сортировка по алфавиту (в комментарии)', font=('Arial', 10), foreground='black',
               relief='raised',
               background='white', bd=3, command=lambda: comment_time_sort())
b4.grid(row=3, column=4, stick='wens', padx=5, pady=5)
b5 = tk.Button(win, text='Сортировка по дате (в возрастании)', font=('Arial', 8), foreground='black', relief='raised',
               background='white', bd=3, command=lambda: comment_time_sort2())
b5.grid(row=4, column=4, stick='wens', padx=5, pady=5)

# done
l3 = tk.Label(win, text='3. Форма поиска по аккаунту (введите username)', font=('Arial', 12, 'bold'),
              foreground='black', justify=tk.LEFT)
l3.grid(row=5, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work3 = tk.Entry(win, font=('Arial', 16, 'bold'), justify=tk.LEFT, foreground='grey')
work3.grid(row=6, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work3.insert(0, 'начните ввод')
b6 = tk.Button(win, text='Поиск', font=('Arial', 10), foreground='black', relief='raised',
               background='white', bd=3, command=lambda: comment_acc())
b6.grid(row=6, column=3, stick='wens', padx=5, pady=5)
b7 = tk.Button(win, text='Сортировка по алфавиту (в комментарии)', font=('Arial', 8), foreground='black',
               relief='raised',
               background='white', bd=3, command=lambda: comment_acc_sort())
b7.grid(row=6, column=4, stick='wens', padx=5, pady=5)

# done
l4 = tk.Label(win, text='4. Форма поиска по слову в комментарии', font=('Arial', 12, 'bold'), foreground='black',
              justify=tk.LEFT)
l4.grid(row=7, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work4 = tk.Entry(win, font=('Arial', 16, 'bold'), justify=tk.LEFT, foreground='grey')
work4.grid(row=8, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work4.insert(0, 'начните ввод')
b8 = tk.Button(win, text='Поиск', font=('Arial', 10), foreground='black', relief='raised',
               background='white', bd=3, command=lambda: comment_word())
b8.grid(row=8, column=3, stick='wens', padx=5, pady=5)
b9 = tk.Button(win, text='Сортировка по алфавиту (в комментарии)', font=('Arial', 8), foreground='black',
               relief='raised',
               background='white', bd=3, command=lambda: comment_word_sort())
b9.grid(row=8, column=4, stick='wens', padx=5, pady=5)

l5 = tk.Label(win, text='Вывод пользователей, которые написали больше n-ого числа комментариев',
              font=('Arial', 12, 'bold'), foreground='black', justify=tk.LEFT)
l5.grid(row=9, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work5 = tk.Entry(win, font=('Arial', 16, 'bold'), justify=tk.LEFT, foreground='grey')
work5.grid(row=10, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work5.insert(0, 'введите число')
b10 = tk.Button(win, text='Поиск', font=('Arial', 10), foreground='black', relief='raised',
                background='white', bd=3, command=lambda: n_comment())
b10.grid(row=10, column=3, stick='wens', padx=5, pady=5)

# doing
l6 = tk.Label(win, text='Введите запрос в базу данных', font=('Arial', 12, 'bold'), foreground='black', justify=tk.LEFT)
l6.grid(row=11, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work6 = tk.Entry(win, font=('Arial', 16, 'bold'), justify=tk.LEFT, foreground='grey')
work6.grid(row=12, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work6.insert(0, 'введите запрос')
b10 = tk.Button(win, text='Отправить', font=('Arial', 10), foreground='black', relief='raised',
                background='white', bd=3, command=lambda: request())
b10.grid(row=12, column=3, stick='wens', padx=5, pady=5)

win.mainloop()
