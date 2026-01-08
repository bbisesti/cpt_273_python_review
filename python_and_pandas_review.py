#%% Import necessary libraries

# SQL Alchemy for database connection
from sqlalchemy import create_engine

# Pandas for Data Manipulation
import pandas as pd

# Dotenv and os for loading environment variables
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

#%% Set up database connection
db_user = os.getenv("db_user")
db_pass = os.getenv("db_pass")
db_port = os.getenv("db_port")
db_db = os.getenv("db_db")
db_host = os.getenv('db_host')

# Create PostgreSQL connection string
connection_string = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_db}"

# Create database connection engine
engine = create_engine(connection_string)

#%%
# Query data from the database

# PostgreSQL query to fetch data
query = "SELECT * FROM electricity.usage_data;"

# Collect data into DataFrame
df = pd.read_sql(query, engine)

# Print the first few rows of the DataFrame
df.head()

#%% Data Manipulation with Pandas

'''

Assignment Starts HERE

Your Assignment is to complete the following tasks using Pandas.  

You will then group all of these numbers into a single Dictionary with the following layout:

summary_dict = {
    "total_overall_usage": <value>,
    "monthly_usage": {
        "YYYY-MM": <value>,
        ...
    },
    "highest_month": {
        "month": "YYYY-MM",
        "usage": <value>
    },
    "highest_hourly_average": {
        "hour": <value>,
        "average_usage": <value>
    }
}
'''


# Task One: Calculate total overall usage (sum kwh)

# Task Two: Group by month and sum overall_usage (sum kwh by month and year)

# Task Three: Find the month with the highest overall usage

# Task Four: Find the Hour of the day with the highest average overall usage


# Finally: Fill out and print the summary dictionary


summary_dict = {
    "total_overall_usage": None,
    "monthly_usage": {},
    "highest_month": {
        "month": None,
        "usage": None
    },
    "highest_hourly_average": {
        "hour": None,
        "average_usage": None
    }
}
print(summary_dict)

# Assignment Bonus (Optional - 10 points):
# Using Pandas, create a line plot that shows the trend of overall usage over time (by month).

# Assignment Easter Egg (Optional - 5 points):
# Why would we not be able to compare these values year over year?

'''

    Assignment Ends Here

'''