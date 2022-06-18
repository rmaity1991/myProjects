from urllib.request import urlopen
import json

from pprint import pprint


# Section 1 - Simple HTTP request to get body

response=urlopen("https://www.example.com")

body=response.read() # returns a byte stream from the response string

#print(body)

# Section 2 - Converting JSON data if returned to a python dict

url = "https://jsonplaceholder.typicode.com/todos/1"

response=urlopen(url)

body=response.read()

json_dict=json.loads(body) # returns a dict from json data

#print(json_dict)


# Section 3 - Methods of HTTP Objects returned from responses

response=urlopen("https://www.example.com")

#pprint(dir(response))

#print(response.headers)
#print(response.headers.items())


#print(response.headers['Server'])
#print(response.getheader("Server"))


#print(response.read(50))

body=response.read()

decoded_data=body.decode('utf-8')
print(decoded_data)

html_file=open("example.html",mode='wb')
html_file.write(body)
response.close()





