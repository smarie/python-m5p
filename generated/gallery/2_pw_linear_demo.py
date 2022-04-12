"""
Piecewise-Linear artificial example
===================================

This demo is reproducing the results from the "Artificial Dataset" in the M5
paper, named `pw-linear` in the M5' paper.
"""
# %%
# Import the necessary modules and libraries
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor, export_text
from m5py import M5Prime

# %%
# Create a random dataset
rng = np.random.RandomState(1)
nb_samples = 200

X1 = rng.randint(0, 2, nb_samples) * 2 - 1
X2 = rng.randint(-1, 2, nb_samples)
X3 = rng.randint(-1, 2, nb_samples)
X4 = rng.randint(-1, 2, nb_samples)
X5 = rng.randint(-1, 2, nb_samples)
X6 = rng.randint(-1, 2, nb_samples)
X7 = rng.randint(-1, 2, nb_samples)
X8 = rng.randint(-1, 2, nb_samples)
X9 = rng.randint(-1, 2, nb_samples)
X10 = rng.randint(-1, 2, nb_samples)

feature_names = ["X%i" % i for i in range(1, 11)]
X = np.c_[X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

y = np.where(
    X1 > 0,
    3 + 3 * X2 + 2 * X3 + X4,
    -3 + 3 * X5 + 2 * X6 + X7
) + rng.normal(loc=0., scale=2 ** 0.5, size=nb_samples)

# %%
# Define regression models and evaluate them on 10-fold CV
regr_0 = DecisionTreeRegressor()
regr_0_label = "Tree 0"
regr_0_scores = cross_val_score(regr_0, X, y, cv=10)

regr_1 = M5Prime(use_smoothing=False, use_pruning=False)
regr_1_label = "Tree 1"
regr_1_scores = cross_val_score(regr_1, X, y, cv=10)

regr_2 = M5Prime(use_smoothing=False)
regr_2_label = "Tree 2"
regr_2_scores = cross_val_score(regr_2, X, y, cv=10)

regr_3 = M5Prime(use_smoothing=True)
regr_3_label = "Tree 3"
regr_3_scores = cross_val_score(regr_3, X, y, cv=10)

scores = np.c_[regr_0_scores, regr_1_scores, regr_2_scores, regr_3_scores]
avgs = scores.mean(axis=0)
stds = scores.std(axis=0)
labels = [regr_0_label, regr_1_label, regr_2_label, regr_3_label]

scores_df = pd.DataFrame(data=scores, columns=labels)
sns.violinplot(data=scores_df)

# %%
# Fit the final models and print the trees:
#
regr_0.fit(X, y)
print("\n----- %s" % regr_0_label)
print(export_text(regr_0, feature_names=feature_names))

# %%
regr_1.fit(X, y)
print("\n----- %s" % regr_1_label)
print(regr_1.as_pretty_text(feature_names=feature_names))

# %%
regr_2.fit(X, y)
print("\n----- %s" % regr_2_label)
print(regr_2.as_pretty_text(feature_names=feature_names))

# %%
regr_3.fit(X, y)
print("\n----- %s" % regr_3_label)
print(regr_3.as_pretty_text(feature_names=feature_names))
