#!/usr/bin/python

# json.dumps() => Dumps json data into a string.

# import json module
import json

#json_file = "postman-collection-file.json"


#with open(json_file,'r') as file:
#    data = json.load(file)
#    dump = json.dumps(data,indent=4)
#    print(dump)

# In short => when u want to work with strings -> use loads() and when u want to work with file -> use load()
# both load() and loads() -> Serialization i.e -> conversion of JSON to Python Object

# and for the case of dump() and dumps() -> DeSerialization i.e. -> conversion of Python Object to JSON
# dump() -> when want to write json into file
# dumps() -> when want to work with strings to convert Python Object to JSON


# Example 2 for dumps()

json_str = r'''{
    "variables": [],
    "info": {
        "name": "Sample Postman Collection",
        "_postman_id": "35567af6-6b92-26c2-561a-21fe8aeeb1ea",
        "description": "A sample collection to demonstrate collections as a set of related requests",
        "schema": "https://schema.getpostman.com/json/collection/v2.0.0/collection.json"
    },
    "item": [
        {
            "name": "A simple GET request",
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "type": "text/javascript",
                        "exec": [
                            "pm.test('expect response be 200', function () {",
                            "    pm.response.to.be.ok",
                            "})",
                            "pm.test('expect response json contain args', function () {",
                            "    pm.expect(pm.response.json().args).to.have.property('source')",
                            "      .and.equal('newman-sample-github-collection')",
                            "})"
                        ]
                    }
                }
            ],
            "request": {
                "url": {
                    "raw": "https://postman-echo.com/get?source=newman-sample-github-collection",
                    "protocol": "https",
                    "host": [
                        "postman-echo",
                        "com"
                    ],
                    "path": [
                        "get"
                    ],
                    "query": [
                        {
                            "key": "source",
                            "value": "newman-sample-github-collection",
                            "equals": true,
                            "description": ""
                        }
                    ],
                    "variable": []
                },
                "method": "GET",
                "header": [],
                "body": {},
                "description": ""
            },
            "response": []
        },
        {
            "name": "A simple POST request",
            "request": {
                "url": "https://postman-echo.com/post",
                "method": "POST",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "text/plain"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": "Duis posuere augue vel cursus pharetra. In luctus a ex nec pretium..."
                },
                "description": ""
            },
            "response": []
        },
        {
            "name": "A simple POST request with JSON body",
            "request": {
                "url": "https://postman-echo.com/post",
                "method": "POST",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": "{\"text\":\"Duis posuere augue vel cursus pharetra. In luctus a ex nec pretium...\"}"
                },
                "description": ""
            },
            "response": []
        }
    ]
}'''


json_dict = json.loads(json_str)

json_dump = json.dumps(json_dict,indent=4)

print(json_dump)

### why I  used r'''<json string> ''' ?
# Because in json string there is word true which will not work with python while conversion
# in python true is True - so above json string not work
# But , if we use with r''' json string''' => then it will work