import sqlite3

class Worker():#κλαση που θα βαλουμε στη δοκιμαστικη λιστα
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
x=[]
x.append(Worker('elena','rodrigez',10000))
x.append(Worker("jane","five",400000))
x.append(Worker('merry','onona',50000))
x.append(Worker('Edouardo','katsos',100000))
x.append(Worker('john','janesan',50000))
x.append(Worker('alpha','esperanza',10000))
x.append(Worker('elza','zoro',37000)) 
x.append(Worker('anna','three',10000))#τα στοιχεια που θα μπουν στη λιστα
         
con=sqlite3.connect(':memory:') #database στην ram
c = con.cursor()

c.execute("""CREATE TABLE employees (
        firstname text,
        lastname text,
        pay integer
        )""")#δημιουργια database με τρεις κατηγοριες


for i in range(len(x)):
    c.execute("INSERT INTO employees VALUES (?,?,?)",(x[i].first,x[i].last,x[i].pay))#είσαγουμε τα στοιχεια στο database


con.commit()

def elements():
        allofthem = c.execute("SELECT COUNT(lastname) FROM employees").fetchone()
        string = str(allofthem[0])+" elements availabe"#κοιταει ποσα στοιχεια εχει
        return string

def search(z):
        result = c.execute("SELECT * FROM employees WHERE firstname LIKE '%{}%'".format(z)).fetchall()
        result = result + c.execute("SELECT * FROM employees WHERE lastname LIKE '%{}%' and not firstname LIKE '%{}%'".format(z,z)).fetchall()
        result = result + c.execute("SELECT * FROM employees WHERE pay LIKE '%{}%' and not firstname LIKE'%{}%' and not lastname LIKE '%{}%'".format(z,z,z)).fetchall()
        con.commit()
        print("--------------------"*2)
        return result
def searchname(z):
        result = c.execute("SELECT * FROM employees WHERE firstname LIKE '%{}%'".format(z)).fetchall()
        con.commit()
        print("--------------------"*2)
        return result
        
def searchsurname(z):
        result = c.execute("SELECT * FROM employees WHERE lastname LIKE '%{}%'".format(z)).fetchall()
        con.commit()
        print("--------------------"*2)
        return result
def searchcash(z):
        result = c.execute("SELECT * FROM employees WHERE pay LIKE '%{}%'".format(z)).fetchall()
        con.commit()
        print("--------------------"*2)
        return result

