import requests
from bs4 import BeautifulSoup

def scrape(query):
    l=[]
    store={}

    URL = "https://news.google.com/search?q="+str(query)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    name = soup.find_all(class_="JtKRv")
    image=soup.find_all(class_="K0q4G")
    time=soup.find_all(class_="hvbAAd")
    link=soup.find_all(class_="WwrzSb")

    for i in range(0,len(name)):
        try:
            title=str(name[i]).split('tabindex="0">')[1].split("</h4>")[0]
            imagelink=str(image[i]).split('src="')[1].split('" src')[0]
            upload=time[i].text
            articleLink=str(link[i]).split('href="')[1].split('" jslog')[0]
            store[i]={"title":title,"image":imagelink,"uploadTime":upload,"articlelink":articleLink}
        except:
            print("That's Enough!")
            break
    #print(store[0])
    return store
