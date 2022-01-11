import tkinter as tk
import os.path
import sys
from tkinter import messagebox
from askhsh import *

check = True
download = False
localize_pdf = False

def check():
    checking = os.path.isfile("work.db")
    if not checking:
        messagebox.showinfo("ERROR","Δεν υπαρχει απθηκευμενη database")
        global check
        check = False
    elif internet: page.destroy()
    
def done():
    global localize_pdf
    global answer
    answer = messagebox.askquestion("Προσοχη!","Για να κατεβούν τα pdf χρειάζεται πολύ ώρα.Είστε σίγουροι οτι θέλετε να συνεχίσετε;")
    if answer == 'yes':
        localize_pdf = True
        pdfpage.destroy()

def yes():
    global download,check
    download,check = True,True
    page.destroy()

if internet:   
    page = tk.Tk()
    page.resizable(False,False)

    b1 = tk.Button(page,text ='renew database',font ='Arial 25',bg='blue',command = yes)
    b1.pack(fill = 'x')
    b2 = tk.Button(page,text ='offline version',font ='Arial 25',bg='blue',command = check)
    b2.pack(fill = 'x')

    page.mainloop()
else:check()

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

    
if not check: sys.exit()  

