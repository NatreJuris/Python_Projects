import time
import os
import shutil
from tkinter import filedialog
from tkinter import *


def but1():                     #button 1
    filename1 = filedialog.askdirectory()
    lbl1.delete(0, END)
    lbl1.insert(0, filename1)

def but2():                     #buttton 2
    filename2 = filedialog.askdirectory()
    lbl2.delete(0, END)
    lbl2.insert(0, filename2)

def but3():                     #button 3
    but3 = b3
    SECONDS_IN_DAY = 24 * 60 * 60           #24 hour count

    src = lbl1.get()
    dst = lbl2.get()

    now = time.time()
    before = now - SECONDS_IN_DAY

    def last_mod_time(fname):
        return os.path.getmtime(fname)

    for fname in os.listdir(src):
        src_fname = os.path.join(src, fname)
        if (last_mod_time(src_fname) < before):
            dst_fname = os.path.join(dst, fname)
            shutil.move(src_fname, dst_fname)
            print("File Transfer Started")

win = Tk()
b1 = Button(win, text="Source Directory", bg='orange', command=but1)      #gui layout
b2 = Button(win, text="Destination Directory", bg='green', command=but2)
b3 = Button(win, text="Start File Transfer", bg='yellow', command=but3)

b1.grid(row=0, column=0)
b2.grid(row=3, column=0)
b3.grid(row=5, column=0)

lbl1 = Entry(win, width=100)
lbl1.grid(row=0, column=3)

lbl2 = Entry(win, width=100)
lbl2.grid(row=3, column=3)


win.mainloop()

























































































