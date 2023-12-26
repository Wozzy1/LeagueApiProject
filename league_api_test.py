# DEPRECIATED FILE
# NEW MAIN FILE WILL BE /main.py

from riotwatcher import LolWatcher, ApiError
import pandas as pd
import requests
import json
api_key = "RGAPI-9b962e27-e9bc-4bfb-a8c9-4fea51739ffe"

# create a function to do all the set up so you can call it in the run program
def player_info():
    watcher = LolWatcher(api_key)
    
    # player information hardcoded for now; there is room to make this a user input
    player_region = 'na1'
    player_name = 'Wozzy'
    # player_name = 'Oreo Frost'
    
    # returns a player object to be used in querying matches
    player = watcher.summoner.by_name(player_region, player_name)
    player_matches = watcher.match.matchlist_by_puuid(player_region, player['puuid'], count=20, queue=420)
    return player_matches


# fetch last match detail
# can change later to grab more matches to feed into algo
#last_match = player_matches[0]
#match_detail = watcher.match.by_id(player_region, last_match)
match_detail = None

    
#    return(match_detail)
'''f = open('testing_league_match_details.json','a')
f.write(json.dumps(match_detail, indent=4, sort_keys=True))
'''
#print(match_detail['info']['participants'])
#print(match_detail['info']['participants'][0]['championId'])

def get_player_info(match_detail):
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

def get_player_details_multiple_games(player_matches):
    games_info = []
    for game_num in range(len(player_matches)):
        last_match = player_matches[game_num]
        match_detail = watcher.match.by_id(player_region, last_match)
        for part_num in range(len(match_detail['info']['participants'])):
            #print(match_detail['info']['participants'][part_num]['summonerName'])
            if match_detail['info']['participants'][part_num]['summonerName'] == player_name:
                
                #playernum = match_detail['info']['participants']['summonerName'].index('WZ802')
                part_row = {}
                part_row['Win'] = match_detail['info']['participants'][part_num]['win']
                part_row['champion'] = match_detail['info']['participants'][part_num]['championName']
                part_row['game length (sec)'] = match_detail['info']['participants'][part_num]['timePlayed']
                part_row['kills'] = match_detail['info']['participants'][part_num]['kills']
                part_row['deaths'] = match_detail['info']['participants'][part_num]['deaths']
                part_row['assists'] = match_detail['info']['participants'][part_num]['assists']
                part_row['goldEarned'] = match_detail['info']['participants'][part_num]['goldEarned']
                part_row['CS'] = match_detail['info']['participants'][part_num]['totalMinionsKilled']
                part_row['dmg to champs'] = match_detail['info']['participants'][part_num]['totalDamageDealtToChampions']
                games_info.append(part_row)
    df = pd.DataFrame(games_info)
    return(print(df))

def main(match_detail):
    player_info()
    get_player_details_multiple_games(player_matches)
    #get_player_info(match_detail)
    
main(match_detail)


#participants = []

#print(match_detail(['info']['gameId']))
#i=0
#while i < 10:
# row is essentially a person in an array

'''for row in match_detail(['info']['participants']):
    participants_row = {}
    participants_row['champion'] = row['championName']
    participants.append(participants_row)

    i+=1
df = pd.DataFrame(participants)
print(df)
'''
'''
participants = []
for row in match_detail['participants']:
    participants_row = {}
    participants_row['champion'] = row['championId']
    participants_row['spell1'] = row['spell1Id']
    participants_row['spell2'] = row['spell2Id']
    participants_row['win'] = row['stats']['win']
    participants_row['kills'] = row['stats']['kills']
    participants_row['deaths'] = row['stats']['deaths']
    participants_row['assists'] = row['stats']['assists']
    participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
    participants_row['goldEarned'] = row['stats']['goldEarned']
    participants_row['champLevel'] = row['stats']['champLevel']
    participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
    participants_row['item0'] = row['stats']['item0']
    participants_row['item1'] = row['stats']['item1']
    participants.append(participants_row)
df = pd.DataFrame(participants)'''