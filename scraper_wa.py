import requests
from bs4 import BeautifulSoup

def main():
    # 1. Scrape Berita
    url = "https://www.detik.com/terpopuler/inet"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article", limit=5)

        berita_list = ["*--- TOP 5 BERITA TEKNOLOGI HARI INI ---*\n"]
        for idx, article in enumerate(articles, 1):
            title_tag = article.find("h3") or article.find("a")
            link_tag = article.find("a")
            if title_tag and link_tag:
                title = title_tag.get_text(strip=True)
                link = link_tag.get("href")
                berita_list.append(f"{idx}. *{title}*\n{link}\n")

        pesan = "\n".join(berita_list)

        # 2. Kirim via Fonnte API
        fonnte_url = "https://api.fonnte.com/send"
        fonnte_payload = {
            "target": "08951829763",
            "message": pesan,
        }
        fonnte_headers = {
            "Authorization": "ufzJopJEsfVjCUgjhUTf"
        }

        res = requests.post(fonnte_url, data=fonnte_payload, headers=fonnte_headers, timeout=10)
        print("Respon Fonnte:", res.text)

    except Exception as e:
        print("Terjadi error/timeout:", e)

if __name__ == "__main__":
    main()