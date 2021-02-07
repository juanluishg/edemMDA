FROM jupyter/pyspark-notebook
USER root
RUN sudo apt update -y
RUN sudo apt-get install openjdk-8-jdk-headless -qq > /dev/null
RUN apt install libpq-dev python3-dev
RUN wget https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz
RUN mkdir /content
RUN tar xf spark-3.0.1-bin-hadoop2.7.tgz -C /content/
RUN sudo wget -q https://github.com/masfworld/datahack_docker/raw/master/zeppelin/libs/libs-kafka_301.zip --directory-prefix=/content/spark-3.0.1-bin-hadoop2.7/jars/
RUN sudo unzip -n /content/spark-3.0.1-bin-hadoop2.7/jars/libs-kafka_301.zip -d /content/spark-3.0.1-bin-hadoop2.7/jars/