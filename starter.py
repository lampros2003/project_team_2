import tkinter as tk

download = False

def yes():
    global download
    download = True
    page.destroy()

    
page = tk.Tk()
page.resizable(False,False)

b1 = tk.Button(page,text ='renew database',font ='Arial 30',bg='blue',command = yes)
b1.pack()
b2 = tk.Button(page,text ='offline version',font ='Arial 30',bg='blue',command = page.destroy)
b2.pack()

page.mainloop()
