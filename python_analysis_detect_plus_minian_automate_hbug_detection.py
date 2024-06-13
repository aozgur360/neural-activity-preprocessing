### generate list of folders that need to be minchecked in matlab

import os
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
    for subfolder in subfolders:
         subfolders=getsubfolders(subfolder)
         for subfolder in subfolders:
             if "ignore" not in subfolder:
                 if "good" not in subfolder:
                     if "hbug" not in subfolder:
    #             if 'mcheck' not in subfolder:
                         basefolders.append(subfolder)
                         subfolders = getsubfolders(subfolder)
                         for subfolder in subfolders:
                             subfolders = getsubfolders(subfolder)
                             for subfolder in subfolders:
                                 if "My_V4_Miniscope" in subfolder:
                                     temp.append(subfolder)
                                 
#print(temp)
video_folders = {folder for folder in temp}
print(f"video_folders = {video_folders}")
 
#%%
### rename minchecked folders based on results
if len(temp) == len(basefolders):
    test_exist_good = []
    test_exist_hbug = []
    true_index_good = []
    true_index_hbug = []
    hbug_exist = []
    good_exist = []
    
    # for good files
    for i in temp:
        file_exists_good = os.path.exists(i+'/checked_good.txt')
        #just to get position of all files
        test_exist_good.append(file_exists_good)
        true_index_good = [i for i, x in enumerate(test_exist_good) if x]
        if file_exists_good == True:
            good_exist.append(i)
            
    for i in true_index_good:
        #print(basefolders[i]) 
        try:
            name = basefolders[i]
            os.rename(name,name+'_good')
        except:
            name = basefolders[i]
            print(name)
            continue
        
    # for hbug files
    for i in temp:
        file_exists_hbug = os.path.exists(i+'/checked_hbug.txt')
        #just to get position of all files
        test_exist_hbug.append(file_exists_hbug)
        true_index_hbug = [i for i, x in enumerate(test_exist_hbug) if x]
        if file_exists_hbug == True:
            hbug_exist.append(i)
            
    for i in true_index_hbug:
        #print(basefolders[i]) 
        try:
            name = basefolders[i]
            os.rename(name,name+'_hbug')
        except:
            name = basefolders[i]
            print(name)
            continue
else:
    print('error')
    
#%%
#### check and rename for blood vessels analysis

import os
def getsubfolders(folder):
    ''' returns list of subfolders '''
    return [os.path.join(folder,p) for p in os.listdir(folder) if os.path.isdir(os.path.join(folder,p))]

shuffle=1
basepath='Z:\Ali O\yarm_miniscope_recording'
basefolders = []
testfolders = []
subfolders=getsubfolders(basepath)
for subfolder in subfolders:
    subfolders=getsubfolders(subfolder)
    for subfolder in subfolders:
         subfolders=getsubfolders(subfolder)
         for subfolder in subfolders:
             basefolders.append(subfolder)
             subfolders = getsubfolders(subfolder)
             for subfolder in subfolders:
                 subfolders=getsubfolders(subfolder)
                 testfolders.append(subfolder)
                            
                 
                     
test_exist = []
true_index = []
for i in testfolders:
    file_exists = os.path.exists(i + '/rejected_cells.csv')
    test_exist.append(file_exists)
    true_index= [i for i, x in enumerate(test_exist) if x]
    
if len(test_exist) == len(basefolders):
    for i in true_index:
        #so that we don't keep renaming already finished files
        if "bv" not in basefolders[i]:
            try:
                name = basefolders[i]
                os.rename(name,name+'_bv')
            except:
                name = basefolders[i]
                print(name)
                continue
else:
    print('error')



#%%

### check and rename for exported python analysis

import os
def getsubfolders(folder):
    ''' returns list of subfolders '''
    return [os.path.join(folder,p) for p in os.listdir(folder) if os.path.isdir(os.path.join(folder,p))]

shuffle=1
basepath='Z:\Ali O\yarm_miniscope_recording'
basefolders = []
testfolders = []
subfolders=getsubfolders(basepath)
for subfolder in subfolders:
    subfolders=getsubfolders(subfolder)
    for subfolder in subfolders:
         subfolders=getsubfolders(subfolder)
         for subfolder in subfolders:
             basefolders.append(subfolder)
             subfolders = getsubfolders(subfolder)
             for subfolder in subfolders:
                 subfolders=getsubfolders(subfolder)
                 testfolders.append(subfolder)
                            
                 
                     
test_exist = []
true_index = []
for i in testfolders:
    file_exists = os.path.exists(i + '/exported_python_analysis')
    test_exist.append(file_exists)
    true_index= [i for i, x in enumerate(test_exist) if x]
    
if len(test_exist) == len(basefolders):
    for i in true_index:
        #so that we don't keep renaming already finished files
        if "epa" not in basefolders[i]:
            try:
                name = basefolders[i]
                os.rename(name,name+'_epa')
            except:
                name = basefolders[i]
                print(name)
                continue
else:
    print('error')

#%%
#### check that each basefolder has only 1 folder 

for i in basefolders:
    folder_count = 0
    input_path = i  # type: str
    for folders in os.listdir(input_path):
        folder_count += 1  # increment counter
        if folder_count > 1:
            print(i)
    
#    print("There are {0} folders".format(folder_count))






#%%
### get files to run in minian analysis

### generate list of folders that need to be minchecked in matlab (if yrA is not present and no hbug)

import os
def getsubfolders(folder):
    ''' returns list of subfolders '''
    return [os.path.join(folder,p) for p in os.listdir(folder) if os.path.isdir(os.path.join(folder,p))]

shuffle=1
temp = []
basepath='Z:\Ali O\yarm_miniscope_recording'
basefolders = []
subfolders=getsubfolders(basepath)
mice = ["m30lr","m31r","m32l","m33r",'m36rr','m37l','m38n','m39rr','m40l','m41r']


for subfolder in subfolders:
    subfolders=getsubfolders(subfolder)
    for mouse in mice:
        if mouse in subfolder:
            for subfolder in subfolders:
                 subfolders=getsubfolders(subfolder)
                 for subfolder in subfolders:
                         if "hbug" not in subfolder:
                             if"abug" not in subfolder:
                                 if "good" in subfolder:
                #             if 'mcheck' not in subfolder:
                                     basefolders.append(subfolder)
                                     subfolders = getsubfolders(subfolder)
                                     for subfolder in subfolders:
                                         subfolders = getsubfolders(subfolder)
                                         isExist = os.path.exists(subfolder + '/YrA.csv')
                                         if isExist:
                                             continue
                                         else:
                                             temp.append(subfolder)

print(temp)
