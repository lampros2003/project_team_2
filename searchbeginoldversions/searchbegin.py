
import tkinter as tk


#Η κλαση μπαρα παιρνει ενα tk.Tk() object και το κανει παραθυρο αναζητησης
#Η κλάση bara λειτουργεί με self structure(δες αν γίνεται να συμπεριλάβεις το παράθυρο μέσα στην μπάρα)
class bara():
    
    def __init__(self, w):#το initialization της μπάρας 
        self.w = w
        self.w.title("Αναζήτηση")
        self.search()
        self.draw() 
        
    
    def draw(self):#το γραφικό περιβάλλων,ν γίνει πιο ευπαρουσίαστο
        global var
        var = tk.StringVar(self.w)#το κείμενο μεσα στην μπαρα ορίζεται ως μεταβλητη var (οχι τελικό ονομα)
        self.lab1 = tk.Label(self.w, text = 'Γράψε δίπλα για αναζήτηση' )
        self.lab1.grid(row=1,column=0)
        self.ent = tk.Entry(self.w, textvariable= var)
        self.ent.grid(row=1,column=1)
        self.listbo = tk.Listbox(self.w,)
        for i in searchreturn:
            self.listbo.insert(searchreturn.index(i),i)
        self.listbo.grid(row=1,column=2)
        def displayvalue(*args):#εκτυπωνει τπ περιεχόμενο της μπαρας 
    
            print(args)
            print(str(var.get()))

        var.trace_add('write', displayvalue)#κανει trace το περιεχώμενο της μπαρας
    def search(self):
        #εδω ψαχνει το database(μη ολοκληρωμένο)
        global searchreturn
        searchreturn = ['apo1','apo2','apo3','apo4']
        
        
        


w = tk.Tk()
bara(w)
w.mainloop()



