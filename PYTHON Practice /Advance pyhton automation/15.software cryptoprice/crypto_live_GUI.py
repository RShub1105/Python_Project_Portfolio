import tkinter as tk
from tkinter import ttk
import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "inr",  # Currency set to INR
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

        # Clear old data in Treeview
        for row in tree.get_children():
            tree.delete(row)

        # Insert new data into Treeview
        for _, row in df.iterrows():
            tree.insert("", tk.END, values=(row["name"], row["current_price"], row["market_cap"], row["total_volume"]))

        # Auto-adjust column widths
        for col in columns:
            tree.column(col, width=tkFont.Font().measure(col) + 20)
            for item in tree.get_children():
                col_width = tkFont.Font().measure(tree.set(item, col)) + 20
                if tree.column(col, width=None) < col_width:
                    tree.column(col, width=col_width)


    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
    except KeyError as e:
        print(f"Missing expected column: {e}")
    except ValueError as e:
        print(f"Error processing API data: {e}")

    # Schedule auto-refresh every 60 seconds
    root.after(60000, fetch_data)


# Tkinter window setup
root = tk.Tk()
root.title("Crypto Price Dashboard")
root.geometry("700x400")

columns = ("Name", "Price (INR)", "Market Cap", "Total Volume")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill=tk.BOTH, expand=True)

# Manual refresh button
refresh_btn = tk.Button(root, text="Refresh Data", command=fetch_data)
refresh_btn.pack(pady=10)

# Auto-refresh every 60 sec
import tkinter.font as tkFont

fetch_data()
root.mainloop()
