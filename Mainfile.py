import tkinter.font
from tkinter import *
import sys
from DB import DbFilms, DbSessions, DbHall
from Cal import *
import tkinter as tk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.dbFilms = dbFilms
        self.dbSessions = dbSessions
        self.dbHall = dbHall
        self.table()
        self.view_records_film()

    def table(self):
        m = Menu(root)
        root.config(menu=m)
        sm = Menu(m)
        m.add_cascade(label="Опции", menu=sm)
        sm.add_command(label="Сеансы", command=self.table_sessions)
        sm.add_command(label="Фильмы", command=self.table)
        sm.add_command(label="Зал", command=self.check_film)

        self.films = ttk.Treeview(self,
                                  columns=('ID', 'Title', 'Genre', 'Age', 'Description', 'Visual'),
                                  height=15,
                                  show='headings'
                                  )
        self.films.column('ID', width=30, anchor=tk.CENTER)
        self.films.column('Title', width=250, anchor=tk.CENTER)
        self.films.column('Genre', width=50, anchor=tk.CENTER)
        self.films.column('Age', width=200, anchor=tk.CENTER)
        self.films.column('Description', width=250, anchor=tk.CENTER)
        self.films.column('Visual', width=250, anchor=tk.CENTER)

        self.films.heading('ID', text='ID')
        self.films.heading('Title', text='Название')
        self.films.heading('Genre', text='Жанр')
        self.films.heading('Age', text='Возраст')
        self.films.heading('Description', text='Описание')
        self.films.heading('Visual', text='2D/3D')

        self.films.grid(row=0, column=0, columnspan=4)
        self.view_records_film()

        self.btn_add = tk.Button(self, text='Добавить', command=self.add_film, compound=tk.BOTTOM)
        self.btn_delete = tk.Button(self, text='Удалить', command=self.delete_film, compound=tk.BOTTOM)
        self.btn_exit = tk.Button(self, text='Выход', command=root.destroy, background='red', compound=tk.BOTTOM)

        self.btn_add.grid(row=1, column=0)
        self.btn_delete.grid(row=1, column=1)
        self.btn_exit.grid(row=1, column=3)


    def table_sessions(self):
        self.sessions = ttk.Treeview(self,
                                     columns=('ID', 'Title', 'Date', 'Time', 'Tickets', 'Tickets_sold_out'),
                                     height=15,
                                     show='headings'
                                     )
        self.sessions.column('ID', width=30, anchor=tk.CENTER)
        self.sessions.column('Title', width=250, anchor=tk.CENTER)
        self.sessions.column('Date', width=200, anchor=tk.CENTER)
        self.sessions.column('Time', width=200, anchor=tk.CENTER)
        self.sessions.column('Tickets', width=150, anchor=tk.CENTER)
        self.sessions.column('Tickets_sold_out', width=200, anchor=tk.CENTER)

        self.sessions.heading('ID', text='ID')
        self.sessions.heading('Title', text='Название')
        self.sessions.heading('Date', text='Дата показа')
        self.sessions.heading('Time', text='Время начала')
        self.sessions.heading('Tickets', text='Билетов всего')
        self.sessions.heading('Tickets_sold_out', text='Билетов продано')

        self.sessions.grid(row=0, column=0, columnspan=4)
        self.view_records_session()

        self.btn_add_drug = tk.Button(self, text='Добавить', command=self.add_session, compound=tk.BOTTOM)
        self.btn_delete_drug = tk.Button(self, text='Удалить', command=self.delete_session, compound=tk.BOTTOM)

        self.btn_add_drug.grid(row=1, column=0)
        self.btn_delete_drug.grid(row=1, column=1)

    def table_hall(self):
        self.hall = ttk.Treeview(self,
                                 columns=('ID', 'FirstColumn', 'SecondColumn', 'ThirdColumn', 'FourthColumn', 'FifthColumn'),
                                 height=15,
                                 show='headings'
                                 )
        self.hall.column('ID', width=170, anchor=tk.CENTER)
        self.hall.column('FirstColumn', width=170, anchor=tk.CENTER)
        self.hall.column('SecondColumn', width=170, anchor=tk.CENTER)
        self.hall.column('ThirdColumn', width=170, anchor=tk.CENTER)
        self.hall.column('FourthColumn', width=170, anchor=tk.CENTER)
        self.hall.column('FifthColumn', width=170, anchor=tk.CENTER)

        self.hall.heading('ID', text='Номер ряда/Номер места')
        self.hall.heading('FirstColumn', text='1 Место')
        self.hall.heading('SecondColumn', text='2 Место')
        self.hall.heading('ThirdColumn', text='3 Место')
        self.hall.heading('FourthColumn', text='4 Место')
        self.hall.heading('FifthColumn', text='5 Место')

        self.hall.grid(row=0, column=0, columnspan=4)
        self.view_records_hall()

        self.btn_add = tk.Button(self, text='Добавить', command=self.add_hall, compound=tk.BOTTOM)
        self.btn_upd = tk.Button(self, text='Редактировать', command=self.update_hall, compound=tk.BOTTOM)
        self.btn_delete = tk.Button(self, text='Удалить', command=self.delete_hall, compound=tk.BOTTOM)

        self.btn_add.grid(row=1, column=0)
        self.btn_delete.grid(row=1, column=1)
        self.btn_upd.grid(row=1, column=2)
    '''Зрительские залы'''

    def records_hall(self, FirstColumn, SecondColumn, ThirdColumn, FourthColumn, FifthColumn):
        self.dbHall.insert_data(FirstColumn, SecondColumn, ThirdColumn, FourthColumn, FifthColumn)
        self.view_records_hall()

    def update_record_hall(self, FirstColumn, SecondColumn, ThirdColumn, FourthColumn, FifthColumn):
        self.dbHall.c.execute('''UPDATE Hall SET FirstColumn=?, SecondColumn=?, ThirdColumn=?, FourthColumn=?, FifthColumn=? WHERE ID=?''',
                               (FirstColumn, SecondColumn, ThirdColumn, FourthColumn, FifthColumn,
                                self.hall.set(self.hall.selection()[0], '#1'))
                               )
        self.dbHall.conn.commit()
        self.view_records_hall()

    def view_records_hall(self):
        self.dbHall.c.execute('''SELECT * FROM Hall''')
        [self.hall.delete(i) for i in self.hall.get_children()]
        [self.hall.insert('', 'end', values=row) for row in self.dbHall.c.fetchall()]

    def delete_hall(self):
        for selected_item in self.hall.selection():
            self.dbHall.c.execute("DELETE FROM Hall WHERE ID=?", (self.hall.set(selected_item, '#1'),))
            self.dbHall.conn.commit()
            self.hall.delete(selected_item)
        self.view_records_hall()

    '''Фильмы'''

    def records_film(self, Title, Genre, Age, Description, Visual):
        self.dbFilms.insert_data(Title, Genre, Age, Description, Visual)
        self.view_records_film()

    def view_records_film(self):
        self.dbFilms.c.execute('''SELECT * FROM Films''')
        [self.films.delete(i) for i in self.films.get_children()]
        [self.films.insert('', 'end', values=row) for row in self.dbFilms.c.fetchall()]

    def delete_film(self):
        for selected_item in self.films.selection():
            self.dbFilms.c.execute("DELETE FROM Films WHERE ID=?", (self.films.set(selected_item, '#1'),))
            self.dbFilms.conn.commit()
            self.films.delete(selected_item)
        self.view_records_film()

    '''Сеансы'''

    def records_session(self, Title, Date, Time, Tickets, Tickets_sold_out):
        self.dbSessions.insert_data(Title, Date, Time, Tickets, Tickets_sold_out)
        self.view_records_session()

    def view_records_session(self):
        self.dbSessions.c.execute('''SELECT * FROM Sessions''')
        [self.sessions.delete(i) for i in self.sessions.get_children()]
        [self.sessions.insert('', 'end', values=row) for row in self.dbSessions.c.fetchall()]

    def delete_session(self):
        for selected_item in self.sessions.selection():
            self.dbSessions.c.execute("DELETE FROM Sessions WHERE ID=?", (self.sessions.set(selected_item, '#1'),))
            self.dbSessions.conn.commit()
            self.sessions.delete(selected_item)
        self.view_records_session()

    @staticmethod
    def add_film():
        AddFilm()

    @staticmethod
    def add_session():
        AddSession()

    @staticmethod
    def add_hall():
        AddHall()

    @staticmethod
    def update_hall():
        UpdateHall()

    @staticmethod
    def check_film():
        CheckFilm()


