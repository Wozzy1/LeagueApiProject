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
            for participant_num in range(1, len(match_detail['info']['participants']) + 1):
                #print(match_detail['info']['participants'][participant_num]['summonerName'])
                if match_detail['info']['participants'][participant_num]['summonerName'] == self.Player.name:
                    participant_row = {}
                    participant_row['gameId'] = match_detail['metadata']['matchId']
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
    - avg champion levels (float) X
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
    - dragons killed (int) X
        - elder dragon (int) no datapoint
    - first rift
    - rift heralds taken (int)
    - first baron
    - barons (int) X
    - first tower X
    - towers destroyed (int) X
    - blue team win (boolean) X
    - blue team first blood (boolean) X
    - team total KDA X
        - Kills
        - Deaths
        - Assists
    - vision score X
    - pink wards X
    - wards placed X
    - wards killed X
    """
    def getMultipleGameStatsById(self, matchIdList):
        games_info = []
        for matchId in matchIdList:
            match_detail = self.Watcher.match.by_id("na1", matchId)
            game_info = {}
            game_info['gameId'] = matchId
            game_info['blueTeamWin'] = match_detail['info']['teams'][0]['win']

            game_info['blueFirstBlood'] = match_detail['info']['teams'][0]['objectives']['champion']['first']   
            
            kills, deaths, assists, level, goldEarned = 0, 0, 0, 0, 0
            visionScore, pinkWards, wardsPlaced, wardsKilled = 0, 0, 0, 0
            for player in range(0, 5):
                kills += match_detail['info']['participants'][player]['kills']
                deaths += match_detail['info']['participants'][player]['deaths']
                assists += match_detail['info']['participants'][player]['assists']
                visionScore += match_detail['info']['participants'][player]['visionScore']
                pinkWards += match_detail['info']['participants'][player]['visionWardsBoughtInGame']
                wardsPlaced += match_detail['info']['participants'][player]['wardsPlaced']
                wardsKilled += match_detail['info']['participants'][player]['wardsKilled']
                level += match_detail['info']['participants'][player]['champLevel']
                goldEarned += match_detail['info']['participants'][player]['goldEarned']

            game_info['blueTeamKills'] = kills
            game_info['blueTeamDeaths'] = deaths
            game_info['blueTeamAssists'] = assists
            game_info['blueVisionScore'] = visionScore
            game_info['bluePinkWards'] = pinkWards
            game_info['blueWardsPlaced'] = wardsPlaced
            game_info['blueWardsKilled'] = wardsKilled
            game_info['blueAverageLevel'] = level / 5.0
            game_info['blueAverageGold'] = goldEarned / 5.0

            kills, deaths, assists, level, goldEarned = 0, 0, 0, 0, 0
            visionScore, pinkWards, wardsPlaced, wardsKilled = 0, 0, 0, 0
            for player in range(5, 10):
                kills += match_detail['info']['participants'][player]['kills']
                deaths += match_detail['info']['participants'][player]['deaths']
                assists += match_detail['info']['participants'][player]['assists']
                visionScore += match_detail['info']['participants'][player]['visionScore']
                pinkWards += match_detail['info']['participants'][player]['visionWardsBoughtInGame']
                wardsPlaced += match_detail['info']['participants'][player]['wardsPlaced']
                wardsKilled += match_detail['info']['participants'][player]['wardsKilled']
                level += match_detail['info']['participants'][player]['champLevel']
                goldEarned += match_detail['info']['participants'][player]['goldEarned']

            game_info['redTeamKills'] = kills
            game_info['redTeamDeaths'] = deaths
            game_info['redTeamAssists'] = assists
            game_info['redVisionScore'] = visionScore
            game_info['redPinkWards'] = pinkWards
            game_info['redWardsPlaced'] = wardsPlaced
            game_info['redWardsKilled'] = wardsKilled
            game_info['redAverageLevel'] = level / 5.0
            game_info['redAverageGold'] = goldEarned / 5.0

            game_info['blueFirstDragon'] = match_detail['info']['teams'][0]['objectives']['dragon']['first']
            game_info['blueDragonsKilled'] = match_detail['info']['teams'][0]['objectives']['dragon']['kills']
            game_info['redDragonsKilled'] = match_detail['info']['teams'][1]['objectives']['dragon']['kills']

            game_info['blueFirstRiftHerald'] = match_detail['info']['teams'][0]['objectives']['riftHerald']['first']
            game_info['blueRiftHeraldsKilled'] = match_detail['info']['teams'][0]['objectives']['riftHerald']['kills']
            game_info['redRiftHeraldsKilled'] = match_detail['info']['teams'][1]['objectives']['riftHerald']['kills']

            game_info['blueFirstBaron'] = match_detail['info']['teams'][0]['objectives']['baron']['first']
            game_info['blueBaronsKilled'] = match_detail['info']['teams'][0]['objectives']['baron']['kills']
            game_info['redBaronsKilled'] = match_detail['info']['teams'][1]['objectives']['baron']['kills']

            game_info['blueFirstTower'] = match_detail['info']['teams'][0]['objectives']['tower']['first']
            game_info['blueTowersDestroyed'] = match_detail['info']['teams'][0]['objectives']['tower']['kills']
            game_info['redTowersDestroyed'] = match_detail['info']['teams'][1]['objectives']['tower']['kills']



            games_info.append(game_info)
        df = pd.DataFrame(games_info)
            

        return df
        

    
class PlayerInfo():
    def __init__(self, region, name) -> None:
        self.region = region
        self.name = name

    