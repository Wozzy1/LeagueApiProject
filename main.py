from riotWatcher import LolWatcher, ApiError
import pandas as pd
import requests
import json
api_key = "RGAPI-9b962e27-e9bc-4bfb-a8c9-4fea51739ffe"


class GameDataGenerator():

    def __init__(self, Watcher, ) -> None:
        self.Watcher = LolWatcher(api_key)


    def getPlayerInfo(self):
        
        # player information hardcoded for now; there is room to make this a user input
        region = 'na1'
        player_name = 'Wozzy'
        # player_name = 'Oreo Frost'
        
        # returns a player object to be used in querying matches
        player = self.Watcher.summoner.by_name(region, player_name)
        player_matches = self.Watcher.match.matchlist_by_puuid(region, player['puuid'], count=20, queue=420)
        return player_matches

    def getMatchDetail(player_matches, Watcher):
        last_match = player_matches[0]
        Watcher.match.by_id(region, last_match)
        return 