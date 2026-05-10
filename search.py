#! /usr/bin/env python3
"""
Keneviz - Track and Unveil Online identities across social media platforms.
Developed by Keneviz
"""
import os
import re
import datetime
import random
import time
import requests
import warnings
import ssl
import urllib3
from bs4 import BeautifulSoup

# TÜM UYARILARI KAPAT
warnings.filterwarnings('ignore')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

__version__ = "1.1.3"

# Keneviz - Renkli Banner
banner = f"""
\033[1;32m            _  __      \033[1;31mUserName Search Tool\033[1;32m      _         
\033[1;32m           | |/ /   ___   _ __     ___  __   __ (_)  ____  
\033[1;32m           | ' /   / _ \\ | '_ \\   / _ \\ \\ \\ / / | | |_  /  
\033[1;32m           | . \\  |  __/ | | | | |  __/  \\ V /  | |  / /   
\033[1;32m           |_|\\_\\  \\___| |_| |_|  \\___|   \\_/   |_| /___|  
\033[1;36m                            Dev : Keneviz
\033[1;32m═══════════════════════════════════════════════════════════════\033[0m
"""

# Soft404 indicators
soft404_indicators = [
    "This profile could not be found", "Sorry, this user was not found",
    "Page Not Found", "the profile was either removed ",
    "The specified profile could not be found", "doesn&apos;t&nbsp;exist",
    "This page doesn't exist", "404 Not Found",
    "Sorry, nobody on Reddit goes by that name", "user does not exist",
    "User not found.", "Not Found!", "Page not found", "doesn't exist",
    "This profile is not available", "No user found", "User not active",
    "Account not found", "Profile not found", "does not exist"
]

# User-Agents list
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
]

