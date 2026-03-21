import random


def charger_proxies():
    try:
        with open("proxies.txt", "r", encoding="utf-8") as f:
            proxies = [line.strip() for line in f if line.strip()]
        return proxies
    except FileNotFoundError:
        return []


def get_proxy(proxies):
    if not proxies:
        return None
    proxy = random.choice(proxies)
    return proxy