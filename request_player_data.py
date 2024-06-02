import json
import requests

# Edinson Cavani, ID: 274, Team: 85 (PSG), League: 61 (Ligue 1), Seasons 2014-15, 2015-16, 2016-17.

url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {
    "id"    : "274",
    "season": "2014",
    "team"  : "85",
    "league": "61"
}

headers = {
	"X-RapidAPI-Key" : "4d8d14fda7msh01627ef5ab0f03fp14055bjsn2d65330d45b3",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Send response to .json file.
with open("cavani_2014_stats.json", "w") as file:
    json.dump(response.json(), file, indent=4)