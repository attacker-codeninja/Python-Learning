#!/usr/bin/python

# json.dump() => convert the given python object into an equivalent JSON object and then stores the result in a text file
# We use json.dump() when we want to dump JSON into a file
# json.dumps(dump string) is used when we need the JSON data as a string for parsing or printing

# import json module
import json


input_json_filename = "postman-collection-file.json"
output_json_filename = "new_json_file.json"

with open(input_json_filename) as input_json_file:
    converted_json_to_dict = json.load(input_json_file)

with open(output_json_filename, 'w') as output_json_file:
    json.dump(converted_json_to_dict, output_json_file)

'''
so , dump() -> use to write json to new file right ?
in code -> we use with command 2 times

1st for load the old json file 
2nd for dump old json file to new json file in JSON

and json.dumps() to write json data to an str variable.

the output of 2nd new file will be not in pretty format , so to make json pretty ->

json.dump(converted_json_to_dict,output_json_file,indent=4s)
'''