class AddSession(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.dbSessions = dbSessions
        self.init_session()
        self.view = app

    def init_session(self):
        self.title('Добавить Сеанс')
        self.geometry('450x350+400+300')
        self.resizable(False, False)

        label_title = tk.Label(self, text='Название:')
        label_title.place(x=50, y=10)
        self.label_date = tk.Label(self, text='')
        self.label_date.place(x=200, y=40)
        label_time = tk.Label(self, text='Время начала:')
        label_time.place(x=50, y=70)
        label_tickets = tk.Label(self, text='Всего билетов:')
        label_tickets.place(x=50, y=100)
        label_sold_out = tk.Label(self, text='Билетов продано:')
        label_sold_out.place(x=50, y=130)

        self.dbSessions.c.execute('''SELECT Title FROM Films''')
        self.combobox_title = ttk.Combobox(self, values=[row for row in self.dbSessions.c.fetchall()])
        self.combobox_title.current(0)
        self.combobox_title.place(x=200, y=10)
        self.entry_time = ttk.Entry(self)
        self.entry_time.place(x=200, y=70)
        self.entry_tickets = ttk.Entry(self)
        self.entry_tickets.place(x=200, y=100)
        self.entry_sold_out = ttk.Entry(self)
        self.entry_sold_out.place(x=200, y=130)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=350, y=320)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=10, y=320)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records_session(self.combobox_title.get(),
                                                                               self.date[:10],
                                                                               self.entry_time.get(),
                                                                               self.entry_tickets.get(),
                                                                               self.entry_sold_out.get()
                                                                               ))
        self.date_ = ttk.Button(self, text='Выбрать дату')
        self.date_.place(x=50, y=40)
        self.date_.bind('<Button-1>', self.how_cal)
        self.grab_set()
        self.focus_set()

    def how_cal(self, ttkcal):
        self.cal = tkinter.Tk()
        self.cal.title('Календарь')
        self.ttkcal = Calendar(self.cal, firstweekday=calendar.SUNDAY)
        self.ttkcal.pack(expand=1)
        if 'win' not in sys.platform:
            style = ttk.Style()
            style.theme_use('clam')
        self.btn_all = tk.Button(self.cal, text="Выбор", command=self.func_dat)
        self.btn_all.pack()
        self.cal.mainloop()

    def func_dat(self):
        self.date = str(self.ttkcal.selection)
        self.label_date.configure(text=self.date[:10])
        self.cal.destroy()


