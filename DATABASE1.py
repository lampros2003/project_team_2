import sqlite3
from internet_part2 import *
from unidecode import unidecode

amount = 0

con=sqlite3.connect('work.db') #database που απηθηκεύουμε σε αρχειο
c = con.cursor()

if download and not error:
    try:
        c.execute('DROP TABLE work;')#διαγραφει την database εαν υπαρχει 
    except:
        pass
    
try:
    c.execute("""CREATE TABLE work (
        name text,
        title text,
        trans_title text,
        date text,
        kwords text,
        trans_kwords text,
        summary text
        )""")#δημιουργια database με επτα κατηγοριες



    for i in range(len(x)):
        c.execute("INSERT INTO work VALUES (?,?,?,?,?,?,?)",(unidecode(x[i].writer),unidecode(x[i].title),x[i].trans_title,x[i].date,unidecode(x[i].kwords),x[i].trans_kwords,x[i].summary))#είσαγουμε τα στοιχεια στο database
except:
    pass

con.commit()

def elements():
        allofthem = c.execute("SELECT COUNT(name) FROM work").fetchone()
        string = str(allofthem[0])+" elements availabe"#κοιταει ποσα στοιχεια εχει
        return string

def search(z):
        global amount
        z = unidecode(z)
        result = c.execute("SELECT name,trans_title,date FROM work WHERE name LIKE '%{}%'COLLATE NOCASE ".format(z)).fetchall()
        result = result + c.execute("SELECT name,trans_title,date FROM work WHERE (title LIKE '%{}%' or trans_title LIKE'%{}%') and not name LIKE '%{}%' COLLATE NOCASE".format(z,z,z)).fetchall()
        result = result + c.execute("SELECT name,trans_title,date FROM work WHERE (trans_kwords LIKE'%{}%' or  kwords LIKE'%{}%') and not name LIKE '%{}%' and not title LIKE '%{}%' and not trans_title LIKE '%{}%' COLLATE NOCASE".format(z,z,z,z,z)).fetchall()
        result = result + c.execute("SELECT name,trans_title,date FROM work WHERE summary LIKE '%{}%' and not trans_kwords LIKE'%{}%' and not kwords LIKE'%{}%' and not name LIKE '%{}%' and not title LIKE '%{}%' and not trans_title LIKE '%{}%' COLLATE NOCASE".format(z,z,z,z,z,z)).fetchall() 
        result = result + c.execute("SELECT name,trans_title,date FROM work WHERE date Like '%{}%' and not summary LIKE '%{}%' and not trans_kwords LIKE'%{}%' and not kwords LIKE'%{}%' and not name LIKE '%{}%' and not title LIKE '%{}%' and not trans_title LIKE '%{}%' COLLATE NOCASE".format(z,z,z,z,z,z,z)).fetchall()
        con.commit()
        amount = len(result)
        return result


def searchbydate(z):
        global amount
        result = c.execute("SELECT name,trans_title,date FROM work WHERE name LIKE '%{}%' or trans_title LIKE'%{}%' or date LIKE'%{}%' or trans_kwords LIKE'%{}%' or title LIKE'%{}%' or kwords LIKE'%{}%' or summary LIKE '%{}%' COLLATE NOCASE ".format(z,z,z,z,z,z,z)).fetchall()
        con.commit()
        amount = len(result)
        return result


def searchname(z):
        global amount
        z = unidecode(z)
        result = c.execute("SELECT name,trans_title,date FROM work WHERE name LIKE '%{}%' COLLATE NOCASE".format(z)).fetchall()
        con.commit()
        amount = len(reult)
        return result

        
def searchtitle(z):
        global amount
        z = unidecode(z)
        result = c.execute("SELECT name,trans_title,date FROM work WHERE trans_title LIKE '%{}%' or title LIKE '%{}%' COLLATE NOCASE".format(z,z)).fetchall()
        con.commit()
        amount = len(result)
        return result
    
