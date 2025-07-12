import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


df = pd.read_csv("superstore.csv", encoding='ISO-8859-1')  # Adjust path if needed

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
df.dropna(subset=['Order Date', 'Sales'], inplace=True)
df.drop_duplicates(inplace=True)


q = df['Sales'].quantile(0.99)
df = df[df['Sales'] <= q]

df['Month_Year'] = df['Order Date'].dt.to_period('M')
df['Month_Year_str'] = df['Month_Year'].astype(str)
df['Month_Year_dt'] = pd.to_datetime(df['Month_Year_str'])


monthly_avg = df.groupby('Month_Year')['Sales'].mean().reset_index()
monthly_avg.columns = ['Month_Year', 'Avg_Sales']
df = pd.merge(df, monthly_avg, on='Month_Year', how='left')

df['Month'] = df['Order Date'].dt.month
df['Is_Holiday_Season'] = df['Month'].apply(lambda x: 1 if x in [11, 12] else 0)

monthly_sales = df.groupby(['Month_Year', 'Category'])['Sales'].sum().reset_index()
monthly_sales['Lag_1'] = monthly_sales.groupby('Category')['Sales'].shift(1)
df = pd.merge(df, monthly_sales[['Month_Year', 'Category', 'Lag_1']],
              on=['Month_Year', 'Category'], how='left')

rolling_df = df.groupby(['Category', 'Month_Year_dt'])['Sales'].sum().reset_index()
rolling_df['Rolling_3_Month'] = rolling_df.groupby('Category')['Sales'].rolling(3).mean().reset_index(0, drop=True)
df = pd.merge(df, rolling_df[['Month_Year_dt', 'Category', 'Rolling_3_Month']],
              on=['Month_Year_dt', 'Category'], how='left')


sales_monthly = df.groupby('Month_Year_dt')['Sales'].sum().reset_index()
sales_monthly.columns = ['ds', 'y']

train = sales_monthly[:-6]
test = sales_monthly[-6:]

model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
model.fit(train)

future = model.make_future_dataframe(periods=6, freq='M')
forecast = model.predict(future)

combined = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].merge(sales_monthly, on='ds', how='left')
combined.columns = ['Date', 'Forecast_Sales', 'Lower_Bound', 'Upper_Bound', 'Actual_Sales']


actual = test['y'].values
predicted = forecast[-6:]['yhat'].values
mae = mean_absolute_error(actual, predicted)
rmse = np.sqrt(mean_squared_error(actual, predicted))
print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}")


sns.set(style="whitegrid")


plt.figure(figsize=(12, 6))
plt.plot(combined['Date'], combined['Actual_Sales'], label='Actual Sales', color='royalblue', linewidth=2)
plt.plot(combined['Date'], combined['Forecast_Sales'], label='Forecasted Sales', color='orange', linestyle='--', linewidth=2)
plt.fill_between(combined['Date'], combined['Lower_Bound'], combined['Upper_Bound'], color='orange', alpha=0.2, label='Confidence Interval')
plt.title('📈 Forecast vs Actual Sales', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.tight_layout()
plt.show()


combined['Error'] = combined['Actual_Sales'] - combined['Forecast_Sales']
plt.figure(figsize=(12, 4))
sns.lineplot(x='Date', y='Error', data=combined, marker='o', color='crimson')
plt.axhline(0, linestyle='--', color='gray')
plt.title('🧮 Forecast Residuals (Error = Actual - Forecast)', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Error')
plt.tight_layout()
plt.show()


future_only = combined[combined['Actual_Sales'].isna()]
plt.figure(figsize=(10, 5))
plt.plot(future_only['Date'], future_only['Forecast_Sales'], label='Forecast', color='green', marker='o')
plt.fill_between(future_only['Date'], future_only['Lower_Bound'], future_only['Upper_Bound'], color='green', alpha=0.2, label='Confidence Interval')
plt.title('🔮 Future Sales Forecast (Next 6 Months)', fontsize=15)
plt.xlabel('Date')
plt.ylabel('Forecasted Sales')
plt.legend()
plt.tight_layout()
plt.show()


model.plot_components(forecast)
plt.tight_layout()
plt.show()
