from riotwatcher import LolWatcher, ApiError
import pandas as pd
import requests
import json
api_key = "RGAPI-c6670e3d-3770-49cd-ae8e-293c3f154f31"

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
    df = program.getPlayerMultipleGameStats(list)
    print(df)

if __name__ == '__main__':
    main()