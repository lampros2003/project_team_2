import tkinter as tk
import os.path
import sys
from tkinter import messagebox
from askhsh import *
from tkinter import filedialog

check = False
download = False
localize_pdf = False

if not os.path.isfile('wheretosave.txt') :#αν δεν υπαρχει αρχειο που σώζει το Path το φτιαχνω (μονο στην πρωτη φορα θα συμβει αυτο προφανως )   
    with open('wheretosave.txt', 'w') as f:#σωζω το αρχικό save_directory 
        f.write('nemertespdfs')
    
    save_path ='nemertespdfs'
else :
    
    with open('wheretosave.txt', 'r') as f:#εαν το αρχείο υπαρχει διαβάζω το save directory
        save_path = f.read()
     
def check():   #ελέγχει εάν υπάρχει το database. εάν οχι δίνει warning
    checking = os.path.isfile("work.db")
    
    if not checking:
        messagebox.showwarning("ERROR","Δεν υπαρχει απθηκευμενη database")
        global check
        check = False
    elif internet: page.destroy()
    
def yes():
    global localize_pdf
    answer = messagebox.askquestion("Προσοχη!","Εάν έχετε ήδη κατεβασμένα pdf και αλλαξετε το directory δεν θα μπορειτε να έχετε πρόσβαση μέσω της εφαρμογής")
    if answer == 'yes':
        global save_path
        localize_pdf = True
        save_path = filedialog.askdirectory()#(Λαμπρος Αβουρης) Παίρνω path απο τον χρήστη  
        with open('wheretosave.txt', 'w') as f:#σώζω το path σε αρχέιο
            f.write(save_path)
        pdfpage.destroy()

def renew():
    global download,check
    download,check = True,True
    page.destroy()

if internet:  
    page = tk.Tk()       # window που δίνει στον χρήστη την επιλογή να ανανεώσει τη βάση δεδομένων ή όχι αμα υπάρχει σύνδεση στο ιντερνετ
    page.resizable(False,False)

    b1 = tk.Button(page,text ='renew database',font ='Arial 25',bg='blue',command = renew)
    b1.pack(fill = 'x')
    b2 = tk.Button(page,text ='saved version',font ='Arial 25',bg='blue',command = check)
    b2.pack(fill = 'x')

    page.mainloop()

    pdfpage = tk.Tk() 
    pdfpage.resizable(False,False)
    
    l1 = tk.Label(pdfpage,text = "Θέλετε να αλλάξετε το save directory των pdfs; ",font ='Arial 20',bg='white')
    l1.pack(fill = 'x')
    b1 = tk.Button(pdfpage,text ="YES",font ='Arial 25',bg='blue',command = yes)
    b1.pack(fill = 'x')
    b2 = tk.Button(pdfpage,text ='NO',font ='Arial 25',bg='blue',command = pdfpage.destroy)
    b2.pack(fill = 'x')
    
    pdfpage.mainloop()
else:check()


   
if not check: sys.exit()  #εαν δεν υπάρχει η βάση δεδομένων ή δεν θα την κατεβάσει ο χρήστης κλείνει το πρόγραμμα

