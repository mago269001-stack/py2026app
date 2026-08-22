# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# f344ba94b0d9af9da3b2710ba554e05e

import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q=taipei,TW&appid=f344ba94b0d9af9da3b2710ba554e05e&units=metric&lang=zh_TW'
response = requests.get(url)
#APP >文件>API >COPY網址 >修改網址 :q=地區appide=貼上API KEY &units修改溫度單位為緯度 =metric緯度&lang
# 'https://api.openweathermap.org/data/2.5/weather?q=taipei,TW（地區）&appid=（API KEY）f344ba94b0d9af9da3b2710ba554e05e&units(單位)=metric(緯度)&lang(語言)=zh_TW'
print(response.json())