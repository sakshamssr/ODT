from django.shortcuts import render
import requests as req

from .GNews_scrape import scrape
from .graph2 import graph_data,topchart

# Create your views here.
def home(requests):
    data = scrape("query")
    top=topchart()

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

    dataJson={
        "news1":[{"title":data[0]["title"],"image":data[0]["image"],"link":"https://news.google.com/"+data[0]["articlelink"]},
                 {"title":data[1]["title"],"image":data[1]["image"],"link":"https://news.google.com/"+data[1]["articlelink"]},
                 {"title":data[2]["title"],"image":data[2]["image"],"link":"https://news.google.com/"+data[2]["articlelink"]},
                 {"title":data[3]["title"],"image":data[3]["image"],"link":"https://news.google.com/"+data[3]["articlelink"]},
                 {"title":data[4]["title"],"image":data[4]["image"],"link":"https://news.google.com/"+data[4]["articlelink"]},
                 {"title":data[5]["title"],"image":data[5]["image"],"link":"https://news.google.com/"+data[5]["articlelink"]},
                 {"title":data[6]["title"],"image":data[6]["image"],"link":"https://news.google.com/"+data[6]["articlelink"]},
                 {"title":data[7]["title"],"image":data[7]["image"],"link":"https://news.google.com/"+data[7]["articlelink"]},],
        "title":"Welcome",
        "topc":topcolor,
    }
    #print(dataJson["news1"])
    return render(requests,"home.html",dataJson)

def explore(request):
    return render(request,"explore_website.html")

def search(request,para):
    response=req.get("https://bonds-terminal.vercel.app/search2/"+str(para))
    data=response.json()
    #print(data)
    context={
        "data":data,
        "list":data.keys(),
        "name":para,
        "title":"Search",
    }
    return render(request,"searchpage.html",context)

def details(request,para,para2,para3,bondname):
    from json import dumps
    response=req.get("https://bonds-terminal.vercel.app/search2/details/"+str(para2))
    data=response.json()
    #print(data)

    fetchgraphData=eval(data["graphdata"].split(";")[0].replace("vardetailChartViewmodel",""))
    #print(fetchgraphData)

    gdata=graph_data(fetchgraphData["TKData"])
    jdata=dumps(gdata)
    #print(gdata)
    del data["graphdata"]

    newsdata = scrape(bondname+" bond")
    #print(type(fetchgraphData))

    context={
        "data":data,
        "name":para3.replace("%20"," "),
        "date":gdata["date"],
        "close":gdata["close"],
        "graphdata":jdata,
        "fetchgraph":fetchgraphData,
        "bondname":bondname,
        "news1":[{"title":newsdata[0]["title"],"image":newsdata[0]["image"],"link":"https://news.google.com/"+newsdata[0]["articlelink"]},
                 {"title":newsdata[1]["title"],"image":newsdata[1]["image"],"link":"https://news.google.com/"+newsdata[1]["articlelink"]},
                 {"title":newsdata[2]["title"],"image":newsdata[2]["image"],"link":"https://news.google.com/"+newsdata[2]["articlelink"]},
                 {"title":newsdata[3]["title"],"image":newsdata[3]["image"],"link":"https://news.google.com/"+newsdata[3]["articlelink"]},],
        "issue":data["Issue Price"],
        "title": bondname
    }
    return render(request,"details.html",context)

def about(request):
    context={
        "title":"About",
    }
    return render(request,"about.html",context)

def contact(request):
    context={
        "title":"Contact"
    }
    return render(request,"contact.html",context)