import time
import os
import shutil
import pathlib
from tkinter import filedialog
from tkinter import *


win = Tk()
b1 = Button(win, text="Source Directory", bg='orange')      #gui layout
b2 = Button(win, text="Destination Directory", bg='green')
b3 = Button(win, text="Start File Transfer", bg='yellow')
b1.grid(row=0, column=0)
b2.grid(row=3, column=0)
b3.grid(row=5, column=0)

def but1():                     #button 1
    but1 = b1
    global folder_path1
    filename1 = filedialog.askdirectory()
    folder_path1.set(filename1)
    print(filename1)

folder_path1 = StringVar()
lbl1 = Label(win,textvariable=folder_path1)
lbl1.grid(row=0, column=3)
         

b1.configure(command=but1)

def but2():                     #buttton 2
    but2 = b2
    global folder_path2
    filename2 = filedialog.askdirectory()
    folder_path2.set(filename2)
    print(filename2)

folder_path2 = StringVar()
lbl2 = Label(win,textvariable=folder_path2)
lbl2.grid(row=3, column=3)

        

b2.configure(command=but2)

def but3():                     #button 3
    but3 = b3

    SECONDS_IN_DAY = 24 * 60 * 60           #24 hour count

    src = folder_path1
    dst = folder_path2

    now = time.time()
    before = now - SECONDS_IN_DAY

    def last_mod_time(fname):
        return os.path.getmtime(fname)

    for fname in os.listdir():
        src_fname = os.path.join(fname)
        if (last_mod_time(src_fname) > before):
            dst_fname = os.path.join(fname)
            shutil.move(src_fname, dst_fname)
            print("File Transfer Started")

b3.configure(command=but3)


























































































