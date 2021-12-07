from tkinter import*

win = Tk()
win.geometry("750x250")

my_variable = StringVar()
def tracer(var, index, mode):
   print ("{}".format(my_variable.get()))

my_variable.trace_variable("w", tracer)
Label(win, textvariable = my_variable).pack(padx=5, pady=5)
Entry(win, textvariable = my_variable, width=20).pack(ipadx=20,padx=5, pady=5)
win.mainloop()