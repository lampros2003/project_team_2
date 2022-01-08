from tkinter.constants import TRUE
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
download = True
error = False
localize_pdf = True
save_path = '/pdfs'
if not os.path.exists(save_path):
    os.mkdir(save_path)
def download_pdf(soup):
    links=soup.find_all('a',{'target':'_blank'})
    for link in links:
        if '.pdf' in link.get_text():
            url='https://nemertes.library.upatras.gr/'+link['href']
            return url
def download_file(download_url, filename):
    response = urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()
class Student():
    count=0
    def __init__(self, countofstu ,writer,title,trans_title,date,kwords,trans_kwords,summary , url):
        self.countofstu = countofstu 
        self.writer=writer
        self.title=title
        self.trans_title=trans_title
        self.date=date
        self.kwords=kwords
        self.trans_kwords=trans_kwords
        self.summary=summary
        self.url= url
        self.count+=1
        
    def display_count(self):
        print(self.count)
    def return_contents(self):
        return self.writer + ' , '+self.title +' , '+self.trans_title +' , '+self.date + ' , '+self.kwords +' , '+self.trans_kwords +' , ' +self.summary+' , '+self.url
    def __repr__(self) :
        return str(self.countofstu) + ' , ' +self.writer + ' , '+self.title +' , '+self.trans_title +' , '+self.date + ' , '+self.kwords +' , '+self.trans_kwords +' , ' +self.summary+' , '+self.url
    
def secondary_pages(s):
    bases={}
    Url=urlopen(s)
    info=Url.read()
    soup=BeautifulSoup(info,'html.parser')
    tables=soup.find('table',{'class':'table'})
    i=0
    for tag in tables.find_all('tr'):
        datalist=list(tag.children)
        bases[i]=(datalist[1].get_text(" "))
        i+=1
    bases[i]=download_pdf(soup)
    if localize_pdf :
        completeName = os.path.join(save_path, str(Student.count))
        print(str(Student.count))
        print('at work')
        download_file(bases[list(bases)[-1]],completeName)
    return bases

def main_pages():
    count=0
    global x
    x = []

    
    #try:
    while True:
        url=urlopen('https://nemertes.library.upatras.gr/jspui/handle/10889/43?offset={}'.format(count))
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
                s='https://nemertes.library.upatras.gr'+link['href']
                pfile=secondary_pages(s)

                x.append(Student(Student.count,pfile[2],pfile[0],pfile[1],datalist[0].get_text(),pfile[3], pfile[4],pfile[6],pfile[7]))
                Student.count += 1
                print(x[-1])
        count+=20
        if count == 40:
            print(x[-1])
            break    
            
            
    #except:
        
        #print(count)
        #global error
        #error = True
        

if download :main_pages()
