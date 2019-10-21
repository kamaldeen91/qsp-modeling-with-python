# qsp-modeling-with-python (pqsp) by Kamaldeen

pQSP is a quantitative systems biology and pharmacology modeling toolbox for Python. It provides and facilitate simulation and analyzing ODE models of drug pharmacological systems. The toolbox is developed in the Jaline lab at Northwestern University.

## Installation
To install the standard IDM malaria package, either clone this repository and run pip install -e /path/to/script/folder in the command line



## Getting started
pqsp can be used to simulate a compartment model for QSP for single dose; multiple dose; and multiple dose with delay and with varying bioavailability.

## Example
Consider the following system of ODE for QSP with oral administration
$k = v$

##### For single dose simulation

###### single_dose_simulation(num_comp, num_days: int, dose_mg, c)

num_comp = number of compartment; num_days = number of days to run the simulation; dose_mg = concentration of drug; c = compartment you would like to output (for instance, c = 1 will provide results for the second comparment). Python counts from 0...

##### For multiple dose simulation

###### multi_dose_simulation(num_comp, n_days: int, num_dose: int, interval, dose_mg, c)

num_dose = number of time to take, interval = time interval between drug intake 


##### For multiple dose with delay simulation

###### multi_dose_sim_delay(num_comp, n_days: int, num_dose: int, interval, dose_mg, delay, c):

delay = array of delay during drug intake.
