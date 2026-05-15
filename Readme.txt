Steps to setup and run VIC and VIC-Res:

####################### rainfall-runoff #######################
---------------------------------------------------------------
1) The 'input' folder contains the climate forcings that will go to the rainfall-runoff model. In each input file, the rows represent the days (1/1/1994 to 31/12/2022), and four columns represent the data corresponding to precipitation (mm), maximum temperature (°C), minimum temperature (°C), and wind speed (m/sec). 

2) The 'output' folder (../rainfall_runoff/output) will store your simulated hydrological fluxes (runoff, evapotranspiration, soil moisture, and others).

3) The 'model' folder should contain the source code for the VIC model, version 4.x, which can be downloaded from https://vic.readthedocs.io/en/master/. Make sure you have already installed the dependent compilers (C and Fortran) to build the 'make' file (../rainfall_runoff/model).

4) Edit and save the 'globalparam.txt' file in 'parameter' folder (../rainfall_runoff/parameters), indicating the path to the desired supporting files (soil and vegetation) and the run period.

5) Go to ../rainfall_runoff/model and run the rainfall-runoff model:
a) make clean
b) make
c) ./vicNl -g ../parameter/globalparam.txt

6) Run the routing model once the rainfall-runoff model run is completed.

####################### routing #######################
----------------------------------------------------------------------- 
1) The outputs of the rainfall-runoff model will be the inputs for routing. There is no need to create 'input' folder for routing. 

2) Edit and save the 'configuration.txt' file (../routing/parameters), indicating the path to the desired supporting files (reservoir, flow direction, station to route) and the run period.

3) The 'model' folder (../routing/model) contains the source code for the VIC-Res model, which can be downloaded from https://github.com/Critical-Infrastructure-Systems-Lab/VICRes. Note that the VIC-Res model includes several options for representing reservoirs. In this specific implementation, we use a mix of Option 2 (Predifined target reservoir level) and Option 6 (Predefined reservoir volume time series data). Additional details are provided on the GitHub repo.

4) Go to ../routing/model and run the routing model:
a) make clean
b) make
c) ./rout ../parameters/configuration.txt

5) The final output files will be saved in ../routing/output

