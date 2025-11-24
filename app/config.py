class Config:
    SQL_SERVER = 'localhost'
    SQL_DATABASE = 'crud'
    SQL_USER = 'sa'
    SQL_PASSWORD = '2002'

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER}:{SQL_PASSWORD}@{SQL_SERVER}/{SQL_DATABASE}?"
        "driver=ODBC+Driver+17+for+SQL+Server"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "super_secret_key"
    JWT_ACCESS_TOKEN_EXPIRES = 3600
