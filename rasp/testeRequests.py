import requests
from getmac import get_mac_address as gma

#a = requests.get("https://gsense.azurewebsites.net/GSense-0.0.1-SNAPSHOT/device/test/1/1")
a = requests.post("http://10.1.9.1:38000/device/dashboard/2003/0")
print(gma())
print(a)


#idDevice: 1
#deviceNumber: 1
#Vazamento:

device = 1
host = "http://10.1.9.1:38000/device/dashboard"
print(host + f"/{device}")


