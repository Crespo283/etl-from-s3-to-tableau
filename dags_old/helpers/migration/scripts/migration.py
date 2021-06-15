import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine

list_sheet = [
    "allevents",
    "allusers",
    "category",
    "date2008",
    "listings",
    "sales",
    "venue",
]


def create_dataframe_by_sheets(excel_path: str, sheet_name: str):
    df = pd.read_excel(excel_path, sheet_name=list_sheet)
    return df
