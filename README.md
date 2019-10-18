# qsp-modeling-with-python (pqsp) by Kamaldeen

pQSP is a quantitative systems biology and pharmacology modeling toolbox for Python. It provides and facilitate simulation and analyzing ODE models of drug pharmacological systems. The toolbox is developed in the Jaline lab at Northwestern University.

I have attached a pdf file indicating the same thing: pqsp-CodeManual; and made a short introductory video of the code -

## Installation




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

##

## About me

Kamaldeen is an applied mathematician by training and he has a profound interest in quantitative pharmacology research. Specifically, he is interested in designing, analyzing and simulating PK/PD models to help inform pre-clinical development of drugs.

##### Kamaldeen:
PK/PD modeling is interesting and I have enjoyed it so far. I enrolled in the HMX Fundamentals program (Harvard Medical School online learning platform) for pharmacology and immunology to improve my knowledge of basic pharmacology, necessary to design PK/PD models.

I look forward to a career as a QSP modeler and expert in a pharmaceutical research industry (and maybe in the near future - in an academic environment as I love to teach).

I have spent time and enjoyed reading qsp-related articles, especially, to update myself on qsp modeling tools. Most notable qsp modeling tools include R, NONNEM, Phoenix Winnonlin by , SymBiology - Matlab. 

While several articles have used these tools to analyze and characterize different drugs and dosage regimens, some researchers have carried out survey on the usage and user experience of these tools - this I found very thoughful of the authors as well as important for the progress of qsp modeling.

I will not be discussing about the result of the survey, but instead to highlight the fact that no Python-driven qsp code was included in the survey, despite in the increasing popularity of Python for simulations.

This is not to say that these tools are not efficient as I have only used SymBiology, but most importantly, I want to contribute to the available modling tools, to use Python to develop, analyze and simulate qsp models.
