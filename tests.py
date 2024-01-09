from riotwatcher import LolWatcher, ApiError
import pandas as pd
import requests
import json
import os
import csv
from util import *
api_key = os.environ.get("riot_api_key")
from main import PlayerInfo, GameDataGenerator

def main():
    program = GameDataGenerator(api_key, name=None)
    _util = util()
    # games = [
    #     "NA1_4794682594",
    #     "NA1_4794657120",
    #     "NA1_4794630302",
    #     "NA1_4787649945",
    #     "NA1_4771153160",
    #     "NA1_4560075984"
    #     ]

    # for id in games:
    #     url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{id}?api_key={api_key}"
        
    #     cachedResponse = util.loadFromCache(cacheKey=id)
    #     if cachedResponse is not None:
    #         print(id)
    #         print(cachedResponse)
    #         continue
        
    #     print(f"Was not cached so had to make call and save {id}")
    #     r = requests.get(url)
    #     gameData = program.getOneGameStatsWithResponse(r)
    #     util.saveToCache(gameData, id)

    # print("===============")
    # print(util.loadFromCache("NA1_4560075984"))
    tlist = [        "NA1_4794682594",
        "NA1_4794657120",
        "NA1_4794630302",
        "NA1_4787649945",
        "NA1_4771153160",
        "NA1_4734465839",
        "NA1_4611317771",
        "NA1_4566675850",
        "NA1_4560075984",
        "NA1_4560023330",
        "NA1_4559998177",
]
    # outlist = []
    # for thing in tlist:
    #     outlist.append(_util.loadFromCache(thing))
    # df = pd.DataFrame.from_dict(outlist)
    # # print(df)

    # df.to_csv("temp_data.csv", index=False)

    # info = _util.loadFromCache("NA1_4787649945")
    # print(info)

    # print(os.listdir(_util.cacheDir)[0:10])
    temp = _util.loadFromCache("NA1_4794682594")
    columnNames = temp.keys()
    print(columnNames)

    # r = program.Watcher.match.by_id("NA1", "NA1_4794682594")
    # r = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/NA1_4794630302?api_key={api_key}")

    # print(type(program.getOneMatchDetail("NA1_4794682594")))
    # df = program.getOneGameStatsWithResponse(r)
    # print(df)   

    # print(r.status_code)
    # print(program.exceedsRateLimit(dict(r.headers)))

    # r = r.json()
    # r = json.dumps(r, indent=4)

    # file = open("temp.json", "w")
    # file.write(r)
    # file.close()
    # print("done")



    # list = program.getPlayerMatches(5)
    # print(list)
    # pd.read_csv(usecols=['gameId'])

    # file = open("americas_match_ids.json", "r")
    # data = json.load(file)

    # list = []
    # for id in data['match_ids']:
    #     list.append(id)
    #     if len(list) > 10:
    #         break

    
    # df = program.getMultipleGameStatsById(list)
    # print(df)
    # df.to_csv("data2.csv")

def check_and_add_value(csv_path, new_value):
    # Step 1: Read the CSV file
    existing_values = set()

    with open(csv_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Add the value of the first column to the set
            existing_values.add(row['gameId'])

    # Step 2 and 3: Check for duplicates and avoid adding duplicates
    new_value_id = new_value['gameId']
    if new_value_id in existing_values:
        print("Duplicate was skipped")
    else:
        with open(csv_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=new_value.keys())
            writer.writerow(new_value)

if __name__ == '__main__':
    main()