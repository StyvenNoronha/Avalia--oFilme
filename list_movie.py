import urllib.request
import json

url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=694dada69a356f14cb9823adab59a7cd'

response = urllib.request.urlopen(url)

data = response.read()
data_json = json.loads(data)
#print(data_json['results'])