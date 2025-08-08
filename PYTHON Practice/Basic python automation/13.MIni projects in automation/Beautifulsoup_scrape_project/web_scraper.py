import requests
from bs4 import BeautifulSoup

def fetch_quotes(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes_html = soup.find_all('div', class_='quote')
    
    quotes = []
    for quote_div in quotes_html:
        text = quote_div.find('span', class_='text').get_text()
        author = quote_div.find('small', class_='author').get_text()
        quotes.append({'text': text, 'author': author})

    return quotes

def main():
    url = 'http://quotes.toscrape.com'
    quotes = fetch_quotes(url)

    for i, quote in enumerate(quotes, start=1):
        print(f"{i}. \"{quote['text']}\" - {quote['author']}")

if __name__ == "__main__":
    main()
