import boto3
import pandas as pd

# Extracting data from cloud source
s3 = boto3.client('s3')

bucket_name = 'tenalytics-c9'
folder_name = 'data/'
file_names = ['sales_data.csv', 'customer_profiles.csv']

response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

for obj in response['Contents']:
    if obj['Key'].endswith(tuple(file_names)):
        s3.download_file(bucket_name, obj['Key'], obj['Key'].split('/')[-1])


# Creating dataframes
sales_df = pd.read_csv('sales_data.csv')
customer_df = pd.read_csv('customer_profiles.csv')


# Data transformation
sales_df['Sale_Date'] = pd.to_datetime(sales_df['Sale_Date'])
customer_df['Join_Date'] = pd.to_datetime(customer_df['Join_Date'])



# ## Calculating the total sales revenue generated from sustainable products each month for the year 2022.

# merging the two dataframes 
merged_df = pd.merge(sales_df, customer_df, on='Customer_ID')

# Filtering the merged_df based on the sustainable products, and creating a new dataframe
sustainable_products = ['Hydration', 'Apparel', 'Stationery']
sustainable_df = merged_df[merged_df['Product_Category'].isin(sustainable_products)]


# Extracting the month from the Sale_Date column and creating a new column for it
sustainable_df['Sale_Month'] = sustainable_df['Sale_Date'].dt.month


# creating the revenue column in the dataframe
sustainable_df['Revenue'] = sustainable_df['Price'] * sustainable_df['Quantity']

# Grouping the sustainable_df dataframe by months in 2022 and calculating the total sales revenue for each month, creating a new dataframe for monthly sales
monthly_total_sales_revenue = sustainable_df[sustainable_df['Sale_Date'].dt.year == 2022].groupby('Sale_Month')['Revenue'].sum()



# ## Identifying the top five customer segments that contribute the most to EcoMarket's revenue in 2022.

revenue_by_segment = sustainable_df[sustainable_df['Sale_Date'].dt.year == 2022].groupby('Customer_Segment')['Revenue'].sum()

top_5_segment = revenue_by_segment.sort_values(ascending=False).head(5)



# ## Creating the table "eco_sales_insights"

# Extracting the year and month from the Sale_Date column and creating a new column for it
sustainable_df['Date'] = sustainable_df['Sale_Date'].dt.strftime('%Y-%m')


# Grouping the data by month (Date column) for 2022 and Customer_Segment column, and calculating the total revenue
revenue_by_month_segment = sustainable_df[sustainable_df['Sale_Date'].dt.year == 2022].groupby(['Date', 'Customer_Segment'])['Revenue'].sum()


# Identifying the top customer segment that contributed the most to revenue by each month for 2022
top_segments = revenue_by_month_segment.groupby('Date').idxmax().reset_index()


# Renaming the columns of the top_segments dataframe
top_segments.columns = ['Date', 'Top_Customer_Segment']


# Removing the month and year from the Top_Customer_Segment column
top_segments['Top_Customer_Segment'] = top_segments['Top_Customer_Segment'].apply(lambda x: x[1])


# Calculating the total sales revenue generated from sustainable products in each month for 2022
total_revenue_by_month = sustainable_df[sustainable_df['Sale_Date'].dt.year == 2022].groupby('Date')['Revenue'].sum().reset_index()


# Renaming the columns of the total_revenue_by_month dataframe
total_revenue_by_month.columns = ['Date', 'Total_Sales_Revenue']


# merging the two dataframes on the Date column to create the eco_sales_insights table
eco_sales_insights = pd.merge(total_revenue_by_month, top_segments, on='Date')

df = eco_sales_insights



# ## Loading the transformed data into Amazon Redshift using pyodbc

import pyodbc

table_name = 'eco_sales_insights'
dsn_name = 'PostgreSQL35W'
conn = pyodbc.connect('DSN=' + dsn_name)
cursor = conn.cursor()

for index, row in df.iterrows():
    # Defining an INSERT INTO statement based on the table's columns
    sql_insert = f"INSERT INTO {table_name} (date, total_sales_revenue, top_customer_segment) VALUES (?, ?, ?)"
    
    # Extracting values from the DataFrame row
    values = (row['date'], row['total_sales_revenue'], row['top_customer_segment'])
    
    # Executing the INSERT statement
    cursor.execute(sql_insert, values)

# Committing the transaction
conn.commit()

# Closing the cursor and connection
cursor.close()
conn.close()