# QSP-modeling-with-python (:pill:pqsp) by Kamaldeen

:pill:pqsp is a Python object oriented programming software used for simulating, analyzing and visualizing models of quantitative systems biology and pharmacology.

The toolbox is developed by Kamaldeen :soccer: - a postdoctoral researcher in the Jaline lab at Northwestern University.

## Installation
This software works with Python 3.7 and previous versions (and not Python 3.8 as scikit-learn tends not to work with the new 3.8 version). In addition ensure the following prerequisite packages - numpy, pandas, scipy and scikit-learn, are installed.
> Prerequisite - Python 3.7 (or previous release), numpy, pandas, scipy and scikit-learn

#### Windows
**Clone** or **download** this repository and install the pqsp package using:
`pip install -e /path/to/script/folder`
in the command line OR navigate to the folder path in the command window and install pqsp using: `python setup.py install`

#### Mac OS
Navigate to the folder path in the terminal window and install pqsp using: `python setup.py install`

:+1:

## Getting started
pqsp can be used to simulate a compartment model for QSP for ***single dose; multiple dose; and multiple dose with delay and with varying bioavailability***. In the preferred IDE, use the following command lines to import required functions and pacakages:
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
parameters = [ka, F, K, K12, K21]  # in the same order as defined in my_model
``` 

### For single dose simulation :pill:.

```Python
mysinglemodel = SingleDose(my_model, parameters, number_of_compartments=3)  
# Although model above is a two-compartmental pk model, the number of compartment defined in the simulation is the number of ODE equations defined in the model

time, conc = mysinglemodel.simulation(simulation_time=2, time_unit='days', dose_mg=[100], compartment_pos=[1])
# This code simulate the model at initial drug concentration of 100 mg for 2 days 
# The result output is for the second compartment - compartment_pos=[1]: remember Python counts from 0
# This simulation also be written as - model_sd.simulation(simulation_time=24, time_unit='hrs', dose_mg=[100], compartment_pos=[1])
# i.e., for 24 hrs
    
mysinglemodel.plot_simulation(time, conc, show_max=True, show_auc=True, auc_start=2, auc_end=30)
# This code plots the simulation output from previous command line and will show (if show_max = True) the Cmax (and corresponding tmax)
# This function will also show the AUC from auc_start to auc_end (auc_start = 0 and auc_start = 'inf' if not indicated)
# Note that one could easily plot the time vs conc using different plot function

mysinglemodel.single_dose_plot(simulation_time=20, time_unit='hrs', drug_doses=[100, 400, 800], compartment_pos=[0, 1, 2], figsize=(16,8))
# This code allow for plotting the model for different initial doses and for different compartments of the model

mysinglemodel.dose_auc_plot(simulation_time=3, time_unit='days', drug_doses=[100, 200, 300, 400, 500], compartment_pos=[1], auc_start=0, auc_end=30, figsize=(8,5))
# This code plot the dose vs AUC of the model for different doses and AUC region specified
# When auc_start and auc_end are not indicated, the plot show result for auc_start = 0 and auc_end = inf
```

### For multiple dose simulation :pill:.:pill:.:pill:.

```Python
mymultimodel = MultipleDose(my_model, parameters, number_of_compartments=3, number_of_dose=3, interval=24)

time_1, conc_1 = mymultimodel.simulation(simulation_time=5, time_unit='days', dose_mg=[100], compartment_pos=[2])
# dose_mg can also be given as: dose_mg = [100, 100, 100}
# This allow for possible change in dose during therapy, for instance dose_mg = [100, 75, 100]
# It also for checking impact of incomplete dose, for instance dose_mg = [100, 0, 100]

mymultimodel.plot_simulation(time_1, conc_1, show_max=True, show_auc=True)

mymultimodel.multi_dose_plot(simulation_time=100, time_unit='hrs', drug_doses=[100, 400, 800],compartment_pos=range(3),figsize=(14,9))

mymultimodel.dose_auc_plot(simulation_time=3, time_unit='days', drug_doses=[100, 400, 800], compartment_pos=[1])

