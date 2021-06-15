import io
import os

import boto3
import pandas as pd


AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")


s3c = boto3.client(
    "s3",
    region_name="us-east-2",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)
obj = s3c.get_object(
    Bucket="migrationawsbucket", Key="ecomerce_folder/CA1_Ecommerce_database.xlsx"
)


def mains3():
    for sheet in obj:
        df = pd.read_excel(
            io.BytesIO(obj["Body"].read()), encoding="utf8", sheet_name=sheet
        )


if __name__ == "__mains3__":
    mains3()
