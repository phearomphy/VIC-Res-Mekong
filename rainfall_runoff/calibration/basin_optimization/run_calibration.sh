#!/bin/bash
#SBATCH --job-name=vicres             # Job name
#SBATCH --output=calibration_output.log        # Standard output and error log
#SBATCH --error=calibration_error.log          # Optional: separate error log
#SBATCH --ntasks=1                     # Number of tasks (1 for serial job)

# Load any necessary modules, if applicable


# Navigate to the directory where your VIC model and Calibration Scripts are
cd /home/fs01/spec1174/VICRes/Mekong/toolbox/calibration/

# Run the vic postprocessing script
module load python/3.11.5
python3 basin_calibration_eNSGAII.py
