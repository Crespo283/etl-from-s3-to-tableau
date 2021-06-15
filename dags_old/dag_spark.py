from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.email import EmailOperator

from datetime import datetime, timedelta
import csv
import requests
import json

from spark_test import test_spark


default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def printar():
    print("success!")


with DAG(
    "samuel",
    start_date=datetime(2021, 1, 1),
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
) as dag:

    downloading_rates = PythonOperator(task_id="test1", python_callable=printar)
    # dos = PythonOperator(task_id="test2", python_callable=test_spark)
    operator = SparkSubmitOperator(
        task_id="spark_submit_job",
        conn_id="spark_conn",
        application="/opt/airflow/dags/test.py",
        total_executor_cores="1",
        executor_cores="1",
        executor_memory="2g",
        num_executors="1",
        name="airflow-spark1",
        verbose=False,
        driver_memory="2g",
        conf={
            "spark.master": "spark://spark-master:7077",
            # "spark.dynamicAllocation.enabled": "false",
            # "spark.shuffle.service.enabled": "false",
            # "spark.driver.port": "8083",
            # "spark.blockManager.port": "51814",
        },
    )

    downloading_rates >> operator


# forex_processing = SparkSubmitOperator(
#     task_id="spark1",
#     application="/opt/airflow/dags/test.py",
#     conn_id="spark_conn",
#     executor_cores=1,
#     executor_memory="512m",
#     driver_memory="512m",
#     driver_cores=1,
#     verbose=False,
# )
