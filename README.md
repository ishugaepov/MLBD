# MLBD
Materials for "Machine Learning on Big Data" course

## Docker

В рамках курса мы будем использовать Docker container с Hadoop, для того чтобы эмулировать кластер и запускать различные примеры.

См. [Docker Tutorial](https://github.com/ishugaepov/MLBD/blob/master/docker/Docker-tutorial.md)

## Datasets

* [MovieLens](https://drive.google.com/file/d/1uNG51xzfUahzexIv-Ka1ylpvn8mVdFOQ/view?usp=sharing)
* [Criteo Ads](https://labs.criteo.com/2014/02/download-kaggle-display-advertising-challenge-dataset/)

## Программа курса

[Introduction](https://github.com/ishugaepov/MLBD/tree/master/intro/slides)

### Методы и системы обработки больших данных

1. [Hadoop and MapReduce](https://github.com/ishugaepov/MLBD/tree/master/hadoop_map_reduce)
2. [Apache Spark](https://github.com/ishugaepov/MLBD/tree/master/apache_spark)
3. [Spark SQL](https://github.com/ishugaepov/MLBD/tree/master/spark_sql)

### Машинное обучение на больших данных

4. [Distributed ML Introduction](https://github.com/ishugaepov/MLBD/tree/master/distributed_ml_intro)
5. Stochastic Gradient Descent, Linear Models, Neural Networks
6. Hyperparameters Optimization
7. Gradient Boosting Decision Tree
8. Word2Vec, k-Nearest Neighbors
9. Collaborative Filtering (ALS)
10. Latent Dirichlet Allocation
11. Dimensionality Reduction
12. Online Learning
13. Algorithms on Graphs

### Проведение онлайн экспериментов

14. How to conduct AB Tests (Experiment Design, Execution, Analysis)
15. Results Analysis ((Multiple) Hypothesis testing, Sensitivity, Power)
16. Heterogeneous Treatment Effect

## Практики

Для выполнения практик нужно сделать fork ([GitHub Help: Forks](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks)) данного репозитория.

#### Порядок выполнения и отправки задания на проверку

Задания находятся в `<topic>/notebooks/<practice_name>.ipynb`.

1. Убедитесь, что ваш fork репозиторий содержит все актуальные изменения данного репозитория ([GitHub Help: Syncing a fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork))
2. Выполните задание в отдельной ветке, например, `practice_1` ([GitHub Help: Branches](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)).
3. Сделайте Pull Request (`<current_practice_branch> -> master`), назначьте PR на ishugaepov ([GitHub Help: PRs](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)). 
4. После проверки PR, ревьювер либо оставляет комментарии с замечаниями либо мерджит текущую ветку в мастер вашего репозитория.

#### Deadlines

* PR с выполненным заданием должен быть отправлен на проверку не позднее времени начала занятия, следующего за занятием, на котором было выдано задание.
* По прошествии дедлайна, в рамках PR можно только исправлять замечания, но не отправлять на проверку новые задачи.

## Домашние задания

1. [Kaggle: CTR Prediction](https://www.kaggle.com/c/mlbd-20-ctr-prediction-1)
2. TBD
3. TBD
