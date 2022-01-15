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
#Λάμπρος Αβούρης :-)
class bara():
    global var
    locale.setlocale(locale.LC_ALL, 'en_US')#Η εντολή κάνει το προγραμμα να διαβάζει ημερομηνίες
    #(και διάφορα αλλα στοιχεία που δεν χρειάζονται) σαν να είναι γραμμένα σε locale en_US
    #(Αμερικάνικα Αγγλικά) π.χ. ημ: 10-JUN-2020
    #Αυτό καθώς ο nemertes αποθηkεύει τις ημερομηνίες του με αυτό το locale
    
    def convertTuple(self,tup):#Μετατρέπει ένα tuple σε str χωρίζοντας με \t τα items του
        #χρησημεύει στο να εισάγω στο listbox τα items του searchreturn καθώς η εισαγωγή πλειάδων σε 
        #listbox δεν έχει καλό εμφανισιακό αποτέλεσμα
        
        str = ''
        
        for item in tup:
            str = str +'  '+ item
        return str
    truesearch = search
    #Τα διαφορετικά search 
    def searchbynamecall(self) :
        self.truesearch= searchname#θέτω το truesearch  ως το searchname της database
        
    def searchbytitlecall(self):#όμοια οπως παραπάνω με search title
        self.truesearch = searchtitle
        
    def searchbyallcall(self):#και με search
        self.truesearch = search
        
    def __init__(self, w):#το initialization της μπάρας 
        self.w = w
        
        self.w.title("Αναζήτηση")#Τίτλος 
        self.draw() #δημιουργεία ui 
    def makeorder(self):#Το function ταξινόμησης 
        #άναλογα με την επιλογή του user  κανει sort βάσει αντίσοιχα κριτίρια
        if str(makeordervar.get()) == 'Παλαιότερο' :
            return sorted(self.truesearch((str(var.get()))),key = lambda x:datetime.strptime(x[3], '%d-%b-%Y'))
            #Παραπάνω περνω αυτό που επιστρέφει η search return και κάνω sort  θέτοντας όπου key
            #(key είναι αυτό βασει το οποίο γινετε η συγκριση της λίστας)  αντι για το στοιχείο x το datetime object
            # To οποίο προκειψει αφού μετατρέψω το 3 index της πλειάδας x (το self.truesearch σαφώς αποτελεί
            # μια λίστα πλειάδων)  μέσω της μεθόδου datetime.strptime()(το χ[3] είναι ημερομηνία σε locale en_US)
            # το %d %b δηλώνουν οτι η ημερομηνία είναι locale
            
        if str(makeordervar.get()) == 'Αλφαβιτική σειρά συγγραφέα':
            return sorted((self.truesearch(str(var.get()))),key = lambda x: x[1])
            # sort της λιστας οπου για το item x της λιστας θετω x[1]

            
        if str(makeordervar.get()) == 'Νεότερο':
            #ακριβώς η ίδια διαδικασία με το παλαιότερο αλλα reversed
            return sorted(self.truesearch((str(var.get()))),key = lambda x:datetime.strptime(x[3], '%d-%b-%Y'),reverse = True)
        if str(makeordervar.get()) == 'Αλφαβιτική σειρά τίτλου':
            return  sorted(self.truesearch((str(var.get()))),key = lambda x: x[2])
            #sort βάσει το δεύτερο στοιχείο της πλειάδας x (ο τιτλος)
        if str(makeordervar.get()) == 'Ομοιότητα':
            #δεν χρειάζεται να κάνω sort
            return self.truesearch(str(var.get()))

        
        
    
    def draw(self):#το γραφικό περιβάλλων
        global var#ορισμένες μεταβλητες που χρειάζεται όλο το πρόγραμμα
        global truesearch
        global makeordervar
        global display
        
        makeordervar = tk.StringVar(self.w)
        makeordervar.set('Ομοιότητα')#οριζω τον αρχικό τροπο ταξινώμησης
        self.searchbyallcall()#καλω για να φτιαχτει το listbox
        self.w.config(bg= 'white')#χρώμα
        self.w.geometry('1000x1000')#γεωμετρια του παραθυρου
        
                
        var = tk.StringVar(self.w)#το κείμενο μεσα στην μπαρα ορίζεται ως μεταβλητη stringvar 
        self.frame = tk.Frame(bg = 'Blue')
        self.frame.pack(side= TOP , fill = BOTH, expand = False)#με την μέθοδο pack τοποθετό το πρωτο frame μεσα στο window 
        #το παραπάνω ισχύει για όλα τα γραφικά στοιχεία τοποθετούνται δηλαδη στο αντίστοιχο master τους με μέθοδο .pack 
        
        self.lab1 = tk.Label(self.frame, text = 'Γράψε απο κάτω για αναζήτηση βασει' ,bg='blue',fg='white')#δείχνω κειμενο
        
        self.searchbyname = tk.Button(self.frame ,text= 'όνομα συγγραφέα',background='blue',fg='white',command= lambda :[self.searchbynamecall(),display()])
        self.searchbytitle = tk.Button(self.frame, text= '     τίτλο    ',background='blue',fg='white',command= lambda :[self.searchbytitlecall(),display()])
        self.searchbyall = tk.Button(self.frame,text = 'όλα τα στοιχεία',background='blue',fg='white',command= lambda :[self.searchbyallcall(),display()])
        #πάνω είναι τα κουμπιά που διαχειρίζονται τις διαφορες μεθόδους αναζητησης (αναλογα ποιο παατήσει ο user αυτη η μεθοδος επιλέγεται)
        self.frame2 = tk.Frame(bg='Blue')#δευτερο frame 
        self.frame2.pack(side= TOP , fill = X, expand = False)#pack του frame
        self.ordlab = tk.Label(self.frame2, text = 'Ταξινόμισε την αναζήτηση βάσει' ,bg='blue',fg='white')#δείχνω κείμενο στο χρηστη 
        self.ordlab.pack(side= LEFT , fill = X, expand = False)#pack όλα τα στοιχεία των δύο frames
        self.lab1.pack(side= LEFT , fill = BOTH, expand = True,)
        self.searchbyall.pack(side= RIGHT , fill = BOTH, expand = True,)
        self.searchbyname.pack(side= RIGHT , fill = BOTH, expand = True)
        self.searchbytitle.pack(side= RIGHT , fill = BOTH, expand = True)
        
        
        
        self.ent = tk.Entry(self.w, textvariable= var)#το entry που παιρνει Input
        self.ent.pack(side=TOP, fill= BOTH)#pack
        self.listbo = tk.Listbox(self.w,)#to listbox που δείχνει το output
        self.scrollbar1 = tk.Scrollbar(self.w)#scrollbar για το listbox
        self.scrollbar1.pack(side = RIGHT, fill = Y)#ston y
        self.listbo.pack(side=TOP,fill=BOTH,expand=True  )
        
        self.listbo.config(yscrollcommand = self.scrollbar1.set)
        self.scrollbar1.config(command = self.listbo.yview)#scroll bar se y
        self.scrollbar2 = tk.Scrollbar(self.w, orient= 'horizontal')
        self.scrollbar2.pack(side = BOTTOM, fill = X)
        self.listbo.config(xscrollcommand = self.scrollbar2.set)
        self.scrollbar2.config(command = self.listbo.xview)#allo scrollbar για αξονα χ
        def searchweb():#το function που ψάχνει pdf στο web
            try : 
                tosearch = self.listbo.curselection()[-1]#pernv to τελευταίο (και μοναδικο στοιχείο )που έχει απιλεχθεί απο τον χρηστη
                
                thelink = self.listbo.get(tosearch).split(' ')[-1]# παιρνω το pdf απο τo listbox κανοντας του split και πρνοντας το τελευταιο item
                
                webbrowser.open(thelink)#ψάχνω στο διαδίκτυο για το λινκ του pdf
            except: print('Επιλέξτε ένα απο τα αποτελέσματα με δεξί κλικ')

        def searchlocal():#function που ψάχνει το αρχίο στο savepath 
            try:   
                tosearch = self.listbo.curselection()[-1]
                
                thenum = os.path.join(save_path,self.listbo.get(tosearch).split('  ')[2] )#παιρνω το όνομα του μαθητη
                # μετα δημιουργώ το path που θα είχε ο αριθμός αυτος αν ηταν κατεβασμενο το pdf
                subprocess.Popen( thenum + '.pdf' ,shell=True)#ψάχνω και ανοίγω το pdf μέσω της process  popen
            except: print('Επιλέξτε ένα απο τα αποτελέσματα με δεξί κλικ')
        def downloadspecific():
            try:
                tosearch = self.listbo.curselection()[-1]
                dlpath = os.path.join(save_path, self.listbo.get(tosearch).split('  ')[2])
                filurl = self.listbo.get(tosearch).split('  ')[-1]
                #και το λινκ fileurl και το complete directory του αρχείου dlpath
                download_file(filurl,dlpath)
                #κατεβάζω το αρχείο στο dlpath
            except: print('Επιλέξτε ένα απο τα αποτελέσματα με δεξί κλικ')

        



        self.msearch = tk.Menu(self.w, tearoff=0)#φτίχνω popupmenu Που διαχειρίζεται τα functions για να ψάξω pdf που έκανα παραπάνω
        self.msearch.add_command(label="Ψάξε στο save_directory", command= searchlocal )
        self.msearch.add_separator()
        self.msearch.add_command(label="Ψάξε στο ίντερνετ", command= searchweb)
        self.msearch.add_separator()
        self.msearch.add_command(label="Κατέβασε το συγκεκριμένο αρχείο", command= downloadspecific)
        def popemup(event):#το function που δημηουργέει το popoup menu στο σημείο που έκανε  leftclick ο χρήστης 
            
            self.msearch.tk_popup(event.x_root, event.y_root)
            
        def display(*args):# δείχνει την λίστα τών αποτελεσμάτων αναζητηασης
            
            
            self.listbo.delete(0,END)#κανω refresh το listbox
            if not str(var.get()) == '':#εαν υπάρχει κατι με βάσει το οποίο να γίνει αναζήτηση αναζητώ
                try:
                    searchreturn = self.makeorder()
                    
                    for i in searchreturn:#βάζω τα αποτελέσματα στο Listbox ως str
                        self.listbo.insert(searchreturn.index(i),self.convertTuple(i))
                    self.listbo.pack(side= TOP , fill = BOTH, expand = True)#κάνω pack to listbox
                    self.listbo.bind('<Button-3>',popemup)#κάνω bind το button3 με το popemup
                    self.scrollbar1.pack(side= RIGHT , fill= Y)    #ξανακάνω pack to σψρολλβαρ για να μείνει στην ίδια θέση
                except: pass
                
                
            else :pass
        
        
        
        
        #ορίζω το μενού οπου ο χρήστης επιλέγει μέθοδο ταξινώμησης 
        self.ordermenu =  tk.OptionMenu(self.frame2, makeordervar, "Νεότερο", "Αλφαβιτική σειρά συγγραφέα","Αλφαβιτική σειρά τίτλου", "Παλαιότερο", 'Ομοιότητα',command= display )
        self.ordermenu.config(bg = 'blue')
        self.ordermenu.pack(side= RIGHT , fill = X, expand = False)

        var.trace_add('write', display)#κανει trace το περιεχώμενο της μπαρας και κάθε φορά που αλλάζει ψάχνει εκ νέου
        
        
        


w = tk.Tk()#το παραθηρο 
bara(w)
w.mainloop()
#########_______________________________END______________________________________