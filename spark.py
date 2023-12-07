# Import necessary libraries
import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col, coalesce

# Set environment variables for PySpark
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Create a Spark session
spark = SparkSession.builder \
    .appName("XMLDataLoadExample") \
    .config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.14.0") \
    .getOrCreate()

# Specify the path to the XML file
xml_file_path = "enwiki-latest-pages-articles.xml.bz2"

# Load XML data into a DataFrame
df = spark.read.format("xml").option("rowTag", "page").load(xml_file_path)

# Define a list of titles to filter
title_list = ["finals_champ"]

# Define a filter condition based on titles and case-insensitive search for hockey-related terms
filter_condition = col('title').contains("NHL season")

# Apply the filter to create a new DataFrame
filtered_df = df.filter(filter_condition).withColumnRenamed('title', 'season')

# Define regex patterns to extract information from the 'revision.text._VALUE' column
regex_pattern_winner = r'\|\sfinals_champ(?![^=]*_)\D*\[\[([^&<\n]+)\]\][^\n]'
regex_pattern_player = r'\|\stop_scorer(?![^=]*_)\s*=\s*([^(&<\n]+)'
regex_pattern_season = r'\|\sdraft_link\s=\s(\d+)'

# Extract information using regexp_extract and create a new DataFrame
result_df = filtered_df.withColumn("winner", F.regexp_extract('revision.text._VALUE', regex_pattern_winner, 1)) \
    .withColumn("player", F.regexp_extract('revision.text._VALUE', regex_pattern_player, 1)) \
    .withColumn("season", F.regexp_extract('revision.text._VALUE', regex_pattern_season, 1))

# Show the resulting DataFrame
result_df.show(n=1000)

# Read data from a CSV file into a DataFrame
csv_file_path = 'crawled_data.csv'
crawled_df = spark.read.option("delimiter", "\t").csv(csv_file_path, header=True)
crawled_df.show()

# Convert the "YEAR" column to string type
crawled_df = crawled_df.withColumn("YEAR", crawled_df["YEAR"].cast("string"))

# Select specific columns for joining
selected_columns = ["season", "winner", "player"]

# Perform a left outer join based on the "YEAR" and "season" columns
join_df = crawled_df.join(result_df.select(selected_columns), crawled_df["YEAR"] == result_df["season"], "left_outer")

# Show the resulting joined DataFrame
join_df.show(n=20000)

# Specify the output path for the joined DataFrame
output_path = "/data/joined_df.csv"

# Write the joined DataFrame to a CSV file with specified options
join_df.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").option("encoding", "UTF-8").csv(output_path)
