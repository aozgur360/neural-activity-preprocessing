import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

calraw = pd.read_csv(r"Z:\Ali O\yarm_miniscope_recording\m12lr\m12lr_3\2022_05_20_r2_dlc_ez_good_epa_bv\15_00_33\exported_python_analysis\05_20_2022___15_00_32\calcium_raw_05_20_2022___15_00_32.csv")
spikes = pd.read_csv(r"Z:\Ali O\yarm_miniscope_recording\m12lr\m12lr_3\2022_05_20_r2_dlc_ez_good_epa_bv\15_00_33\exported_python_analysis\05_20_2022___15_00_32\spikerate_05_20_2022___15_00_32.csv")
c_norm = pd.read_csv(r"C:\Users\LurLab\Downloads\c_norm_test.csv")
params = pd.read_csv(r"Z:\Ali O\yarm_miniscope_recording\m12lr\m12lr_3\2022_05_20_r2_dlc_ez_good_epa_bv\15_00_33\exported_python_analysis\05_20_2022___15_00_32\trial_parameters_05_20_2022___15_00_32.csv")
del c_norm[c_norm.columns[0]]
del calraw[calraw.columns[0]]
del spikes[spikes.columns[0]]

clean_df = params[params['clarity']=='clean']      

###del when not using all trials
#clean_df = params

#only mixstage
#if init_only == 1:
clean_df = clean_df[clean_df['mode']=='INIT']

clean_df = clean_df.reset_index(drop=True)
    
clean_trial_start_frames = []
clean_trial_stim_start_frames = []
clean_trial_end_frames = []
clean_trial_turn_frames = []
clean_trial_correctness = []
clean_trial_direction = []
for i in range(len(clean_df)):
  clean_trial_stim_start_frames.append(int(clean_df['stim_start'].iloc[i])) ###      2
  clean_trial_end_frames.append(int(clean_df['trial_end'].iloc[i]))
  clean_trial_turn_frames.append(int(clean_df['turn_frame'].iloc[i]))          #######       3
  clean_trial_start_frames.append(int(clean_df['trial_start'].iloc[i]))
  
#%%
cal_smooth = calraw
# get df/f
for i in range(len(cal_smooth.columns)):
  f0 = np.percentile(cal_smooth.iloc[:,0], [10]) #10th percentile
  cal_smooth.iloc[:,i] = (cal_smooth.iloc[:,i] - f0) / f0

# z score cal
from scipy.stats import zscore
cal_smooth = cal_smooth.apply(zscore)
calraw = calraw.apply(zscore)

# Apply a 30-row moving average to each column, excluding NaN values
#cal_smooth = cal_smooth.apply(lambda x: x.rolling(window=30, min_periods=1).mean())
window_size = 10
cal_smooth = cal_smooth.apply(lambda x: x.rolling(window=2 * window_size + 1, center=True, min_periods=1).mean())

#%%
calraw = calraw/calraw.max()
#c_norm = c_norm/c_norm.max()
cal_smooth = cal_smooth/cal_smooth.max()


plt.plot(calraw.iloc[:,2])
plt.plot(cal_smooth.iloc[:,2])

#%%
#plt.plot(calraw.iloc[:,2])

#plt.plot(spikes.iloc[:,2])

#plt.plot(c_norm.iloc[:,2])
#plt.plot(c_norm.iloc[:,4])

plt.plot(calraw.iloc[:,2:5])


for i in clean_trial_stim_start_frames:
    plt.axvline(x = i, color = 'g', label = 'axvline - full height')
    
for i in clean_trial_turn_frames:
    plt.axvline(x = i, color = 'orange', label = 'axvline - full height')
    
for i in clean_trial_end_frames:
    plt.axvline(x = i, color = 'r', label = 'axvline - full height')







#%%

#spike = pd.read_csv(r"Z:\Ali O\yarm_miniscope_recording\m12lr\m12lr_3\2022_05_20_r2_dlc_ez_good_epa_bv\15_00_33\exported_python_analysis\05_20_2022___15_00_32\spikerate_05_20_2022___15_00_32.csv")
#cal = pd.read_csv(r"Z:\Ali O\yarm_miniscope_recording\m12lr\m12lr_3\2022_05_20_r2_dlc_ez_good_epa_bv\15_00_33\exported_python_analysis\05_20_2022___15_00_32\calcium_raw_05_20_2022___15_00_32.csv")
c_norm = pd.read_csv(r"C:\Users\LurLab\Downloads\c_norm_test.csv")
#c = pd.read_csv(r"C:\Users\LurLab\Downloads\c_test.csv")

#del cal[cal.columns[0]]
#del spike[spike.columns[0]]
del c_norm[c_norm.columns[0]]
#del c[c.columns[0]]


#plt.plot(cal)


#plt.plot(cal.iloc[16087:16103,3])
#plt.plot(spike.iloc[16087:16103,3])


#for i in range(len(cal.columns)):
#    plt.plot(spike.iloc[16087:16103,i])

#plt.plot(cal.iloc[:,2])
#plt.plot(spike.iloc[:,0])

plt.plot(c_norm.iloc[:,2])



#cal=(cal-cal.min())/(cal.max()-cal.min())
#c_norm=(c_norm-c_norm.min())/(c_norm.max()-c_norm.min())

#cal = cal/cal.max()
#c_norm = c_norm/c_norm.max()

#spike=(spike-spike.min())/(spike.max()-spike.min())

#%%
params = pd.read_csv(r"Z:\Ali O\yarm_miniscope_recording\m12lr\m12lr_3\2022_05_18_r2_dlc_ez_good_epa_bv\13_28_33\exported_python_analysis\05_18_2022___13_28_32\trial_parameters_05_18_2022___13_28_32.csv")

clean_df = params[params['clarity']=='clean']
clean_df = clean_df[clean_df['mode']=='INIT']
# for i in range(len(clean_df)):

trial_lengths = clean_df['turn_frame'] - clean_df['stim_start']

plt.hist(trial_lengths)