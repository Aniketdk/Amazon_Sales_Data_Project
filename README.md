# 🧊 Amazon Sales Data Engineering Project – Snowflake x Power BI

A complete end-to-end **Data Engineering Project** built using **Snowflake**, **Python**, and **Power BI** with a **modern gradient dashboard** design.  
This project demonstrates how to build a data pipeline for Amazon sales analytics — from raw CSV to cleaned insights and visual dashboards.

---

## 🚀 Project Overview

This project shows a real-world data flow:
1. **Data Ingestion** → Load Amazon sales data from CSV into Snowflake.
2. **Data Cleaning & Transformation** → Using SQL and Python to remove duplicates, handle nulls, and normalize columns.
3. **Data Modeling** → Create curated tables for analytics (Sales, Products, Regions, Profit).
4. **Data Visualization** → Build a Power BI dashboard with a modern gradient theme.
5. **Automation** → Optional GitHub Actions or scheduling can be added for continuous refresh.

---

## 🧱 Architecture

```text
+---------------------+
|  Amazon Sales Data  |
|   (CSV Source)      |
+----------+----------+
           |
           v
+---------------------+
|  Snowflake Stage    |
|  (Raw Layer)        |
+----------+----------+
           |
           v
+---------------------+
|  Cleaning Pipeline  |
|  (Python + SQL)     |
+----------+----------+
           |
           v
+---------------------+
|  Snowflake Curated  |
|  (Clean Layer)      |
+----------+----------+
           |
           v
+---------------------+
|  Power BI Dashboard |
|  (Modern Gradient)  |
+---------------------+
📂 Docs: Architecture visuals available in docs/architecture_flow.png and docs/full_architecture.png.

🧮 Tech Stack
Layer	Technology
Data Source	Amazon Sales CSV
Data Warehouse	Snowflake
Transformation	Python + SQL
Visualization	Power BI
Version Control	GitHub

🧰 Project Structure
pgsql
Copy code
amazon-sales-snowflake-project-gradient/
│
├── data/
│   └── amazon_sales_data.csv
│
├── sql/
│   └── amazon_sales_cleaning_pipeline.sql
│
├── python/
│   ├── amazon_sales_cleaning_pipeline.py
│   └── amazon_sales_etl.py
│
├── docs/
│   ├── architecture_flow.png
│   └── full_architecture.png
│
├── dashboard/
│   ├── Amazon_Sales_Dashboard.pbix
│   ├── modern_theme.json
│   ├── dashboard_design_guide.md
│   ├── preview_1.png … preview_5.png
│   └── powerbi_notes.txt
│
└── README.md
🧹 Data Cleaning Steps
Step	Action
1	Removed null & duplicate rows
2	Standardized column names
3	Converted data types (date, numeric)
4	Trimmed extra spaces & special characters
5	Validated key metrics consistency

📊 Power BI Dashboard
Multi-page dashboard with a modern gradient theme (Violet, Aqua, Peach):

🏠 Overview – KPIs, Sales Summary, Profit %

🛍️ Products – Top Products, Category Profit

🌍 Region – Regional Performance Map

📆 Trends – Monthly Sales & Growth

📈 Profit – Margin Distribution & Insights

Dashboard Previews
(All previews in /dashboard/)

Overview	Products	Region	Trends	Profit

⚙️ How to Run
1️⃣ Clone this Repository
bash
Copy code
git clone https://github.com/<your-username>/amazon-sales-snowflake-project.git
cd amazon-sales-snowflake-project
2️⃣ Setup Snowflake
Create database & schema.

Execute SQL script:

sql
Copy code
RUN amazon_sales_cleaning_pipeline.sql;
3️⃣ Run Python ETL (optional)
bash
Copy code
python python/amazon_sales_etl.py
4️⃣ Open Power BI Dashboard
Import amazon_sales_data.csv or connect live to Snowflake.

Apply modern_theme.json (View → Themes → Browse for themes).

📈 Key Insights
📦 Top products and categories by total sales.

🌍 Regional contribution to revenue.

📆 Seasonal and monthly sales trends.

💰 Profit margin distribution across products.

⚡ Clean pipeline ready for automation or scheduling.

📄 Future Improvements
Add GitHub Actions CI/CD to deploy SQL changes automatically.

Enable Snowpipe for real-time ingestion.

Add Power BI service refresh automation.

🙌 Acknowledgements
This project is built for portfolio showcasing data engineering and visualization skills using Snowflake and Power BI.
