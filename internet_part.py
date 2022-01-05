from urllib.request import urlopen
from bs4 import BeautifulSoup
x=[]

def download_pdf(soup):
    links=soup.find_all('a',{'target':'_blank'})
    for link in links:
        if '.pdf' in link.get_text():
            url='https://nemertes.library.upatras.gr/'+link['href']
class Student():
    count=0
    def __init__(self,writer,title,trans_title,date,kwords,trans_kwords,summary):
        self.writer=writer
        self.title=title
        self.trans_title=trans_title
        self.date=date
        self.kwords=kwords
        self.trans_kwords=trans_kwords
        self.summary=summary
        self.url=url
        self.count+=1
    def display_count(self):
        print(self.count)
    def return_contents(self):
        return self.writer + ' / '+self.title +' / '+self.trans_title +' / '+self.date + ' / '+self.kwords +' / '+self.trans_kwords +' / ' +self.summary+' / '+self.url
    def __repr__(self) :
        return self.writer + ' / '+self.title +' / '+self.trans_title +' / '+self.date + ' / '+self.kwords +' / '+self.trans_kwords +' / ' +self.summary+' / '+self.url
    
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
    return bases

def main_pages():
    count=0
    global stulist
    stulist = []
    global x
    x = stulist
    
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
                    s='https://nemertes.library.upatras.gr'+link['href']
                    pfile=secondary_pages(s)
                    stulist.append(Student(pfile[2],pfile[0],pfile[1],datalist[0].get_text(),pfile[3], pfile[4],pfile[6],pfile[7]))
            count+=20
            
            
            
    except:
        print("Completed")
        

if __name__ =="__main__":main_pages()
