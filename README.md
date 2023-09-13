
# Sales Analytics for Eco-Friendly Products 

Welcome to the EcoMarket Sales Analysis project! This repository contains Python code that extracts data from a cloud source, performs data transformation and analysis, and loads the results into an Amazon Redshift database. In this README, we'll provide an overview of the project, its functionality, and how to use it.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Data Transformation](#data-transformation)
- [Analysis](#analysis)
- [Loading Data into Amazon Redshift](#loading-data-into-amazon-redshift)
- [Contributing](#contributing)
- [License](#license)


## Introduction

EcoMarket is a sustainable products retailer, and this project aims to analyze its sales data to derive valuable insights. The project is divided into several steps:

1. Data Extraction: Data is extracted from a cloud source (Amazon S3) containing sales and customer profiles data.

2. Data Transformation: The extracted data is transformed to prepare it for analysis. This includes date format conversion and calculations.

3. Analysis: Two main analyses are performed:

	• Calculation of total sales revenue generated from sustainable products each month in the year 2022.
	
	• Identification of the top five customer segments that contribute the most to EcoMarket's revenue in 2022.
	
4. Loading Data into Amazon Redshift: The transformed data is loaded into an Amazon Redshift database for further reporting and analysis.





## Prerequisites

Before using this project, ensure you have the following prerequisites:

Before using this project, ensure you have the following prerequisites:
• Python 3.x

• Boto3 (for AWS S3 interaction)

• Pandas (for data manipulation)

• Pyodbc (for connecting to Amazon Redshift)

• An Amazon Redshift instance with proper credentials and a DSN configured.

• Access to an Amazon S3 bucket containing the required sales and customer profiles data.

## Project Structure

The project consists of a single Python script, ecomarket_cloud_project.py, which performs the data extraction, transformation, analysis, and loading steps.


├── ecomarket_cloud_project.py 

└── README.md

## Deployment

To use this project, follow these steps:

1. Install the required Python libraries using pip:

```bash
pip install boto3 pandas pyodbc
``` 

2. Configure your AWS credentials to access the S3 bucket. You can use AWS CLI or configure them directly in the script.

3. Update the script with the necessary S3 bucket name and file names to match your data sources.

4. Configure your Amazon Redshift connection by updating the dsn_name variable with your DSN name.

5. Run the script:
```bash
python ecomarket_cloud_project.py
```
## Data Transformation

In the data transformation step, the script performs the following transformations:

• Converts date columns to datetime objects.

• Calculates revenue for each sale.

• Extracts the month from the sale date.


## Analysis

The script performs two main analyses:

1. Total Sales Revenue by Month (2022): It calculates the total sales revenue generated from sustainable products each month in the year 2022.

2. Top Customer Segments: It identifies the top five customer segments that contribute the most to EcoMarket's revenue in 2022.


## Loading Data into Amazon Redshift

The script loads the transformed data into an Amazon Redshift table named "eco_sales_insights". It inserts the date, total sales revenue, and top customer segment for each month in 2022.

## Contributing

I welcome contributions to improve this project! If you have any ideas, bug fixes, or enhancements, please open an issue or create a pull request.
## License

Personal Project Disclaimer

This project is a personal endeavor and is not provided with any licensing or permission for external use. It is intended solely for personal, non-commercial purposes. No warranties or guarantees are provided, and the project creator assumes no liability for any issues or consequences arising from its use or misuse.

You may view, study, and learn from this project, but you may not copy, distribute, modify, or use it for any purpose other than personal exploration. If you wish to use or adapt any part of this project for any other purpose, please seek explicit permission from the project creator.

© Obinna Okorocha - 2023