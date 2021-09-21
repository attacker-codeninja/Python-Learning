#!/usr/bin/python

# This script is to work with JSON using Python

# Step 1 - import the module - import json
import json 



# load() => To parse JSON from URL or file, use json.load()

# Step 2 - Load File [postman-collection-file.json] using load() Function


json_file = "postman-collection-file.json"

print("Start Reading JSON File: ")
#with open(json_file,'r') as file:
#    json_read = json.load(file)
#    print(json_read)


# Still we are getting result in Dictionary => Because json.load => convert JSON to Dictionary in Python

# Now If we want to play with =>

#with open(json_file,'r') as file:
#    json_read = json.load(file)
#    for key,value in json_read.items():
#        print("Key : {} , Value: {}".format(key,value))

# More play =>

with open(json_file,'r') as file:
    json_read = json.load(file)
    # print(json_read['info']) # Will give  all the items in info item
    #print(json_read['info']['name']) # This item have name and this name => "name": "Sample Postman Collection"
    #print(json_read['item']) # Will give all the items in item => Now this item have data in Array
    #print(json_read['item'][1]) # 1st Element of item data
    #print(json_read['item'][1]['name']) # print the result of name of the 1st Element in item data
    #print(json_read['item'][1]['request']) # print the result of request of the 1st Element in item data
    #print(json_read['item'][1]['request']['url']) # print the url in  result of name of the 1st Element in item data

# Simple thing is when working with json to print specific data always keep in mind about Array and Lists

# Examples =>

# 1 :  {info :{data1 , data2, data3}} => 

# print(file['info]) => all data1,data2,data3
# print(file['info']['data1'])  => just result of data1

# 2: {info : {data1: [{value1: 'result1'}, {value2: 'result2' }], data2: [{value1: 'result1'}, {value2: 'result2' }] , data3: [{value1: 'result1'}, {value2: 'result2' }] } } 
# We need to play with that => [0,1,2] => always remember in []  first element is 0 
# So => {a: [0: {b}]}
# print(a[0]['b'])






