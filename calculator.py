from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
import math

root = Tk()
root.title('Calculator')
pattern = r'[^0-9]^√'


# basic logic
def calc(key):
    global memory
    if key == '=':
        entry = "".join(calc_entry.get())
        if re.match(pattern, entry[0]):
            calc_entry.insert(END, 'First symbol is not digit')
            messagebox.showerror('Error!', 'You entered not digit!')
        # count
        try:
            if '√' in calc_entry.get():
                k = re.search(r'√\d+', entry)
                entry = entry.replace(k.group(), str(math.sqrt(int(k.group()[1:]))))
            result = eval(entry)
            calc_entry.insert(END, '=' + str(result))
        except:
            calc_entry.insert(END, 'Error!')
            messagebox.showerror('Error', 'Check your data.')
        # clean entry
    elif key == 'C':
        calc_entry.delete(0, END)
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


# creat all buttons
bttn_list = [
    '7', '8', '9', '+', '-',
    '4', '5', '6', '*', '/',
    '1', '2', '3', '√', '^2',
    '0', '.', 'C', '%', '='
]
r = 1
c = 0

for i in bttn_list:
    # rel = ''
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width=55)
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()
