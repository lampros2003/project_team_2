from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup
import ssl
import certifi
import os
from starter import *

error = False
#Δημοσθένης Καραμπάρπας = Δ
#Λάμπρος Αβούρης= Λ

ssl._create_default_https_context = ssl._create_unverified_context
if not os.path.exists(save_path):#(Λ) Αν το save_path δεν υπάρχει το φτίαχνω
    os.mkdir(save_path)

def download_pdf(soup):#(Δ) 
    links=soup.find_all('a',{'target':'_blank'})
    for link in links:
        if '.pdf' in link.get_text():
            url='https://nemertes.library.upatras.gr/'+link['href']
            return url

def download_file(download_url, filename):#(Δ)Κατέβασμα αρχείου pdf με όνομα βασισμένο στα δεδομένα του μαθητή
    response = urlopen(download_url)  #(Δ) περνω το url του pdf
    file = open(filename + ".pdf", 'wb')#(Δ) ανοίγω το url και αντιγράφω το στοιχεία του σε ένα αρχείο
    file.write(response.read())
    file.close()
class Student():#(Δ) κλάση που αποθηκεύει και οργανώνει τις κατέβασμένες πληροφορίες για τις εργασίες
    count=0
    def __init__(self,stucount,title='',trans_title='',writer='',kwords='',trans_kwords='',summary='',trans_summary='',url='',date=''):
        self.stucount = stucount
        self.writer=writer
        self.title=title
        self.trans_title=trans_title
        self.date=date
        self.kwords=kwords
        self.trans_kwords=trans_kwords
        self.summary=summary
        self.trans_summary=trans_summary
        self.url=url
        self.count+=1
    def display_count(self):
        print(self.count)
    def return_contents(self):
        return self.writer + ' , '+self.title +' , '+self.trans_title +' , '+self.date + ' , '+self.kwords +' , '+self.trans_kwords +' , ' +self.summary +' , '+self.trans_summary
    def __repr__(self) :
        return str(self.writer) + ' , '+str(self.title) +' , '+str(self.trans_title) +' , '+str(self.date) + ' , '+str(self.kwords) +' , '+str(self.trans_kwords) +' , ' +str(self.summary) +' , '+str(self.trans_summary)

def secondary_pages(s):#(Δ)Συνάρτηση που μεταφέρεται μεταξύ των δευτερεύοντων σελίδων
    bases={}
    Url=urlopen(s)
    info=Url.read()
    soup=BeautifulSoup(info,'html.parser')#(Δ)Τα περιεχόμενα της σελίδας html αποθηκεύονται σε μεταβλητή
    tables=soup.find('table',{'class':'table'})#(Δ)Αποδήκευση του πίνακα που περιέχει η σελίδα με τις μεταβλητές που θέλω
    L ={'Title:','Other Titles:','Authors:','Keywords:','Keywords (translated):','Abstract:','Abstract (translated):'}
    for tag in tables.find_all('tr'):#(Δ)Αποθήκευση των στοιχείων που με ενδιαφέρουν με κατάλληλο κλειδί που τους ταιριάζει
        datalist=list(tag.children)
        k = datalist[0].get_text().strip()
        v = (datalist[1].get_text(" "))
        bases[k] = v     
    P=L-(set(bases.keys()))#(Δ)Για να μη ζητά κλειδί για μεταβλητή που δεν είχε μια εργασία
    for i in P:
        bases[i]=''
    bases['pdf']=download_pdf(soup)#(Δ)Αποθηκέυει το url του pdf
    
    #if localize_pdf:#(Λ) εαν ο χρήστης θέλει να κατεβάσει τα pdf τα κατεβάζω
    #    completeName = os.path.join(save_path, str(Student.count))
    
        #(Λ)το συνολικό ονομα του pdf ειναι ο αριθμός του μαθητη του οποιου αποτελει διπλωματικη συνδιασμένο με το save_path
        #(Λ)τα κάνω join με το os.join για να είμαι σιγουρος οτι αποτελούν σωστό directory
            
    #    download_file(bases['pdf'],completeName)#(Δ)Κατέβασμα pdf
    #(Λ)SOS note η παραπάνω δομη δεν χρησημοποιειτε λογω περιορισμων του nemertes(δεν αφήνει  τη ληψη τόσο μεγάλου όγκου pdfs)
    #αν ο περιορισμος αυτος παυσει να υπάρχει απλα βγάλτε τις γραμμες 66,67,72 απο comment

    return bases

def main_pages():
    counts=0
    global x
    x = []
    try:  
        while True:
        
            url=urlopen('https://nemertes.library.upatras.gr/jspui/handle/10889/43?offset={}'.format(counts))#(Δ)Μετακίνηση μεταξύ των σελιδών
            info=url.read()
            soup=BeautifulSoup(info,'html.parser')
            table=soup.find('table',{'class':'table'})#(Δ)Εύρεση του κύριου πίνακα με τις ημερομηνίες και hypertexts
            i=0
            for tag in table.find_all('tr'):#(Δ)Εύρεση του κάθε μαθητή
                if i==0:#(Δ)Το πρώτο στοιχείο στην λίστα δεν χρειάζεται
                    i+=1
                    continue
                datalist=list(tag.children)#(Δ)
                for link in datalist[1].find_all('a', href=True):#(Δ) 
                    short_link=link['href'][13:]#(Δ) Ακολουθία οδηγιών στο nemertes πιθανόν λόγω συχνής χρήσης
                    s='http://hdl.handle.net'+short_link
                    bases=secondary_pages(s)#(Δ)Τρέχει δευτερεύουσες σελίδες για να πάρει τις πληροφορίες από το html του hyperlink
                    x.append(Student(str(Student.count), bases['Title:'],bases['Other Titles:'],bases['Authors:'],bases['Keywords:'],bases['Keywords (translated):'],bases['Abstract:'],bases['Abstract (translated):'],bases['pdf'],datalist[0].get_text()))
                    if x[-1].writer == 'Τάσση, Σταυρούλα':
                        print(x[-1])
                    #(Δ)Βάζει τα στοιχεία στην κλάση για λόγους οργάνωσης και μετά σε λίστα για χρήση από τα άλλα κομμάτια της εργασίας
                    Student.count += 1
            if counts%100==0:
                print('{:3.2f}%'.format((len(x)/2288)*100))
                #(Δ)Δείχνει ποσοστό που έχει κατέβει η εργασία
            counts+=20
            
            
    except AttributeError:#(Δ)Το πρόγραμμα τελειώνει όταν δεν έχουν μείνει καθόλου στοιχεία
        print("Completed")
    except (urllib.error.URLError,urllib.error.HTTPError) as e:
    print(e.code+' There was a problem with the website')    
if download :main_pages()

