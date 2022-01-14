import sqlite3

from bs4 import element
from Internet_part3 import *
from unidecode import unidecode


con=sqlite3.connect('work.db') #συνδεόμαστε με την database
c = con.cursor()

if download:
    try:
        c.execute("""CREATE TABLE work (
            number text,
            Greekname text,
            name text,
            Greektitle text,
            title text,
            trans_title text,
            date text,
            kwords text,
            trans_kwords text,
            summary text,
            trans_summary text,
            url text
            )""")#δημιουργια table με δωδεκα κατηγοριες
    except:
        c.execute('DELETE FROM work') #διαγραφει τα στοιχεια απο το table
        con.commit()

        
    for i in range(len(x)):   #είσαγουμε τα στοιχεια απο την x στο table
        c.execute("INSERT INTO work VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(x[i].stucount,x[i].writer,unidecode(x[i].writer),x[i].title,unidecode(x[i].title),x[i].trans_title,x[i].date,unidecode(x[i].kwords),x[i].trans_kwords,unidecode(x[i].summary),x[i].trans_summary,x[i].url))
    con.commit()

# η συνάρτηση search δίνει λίστα με το νούμερο,όνομα,τίτλο,ημερομηνία και url των στοιχείων που έχουν το z 
# στο όνομα ή στον τίτλο ή στις λέξεις κλειδιά ή στην περίληψη ή στην ημερομηνία με αυτήν την προτεραιότητα
def search(z):  
        z = unidecode(z)
        result = c.execute("SELECT number,Greekname,Greektitle,date,url FROM work WHERE name LIKE '%{}%'COLLATE NOCASE ".format(z)).fetchall()
        result = result + c.execute("SELECT number,Greekname,Greektitle,date,url FROM work WHERE (title LIKE '%{}%' or trans_title LIKE'%{}%') and not name LIKE '%{}%' COLLATE NOCASE".format(z,z,z)).fetchall()
        result = result + c.execute("SELECT number,Greekname,Greektitle,date,url FROM work WHERE (trans_kwords LIKE'%{}%' or  kwords LIKE'%{}%') and not name LIKE '%{}%' and not title LIKE '%{}%' and not trans_title LIKE '%{}%' COLLATE NOCASE".format(z,z,z,z,z)).fetchall()
        result = result + c.execute("SELECT number,Greekname,Greektitle,date,url FROM work WHERE summary LIKE '%{}%' and not trans_kwords LIKE'%{}%' and not kwords LIKE'%{}%' and not name LIKE '%{}%' and not title LIKE '%{}%' and not trans_title LIKE '%{}%' COLLATE NOCASE".format(z,z,z,z,z,z)).fetchall() 
        result = result + c.execute("SELECT number,Greekname,Greektitle,date,url FROM work WHERE date Like '%{}%' and not summary LIKE '%{}%' and not trans_kwords LIKE'%{}%' and not kwords LIKE'%{}%' and not name LIKE '%{}%' and not title LIKE '%{}%' and not trans_title LIKE '%{}%' COLLATE NOCASE".format(z,z,z,z,z,z,z)).fetchall()
        return result


def searchname(z):      # δίνει λίστα με το νούμερο,όνομα,τίτλο,ημερομηνία και url των στοιχείων που έχουν το z κάπου στον όνομα
        z = unidecode(z)
        result = c.execute("SELECT number,Greekname,Greektitle,date,url FROM work WHERE name LIKE '%{}%' COLLATE NOCASE".format(z)).fetchall()
        return result

        
def searchtitle(z):   # δίνει λίστα με το νούμερο,όνομα,τίτλο,ημερομηνία και url των στοιχείων που έχουν το z κάπου στον τίτλο
        z = unidecode(z)
        result = c.execute("SELECT number,Greekname,Greektitle,date,url FROM work WHERE trans_title LIKE '%{}%' or title LIKE '%{}%' COLLATE NOCASE".format(z,z)).fetchall()
        return result
   
