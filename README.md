# qsp-modeling-with-python (pqsp) by Kamaldeen

pQSP is a quantitative systems biology and pharmacology modeling toolbox for Python. It provides and facilitate simulation and analyzing ODE models of drug pharmacological systems. The toolbox is developed in the Jaline lab at Northwestern University.

## Installation
To install the pqsp package, either clone this repository and run **pip install -e /path/to/script/folder in the command line** Allowing users to run code in different folder and using preferred IDE. :+1:



## Getting started
pqsp can be used to simulate a compartment model for QSP for single dose; multiple dose; and multiple dose with delay and with varying bioavailability. In the preferred IDE, use the following command lines to import required functions and pacakages:
``` Python
import pqsp

from pqsp.pqsp_single_dose_simulations import SingleDose  # for simulation and plots of model with single dose
from pqsp.pqsp_multi_dose_simulations import MultipleDose  # for simulation and plots of model with multiple dose
from pqsp.pqsp_multi_dose_delay_simulations import MultipleDoseDelay  # for simulation and plots of model with multiple dose with delay

from pqsp.pqsp_multi_bioav import MultipleDoseVaryBioav  # for simulation and plots of model with varying bioavailability
from pqsp.pqsp_multi_bioav_delay import MultipleDoseVaryBioavDelay  # for simulation and plots of model with delay and varying bioavailability
```

## Example
Consider the following system of ODE for QSP with oral administration (this example is executed using both PyCharm, and Jupyter notebook)


##### For single dose simulation

###### single_dose_simulation(num_comp, num_days: int, dose_mg, c)

num_comp = number of compartment; num_days = number of days to run the simulation; dose_mg = concentration of drug; c = compartment you would like to output (for instance, c = 1 will provide results for the second comparment). Python counts from 0...

##### For multiple dose simulation

###### multi_dose_simulation(num_comp, n_days: int, num_dose: int, interval, dose_mg, c)

num_dose = number of time to take, interval = time interval between drug intake 


##### For multiple dose with delay simulation

###### multi_dose_sim_delay(num_comp, n_days: int, num_dose: int, interval, dose_mg, delay, c):

delay = array of delay during drug intake.
