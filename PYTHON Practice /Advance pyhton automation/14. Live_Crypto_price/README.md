
# 📊 Crypto Price & Market Cap Visualizer

This Python script fetches real-time cryptocurrency data from the CoinGecko API and creates two charts:

     1. Bar chart → showing current prices of the top 10 cryptocurrencies (in USD).

     2. Pie chart → showing each coin’s share of the total market cap.

Both charts are saved as .png files and displayed on screen.


## Features

- Live crypto data from CoinGecko API.

- Top 10 coins by market capitalization.

- Automatically cleans missing values to avoid chart errors.

- Saves charts as:

-     crypto_prices.png

-     crypto_market_cap.png

- Error handling for API failures or missing data.


## Output

- Bar Chart: Top 10 Cryptocurrency Prices in USD.

- Pie Chart: Market Cap Distribution.
## Note

- Requires an internet connection to fetch live data.

- CoinGecko has free rate limits — avoid running the script too often in a short time.

- If you get a "cannot convert float NaN" error, it means the API returned missing  values (the script already drops these automatically).

## License

Free to use and modify for personal or educational projects [MIT](https://choosealicense.com/licenses/mit/).

