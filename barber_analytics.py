import pandas as pd
import matplotlib.pyplot as plt

# Sample data - replace with your barber's real data later
data = {
      'Date' : ['2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23', '2026-10-24'],
    'Service' : ['Freehand lines', 'Fade', 'Braids', 'Freehand lines', 'Fade'],
    'Price' : [150, 100, 250, 150, 100],
    'Client_Type' : ['Regular', 'New', 'Regular', 'New', 'Regular']

}

df = pd.DataFrame(data)

# Analysis - this is what clients pay for
print("--- Barber Business Insights ---")
print(f"Total Income: R{df['Price'].sum()}")
print(f"Busiest Service: {df['Service'].mode()[0]}")
print("\nAverage per day:")
print(df.groupby('Date')['Price'].sum())

# Simple chart
df.groupby('Service')['Price'].sum().plot(kind='bar')
plt.title('Income by Service - Pretoria Barber')
plt.ylabel('Rands')
plt.savefig('barber_income.png')
plt.show()
