import tkinter as tk
from tkinter import ttk
import requests
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use("TkAgg")

API_KEY= "fee7d994eb5be5cdc01be0a4d71595e9"
def fetch_weather():
    cities = ["Delhi","Mumbai","Bangalore","Chennai","Kolkata","Coimbatore","Kerala","Jamshedpur"]
    weather_data = []
    
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()
            weather_data.append({"City":city,"Temperature(℃)":data["main"]["temp"],"Humidity(%)":data["main"]["humidity"],"Condition":data["weather"][0]["description"]})
        except Exception as e:
            print(f"Error fetching {city}: {e}")
    
    df = pd.DataFrame(weather_data)

    for row in tree.get_children():
        tree.delete(row)
    for _,row in df.iterrows():
        tree.insert("",tk.END,values=(row["City"],row["Temperature(℃)"],row["Humidity(%)"],row["Condition"]))

    fig1, ax1 = plt.subplots(figsize=(6, 4))
    ax1.bar(df["City"], df["Temperature(℃)"], color="skyblue")
    ax1.set_title("City Temperature Comparison")
    ax1.set_ylabel("Temperature (℃)")
    plt.xticks(rotation=45)
    fig1.tight_layout()
    fig1.savefig("temperature_chart.png")  

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.bar(df["City"], df["Humidity(%)"], color="orange")
    ax2.set_title("City Humidity Comparison")
    ax2.set_ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    fig2.tight_layout()
    fig2.savefig("humidity_chart.png") 


    for widget in chart_frame.winfo_children():
        widget.destroy()  # Clear old charts

    canvas1 = FigureCanvasTkAgg(fig1, master=chart_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    canvas2 = FigureCanvasTkAgg(fig2, master=chart_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    root.after(60000, fetch_weather)

root = tk.Tk()
root.title("Global Weather Dashboard")
root.geometry("700x400")

columns = ("City","Temperature(℃)","Humidity(%)","Condition")
tree = ttk.Treeview(root,columns=columns,show="headings")
for col in columns:
    tree.heading(col,text=col)
tree.pack(fill=tk.BOTH,expand=True)
refresh_btn = tk.Button(root,text="REFRESHn DATA",command=fetch_weather)
refresh_btn.pack(pady=10)

chart_frame = tk.Frame(root)
chart_frame.pack(fill=tk.BOTH, expand=True)

import tkinter.font as tkFont
fetch_weather()
root.mainloop()
