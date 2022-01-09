from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import certifi
import os
localize_pdf = False
download = False
error = False
save_path = '/nemertespdfs'
ssl._create_default_https_context = ssl._create_unverified_context
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
    if localize_pdf:
        completeName = os.path.join(save_path, str(Student.count))
        if not os.path.exists(completeName):
            
            download_file(bases['pdf'],completeName)

    return bases

def main_pages():
    count=0
    global x
    x = []
    try:  
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
                    short_link=link['href'][13:]
                    s='http://hdl.handle.net'+short_link
                    bases=secondary_pages(s)
                    x.append(Student(str(Student.count), bases['Title:'],bases['Other Titles:'],bases['Authors:'],bases['Keywords:'],bases['Keywords (translated):'],bases['Abstract:'],bases['Abstract (translated):'],bases['pdf'],datalist[0].get_text()))
                    Student.count += 1
            if count%100==0:
                print('{:3.2f}%'.format((len(x)/2288)*100))
            counts+=20
    except AttributeError:
        print("Completed")
if download :main_pages()

