# ETL pipeline project

## Introduction

This project outlines a postgres based ETL pipeline for the fictional company sparkify. The data originates in two folders of json files. One is composed of data on songs and the other of log data from the fictional service. The code is designed to help sparkify load in data from multiple sources and aggregate them into a postgres database, constructed in accordance with a star schema. 

## Files

    --data
    --create_tables.py
    --etl.ipynb
    --etl.py
    --README.md
    --sql_queries.py
    --test.ipynb


## Running the code

To populate the database, run the following in succession:

    python create_tables.py
    python etl.py

## Additional info

Data can be explored and the etl pipeline can be executed for a single row of data in ´etl.ipynb´. The full pipeline is run using ´etl.py´. ´test.ipynb´ is used to test the resulting database. ´sql_queries.py´ contains sql statements and ´create_tables.py` is responsible for running the queries using psycopg2.  