import requests
import json

# # URL='http://127.0.0.1:8000/api/allStudents/'
# # # x = requests.get('http://127.0.0.1:8000/api/allStudents/')
# # x = requests.get(url=URL)
# # print((x.json()))
# # # print(type(x.json))

# # post method

# URL="http://127.0.0.1:8000/api/studentApi/"

# # data = {
# #   'name':'Sonam Kapoor',
# #   'roll':107,
# #   'city':'Mumbai'
# # }

# # # converting this python dictionary into json data and passing with post method
# # json_data = json.dumps(data)
# # r = requests.post(url=URL, data=json_data)
# # print(r)
# # dataj = r.json()
# # print(dataj)

URL="http://127.0.0.1:8000/api/studentApi/"

def get_data(id=None):
  data= {}
  if id is not None:
    data = {"id":id}
    headers= {'content-Type':'application/json'}
    r  = requests.get(url=URL, headers=headers ,data=json.dumps(data))
    print(r.json())
  else:
    r  = requests.get(url=URL)
    print(r.json())

# get_data()
# get_data(35)

# postUrl = "http://127.0.0.1:8000/api/createStudent/"


# def post_data():
#   data={
#     "name":"jkjhiraj Yadav",
#     "roll":300,
#     "city":"Gothula"
#   }
#   res = requests.post(url=postUrl, data=json.dumps(data))
#   print(res.json())

# post_data()


UpdateURL="http://127.0.0.1:8000/api/studentApi/"

def update(id=None,name=None,city=None):
  if id is not None:
    data={
      "id":id,
      "name":name,
      "city":city
    }
    headers = {'content-Type':'application/json'}
    res = requests.put(url=UpdateURL, headers=headers ,data=json.dumps(data))
    print(res.json())

def updatePatch(id=None,name=None,city=None):
  if id is not None:
    data={
      "id":id,
      "name":name,
      "city":city
    }
    headers = {'content-Type':'application/json'}
    res = requests.patch(url=UpdateURL, headers=headers ,data=json.dumps(data))
    print(res.json())

# update(id=35,name="Minakshi Yadav",city="Dumrao")
# updatePatch(id=35,name="Minakshi Yadav",city="Dumrao")

deleteURL="http://127.0.0.1:8000/api/studentApi/"

def delete_data(id=None):
  if id is not None:
    data={"id":id}
    headers = {'content-Type':'application/json'}
    res = requests.delete(url=deleteURL, headers=headers ,data=json.dumps(data))
    print(res.json())

# delete_data(35)


postUrl = "http://127.0.0.1:8000/api/studentApi/"


def post_data():
  data={
    "name":"jkjhiraj Yadav",
    "roll":332,
    "city":"Gothula"
  }

  headers = {'content-Type':'application/json'}

  res = requests.post(url=postUrl,headers=headers ,data=json.dumps(data))
  print(res.json())

# post_data()