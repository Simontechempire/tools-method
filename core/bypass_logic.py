import random

class BypassLogic:
    def __init__(self):
        try:
            with open('data/user_agents.txt', 'r') as f:
                self.uas = [l.strip() for l in f if l.strip()]
            with open('data/proxies.txt', 'r') as f:
                self.proxies = [l.strip() for l in f if l.strip()]
        except:
            self.uas = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)"]
            self.proxies = []

    def get_random_ua(self):
        return random.choice(self.uas) if self.uas else "Mozilla/5.0"

    def get_random_proxy(self):
        return random.choice(self.proxies) if self.proxies else None
