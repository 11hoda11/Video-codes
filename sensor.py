# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:22:26 2023

@author: hodan
"""

import pandas as pd
import numpy as np
import matplotlib as plt
import csv



def read_csv_with_header(file_path, start_row):
    try:
        df = pd.read_csv(file_path, header=start_row)
        return df
    except Exception as e:
        print("Error occurred:", e)
        return None

# Usage exampleour/csv/file.
csv_file_path = 'C:/Users/hodan/OneDrive/Desktop/Video codes/Joint_Angles.csv'
start_row = 14

data = read_csv_with_header(csv_file_path, start_row)

if data is None:
    print("Failed to read rows from the CSV file.")
