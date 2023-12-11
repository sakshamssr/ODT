import requests as req

response=req.get("https://www.bondsupermart.com/main/ws/v3/bond-info/bond-factsheet/AU3CB0237881")
data=response.json()
print(data)