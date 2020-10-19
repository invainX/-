import requests
import json
import os,base64
#发送答案
data1={"teamid": 8,
        "token": "ae050dca-06fb-4425-b6ff-3c3f2b20b7f6"
    }
header ={}


response = requests.post('http://47.102.118.1:8089/api/challenge/start/c7189d4c-791a-411c-8d6e-21dc29c6e7eb',headers = header, json=data1 )
dict1 = response.json()
str0 = dict1["uuid"]

data2={
    "uuid": str0,
    "teamid": 8,
    "token": "ae050dca-06fb-4425-b6ff-3c3f2b20b7f6",
    "answer": {
        "operations": "wassdwdsawawdsdwasdsawasddwa",
        "swap": []
    }
}

response1 = requests.post('http://47.102.118.1:8089/api/challenge/submit',headers = header, json=data2 )
dict1 = response1.json()
str1 = dict1["rank"]
print(str1)
