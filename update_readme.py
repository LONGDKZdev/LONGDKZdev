import requests
import matplotlib.pyplot as plt
from datetime import date
import os

USERNAME = "LONGDKZdev"

# Lấy danh sách repo
url = f"https://api.github.com/users/{USERNAME}/repos"
response = requests.get(url)
repos = response.json()
public_repos = len(repos)

# Thống kê ngôn ngữ
lang_count = {}
for repo in repos:
    lang = repo["language"]
    if lang:
        lang_count[lang] = lang_count.get(lang, 0) + 1

langs = list(lang_count.keys())
counts = list(lang_count.values())

# Vẽ biểu đồ tròn
plt.figure(figsize=(6, 6))
plt.pie(counts, labels=langs, autopct='%1.1f%%', startangle=140)
plt.title('📚 Tỷ lệ ngôn ngữ theo repo')
plt.tight_layout()
os.makedirs("charts", exist_ok=True)
plt.savefig('charts/lang_chart.png')

# Cập nhật readme.md
with open("readme.md", "w", encoding="utf-8") as f:
    f.write(f"""# 👨‍💻 Dashboard của {USERNAME}

## 📦 Tổng số repo: {public_repos}

## 📊 Tỷ lệ ngôn ngữ theo repo

![Biểu đồ ngôn ngữ](charts/lang_chart.png)

_Last updated: {date.today()}_

---
""")
