from django.shortcuts import render
import requests as req

from .GNews_scrape import scrape
from .graph2 import graph_data

url = "https://gnewssapi.vercel.app/news/finance"
headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
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
    response=req.get("https://bonds-terminal.vercel.app/search2/"+str(para))
    data=response.json()
    print(data)
    context={
        "data":data,
        "list":data.keys(),
        "name":para
    }
    return render(request,"searchpage.html",context)

def details(request,para,para2,para3):
    from json import dumps
    response=req.get("https://bonds-terminal.vercel.app/search2/details/"+str(para2))
    data=response.json()
    print(data)
    gdata=graph_data()
    jdata=dumps(gdata)
    print(gdata)

    fetchgraphData=eval(data["graphdata"].split(";")[0].replace("vardetailChartViewmodel",""))
    print(fetchgraphData)

    print(type(fetchgraphData))

    context={
        "data":data,
        "name":para3,
        "date":gdata["date"],
        "close":gdata["close"],
        "graphdata":jdata
    }
    return render(request,"details.html",context)