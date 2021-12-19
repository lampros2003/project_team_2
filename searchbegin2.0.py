import tkinter as tk
from tkinter.constants import END
from DATABASE1 import *

#Η κλαση μπαρα παιρνει ενα tk.Tk() object και το κανει παραθυρο αναζητησης
#Η κλάση bara λειτουργεί με self structure(δες αν γίνεται να συμπεριλάβεις το παράθυρο μέσα στην μπάρα)
class bara():
    
    def __init__(self, w):#το initialization της μπάρας 
        self.w = w
        self.label=tk.Label(self.w,text=elements()).grid(row=0,column=0)
        self.w.title("Αναζήτηση")
        self.draw() 
        
    
    def draw(self):#το γραφικό περιβάλλων,ν γίνει πιο ευπαρουσίαστο
        global var
        self.w.config(bg= 'white')
        self.w.geometry('400x300')
        var = tk.StringVar(self.w)#το κείμενο μεσα στην μπαρα ορίζεται ως μεταβλητη var (οχι τελικό ονομα)
        
        
        self.lab1 = tk.Label(self.w, text = 'Γράψε δίπλα για αναζήτηση' ,bg='blue',fg='white')
        self.lab1.grid(row=1,column=0)
        self.ent = tk.Entry(self.w, textvariable= var)
        self.ent.grid(row=1,column=1)
        self.listbo = tk.Listbox(self.w,)
        def display(*args):#εκτυπωνει το περιεχόμενο της μπαρας και δείχνει την λίστα
            
            print(str(var.get()))
            self.listbo.delete(0,END)
            if not str(var.get()) == '':
                searchreturn = search(str(var.get()))
                for i in searchreturn:
                    self.listbo.insert(searchreturn.index(i),i)
                    print(type(i))#check remove 
                    print(i)
                self.listbo.grid(row=2,column=1)
            else :pass
            

        var.trace_add('write', display)#κανει trace το περιεχώμενο της μπαρας
        
        
        


w = tk.Tk()
bara(w)
w.mainloop()
