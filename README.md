# qsp-modeling-with-python (pqsp) by Kamaldeen

pQSP is a quantitative systems biology and pharmacology modeling toolbox for Python. It provides and facilitate simulation and analyzing ODE models of drug pharmacological systems. The toolbox is developed in the Jaline lab at Northwestern University.

I have attached a pdf file indicating the same thing: pqsp-CodeManual; and made a short introductory video of the code -

## Installation
To install the standard IDM malaria package, either clone this repository and run pip install -e /path/to/script/folder in the command line



## Getting started



## Example

In pk_model_simulation.py, the model can be simulated for single dose (single_dose_simulation); multiple dose (multi_dose_simulation); and multiple dose with delay (multi_dose_sim_delay) - nice!

##### For single dose simulation

###### single_dose_simulation(num_comp, num_days: int, dose_mg, c)

num_comp = number of compartment; num_days = number of days to run the simulation; dose_mg = concentration of drug; c = compartment you would like to output (for instance, c = 1 will provide results for the second comparment). Python counts from 0...

##### For multiple dose simulation

###### multi_dose_simulation(num_comp, n_days: int, num_dose: int, interval, dose_mg, c)

num_dose = number of time to take, interval = time interval between drug intake 


##### For multiple dose with delay simulation

###### multi_dose_sim_delay(num_comp, n_days: int, num_dose: int, interval, dose_mg, delay, c):

delay = array of delay during drug intake.
