from riotwatcher import LolWatcher, ApiError
import pandas as pd
import requests
import json
api_key = "RGAPI-08576416-f07a-44ac-8e9c-777919706474"

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
    df = program.getMultipleGameStatsByPlayer(list)
    print(df)

if __name__ == '__main__':
    main()