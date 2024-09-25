import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"name": "Python API development","views": 1000000 ,"likes": 16000},
#     {"name": "Flutter for Beginners","views": 20000 ,"likes": 10000},
#     {"name": "JAVA for Game Development","views": 1000 ,"likes": 500}
# ]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), json=data[i])
#     print("PUT: ",response.json())


# input()
response = requests.patch(BASE + "video/2", json={'likes': 600})
print("PATCH: ",response.json())
