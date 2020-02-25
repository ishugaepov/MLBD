import numpy as np
import pyspark
import pyspark.sql.functions as F
from pyspark.sql.types import *


def split_by_col(df, split_col, parts_fractions):
    probs = list(np.cumsum(parts_fractions))
    split_points = df.approxQuantile(split_col, [0.0] + probs, 0.0)
    
    parts = []
    for i in range(len(split_points) - 1):
        l = split_points[i]
        r = split_points[i + 1]
        p = df.filter((F.lit(l) <= F.col(split_col)) & (F.col(split_col) < F.lit(r)))
        parts.append(p)

    return parts