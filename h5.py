# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 17:22:13 2023

@author: hodan
"""
import h5py
import pandas as pd

file_path = 'C:/Users/hodan/OneDrive/Desktop/Video codes/raw data.h5'



def explore_hdf5(file_obj, parent_name='', dataset_list=None):
    if dataset_list is None:
        dataset_list = []

    for name in file_obj:
        item = file_obj[name]
        full_name = f'{parent_name}/{name}' if parent_name else name

        if isinstance(item, h5py.Group):
            # If the item is a group, recursively explore its contents
            explore_hdf5(item, full_name, dataset_list)
        elif isinstance(item, h5py.Dataset):
            # If the item is a dataset, add its name and path to the list
            dataset_list.append({'Dataset Name': name, 'Full Path': full_name})

    return dataset_list

# Replace 'your_existing_file.h5' with the actual file path of your HDF5 file


# Open the HDF5 file in read-only mode
with h5py.File(file_path, 'r') as hf:
    # Explore the contents of the HDF5 file and get the dataset list
    dataset_list = explore_hdf5(hf)

# Convert the dataset list to a pandas DataFrame
df_datasets = pd.DataFrame(dataset_list)

# Display the DataFrame containing information about all datasets
print(df_datasets)

file_path = 'C:/Users/hodan/Downloads/CH006_tug_stand_walk_sit.pickle'

with open(file_path, 'rb') as file:
    data = pickle.load(file)



