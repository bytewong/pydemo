#! /usr/bin/python

import requests
import json

def get():
    package = requests.get(url = "http://dl.baidu.com/v1.cab")
    cab = open("py_cab", 'w')
    cab.write(package.content)
    cab.close()

def post():
    url = 'https://download.baidu.com/api/checklibupdate'
    body = {"os":"win7",
            "source": "client",
            "ccid": "123456"}

    response = requests.post(url, data = json.dumps(body))
    print response.text
    print response.status_code

def main():
    get()
    post()

if __name__ == "__main__":
    main()
