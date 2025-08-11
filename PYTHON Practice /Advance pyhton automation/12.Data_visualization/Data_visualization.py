import pandas as pd 
import matplotlib.pyplot as plt

data = {
    "Month": ["JAN","FEB","MAR","APR","MAY","JUNE","JULY","AUG"],
    "Sales": [200,250,300,280,350,400,450,500]

}
df = pd.DataFrame(data)
df.to_csv('sales.csv',index=False)
print("☑️ Sales.Csv Created")
sales_data = pd.read_csv('sales.csv')
print ("Data from sales.csv")
print (sales_data)

plt.figure(figsize=(8, 5))
plt.plot(sales_data['Month'], sales_data['Sales'], marker='o', linestyle='-', color='blue')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.savefig('sales_chart.png')
plt.close()

print("📊 Chart saved as sales_chart.png.")

