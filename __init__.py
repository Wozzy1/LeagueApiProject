"""from riotwatcher import LolWatcher, ApiError
import pandas as pd
import requests
import json
api_key = "RGAPI-f7cded24-ac04-42e8-9f38-a080213c91e2"

watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'Wz802')
my_matches = watcher.match.matchlist_by_puuid(my_region, me['puuid'], count=5)
last_match = my_matches[0]
match_detail = watcher.match.by_id(my_region, last_match)
"""