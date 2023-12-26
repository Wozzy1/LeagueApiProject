from riotwatcher import LolWatcher, ApiError
import pandas as pd
import requests
import json
api_key = "RGAPI-9b962e27-e9bc-4bfb-a8c9-4fea51739ffe"

from main import PlayerInfo, GameDataGenerator

def main():
    program = GameDataGenerator(api_key, "WZ802")
    
    list = program.getPlayerMatches()
    # for thing in list:
    #     print(thing)

    # match_detail = program.getLastMatchDetail(list)


    # f = open('testing_league_match_details.json','w')
    # f.write(json.dumps(match_detail['info'], indent=4, sort_keys=True))
    # f.close()

    # program.getPlayerOneGameStats(0)
    program.getPlayerMultipleGameStats(list)

if __name__ == '__main__':
    main()