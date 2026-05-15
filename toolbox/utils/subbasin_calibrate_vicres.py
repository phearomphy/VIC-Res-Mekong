# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 17:40:35 2025

@author: Phearom
"""

import pandas as pd

# Define file paths
"""
file1 is excel file containing grid locations for each subbasin
file2 is soil file to be modified
change the example file paths accordingly
"""
file1 = "subbasin_calibrate.xlsx"
file2 = "/home/phearom/VIC-Res-Mekong/rainfall_runoff/parameters/soilparam.txt"
output_file = "/home/phearom/VIC-Res-Mekong/rainfall_runoff/parameters/soilparam_1.txt"

# Read sheets representing subbasins from the first file.
# Each sheet must have columns named 'lat' and 'lon'
df_chiangsaen = pd.read_excel(file1, sheet_name="CS")
df_luangprabang = pd.read_excel(file1, sheet_name="LP")
df_chiangkhan = pd.read_excel(file1, sheet_name="CK")
df_mukdahan = pd.read_excel(file1, sheet_name="MK")
df_khongchiam = pd.read_excel(file1, sheet_name="KC")
df_pakse = pd.read_excel(file1, sheet_name="PS")
df_stungtreng = pd.read_excel(file1, sheet_name="ST")

# Create coordinate tuples for lookup
chiangsaen_coords = set(zip(df_chiangsaen['lat'], df_chiangsaen['lon']))
luangprabang_coords = set(zip(df_luangprabang['lat'], df_luangprabang['lon']))
chiangkhan_coords = set(zip(df_chiangkhan['lat'], df_chiangkhan['lon']))
mukdahan_coords = set(zip(df_mukdahan['lat'], df_mukdahan['lon']))
khongchiam_coords = set(zip(df_khongchiam['lat'], df_khongchiam['lon']))
pakse_coords = set(zip(df_pakse['lat'], df_pakse['lon']))
stungtreng_coords = set(zip(df_stungtreng['lat'], df_stungtreng['lon']))

# Read the second file
df_soilpar = pd.read_csv(file2, sep='\t')

# Create boolean masks for df_soilpar
# In df_soilpar, the lat is in column index 2 and lon in column index 3.
chiangsaen_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in chiangsaen_coords, axis=1)
luangprabang_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in luangprabang_coords, axis=1)
chiangkhan_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in chiangkhan_coords, axis=1)
mukdahan_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in mukdahan_coords, axis=1)
khongchiam_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in khongchiam_coords, axis=1)
pakse_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in pakse_coords, axis=1)
stungtreng_mask = df_soilpar.apply(lambda row: (row[2], row[3]) in stungtreng_coords, axis=1)

# For overlapping coordinates
# chiangsaen
df_soilpar.loc[chiangsaen_mask, 4] = 0.4        #INFILT = 0.4 (config 30n18)
df_soilpar.loc[chiangsaen_mask, 5] = 0.9        #Ds = 0.9 (config 30n18)
df_soilpar.loc[chiangsaen_mask, 6] = 7.167      #Ds_MAX = 7.167 (config 30n18)
df_soilpar.loc[chiangsaen_mask, 7] = 1          #Ws = 1 (config 30n18)
df_soilpar.loc[chiangsaen_mask, 18] = 0.5       #DEPTH_1 = 0.3 (config 30n18)
df_soilpar.loc[chiangsaen_mask, 19] = 0.7       #DEPTH_2 = 0.7 (config 30n18)

# luangprabang
df_soilpar.loc[luangprabang_mask, 4] = 0.4       #INFILT = 0.4 (config 30n18)
df_soilpar.loc[luangprabang_mask, 5] = 0.9       #Ds = 0.9 (config 30n18)
df_soilpar.loc[luangprabang_mask, 6] = 7.167     #Ds_MAX = 7.167 (config 30n18)
df_soilpar.loc[luangprabang_mask, 7] = 1         #Ws = 1 (config 30n18)
df_soilpar.loc[luangprabang_mask, 18] = 0.5      #DEPTH_1 = 0.3 (config 30n18)
df_soilpar.loc[luangprabang_mask, 19] = 0.7      #DEPTH_2 = 0.7 (config 30n18)

# chiangkhan
df_soilpar.loc[chiangkhan_mask, 4] = 0.4        #INFILT = 0.4 (config 30n18)
df_soilpar.loc[chiangkhan_mask, 5] = 0.9        #Ds = 0.9 (config 30n18)
df_soilpar.loc[chiangkhan_mask, 6] = 7.167      #Ds_MAX = 7.167 (config 30n18)
df_soilpar.loc[chiangkhan_mask, 7] = 1          #Ws = 1 (config 30n18)
df_soilpar.loc[chiangkhan_mask, 18] = 0.5       #DEPTH_1 = 0.3 (config 30n18)
df_soilpar.loc[chiangkhan_mask, 19] = 0.7       #DEPTH_2 = 0.7 (config 30n18)

# mukdahan
df_soilpar.loc[mukdahan_mask, 4] = 0.5         #INFILT = 0.4 (config 30n18)
df_soilpar.loc[mukdahan_mask, 5] = 0.59        #Ds = 0.9 (config 30n18)
df_soilpar.loc[mukdahan_mask, 6] = 7           #Ds_MAX = 10 (config 30n18)
df_soilpar.loc[mukdahan_mask, 7] = 0.60        #Ws = 0.6 (config 30n18)
df_soilpar.loc[mukdahan_mask, 18] = 0.1        #DEPTH_1 = 0.2 (config 30n18)
df_soilpar.loc[mukdahan_mask, 19] = 1.2        #DEPTH_2 = 0.8 (config 30n18)

# khongchiam
df_soilpar.loc[khongchiam_mask, 4] = 0.4       #INFILT = 0.4 (config 30n18)
df_soilpar.loc[khongchiam_mask, 5] = 0.3       #Ds = 0.9 (config 30n18)
df_soilpar.loc[khongchiam_mask, 6] = 10        #Ds_MAX = 10 (config 30n18)
df_soilpar.loc[khongchiam_mask, 7] = 0.6       #Ws = 0.6 (config 30n18)
df_soilpar.loc[khongchiam_mask, 18] = 0.3      #DEPTH_1 = 0.3 (config 30n18)
df_soilpar.loc[khongchiam_mask, 19] = 0.7      #DEPTH_2 = 0.7 (config 30n18)

# pakse
df_soilpar.loc[pakse_mask, 4] = 0.6        #INFILT = 0.6 (config 30n18)
df_soilpar.loc[pakse_mask, 5] = 0.9        #Ds = 0.9 (config 30n18)
df_soilpar.loc[pakse_mask, 6] = 2          #Ds_MAX = 2 (config 30n18)
df_soilpar.loc[pakse_mask, 7] = 0.8        #Ws = 0.8 (config 30n18)
df_soilpar.loc[pakse_mask, 18] = 1         #DEPTH_1 = 1 (config 30n18)
df_soilpar.loc[pakse_mask, 19] = 2         #DEPTH_2 = 2 (config 30n18)

# stungtreng
# df_soilpar.loc[stungtreng_mask, 4] = 0.6          #INFILT = 0.6 (config 30n18)
# df_soilpar.loc[stungtreng_mask, 5] = 0.9          #Ds = 0.9 (config 30n18)
# df_soilpar.loc[stungtreng_mask, 6] = 2            #Ds_MAX = 2 (config 30n18)
# df_soilpar.loc[stungtreng_mask, 7] = 0.8          #Ws = 0.8 (config 30n18)
# df_soilpar.loc[stungtreng_mask, 18] = 0.8         #DEPTH_1 = 0.8 (config 30n18)
# df_soilpar.loc[stungtreng_mask, 19] = 2           #DEPTH_2 = 2 (config 30n18)


# Save the updated dataframe as a new Excel file.
df_soilpar.to_csv(output_file, sep='\t',index=False, header=True)

print("Updated file saved as:", output_file)
