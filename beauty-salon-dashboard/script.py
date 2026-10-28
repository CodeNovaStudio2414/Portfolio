import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Beauty_Salon_Portfolio_Dataset.xlsx')
df.columns = df.columns.str.strip()

service_col = [c for c in df.columns if 'service' in c.lower()][0]
price_col = [c for c in df.columns if any(w in c.lower() for w in ['price','amount','total','revenue','cost'])][0]

stats = df.groupby(service_col)[price_col].agg(['count','sum']).sort_values('sum', ascending=False)

fig, axes = plt.subplots(1,2, figsize=(14,6))
stats['count'].plot(kind='bar', ax=axes[0], color='skyblue')
axes[0].set_title('Bookings by Service')
stats['sum'].plot(kind='bar', ax=axes[1], color='salmon')
axes[1].set_title(f'Revenue - Total R{stats["sum"].sum():.2f}')
plt.tight_layout()
plt.savefig('salon_dashboard.png')
print("Dashboard saved!")
print(stats)
