import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data)
    df = df[["name", "current_price", "market_cap", "total_volume"]]


    df.dropna(subset=["current_price", "market_cap"], inplace=True)

    print(df)

    
    plt.figure(figsize=(8, 5))
    plt.bar(df["name"], df["current_price"], color="skyblue")
    plt.title("Top 10 Cryptocurrency Prices (USD)")
    plt.xlabel("Cryptocurrency")
    plt.ylabel("Price in USD")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("crypto_prices.png")
    plt.show()  

    plt.figure(figsize=(8, 8))
    plt.pie(df["market_cap"], labels=df["name"], autopct="%1.1f%%", startangle=140)
    plt.title("Top 10 Cryptocurrencies by Market Cap")
    plt.tight_layout()
    plt.savefig("crypto_market_cap.png")
    plt.show()  

    print("Charts saved: crypto_prices.png, crypto_market_cap.png")

except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")

except KeyError as e:
    print(f"Missing expected column: {e}")

except ValueError as e:
    print(f"Error processing API data: {e}")
