Tamam kardeşim, README dosyasını çektiğin resimlere göre düzenliyorum. İşte hatasız, güzel görünümlü README.md:

```markdown
# 🔍 Keneviz - UserName Search Tool

---

## 🎯 Hakkında

**Keneviz**, bir kullanıcı adının 200'den fazla sosyal medya, e-ticaret, eğitim, oyun ve diğer platformlardaki varlığını tarayan güçlü bir **OSINT (Açık Kaynak İstihbarat)** aracıdır.

> ⚡ **Hızlı**, **güvenilir** ve **kullanımı kolay** - Sadece bir kullanıcı adı girin, tüm platformlardaki izlerini keşfedin!

---

## ✨ Özellikler

| Özellik | Açıklama |
|---------|----------|
| 🌐 **200+ Site** | Sosyal medya, e-ticaret, oyun, eğitim, blog ve daha fazlası |
| 🚀 **Hızlı Tarama** | Çoklu thread desteği ile saniyeler içinde sonuç |
| 📁 **Otomatik Kayıt** | Sonuçlar `data/username.txt` dosyasına kaydedilir |
| 🎨 **Renkli Çıktı** | Bulunan siteler yeşil, bulunamayanlar kırmızı ile gösterilir |
| 🔄 **Sonsuz Döngü** | Tarama bitince ENTER ile devam, manuel çıkış |
| 🛡️ **SSL Hatasız** | Tüm SSL uyarıları kapatıldı, temiz çıktı |
| 📱 **Termux Uyumlu** | Android'de sorunsuz çalışır |

---

```

🔧 Termux / Linux

```Kurulum
# Gerekli paketleri yükle
pkg update && pkg upgrade -y
pkg install python git -y

# Repoyu clone'la
git clone https://github.com/jameikakeno/Rdmke.git
cd Rdmke

# Python kütüphanelerini yükle
pip install requests beautifulsoup4

# Çalıştır
python search.py
```

---

🚀 Kullanım

Temel Kullanım

```bash
python search.py
```

Program başladığında sizden kullanıcı adını isteyecektir:

```
[?] Kullanıcı adı: keneviz
[*] keneviz taranıyor (201 site)

[1] [+] Twitter
[2] [+] Instagram
[3] [+] GitHub
...
[+] Bulunan: 26 site
```

Sonuçlar

Tarama sonuçları otomatik olarak data/ klasörüne kaydedilir:

```
data/
└── kullaniciadi.txt
```

---

📸 Desteklenen Platformlar (201+ Site)

<details>
<summary><b>Sosyal Medya (30+ site)</b></summary>

· Facebook, Twitter, Instagram, YouTube, Snapchat, TikTok, Reddit
· Pinterest, Tumblr, LinkedIn, Telegram, Twitch, VK
· Threads, Bluesky, Mastodon, WhatsApp, Discord, Signal
· WeChat, QQ, SinaWeibo, Likee, Triller, Mewe
· Parler, Gab, TruthSocial, Rumble, Odysee

</details>

<details>
<summary><b>E-ticaret (15+ site)</b></summary>

· eBay, Fiverr, Amazon, Etsy, AliExpress, Shopify
· Wish, Mercari, Poshmark, Depop, Grailed, Reverb, Discogs

</details>

<details>
<summary><b>Eğitim (12+ site)</b></summary>

· Khan Academy, Coursera, Udemy, edX, Duolingo, Quizlet
· Brilliant, Codecademy, FreeCodeCamp, SoloLearn, W3Schools

</details>

<details>
<summary><b>Yazılım & Kariyer (25+ site)</b></summary>

· GitHub, GitLab, Bitbucket, Stack Overflow, Medium, Dev.to
· HackerRank, LeetCode, Coderbyte, Upwork, Freelancer
· Topcoder, Codeforces, AtCoder, HackerEarth, CodinGame

</details>

<details>
<summary><b>Oyun Platformları (15+ site)</b></summary>

· Steam, Roblox, Epic Games, Xbox, PlayStation, Nintendo
· Chess.com, Lichess, RuneScape, Minecraft, Kongregate

</details>

<details>
<summary><b>Diğer Platformlar (100+ site)</b></summary>

· Spotify, SoundCloud, Patreon, DeviantArt, Behance, Dribbble
· Wikipedia, Quora, Wattpad, Pastebin, Linktree, Imgur
· Tinder, Bumble, Hinge, OkCupid, POF (Dating)
· Ve daha fazlası...

</details>

---

📱 Desteklenen Platformlar

Platform Durum
✅ Termux (Android) Tam destek
✅ Linux (Ubuntu/Debian) Tam destek
✅ Windows (CMD/PowerShell) Tam destek
✅ macOS Tam destek
✅ Replit Tam destek

---

👨‍💻 Geliştirici

<p align="center">
  <img src="https://img.shields.io/badge/Dev-Keneviz-red?style=for-the-badge">
</p>

Telegram: @KenevizPremiumTool
---

⭐ Destek

Projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐

<p align="center">
  <img src="https://img.shields.io/github/stars/jameikakeno/Rdmke?style=social">
  <img src="https://img.shields.io/github/forks/jameikakeno/Rdmke?style=social">
  <img src="https://img.shields.io/github/watchers/jameikakeno/Rdmke?style=social">
</p>

---

Keneviz - Güçlü, Hızlı, Etkili 🔍

```

Keneviz tarafından hazırlanmıştır. 🚀
