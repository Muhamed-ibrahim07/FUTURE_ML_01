# 🛍️ Retail Sales Forecasting Dashboard

This project is part of a real-world ML internship task at Future Intern. It focuses on building a predictive analytics solution to **forecast future retail sales** using historical transaction data, machine learning models, and an interactive dashboard built in Power BI.

---

## 📦 Project Overview

We aim to help retail businesses anticipate future sales patterns and make informed decisions on inventory, marketing, and operations.

**Key Outputs:**
- Machine Learning-based sales forecasts (Prophet)
- Confidence intervals for prediction
- Interactive visualizations in Power BI
- Business recommendations based on trends

---

## 🛠️ Tools & Technologies

- **Python**: Data preprocessing, time series modeling
- **Facebook Prophet**: Forecasting model
- **Pandas, Matplotlib, Seaborn**: Data handling & visualizations
- **Power BI**: Dashboard and storytelling
- **Git & GitHub**: Version control and documentation

---

## 🔁 Project Workflow

### 📌 Phase 1: Data Preparation
- Loaded and cleaned historical retail sales data (Superstore dataset)
- Engineered features: `Month`, `Year`, `Quarter`, etc.

### 📌 Phase 2: Forecasting Model
- Used **Prophet** to build a time series model
- Evaluated forecast with RMSE, MAE
- Exported predictions to CSV for Power BI

### 📌 Phase 3: Dashboard Creation (Power BI)
- Visuals built:
  - Line chart: Forecast vs Actual Sales
  - Bar charts: Yearly & Monthly comparisons
  - Table view: Quarter-wise breakdown
  - Cards: KPI summaries
  - Slicers: Month, Year, Quarter filters

---

## 📈 Key Insights from Dashboard

- 🔹 **Forecast Overestimation**: The forecasted total sales (~1.78M) exceeded actual sales (~1.44M) by ~24%.
- 🔹 **Seasonal Spikes**: December, November, and September showed significantly higher actual sales — indicating strong Q4 performance.
- 🔹 **Year 2017 Underperformance**: Despite optimistic forecasts, 2017 sales were the lowest, requiring deeper root-cause analysis.
- 🔹 **Strong Q4 Sales Trend**: Majority of sales happened in Qtr 4 across all years (Oct–Dec).

---

## 💡 Recommendations

- ✅ **Recalibrate forecast model** to better adapt to seasonal dips and overestimations (especially in Q1 and Q2).
- ✅ **Focus inventory and marketing in Q4** to leverage peak sales months (Nov–Dec).
- ✅ **Investigate 2017 drop** — consider external factors or internal operational issues that impacted performance.
- ✅ **Monitor KPI deviations** using Power BI cards and apply alert thresholds if actual sales deviate by >15% from forecast.

---

## 📁 Deliverables

| File | Description |
|------|-------------|
| `sales_forecast_powerbi.csv` | Forecast output ready for Power BI |
| `SalesForecastDashboard.pbix` | Power BI interactive report |
| `forecast_model.py` | Python code for model building |
| `README.md` | Project overview and documentation |
| `requirements.txt` | Python dependencies |

---

## 🚀 How to Run

1. Clone the repo
2. Run `forecast_model.py` to generate forecast data
3. Open `SalesForecastDashboard.pbix` in Power BI Desktop
4. Explore insights, filter by month/year, and export reports

---

## 📌 Author
**Muhamed Ibrahim** – Machine Learning Intern at Future Intern

---

⭐️ If you found this helpful, feel free to star the repository!
