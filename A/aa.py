import sqlite3
                                        #connect to test.db
conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()                             #create tbl_files 
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_name TEXT, col_type TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_string(col_string VARCHAR(255))")
    conn.commit()                                           #create tbl_string
conn = sqlite3.connect('test.db')

files = ('information.docx','hello.txt','myimage.phg', \        #giles to sort
                 'mymovie.mpg','world.txt','data.pdf','myphoto.jpg')

for x in files:
    if x.endswith('txt'):               #insert only txt files into table
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_name) VALUES (?)", (x,))
            print(x)
