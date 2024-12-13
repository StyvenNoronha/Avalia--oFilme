import urllib.request
import json

def list_movies(typeMovie):
    if typeMovie == 'popular':
        url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=694dada69a356f14cb9823adab59a7cd&language=pt-BR'
    elif typeMovie == 'animacao':
        url = 'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&with_genres=16&api_key=694dada69a356f14cb9823adab59a7cd&language=pt-BR'
    elif typeMovie == '2024':
        url = 'https://api.themoviedb.org/3/discover/movie?primary_release_year=2022&sort_by=vote_average.desc&api_key=694dada69a356f14cb9823adab59a7cd&language=pt-BR'        


    response = urllib.request.urlopen(url)

    data = response.read()
    data_json = json.loads(data)

    return data_json['results']
#print(data_json['results'])