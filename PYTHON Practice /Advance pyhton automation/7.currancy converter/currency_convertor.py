import requests
from colorama import Fore, Style, init

Api_key = "cf849e7eb31bd92f1d5c39a0"
BASE_URL = "https://v6.exchangerate-api.com/v6"

def convert_currency(base,target,amount):
    url = f"{BASE_URL}/{Api_key}/latest/{base.upper()}"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(Fore.RED + "Api error:", data.get("error type","Unknown error"))
            return
        rate = data["conversion_rates"].get(target.upper())
        if not rate:
            print("Traget Currency Not found!")
            return
        result = amount * rate
        print(f"\n{amount}{base.upper()} = {result:.2f}{target.upper()}")
    except Exception as e :
        print("Error:",str(e))

while True:
    print(Style.BRIGHT + "\n*** Currency Converter ***")
    base = input(Fore.CYAN +"From (currency code, e.g.,USD):")
    target = input(Fore.MAGENTA+"To (currency code . e.g.,INR):")
    try:
        amount = float(input(Fore.YELLOW+"Amount:"))
    except ValueError:
        print("please enter a valid number.")
        continue
    convert_currency(base,target,amount)

    again = input(Style.BRIGHT + "Do you want to convert another?(y/n):")
    if again.lower()!='y':
        print(Fore.WHITE +"""Exiting.👋🏻 \nThank you""")
        break