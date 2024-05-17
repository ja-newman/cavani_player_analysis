import json
import requests

url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {
    "id"    : "274",
    "season": "2016",
    "team"  : "85"
}

headers = {
	"X-RapidAPI-Key" : "4d8d14fda7msh01627ef5ab0f03fp14055bjsn2d65330d45b3",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Send response to .json file.
with open("cavani_2016_stats.json", "w") as file:
    json.dump(response.json(), file, indent=4)