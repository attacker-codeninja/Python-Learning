#!/usr/bin/python

# import essential modules
import requests
import json

# Note ->  requests module also have in-built json

api_url = "https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}"


# requests.get 
r = requests.get(api_url)
#print(r) # 200 i.e print status code

# if we want json result
#print(r.json())
json_response = r.json()

# Now pretty json response using json.dumps() function and store in json_data variable

json_data = json.loads(json.dumps(json_response,indent=4)) 
# If we use json.loads(json.dumps) => function then it can solve this problem -> TypeError: string indices must be integers json
#print(json_data)

# Grab specific data from json_data
# Like -> from items -> url, id, user , assignees 
# and from under user ->  [login,id,url]
# and from under assignees -> [login,id,url]

# Let's Start
#print("Url : {} ".format(json_data['items'][0]['url'])) # To print only 1 url

# If we want to grab all urls 
#for i in range(1,10):
#    print("Url : {} ".format(json_data['items'][i]['url']))


#print("Url : {} ".format(json_data['items'][0]['url']))
#print("ID : {} ".format(json_data['items'][0]['id']))
#print("User  Login: {} ".format(json_data['items'][0]['user']['login']))
#print("User  Login: {} ".format(json_data['items'][0]['user']['id']))
#print("User  url: {} ".format(json_data['items'][0]['user']['url']))
#print("Assignees  Login: {} ".format(json_data['items'][0]['assignees'][0]['login']))
#print("Assignees  ID: {} ".format(json_data['items'][0]['assignees'][0]['id']))
#print("Assignees  url: {} ".format(json_data['items'][0]['assignees'][0]['url']))


# To get all the details at once from json response =>

for i in range(1,10):
    print("Detail :", i)
    print("-" * 50)
    print("Url : {} ".format(json_data['items'][i]['url']))
    print("ID : {} ".format(json_data['items'][i]['id']))
    print("User  Login: {} ".format(json_data['items'][i]['user']['login']))
    print("User  Login: {} ".format(json_data['items'][i]['user']['id']))
    print("User  url: {} ".format(json_data['items'][i]['user']['url']))
    print("Assignees  Login: {} ".format(json_data['items'][0]['assignees'][0]['login']))
    print("Assignees  ID: {} ".format(json_data['items'][0]['assignees'][0]['id']))
    print("Assignees  url: {} ".format(json_data['items'][0]['assignees'][0]['url']))
    print("-" *  50)



