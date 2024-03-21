import requests
from bs4 import BeautifulSoup

def scrape(query):
    l=[]
    store={}

    URL = "https://news.google.com/search?q="+str(query)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    name = soup.find_all(class_="JtKRv")
    #image=soup.find_all(class_="K0q4G")
    #time=soup.find_all(class_="hvbAAd")
    link=soup.find_all(class_="WwrzSb")

    #print("Name:",name)
    #print(image)
    
    #print("Time:",time)
    #print(link)

    for i in range(0,len(name)):
        try:
            title=str(name[i]).split('target="_blank">')[1].split("</a>")[0]
            #print(title)
            #imagelink=str(image[i]).split('src="')[1].split('" src')[0]
            #upload=time[i].text
            articleLink=str(link[i]).split('href="')[1].split('" jslog')[0]
            store[i]={"title":title,"image":"#","uploadTime":"#","articlelink":articleLink}
        except:
            print("That's Enough!")
            break
    #print(store)
    return store

#scrape("bjp")
