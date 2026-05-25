# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:47:17 2024

@author: Phearom
"""

# =============================================================================
# For MERRA2 and IMERG data extraction for VIC
# =============================================================================

import xarray as xr
import pandas as pd
import os

# File paths
coordinates_file = "grids_mekong.txt" # Input the text file containing coordinates
data_folder = r""       # Input the folder containing MERRA2 and IMERG data
output_folder = r""     # Input the output folder

os.makedirs(output_folder, exist_ok=True)

# Read coordinates from the text file
coords = pd.read_csv(coordinates_file, delim_whitespace=True, header=None, names=["index", "lat", "lon"])


# Function to extract data
"""
NOTE: This fuction works for the data that were already processed in daily resolution and grouped for every year
e.g, 2001_imerg_prcp.nc4 contains daily rainfall data for 2001
Change this function to tailor to the data format
"""

def extract_yearly_data(year, lat, lon):
    rainfall = []
    tmax = []
    tmin = []
    wspd = []
    
    try:
        # Extracting precipitation
        prcp_file = os.path.join(data_folder, f"{year}_imerg_prcp.nc4")
        if os.path.exists(prcp_file):
            ds_prcp = xr.open_dataset(prcp_file)
            prcp_data = ds_prcp['daily_precipitation'].sel(lat=lat, lon=lon, method='nearest').values
            rainfall = prcp_data.tolist()
        else:
            print(f"Precipitation file not found for year {year}: {prcp_file}")
            
        # Extracting temperature
        temp_file = os.path.join(data_folder, f"{year}_merra2_temp.nc4")
        if os.path.exists(temp_file):
            ds_temp = xr.open_dataset(temp_file)
            tmax_data = ds_temp['T2MMAX'].sel(lat=lat, lon=lon, method='nearest').values
            tmin_data = ds_temp['T2MMIN'].sel(lat=lat, lon=lon, method='nearest').values
            tmax = tmax_data.tolist()
            tmin = tmin_data.tolist()
        else:
            print(f"Temperature file not found for year {year}: {temp_file}")
        
        # Extracting wind speed
        wspd_file = os.path.join(data_folder, f"{year}_merra2_wspd.nc4")
        if os.path.exists(wspd_file):
            ds_wspd = xr.open_dataset(wspd_file)
            wspd_data = ds_wspd['daily_avg_wind_speed'].sel(lat=lat, lon=lon, method='nearest').values
            wspd = wspd_data.tolist()
        else:
            print(f"Wind Speed file not found for year {year}: {wspd_file}")

    except Exception as e:
        print(f"Error extracting data for year {year}, lat {lat}, lon {lon}: {e}")
    
    return rainfall, tmax, tmin, wspd

# Iterate over each coordinate
for _, row in coords.iterrows():
    lat, lon = row["lat"], row["lon"]
    lat_str = f"{lat:.4f}"
    lon_str = f"{lon:.4f}"
    
    output_file = os.path.join(output_folder, f"data_{lat_str}_{lon_str}")
    
    with open(output_file, 'w') as outfile:
        for year in range(1994, 2023):  # Iterates from 1994 to 2022
            rainfall, tmax, tmin, wspd = extract_yearly_data(year, lat, lon)
            
            # Determine the number of records to write based on available data
            num_records = max(len(rainfall), len(tmax), len(tmin), len(wspd))
            
            for i in range(num_records):
                # Handle cases where some data might be missing
                prcp = rainfall[i] if i < len(rainfall) else float('nan')
                Tmax = tmax[i] if i < len(tmax) else float('nan')
                Tmin = tmin[i] if i < len(tmin) else float('nan')
                Wspd = wspd[i] if i < len(wspd) else float('nan')
                
                outfile.write(f"{prcp:.3f} {Tmax:.3f} {Tmin:.3f} {Wspd:.5f}\n")