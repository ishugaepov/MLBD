# MLBD
Materials for "Machine Learning on Big Data" course

## Программа курса

[Introduction](/intro/slides)

### Методы и системы обработки больших данных
<details>
  <summary>Список тем</summary>

#### 1. [Hadoop and MapReduce](/hadoop_map_reduce)
>   <ins><i>Keywords:</i></ins> Google FS (master, chunkservers), Hadoop, HDFS (NameNode, DataNode), MapReduce (master, workers)
#### 2. [Apache Spark](/apache_spark)
>  <ins><i>Keywords:</i></ins> Pig, Hive, Spark (RDDs, transformations, actions, lineage graph, fault-tolerance, persist, driver, workers, stages, dependencies, tasks, partition)
#### 3. [Spark SQL](/spark_sql)
>  <ins><i>Keywords:</i></ins> Shark, DataFrames (DSL, cache, UDFs), Catalyst (tree, rule, catalyst in spark-sql)

</details>

### Машинное обучение на больших данных
<details>
  <summary>Список тем</summary>

#### 4. [Distributed ML Introduction](/distributed_ml_intro)
>  <ins><i>Keywords:</i></ins> Stochastic Gradient Descent, Data/Model Parallelism, General Purpose Distributed Computing(MapReduce, MR SGD, SparkNet, MLlib), Natively Distributed ML Systems (Parameter Server, DistBelief, TensorFlow, AllReduce, Horovod)
#### 5. [Categorical Features in Large Scale ML](/sgd_logreg_nn)
>  <ins><i>Keywords:</i></ins> One-hot encoding, Cross features, Factorization Machines (FM, FFM), Neural Networks (Deep Crossing, Deep & Cross, DeepFM)
#### 6. [Gradient Boosting Decision Tree](/gradient_boosting)
>  <ins><i>Keywords:</i></ins> Categorical features (Naive Bayes, Mean Target Encoding), PLANET, XGBoost, CatBoost, SHAP values
#### 7. Hyperparameters Optimization
#### 8. Word2Vec, k-Nearest Neighbors
#### 9. Collaborative Filtering (ALS)
#### 10. Latent Dirichlet Allocation
#### 11. Dimensionality Reduction
#### 12. Online Learning
#### 13. Algorithms on Graphs

</details>

### Проведение онлайн экспериментов
<details>
  <summary>Список тем</summary>

#### 14. How to conduct AB Tests (Experiment Design, Execution, Analysis)
#### 15. Results Analysis ((Multiple) Hypothesis testing, Sensitivity, Power)
#### 16. Heterogeneous Treatment Effect

</details>

## Практики

Для выполнения практик нужно сделать fork ([GitHub Help: Forks](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks)) данного репозитория.

#### Порядок выполнения и отправки задания на проверку

Задания находятся в `<topic>/notebooks/<practice_name>.ipynb`.

1. Убедитесь, что ваш fork репозиторий содержит все актуальные изменения данного репозитория ([GitHub Help: Syncing a fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork))
2. Выполните задание в отдельной ветке, например, `practice_1` ([GitHub Help: Branches](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)).
3. Сделайте Pull Request (`<current_practice_branch> -> master`), назначьте PR на ishugaepov ([GitHub Help: PRs](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)). 
4. После проверки PR, ревьювер либо оставляет комментарии с замечаниями либо мерджит текущую ветку в мастер вашего репозитория.

#### Deadlines

* PR с выполненным заданием должен быть отправлен на проверку не позднее чем через 8 дней после того как было выдано задание.
* По прошествии дедлайна, в рамках PR можно только исправлять замечания, но не отправлять на проверку новые задачи.

## Домашние задания

1. [Kaggle: CTR Prediction](https://www.kaggle.com/c/mlbd-20-ctr-prediction-1)
2. TBD
3. TBD

## Docker

В рамках курса мы будем использовать Docker container с Hadoop, для того чтобы эмулировать кластер и запускать различные примеры.

См. [Docker Tutorial](/docker/Docker-tutorial.md)

## Datasets

* [MovieLens](https://drive.google.com/file/d/1uNG51xzfUahzexIv-Ka1ylpvn8mVdFOQ/view?usp=sharing)
* [Criteo Ads](https://labs.criteo.com/2014/02/download-kaggle-display-advertising-challenge-dataset/)