# TÜM SİTELER - EKSİKSİZ
sites = {
    # Social Media Platforms
    "Facebook": "https://www.facebook.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Tumblr": "https://{}.tumblr.com",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Telegram": "https://t.me/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "VK": "https://vk.com/{}",
    "Threads": "https://www.threads.net/@{}",
    "Bluesky": "https://bsky.app/profile/{}",
    "Mastodon": "https://mastodon.social/@{}",
    "WhatsApp": "https://wa.me/{}",
    "Discord": "https://discord.com/users/{}",
    "Signal": "https://signal.me/#p/{}",
    "Telegram": "https://t.me/{}",
    "WeChat": "https://wechat.com/{}",
    "QQ": "https://user.qzone.qq.com/{}",
    "SinaWeibo": "https://weibo.com/u/{}",
    "Likee": "https://likee.video/@{}",
    "Triller": "https://triller.co/@{}",
    "Mewe": "https://mewe.com/i/{}",
    "Parler": "https://parler.com/{}",
    "Gab": "https://gab.com/{}",
    "TruthSocial": "https://truthsocial.com/@{}",
    "Rumble": "https://rumble.com/user/{}",
    "Odysee": "https://odysee.com/@{}",
    # E-commerce & Marketplace
    "eBay": "https://www.ebay.com/usr/{}",
    "Fiverr": "https://www.fiverr.com/{}",
    "Amazon": "https://www.amazon.com/gp/profile/amzn1.account.{}",
    "Etsy": "https://www.etsy.com/shop/{}",
    "AliExpress": "https://www.aliexpress.com/store/{}",
    "Shopify": "https://{}.myshopify.com",
    "Wish": "https://www.wish.com/u/{}",
    "Mercari": "https://www.mercari.com/u/{}",
    "Poshmark": "https://poshmark.com/closet/{}",
    "Depop": "https://www.depop.com/{}",
    "Grailed": "https://www.grailed.com/user/{}",
    "Reverb": "https://reverb.com/user/{}",
    "Discogs": "https://www.discogs.com/user/{}",
    # Educational Platforms
    "Khan Academy": "https://www.khanacademy.org/profile/{}",
    "Coursera": "https://www.coursera.org/user/{}",
    "Udemy": "https://www.udemy.com/user/{}",
    "edX": "https://www.edx.org/user/{}",
    "Duolingo": "https://www.duolingo.com/profile/{}",
    "Quizlet": "https://quizlet.com/{}",
    "Brilliant": "https://brilliant.org/profile/{}",
    "Codecademy": "https://www.codecademy.com/profiles/{}",
    "FreeCodeCamp": "https://www.freecodecamp.org/{}",
    "SoloLearn": "https://www.sololearn.com/profile/{}",
    "W3Schools": "https://www.w3schools.com/profile/{}",
    # Professional & Business Networks
    "Crunchbase": "https://www.crunchbase.com/person/{}",
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Bitbucket": "https://bitbucket.org/{}",
    "Behance": "https://www.behance.net/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Stack Overflow": "https://stackoverflow.com/users/{}",
    "Medium": "https://medium.com/@{}",
    "Dev.to": "https://dev.to/{}",
    "HackerRank": "https://hackerrank.com/{}",
    "LeetCode": "https://leetcode.com/{}",
    "Coderbyte": "https://www.coderbyte.com/profile/{}",
    "Upwork": "https://www.upwork.com/freelancers/{}",
    "Freelancer": "https://www.freelancer.com/u/{}",
    "F6S": "https://www.f6s.com/{}",
    "Keybase": "https://keybase.io/{}",
    "AngelList": "https://angel.co/u/{}",
    "Wellfound": "https://wellfound.com/u/{}",
    "Meetup": "https://www.meetup.com/members/{}",
    "ResearchGate": "https://www.researchgate.net/profile/{}",
    "Academia.edu": "https://{}.academia.edu",
    "Google Scholar": "https://scholar.google.com/citations?user={}",
    "ORCID": "https://orcid.org/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    # Creative & Multimedia Platforms
    "DeviantArt": "https://{}.deviantart.com",
    "Patreon": "https://www.patreon.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Vimeo": "https://vimeo.com/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Bandcamp": "https://bandcamp.com/{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "Mixcloud": "https://www.mixcloud.com/{}",
    "Audiojungle": "https://audiojungle.net/user/{}",
    "500px": "https://500px.com/{}",
    "Imgur": "https://imgur.com/user/{}",
    "Unsplash": "https://unsplash.com/@{}",
    "Pexels": "https://www.pexels.com/@{}",
    "ArtStation": "https://www.artstation.com/{}",
    "Pixiv": "https://www.pixiv.net/en/users/{}",
    "Newgrounds": "https://{}.newgrounds.com",
    "Smule": "https://www.smule.com/{}",
    # Blogging & Writing Platforms
    "Blogger": "https://{}.blogspot.com",
    "WordPress": "https://{}.wordpress.com",
    "WordPressOrg": "https://profiles.wordpress.org/{}",
    "Wix": "https://{}.wixsite.com/website",
    "Weebly": "https://{}.weebly.com",
    "LiveJournal": "https://{}.livejournal.com",
    "BuzzFeed": "https://buzzfeed.com/{}",
    "HubPages": "https://hubpages.com/@{}",
    "Note": "https://note.com/{}",
    "Substack": "https://substack.com/@{}",
    "Ghost": "https://{}.ghost.io",
    "Hashnode": "https://hashnode.com/@{}",
    "GithubPages": "https://{}.github.io",
    "Netlify": "https://{}.netlify.app",
    "Vercel": "https://{}.vercel.app",
    # Gaming & Streaming Platforms
    "Steam": "https://steamcommunity.com/id/{}",
    "SteamGroup": "https://steamcommunity.com/groups/{}",
    "Roblox": "https://www.roblox.com/user.aspx?username={}",
    "AQW": "https://account.aq.com/CharPage?id={}",
    "SourceForge": "https://sourceforge.net/u/{}",
    "GOG": "https://www.gog.com/u/{}",
    "Osu!": "https://osu.ppy.sh/users/{}",
    "RuneScape": "https://apps.runescape.com/runemetrics/app/overview/player/{}",
    "Kongregate": "https://www.kongregate.com/accounts/{}",
    "EpicGames": "https://www.epicgames.com/id/{}",
    "Xbox": "https://www.xboxgamertag.com/{}",
    "PlayStation": "https://psnprofiles.com/{}",
    "Nintendo": "https://www.nintendo.com/users/{}",
    "BattleNet": "https://www.battlenet.com/{}",
    "Minecraft": "https://namemc.com/profile/{}",
    "Chess": "https://www.chess.com/member/{}",
    "Lichess": "https://lichess.org/@/{}",
    "PokemonShowdown": "https://pokemonshowdown.com/users/{}",
    "TETR.IO": "https://ch.tetr.io/u/{}",
    "Monkeytype": "https://monkeytype.com/profile/{}",
    # Other Platforms
    "Houzz": "https://houzz.com/user/{}",
    "Gravatar": "https://gravatar.com/{}",
    "SlideShare": "https://www.slideshare.net/{}",
    "Wikipedia": "https://en.wikipedia.org/wiki/User:{}",
    "DailyMotion": "https://www.dailymotion.com/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Wattpad": "https://www.wattpad.com/user/{}",
    "PyPi": "https://pypi.org/user/{}",
    "Slides": "https://slides.com/{}",
    "SpeakerDeck": "https://speakerdeck.com/{}",
    "Goodreads": "https://www.goodreads.com/{}",
    "Last.fm": "https://www.last.fm/user/{}",
    "Letterboxd": "https://letterboxd.com/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "MySpace": "https://www.myspace.com/{}",
    "MyAnimeList": "https://myanimelist.net/profile/{}",
    "BuyMeACoffee": "https://www.buymeacoffee.com/{}",
    "Pastebin": "https://pastebin.com/u/{}",
    "Mydramalist": "https://www.mydramalist.com/profile/{}",
    "Scribd": "https://www.scribd.com/{}",
    "Fixya": "https://www.fixya.com/users/{}",
    "Issuu": "https://issuu.com/{}",
    "Venmo": "https://account.venmo.com/u/{}",
    "ThemeForest": "https://themeforest.net/user/{}",
    "TradingView": "https://www.tradingview.com/u/{}",
    "Scratch": "https://scratch.mit.edu/users/{}",
    "Replit": "https://replit.com/@{}",
    "OpenStreetMap": "https://www.openstreetmap.org/user/{}",
    "Linktree": "https://linktr.ee/{}",
    "Instructables": "https://www.instructables.com/member/{}",
    "GaiaOnline": "https://www.gaiaonline.com/profiles/{}",
    "Flipboard": "https://flipboard.com/{}",
    "Disqus": "https://disqus.com/by/{}",
    "AppleDiscussions": "https://discussions.apple.com/profile/{}",
    "Anilist": "https://anilist.co/user/{}",
    "Minds": "https://www.minds.com/{}",
    "uID": "https://uid.me/{}",
    "Interpals": "https://www.interpals.net/{}",
    "Geocaching": "https://www.geocaching.com/p/default.aspx?u={}",
    "FurAffinity": "https://www.furaffinity.net/user/{}",
    "devRant": "https://devrant.com/users/{}",
    "Couchsurfing": "https://www.couchsurfing.com/people/{}",
    "YouPic": "https://youpic.com/photographer/{}",
    "UltimateGuitar": "https://ultimate-guitar.com/u/{}",
    "TryHackMe": "https://tryhackme.com/p/{}",
    "Trello": "https://trello.com/{}",
    "Trakt": "https://www.trakt.tv/users/{}",
    "Periscope": "https://www.periscope.tv/{}",
    "Polarsteps": "https://polarsteps.com/{}",
    "Naver": "https://blog.naver.com/{}",
    "Hackaday": "https://hackaday.io/{}",
    "Clapper": "https://clapperapp.com/{}",
    "Bikemap": "https://www.bikemap.net/en/u/{}/routes/created/",
    "BioHacking": "https://forum.dangerousthings.com/u/{}",
    "Weblate": "https://hosted.weblate.org/user/{}",
    "GitHubGist": "https://gist.github.com/{}",
    "GitstarRanking": "https://gitstar-ranking.com/{}",
    # Dating Apps
    "Tinder": "https://www.tinder.com/@{}",
    "Bumble": "https://bumble.com/{}",
    "Hinge": "https://hinge.co/{}",
    "OkCupid": "https://www.okcupid.com/profile/{}",
    "PlentyOfFish": "https://www.pof.com/viewprofile.aspx?username={}",
    # Coding Platforms
    "Topcoder": "https://www.topcoder.com/members/{}",
    "Codeforces": "https://codeforces.com/profile/{}",
    "AtCoder": "https://atcoder.jp/users/{}",
    "HackerEarth": "https://www.hackerearth.com/@{}",
    "CodinGame": "https://www.codingame.com/profile/{}",
    "JSFiddle": "https://jsfiddle.net/user/{}",
    "CodePen": "https://codepen.io/{}",
    "Replit": "https://replit.com/@{}",
    "Glitch": "https://glitch.com/@{}",
    "GitKraken": "https://www.gitkraken.com/user/{}",
}

