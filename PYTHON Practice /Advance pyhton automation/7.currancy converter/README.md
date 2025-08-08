
# Currency Converter (CLI)

A simple and interactive command-line currency converter written in Python. It uses real-time exchange rates powered by the ExchangeRate API.

## Features

✅ Convert any currency to another using live exchange rates

✅ User-friendly CLI with colored prompts

✅ Error handling for invalid input and API issues

## ⚙️ How to Use

bash

-     Copy Edit python currency_convertor.py
    You'll be prompted to enter:

The base currency code (e.g., USD)

The target currency code (e.g., INR)

The amount to convert

Example:

vbnet
Copy
Edit
From (currency code, e.g.,USD): USD  
To (currency code, e.g.,INR): INR  
Amount: 100  
## 🔐 API Key


This project uses the ExchangeRate API.
You must replace the default API_KEY with your own for production use:

-   python Copy Edit
-     Api_key = "your-api-key-here"
-     Sign up at exchangerate-api.com to get a free key.


## Known Limitations

-  Limited number of requests on free API tier

-  No GUI (CLI-only)

-  API key is hardcoded — consider using environment variables for better security.


## License

[MIT](https://choosealicense.com/licenses/mit/)

