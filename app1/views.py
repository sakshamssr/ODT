from django.shortcuts import render
import requests as req

from .GNews_scrape import scrape

url = "https://gnewssapi.vercel.app/news/finance"
#print(data)

# Create your views here.
def home(requests):
    response = scrape()
    data = scrape()
    dataJson={
        "news1":[{"title":data[0]["title"],"image":data[0]["image"],"link":"https://news.google.com/"+data[0]["articlelink"]},
                 {"title":data[1]["title"],"image":data[1]["image"],"link":"https://news.google.com/"+data[1]["articlelink"]},
                 {"title":data[2]["title"],"image":data[2]["image"],"link":"https://news.google.com/"+data[2]["articlelink"]},
                 {"title":data[3]["title"],"image":data[3]["image"],"link":"https://news.google.com/"+data[3]["articlelink"]},
                 {"title":data[4]["title"],"image":data[4]["image"],"link":"https://news.google.com/"+data[4]["articlelink"]},
                 {"title":data[5]["title"],"image":data[5]["image"],"link":"https://news.google.com/"+data[5]["articlelink"]},
                 {"title":data[6]["title"],"image":data[6]["image"],"link":"https://news.google.com/"+data[6]["articlelink"]},
                 {"title":data[7]["title"],"image":data[7]["image"],"link":"https://news.google.com/"+data[7]["articlelink"]},]
    }
    #print(dataJson["news1"])
    return render(requests,"home.html",dataJson)

def explore(request):
    return render(request,"explore_website.html")

def search(request,para):
    response=req.get("https://bond-terminal.vercel.app/search2/"+str(para))
    data=response.json()
    print(data)
    context={
        "data":data,
        "list":data.keys(),
        "name":para
    }
    return render(request,"searchpage.html",context)

def details(request,para):
    response=req.get("https://www.bondsupermart.com/main/ws/v3/bond-info/bond-factsheet/"+str(para))
    data=response.json()
    print(data)
    return render(request,"details.html")