from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import certifi
import os
from starter import *

error = False

ssl._create_default_https_context = ssl._create_unverified_context
if not os.path.exists(save_path):#(Λάμπρος Αβούρης ) αν το save_path δεν υπάρχει το φτίαχνω
    os.mkdir(save_path)
def download_pdf(soup):
    links=soup.find_all('a',{'target':'_blank'})
    for link in links:
        if '.pdf' in link.get_text():
            url='https://nemertes.library.upatras.gr/'+link['href']
            return url

def download_file(download_url, filename):#προγραμμα που κατεβάζει ένα αρχείο pdf  με url:downloadurl και το σώζει ως αρχείο με ονομα filename
    response = urlopen(download_url)   #περνω τα bytes του pdf
    file = open(filename + ".pdf", 'wb')#γράφω τα bytes του pdf σε ενα αρχέιο ανοιχτο ως writebytes(wb)
    file.write(response.read())
    file.close()#κλείνω
class Student():
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

def secondary_pages(s):
    bases={}
    Url=urlopen(s)
    info=Url.read()
    soup=BeautifulSoup(info,'html.parser')
    tables=soup.find('table',{'class':'table'})
    L ={'Title:','Other Titles:','Authors:','Keywords:','Keywords (translated):','Abstract:','Abstract (translated):'}
    for tag in tables.find_all('tr'):
        datalist=list(tag.children)
        k = datalist[0].get_text().strip()
        v = (datalist[1].get_text(" "))
        bases[k] = v
        
    P=L-(set(bases.keys()))
    for i in P:
        bases[i]=''
    bases['pdf']=download_pdf(soup)
    if localize_pdf:#(Λαμπρος Αβούρης ) εαν ο χρήστης θέλει να κατεβάσει τα pdf τα κατεβάζω
        completeName = os.path.join(save_path, str(Student.count))
        print(completeName)
        #το συνολικό ονομα του pdf ειναι ο αριθμός του μαθητη του οποιου αποτελει διπλωματικη συνδιασμένο με το save_path
        #τα κάνω join με το os.join για να είμαι σιγουρος οτι αποτελούν σωστό directory
            
        download_file(bases['pdf'],completeName)#κατεβάζω το αρχείο στο directory

    return bases

def main_pages():
    counts=0
    global x
    x = []
    try:  
        while True:
        
            url=urlopen('https://nemertes.library.upatras.gr/jspui/handle/10889/43?offset={}'.format(counts))
            info=url.read()
            soup=BeautifulSoup(info,'html.parser')
            table=soup.find('table',{'class':'table'})
            i=0
            for tag in table.find_all('tr'):
                if i==0:
                    i+=1
                    continue
                datalist=list(tag.children)
                for link in datalist[1].find_all('a', href=True):
                    short_link=link['href'][13:]
                    s='http://hdl.handle.net'+short_link
                    bases=secondary_pages(s)
                    x.append(Student(str(Student.count), bases['Title:'],bases['Other Titles:'],bases['Authors:'],bases['Keywords:'],bases['Keywords (translated):'],bases['Abstract:'],bases['Abstract (translated):'],bases['pdf'],datalist[0].get_text()))
                    Student.count += 1
            if counts%100==0:
                print('{:3.2f}%'.format((len(x)/2288)*100))
            counts+=20
            
            
    except AttributeError:
        print("Completed")
        
if download :main_pages()

