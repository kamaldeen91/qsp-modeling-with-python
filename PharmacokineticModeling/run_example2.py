from PharmacokineticModeling.pk_model_simulations import single_dose_simulation, multi_dose_simulation, \
    multi_dose_sim_delay

from ModelPlots.plot_simulations_with_AUC import plot_multi_dose_output, plot_multi_dose_delay_output, \
    plot_single_dose_output
from PharmacokineticModeling.pk_model_and_par import my_model, model_parameters

num_comp = 3

###

num_days = 3
num_dose = 3

interval = 12

delay = [4, 0]

dose_mg = [100,100,100]
comp = range(num_comp)

ka = 1.8; F = 0.89
K12 = 0.7; K21 = 0.3


K = 0.28
par = (ka, F, K12, K21, K)

t0, C0 = single_dose_simulation(my_model, par, num_comp, num_days, 'days', dose_mg, [2])
#
plot_single_dose_output(t0, C0, (12,6), 'concentration', 'ng/ml', show_auc = True, auc_start = 0, auc_end = 'inf', show_max = False)
# single_dose_plot(my_model, par, num_comp, dose_mg,  num_days, 'days', comp)
#
# ###
#
t1, C1 = multi_dose_simulation(my_model, par, num_comp, num_days, 'days', num_dose, interval, dose_mg, [1])
plot_multi_dose_output(t1, C1, num_dose, interval, (10, 6), 'concentration', 'ng/mL', show_auc = True, show_max = True, auc_start = 10, auc_end = 'inf')
# # #
# # #
t2, C2 = multi_dose_sim_delay(my_model, model_parameters, num_comp, num_days, 'days', num_dose, interval, dose_mg, delay, [1])
plot_multi_dose_delay_output(t2, C2, num_dose, interval, delay, (10, 6), 'concentration', 'ng/mL', show_auc=True,
                           show_max = True, auc_start = 10, auc_end = 'inf')
