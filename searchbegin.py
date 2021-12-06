
import tkinter as tk


#Η κλαση μπαρα παιρνει ενα tk.Tk() object και το κανει παραθυρο αναζητησης
class bara():
    
    def __init__(self, w):
        self.w = w
        self.w.title("Αναζήτηση")
        self.draw() 
        self.search()
    
    def draw(self):
        var = tk.StringVar()
        self.lab1 = tk.Label(self.w, text = 'Γράψε δίπλα για αναζήτηση' )
        self.lab1.grid(row=1,column=0)
        self.ent = tk.Entry(self.w, textvariable= var)
        self.ent.grid(row=1,column=1)
        
    def search(self):


w = tk.Tk()
bara(w)
w.mainloop()



