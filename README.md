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
Consider the following system of ODE and parameters for QSP with oral administration
``` Python
def my_model(y, t, ka, F, K, K12, K21):

    G=y[0]; A1 = y[1]; A2 = y[2]; 

    dGdt = -ka*G
    dA1dt = F*ka*G + (K21*A2 - K12*A1) - K * A1
    dA2dt = K12*A1 - K21*A2

    return [dGdt, dA1dt, dA2dt]
    
ka = 1.8; K = 0.28; F = 0.89; K12 = 0.7; K21 = 0.3;
parameters = (ka, F, K, K12, K21)  # or parameters = [ka, F, K, K12, K21]
``` 

### For single dose simulation

```Python
model_sd = SingleDose(my_model, parameters, number_of_compartments=3)  
# although model above is a two-compartmental pk model, the number of compartment defined in the simulation is the number of ODE equations defined in the model

time, conc = model_sd.simulation(simulation_time=2, time_unit='days', dose_mg=[100], compartment_pos=[1])
# This line simulate the model at initial drug concentration of 100 mg for 2 days 
# The result output is for the second compartment - compartment_pos=[1]: remember Python counts from 0
# This simulation also be written as - model_sd.simulation(simulation_time=24, time_unit='hrs', dose_mg=[100], compartment_pos=[1])
# i.e., for 24 hrs
    
mymodel.plot_simulation(time, conc, show_max=True, show_auc=True)
# This line plots the simulation output from previous command line

mymodel.single_dose_plot(simulation_time=20, time_unit='hrs', drug_doses=[100, 400, 800], compartment_pos=[0, 1, 2], figsize=(16,8))
# This line code allow for plotting the model for different initial doses and for different compartments of the model

mymodel.model_properties(time, conc)
# This line output the Cmax and corresponding Tmax of the model
```

###### single_dose_simulation(num_comp, num_days: int, dose_mg, c)

num_comp = number of compartment; num_days = number of days to run the simulation; dose_mg = concentration of drug; c = compartment you would like to output (for instance, c = 1 will provide results for the second comparment). Python counts from 0...

##### For multiple dose simulation

###### multi_dose_simulation(num_comp, n_days: int, num_dose: int, interval, dose_mg, c)

num_dose = number of time to take, interval = time interval between drug intake 


##### For multiple dose with delay simulation

###### multi_dose_sim_delay(num_comp, n_days: int, num_dose: int, interval, dose_mg, delay, c):

delay = array of delay during drug intake.
