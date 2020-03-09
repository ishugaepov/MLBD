import pandas as pd
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


def get_ate(groups, control_name) -> pd.DataFrame:
    """Get Average Treatment Effect
    groups - dictionary where keys - names of models, values - dicts of pairs <metric_name>, <metric_value>
    control_name - name of baseline model
    
    return pd.DataFrame (rows corresponds to metrics, cols corresponds to models and ATE with respect to control)
    """
    
    control_metrics = groups[control_name]
    metrics = list(control_metrics.keys())
    
    df = {'metric': metrics}
    
    for name, treatment in groups.items():
        if name == control_name:
            continue
        
        ate = []
        for metric_name in metrics:
            ate.append((treatment[metric_name] / control_metrics[metric_name] - 1.0) * 100)

        df['{} ate %'.format(name)] = ate
            
    return pd.DataFrame(df)