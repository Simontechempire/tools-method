import requests
from core.bypass_logic import BypassLogic

class StrikeEngine:
    def __init__(self):
        self.bypass = BypassLogic()

    def execute_report(self, platform, target, reason):
        # Mapping endpoints for different platforms
        endpoints = {
            "whatsapp": "https://api.whatsapp.com/report",
            "tiktok": "https://www.tiktok.com/api/report",
            "telegram": "https://core.telegram.org/report"
        }
        url = endpoints.get(platform, "https://api.null.com")
        proxy = self.bypass.get_random_proxy()
        ua = self.bypass.get_random_ua()
        
        try:
            proxies = {"http": proxy, "https": proxy} if proxy else None
            r = requests.post(url, data={"target": target, "reason": reason}, headers={"User-Agent": ua}, proxies=proxies, timeout=5)
            return True
        except:
            return False
