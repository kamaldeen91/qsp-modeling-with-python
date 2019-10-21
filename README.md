# qsp-modeling-with-python (pqsp) by Kamaldeen

pqsp ia aPython object oriented programming software used for simulating and analyzing models of quantitative systems biology and pharmacology. It facilitates the simulation and visualization of ODE models for QSP. The toolbox is developed in the Jaline lab at Northwestern University.

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
# Although model above is a two-compartmental pk model, the number of compartment defined in the simulation is the number of ODE equations defined in the model

time, conc = model_sd.simulation(simulation_time=2, time_unit='days', dose_mg=[100], compartment_pos=[1])
# This line simulate the model at initial drug concentration of 100 mg for 2 days 
# The result output is for the second compartment - compartment_pos=[1]: remember Python counts from 0
# This simulation also be written as - model_sd.simulation(simulation_time=24, time_unit='hrs', dose_mg=[100], compartment_pos=[1])
# i.e., for 24 hrs
    
mymodel.plot_simulation(time, conc, show_max=True, show_auc=True)
# This line plots the simulation output from previous command line and will show (if = True) the Cmax (and tmax) and the AUC
# Note that one could easily plot the time vs conc using different plot function

mymodel.single_dose_plot(simulation_time=20, time_unit='hrs', drug_doses=[100, 400, 800], compartment_pos=[0, 1, 2], figsize=(16,8))
# This line code allow for plotting the model for different initial doses and for different compartments of the model

mymodel.model_properties(time, conc)
# This line output the Cmax and corresponding Tmax of the model
```

### For Multiple dose simulation

```Python
mymultimodel = MultipleDose(my_model, parameters, number_of_compartments=3, number_of_dose=3, interval=24)

time_1, conc_1 = mymultimodel.simulation(simulation_time=5, time_unit='days', dose_mg=[100], compartment_pos=[2])
# dose_mg = [100, 100, 100}
# This allow for possible change in dose during therapy, for instance dose_mg = [100, 75, 100]
# It also for checking impact of incomplete dose, for instance dose_mg = [100, 0, 100]

mymultimodel.plot_simulation(time_1, conc_1, show_max=True, show_auc=True)

mymultimodel.multi_dose_plot(simulation_time=100, time_unit='hrs', drug_doses=[100, 400, 800],compartment_pos=range(3),figsize=(14,9))
```

### For Multiple dose with delay simulation
In addition to checking the effect of incomplete dose, pqsp can be used to check the effect of delay in drug dose
num_dose = number of time to take, interval = time interval between drug intake 

```Python
mydelaymodel = MultipleDoseDelay(my_model, parameters, number_of_compartments=3, number_of_dose=4, interval=24, 
                              delay=[5, 2, 0])

time_2, conc_2 = mydelaymodel.simulation(simulation_time=5, time_unit='days', dose_mg=[150], compartment_pos=[1])
# Try the command line below to combine delay with incomplete dose                               
# time, conc = mydelaymodel.simulation(simulation_time=10, time_unit='days', dose_mg=[100, 150, 0, 100], compartment_pos=[1])

mydelaymodel.plot_simulation(time_3, conc_3, show_max=True, show_auc=True)

mydelaymodel.multi_dose_delay_plot(simulation_time=5,time_unit='days',drug_doses=[100, 400, 800],compartment_pos=range(3),figsize=(16,12))
```
##### For multiple dose with delay simulation

###### multi_dose_sim_delay(num_comp, n_days: int, num_dose: int, interval, dose_mg, delay, c):

delay = array of delay during drug intake.
