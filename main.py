from riotwatcher import LolWatcher, ApiError
import pandas as pd
import requests
import json
api_key = "RGAPI-08576416-f07a-44ac-8e9c-777919706474"


class GameDataGenerator():

    def __init__(self, _api_key, name) -> None:
        if name is None:
            self.Watcher = LolWatcher(_api_key)
        elif name is not None:
            self.Watcher = LolWatcher(_api_key)
            self.Player = PlayerInfo("na1", name)
        else:
            print("An error occurred with the constructor for GameDataGenerator")

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
                participant_row = {}
                participant_row['champion'] = match_detail['info']['participants'][playernum]['championName']
                participant_row['goldEarned'] = match_detail['info']['participants'][playernum]['goldEarned']
                participant_row['kills'] = match_detail['info']['participants'][playernum]['kills']
                participant_row['deaths'] = match_detail['info']['participants'][playernum]['deaths']
                participant_row['assists'] = match_detail['info']['participants'][playernum]['assists']
                #print(match_detail['info']['participants'][playernum]['championId'])
                participants.append(participant_row)
                playernum +=1
        #print(match_detail['info']['participants'][0])
        df = pd.DataFrame(participants)

        return(print(df))
    
    def getMultipleGameStatsByPlayer(self, matches) -> pd.DataFrame:
        games_info = []
        for game_num in range(len(matches)):
            last_match = matches[game_num]
            match_detail = self.Watcher.match.by_id(self.Player.region, last_match) # doesnt need error catching becasue is done in a controlled for loop
            
            # simplify to for in range 10?
            for participant_num in range(len(match_detail['info']['participants'])):
                #print(match_detail['info']['participants'][participant_num]['summonerName'])
                if match_detail['info']['participants'][participant_num]['summonerName'] == self.Player.name:
                    participant_row = {}
                    participant_row['Win'] = match_detail['info']['participants'][participant_num]['win']
                    participant_row['championPlayed'] = match_detail['info']['participants'][participant_num]['championName']
                    # participant_row['championId'] = match_detail['info']['participants'][participant_num]['championId']
                    participant_row['gameLength (sec)'] = match_detail['info']['participants'][participant_num]['timePlayed']
                    participant_row['kills'] = match_detail['info']['participants'][participant_num]['kills']
                    participant_row['deaths'] = match_detail['info']['participants'][participant_num]['deaths']
                    participant_row['assists'] = match_detail['info']['participants'][participant_num]['assists']
                    participant_row['goldEarned'] = match_detail['info']['participants'][participant_num]['goldEarned']
                    # participant_row['CS'] = match_detail['info']['participants'][participant_num]['totalMinionsKilled'] # FIX THE COMPUTATION OF TOTAL CS
                    participant_row['dmgToChamps'] = match_detail['info']['participants'][participant_num]['totalDamageDealtToChampions']
                    games_info.append(participant_row)
        df = pd.DataFrame(games_info)
        # return(print(df))
        return df

    """
    For this method, I want to get data in a different fashion. I want to look at the game in a broader sense rather 
    than focusing on one player. Some conditions that are strongly associated with winning are:
    - avg champion levels (float)
    - total exp (int)
    - minions killed (int)
    - jungle monsters killed (int)
    - avg gold difference (float)
    - lane gold difference
        - top vs top
        - jg vs jg
        - mid vs mid
        - bot vs bot
        - sup vs sup
    - dragons killed (int)
        - elder dragon (int)
    - rift heralds taken (int)
    - barons (int)
    - towers destroyed (int)
    - blue team win (boolean)
    - team total KDA
        - Kills
        - Deaths
        - Assists
    - vision score
    - pink wards
    - wards placed
    - wards killed
    """
    def getMultipleGameStatsById(self, matchIdList):
        games_info = []
        for matchId in matchIdList:
            match_detail = self.Watcher.match.by_id("na1", matchId)
            game_info = {}
            game_info['gameId'] = matchId
            game_info['blueTeamWin'] = match_detail['info']['teams'][0]['win']
            games_info.append(game_info)
        df = pd.DataFrame(games_info)
            

        return df

    
class PlayerInfo():
    def __init__(self, region, name) -> None:
        # values are hardcoded for now
        self.region = region
        self.name = name

    