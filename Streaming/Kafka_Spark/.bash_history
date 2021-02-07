ls
tar xf spark-3.0.1-bin-hadoop3.2.tgz -C /content/
cd /content/spark-3.0.1-bin-hadoop3.2/
ls
cd jars/
ls
wget -q https://github.com/masfworld/datahack_docker/raw/master/zeppelin/libs/libs-kafka_301.zip --directory-prefix=/content/spark-3.0.1-bin-hadoop2.7/jars/
unzip -n /content/spark-3.0.1-bin-hadoop2.7/jars/libs-kafka_301.zip -d /content/spark-3.0.1-bin-hadoop2.7/jars/
cd ..
cd ..
cd spark-3.0.1-bin-hadoop2.7/jars/
ls kaf*
ls *kaf*
ls *kafka*
exit
pip install psycopg2
python setup.py build_ext --pg-config /path/to/pg_config build ...
sudo pip install psycopg2 --user
apt update
apt install libpq-dev python3-dev
apt install libpq-dev python-dev
pip install psycopg2
ls
exit
