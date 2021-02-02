FROM cloudera/quickstart:latest

COPY CentOS-Base.repo /etc/yum.repos.d/

RUN yum -y install epel-release
RUN yum -y install sqlite-devel
RUN yum -y update curl && cd /usr/src && \
 curl -1 https://www.python.org/ftp/python/3.5.9/Python-3.5.9.tgz -o Python-3.5.9.tgz && \
 tar xzf Python-3.5.9.tgz && \
 cd Python-3.5.9 && \
 ./configure --enable-loadable-sqlite-extensions && \
 make altinstall

RUN yum -y install gcc-c++ freetype-devel libpng-devel atlas-devel blas-devel pandoc ; yum clean all

#RUN pip3.5 install -U pip

RUN pip3.5 install -U jupyter nano
RUN pip3.5 install -U py4j

COPY requirements.txt ./
RUN pip3.5 install -r requirements.txt 

RUN  ln -s /etc/hive/conf/hive-site.xml /etc/spark/conf

ENV SPARK_HOME /usr/lib/spark
ENV PYSPARK_PYTHON python3.5
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.9-src.zip

WORKDIR /workspace
