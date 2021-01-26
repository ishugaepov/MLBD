FROM cloudera/quickstart:latest

# RUN yum install -y https://repo.ius.io/ius-release-el6.rpm

RUN yum install https://repo.ius.io/ius-release-el7.rpm https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

RUN yum install -y python35u python35u-pip python35u-devel
RUN yum -y install gcc-c++ freetype-devel libpng-devel atlas-devel blas-devel pandoc ; yum clean all

RUN pip3.5 install -U pip
RUN pip3.5 install -U jupyter nano
RUN pip3.5 install -U py4j

COPY requirements.txt ./
RUN pip3.5 install -r requirements.txt 

RUN  ln -s /etc/hive/conf/hive-site.xml /etc/spark/conf

ENV SPARK_HOME /usr/lib/spark
ENV PYSPARK_PYTHON python3.5
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.9-src.zip

WORKDIR /workspace
