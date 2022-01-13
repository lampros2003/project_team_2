import sqlite3

from bs4 import element
from Internet_part3 import *
from unidecode import unidecode


con=sqlite3.connect('work.db') #database που απηθηκεύουμε σε αρχειο
c = con.cursor()

if download and not error:
    try:
        c.execute('DROP TABLE work;')#διαγραφει την database εαν υπαρχει 
        con.commit()
    except:
        pass
    
try:
    c.execute("""CREATE TABLE work (
        number text,
        Greekname text,
        name text,
        title text,
        trans_title text,
        date text,
        kwords text,
        trans_kwords text,
        summary text,
        trans_summary text,
        url text
        )""")#δημιουργια database με επτα κατηγοριες



    for i in range(len(x)):
        c.execute("INSERT INTO work VALUES (?,?,?,?,?,?,?,?,?,?,?)",(x[i].stucount,x[i].writer,unidecode(x[i].writer),unidecode(x[i].title),x[i].trans_title,x[i].date,unidecode(x[i].kwords),x[i].trans_kwords,unidecode(x[i].summary),x[i].trans_summary,x[i].url))#είσαγουμε τα στοιχεια στο database
        
except:
    pass

con.commit()


def search(z):
        z = unidecode(z)
        result = c.execute("SELECT number,Greekname,trans_title,date,url FROM work WHERE name LIKE '%{}%'COLLATE NOCASE ".format(z)).fetchall()
        result = result + c.execute("SELECT number,Greekname,trans_title,date,url FROM work WHERE (title LIKE '%{}%' or trans_title LIKE'%{}%') and not name LIKE '%{}%' COLLATE NOCASE".format(z,z,z)).fetchall()
        result = result + c.execute("SELECT number,Greekname,trans_title,date,url FROM work WHERE (trans_kwords LIKE'%{}%' or  kwords LIKE'%{}%') and not name LIKE '%{}%' and not title LIKE '%{}%' and not trans_title LIKE '%{}%' COLLATE NOCASE".format(z,z,z,z,z)).fetchall()
        result = result + c.execute("SELECT number,Greekname,trans_title,date,url FROM work WHERE summary LIKE '%{}%' and not trans_kwords LIKE'%{}%' and not kwords LIKE'%{}%' and not name LIKE '%{}%' and not title LIKE '%{}%' and not trans_title LIKE '%{}%' COLLATE NOCASE".format(z,z,z,z,z,z)).fetchall() 
        result = result + c.execute("SELECT number,Greekname,trans_title,date,url FROM work WHERE date Like '%{}%' and not summary LIKE '%{}%' and not trans_kwords LIKE'%{}%' and not kwords LIKE'%{}%' and not name LIKE '%{}%' and not title LIKE '%{}%' and not trans_title LIKE '%{}%' COLLATE NOCASE".format(z,z,z,z,z,z,z)).fetchall()
        con.commit()
        return result


def searchname(z):
        z = unidecode(z)
        result = c.execute("SELECT number,Greekname,trans_title,date,url FROM work WHERE name LIKE '%{}%' COLLATE NOCASE".format(z)).fetchall()
        con.commit()
        return result

        
def searchtitle(z):
        z = unidecode(z)
        result = c.execute("SELECT number,Greekname,trans_title,date,url FROM work WHERE trans_title LIKE '%{}%' or title LIKE '%{}%' COLLATE NOCASE".format(z,z)).fetchall()
        con.commit()
        return result
   
