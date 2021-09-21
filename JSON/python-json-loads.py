#!/usr/bin/python

# This script is to work with JSON using Python

# Step 1 - import the module - import json
import json 

# Step 2 - make  a json_string variable 
'''json_string = """
{
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
}"""
'''

json_string = r"""{
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
}"""

# We putted JSON Strings in Triple Double Quotes

# Now check if it working or not by printing it - Good for testing purpose in starting while working code
# Once confirmed we can do things what we want from thie given string
#print(json_string)

# Step 3 - Convert JSON String to Dictionary
#json_dict = json.loads(json_string)
#print(json_dict)

# Above result give an error => json.decoder.JSONDecodeError: Expecting ',' delimiter: line 90 column 16 (char 2026)
# Solution => in json_string -> there is Triple Double Quotes -> we need to put r there like => r""" <json-string-here> """

json_dict = json.loads(json_string)
print(json_dict)
# Now above code will work fine
''' Above code will give output => 
{'variables': [], 'info': {'name': 'Sample Postman Collection', '_postman_id': '35567af6-6b92-26c2-561a-21fe8aeeb1ea', 'description': 'A sample collection to demonstrate collections as a set of related requests', 'schema': 'https://schema.getpostman.com/json/collection/v2.0.0/collection.json'}, 'item': [{'name': 'A simple GET request', 'event': [{'listen': 'test', 'script': {'type': 'text/javascript', 'exec': ["pm.test('expect response be 200', function () {", '    pm.response.to.be.ok', '})', "pm.test('expect response json contain args', function () {", "    pm.expect(pm.response.json().args).to.have.property('source')", "      .and.equal('newman-sample-github-collection')", '})']}}], 'request': {'url': {'raw': 'https://postman-echo.com/get?source=newman-sample-github-collection', 'protocol': 'https', 'host': ['postman-echo', 'com'], 'path': ['get'], 'query': [{'key': 'source', 'value': 'newman-sample-github-collection', 'equals': True, 'description': ''}], 'variable': []}, 'method': 'GET', 'header': [], 'body': {}, 'description': ''}, 'response': []}, {'name': 'A simple POST request', 'request': {'url': 'https://postman-echo.com/post', 'method': 'POST', 'header': [{'key': 'Content-Type', 'value': 'text/plain'}], 'body': {'mode': 'raw', 'raw': 'Duis posuere augue vel cursus pharetra. In luctus a ex nec pretium...'}, 'description': ''}, 'response': []}, {'name': 'A simple POST request with JSON body', 'request': {'url': 'https://postman-echo.com/post', 'method': 'POST', 'header': [{'key': 'Content-Type', 'value': 'application/json'}], 'body': {'mode': 'raw', 'raw': '{"text":"Duis posuere augue vel cursus pharetra. In luctus a ex nec pretium..."}'}, 'description': ''}, 'response': []}]}'''

# loads() => Function to load string + Convert JSON to Ditionary





