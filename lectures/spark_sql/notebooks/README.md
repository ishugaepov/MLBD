## Ten easy steps to update your spark

In order to use `Spark SQL` we need to install recent version of spark.

0. Shutdown Jupyter

#### Update java

1. `sudo yum -y remove java`
2. `sudo yum install -y java-1.8.0-openjdk`
3. `export JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk.x86_64`

Optionaly you can install nano: `yum install -y nano`

#### Update spark

4. Download [spark-2.4.*](http://spark.apache.org/downloads.html) (Choose spark version 2.4 and pre-build for Apache Hadoop 2.6)
5. `tar -xvf spark-2.4.*-bin-hadoop2.6.tgz`
6. `sudo mv spark-2.4.*-bin-hadoop2.6 /usr/local/spark`

#### Update paths

7. In the following files `/usr/bin/pyspark, /usr/bin/spark-shell, /usr/bin/spark-submit` change `/usr/lib/spark` to `/usr/local/spark` 
8. `export SPARK_HOME=/usr/local/spark`
9. `export PATH=$SPARK_HOME/bin:$PATH`
10. `export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip`


Now you can start Jupyter.


### Known Issues

* After these steps you can run your spark applications only in local mode. You can follow this [tutorial](https://blog.clairvoyantsoft.com/installing-spark2-in-cloudera-cluster-through-docker-c9818ab59671) if you would like to be able to run your applications in cluster mode.
