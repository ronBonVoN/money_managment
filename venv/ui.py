import tkinter as tk
from tkinter import *
import money_classes_functions as M
import current_log as CL

font = ('calibri', 12)

win = tk.Tk()
win.title('money_managment')
win.geometry='50x25'
win.resizable(False, False)
gridx = 40
gridy = 20

drop_options = ['withdraw', 'deposite']
type = StringVar()
type.set(drop_options[0])
drop = tk.OptionMenu(win, type, *drop_options)
drop.grid(row=0, column=0, padx=gridx, pady=gridy)

amt_label = tk.Label(win, text='amt')
amt_label.grid(row=0, column=1)

amt_input = tk.Text(win, font=font, width=10, height = 1)
amt_input.grid(row=0, column=2, padx=gridx, pady=gridy)

reason_label = tk.Label(win, text='reason', font=font)
reason_label.grid(row=0, column=3, padx=gridx, pady=gridy)

reason_imput = tk.Text(win, font=font, width=20, height=1)
reason_imput.grid(row=0, column=4, padx=gridx, pady=gridy)


def enter_command():
    if type=='withdraw':
        pass
       # M.withdraw(CL.log, -int(amt_input.get()),


enter = tk.Button(win, text='enter', width=10, anchor='center')
enter.grid(row=1, column=0, columnspan=4)

win.mainloop()


