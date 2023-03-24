api_key = "RGAPI-a7e5bc3b-0a00-4ab7-987d-99b8604e5122"

#/lol/summoner/v4/summoners/by-account/{encryptedAccountId}


api_url = "https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
user= "beast10000"
import requests 
import json
api_url = api_url+user+"/"+"?api_key="+api_key
respuesta= requests.get(api_url)
player_info = respuesta.json()
player_name =player_info["name"]
player_lvl= player_info["summonerLevel"]
my_list= list([player_name,player_lvl])
player_puid= player_info["puuid"]
print (my_list)
print(player_puid)


api_matchs= "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"+player_puid+"/ids?start=0&count=20&api_key="+api_key
print(api_matchs)
#api_macths= "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/jeY5_-kEIMcRVn58AJJWQxVUH6IyX5Ju8ZbgoXmx1ujAwZuWJmUOoDLIyYChUyJLRwZQbBVtKXTZuA/ids?start=0&count=20&api_key="+api_key

respuesta_matchs = requests.get(api_matchs)

juegos_ids= respuesta_matchs.json()
print (my_list)
print(juegos_ids)
last_game= juegos_ids[0]


api_lastmatch = "https://americas.api.riotgames.com/lol/match/v5/matches/"+last_game+"?api_key="+api_key

request_lastmach= requests.get(api_lastmatch)

lastmachjs= request_lastmach.json()

metadata= lastmachjs["metadata" ["participants"]]

print(metadata)
#participantes= lastmachjs['participants']

#dic_partida = json.loads(last_game)




