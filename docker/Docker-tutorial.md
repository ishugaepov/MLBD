## Install Stable Docker Community Edition (CE)

- For Mac: 
https://docs.docker.com/docker-for-mac/install/

- For Ubuntu: 
https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/ (see also other Linux distributives in the menu).

## Change RAM Limits of the Container

Your container might have memory limits that are different from the actual limits of your physical machine, which might lead to a crash of your code due memory shortage.

- If you're running Windows or OSX, the default limit is 2GB, but you can change it by following this tutorials:
  - For Windows: https://docs.docker.com/docker-for-windows/#advanced
  - For Mac OSX: https://docs.docker.com/docker-for-mac/#advanced

- If you're running Linux, you're all set as the memory limits are the same as the physical memory of your machine.

**Important**: Recommended amount of RAM is 8GB.

## Run Container

Для того чтобы запустить Docker контейнер с Hadoop нужно сделать следующее:
1. ```cd ./docker```
1. ```bash download_image.sh```
1. (опционально) Собрать Docker image с нуля ```bash build_image.sh```
1. ```bash run.sh```

**Замечание**:
После того как образ был успешно создан, для перезапуска контейнера достаточно пользоваться только последней командой.

### Run Jupyter
После того как контейнер запустится, нужно в командной строке ввести 

```jupyter notebook --no-browser --port 9999 --ip='*' --allow-root```

Этот код запустит Jupyter.

После того как запустится Jupyter, в браузере по адресу ```localhost:9999``` будет доступен jupyter's web gui.

### PySpark Application Example

Для того чтобы убедиться в том, что все работает нормально, можно запустить пример в тетрадке ```/lectures/hadoop_mapreduce/notebooks/start_spark_example.ipynb```, который запустит небольшое pyspark приложение.

Если все работает корректно, то в браузере по адресу ```localhost:8088``` будет доступен Yarn, в котором можно состояние кластера и задач.

### Known Issues

* Иногда в адресной строке приходиться в ручную заменять ```quickstart.cloudera``` на ```localhost```.
