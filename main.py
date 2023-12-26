from riotwatcher import LolWatcher, ApiError
import pandas as pd
import requests
import json
api_key = "RGAPI-9b962e27-e9bc-4bfb-a8c9-4fea51739ffe"


class GameDataGenerator():

    def __init__(self, _api_key, name) -> None:
        self.Watcher = LolWatcher(_api_key)
        self.Player = PlayerInfo("na1", name)


    def getPlayerMatches(self) -> list:        
        # returns a player object to be used in querying matches
        player = self.Watcher.summoner.by_name(self.Player.region, self.Player.name)
        matches = self.Watcher.match.matchlist_by_puuid(self.Player.region, player['puuid'], count=20, queue=420)
        return matches

    def getLastMatchDetail(self, matches) -> dict:
        last_match = matches[0]
        match_detail = self.Watcher.match.by_id(self.Player.region, last_match)
        return match_detail
    
    def getPlayerOneGameStats(self, matchNumber) -> str:
        matches = self.getPlayerMatches()
        try:
            match_detail = self.Watcher.match.by_id(self.Player.region, matches[matchNumber])
        except IndexError as ie:
            print(f"Index {matchNumber} is greater than {len(matches)-1}, therefore is out of bounds.")
            return None
        except Exception as e:
            print(f"Unexpected error {e} from input {matchNumber}")
            return None

        playernum = 0
        participants = []
        while playernum < 10:
            for item in match_detail['info']['participants']:
                part_row = {}
                part_row['champion'] = match_detail['info']['participants'][playernum]['championName']
                part_row['goldEarned'] = match_detail['info']['participants'][playernum]['goldEarned']
                part_row['kills'] = match_detail['info']['participants'][playernum]['kills']
                part_row['deaths'] = match_detail['info']['participants'][playernum]['deaths']
                part_row['assists'] = match_detail['info']['participants'][playernum]['assists']
                #print(match_detail['info']['participants'][playernum]['championId'])
                participants.append(part_row)
                playernum +=1
        #print(match_detail['info']['participants'][0])
        df = pd.DataFrame(participants)

        return(print(df))
    
    def getPlayerMultipleGameStats(self, matches) -> str:
        games_info = []
        for game_num in range(len(matches)):
            last_match = matches[game_num]
            match_detail = self.Watcher.match.by_id(self.Player.region, last_match) # doesnt need error catching becasue is done in a controlled for loop
            for part_num in range(len(match_detail['info']['participants'])):
                #print(match_detail['info']['participants'][part_num]['summonerName'])
                if match_detail['info']['participants'][part_num]['summonerName'] == self.Player.name:
                    
                    #playernum = match_detail['info']['participants']['summonerName'].index('WZ802')
                    part_row = {}
                    part_row['Win'] = match_detail['info']['participants'][part_num]['win']
                    part_row['championPlayed'] = match_detail['info']['participants'][part_num]['championName']
                    part_row['gameLength (sec)'] = match_detail['info']['participants'][part_num]['timePlayed']
                    part_row['kills'] = match_detail['info']['participants'][part_num]['kills']
                    part_row['deaths'] = match_detail['info']['participants'][part_num]['deaths']
                    part_row['assists'] = match_detail['info']['participants'][part_num]['assists']
                    part_row['goldEarned'] = match_detail['info']['participants'][part_num]['goldEarned']
                    part_row['CS'] = match_detail['info']['participants'][part_num]['totalMinionsKilled']
                    part_row['dmgToChamps'] = match_detail['info']['participants'][part_num]['totalDamageDealtToChampions']
                    games_info.append(part_row)
        df = pd.DataFrame(games_info)
        return(print(df))


    
class PlayerInfo():
    def __init__(self, region, name) -> None:
        # values are hardcoded for now
        self.region = region
        self.name = name

    