from config import Config
import random

def get_random_proxy():
    return random.choice(Config.PROXY_LIST)
