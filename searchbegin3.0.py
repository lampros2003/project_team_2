import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, END, LEFT, RIGHT, TOP, X, Y
from DATABASE1 import *
from operator import itemgetter
from unidecode import unidecode
from datetime import *
import locale
#Η κλαση μπαρα παιρνει ενα tk.Tk() object και το κανει παραθυρο αναζητησης
#Η κλάση bara λειτουργεί με self structure(δες αν γίνεται να συμπεριλάβεις το παράθυρο μέσα στην μπάρα)
class bara():
    global var
    locale.setlocale(locale.LC_ALL, 'en_US')
    
     
    truesearch = search
    def searchbynamecall(self) :
        self.truesearch= searchname
        
    def searchbytitlecall(self):
        self.truesearch = searchtitle
        
    def searchbyallcall(self):
        self.truesearch = search
        
    def __init__(self, w):#το initialization της μπάρας 
        self.w = w
        
        self.w.title("Αναζήτηση")
        self.draw() 
    def makeorder(self):
        if str(makeordervar.get()) == 'date reverse' :
            
            
            return sorted(self.truesearch((str(var.get()))),key = lambda x:datetime.strptime(x[2], '%d-%b-%Y'))
        
            
        if str(makeordervar.get()) == 'alpha writer':
            return sorted((self.truesearch(str(var.get()))))
            
        if str(makeordervar.get()) == 'date':
            return sorted(self.truesearch((str(var.get()))),key = lambda x:datetime.strptime(x[2], '%d-%b-%Y'),reverse = True)
        if str(makeordervar.get()) == 'alpha title':
            return  sorted(self.truesearch((str(var.get()))),key = lambda x: x[1])


        
        
    
    def draw(self):#το γραφικό περιβάλλων,ν γίνει πιο ευπαρουσίαστο
        global var
        global truesearch
        global makeordervar
        global display
        
        makeordervar = tk.StringVar(self.w)
        makeordervar.set('date')
        self.searchbyallcall()
        self.w.config(bg= 'white')
        self.w.geometry('1000x1000')
        var = tk.StringVar(self.w)#το κείμενο μεσα στην μπαρα ορίζεται ως μεταβλητη var (οχι τελικό ονομα)
        self.frame = tk.Frame(bg = 'Blue')
        self.frame.pack(side= TOP , fill = BOTH, expand = False)
        
        self.lab1 = tk.Label(self.frame, text = 'Γράψε απο κάτω για αναζήτηση βασει' ,bg='blue',fg='white')
        
        self.searchbyname = tk.Button(self.frame ,text= 'όνομα συγγραφέα',background='blue',fg='white',command= lambda :[self.searchbynamecall(),display()])#οι διαφορετικες μεθοδοι αναζητησης
        self.searchbytitle = tk.Button(self.frame, text= '     τίτλο    ',background='blue',fg='white',command= lambda :[self.searchbytitlecall(),display()])
        self.searchbyall = tk.Button(self.frame,text = 'όλα τα στοιχεία',background='blue',fg='white',command= lambda :[self.searchbyallcall(),display()])
        self.frame2 = tk.Frame(bg='Blue')
        self.frame2.pack(side= TOP , fill = X, expand = False)
        self.ordlab = tk.Label(self.frame2, text = 'Ταξινόμισε την αναζήτηση βάσει' ,bg='blue',fg='white')
        self.ordlab.pack(side= LEFT , fill = X, expand = False)
        
        
        
        self.lab1.pack(side= LEFT , fill = BOTH, expand = True,)
        self.searchbyall.pack(side= RIGHT , fill = BOTH, expand = True,)
        self.searchbyname.pack(side= RIGHT , fill = BOTH, expand = True)
        self.searchbytitle.pack(side= RIGHT , fill = BOTH, expand = True)
        
        
        
        self.ent = tk.Entry(self.w, textvariable= var)
        self.ent.pack(side=TOP, fill= BOTH)
        self.listbo = tk.Listbox(self.w,)
        self.scrollbar1 = tk.Scrollbar(self.w)
        self.scrollbar1.pack(side = RIGHT, fill = Y)
        self.listbo.pack(side=TOP,fill=BOTH,expand=True  )
        
        self.listbo.config(yscrollcommand = self.scrollbar1.set)
        self.scrollbar1.config(command = self.listbo.yview)
        self.scrollbar2 = tk.Scrollbar(self.w, orient= 'horizontal')
        self.scrollbar2.pack(side = BOTTOM, fill = X)
        self.listbo.config(xscrollcommand = self.scrollbar2.set)
        self.scrollbar2.config(command = self.listbo.xview)
        def display(*args):#εκτυπωνει το περιεχόμενο της μπαρας και δείχνει την λίστα
            
            
            self.listbo.delete(0,END)
            if not str(var.get()) == '':
                searchreturn = self.makeorder()
                
                for i in searchreturn:
                    self.listbo.insert(searchreturn.index(i),i)
                self.listbo.pack(side= TOP , fill = BOTH, expand = True)
                self.scrollbar1.pack(side= RIGHT , fill= Y)    
                
            else :pass
        
        
        
        

        self.ordermenu =  tk.OptionMenu(self.frame2, makeordervar, "date", "alpha writer","alpha title", "date reverse",command= display )
        self.ordermenu.config(bg = 'blue')
        self.ordermenu.pack(side= RIGHT , fill = X, expand = False)

        var.trace_add('write', display)#κανει trace το περιεχώμενο της μπαρας
        
        
        


w = tk.Tk()
bara(w)
w.mainloop()
