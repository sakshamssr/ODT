from django.shortcuts import render
import requests as req
from .GNews_scrape import scrape
from .graph2 import graph_data,topchart
from .details import businessi

# Create your views here.
def home(requests):
    data = scrape("live mint")
    top=topchart()

    topbonds=req.get("https://finance-api-ssr.vercel.app/topbonds").json()
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
        news.append({"title":data[i]["title"],"image":"https://news.google.com"+data[i]["image"],"link":"https://news.google.com/"+data[i]["articlelink"]})

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
    response=req.get("https://finance-api-ssr.vercel.app/search2/"+str(para))
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
    from bs4 import BeautifulSoup
    store={}

    URL="https://markets.businessinsider.com/bonds/"+link
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    page = req.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    table=soup.find_all(class_="table__tr")
    scripts=soup.find_all("script")

    st=[]
    rating=soup.find(class_="moodys-rating__rating")


    for i in range(0,len(scripts)):
        st.append(str(scripts[i]))
        
    tabledata=[]

    for i in table:
        if('class="table__td">' in str(i)):
            tabledata.append(str(i))

    for i in range(0,len(tabledata)-5):
        base=str(tabledata[i]).replace("\t","").replace("\n",'')
        name=base.split('class="table__td">')[1].split('</td>')[0]
        data=base.split('class="table__td">')[1].split('</td>')[1].split('<td class="table__td text-right">')[1]

        store[name]=data

    Issue=str(store["Issuer"]).split('">')[1].split("</a>")[0]
    store["Issuer"]=Issue
    
    try:
        rating=rating.text
        store["rating"]=100-int(rating)
        if (int(rating)<33):
            store["color"]="green"
        elif(int(rating)>33 and int(rating)<66):
            store["color"]="orange"
        else:
            store["color"]="red"
    except:
        store["rating"]="-"
    store["graphdata"]=st[23].replace("<script>","").replace("</script>","").replace("=","").replace(" ","").replace("null","None").replace("false","False").replace("true","True").replace("\n","").replace("\t","").replace('/','')

    store["graphdata"]=store["graphdata"].split(";")[0].replace("vardetailChartViewmodel","")
    from json import dumps
    # response=req.get("https://finance-api-ssr.vercel.app/search2/details/"+str(link))
    data=store
    # print(data)

    fetchgraphData=eval(data["graphdata"])
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

def submitcontact(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        body = request.POST.get('message')
        to_email = 'sakshamraghav57@gmail.com'

        tosend="From: "+email + " Message:"+body

        send=req.get("https://finance-api-ssr.vercel.app/contact/"+subject+"/"+to_email+"/"+tosend)

        return render(request, "contact.html", {'success': True,"title":"Thanks For Contacting Us!"})