class AddFilm(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_film()
        self.view = app

    def init_film(self):
        self.title('Добавить фильм')
        self.geometry('450x350+400+300')
        self.resizable(False, False)

        label_title = tk.Label(self, text='Название:')
        label_title.place(x=50, y=10)
        label_genre = tk.Label(self, text='Жанр:')
        label_genre.place(x=50, y=40)
        label_age = tk.Label(self, text='Возраст:')
        label_age.place(x=50, y=70)
        label_description = tk.Label(self, text='Описание:')
        label_description.place(x=50, y=100)
        label_visual = tk.Label(self, text='2D/3D')
        label_visual.place(x=50, y=130)

        self.entry_title = ttk.Entry(self)
        self.entry_title.place(x=200, y=10)
        self.entry_genre = ttk.Entry(self)
        self.entry_genre.place(x=200, y=40)
        self.entry_age = ttk.Entry(self)
        self.entry_age.place(x=200, y=70)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=100)
        self.combobox_visual = ttk.Combobox(self, values=[u'2D', '3D'])
        self.combobox_visual.current(0)
        self.combobox_visual.place(x=200, y=130)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=350, y=320)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=10, y=320)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records_film(self.entry_title.get(),
                                                                            self.entry_genre.get(),
                                                                            self.entry_age.get(),
                                                                            self.entry_description.get(),
                                                                            self.combobox_visual.get(),
                                                                            ))
        self.grab_set()
        self.focus_set()

