{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}
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
        df.loc[:, ['RespId', 'ppage', 'gender', 'educ', 'race', 'voter_category']]
        .rename(columns={'RespId': 'id', 'voter_category': 'cat'})
        .dropna(subset = ['id', 'ppage', 'gender', 'educ', 'race', 'cat'])
        .sort_values("id")
        .reset_index(drop=True)
            )
        return df1
    
    elif i == 2:
        df2 = (
        df.loc[:, ['ppage', 'gender']]
        .sort_values("ppage")
        .reset_index(drop=True)
            )
        return df2
    
    else:
        df3 = (
        df.loc[:, ['RespId', 'gender', 'voter_category']]
        .rename(columns={'RespId': 'id', 'voter_category': 'cat'})
        .dropna(subset = ['id', 'gender', 'cat'])
        .sort_values("id")
        .reset_index(drop=True)
            )
        return df3