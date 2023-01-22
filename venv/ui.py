import tkinter as tk
from tkinter import *
import money_classes_functions as M
import current_log as CL

font = ('calibri', 11)

win = tk.Tk()
win.title('money_managment')
win.geometry='50x25'
win.resizable(False, False)
gridx = 40
gridy = 20

drop_options = ['withdraw', 'deposite']
type = StringVar(win)
type.set(drop_options[0])
drop = tk.OptionMenu(win, type, *drop_options)
drop.grid(row=0, column=0, padx=gridx, pady=gridy)

amt_label = tk.Label(win, text='amt', font=font)
amt_label.grid(row=0, column=1)

amt_input = tk.Text(win, font=font, width=10, height = 1)
amt_input.grid(row=0, column=2, padx=gridx, pady=gridy)

reason_label = tk.Label(win, text='reason', font=font)
reason_label.grid(row=0, column=3, padx=gridx, pady=gridy)

reason_input = tk.Text(win, font=font, width=20, height=1)
reason_input.grid(row=0, column=4, padx=gridx, pady=gridy)

date_label = tk.Label(win, text='date', font=font)
date_label.grid(row=1, column=0, padx=gridx, pady=gridy)

date_input = tk.Text(win, font=font, width=20, height=1)
date_input.grid(row=1, column=1, padx=gridx, pady=gridy)


def enter_command():
    if type.get()=='withdraw':
       M.withdraw(CL.log, -int(amt_input.get(1.0, "end-1c")), date_input.get(1.0, "end-1c"), reason_input.get(1.0, "end-1c"))


enter = tk.Button(win, text='enter', width=10, anchor='center', command=enter_command)
enter.grid(row=2, column=0, columnspan=4)

win.mainloop()


