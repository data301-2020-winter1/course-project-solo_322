#script that return a section of the complete database based on the input integer
#filters data accordingly

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling


def load_and_process(url_path_csv, i):
    
    df = pd.read_csv(url_path_csv)
    if i == 0:
        return df
    
    elif i == 1:
        df1 = (
        df.loc[:, ['RespId', 'ppage', 'gender', 'educ', 'race', 'voter_category', 'Q2_1']]
        .rename(columns={'RespId': 'id', 'voter_category': 'cat', 'Q2_1': 'voting_imp'})
        .dropna(subset = ['id', 'ppage', 'gender', 'educ', 'race', 'cat', 'voting_imp'])
        .drop(df.loc[df['Q2_1'] < 1].index)
        .sort_values("id")
        .reset_index(drop=True)
        )
        return df1
    
    elif i == 2:
        df2 = (
        df.loc[:, ['ppage', 'gender', 'Q29_1', 'Q29_2', 'Q29_3', 'Q29_4', 'Q29_5', 'Q29_6', 'Q29_7', 'Q29_8', 'Q29_9', 'voter_category']]
        .rename(columns={'voter_category': 'cat'})
        .sort_values("ppage")
        .reset_index(drop=True)
        )
        return df2
    
    elif i == 3:
        df3 = (
        df.loc[:, ['Q16', 'ppage', 'gender']]
        .rename(columns={'Q16': 'difficulty'})
        .dropna(subset = ['difficulty', 'ppage', 'gender'])
        .drop(df.loc[df['Q16'] < 1].index)
        .sort_values("ppage")
        .reset_index(drop=True)
        )
        return df3
    
    elif i == 4:
        df4 = (
        df.loc[:, ['RespId', 'Q7', 'ppage', 'gender', 'voter_category']]
        .rename(columns={'RespId': 'id', 'voter_category': 'cat', 'Q7': 'need_change'})
        .drop(df.loc[df['Q7'] < 1].index)
        .dropna(subset = ['need_change', 'id', 'gender', 'cat', 'ppage'])
        .sort_values("id")
        .reset_index(drop=True)
        )
        return df4
    else:
        df5 = (
        df.loc[:, ['RespId', 'ppage', 'gender', 'educ', 'race', 'voter_category', 'Q2_1', 'Q29_1', 'Q29_2', 'Q29_3', 'Q29_4', 'Q29_5', 'Q29_6', 'Q29_7', 'Q29_8', 'Q29_9', 'Q16', 'Q7']]
        .rename(columns={'RespId': 'id', 'voter_category': 'cat', 'Q2_1': 'voting_imp', 'Q16': 'difficulty', 'Q7': 'need_change'})
        .dropna(subset = ['id', 'ppage', 'gender', 'educ', 'race', 'cat', 'voting_imp', 'difficulty', 'need_change'])
        .sort_values("id")
        .reset_index(drop=True)
        )
        return df5

#ignore these statements
#.drop(df.loc[df['Q2_1'] < 1].index)
#.drop(df.loc[df['Q16'] < 1].index)
#.drop(df.loc[df['Q7'] < 1].index)