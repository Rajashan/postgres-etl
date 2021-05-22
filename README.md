# ETL pipeline project

This project outlines a postgres based ETL pipeline for the fictional company sparkify. The data originates in two folders of json files. One is composed of data on songs and the other of log data from the fictional service. 

## Running the code

To populate the database, run the following in succession:

    python create_tables.py
    python etl.py

## Additional info

Data can be explored and tested in the accompanying jupyter notebooks. 