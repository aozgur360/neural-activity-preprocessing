import os
import numpy as np
import pickle
import pandas as pd
import scipy.stats as sp
from matplotlib import pyplot as plt
import scipy.io as spio
import re
from pathlib import Path
import time
import glob

def getsubfolders(folder):
    ''' returns list of subfolders '''
    return [os.path.join(folder,p) for p in os.listdir(folder) if os.path.isdir(os.path.join(folder,p))]

shuffle=1
temp = []
basepath='Z:\Ali O\yarm_miniscope_recording'
basefolders = []
subfolders=getsubfolders(basepath)

for subfolder in subfolders:
    subfolders=getsubfolders(subfolder)
    if "m25lr" in subfolder:
        for subfolder in subfolders:
             subfolders=getsubfolders(subfolder)
             for subfolder in subfolders:
                     if "hbug" not in subfolder:
    #             if 'mcheck' not in subfolder:
                         basefolders.append(subfolder)
                         subfolders = getsubfolders(subfolder)
                         for subfolder in subfolders:
                             subfolders = getsubfolders(subfolder)
                             #isExist = os.path.exists(subfolder + '/spikerate.csv')
                             isExist = os.path.exists(subfolder + '/spikerate')
                             if isExist:
                                 continue
                             else:
                             
                                 isExist = os.path.exists(subfolder + '/S.csv')
                                 if isExist:            
    
                                    #plot single cell traces for minian
                                    main_base = subfolder
                                    #main_base = r'Z:\Ali O\yarm_miniscope_recording\m12lr\m12lr_3\2022_05_23_r2_dlc_ez_good_epa_bv\13_56_30'
                                    
                                    #calcium_csv_path = main_base + '\\YrA.csv'
                                    
                                    #for spike rate
                                    calcium_csv_path = main_base + '\\S.csv'
                                    
                                    os.chdir(main_base)
                                    main_text = glob.glob('*.txt')[0]
                                    
                                    split_frame_numbers = []
                                    
                                    def get_saved_data(file_name):
                                        try:
                                            with open(file_name, 'rb') as handle:
                                                response = pickle.load(handle)
                                                return response
                                        except FileNotFoundError:
                                            print(f'Could not find saved data for file {file_name}')
                                            return None
                                    
                                    
                                    
                                    def save_data(data, file_name):
                                        with open(file_name, 'wb') as handle:
                                            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
                                    
                                    
                                    
                                    def get_or_save_data_frame_from_csv(csv_path, use_pickle = True):
                                        if not use_pickle:
                                            data_frame = pd.read_csv(csv_path, usecols=["unit_id","frame","S"])
                                        else:
                                            csv_pickle_path = csv_path + '.pickle'
                                            data_frame = get_saved_data(csv_pickle_path)
                                            if (data_frame is None):
                                                data_frame = pd.read_csv(csv_path, usecols=["unit_id","frame","S"])
                                                save_data(data_frame, csv_pickle_path)
                                            
                                        return data_frame
                                    
                                    
                                    def get_yras_for_unique_cells(data_frame):
                                        data = pd.DataFrame()
                                    
                                        unique_cell_ids = np.unique(data_frame["unit_id"])
                                    
                                        for cell_id in unique_cell_ids:
                                            if cell_id == -1:
                                                continue
                                    
                                            cell_data_series = data_frame[data_frame['unit_id'] == cell_id]
                                            data[str(cell_id)] = cell_data_series['S'].to_numpy()
                                    
                                        #drop nans
                                        data = data.dropna(axis=1, how='all')
                                    
                                        #rename columns because may need reordering after dropped nans
                                        rename_col = list(range(len(data.columns)))
                                        data.columns = rename_col
                                    
                                        return data
                                    
                                    def normalize_yras_for_each_cell(data_frame):
                                        max_scaled = data_frame / data_frame.max()
                                        return max_scaled
                                    
                                    
                                    
                                    
                                    def split_daily_data_frames(data_frame, split_frame_numbers):
                                        split_data_frames = []
                                        remaining_data_frame = data_frame
                                    
                                        for split_frame_number in split_frame_numbers:
                                            split_data_frame = remaining_data_frame.head(split_frame_number)
                                            split_data_frames.append(split_data_frame)
                                    
                                            remaining_data_frame = remaining_data_frame[split_frame_number:]
                                    
                                            # re index frames to start from 0 again
                                            remaining_data_frame = remaining_data_frame.reset_index()
                                    
                                            # drop first column of all index
                                            remaining_data_frame = remaining_data_frame.drop(['index'], axis = 1)
                                    
                                        split_data_frames.append(remaining_data_frame)
                                    
                                        return split_data_frames
                                    
                                    ###TEST
                                    def split_daily_data_frames_then_normalize(data_frame, split_frame_numbers):
                                        split_data_frames = []
                                        remaining_data_frame = data_frame
                                    
                                        for split_frame_number in split_frame_numbers:
                                            split_data_frame = remaining_data_frame.head(split_frame_number)
                                            split_data_frames.append(split_data_frame)
                                    
                                            remaining_data_frame = remaining_data_frame[split_frame_number:]
                                    
                                            # re index frames to start from 0 again
                                            remaining_data_frame = remaining_data_frame.reset_index()
                                    
                                            # drop first column of all index
                                            remaining_data_frame = remaining_data_frame.drop(['index'], axis = 1)
                                            
                                            remaining_data_frame = remaining_data_frame / remaining_data_frame.max()
                                    
                                        split_data_frames.append(remaining_data_frame)
                                        split_data_frames_temp = []
                                        for i in split_data_frames:
                                            split_data_frames_temp.append(i / i.max())
                                            
                                        split_data_frames = split_data_frames_temp
                                        return split_data_frames
                                    
                                    tic = time.perf_counter()
                                    calcium_data_frame = get_or_save_data_frame_from_csv(calcium_csv_path)
                                    
                                    unique_cells_yras_data_frame = get_yras_for_unique_cells(calcium_data_frame)
                                    spikerate = unique_cells_yras_data_frame
                                    
                                    daily_data_frames_raw = split_daily_data_frames(unique_cells_yras_data_frame, split_frame_numbers)
                                    normalized_cells_yras_data_frame = normalize_yras_for_each_cell(unique_cells_yras_data_frame)
                                    
                                    daily_data_frames = split_daily_data_frames(normalized_cells_yras_data_frame, split_frame_numbers)
                                    
                                    #sessions_data = get_sessions_data(daily_data_frames)
                                    toc = time.perf_counter()
                                    print(f"Function took {toc - tic:0.4f} seconds")
                                    
                                    new_folder = subfolder + '\\spikerate'
                                    os.makedirs(new_folder)
                                    date = Path(main_text).stem
                                    # save csv
                                    #spikerate = unqiue_cells_yras_data_frame
                                    #file = subfolder + '\\spikerate.csv'
                                    file = new_folder + '\\spikerate_' + date + '.csv'
                                    spikerate.to_csv(file)
                                 else:
                                     continue














