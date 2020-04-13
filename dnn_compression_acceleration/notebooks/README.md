# Knowledge Distillation in Neural Networks 

Будем выполнять Knowledge Distillation на примере задачи CTR-prediction на датасете от Criteo, с которым мы уже работали в рамках предыдущих заданий.

---

## Задание

Нужно обучить модель, которая

* в терминах ROC AUC не намного хуже модели учителя, и в то же время
* сильно меньше по размеру

---

## Файлы

### [Teacher Model](./teacher_model_train_full.ipynb) 

Обучение модели учителя (не нужно запускать, но нужно посмотреть для понимания задания).

### [soft_targets.csv](https://drive.google.com/file/d/1tBbPOUT-Ow9f3zTDApykGXYwt-KslYle/view?usp=sharing) 

Файл содержит новые таргеты для обучения модели ученика. 

В каждой строке `<id>,<target>`, где `id` --- идентификатор записи в датасете Criteo.

### [Student Model](./student_model_train.ipynb)

Тетрадка с заданием.

---

## Критерии оценивания

Чем больше compression rate и ROC AUC, тем больше баллов можно получить за работу.
