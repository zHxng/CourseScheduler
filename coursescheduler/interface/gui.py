from helpers import makeschedule
import tkinter as tk
from tkinter import font as tkfont


class CourseScheduler(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight='bold', slant='italic')
        self.frames = {
                'StartPage':StartPage, 
                'ResultsPage':ResultsPage
        }

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.shared_data = {
                'Courses': tk.StringVar(),
                'Restrictions': tk.StringVar()
        }
        
        self.show_frame('StartPage')

    def show_frame(self, page_name):
        self.clear_frames()
        frame = self.frames[page_name](parent=self.container, controller=self)
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def clear_frames(self):
        self.container.destroy()
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
        fields = ('Courses', 'Restrictions')

        for field in fields:
            row = tk.Frame(self)
            lab = tk.Label(row, width=10, text=field+': ', anchor='w')
            ent = tk.Entry(row, textvariable=self.controller.shared_data[field])
            row.pack(side='top', fill='x', padx=5, pady=5)
            lab.pack(side='left')
            ent.pack(side='right', expand='yes', fill='x')
        
        b1 = tk.Button(self, text='Make Schedule',
               command=(lambda: controller.show_frame('ResultsPage')))
        b1.pack(side='left', padx=5, pady=5)


class ResultsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        if self.controller.shared_data['Courses'].get() == '':
            return controller.show_frame('StartPage')

        label = tk.Label(self, text='Schedule', font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)

        courses = self.controller.shared_data['Courses'].get().split(', ')
        res = self.controller.shared_data['Restrictions'].get().split(', ')

        schedule = makeschedule(courses, res)

        for course in schedule:
            row = tk.Frame(self)
            lab = tk.Label(row, width=50, text=str(course), anchor='w')
            row.pack(side='top', fill='x', padx=5, pady=5)
            lab.pack(side='left')

        b1 = tk.Button(self, text='Back', command=(lambda: controller.show_frame('StartPage')))
        b1.pack(side='left', padx=5, pady=5)
