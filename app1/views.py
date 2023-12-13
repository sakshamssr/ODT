from django.shortcuts import render
import requests as req

from .GNews_scrape import scrape
from .graph2 import graph_data,topchart

# Create your views here.
def home(requests):
    data = scrape("live mint")
    top=topchart()

    topbonds=req.get("https://bonds-terminal.vercel.app/topbonds").json()
    print(topbonds)

    topcolor=[]

    for i in range(0,len(top)):
        topcolor.append(top[i]["Quotes"][0])

    for i in range(0,len(topcolor)):
        if(topcolor[i]["ChangePercent"]) > 0:
            topcolor[i]["color"]="green"
            topcolor[i]["name"]=top[i]["Name"].capitalize()
            topcolor[i]["transform"]=""
        else:
            topcolor[i]["color"]="red"
            topcolor[i]["name"]=top[i]["Name"].capitalize()
            topcolor[i]["transform"]=" rotate-180"
    
    #print(topcolor)
    news=[]

    for i in range(0,24):
        news.append({"title":data[i]["title"],"image":data[i]["image"],"link":"https://news.google.com/"+data[i]["articlelink"]})

    dataJson={
        "news1":news,
        "title":"Welcome",
        "topc":topcolor,
        "topbonds":topbonds,
    }
    #print(dataJson["news1"])
    return render(requests,"home.html",dataJson)

def explore(request):
    return render(request,"explore_website.html")

def search(request,para):
    response=req.get("https://bonds-terminal.vercel.app/search2/"+str(para))
    data=response.json()
    #print(data)

    datakeys=data.keys()

    for i in datakeys:
        data[i]["name"]=data[i]["name"].replace("/","%5E")

    context={
        "data":data,
        "list":data.keys(),
        "name":para,
        "title":"Search",
    }
    return render(request,"searchpage.html",context)

def details(request,para,link,para3,bondname):
    from json import dumps
    response=req.get("https://bonds-terminal.vercel.app/search2/details/"+str(link))
    data=response.json()
    #print(data)

    fetchgraphData=eval(data["graphdata"].split(";")[0].replace("vardetailChartViewmodel",""))
    #print(fetchgraphData)

    gdata=graph_data(fetchgraphData["TKData"])
    jdata=dumps(gdata)
    #print(gdata)
    del data["graphdata"]

    newsdata = scrape(str(bondname).replace("%20"," ")+" bond")
    #print(type(fetchgraphData))

    print(para3)
    news=[]

    for i in range(0,5):
        try:
            news.append({"title":newsdata[i]["title"],"image":newsdata[i]["image"],"link":"https://news.google.com/"+newsdata[i]["articlelink"]})
        except:
            break

    context={
        "data":data,
        "name":para3.replace("%20"," ").replace("^","/"),
        "date":gdata["date"],
        "close":gdata["close"],
        "graphdata":jdata,
        "fetchgraph":fetchgraphData,
        "bondname":bondname.replace("%20"," "),
        "news1":news,
        "issue":data["Issue Price"],
        "title": bondname.replace("%20"," ")
    }
    return render(request,"details.html",context)

def about(request):
    context={
        "title":"About Us",
    }
    return render(request,"about.html",context)

def contact(request):
    context={
        "title":"Contact Us"
    }
    return render(request,"contact.html",context)

def learn(request):
    context={
        "title":"Learn About Finance - Bonds"
    }
    return render(request,"learn.html",context)