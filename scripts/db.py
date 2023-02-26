# Import libraries
import sqlalchemy as sql
from sqlalchemy import create_engine
import pandas as pd


# Write dataframe to database

def insert_data(df: pd.DataFrame, table_name: str, db_uri: str) -> None:
    """
    Inserts a pandas DataFrame into a specified table in a PostgreSQL database.

    Args:
        df (pd.DataFrame): The pandas DataFrame to be inserted into the database.
        table_name (str): The name of the table to insert the data into.
        db_uri (str): The database URI in the format 'postgresql://user:password@host:port/database'.
    """
    
    df.to_sql(name= table_name, schema="sa", con= db_uri, if_exists='append', index=False)
    
   
