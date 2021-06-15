FROM apache/airflow:2.0.0-python3.7

USER root

# Install OpenJDK-11
RUN apt update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

USER airflow

COPY ./requirements.txt /requirements.txt

RUN pip install apache-airflow-providers-apache-spark
RUN pip install -r /requirements.txt -U