print(f"\033[1;33m[!] Toplam {len(sites)} site taranacak\033[0m")

class Keneviz:
    def __init__(self, username: str):
        self.username = username
        self.found_sites = []
        self.total_sites = len(sites)
        self.counter = 0

    def is_soft404(self, html):
        try:
            soup = BeautifulSoup(html, "html.parser")
            title = soup.title.string.strip() if soup.title else ""
            for error in soft404_indicators:
                if error.lower() in html.lower() or error.lower() in title.lower():
                    return True
        except:
            pass
        return False

    def check_site(self, site, url_template, num):
        url = url_template.format(self.username)
        try:
            session = requests.Session()
            session.verify = False
            headers = {"User-Agent": random.choice(user_agents)}
            response = session.get(url, headers=headers, timeout=8)
            
            if response.status_code == 200 and self.username.lower() in response.text.lower() and not self.is_soft404(response.text):
                self.found_sites.append((site, url))
                print(f"\033[1;32m[{num}] [+]\033[0m \033[1;32m{site}\033[0m")
            else:
                print(f"\033[1;31m[{num}] [-]\033[0m \033[1;31m{site}\033[0m")
        except:
            print(f"\033[1;31m[{num}] [-]\033[0m \033[1;31m{site}\033[0m")

    def start(self):
        print(f"\n\033[1;33m[*] {self.username} taranıyor ({self.total_sites} site)\033[0m\n")
        
        if not os.path.exists("data"):
            os.mkdir("data")
        
        with open(f"data/{self.username}.txt", "a", encoding='utf-8') as f:
            f.write(f"\n{'#'*50}\n{datetime.datetime.now()}\n{'#'*50}\n\n")
        
        num = 1
        for site_name, url in sites.items():
            self.check_site(site_name, url, num)
            num += 1
            time.sleep(0.01)
        
        print(f"\n\033[1;32m[+] Bulunan: {len(self.found_sites)} site\033[0m")
        
        if self.found_sites:
            print(f"\n\033[1;33m[!] Linkler:\033[0m")
            for site, url in self.found_sites:
                print(f"\033[1;32m  -> {site}: \033[1;34m{url}\033[0m")
            
            with open(f"data/{self.username}.txt", "a", encoding='utf-8') as f:
                f.write(f"\nBULUNANLAR ({len(self.found_sites)}):\n")
                for site, url in self.found_sites:
                    f.write(f"{site}: {url}\n")
            
            print(f"\n\033[1;32m[@] Kayıt: data/{self.username}.txt\033[0m")
        else:
            print(f"\n\033[1;31m[!] Hiçbir sonuç bulunamadı\033[0m")
        
        print(f"\n\033[1;36m{'─'*50}\033[0m")

def main():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(banner)
        
        username = input(f"\n\033[1;36m[?] Kullanıcı adı: \033[0m").strip()
        
        if not username:
            print(f"\n\033[1;31m[!] Boş olamaz!\033[0m")
            time.sleep(1)
            continue
        
        k = Keneviz(username)
        k.start()
        
        input(f"\n\033[1;33m[ENTER] Devam etmek için...\033[0m")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\033[1;31m\n[!] Çıkış Yapılıyor...\033[0m")
