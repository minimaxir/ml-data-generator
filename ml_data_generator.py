from faker import Faker
from datetime import datetime
import pandas as pd
import numpy as np
from gen_utils import *

fake = Faker()

nrow = 100

df = pd.DataFrame()


# Build up fake data of all data types for the model.
# See the README for more information about each field.

# Numeric data

df['num1'] = np.random.normal(0, 1, nrow)
df['num2'] = np.random.randint(1, 100, nrow)

# Text data

df['text1'] = [fake.sentence(nb_words=10, variable_nb_words=True)
               for _ in range(nrow)]
df['text2'] = [fake.sentence(nb_words=4, variable_nb_words=True)
               for _ in range(nrow)]
df['name'] = [fake.name()
              for _ in range(nrow)]

# Categorical data

df['cat1'] = np.random.randint(1, 10, nrow)
df['cat2'] = np.random.choice(['a', 'b', 'c'], nrow, p=[0.5, 0.45, 0.05])

# Datetime data

df['datetime1'] = [fake.date_time_between(
    start_date=datetime(2017, 1, 1),
    end_date=datetime(2018, 12, 31))
    for _ in range(nrow)]
df['datetime2'] = df['datetime1'].apply(lambda x: x +
                                        pd.Timedelta(seconds=np.random.randint(0, 72 * 60 * 60)))


# Process each generated field to derive a target statistic.


num1_tf = df['num1']**2
num2_tf = df['num2'] / 10 * num1_tf

text1_tf = df['text1'].apply(text1_transform)
text2_tf = df['text2'].apply(text2_transform)

datetime1_tf = (df['datetime2'] - df['datetime1'])
datetime1_tf = datetime1_tf / np.timedelta64(1, 'h') / 12

cat1_dict = {
    1: 2,
    2: -1,
    3: 4,
    4: 6,
    5: -6,
    6: 4,
    7: 9,
    8: 10,
    9: -4,
    10: 0
}

cat2_dict = {
    'a': 1,
    'b': 4,
    'c': 15
}

cat1_tf = df['cat1'].apply(lambda x: cat1_dict[x])
cat2_tf = df['cat2'].apply(lambda x: cat2_dict[x])

df['target'] = (num1_tf + num2_tf + text1_tf + text2_tf +
                datetime1_tf + cat1_tf + cat2_tf)

# Save the 3 dataframes.

df.to_csv("gen_df_regression.csv", index=False)

df_copy = df.copy()
bins = df_copy['target'].quantile()
df_copy['target'] = pd.cut(
    df_copy['target'], bins=bins, labels=False, include_lowest=True)
df_copy.to_csv("gen_df_binary.csv", index=False)

df_copy = df.copy()
bins = df_copy['target'].quantile(np.linspace(0, 1, 11))
df_copy['target'] = pd.cut(
    df_copy['target'], bins=bins, labels=False, include_lowest=True).astype(int)
df_copy.to_csv("gen_df_categorical.csv", index=False)
