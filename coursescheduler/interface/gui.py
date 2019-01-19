from helpers import makeschedule
import tkinter as tk


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+': ', anchor='w')
        ent = tk.Entry(row)
        row.pack(side='top', fill='x', padx=5, pady=5)
        lab.pack(side='left')
        ent.pack(side='right', expand='yes', fill='x')
        entries[field] = ent
    return entries

def resultsgui(ents):
    root = tk.Tk()

    if ents is None:
        return setgui(prev=root, ty='home')
    
    courses = str(ents['Courses'].get()).split(", ")
    res = str(ents['Restrictions'].get()).split(", ")

    schedule = makeschedule(courses, res)

    for course in schedule:
        row = tk.Frame(root)
        lab = tk.Label(row, width=50, text=str(course), anchor='w')
        row.pack(side='top', fill='x', padx=5, pady=5)
        lab.pack(side='left')

    b1 = tk.Button(root, text='Back',
            command=(lambda e=ents: setgui(prev=root, ty='home')))
    b1.pack(side='left', padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side='left', padx=5, pady=5)

    root.mainloop()

def homegui():
    fields = ('Courses', 'Restrictions')

    root = tk.Tk()
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='Make Schedule',
                    command=(lambda e=ents: setgui(prev=root, ty='results', info=e)))
    b1.pack(side='left', padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side='left', padx=5, pady=5)
    root.mainloop()


def setgui(prev=None, ty='home', info=None):
    if prev is not None:
        prev.quit

    if ty == 'home':
        homegui()
    elif ty == 'results':
        resultsgui(info)
    else:
        pass

