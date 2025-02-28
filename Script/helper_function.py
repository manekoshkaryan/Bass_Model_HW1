#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

import pandas as pd
from pathlib import Path

# In[3]:


def bass_model(t, p, q, M):
    return (M * (p + q) ** 2 * np.exp(-(p + q) * t)) / (p + q * np.exp(-(p + q) * t)) ** 2


# In[4]:
def load_and_clean_data():
    
    current_file_dir = Path.cwd()
    data_file = current_file_dir.parent / "data" / "TV2.xlsx"
    
    df = pd.read_excel(data_file, sheet_name="Data", skiprows=4, header=None)
   
    df_cleaned = df[[1, 3]]
    df_cleaned.columns = ["Year", "LCD TV"]
    df_cleaned = df_cleaned.dropna(subset=["Year"])
    df_cleaned["Year"] = df_cleaned["Year"].astype(int)
    
    return df_cleaned