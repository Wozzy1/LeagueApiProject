import os
import pickle
import time

class util:

    def __init__(self):
        if os.path.exists("\cache"):
            self.cacheDir = "\cache"
            print("It exists already")
        else:
            os.makedirs("\cache")
            self.cacheDir= "\cache"
            print("Created the cache folder")

    def saveToCache(self, cacheData, cacheKey: str) -> None:
        cachePath = os.path.join(self.cacheDir, f"{cacheKey}.pkl")
        cacheData = {"data": cacheData, "timestamp": int(time.time())}
        # print(cacheData)
        with open(cachePath, "wb") as content:
            pickle.dump(cacheData, content)

    def loadFromCache(self, cacheKey: str):
        cachePath = os.path.join(self.cacheDir, f"{cacheKey}.pkl")

        if os.path.exists(cachePath):
            with open(cachePath, "rb") as content:
                cacheData = pickle.load(content)
                
                """
                this line is not needed because my data shouldnt change over time
                I am okay with having a local cache for as long as needed
                """
                # if (int(time.time()) - cacheData["timestamp"] <= 1000):
                return cacheData["data"]
        
    

"""
if settings_manager.cache_enabled == True:
    cache_dir = "cache"

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)


def save_to_cache(cache_data, cache_key: str):
    if settings_manager.cache_enabled == True:
        cache_path = os.path.join(cache_dir, f"{cache_key}.pkl")
        cache_data = {"data": cache_data, "timestamp": int(time.time())}

        with open(cache_path, "wb") as cfp:
            pickle.dump(cache_data, cfp)


def load_from_cache(cache_key: str):
    if settings_manager.cache_enabled == True:
        cache_path = os.path.join(cache_dir, f"{cache_key}.pkl")

        if os.path.exists(cache_path):
            with open(cache_path, "rb") as cfp:
                cache_data = pickle.load(cfp)

                if (int(time.time()) - cache_data["timestamp"] <= settings_manager.cache_ttl):
                    return cache_data["data"]

        return None"""