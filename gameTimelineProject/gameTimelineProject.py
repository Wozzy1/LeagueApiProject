import time
from riotwatcher import LolWatcher, ApiError
import pandas as pd
import requests
import json
import os

class GameTimelineGenerator():

    def __init__(self) -> None:
        self.api_key = os.environ.get("riot_api_key")

    def makeCall(self, match_id: str) -> requests.Response:
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline?api_key={self.api_key}"
        response = requests.get(url)
        return response

    def getOneMatchTimelineDetail(self, response: requests.Response):
        pass


class PlayerInfo():
    def __init__(self, region, name) -> None:
        self.region = region
        self.name = name
