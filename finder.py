import requests
import json

url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {"league":"140","season":"2017"}

headers = {
	"X-RapidAPI-Key": "4d8d14fda7msh01627ef5ab0f03fp14055bjsn2d65330d45b3",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

with open("player_team_finder.json", "w") as file:
    json.dump(response.json(), file, indent=4)