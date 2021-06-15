import numpy as np
import pandas as pd
import sqlalchemy
from typing import List

excel_path = (
    "C:/Users/Samuel/Google Drive/Proyectos/data_migration/CA1_Ecommerce_database.xlsx"
)


list_sheet = [
    "allevents",
    "allusers",
    "category",
    "date2008",
    "listings",
    "sales",
    "venue",
]


def create_dataframe_by_sheets(excel_path: str, sheet_name: List):
    df = pd.read_excel(excel_path, sheet_name=list_sheet)
    return df


for sheet in list_sheet:
    df = create_dataframe_by_sheets(excel_path=excel_path, sheet_name=sheet)


df = create_dataframe_by_sheets(excel_path, "allevents")
