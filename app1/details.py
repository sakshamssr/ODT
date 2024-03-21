import requests
from bs4 import BeautifulSoup

def businessi(term):
    store={}

    URL="https://markets.businessinsider.com/bonds/"+term
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    page = requests.get(URL,headers=headers)
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

    return store