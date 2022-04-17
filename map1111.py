from bs4 import BeautifulSoup 
import urllib.request 



def make_issac_list():
    url = 'http://www.isaacs.co.kr/bbs/board.php?bo_table=branches&page=' 
    page_num = 2
    issac_list = []
    
    for j in range(1,page_num):
        sourcecode = urllib.request.urlopen(url+str(j)).read()
        soup = BeautifulSoup(sourcecode, 'html.parser')

        for i in soup.find_all('td','td_subject'):
            temp_text = i.get_text()

            issac_list.append(temp_text)
    return issac_list

print(make_issac_list())

