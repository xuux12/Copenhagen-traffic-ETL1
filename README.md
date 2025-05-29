# 🚦 Copenhagen Traffic Congestion ETL Project (AWS Cloud)

## 📌 Project Summary

This project builds a data engineering pipeline for monitoring and analyzing traffic congestion in Copenhagen using AWS cloud services. It covers ingestion, cataloging, transformation, querying, and visualization of traffic data.

## ☁️ AWS Services Used

- **Amazon S3** – Store raw and processed traffic data
- **AWS Glue Crawler** – Automatically detect schema from CSV files
- **AWS Glue Job (PySpark)** – Clean and transform traffic data
- **Amazon Athena** – Query traffic data using SQL
- **Amazon QuickSight** – Visualize congestion levels by location and time

## 🧱 Architecture

1. CSV files uploaded to S3
2. Glue Crawler catalogs schema into Glue Data Catalog
3. Glue ETL Job transforms and cleans the data
4. Processed data stored in a new S3 path
5. Athena queries the cleaned data
6. QuickSight builds dashboards from Athena output

(📸 Architecture diagram: `docs/architecture.png` - add manually)

## 🔁 ETL Pipeline Steps

1. Upload raw traffic data to S3
2. Use Glue Crawler to catalog data into `traffic_db`
3. Glue Job drops nulls and formats timestamps
4. Store cleaned data to `s3://<your-bucket>/processed/`
5. Query data in Athena
6. Build dashboard in QuickSight

## 📊 Sample Queries (Athena)

```sql
SELECT location, AVG(congestion_level) as avg_congestion
FROM traffic_db.cleaned_traffic_data
GROUP BY location
ORDER BY avg_congestion DESC;
```

## 📸 Screenshots

Add screenshots in `docs/screenshots/`:
- S3 Upload
- Glue Crawler
- Glue Job Script
- Athena Query
- QuickSight Dashboard

## 🚀 How to Run

1. Clone this repo
2. Upload the sample CSV to your S3 bucket
3. Follow README steps to recreate pipeline
4. Use Athena + QuickSight for analysis

## 🎓 What I Learned

- How to design cloud-based ETL with AWS Glue
- PySpark for data cleaning
- Serverless querying with Athena
- Building dashboards with QuickSight

---
