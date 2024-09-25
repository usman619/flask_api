import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "Python API development","views": 1000000 ,"likes": 16000},
    {"name": "Flutter for Beginners","views": 20000 ,"likes": 10000},
    {"name": "JAVA for Game Development","views": 1000 ,"likes": 500}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json=data[i])
    print("PUT: ",response.json())

input()
response = requests.delete(BASE + "video/6")
print("DELETE...",response)

input()
response = requests.delete(BASE + "video/1")
print("DELETE...",response)

input()
response = requests.get(BASE + "video/2")
print("GET: ",response.json())


# response1 = requests.put(BASE + "video/1", json={"name": "python api development","views": 10000 ,"likes": 10})
# print("PUT: ",response1.json())
# response2 = requests.get(BASE + "video/6")
# print("GET: ",response2.json())