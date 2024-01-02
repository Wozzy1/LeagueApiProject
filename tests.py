from riotwatcher import LolWatcher, ApiError
import pandas as pd
import requests
import json
api_key = "RGAPI-4f036562-2a9d-4deb-b4ae-5bb84f4824ec"

from main import PlayerInfo, GameDataGenerator

def main():
    program = GameDataGenerator(api_key, "WZ802")
    
    list = program.getPlayerMatches()
    # print(list)
    # for thing in list:
    #     print(thing)

    # match_detail = program.getLastMatchDetail(list)


    # f = open('testing_league_match_details.json','w')
    # f.write(json.dumps(match_detail['info'], indent=4, sort_keys=True))
    # f.close()

    # program.getPlayerOneGameStats(0)
    # df = program.getMultipleGameStatsByPlayer(list)
    # print(df)

    df = program.getMultipleGameStatsById(list)
    
    df.to_csv("data2.csv")

if __name__ == '__main__':
    main()