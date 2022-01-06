import sqlite3
from internet_part2 import *
from unidecode import unidecode

con=sqlite3.connect('work.db') #database που απηθηκεύουμε σε αρχειο
c = con.cursor()
print(len(x))
if download and not error:
    try:
        c.execute('DROP TABLE work;')
    except:
        pass
    
try:
    c.execute("""CREATE TABLE work (
        name text,
        title text,
        trans_title text,
        date text,
        kwords text,
        trans_kwords text
        )""")#δημιουργια database με εξι κατηγοριες



    for i in range(len(x)):
        c.execute("INSERT INTO work VALUES (?,?,?,?,?,?)",(unidecode(x[i].writer),x[i].title,x[i].trans_title,x[i].date,x[i].kwords,x[i].trans_kwords))#είσαγουμε τα στοιχεια στο database
except:
    pass

con.commit()

def elements():
        allofthem = c.execute("SELECT COUNT(name) FROM work").fetchone()
        string = str(allofthem[0])+" elements availabe"#κοιταει ποσα στοιχεια εχει
        return string

def search(z):
        result = c.execute("SELECT name,trans_title,date FROM work WHERE name LIKE '%{}%' or trans_title LIKE'%{}%' or date LIKE'%{}%' or trans_kwords LIKE'%{}%' or title LIKE'%{}%' or kwords LIKE'%{}%' COLLATE NOCASE ".format(z,z,z,z,z,z)).fetchall()
        con.commit()
        return result

def searchname(z):
        result = c.execute("SELECT name,trans_title,date FROM work WHERE name LIKE '%{}%' COLLATE NOCASE".format(z)).fetchall()
        con.commit()
        return result
        
def searchtitle(z):
        result = c.execute("SELECT name,trans_title,date FROM work WHERE trans_title LIKE '%{}%' or title LIKE '%{}%' COLLATE NOCASE".format(z,z)).fetchall()
        con.commit()
        return result
print(elements())
    
