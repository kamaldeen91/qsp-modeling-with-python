# qsp-modeling-with-python (pqsp) by Kamaldeen
Python codes to facilitate quantitative system pharmacology (QSP) modeling.
(Please see below to code-manual to read about me)

### See details below for step by step running of the codes

PS: Very little comments are provided in the codes and that is the reseaon I have (1) explain each folder and .py files here (2) attached a pdf file indicating the same thing: pqsp-CodeManual (3) made a short introductory video of the code - . 

### General overview - pqsp-CodeMaunal

To run a pharmacokinetic model of your choice, go to the folder PharmacokineticModeling and provide the ODE model formulation and parameter values using the format provided in

#### pk_model_and_par.py

Notice that the model function (def my_model) and the parameter values is named (def model_parameters). Do not change this as the model and paraemeters are called in

#### pk_model_simulation.py -- where all model analysis is carried out.

In pk_model_simulation.py, the model you have provided can be simulated for single dose (def single_dose_simulation), multiple dose (def multi_dose_simulation) and multiple dose with delay (def multi_dose_sim_delay) - nice!

##### For single dose simulation, the function require

def single_dose_simulation(num_comp, n_days: int, dose_mg, c: int = 1)

num_comp = number of compartment, n_days = number of days to run the simulation, dose_mg = concentration of drug; c = compartment you would like to output (for instance, c = 1 by default will provide simulations for the central comparment)

##### For multiple dose simulation, the function require in addition to above

def multi_dose_simulation(num_comp, n_days: int, num_dose: int, interval, dose_mg, c: int = 1)

num_dose = amount of time to take of dose, interval = time interval between drug intake 

For instance:

###### multi_dose_simulation(3, 7, 3, 24, 100, 1) 

will simulate the 3 system of ODE model (with parameters provided in #pk_model_and_par.py) for 7 days for drug of 100mg/l taken 3 times every 24 hours - and provide an output for the central compartment (c = 1)

##### For multiple dose with delay simulation, the function require in addition to above

multi_dose_sim_delay(num_comp, n_days: int, num_dose: int, interval, dose_mg, delay, c: int = 1):

delay = array of delay during drug intake.

For instance:

###### multi_dose_sim_delay(3, 7, 3, 24, 100, [5, 0], 1) 

will simulate similar scenario as above but with 5 hr delay in the intake of the second drug and no delay in intake of third (final) dose of a 3 dose regimen.


#### To execute/display the simulation

### Simulation plot - model_simulation_plots.py

This include 

###### single_dose_plot(drug_doses, num_comp, num_days, comp)

where drug_dose is an array of the drug dose(s) to be taken
num_comp, num_days are as defined above as number of model compartments and number days to run simulation,
comp = array of compartment to be plotted

For instance (as written in run_example1.py):

###### single_dose_plot([200, 400], 3, 10, [1,2,3])
will plot the 3 ODE models (defined in pk_model_and_par.py) for 10 days and plot the third and fourth compartments of the model for two drug dose 200mg/l and 400mg/l.

###### multi_dose_plot(drug_doses, num_comp, num_days, num_dose, interval, comp)
will plot the same compartments and doses for multiple drugs

###### multi_dose_with_delay_plot(drug_doses, num_comp, num_days, num_dose, interval, delay, comp)
will plot the same compartments and doses for multiple drugs with delay.


### Simulation plot with AUC - plot_simulations_with_AUC.py
This plot additional properties of the pharmacokinetics of the drug from the model simulation - see run_example2.py

t, C = single_dose_simulation(num_comp, num_days, dose_1)
plot_single_dose_output(t, C, (7, 5), 'ng/mL', 'central compartment', show_auc = True, tS=10, tC='inf', show_max = True)

t1, C1 = multi_dose_simulation(num_comp, num_days, num_dose, interval, [dose_1] * num_dose)
plot_multi_dose_output(t1, C1, num_dose, interval, (10, 6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')


### In-built one-and two-compartment models

I have also included one-and two-compartment pk models in the folders OneComparment and TwoComparment respectively.

These codes will require only the model parameter inputs which is given in one_comp_model_parameters.py and two_comp_model_parameters.py

run_example_1C.py and run_example_2C.py for examples.


### Simulation time - simulation_time.py
All the simulation uses simulation time that has been defined simulation_time.py which include

def time_for_single_dose for single dose simulation time

def time_for_multi_dose for multiple dose simulation time

and time_for_multi_dose_delay for multiple dose with delay simulation time



## About me

Kamaldeen is an applied mathematician by training and he has a profound interest in quantitative pharmacology research. Specifically, he is interested in designing, analyzing and simulating PK/PD models to help inform pre-clinical development of drugs.

##### Kamaldeen:
PK/PD modeling is interesting and I have enjoyed it so far. I enrolled in the HMX Fundamentals program (Harvard Medical School online learning platform) for pharmacology and immunology to improve my knowledge of basic pharmacology, necessary to design PK/PD models.

I look forward to a career as a QSP modeler and expert in a pharmaceutical research industry (and maybe in the near future - in an academic environment as I love to teach).

I have spent time and enjoyed reading qsp-related articles, especially, to update myself on qsp modeling tools. Most notable qsp modeling tools include R, NONNEM, Phoenix Winnonlin by , SymBiology - Matlab. 

While several articles have used these tools to analyze and characterize different drugs and dosage regimens, some researchers have carried out survey on the usage and user experience of these tools - this I found very thoughful of the authors as well as important for the progress of qsp modeling.

I will not be discussing about the result of the survey, but instead to highlight the fact that no Python-driven qsp code was included in the survey, despite in the increasing popularity of Python for simulations.

This is not to say that these tools are not efficient as I have only used SymBiology, but most importantly, I want to contribute to the available modling tools, to use Python to develop, analyze and simulate qsp models.
