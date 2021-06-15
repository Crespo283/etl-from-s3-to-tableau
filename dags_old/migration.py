from data.mysql_connector import MysqlConnection
from helpers.migration.scripts.migration import create_dataframe_by_sheets

mysql_conn = MysqlConnection(
    user="admin",
    password="06049084j",
    host="database-2.c9uodnq6xba6.eu-west-3.rds.amazonaws.com",
    port="3306",
    database="samuel",
)

engine = mysql_conn.create_sqlalchemy_engine()

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


def main():

    for sheet in list_sheet:
        df = create_dataframe_by_sheets(excel_path=excel_path, sheet_name=sheet)
        df.to_sql(
            sheet,
            con=engine,
            schema=mysql_conn.database,
            index=False,
            if_exists="replace",
        )


if __name__ == "__main__":
    main()