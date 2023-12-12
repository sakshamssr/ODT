import requests
#import plotly.express as px

from .mdate import getdate,todaydate

def graph_data(tkdata):
    response=requests.get("https://markets.businessinsider.com/Ajax/Chart_GetChartData?instrumentType=Bond&tkData="+str(tkdata)+"&from=19700201&to="+str(todaydate()))
    data=response.json()

    #print(data)

    close_data=[]
    date_data=[]

    for i in range(0,len(data)):
        close_data.append(data[i]["Close"])
        date_data.append(data[i]["Date"].split(" ")[0])

    final_data={"close":close_data,"date":date_data}

    return final_data

    '''
    fig = px.line(x=date_data, y=close_data, title='Graph')
    #fig.add_scatter(x=bidx,y=bidy)
    fig.update_xaxes(
        title_text='Date',
        tickformat='%b %d, %Y',
        dtick=3 * 24 * 60 * 60 * 1000,  # Set the tick interval to one month
    )


    fig.show()'''

def topchart():
    store={}

    URL="https://markets.businessinsider.com/ajax/finanzen/api/commodities?urls=gold-price,oil-price"
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    page = requests.get(URL,headers=headers)
    data = page.json()

    return data