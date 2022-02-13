from tkinter import *




win = Tk()
b1 = Button(win, text="Save text")      #create buttons
b2 = Button(win, text="Display page")
b1.grid(row=5, column=0)
b2.grid(row=5, column=4)
l = Label(win, text="Enter message to be displayed:")
l.grid(row=0, column=0)


v = StringVar()
e = Entry(win, textvariable = v)        #user input
e.grid(row=3, column=0)
  

def but1():
    but1 = b1
    h = e.get()
    html_content = f"<html> <body> <h1> {h} </h1> </body> </html>"
    f = open("index.html", "w")
    f.write(html_content)
    print(html_content)      #creates basic web page

b1.configure(command=but1)

def but2():
    but2 = b2
    import webbrowser
    webbrowser.open_new("index.html")       #opens webpage in browser

b2.configure(command=but2)

win.mainloop()
