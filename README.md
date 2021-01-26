# Machine Learning on BigData
Materials for "Machine Learning on Big Data" course

## Syllabus

[Introduction](/lectures/intro/slides)

### Tools and Systems for Big Data Storage and Processing 
<details>
  <summary>List of topics</summary>

#### 1. [Hadoop and MapReduce](/lectures/hadoop_mapreduce)
>   <ins><i>Keywords:</i></ins> Google FS (master, chunkservers), Hadoop, HDFS (NameNode, DataNode), MapReduce (master, workers)
#### 2. [Apache Spark](/lectures/spark)
>  <ins><i>Keywords:</i></ins> Pig, Hive, Spark (RDDs, transformations, actions, lineage graph, fault-tolerance, persist, driver, workers, stages, dependencies, tasks, partition)
#### 3. Spark SQL
>  <ins><i>Keywords:</i></ins> Shark, DataFrames (DSL, cache, UDFs), Catalyst (tree, rule, catalyst in spark-sql)

</details>

### Large Scale Machine Learning
<details>
  <summary>List of topics</summary>

#### 1. Distributed ML Introduction
>  <ins><i>Keywords:</i></ins> Stochastic Gradient Descent, Data/Model Parallelism, General Purpose Distributed Computing(MapReduce, MR SGD, SparkNet, MLlib), Natively Distributed ML Systems (Parameter Server, DistBelief, TensorFlow, AllReduce, Horovod)
#### 2. Categorical Features in Large Scale ML
>  <ins><i>Keywords:</i></ins> One-hot encoding, Cross features, Factorization Machines (FM, FFM), Neural Networks (Deep Crossing, Deep & Cross, DeepFM)
#### 3. Gradient Boosting Decision Tree
>  <ins><i>Keywords:</i></ins> Categorical features (Naive Bayes, Mean Target Encoding), PLANET, XGBoost, CatBoost, SHAP values
#### 4. Hyperparameters Optimization
>  <ins><i>Keywords:</i></ins> Grid Search, Random Search (low effective dimensionality), Bayesian Optimization (Gaussian Process, surrogate, acquisition), Predictive Termination, Hyperband (successive halving), Multi-task Bayesian Optimization
#### 5. DNN Compression and Acceleration
> <ins><i>Keywords:</i></ins> Quantization, Knowledge Distillation, Pruning (one-shot, iterative, Lottery Ticket Hypothesis), Deep Compression, DeepGBM
#### 6. Recommender Systems
>  <ins><i>Keywords:</i></ins> Simple RS (Item/User-based, Content based), Ranking Metrics, Matrix Factorization (SVD, PMF, ALS, iALS, Incremental ALS, Neural CF), Large Scale RS (MF with Distributed SGD, PytorchBigGraph, GraphVite), Ranking losses (BPR, WARP)
#### 7. Nearest Neighbors Search
>  <ins><i>Keywords:</i></ins> Exact-kNN, Approximate NN (eps-NN), (Hierarchical) Navigatable Small World, LSH (random projections, minhash), Learning to Hash (Deep Supervised Hashing), Annoy, FAISS, ANN-benchmarks and evaluation
#### 8. Latent Dirichlet Allocation
#### 9. Dimensionality Reduction
#### 10. Online Learning
#### 11. Algorithms on Graphs

</details>

### Online Controlled Experiments
<details>
  <summary>List of topics</summary>

#### 1. How to conduct AB Tests (Experiment Design, Execution, Analysis)
>  <ins><i>Keywords:</i></ins> Offline Evaluation (hypothesis testing, 5x2 cv test, testing over multiple datasets), Online Evaluation
#### 2. Results Analysis ((Multiple) Hypothesis testing, Sensitivity, Power)
#### 3. Heterogeneous Treatment Effect

</details>

## Практики

Для выполнения практик нужно сделать fork ([GitHub Help: Forks](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks)) данного репозитория.

#### Порядок выполнения и отправки задания на проверку

Задания находятся в `<topic>/notebooks/<practice_name>.ipynb`.

1. Убедитесь, что ishugaepov добавлен в список коллабораторов вашего форка (`Settings -> Manage access -> Invite a collaborator`)
2. Убедитесь, что ваш fork репозиторий содержит все актуальные изменения данного репозитория ([GitHub Help: Syncing a fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork))
3. Выполните задание в отдельной ветке, например, `practice_1` ([GitHub Help: Branches](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)).
4. Сделайте Pull Request (`<current_practice_branch> -> master`), добавьте ishugaepov в Assignees ([GitHub Help: PRs](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)). 
5. После проверки PR, ревьювер либо оставляет комментарии с замечаниями либо мерджит текущую ветку в мастер вашего репозитория.

#### Deadlines

* PR с выполненным заданием должен быть отправлен на проверку не позднее чем через 8 дней после того как было выдано задание.
* По прошествии дедлайна, в рамках PR можно только исправлять замечания, но не отправлять на проверку новые задачи.

## Контесты

1. [Kaggle: CTR Prediction](https://www.kaggle.com/c/mlbd-20-ctr-prediction-1)
2. TBD

#### Общая информация

1. Для решения контестов можно использовать любые методы/приемы/фрэймворки, которые обсуждались на лекциях.
2. После окончания контеста нужно будет написать отчет об итоговом решении.

## Ответы на организационные вопросы

<details>
  <summary>FAQ</summary>

#### Q: Сколько домашних заданий? Будет ли экзамен? С каким весом берется то и другое? 

Оценка за курс выставляется по результатам выполнения практических заданий. <br>
При выставлении оценки все задания учитываются с одинаковым весом. <br>
Очередное практическое задание будет появлятся после лекции.

#### Q: Что обязательное, а за что можно получить доп. баллы?

Контесты обязательны и нужны для более объективной оценки некоторых практических заданий. <br>
Позиция в лидерборде + отчет об итоговом решении позволяют получить дополнительные баллы, после завершения контеста.

</details>

## Docker

В рамках курса мы будем использовать Docker container с Hadoop, для того чтобы эмулировать кластер и запускать различные примеры.

См. [Docker Tutorial](/docker/Docker-tutorial.md)

## Datasets

* [MovieLens](https://drive.google.com/file/d/1uNG51xzfUahzexIv-Ka1ylpvn8mVdFOQ/view?usp=sharing)
* [Criteo Ads](https://labs.criteo.com/2014/02/download-kaggle-display-advertising-challenge-dataset/)

