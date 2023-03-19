#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 13:21:49 2023

@author: nicholasmagal
Given a directory, extracts and saves melspectogram numpy arrays.

Steps:
    1.) Get highlight from audio (loudest portion)
    2.) Convert that portion into melspectogram data
    3.) Save file as numpy array
    
"""

import os
import shutil
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from collections import defaultdict

#Create a directory for our subsets based on our genre. Return a list of output dirs
def create_output_dir(genres, path):
    genres = (list(genres))
    genres = set([genre.split(".")[0] for genre in genres])
    
    file_dirs = []
    
    #remove if we already have it to keep things clean
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.makedirs(path)
    
    #Creating directories
    for genre in genres:
        genre_path = path + '/' + genre.split('.')[0]
        os.makedirs(genre_path)
        file_dirs.append(genre_path)
    
    return file_dirs

#Get all songs in a dir, seperate by genre 
def get_songs(input_dir):

    files = defaultdict(list)
    for (dirpath, dirnames, filenames) in os.walk(input_dir):
        for file in filenames:
            if file.split('.')[-1] in ['mp3', 'wav', 'npy']:
                files[dirpath.split('/')[-1]].append(os.path.join(dirpath, file))
    
    return files

#creates and saves mel_spectogram highlights 
def extract_mel_spectogram(source_sep, files, output_path, plot = False):
    
    #Per source seperated track, get highlight, turn into mel spectogram, and save
    for song_name, song_paths in (files.items()):
        
        #Create directory
        if source_sep == True:
            genre = song_name.split(".")[0]
            save_path = output_path + '/' + genre + '/' + song_name + '/'
            os.makedirs(save_path)
        
        else:
            genre = song_name.split(".")[0]
            save_path = output_path + '/' + song_name + '/'
        
        
        #Loop through all song_paths for each source seperated track
        for song_path in tqdm(song_paths):
            #Reading in track 
            try:
                sound, sr = librosa.load(song_path)
         
                mel_spectogram = librosa.feature.melspectrogram(y=sound, sr = sr)
                    
                #Saving our data 
                file_name = save_path + song_path.split('/')[-1].split('.')[0]+'.npy'
                np.save(file_name ,mel_spectogram)
            except:
                print("error reading", song_path)
    
        
if __name__ == '__main__':
    
    input_dir = '/Users/nicholasmagal/Documents/Research/CMC_with_source_seperation/datasets/magnatagatune/og_dataset'
    output_dir = input_dir + '_mel_spectogram'
    source_seperated = False
    
    #Getting list of file names    
    input_files = get_songs(input_dir)
    
    #Creating empty file structure
    output_dirs = create_output_dir(input_files.keys(), output_dir)
    
    #Creating highlights and converting to melspectogram and saving to numpy array
    extract_mel_spectogram(source_seperated, input_files, output_dir, False)
    

    
    
    
