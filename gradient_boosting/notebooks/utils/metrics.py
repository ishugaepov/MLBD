import pyspark
import pyspark.sql.functions as F
from pyspark.sql.types import *
from pyspark.mllib.evaluation import BinaryClassificationMetrics


def rocauc(model, df, probabilities_col='probability'):
    df = model.transform(df)
    df = df.withColumn('proba', F.udf(lambda v: float(v[1]), FloatType())(F.col(probabilities_col)))
    
    preds_and_labels = df\
        .select(F.col('proba'), F.col('label').cast('float')) \
        .rdd.map(lambda row: (row[0], row[1]))
    
    metrics = BinaryClassificationMetrics(preds_and_labels)

    return metrics.areaUnderROC


def logloss(model, df, probabilities_col='probability'):
    df = model.transform(df)
    df = df.withColumn('proba', F.udf(lambda v: float(v[1]), FloatType())(F.col(probabilities_col)))

    df = df.withColumn('logloss',
                       - F.col('label') * F.log(F.col('proba')) - (1. - F.col('label')) * F.log(1. - F.col('proba')))

    return df.agg(F.mean('logloss')).first()[0]


def ne(model, df, probabilities_col='probability'):
    ll = logloss(model, df, probabilities_col)
    p = df.select(F.mean('label')).first()[0]
    ll_baseline =  -(p * np.log(p) + (1 - p) * np.log(1 - p))
    return ll / ll_baseline