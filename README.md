# qsp-modeling-with-python (pqsp) by Kamaldeen
Python codes to facilitate quantitative system pharmacology (QSP) modeling.
(Please see below to code-manual to read about me)

### See details below for step by step running of the codes

PS: Very little comments are provided in the codes and that is the reseaon I have (1) explain each folder and .py files here (2) attached a pdf file indicating the same thing: pqsp-CodeManual (3) made a short introductory video of the code - . 

For more details on QSP pharmacokinetic-pharmacodynamic (PK/PD) modeling (history, formulation and analytic solutions), see 
(1)
(2)
(3)

### General overview - pqsp-CodeMaunal

To run a pharmacokinetic model of your choice, go to the folder PharmacokineticModeling and provide the ODE model formulation and parameter values using the format provided in 
##### pk_model_and_par.py

Notice that the model function (def my_model) and the parameter values is named (def model_parameters). Do not change this as the model and paraemeters are called in 
##### pk_model_simulation.py -- where all model analysis is carried out.

In ## pk_model_simulation.py, the model you have provided can be simulated for single dose (def single_dose_simulation), multiple dose (def multi_dose_simulation) and multiple dose with delay (def multi_dose_sim_delay) - nice!

###### For single dose simulation, the function require

def single_dose_simulation(num_comp, n_days: int, dose_mg, c: int = 1)

num_comp = number of compartment, n_days = number of days to run the simulation, dose_mg = concentration of drug; c = compartment you would like to output (for instance, c = 1 by default will provide simulations for the central comparment)

###### For multiple dose simulation, the function require in addition to above

def multi_dose_simulation(num_comp, n_days: int, num_dose: int, interval, dose_mg, c: int = 1)

num_dose = amount of time to take of dose, interval = time interval between drug intake 

For instance num_dose = multi_dose_simulation(3, 7, 3, 24, 100, 1) will simulate the 3 system of ODE model (with parameters provided in #pk_model_and_par.py) for 7 days for drug of 100mg/l taken 3 times every 24 hours - and provide an output for the central compartment (c = 1)

###### For multiple dose simulation, the function require in addition to above

multi_dose_sim_delay(num_comp, n_days: int, num_dose: int, interval, dose_mg, delay, c: int = 1):
  

#### To execute or display the simulation
run_example.py execute the code.

I have included the default one-and two-compartment models with simulations that will require only the model parameter inputs.

These models also use the simulation time and simulation plots mentioned above.

#### pqsp One-compartment model

#### pqsp Two-compartment model
Same as above but with the equation given by



### About me

Kamaldeen is an applied mathematician by training and he has a profound interest in quantitative pharmacology research. Specifically, he is interested in designing, analyzing and simulating PK/PD models to help inform pre-clinical development of drugs.

##### Kamaldeen:
PK/PD modeling is interesting and I have enjoyed it so far. I enrolled in the HMX Fundamentals program (Harvard Medical School online learning platform) for pharmacology and immunology to improve my knowledge of basic pharmacology, necessary to design PK/PD models.

I look forward to a career as a QSP modeler and expert in a pharmaceutical research industry (and maybe in the near future - in an academic environment as I love to teach).

I have spent time and enjoyed reading qsp-related articles, especially, to update myself on qsp modeling tools. Most notable qsp modeling tools include R, NONNEM, Phoenix Winnonlin by , SymBiology - Matlab. 

While several articles have used these tools to analyze and characterize different drugs and dosage regimens, some researchers have carried out survey on the usage and user experience of these tools - this I found very thoughful of the authors as well as important for the progress of qsp modeling.

I will not be discussing about the result of the survey, but instead to highlight the fact that no Python-driven qsp code was included in the survey, despite in the increasing popularity of Python for simulations.

This is not to say that these tools are not efficient as I have only used SymBiology, but most importantly, I want to contribute to the available modling tools, to use Python to develop, analyze and simulate qsp models.
