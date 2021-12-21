import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, END, LEFT, RIGHT, TOP
from DATABASE1 import *

#Η κλαση μπαρα παιρνει ενα tk.Tk() object και το κανει παραθυρο αναζητησης
#Η κλάση bara λειτουργεί με self structure(δες αν γίνεται να συμπεριλάβεις το παράθυρο μέσα στην μπάρα)
class bara():
    global var
    makeordervar = 'mostlike'
     
    truesearch = search
    def searchbynamecall(self) :
        self.truesearch= searchname
    def searchbytitlecall(self):
        self.truesearch = searchsurname
    def searchbyallcall(self):
        self.truesearch = search
    def __init__(self, w):#το initialization της μπάρας 
        self.w = w
        
        self.w.title("Αναζήτηση")
        self.draw() 
    def makeorder(self):
        if self.makeordervar == 'date':
            pass
        if self.makeordervar == 'alpha':
            pass
        if self.makeordervar == 'mostlike':
            pass
        pass
        
    
    def draw(self):#το γραφικό περιβάλλων,ν γίνει πιο ευπαρουσίαστο
        global var
        global truesearch
        self.searchbyallcall()
        self.w.config(bg= 'white')
        self.w.geometry('400x300')
        var = tk.StringVar(self.w)#το κείμενο μεσα στην μπαρα ορίζεται ως μεταβλητη var (οχι τελικό ονομα)
        self.frame = tk.Frame()
        self.frame.pack(side= TOP , fill = BOTH, expand = True)
        
        self.lab1 = tk.Label(self.frame, text = 'Γράψε απο κάτω για αναζήτηση' ,bg='blue',fg='white',)
        
        self.searchbyname = tk.Button(self.frame ,text= 'όνομα συγγραφέα',background='blue',fg='white',command=self.searchbynamecall)#οι διαφορετικες μεθοδοι αναζητησης
        self.searchbytitle = tk.Button(self.frame, text= 'τίτλο',background='blue',fg='white',command= self.searchbytitlecall)
        self.searchbyall = tk.Button(self.frame,text = 'όλα τα στοιχεία',background='blue',fg='white',command= self.searchbyallcall)
        self.searchbyall.pack(side= RIGHT , fill = BOTH, expand = True)
        self.searchbyname.pack(side= RIGHT , fill = BOTH, expand = True)
        self.searchbytitle.pack(side= RIGHT , fill = BOTH, expand = True)
        
        
        self.lab1.pack(side= LEFT , fill = BOTH, expand = True)
        self.ent = tk.Entry(self.w, textvariable= var)
        self.ent.pack(side=TOP, fill= BOTH)
        self.listbo = tk.Listbox(self.w,)
        self.listbo.pack(side=BOTTOM,fill=BOTH,expand=True  )
        def display(*args):#εκτυπωνει το περιεχόμενο της μπαρας και δείχνει την λίστα
            
            
            self.listbo.delete(0,END)
            if not str(var.get()) == '':
                searchreturn = self.truesearch(str(var.get()))
                for i in searchreturn:
                    self.listbo.insert(searchreturn.index(i),i)
                    
                self.listbo.pack(side= BOTTOM , fill = BOTH, expand = True)
            else :pass
            

        var.trace_add('write', display)#κανει trace το περιεχώμενο της μπαρας
        
        
        


w = tk.Tk()
bara(w)
w.mainloop()
