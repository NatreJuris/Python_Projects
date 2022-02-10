from tkinter import *




win = Tk()
b1 = Button(win, text="Save text")      #create buttons
b2 = Button(win, text="Display page")
b1.grid(row=5, column=0)
b2.grid(row=5, column=4)
l = Label(win, text="Enter message to be displayed:")
l.grid(row=0, column=0)


v = StringVar
e = Entry(win, textvariable = v)        #user input
e.grid(row=3, column=0)

ent = v()
html_content = f"<html> <body> <h1> {ent} </h1> </body> </html>"
def but1():
    but1 = b1
with open("index.html", "w") as html_file:
    html_file.write(html_content)
    print("html file created")      #creates basic web page

b1.configure(command=but1)

def but2():
    but2 = b2
    import webbrowser
    webbrowser.open_new("index.html")       #opens webpage in browser

b2.configure(command=but2)

