import tkinter as tk
from tkinter import messagebox
import os.path
from askhsh import *

download = False
localize_pdf = False


    
def done():
    global localize_pdf
    localize_pdf = True
    pdfpage.destroy()

def yes():
    global download
    download = True
    page.destroy()

if internet:   
    page = tk.Tk()
    page.resizable(False,False)

    b1 = tk.Button(page,text ='renew database',font ='Arial 25',bg='blue',command = yes)
    b1.pack(fill = 'x')
    b2 = tk.Button(page,text ='offline version',font ='Arial 25',bg='blue',command = page.destroy)
    b2.pack(fill = 'x')

    page.mainloop()
else:
    check = os.path.isfile("work.db")
    if not check: messagebox.showinfo("ERROR","Δεν υπαρχει αποθηκευμενη database")

if download:
    
    pdfpage = tk.Tk()
    pdfpage.resizable(False,False)
    
    l1 = tk.Label(pdfpage,text = "Do you want to download the pdf's?",font ='Arial 20',bg='white')
    l1.pack(fill = 'x')
    b1 = tk.Button(pdfpage,text ="YES",font ='Arial 25',bg='blue',command = done)
    b1.pack(fill = 'x')
    b2 = tk.Button(pdfpage,text ='NO',font ='Arial 25',bg='blue',command = pdfpage.destroy)
    b2.pack(fill = 'x')
    
    pdfpage.mainloop() 


