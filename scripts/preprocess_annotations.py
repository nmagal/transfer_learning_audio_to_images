#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:25:20 2023

@author: nicholasmagal

Preprocess labels cv to only contain non corrupted files
"""
import numpy as np
import pandas as pd

#indexes to delete that won't load
indexes_to_delete = np.load("/Users/nicholasmagal/Documents/Research/CMC_with_source_seperation/datasets/magnatagatune/meta_data/to_delete.npy")

labels_path = "/Users/nicholasmagal/Documents/Research/CMC_with_source_seperation/datasets/magnatagatune/meta_data/annotations_final.csv"
labels_df = pd.read_csv(labels_path, sep='\t')
labels_df.drop(indexes_to_delete, inplace = True)

#Only using top50 tags https://github.com/jongpillee/music_dataset_split/blob/master/MTAT_split/top50_tags.txt
top50_path = '/Users/nicholasmagal/Documents/Research/transfer_learning_audio_to_image/data/top50_tags.txt'
with open(top50_path) as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines.append('mp3_path')

labels_df = labels_df[lines]
#saving
labels_df.to_csv("/Users/nicholasmagal/Documents/Research/CMC_with_source_seperation/datasets/magnatagatune/meta_data/annotations_final_proces.csv", index = False, sep='\t')