import pandas as pd
import json

with open("cavani_2016_stats.json", "r") as file:
    data = json.load(file)

statistics = data["response"][0]["statistics"]

df = pd.json_normalize(statistics,
                       meta=[["team", "id"], ["team", "name"], ["team", "logo"], 
                             ["league", "id"], ["league", "name"], ["league", "country"], ["league", "logo"], ["league", "flag"], ["league", "season"],
                             ["games", "appearences"], ["games", "lineups"], ["games", "minutes"], ["games", "number"], ["games", "position"], ["games", "rating"], ["games", "captain"],
                             ["substitutes", "in"], ["substitutes", "out"], ["substitutes", "bench"],
                             ["shots", "total"], ["shots", "on"],
                             ["goals", "total"], ["goals", "conceded"], ["goals", "assists"], ["goals", "saves"],
                             ["passes", "total"], ["passes", "key"], ["passes", "accuracy"],
                             ["tackles", "total"], ["tackles", "blocks"], ["tackles", "interceptions"],
                             ["duels", "total"], ["duels", "won"],
                             ["dribbles", "attempts"], ["dribbles", "success"], ["dribbles", "past"],
                             ["fouls", "drawn"], ["fouls", "committed"],
                             ["cards", "yellow"], ["cards", "yellowred"], ["cards", "red"],
                             ["penalty", "won"], ["penalty", "committed"], ["penalty", "scored"], ["penalty", "missed"], ["penalty", "saved"]])

df.columns = ["team_id", "team_name", "team_logo",
              "league_id", "league_name", "league_country", "league_logo", "league_flag", "league_season",
              "games_appearances", "games_lineups", "games_minutes", "games_number", "games_position", "games_rating", "games_captain",
              "substitutes_in", "substitutes_out", "substitutes_bench",
              "shots_total", "shots_on",
              "goals_total", "goals_conceded", "goals_assists", "goals_saves",
              "passes_total", "passes_key", "passes_accuracy",
              "tackles_total", "tackles_blocks", "tackles_interceptions",
              "duels_total", "duels_won",
              "dribbles_attempts", "dribbles_success", "dribbles_past",
              "fouls_drawn", "fouls_committed",
              "cards_yellow", "cards_yellowred", "cards_red",
              "penalty_won", "penalty_committed", "penalty_scored", "penalty_missed", "penalty_saved"]              

df.to_csv("cavani_2016_stats.csv", sep=",", index=False, encoding="utf-8")