```

### For multiple dose with delay simulation :pill: ... :pill: .. :pill:
In addition to checking the effect of incomplete dose as shown above, pqsp can be used to check the effect of ***delay in drug dose***

```Python
mydelaymodel = MultipleDoseDelay(my_model, parameters, number_of_compartments=3, number_of_dose=4, interval=24, 
                              delay=[5, 2, 0])
# Note that the number of entries in delay is one less than number of dose. This is because delay is expected to start only after the first dose is taken
time_2, conc_2 = mydelaymodel.simulation(simulation_time=5, time_unit='days', dose_mg=[150], compartment_pos=[1])
# Try the command line below to combine delay with incomplete dose                               
# time, conc = mydelaymodel.simulation(simulation_time=10, time_unit='days', dose_mg=[100, 150, 0, 100], compartment_pos=[1])

mydelaymodel.plot_simulation(time_3, conc_3, show_max=True, show_auc=True)

mydelaymodel.multi_dose_delay_plot(simulation_time=5,time_unit='days',drug_doses=[100, 400, 800],compartment_pos=range(3),figsize=(16,12))

mydelaymodel.dose_auc_plot(simulation_time=5, time_unit='days', drug_doses=[100,200, 300], compartment_pos=[1])
```

### For multiple dose with varying bioavailability
Consider the model and parameters below:
```Python
def two_c_model(y, t, ka, K, K12, K21, F):
    G = y[0]; A1 = y[1]; A2 = y[2]

    dGdt = -ka * G
    dA1dt = F * ka * G + K21 * A2 - K12 * A1 - K * A1
    dA2dt = K12 * A1 - K21 * A2

    return [dGdt, dA1dt, dA2dt]

ka = 0.17; Cl = 15.5; Vc = 368; Vd = 1060; Q = 16
K12 = Q / Vc; K21 = Q / Vd; K = Cl / Vc
par = [ka, K, K12, K21]
```
Observe that when defining **two_c_model** in this case, we ensured that F is listed as the last entry in the function.
Always ensure this when executing thr code for varied bioavailability!

The simulation of the model is given as follows

```Python
mymulti_biov = MultipleDoseVaryBioav(two_c_model, par, number_of_compartments=3, number_of_dose=4, interval=24, bioav=[1, 0.51, 0.41, 0.6])

time_3, conc_3 = mymulti_biov.simulation(simulation_time=8, time_unit='days', dose_mg=[100], compartment_pos=[1])

mymulti_biov.plot_simulation(time_3, conc_3, show_auc=True, show_max=True)

mymulti_biov.multi_dose_vary_bioav_plot(simulation_time=8, time_unit='days', drug_doses=[10,20,30], compartment_pos=[0,1,2], figsize=(12,8))
```

### For multiple dose with delay and varying bioavailability

```Python
mymulti_biov_delay = MultipleDoseVaryBioavDelay(two_c_model, par, number_of_compartments=3, number_of_dose=4, interval=24, delay=[6,3,0], bioav=[1, 0.7, 0.9, 0.4])

time_4, conc_4 = mymultimodel_delay.simulation(simulation_time=8, time_unit='days', dose_mg=[100])

mymulti_biov_delay.plot_simulation(time_4, conc_4, show_auc=True, show_max=True)

mymulti_biov_delay.md_delay_vary_bioav_plot(simulation_time=8, time_unit='days', drug_doses=[100, 200, 400], compartment_pos=[0,1,2], figsize=(12,8))
```

##

### Assignment :syringe:
1. Run a single and multiple does (with and without delay) simulations for an intravenous :syringe: model given by

```python
def intravenous_model(y, t, K, K12, K21):
    A1 = y[0]; A2 = y[1]

    dA1dt = - K12 * A1 - K * A1 + K21 * A2
    dA2dt = K12 * A1 - K21 * A2

    return [dA1dt, dA2dt]

Cl = 15.5; Vc = 368; Vd = 1060; Q = 16
K12 = Q / Vc; K21 = Q / Vd; K = Cl / Vc
parameters = [K, K12, K21]
```

2. Run a single, multiple does (with and without delay) simulations for any model of your choice.
