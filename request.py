import requests
import json
import os,base64
#获取题目
data1={"teamid": 8,
        "token": "ae050dca-06fb-4425-b6ff-3c3f2b20b7f6"
    }
header ={}


response = requests.post('http://47.102.118.1:8089//api/challenge/start/e9d5727c-57fa-4182-a1fd-24b43fd392ce',headers = header, json=data1 )
dict1 = response.json()
str0 = dict1["data"]
str2= dict1['uuid']
str1 = str0['img']
str3 = str0['step']
str4 = str0['swap']
print(str2)
print(str3)
print(str4)

imgdata = base64.b64decode(str1)

file=open(r'C:\Users\12604\.ipynb_checkpoints\cz30.png','wb')

file.write(imgdata)

file.close()