class AddHall(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_hall()
        self.view = app

    def init_hall(self):
        self.title('Выбрать место')
        self.geometry('450x350+400+300')
        self.resizable(False, False)

        label_first = tk.Label(self, text='1 Место:')
        label_first.place(x=50, y=10)
        label_second = tk.Label(self, text='2 Место:')
        label_second.place(x=50, y=40)
        label_third = tk.Label(self, text='3 Место:')
        label_third.place(x=50, y=70)
        label_fourth = tk.Label(self, text='4 Место:')
        label_fourth.place(x=50, y=100)
        label_fifth = tk.Label(self, text='5 Место:')
        label_fifth.place(x=50, y=130)

        self.combobox_first = ttk.Combobox(self, values=[u'Пусто', 'Занято'])
        self.combobox_first.current(0)
        self.combobox_first.place(x=200, y=10)
        self.combobox_second = ttk.Combobox(self, values=[u'Пусто', 'Занято'])
        self.combobox_second.current(0)
        self.combobox_second.place(x=200, y=40)
        self.combobox_third = ttk.Combobox(self, values=[u'Пусто', 'Занято'])
        self.combobox_third.current(0)
        self.combobox_third.place(x=200, y=70)
        self.combobox_fourth = ttk.Combobox(self, values=[u'Пусто', 'Занято'])
        self.combobox_fourth.current(0)
        self.combobox_fourth.place(x=200, y=100)
        self.combobox_fifth = ttk.Combobox(self, values=[u'Пусто', 'Занято'])
        self.combobox_fifth.current(0)
        self.combobox_fifth.place(x=200, y=130)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=350, y=320)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=10, y=320)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records_hall(self.combobox_first.get(),
                                                                            self.combobox_second.get(),
                                                                            self.combobox_third.get(),
                                                                            self.combobox_fourth.get(),
                                                                            self.combobox_fifth.get(),
                                                                            ))
        self.grab_set()
        self.focus_set()


class UpdateHall(AddHall):
    def __init__(self):
        super().__init__()
        self.init_hall_upd()
        self.view = app

    def init_hall_upd(self):
        self.btn_ok.bind('<Button-1>', lambda event: self.view.update_record_hall(self.combobox_first.get(),
                                                                                  self.combobox_second.get(),
                                                                                  self.combobox_third.get(),
                                                                                  self.combobox_fourth.get(),
                                                                                  self.combobox_fifth.get(),
                                                                                  ))

class CheckFilm(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.dbFilms = dbFilms
        self.init_check()
        self.view = app

    def init_check(self):
        self.title('Выбрать фильм')
        self.geometry('200x100')
        self.resizable(False, False)

        self.dbFilms.c.execute('''SELECT Title FROM Films''')
        self.combobox_film = ttk.Combobox(self, values=[row for row in self.dbFilms.c.fetchall()])
        self.combobox_film.current(0)
        self.combobox_film.place(x=10, y=10)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=100, y=50)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=10, y=50)
        self.btn_ok.bind('<Button-1>', lambda event: print(self.combobox_film.get()))
        self.grab_set()
        self.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    dbFilms = DbFilms()
    dbSessions = DbSessions()
    dbHall = DbHall()
    app = Main(root)
    app.grid()
    root.title("Кинотеатр")
    root.resizable(False, False)
    root.mainloop()
