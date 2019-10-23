from pqsp.pqsp_single_dose_simulations import SingleDose
from pqsp.pqsp_multi_dose_simulations import MultipleDose
from pqsp.pqsp_multi_dose_delay_simulations import MultipleDoseDelay

import matplotlib.pyplot as plt


def my_model(y, t, ka, F, K12, K21, K13, K31, K):

    G=y[0]; A1 = y[1]; A2 = y[2]; A3 = y[3]

    dGdt = -ka*G
    dA1dt = F*ka*G + (K21*A2 - K12*A1) + (K31*A3 - K13*A1) - K * A1
    dA2dt = K12*A1 - K21*A2
    dA3dt = K13*A1 - K31*A3

    return [dGdt, dA1dt, dA2dt, dA3dt]


def model_parameters():

    ka = 1.8; F = 0.89
    K12 = 0.7; K21 = 0.3
    K13 = 0.01; K31 = 0.002

    K = 0.28  # Cl / Vc

    par = (ka, F, K12, K21, K13, K31, K)

    return par


ka = 1.8; F = 0.89; K12 = 0.7; K21 = 0.3
K13 = 0.01; K31 = 0.002

K = 0.28  # Cl / Vc

npar = [ka, F, K12, K21, K13, K31, K]


def model_oce_c(y, t, K):

    A1 = y[0]

    dA1dt = - K * A1

    return [dA1dt]

#############################


mymodel = SingleDose(model_oce_c, [0.5], number_of_compartments=1)
t0, C0 = mymodel.simulation(simulation_time=3, time_unit='days', dose_mg=[100], compartment_pos=[0])
mymodel.plot_simulation(t0, C0, show_max=True)
mymodel.single_dose_plot(simulation_time=3, time_unit='days', drug_doses=[100, 400, 800], compartment_pos=[0])
mymodel.model_properties(t0, C0)
#
#
# #############################
#

mymultimodel = MultipleDose(my_model, npar, number_of_compartments=4, number_of_dose=3, interval=24)
time, conc = mymultimodel.simulation(simulation_time=3, time_unit='days', dose_mg=[100, 100, 100], compartment_pos=[1])
mymultimodel.plot_simulation(time, conc, show_max=True, show_auc=True)
mymultimodel.multi_dose_plot(simulation_time=3, time_unit='days', drug_doses=[100, 400, 800], compartment_pos=range(4))

####

mymodel_3 = MultipleDoseDelay(my_model, npar, number_of_compartments=4, number_of_dose=3, interval=24, delay=[10, 0])
time, conc = mymodel_3.simulation(simulation_time=3, time_unit='days', dose_mg=[100, 150, 100], compartment_pos=[1])
mymodel_3.plot_simulation(time, conc, show_max=True, show_auc=True)
mymodel_3.multi_dose_delay_plot(simulation_time=3, time_unit='days', drug_doses=[100, 400, 800], compartment_pos=range(3))
