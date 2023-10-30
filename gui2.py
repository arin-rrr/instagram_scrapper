import tkinter as tk
from tkinter import ttk
import sqlite3 as sql

win = tk.Tk()
win.title('Instagram DataBase')
win.geometry('1150x500+100+100')
win.resizable(False, False)

photo = tk.PhotoImage(file='instagram_photo.png')
bg = tk.PhotoImage(file='inst_bg.png')
win.iconphoto(False, photo)
label = tk.Label(win, image=bg)
label.place(x=0, y=0, relwidth=1, relheight=1)

def create_connection(db_file):
    conn = sql.connect(db_file)
    return conn


def accounts():
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select user_id, username, full_name, media_count, follower_count, following_count  from accounts''')
    evr = cur.fetchall()
    root = tk.Tk()
    root.title('accounts')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    tk.Label(second_frame, text='user_id', font=('Arial', 10, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    tk.Label(second_frame, text='username', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=1, stick='wens', padx=5,
                                                       pady=5)
    tk.Label(second_frame, text='full_name', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=2, stick='wens', padx=5,
                                                       pady=5)
    tk.Label(second_frame, text='media_count', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=3, stick='wens', padx=5,
                                                       pady=5)
    tk.Label(second_frame, text='follower_count', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=4, stick='wens', padx=5,
                                                       pady=5)
    tk.Label(second_frame, text='following_count', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=5, stick='wens', padx=5,
                                                       pady=5)
    for i in evr:
        c = 0
        for j in i:
            tk.Label(second_frame, text=j, font=('Arial', 10),
                     foreground='black', justify=tk.LEFT).grid(row=r, column=c, stick='wens', padx=5, pady=5)
            c += 1
        r += 1
    root.mainloop()


def posts_general():
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select user_id, post_id, taken_at, media_type from posts_general''')
    evr = cur.fetchall()
    root = tk.Tk()
    root.title('posts_general')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    tk.Label(second_frame, text='user_id', font=('Arial', 10, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    tk.Label(second_frame, text='post_id', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=1, stick='wens', padx=5,
                                                       pady=5)
    tk.Label(second_frame, text='taken_at', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=2, stick='wens', padx=5,
                                                       pady=5)
    tk.Label(second_frame, text='media_type', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=3, stick='wens', padx=5,
                                                       pady=5)
    for i in evr:
        c = 0
        for j in i:
            tk.Label(second_frame, text=j, font=('Arial', 10),
                     foreground='black', justify=tk.LEFT).grid(row=r, column=c, stick='wens', padx=5, pady=5)
            c += 1
        r += 1
    root.mainloop()


def description_post():
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select post_id, comment_count, like_count from description_post''')
    evr = cur.fetchall()
    root = tk.Tk()
    root.title('description_post')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    tk.Label(second_frame, text='post_id', font=('Arial', 10, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    tk.Label(second_frame, text='comment_count', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=1, stick='wens', padx=5,
                                                       pady=5)
    tk.Label(second_frame, text='like_count', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=2, stick='wens', padx=5,
                                                       pady=5)
    for i in evr:
        c = 0
        for j in i:
            tk.Label(second_frame, text=j, font=('Arial', 10),
                     foreground='black', justify=tk.LEFT).grid(row=r, column=c, stick='wens', padx=5, pady=5)
            c += 1
        r += 1
    root.mainloop()


def comment_info():
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select comment_id, post_id, commentator_id, comment, created_at from comment_info''')
    evr = cur.fetchall()
    root = tk.Tk()
    root.title('comment_info')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    tk.Label(second_frame, text='comment_id', font=('Arial', 10, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    tk.Label(second_frame, text='post_id', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=1, stick='wens', padx=5,
                                                       pady=5)
    tk.Label(second_frame, text='commentator_id', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=2, stick='wens', padx=5,
                                                       pady=5)
    tk.Label(second_frame, text='comment', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=3, stick='wens', padx=5,
                                                       pady=5)
    tk.Label(second_frame, text='created_at', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=4, stick='wens', padx=5,
                                                       pady=6)
    for i in evr:
        c = 0
        for j in i:
            tk.Label(second_frame, text=j, font=('Arial', 10),
                     foreground='black', justify=tk.LEFT).grid(row=r, column=c, stick='wens', padx=5, pady=5)
            c += 1
        r += 1
    root.mainloop()


def commentators():
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select commentator_id, post_id, username from commentators''')
    evr = cur.fetchall()
    root = tk.Tk()
    root.title('commentators')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    tk.Label(second_frame, text='commentator_id', font=('Arial', 10, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    tk.Label(second_frame, text='post_id', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=1, stick='wens', padx=5,
                                                       pady=5)
    tk.Label(second_frame, text='username', font=('Arial', 12, 'bold'),
             foreground='black', justify=tk.LEFT).grid(row=0, column=2, stick='wens', padx=5,
                                                       pady=5)
    for i in evr:
        c = 0
        for j in i:
            tk.Label(second_frame, text=j, font=('Arial', 10),
                     foreground='black', justify=tk.LEFT).grid(row=r, column=c, stick='wens', padx=5, pady=5)
            c += 1
        r += 1
    root.mainloop()


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
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    username = work.get()
    a = db_comment_user(username)
    if a is False:
        tk.Label(second_frame, text='Такого пользователя в базе данных не найдено', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    else:
        tk.Label(second_frame, text='Comment', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
        c = 0
        for i in a:
            tk.Label(second_frame, text=i, font=('Arial', 10),
                     foreground='black', justify=tk.RIGHT).grid(row=r, column=c, stick='w', padx=5, pady=5)
            r += 1
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
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    username = work.get()
    a = db_comment_user_sort(username)
    if a is False:
        tk.Label(second_frame, text='Такого пользователя в базе данных не найдено', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    else:
        tk.Label(second_frame, text='Comment', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
        c = 0
        for i in a:
            tk.Label(second_frame, text=i, font=('Arial', 10),
                     foreground='black', justify=tk.RIGHT).grid(row=r, column=c, stick='w', padx=5, pady=5)
            r += 1
    root.mainloop()


def db_comment_user_sort_data(username):
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
        cur.execute('select commentator_id, comment, created_at from comment_info order by created_at')
        evr1 = cur.fetchall()
        for i in evr1:
            if i[0] == id_user:
                res.append((i[1], i[2]))
        return res


def comment_user_sort_data():
    root = tk.Tk()
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    username = work.get()
    a = db_comment_user_sort_data(username)
    if a is False:
        tk.Label(second_frame, text='Такого пользователя в базе данных не найдено', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    else:
        tk.Label(second_frame, text='Comment', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
        tk.Label(second_frame, text='Data', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=1, stick='w', padx=5, pady=5)
        for i in a:
            tk.Label(second_frame, text=i[0], font=('Arial', 10),
                     foreground='black', justify=tk.RIGHT).grid(row=r, column=0, stick='w', padx=5, pady=5)
            tk.Label(second_frame, text=i[1], font=('Arial', 10),
                     foreground='black', justify=tk.RIGHT).grid(row=r, column=1, stick='w', padx=5, pady=5)
            r += 1
    root.mainloop()


def db_comment_time(b, e):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select comment, created_at from comment_info''')
    evr = cur.fetchall()
    res = []
    for i in evr:
        if b <= i[1] <= e:
            res.append((i[0], i[1]))
    return res


def db_comment_time2(b, e):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select comment, created_at from comment_info order by comment''')
    evr = cur.fetchall()
    res = []
    for i in evr:
        if b <= i[1] <= e:
            res.append((i[0], i[1]))
    return res


def db_comment_time3(b, e):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select comment, created_at from comment_info order by created_at''')
    evr = cur.fetchall()
    res = []
    for i in evr:
        if b <= i[1] <= e:
            res.append((i[0], i[1]))
    return res


def comment_time():
    root = tk.Tk()
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    if len(work1.get()) == 0 or len(work2.get()) == 0 or len(work1.get().split('.')) != 3 or len(
            work2.get().split('.')) != 3:
        tk.Label(second_frame, text='Введите дату в формате dd.mm.yyyy', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    else:
        b = work1.get().split('.')[2] + '-' + work1.get().split('.')[1] + '-' + work1.get().split('.')[0]
        e = work2.get().split('.')[2] + '-' + work2.get().split('.')[1] + '-' + work2.get().split('.')[0]
        res = db_comment_time(b, e)
        if len(res) == 0:
            tk.Label(second_frame, text='В эти даты нет комментариев', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
        else:
            tk.Label(second_frame, text='Comment', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
            tk.Label(second_frame, text='Date', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=1, stick='wens', padx=5, pady=5)
            r = 1
            for i in res:
                tk.Label(second_frame, text=f'{i[0]}', font=('Arial', 10, 'bold'),
                         foreground='black', justify=tk.LEFT).grid(row=r, column=0, stick='w', padx=5, pady=5)
                tk.Label(second_frame, text=f'{i[1]}', font=('Arial', 10, 'bold'),
                         foreground='black', justify=tk.LEFT).grid(row=r, column=1, stick='w', padx=5, pady=5)
                r += 1
    root.mainloop()


def comment_time_sort():
    root = tk.Tk()
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    if len(work1.get()) == 0 or len(work2.get()) == 0 or len(work1.get().split('.')) != 3 or len(
            work2.get().split('.')) != 3:
        tk.Label(second_frame, text='Введите дату в формате dd.mm.yyyy', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    else:
        b = work1.get().split('.')[2] + '-' + work1.get().split('.')[1] + '-' + work1.get().split('.')[0]
        e = work2.get().split('.')[2] + '-' + work2.get().split('.')[1] + '-' + work2.get().split('.')[0]
        res = db_comment_time2(b, e)
        if len(res) == 0:
            tk.Label(second_frame, text='В эти даты нет комментариев', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
        else:
            tk.Label(second_frame, text='Comment', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
            tk.Label(second_frame, text='Date', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=1, stick='wens', padx=5, pady=5)
            r = 1
            for i in res:
                tk.Label(second_frame, text=f'{i[0]}', font=('Arial', 10, 'bold'),
                         foreground='black', justify=tk.LEFT).grid(row=r, column=0, stick='w', padx=5, pady=5)
                tk.Label(second_frame, text=f'{i[1]}', font=('Arial', 10, 'bold'),
                         foreground='black', justify=tk.LEFT).grid(row=r, column=1, stick='w', padx=5, pady=5)
                r += 1
    root.mainloop()


def comment_time_sort2():
    root = tk.Tk()
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    if len(work1.get()) == 0 or len(work2.get()) == 0 or len(work1.get().split('.')) != 3 or len(
            work2.get().split('.')) != 3:
        tk.Label(second_frame, text='Введите дату в формате dd.mm.yyyy', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    else:
        b = work1.get().split('.')[2] + '-' + work1.get().split('.')[1] + '-' + work1.get().split('.')[0]
        e = work2.get().split('.')[2] + '-' + work2.get().split('.')[1] + '-' + work2.get().split('.')[0]
        res = db_comment_time3(b, e)
        if len(res) == 0:
            tk.Label(second_frame, text='В эти даты нет комментариев', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
        else:
            tk.Label(second_frame, text='Comment', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
            tk.Label(second_frame, text='Date', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=1, stick='wens', padx=5, pady=5)
            r = 1
            for i in res:
                tk.Label(second_frame, text=f'{i[0]}', font=('Arial', 10, 'bold'),
                         foreground='black', justify=tk.LEFT).grid(row=r, column=0, stick='w', padx=5, pady=5)
                tk.Label(second_frame, text=f'{i[1]}', font=('Arial', 10, 'bold'),
                         foreground='black', justify=tk.LEFT).grid(row=r, column=1, stick='w', padx=5, pady=5)
                r += 1
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


def db_comment_acc2(username):
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
        cur.execute('select post_id, comment, created_at from comment_info order by created_at')
        evr2 = cur.fetchall()
        for i in evr2:
            if i[0] in posts and isinstance(i[1], str):
                res.append((i[1], i[2]))
        return res


def comment_acc():
    root = tk.Tk()
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    username = work3.get()
    a = db_comment_acc(username)
    if a is False:
        tk.Label(second_frame, text='Такого пользователя в базе данных не найдено', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    else:
        if len(a) == 0:
            tk.Label(second_frame, text='Под постами этого пользователя нет комментариев', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
        else:
            tk.Label(second_frame, text='Comment', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
            c = 0
            for i in a:
                tk.Label(second_frame, text=i, font=('Arial', 10),
                         foreground='black', justify=tk.RIGHT).grid(row=r, column=c, stick='w', padx=5, pady=5)
                r += 1
    root.mainloop()


def comment_acc_sort():
    root = tk.Tk()
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_scrbar1 = ttk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
    my_scrbar1.pack(side=tk.LEFT, fill=tk.X)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    username = work3.get()
    a = db_comment_acc(username)
    if a is False:
        tk.Label(second_frame, text='Такого пользователя в базе данных не найдено', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    else:
        if len(a) == 0:
            tk.Label(second_frame, text='Под постами этого пользователя нет комментариев', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
        else:
            tk.Label(second_frame, text='Comment', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
            c = 0
            a.sort()
            for i in a:
                tk.Label(second_frame, text=i, font=('Arial', 10),
                         foreground='black', justify=tk.RIGHT).grid(row=r, column=c, stick='w', padx=5, pady=5)
                r += 1
    root.mainloop()


def comment_acc_sort_data():
    root = tk.Tk()
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_scrbar1 = ttk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
    my_scrbar1.pack(side=tk.LEFT, fill=tk.X)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    username = work3.get()
    a = db_comment_acc2(username)
    if a is False:
        tk.Label(second_frame, text='Такого пользователя в базе данных не найдено', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='wens', padx=5, pady=5)
    else:
        if len(a) == 0:
            tk.Label(second_frame, text='Под постами этого пользователя нет комментариев', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
        else:
            tk.Label(second_frame, text='Comment', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
            tk.Label(second_frame, text='Date', font=('Arial', 12, 'bold'),
                     foreground='black', justify=tk.LEFT).grid(row=0, column=1, stick='w', padx=5, pady=5)
            for i in a:
                tk.Label(second_frame, text=i[0], font=('Arial', 10),
                         foreground='black', justify=tk.RIGHT).grid(row=r, column=0, stick='w', padx=5, pady=5)
                tk.Label(second_frame, text=i[1], font=('Arial', 10),
                         foreground='black', justify=tk.RIGHT).grid(row=r, column=1, stick='w', padx=5, pady=5)
                r += 1
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


def db_comment_word2(word):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select comment, created_at from comment_info order by created_at''')
    evr = cur.fetchall()
    comments = []
    for i in evr:
        if isinstance(i[0], str):
            work = i[0].split()
            for j in work:
                if j.lower() == word.lower():
                    comments.append((i[0], i[1]))
    return comments


def comment_word():
    root = tk.Tk()
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_scrollbar2 = ttk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
    my_scrollbar2.pack(side=tk.RIGHT, fill=tk.X)

    my_canvas.configure(yscrollcommand=my_scrollbar.set, xscrollcommand=my_scrollbar2.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    word = work4.get()
    a = db_comment_word(word)
    if len(a) == 0:
        tk.Label(second_frame, text='Такого слова нет в комментариях', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
    else:
        tk.Label(second_frame, text='Comment', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
        for i in a:
            tk.Label(second_frame, text=i, font=('Arial', 10),
                     foreground='black', justify=tk.RIGHT).grid(row=r, column=0, stick='w', padx=5, pady=5)
            r += 1
    root.mainloop()


def comment_word_sort():
    root = tk.Tk()
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_scrollbar2 = ttk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
    my_scrollbar2.pack(side=tk.RIGHT, fill=tk.X)

    my_canvas.configure(yscrollcommand=my_scrollbar.set, xscrollcommand=my_scrollbar2.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    word = work4.get()
    a = db_comment_word(word)
    if len(a) == 0:
        tk.Label(second_frame, text='Такого слова нет в комментариях', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
    else:
        tk.Label(second_frame, text='Comment', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
        a.sort()
        for i in a:
            tk.Label(second_frame, text=i, font=('Arial', 10),
                     foreground='black', justify=tk.RIGHT).grid(row=r, column=0, stick='w', padx=5, pady=5)
            r += 1
    root.mainloop()


def comment_word_sort_data():
    root = tk.Tk()
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_scrollbar2 = ttk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
    my_scrollbar2.pack(side=tk.RIGHT, fill=tk.X)

    my_canvas.configure(yscrollcommand=my_scrollbar.set, xscrollcommand=my_scrollbar2.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    word = work4.get()
    a = db_comment_word2(word)
    if len(a) == 0:
        tk.Label(second_frame, text='Такого слова нет в комментариях', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
    else:
        tk.Label(second_frame, text='Comment', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
        tk.Label(second_frame, text='Date', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=1, stick='w', padx=5, pady=5)
        for i in a:
            tk.Label(second_frame, text=i[0], font=('Arial', 10),
                     foreground='black', justify=tk.RIGHT).grid(row=r, column=0, stick='w', padx=5, pady=5)
            tk.Label(second_frame, text=i[1], font=('Arial', 10),
                     foreground='black', justify=tk.RIGHT).grid(row=r, column=1, stick='w', padx=5, pady=5)
            r += 1
    root.mainloop()


def db_n_comment(digit):
    conn = create_connection('instagram_instagram.db')
    cur = conn.cursor()
    cur.execute('''select commentator_id from comment_info''')
    evr = cur.fetchall()
    n_comment = {}
    vv = []
    for i in evr:
        if i[0] not in n_comment:
            n_comment[i[0]] = 1
        else:
            n_comment[i[0]] += 1
    for i in n_comment:
        if n_comment[i] >= int(digit):
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
    root = tk.Tk()
    root.title('Instagram DataBase')
    root.geometry('500x500')

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    my_scrollbar2 = ttk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
    my_scrollbar2.pack(side=tk.RIGHT, fill=tk.X)

    my_canvas.configure(yscrollcommand=my_scrollbar.set, xscrollcommand=my_scrollbar2.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    r = 1
    num = work5.get()
    a = db_n_comment(num)
    if len(a) == 0:
        tk.Label(second_frame, text='Нет пользователей с таким кол-вом комментариев', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
    else:
        tk.Label(second_frame, text='Commentator ID', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=0, stick='w', padx=5, pady=5)
        tk.Label(second_frame, text='Username', font=('Arial', 12, 'bold'),
                 foreground='black', justify=tk.LEFT).grid(row=0, column=1, stick='w', padx=5, pady=5)
        for i in a:
            tk.Label(second_frame, text=i, font=('Arial', 10),
                     foreground='black', justify=tk.RIGHT).grid(row=r, column=0, stick='w', padx=5, pady=5)
            tk.Label(second_frame, text=a[i], font=('Arial', 10),
                     foreground='black', justify=tk.RIGHT).grid(row=r, column=1, stick='w', padx=5, pady=5)
            r += 1
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


tk.Label(win, text='Вывести таблицы:', font=('Arial', 12, 'bold'),
         foreground='black', justify=tk.LEFT, background='#7a61dc').grid(row=0, column=0, columnspan=2, stick='wens', padx=5, pady=5)
bb1 = tk.Button(win, text='accounts', font=('Arial', 10), foreground='black',
                relief='raised',
                background='white', bd=3, command=lambda: accounts())
bb1.grid(row=0, column=2, stick='wens', padx=5, pady=5)

bb2 = tk.Button(win, text='posts_general', font=('Arial', 10), foreground='black',
                relief='raised',
                background='white', bd=3, command=lambda: posts_general())
bb2.grid(row=0, column=3, stick='wens', padx=5, pady=5)

bb3 = tk.Button(win, text='description_post', font=('Arial', 10), foreground='black',
                relief='raised',
                background='white', bd=3, command=lambda: description_post())
bb3.grid(row=0, column=4, stick='wens', padx=5, pady=5)

bb4 = tk.Button(win, text='comment_info', font=('Arial', 10), foreground='black',
                relief='raised',
                background='white', bd=3, command=lambda: comment_info())
bb4.grid(row=0, column=5, stick='wens', padx=5, pady=5)

bb5 = tk.Button(win, text='commentators', font=('Arial', 10), foreground='black',
                relief='raised',
                background='white', bd=3, command=lambda: commentators())
bb5.grid(row=0, column=6, stick='wens', padx=5, pady=5)

l1 = tk.Label(win, text='1. По пользователю (введите username)', font=('Arial', 12, 'bold'),
              foreground='black', justify=tk.LEFT, background='#8f60d9')
l1.grid(row=1, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work = tk.Entry(win, font=('Arial', 16, 'bold'), foreground='grey')
work.grid(row=2, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work.insert(0, 'начните ввод')
b1 = tk.Button(win, text='Поиск', font=('Arial', 10), foreground='black', relief='raised',
               background='white', bd=3, command=lambda: comment_user())
b1.grid(row=2, column=2, stick='wens', padx=5, pady=5)
b2 = tk.Button(win, text='Сортировка по алфавиту', font=('Arial', 8), foreground='black',
               relief='raised',
               background='white', bd=3, command=lambda: comment_user_sort())
b2.grid(row=2, column=3, stick='wens', padx=5, pady=5)
b3 = tk.Button(win, text='Сортировка по дате', font=('Arial', 8), foreground='black',
               relief='raised',
               background='white', bd=3, command=lambda: comment_user_sort_data())
b3.grid(row=2, column=4, stick='wens', padx=5, pady=5)

l2 = tk.Label(win, text='2. По временному промежутку (04.01.19 - 19.10.23)', font=('Arial', 12, 'bold'),
              foreground='black', background='#a85fd5', justify=tk.LEFT)
l2.grid(row=3, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work1 = tk.Entry(win, font=('Arial', 16, 'bold'), justify=tk.LEFT, foreground='grey')
work1.grid(row=4, column=0, stick='wens', padx=5, pady=5)
work1.insert(0, 'начало')
work2 = tk.Entry(win, font=('Arial', 16, 'bold'), justify=tk.LEFT, foreground='grey')
work2.grid(row=4, column=1, stick='wens', padx=5, pady=5)
work2.insert(0, 'конец')
b4 = tk.Button(win, text='Поиск', font=('Arial', 10), foreground='black', relief='raised',
               background='white', bd=3, command=lambda: comment_time())
b4.grid(row=4, column=2, stick='wens', padx=5, pady=5)
b5 = tk.Button(win, text='Сортировка по алфавиту', font=('Arial', 10), foreground='black',
               relief='raised',
               background='white', bd=3, command=lambda: comment_time_sort())
b5.grid(row=4, column=3, stick='wens', padx=5, pady=5)
b6 = tk.Button(win, text='Сортировка по дате', font=('Arial', 8), foreground='black', relief='raised',
               background='white', bd=3, command=lambda: comment_time_sort2())
b6.grid(row=4, column=4, stick='wens', padx=5, pady=5)

l3 = tk.Label(win, text='3. По аккаунту (введите username)', font=('Arial', 12, 'bold'),
              foreground='black', justify=tk.LEFT, background='#c65dd0')
l3.grid(row=5, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work3 = tk.Entry(win, font=('Arial', 16, 'bold'), justify=tk.LEFT, foreground='grey')
work3.grid(row=6, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work3.insert(0, 'начните ввод')
b7 = tk.Button(win, text='Поиск', font=('Arial', 10), foreground='black', relief='raised',
               background='white', bd=3, command=lambda: comment_acc())
b7.grid(row=6, column=2, stick='wens', padx=5, pady=5)
b8 = tk.Button(win, text='Сортировка по алфавиту', font=('Arial', 8), foreground='black',
               relief='raised',
               background='white', bd=3, command=lambda: comment_acc_sort())
b8.grid(row=6, column=3, stick='wens', padx=5, pady=5)
b9 = tk.Button(win, text='Сортировка по дате', font=('Arial', 8), foreground='black',
               relief='raised',
               background='white', bd=3, command=lambda: comment_acc_sort_data())
b9.grid(row=6, column=4, stick='wens', padx=5, pady=5)

l4 = tk.Label(win, text='4. По слову в комментарии', font=('Arial', 12, 'bold'), foreground='black',
              justify=tk.LEFT, background='#e25ec9')
l4.grid(row=7, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work4 = tk.Entry(win, font=('Arial', 16, 'bold'), justify=tk.LEFT, foreground='grey')
work4.grid(row=8, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work4.insert(0, 'начните ввод')
b10 = tk.Button(win, text='Поиск', font=('Arial', 10), foreground='black', relief='raised',
                background='white', bd=3, command=lambda: comment_word())
b10.grid(row=8, column=2, stick='wens', padx=5, pady=5)
b11 = tk.Button(win, text='Сортировка по алфавиту ', font=('Arial', 8), foreground='black',
                relief='raised',
                background='white', bd=3, command=lambda: comment_word_sort())
b11.grid(row=8, column=3, stick='wens', padx=5, pady=5)
b12 = tk.Button(win, text='Сортировка по дате ', font=('Arial', 8), foreground='black',
                relief='raised',
                background='white', bd=3, command=lambda: comment_word_sort_data())
b12.grid(row=8, column=4, stick='wens', padx=5, pady=5)

l5 = tk.Label(win, text='Пользователи с n и более комментариями',
              font=('Arial', 12, 'bold'), foreground='black', justify=tk.LEFT, background='#e0919b')
l5.grid(row=9, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work5 = tk.Entry(win, font=('Arial', 16, 'bold'), justify=tk.LEFT, foreground='grey')
work5.grid(row=10, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work5.insert(0, 'введите число')
b13 = tk.Button(win, text='Поиск', font=('Arial', 10), foreground='black', relief='raised',
                background='white', bd=3, command=lambda: n_comment())
b13.grid(row=10, column=2, stick='wens', padx=5, pady=5)

l6 = tk.Label(win, text='Введите запрос в базу данных', font=('Arial', 12, 'bold'), foreground='black', justify=tk.LEFT, background='#dfbc74')
l6.grid(row=11, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work6 = tk.Entry(win, font=('Arial', 16, 'bold'), justify=tk.LEFT, foreground='grey')
work6.grid(row=12, column=0, columnspan=2, stick='wens', padx=5, pady=5)
work6.insert(0, 'введите запрос')
b14 = tk.Button(win, text='Отправить', font=('Arial', 10), foreground='black', relief='raised',
                background='white', bd=3, command=lambda: request())
b14.grid(row=12, column=2, stick='wens', padx=5, pady=5)

win.mainloop()
