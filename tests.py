from riotWatcher import LolWatcher, ApiError
import pandas as pd
import requests
import json
api_key = "RGAPI-9b962e27-e9bc-4bfb-a8c9-4fea51739ffe"

from main import Player

def main():
    player = Player("na1", "Wozzy")
    
    print("Expected: na1\n" + player.region)
    print("Expected: Wozzy\n" + player.name)

main()