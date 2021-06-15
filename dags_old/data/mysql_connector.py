import sqlalchemy
from sqlalchemy import create_engine


# user = "admin"
# password = "06049084j"
# host = "database-2.c9uodnq6xba6.eu-west-3.rds.amazonaws.com"
# port = "3306"


class MysqlConnection(object):
    def __init__(
        self, user: str, password: str, host: str, port: str, database: str
    ) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def create_sqlalchemy_engine(self):
        uri = f"mysql+pymysql://{self.user}@p{self.password}@{self.host}:{self.port}/{self.database}"
        engine = create_engine(uri, echo=False)
        return engine
