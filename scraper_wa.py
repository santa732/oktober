import os
import requests
from bs4 import BeautifulSoup


FONNTE_TOKEN = "b5RcckpjVtt1Xs2EU2so"
TARGET_WA_NUMBER = "0889518292763"  

headers = {
    'Authorization': 'Tb5RcckpjVtt1Xs2EU2so'
}

def scrape_latest_news():
    url = "https://news.ycombinator.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Mengambil 5 headline berita teratas
        titles = soup.select(".titleline > a")[:5]

        message = "📰 *TOP 5 TECH NEWS HARI INI*\n"
        message += "━━━━━━━━━━━━━━━━━━━━━━━\n\n"

        for index, item in enumerate(titles, 1):
            news_title = item.text
            news_link = item['href']
            message += f"{index}. *{news_title}*\n🔗 {news_link}\n\n"

        message += "🤖 _Laporan Otomatis via GitHub Actions & Fonnte_"
        return message

    except Exception as e:
        print(f"Error saat scraping: {e}")
        return None


def send_whatsapp_message(content):
    if not content:
        return

    url = "https://api.fonnte.com/send"
    payload = {
        'target': TARGET_WA_NUMBER,
        'message': content,
        'countryCode': '62', 
    }
    headers = {
        'Authorization': FONNTE_TOKEN
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        print("Response:", response.text)
        if response.status_code == 200:
            print("✅ Berita berhasil dikirim ke WhatsApp!")
        else:
            print(f"❌ Gagal mengirim: {response.text}")
    except Exception as e:
        print(f"❌ Terjadi error: {e}")


if __name__ == "__main__":
    news = scrape_latest_news()
    send_whatsapp_message(news)