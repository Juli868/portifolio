import requests

url = "https://siddiq-such-flight-v1.p.rapidapi.com/search"

querystring = {"to":"LHE","from":"DXB","depart-date":"2015-03-31","return-date":"2015-04-07"}

headers = {
	"X-RapidAPI-Key": "0236cb0a95msh26bb8f324e6b244p12209cjsnc5590b373b84",
	"X-RapidAPI-Host": "siddiq-such-flight-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
