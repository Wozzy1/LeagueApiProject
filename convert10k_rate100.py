from main import *
import time
import pandas as pd

"""
goal: 
to read 10k rows from csv X
send them through main 100 entries at a time
piece together all 100 runs into one big dataset
output dataset to be split into training and testing data
"""

api_key = "RGAPI-4f036562-2a9d-4deb-b4ae-5bb84f4824ec"

def read10k() -> list:
    data = pd.read_csv("high_diamond_ranked_10min.csv", usecols=['gameId'])
    data = data['gameId'].tolist()
    return data

def main(list_of_10k_ids):
    program = GameDataGenerator(api_key, name=None)
    count = 0
    completed = 0
    output_df = None
    while completed < len(10):

        # every 100 it sleeps for a minute to reset the api maximum
        if count > 100:
            time.sleep(60)
            count = 0
        
        df = program.getMultipleGameStatsById()
        output_df = pd.concat(output_df, df)

