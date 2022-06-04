import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from aprioriAlgorithm import apriori

df = pd.read_xlsx('apriorialgorithmdt.xlsx', header=None)
df.head()


transactions = []
for i in range(0, df.shape[0]):
    transactions.append([str(df.values[i, j]) for j in range(0, 20)])
    print(transactions[0])
    print('nira')

rules = apriori(transactions, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2)
results = list(rules)

results = pd.DataFrame(results)
results.head(5)
