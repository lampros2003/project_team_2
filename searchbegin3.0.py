import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, END, LEFT, RIGHT, TOP, X, Y
from DATABASE1 import *
from operator import itemgetter
from unidecode import unidecode
from datetime import *
import locale
import webbrowser
import subprocess

#Η κλαση μπαρα παιρνει ενα tk.Tk() object και το κανει παραθυρο αναζητησης
#Η κλάση bara λειτουργεί με self structure(δες αν γίνεται να συμπεριλάβεις το παράθυρο μέσα στην μπάρα)
class bara():
    global var
    locale.setlocale(locale.LC_ALL, 'en_US')
    
    def convertTuple(self,tup):
        
        str = ''
        for item in tup:
            str = str +'  '+ item
        return str
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
        if str(makeordervar.get()) == 'Παλαιότερο' :
            
            
            return sorted(self.truesearch((str(var.get()))),key = lambda x:datetime.strptime(x[3], '%d-%b-%Y'))
        
            
        if str(makeordervar.get()) == 'Αλφαβιτική σειρά συγγραφέα':
            return sorted((self.truesearch(str(var.get()))))
            
        if str(makeordervar.get()) == 'Νεότερο':
            return sorted(self.truesearch((str(var.get()))),key = lambda x:datetime.strptime(x[3], '%d-%b-%Y'),reverse = True)
        if str(makeordervar.get()) == 'Αλφαβιτική σειρά τίτλου':
            return  sorted(self.truesearch((str(var.get()))),key = lambda x: x[1])
        if str(makeordervar.get()) == 'Ομοιότητα':
            return self.truesearch(str(var.get()))

        
        
    
    def draw(self):#το γραφικό περιβάλλων,ν γίνει πιο ευπαρουσίαστο
        global var
        global truesearch
        global makeordervar
        global display
        
        makeordervar = tk.StringVar(self.w)
        makeordervar.set('Ομοιότητα')
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
        def searchweb():
            tosearch = self.listbo.curselection()[-1]
            
            thelink = self.listbo.get(tosearch).split(' ')[-1]
            
            webbrowser.open(thelink)

        def searchlocal():
            tosearch = self.listbo.curselection()[-1]
            print(self.listbo.get(tosearch).split('  '))
            thenum = os.path.join(save_path,self.listbo.get(tosearch).split('  ')[1] )
            
            subprocess.Popen( thenum + '.pdf' ,shell=True)
        def downloadspecific():
            tosearch = self.listbo.curselection()[-1]
            dlpath = os.path.join(save_path, self.listbo.get(tosearch).split('  ')[1])
            filurl = self.listbo.get(tosearch).split('  ')[-1]
            
            download_file(filurl,dlpath)

        



        self.msearch = tk.Menu(self.w, tearoff=0)
        self.msearch.add_command(label="Ψάξε στο save_directory", command= searchlocal )
        self.msearch.add_separator()
        self.msearch.add_command(label="Ψάξε στο ίντερνετ", command= searchweb)
        self.msearch.add_separator()
        self.msearch.add_command(label="Κατέβασε το συγκεκριμένο αρχείο", command= downloadspecific)
        def do_popup(event):
            
            self.msearch.tk_popup(event.x_root, event.y_root)
            
        def display(*args):#εκτυπωνει το περιεχόμενο της μπαρας και δείχνει την λίστα
            
            
            self.listbo.delete(0,END)
            if not str(var.get()) == '':
                searchreturn = self.makeorder()
                
                for i in searchreturn:
                    self.listbo.insert(searchreturn.index(i),self.convertTuple(i))
                self.listbo.pack(side= TOP , fill = BOTH, expand = True)
                self.listbo.bind('<Button-3>',do_popup)
                self.scrollbar1.pack(side= RIGHT , fill= Y)    
                
                
            else :pass
        
        
        
        

        self.ordermenu =  tk.OptionMenu(self.frame2, makeordervar, "Νεότερο", "Αλφαβιτική σειρά συγγραφέα","Αλφαβιτική σειρά τίτλου", "Παλαιότερο", 'Ομοιότητα',command= display )
        self.ordermenu.config(bg = 'blue')
        self.ordermenu.pack(side= RIGHT , fill = X, expand = False)

        var.trace_add('write', display)#κανει trace το περιεχώμενο της μπαρας
        
        
        


w = tk.Tk()
bara(w)
w.mainloop()
