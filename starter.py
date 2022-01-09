import tkinter as tk


def yes():
    global download
    download = True
    page.destroy()

def no():
    global download
    download = False
    page.destroy()
    
page = tk.Tk()
page.resizable(False,False)

b1 = tk.Button(page,text ='renew database',font ='Arial 30',bg='blue',command = yes).pack()
b2 = tk.Button(page,text ='offline version',font ='Arial 30',bg='blue',command = no).pack()

page.mainloop()
