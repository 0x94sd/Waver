import asyncio
import httpx
import json
import random
from modules.proxy import charger_proxies, get_proxy


with open("data/wmn-data.json", "r", encoding="UTF-8") as f:
    data = json.load(f)

tier_1 = {
    "Instagram": "https://www.instagram.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Twitter/X": "https://twitter.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "GitHub": "https://github.com/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Discord": "https://discord.com/users/{}",
    "Amazon": "https://www.amazon.com/gp/profile/amzn1.account.{}",
    "Shein": "https://www.shein.com/profile/{}",
    "AliExpress": "https://www.aliexpress.com/store/{}",
    "PayPal.Me": "https://paypal.me/{}",
    "Vinted": "https://www.vinted.fr/member/{}",
}

tier_2 = {
    "Dribbble": "https://dribbble.com/{}",
    "Letterboxd": "https://letterboxd.com/{}/",
    "Threads": "https://www.threads.net/@{}",
    "Quora": "https://www.quora.com/profile/{}",
}

user_agents = [
    # Chrome Desktop
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    # Chrome Mobile
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    # Firefox Desktop
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    # Firefox Mobile
    "Mozilla/5.0 (Android 13; Mobile; rv:125.0) Gecko/125.0 Firefox/125.0",
    # Edge Desktop
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    # Opera Desktop
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0",
    # Safari Desktop
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    # Safari Mobile
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
]


async def verifier_site(site_data, client, pseudo):
    try:
        url = site_data['uri_check'].replace("{account}", pseudo)
        headers = {"User-Agent": random.choice(user_agents)}
        if site_data['name'] == 'Instagram':
            headers['x-ig-app-id'] = '936619743392459'
        response = await client.get(url, headers=headers, timeout=10.0, follow_redirects=True)

        score = 0
        if response.status_code == site_data['e_code'] and site_data['e_string'] in response.text:
            score += 60
            if site_data.get('m_string') and site_data['m_string'] not in response.text:
                score += 20

        return (site_data['name'], score)
    except Exception:
        return (site_data['name'], 0)


async def scanner(pseudo):
    sites_cibles = [s for s in data['sites'] if s['name'] in tier_1 or s['name'] in tier_2]
    proxies = charger_proxies()
    proxy = get_proxy(proxies)
    async with httpx.AsyncClient(proxy=proxy) as client:
        taches = [verifier_site(s, client, pseudo) for s in sites_cibles]
        resultats_bruts = await asyncio.gather(*taches)
    return resultats_bruts